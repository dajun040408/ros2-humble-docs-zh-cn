.. redirect-from::

    Quality-Guide
    Contributing/Quality-Guide

质量指南：确保代码质量
======================

.. contents:: 目录
   :depth: 2
   :local:

本页介绍如何提高 ROS 2 功能包的软件质量，重点关注 :doc:`开发者指南 <Developer-Guide>` 中“质量实践”部分之外的具体领域。内容适用于 ROS 2 核心、应用和生态系统功能包，以及 C++ 和 Python 核心客户端库。

目标是通过设计和实现实践改善可靠性、安全性、可维护性和确定性等质量属性。

将静态代码分析集成到 ament 构建
-------------------------------

**背景：**

* 已经开发 C++ 生产代码。
* 已创建支持 ament 构建的 ROS 2 功能包。

**问题：**

* 功能包构建流程没有运行库级静态代码分析。
* 静态分析需要手动执行，容易在发布新版本前遗漏。

**解决方案：**

使用 ament 集成功能，将静态代码分析作为功能包构建流程的一部分。

在 ``CMakeLists.txt`` 中添加：

.. code-block:: cmake

   if(BUILD_TESTING)
     find_package(ament_lint_auto REQUIRED)
     ament_lint_auto_find_test_dependencies()
   endif()

在 ``package.xml`` 中添加测试依赖：

.. code-block:: xml

   <test_depend>ament_lint_auto</test_depend>
   <test_depend>ament_lint_common</test_depend>

``rclcpp`` 和 ``rclcpp_lifecycle`` 的 CMakeLists.txt 与 package.xml 可作为实现示例。

**结果：** ament 支持的静态分析工具会在构建过程中运行；ament 不支持的工具仍需单独执行。

通过代码注解进行静态线程安全分析
--------------------------------

**背景：**

* 正在开发或调试多线程 C++ 生产代码。
* 多个线程会访问共享数据。

**问题：** 数据竞争和死锁可能导致严重缺陷。

**解决方案：** 使用 Clang 的`线程安全分析 <https://clang.llvm.org/docs/ThreadSafetyAnalysis.html>`_，通过注解标记多线程代码。

启用线程安全分析
^^^^^^^^^^^^^^^^

线程安全分析需要代码注解，让编译器了解代码语义。注解本身是 Clang 专用属性，例如 `__attribute__(capability())``。ROS 2 在 ``rcpputils/thread_safety_annotations.hpp`` 中提供预处理器宏，使用其他编译器时这些宏会被移除。

Clang 文档指出，线程安全分析可以与任何线程库配合使用，但通常需要将线程 API 封装在带有适当注解的类和方法中。ROS 2 希望开发者直接使用 ``std::`` 线程原语，因此选择通过 LLVM ``libc++`` 提供的注解支持来分析标准库类型。

需要了解的 C++ 标准库包括：

* GNU ``libstdc++``：Linux 默认使用。
* LLVM ``libc++``（也称 ``libcxx``）：macOS 默认使用，可通过 ``-stdlib=libc++`` 指定。
* Windows C++ 标准库。

``libc++`` 为 ``std::mutex`` 和 ``std::lock_guard`` 实现添加了线程安全分析注解；GNU ``libstdc++`` 没有这些注解。因此，若要直接对 ``std::`` 类型执行线程安全分析，需要使用 ``libc++``。

编译器选项
^^^^^^^^^^

使用 Clang 时启用 ``-Wthread-safety``：

.. code-block:: cmake

   if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
     add_compile_options(-Wthread-safety)
   endif()

也可以仅对单个 target 启用：

.. code-block:: cmake

   target_compile_options(my_target PUBLIC -Wthread-safety)

为共享数据添加注解
^^^^^^^^^^^^^^^^^^

对受互斥锁保护的数据成员使用 ``RCPPUTILS_TSA_GUARDED_BY(mutex_name)``：

.. code-block:: cpp

   class Foo {
   public:
     void incr(int amount) {
       std::lock_guard<std::mutex> lock(mutex_);
       bar += amount;
     }

     int get() const {
       std::lock_guard<std::mutex> lock(mutex_);
       return bar;
     }

   private:
     mutable std::mutex mutex_;
     int bar RCPPUTILS_TSA_GUARDED_BY(mutex_) = 0;
   };

推荐将互斥锁设为类的私有成员，让数据结构自身负责数据安全。对于复杂访问模式，可以提供专用接口，而不是直接暴露受锁保护的数据。

动态分析
--------

静态分析无法发现所有数据竞争和死锁。可以使用 Clang ThreadSanitizer 对程序进行动态分析。

使用 Clang 编译和链接生产代码，并添加 ``-fsanitize=thread``。如需了解如何对特定函数或文件排除插桩，请参阅`ThreadSanitizer 文档 <https://clang.llvm.org/docs/ThreadSanitizer.html>`_。

动态分析有助于在开发、调试和测试阶段发现数据竞争，但插桩会增加运行开销和内存使用。ThreadSanitizer 仍有自身限制，结果应结合实际测试场景判断。

总结
----

本指南介绍了如何在 ament 构建中集成静态代码分析、使用 Clang 注解执行线程安全分析，以及通过 ThreadSanitizer 进行动态数据竞争检测。
