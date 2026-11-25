.. redirect-from::

    Allocator-Template-Tutorial
    Tutorials/Allocator-Template-Tutorial

实现自定义内存分配器
====================

**目标：** 学习如何在 ROS 2 C++ 代码中使用自定义内存分配器。

**教程级别：** 高级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

本教程介绍如何为发布者和订阅者集成自定义分配器，使 ROS 节点执行期间不调用默认堆分配器。示例代码可参阅 `allocator_tutorial.cpp <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/demo_nodes_cpp/src/topics/allocator_tutorial.cpp>`_。

背景
----

实时安全代码通常需要避免在实时关键区间调用 ``new``，因为大多数平台的默认堆分配器具有非确定性。

许多 C++ 标准库结构在增长时会隐式分配内存，例如 ``std::vector``。这些数据结构支持 Allocator 模板参数，可以指定自定义分配器来代替系统分配器。自定义分配器可以使用预先分配的内存池，更适合实时应用。

ROS 2 C++ 客户端库 ``rclcpp`` 遵循类似的设计理念。发布者、订阅者和执行器都接受分配器模板参数，用于控制相应实体执行期间的内存分配。

编写分配器
----------

要兼容 ROS 2 分配器接口，自定义分配器必须符合 C++ 标准库分配器接口。

C++11 提供了 ``allocator_traits``。C++11 标准规定，自定义分配器只需要满足一组最小要求，就可以通过标准方式分配和释放内存。``allocator_traits`` 是一个通用结构，会根据满足最小要求的分配器补齐其他属性和功能。

例如，下面的自定义分配器声明可以满足 ``allocator_traits`` 的基本要求（仍需实现相应函数）：

.. code-block:: c++

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

之后可以通过 ``std::allocator_traits<custom_allocator<T>>`` 访问 traits 提供的其他函数和成员，例如 ``construct()``。

更多 ``allocator_traits`` 信息请参阅 `C++ 参考文档 <https://en.cppreference.com/w/cpp/memory/allocator_traits>`_。

不过，部分仅支持不完整 C++11 特性的编译器（例如 GCC 4.8）仍然要求分配器实现大量样板代码，才能与 vector、string 等标准库结构配合使用，因为这些结构内部并未使用 ``allocator_traits``。

因此，如果使用的是仅部分支持 C++11 的编译器，分配器可能需要采用更完整的形式：

.. code-block:: c++

   template<typename T>
   struct pointer_traits {
     using reference = T &;
     using const_reference = const T &;
   };

   // 使用空特化，避免对 void 声明引用类型
   template<>
   struct pointer_traits<void> {
   };

   template<typename T = void>
   struct MyAllocator : public pointer_traits<T> {
   public:
     using value_type = T;
     using size_type = std::size_t;
     using pointer = T *;
     using const_pointer = const T *;
     using difference_type = typename std::pointer_traits<pointer>::difference_type;

     MyAllocator() noexcept;
     ~MyAllocator() noexcept;

     template<typename U>
     MyAllocator(const MyAllocator<U> &) noexcept;

     T * allocate(size_t size, const void * = 0);
     void deallocate(T * ptr, size_t size);

     template<typename U>
     struct rebind {
       typedef MyAllocator<U> other;
     };
   };

   template<typename T, typename U>
   constexpr bool operator==(
     const MyAllocator<T> &,
     const MyAllocator<U> &) noexcept;

   template<typename T, typename U>
   constexpr bool operator!=(
     const MyAllocator<T> &,
     const MyAllocator<U> &) noexcept;

编写示例 main 函数
------------------

编写有效的 C++ 分配器后，需要将其作为共享指针传递给发布者、订阅者和执行器。

.. code-block:: c++

   auto alloc = std::make_shared<MyAllocator<void>>();

   rclcpp::PublisherOptionsWithAllocator<MyAllocator<void>> publisher_options;
   publisher_options.allocator = alloc;

   auto publisher = node->create_publisher<std_msgs::msg::UInt32>(
     "allocator_tutorial", 10, publisher_options);

   rclcpp::SubscriptionOptionsWithAllocator<MyAllocator<void>> subscription_options;
   subscription_options.allocator = alloc;

   auto msg_mem_strat = std::make_shared<
     rclcpp::message_memory_strategy::MessageMemoryStrategy<
       std_msgs::msg::UInt32, MyAllocator<void>>>(alloc);

   auto subscriber = node->create_subscription<std_msgs::msg::UInt32>(
     "allocator_tutorial", 10, callback, subscription_options, msg_mem_strat);

   std::shared_ptr<rclcpp::memory_strategy::MemoryStrategy> memory_strategy =
     std::make_shared<AllocatorMemoryStrategy<MyAllocator<void>>>(alloc);

   rclcpp::ExecutorOptions options;
   options.memory_strategy = memory_strategy;
   rclcpp::executors::SingleThreadedExecutor executor(options);

