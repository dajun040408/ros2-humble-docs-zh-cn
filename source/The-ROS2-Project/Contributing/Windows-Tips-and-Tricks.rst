.. redirect-from::

    Contributing/Windows-Tips-and-Tricks

Windows 开发技巧
================

.. contents:: 目录
   :depth: 2
   :local:

ROS 2 将 Windows 10 作为 Tier 1 支持平台，这意味着所有进入 ROS 2 核心的代码都必须支持 Windows。对于习惯在 Linux 或其他类 Unix 系统上开发的人员而言，在 Windows 上开发可能会遇到一些挑战。本文介绍其中的一些差异。

最大路径长度
------------

默认情况下，Windows 的`最大路径长度 <https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation>`_ 为 260 个字符。

其中通常有 4 个字符被盘符、冒号、初始反斜杠和末尾 NULL 字符占用，因此路径各部分的总长度实际上只有 256 个字符。

这会对 ROS 2 产生两个实际影响：

* ROS 2 内部的一些路径名称比较长。因此，始终建议为 ROS 2 目录根路径选择较短的名称，例如 ``C:\dev`` 。
* 从源码构建 ROS 2 时，colcon 默认的 isolated 构建模式可能生成很长的路径。为避免路径过长，在 Windows 上构建时请使用 ``--merge-install`` 。

**注意：** 可以修改 Windows 配置，以支持更长的最大路径。更多信息请参阅`此处 <https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=cmd#enable-long-paths-in-windows-10-version-1607-and-later>`_。

.. _Windows_Symbol_Visibility:

符号可见性
----------

Microsoft Visual C++ Compiler（MSVC）只会导出显式声明导出的动态链接库（DLL）符号。

Clang 和 GCC 也提供类似选项，但默认关闭。因此，当一个原本在 Linux 上构建的库移植到 Windows 后，其他库可能无法解析其外部符号。

以下是符号未正确导出时可能出现的常见错误：

.. code-block:: console

   error C2448: '__attribute__': function-style initializer appears to be a function definition
   'visibility': identifier not found

.. code-block:: console

   CMake Error at C:/ws_ros2/install/random_numbers/share/random_numbers/cmake/ament_cmake_export_libraries-extras.cmake:48 (message):
      Package 'random_numbers' exports the library 'random_numbers' which
      couldn't be found

符号可见性也会影响二进制加载。如果可组合节点无法运行，或者 Qt Visualizer 无法工作，可能是宿主进程无法找到预期的二进制符号导出。

在 Windows 上，可以使用 Windows 开发工具中的 Gflags 诊断此问题。Gflags 提供多种调试选项，其中之一是 *Loader Snaps*，可以在调试时检测加载失败。更多信息请参阅 Microsoft 文档：`Gflags <https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/setting-and-clearing-image-file-flags>`_ 和 `Loader Snaps <https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/show-loader-snaps>`_。

在 Windows 上导出符号有两种解决方案：Visibility Control Headers 和 ``WINDOWS_EXPORT_ALL_SYMBOLS`` 属性。

Microsoft 建议 ROS 开发者使用 Visibility Control Headers 控制二进制符号导出。它们可以更精细地控制符号导出宏，还能缩小二进制文件并减少链接时间。

Visibility Control Headers
^^^^^^^^^^^^^^^^^^^^^^^^^^

Visibility Control Headers 的作用是为每个共享库定义一个宏，正确声明符号应使用 ``dllimport`` 还是 ``dllexport`` 。具体取决于当前库是被其他代码使用，还是正在被自身构建。

宏中的逻辑还会考虑编译器类型，并选择合适的语法。`GCC visibility 文档 <https://gcc.gnu.org/wiki/Visibility>`_ 提供了逐步说明，帮助为库添加显式符号可见性。

可以在每个库的 ``include`` 目录中放置一个名为 ``visibility_control.h`` 的头文件。以下示例展示如何为名为 ``my_lib`` 的库添加可见性控制头文件，其中包含一个名为 ``example_class`` 的类。

在库的 include 目录中添加可见性头文件。使用库名称构造唯一的宏名称，以避免项目中的宏冲突。在其他库中，应将 ``MY_LIB`` 替换为对应库名称。

.. code-block:: c++

   #ifndef MY_LIB__VISIBILITY_CONTROL_H_
   #define MY_LIB__VISIBILITY_CONTROL_H_
   #if defined _WIN32 || defined __CYGWIN__
   #ifdef __GNUC__
      #define MY_LIB_EXPORT __attribute__ ((dllexport))
      #define MY_LIB_IMPORT __attribute__ ((dllimport))
   #else
      #define MY_LIB_EXPORT __declspec(dllexport)
      #define MY_LIB_IMPORT __declspec(dllimport)
   #endif
   #ifdef MY_LIB_BUILDING_LIBRARY
      #define MY_LIB_PUBLIC MY_LIB_EXPORT
   #else
      #define MY_LIB_PUBLIC MY_LIB_IMPORT
   #endif
   #define MY_LIB_PUBLIC_TYPE MY_LIB_PUBLIC
   #define MY_LIB_LOCAL
   #else
    // Linux visibility settings
   #define MY_LIB_PUBLIC_TYPE
   #endif
   #endif  // MY_LIB__VISIBILITY_CONTROL_H_

完整示例请参阅 `rviz_rendering <https://github.com/ros2/rviz/blob/ros2/rviz_rendering/include/rviz_rendering/visibility_control.hpp>`_。

使用该宏时，在需要对外可见的符号前添加 ``MY_LIB_PUBLIC`` 。例如：

.. code-block:: c++

   Class MY_LIB_PUBLIC example_class {}

   MY_LIB_PUBLIC void example_function (){}

