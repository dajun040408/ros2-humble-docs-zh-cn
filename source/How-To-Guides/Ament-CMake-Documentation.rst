.. redirect-from::

  Guides/Ament-CMake-Documentation
  Tutorials/Ament-CMake-Documentation

ament_cmake 用户文档
====================

``ament_cmake`` 是 ROS 2 中基于 CMake 的功能包所使用的构建系统，尤其适用于大多数 C/C++ 项目。它由一组增强 CMake 并为功能包作者提供便利功能的脚本组成。使用 ament_cmake 前，建议先了解 ``CMake`` 基础知识。

.. contents:: 目录
   :depth: 2
   :local:

基础知识
--------

可以通过命令行 ``ros2 pkg create <package_name>`` 生成基本 CMake 项目。构建信息主要保存在同一目录中的 ``package.xml`` 和 ``CMakeLists.txt`` 两个文件中。

``package.xml`` 必须包含所有依赖项和必要元数据，使 colcon 能够确定功能包构建顺序、在 CI 中安装依赖项，并为 Bloom 发布提供信息。``CMakeLists.txt`` 则包含构建和打包可执行程序及库的命令。

基本项目结构
^^^^^^^^^^^^

ament 功能包的 ``CMakeLists.txt`` 基本结构如下：

.. code-block:: cmake

   cmake_minimum_required(VERSION 3.8)
   project(my_project)

   ament_package()

``project`` 的参数是功能包名称，必须与 ``package.xml`` 中的名称完全一致。

每个功能包必须且只能调用一次 ``ament_package()``。该调用会安装 ``package.xml``，在 ament 索引中注册功能包，并安装供其他功能包通过 ``find_package`` 查找的配置文件和 target 文件。

由于 ``ament_package()`` 会收集 ``CMakeLists.txt`` 中的大量信息，因此它应当是文件中的最后一个调用。

``ament_package()`` 可以接收额外参数：

* ``CONFIG_EXTRAS``：指定一组供下游功能包使用的 CMake 文件（``.cmake`` 或通过 ``configure_file()`` 展开的 ``.cmake.in`` 模板）。
* ``CONFIG_EXTRAS_POST``：与 ``CONFIG_EXTRAS`` 类似，但这些文件会在 ``ament_export_*`` 调用生成的文件之后加入。

也可以使用变量 ``${PROJECT_NAME}_CONFIG_EXTRAS`` 和 ``${PROJECT_NAME}_CONFIG_EXTRAS_POST`` 实现相同效果。配置文件的包含顺序依次为 ``CONFIG_EXTRAS``、``${PROJECT_NAME}_CONFIG_EXTRAS``、``${PROJECT_NAME}_CONFIG_EXTRAS_POST`` 和 ``CONFIG_EXTRAS_POST``。

编译器和链接器选项
^^^^^^^^^^^^^^^^^^

ROS 2 面向符合 C++17 和 C99 标准的编译器。未来可能采用更新标准，具体请参阅 ``REP 2000``。

通常会设置对应 CMake 标准：

.. code-block:: cmake

   if(NOT CMAKE_C_STANDARD)
     set(CMAKE_C_STANDARD 99)
   endif()
   if(NOT CMAKE_CXX_STANDARD)
     set(CMAKE_CXX_STANDARD 17)
   endif()

为了保持代码质量，应启用编译器警告并修复可疑代码。建议至少使用：

* Visual Studio：默认 ``W1`` 警告级别。
* GCC 和 Clang：推荐 ``-Wall -Wextra -Wpedantic``，并建议启用 ``-Wshadow``。

可以使用 ``add_compile_options`` 为所有 target 添加选项：

.. code-block:: cmake

   if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
     add_compile_options(-Wall -Wextra -Wpedantic)
   endif()

查找依赖项
^^^^^^^^^^

大多数 ament_cmake 项目依赖其他功能包。在 CMake 中通过 ``find_package`` 查找依赖。例如，依赖 ``rclcpp`` 时：

.. code-block:: cmake

   find_package(rclcpp REQUIRED)

应确保 ``package.xml`` 中也声明对应依赖，以便构建工具和 rosdep 能够正确解析。

目标、安装和导出
----------------

建议使用现代 CMake target，而不是全局目录变量。为库或可执行程序创建 target 后，通过 ``target_include_directories()``、``target_link_libraries()`` 和 ``target_compile_definitions()`` 管理各自的依赖。

使用 ``install()`` 将可执行程序、库、头文件和资源安装到正确目录。使用 ``ament_export_targets()``、``ament_export_dependencies()`` 等宏导出下游功能包需要的 target 和依赖。

测试和代码检查
--------------

在 ``BUILD_TESTING`` 条件中查找测试依赖并注册测试。常见做法是使用 ``ament_lint_auto`` 自动发现 lint 测试依赖：

.. code-block:: cmake

   if(BUILD_TESTING)
     find_package(ament_lint_auto REQUIRED)
     ament_lint_auto_find_test_dependencies()
   endif()

在 ``package.xml`` 中声明对应 ``test_depend``。

总结
----

本页介绍了 ament_cmake 的基本项目结构、``ament_package()``、编译器选项、依赖查找、target 安装和导出，以及测试集成。完整 API 及高级用法仍应以各 ament_cmake 子模块的文档为准。
