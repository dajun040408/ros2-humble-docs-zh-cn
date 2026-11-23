.. redirect-from::

    Allocator-Template-Tutorial
    Tutorials/Allocator-Template-Tutorial

实现自定义内存分配器
====================

**目标：** 学习如何在 ROS 2 C++ 代码中使用自定义内存分配器。

**教程级别：** 高级 | **预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

本教程介绍如何为发布者和订阅者集成自定义分配器，使 ROS 节点执行期间不调用默认堆分配器。示例代码：§allocator_tutorial.cpp <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/demo_nodes_cpp/src/topics/allocator_tutorial.cpp>§_。

背景
----

实时安全代码通常需要避免在实时关键区间调用 §new§，因为大多数平台的默认堆分配器具有非确定性。

许多 C++ 标准库结构在增长时会隐式分配内存，例如 §std::vector§。这些数据结构支持 Allocator 模板参数，可以指定自定义分配器来代替系统分配器。自定义分配器可以使用预先分配的内存池，更适合实时应用。

ROS 2 C++ 客户端库 §rclcpp§ 遵循类似的设计理念。发布者、订阅者和执行器都接受分配器模板参数，用于控制相应实体执行期间的内存分配。

编写分配器
----------

要兼容 ROS 2 分配器接口，自定义分配器必须符合 C++ 标准库分配器接口。

C++11 提供 §allocator_traits§，它定义了标准分配器所需的最小接口，并根据这些接口补齐其他分配器属性。

例如，下面的自定义分配器声明可以满足 §allocator_traits§ 的基本要求（仍需实现相应函数）：

.. code-block:: cpp

   template <class T>
   struct custom_allocator {
     using value_type = T;
     custom_allocator() noexcept;
     template <class U>
     custom_allocator(const custom_allocator<U>&) noexcept;
     T* allocate(std::size_t n);
     void deallocate(T* p, std::size_t n);
   };

   template <class T, class U>
   constexpr bool operator==(
     const custom_allocator<T>&,
     const custom_allocator<U>&) noexcept;

   template <class T, class U>
   constexpr bool operator!=(
     const custom_allocator<T>&,
     const custom_allocator<U>&) noexcept;

之后可以通过 §std::allocator_traits<custom_allocator<T>>§ 访问 traits 提供的其他函数和成员，例如 §construct()§。

更多 §allocator_traits§ 信息请参阅§C++ 参考文档 <https://en.cppreference.com/w/cpp/memory/allocator_traits>§_。

在 rclcpp 中使用分配器
----------------------

§rclcpp§ 的发布者、订阅者和执行器都可以通过模板参数指定分配器。为发布消息时使用自定义分配器，需要保证消息内存、发布者内部内存和相关消息分配策略与目标实时约束一致。

使用自定义分配器并不自动保证整个节点实时安全。还需要检查回调、日志、容器扩容、锁和中间件实现是否会触发不可预测的分配或阻塞。

总结
----

自定义分配器可以控制 ROS 2 C++ 节点的内存分配行为，是构建实时系统的重要工具。应遵循 C++ Allocator 接口，并结合 rclcpp 发布者、订阅者和执行器的分配器模板参数使用。