为了在构建库时正确导出符号，需要在 ``CMakeLists.txt`` 中添加：

.. code-block:: cmake

  target_compile_definitions(${PROJECT_NAME}
    PRIVATE "MY_LIB_BUILDING_LIBRARY")

WINDOWS_EXPORT_ALL_SYMBOLS 目标属性
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CMake 在 Windows 上实现了 ``WINDOWS_EXPORT_ALL_SYMBOLS`` 属性，可以自动导出函数符号。详细工作原理请参阅`CMake 文档 <https://cmake.org/cmake/help/latest/prop_tgt/WINDOWS_EXPORT_ALL_SYMBOLS.html>`_。

可以在 CMakeLists 文件中添加以下内容启用该属性：

.. code-block:: cmake

   set_target_properties(${LIB_NAME} PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS TRUE)

如果一个 CMakeLists 文件中包含多个库，需要分别对每个库调用 ``set_target_properties`` 。

注意，Windows 二进制最多只能导出 65,536 个符号。如果导出的符号超过这一数量，就会出现错误，此时应使用 visibility_control 头文件。

该方法对全局数据符号存在例外。例如：

.. code-block:: c++

   class Example_class
   {
   public:
   static const int Global_data_num;

对于这类情况，必须显式应用 ``dllimport`` / ``dllexport`` 。可以使用 ``generate_export_header`` 实现，具体请参阅 `相关说明 <https://blog.kitware.com/create-dlls-on-windows-without-declspec-using-new-cmake-export-all-feature/>`__。

最后，导出符号的头文件必须至少被软件包中的一个 ``.cpp`` 文件包含，这样宏才会展开并写入最终二进制文件。否则，符号仍然无法被调用。

Debug 构建
----------

在 Windows 上使用 Debug 模式构建时，有几项重要变化。

首先，所有 DLL 名称都会自动添加 ``_d`` 后缀。例如，库名为 ``libfoo.dll`` 时，Debug 模式下会变为 ``libfoo_d.dll`` 。Windows 动态链接器也会查找这种形式的库，因此不会找到没有 ``_d`` 后缀的库。

此外，Windows 会在 Debug 模式下启用一系列编译时和运行时检查，其严格程度远高于 Release 构建。

因此，建议在许多 Pull Request 中运行 Windows Debug 构建和测试。

正斜杠与反斜杠
--------------

Windows 默认使用反斜杠（``\`` ）作为路径分隔符，这与 Linux 和 macOS 使用的正斜杠（``/`` ）不同。

大多数 Windows API 都能将两者作为路径分隔符处理，但并非所有 API 都支持。例如，``cmd.exe`` Shell 只有在使用反斜杠时才能进行 Tab 补全，不能使用正斜杠。

为了最大限度地兼容 Windows，应始终在 Windows 路径中使用反斜杠。

修补 vendor 软件包
------------------

在 ROS 2 中引入 vendor 软件包时，经常需要应用补丁来修复缺陷或添加功能。

常见方法是修改 ``ExternalProject_add`` 调用，添加 ``PATCH`` 命令并使用 ``patch`` 可执行程序。

遗憾的是，Chocolatey 提供的 ``patch`` 可执行程序需要管理员权限才能运行。解决方法是在应用外部项目补丁时使用 ``git apply`` 。

``git apply`` 也有自己的限制：它只有在 Git 仓库中才能正常工作。因此，外部项目应始终使用 ``GIT`` 方法获取源码，然后通过 ``PATCH_COMMAND`` 调用 ``git apply`` 。

下面是上述方法的使用示例：

.. code-block:: cmake

  ExternalProject_Add(mylibrary-${version}
    GIT_REPOSITORY https://github.com/lib/mylibrary.git
    GIT_TAG ${version}
    GIT_CONFIG advice.detachedHead=false
    # Suppress git update due to https://gitlab.kitware.com/cmake/cmake/-/issues/16419
    # See https://github.com/ament/uncrustify_vendor/pull/22 for details
    UPDATE_COMMAND ""
    TIMEOUT 600
    CMAKE_ARGS
      -DCMAKE_INSTALL_PREFIX=${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}_install
      ${extra_cmake_args}
      -Wno-dev
    PATCH_COMMAND
      ${CMAKE_COMMAND} -E chdir <SOURCE_DIR> git apply -p1 --ignore-space-change --whitespace=nowarn ${CMAKE_CURRENT_SOURCE_DIR}/install-patch.diff
  )

Windows 定时器较慢（以及整体性能问题）
--------------------------------------

总体而言，Windows 上运行的软件通常比 Linux 上慢。这是多种因素造成的，例如默认时间片（根据`文档 <https://docs.microsoft.com/en-us/windows/win32/procthread/multitasking>`_ 为每 20 ms）、运行中的防病毒和反恶意软件进程数量，以及后台进程数量。

因此，测试绝不应在 Windows 上依赖非常严格的时间要求。所有测试都应设置较宽松的超时时间，只要求事件最终发生。这也有助于避免 Linux 上的测试出现不稳定（flaky）现象。

Shell
-----

Windows 上主要有两种命令行 Shell：传统的 ``cmd.exe`` 和 PowerShell。

``cmd.exe`` 是最接近传统 DOS Shell 的命令行程序，但功能已经大幅增强。它完全基于文本，并且只识别 DOS/Windows ``batch`` 文件。

PowerShell 是较新的、基于对象的 Shell，也是 Microsoft 对大多数新应用推荐使用的 Shell。它使用 ``ps1`` 文件进行配置。

ROS 2 同时支持 ``cmd.exe`` 和 PowerShell，因此任何变更（尤其是 ``ament`` 或 ``colcon`` 等工具的变更）都应在这两种 Shell 中进行测试。