还需要使用自定义分配器为执行路径中传递的所有消息分配内存：

.. code-block:: c++

   auto alloc = std::make_shared<MyAllocator<void>>();

实例化节点并将执行器添加到节点后，就可以开始循环执行：

.. code-block:: c++

   uint32_t i = 0;
   while (rclcpp::ok()) {
     msg->data = i;
     i++;
     publisher->publish(msg);
     rclcpp::sleep_for(std::chrono::milliseconds(1));
     executor.spin_some();
   }

为进程内通信管线传递分配器
--------------------------

虽然前面在同一个进程中实例化了发布者和订阅者，但还没有使用进程内通信管线（intra-process pipeline）。

``IntraProcessManager`` 是一个通常对用户隐藏的类。为了向其传递自定义分配器，需要从 ``rclcpp Context`` 中获取该对象。

``IntraProcessManager`` 使用了多个标准库数据结构，因此如果没有自定义分配器，仍然会调用默认的 ``new``。

.. code-block:: c++

   auto context = rclcpp::contexts::get_global_default_context();
   auto options = rclcpp::NodeOptions()
     .context(context)
     .use_intra_process_comms(true);
   auto node = rclcpp::Node::make_shared("allocator_example", options);

注意：必须先按照这种方式构造节点，然后再实例化发布者和订阅者。

测试和验证代码
--------------

如何确认自定义分配器确实被调用了？

最直接的方法是在自定义分配器的 ``allocate`` 和 ``deallocate`` 函数中记录调用次数，并将其与 ``new`` 和 ``delete`` 的调用次数进行比较。

在自定义分配器中添加计数功能非常简单：

.. code-block:: c++

   T * allocate(size_t size, const void * = 0) {
     // ...
     num_allocs++;
     // ...
   }

   void deallocate(T * ptr, size_t size) {
     // ...
     num_deallocs++;
     // ...
   }

还可以重载全局 ``new`` 和 ``delete`` 运算符：

.. code-block:: c++

   void operator delete(void * ptr) noexcept {
     if (ptr != nullptr) {
       if (is_running) {
         global_runtime_deallocs++;
       }
       std::free(ptr);
       ptr = nullptr;
     }
   }

   void operator delete(void * ptr, size_t) noexcept {
     if (ptr != nullptr) {
       if (is_running) {
         global_runtime_deallocs++;
       }
       std::free(ptr);
       ptr = nullptr;
     }
   }

这里递增的变量只是全局静态整数，而 ``is_running`` 是一个全局静态布尔值，在调用 ``spin`` 前切换为 true。

示例可执行程序会打印这些变量的值。运行示例：

.. code-block:: console

   $ ros2 run demo_nodes_cpp allocator_tutorial

或者，启用进程内通信管线运行：

.. code-block:: console

   $ ros2 run demo_nodes_cpp allocator_tutorial intra
   Global new was called 15590 times during spin
   Global delete was called 15590 times during spin
   Allocator new was called 27284 times during spin
   Allocator delete was called 27281 times during spin

可以看到，执行路径中大约有三分之二的内存分配和释放操作被自定义分配器捕获。那么剩下的三分之一来自哪里？

实际上，这些分配和释放操作来自本示例底层使用的 DDS 实现。

证明这一点超出了本教程范围。不过，可以查看 ROS 2 持续集成测试中运行的内存分配路径测试。该测试会沿调用栈回溯，判断某些函数调用来自 RMW 实现还是 DDS 实现：

`TLSF 内存分配路径测试 <https://github.com/ros2/realtime_support/blob/{REPOS_FILE_BRANCH}/tlsf_cpp/test/test_tlsf.cpp#L41>`_。

注意：该测试没有使用本教程创建的自定义分配器，而是使用 TLSF 分配器（下文介绍）。

TLSF 分配器
-----------

ROS 2 支持 TLSF（Two Level Segregate Fit，双层分离适配）分配器，该分配器专门针对实时要求设计。

项目地址：`tlsf_cpp <https://github.com/ros2/realtime_support/tree/{REPOS_FILE_BRANCH}/tlsf_cpp>`_。

有关 TLSF 的更多信息，请参阅 `瓦伦西亚理工大学的 TLSF 介绍 <http://www.gii.upv.es/tlsf/>`_。

注意：TLSF 分配器采用 GPL/LGPL 双重许可证。

使用 TLSF 分配器的完整示例：`allocator_example.cpp <https://github.com/ros2/realtime_support/blob/{REPOS_FILE_BRANCH}/tlsf_cpp/example/allocator_example.cpp>`_。
