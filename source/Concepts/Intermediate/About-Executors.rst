.. redirect-from::

   Concepts/About-Executors

执行器（Executor）
==================

.. contents:: 目录
   :local:

概述
------

ROS 2 中的执行管理由执行器（Executor）负责。执行器使用底层操作系统的一个或多个线程，在收到消息或事件时调用订阅、定时器、服务端、动作服务端等实体的回调函数。

显式的 Executor 类（在 rclcpp 的 `executor.hpp <https://github.com/ros2/rclcpp/blob/{REPOS_FILE_BRANCH}/rclcpp/include/rclcpp/executor.hpp>`_、rclpy 的 ``executors.py <https://github.com/ros2/rclpy/blob/{REPOS_FILE_BRANCH}/rclpy/rclpy/executors.py>`_，或 rclc 的 ``executor.h <https://github.com/ros2/rclc/blob/master/rclc/include/rclc/executor.h>`_ 中）相比 ROS 1 的 spin 机制提供了更精细的执行管理控制，尽管两者的基础 API 非常相似。

下面主要介绍 C++ 客户端库 ``rclcpp``。

基本用法
----------

最简单的情况是：通过调用 ``rclcpp::spin(..)``，使用主线程处理节点收到的消息和事件：

.. code-block:: cpp

   int main(int argc, char* argv[])
   {
      // Some initialization.
      rclcpp::init(argc, argv);
      ...

      // Instantiate a node.
      rclcpp::Node::SharedPtr node = ...

      // Run the executor.
      rclcpp::spin(node);

      // Shutdown and exit.
      ...
      return 0;
   }

调用 ``spin(node)`` 本质上会实例化并调用单线程执行器（Single-Threaded Executor），这是最简单的一种执行器：

.. code-block:: cpp

   rclcpp::executors::SingleThreadedExecutor executor;
   executor.add_node(node);
   executor.spin();

调用执行器实例的 ``spin()`` 后，当前线程会开始查询 rcl 和中间件层，检查是否有新消息或其他事件，并调用相应的回调函数，直到节点关闭。

为了不抵消中间件 QoS 设置的作用，收到的消息不会先存储在客户端库层的队列中，而是保留在中间件中，直到回调函数取出并处理它。这一点与 ROS 1 有着关键区别。

执行器通过 *wait set（等待集）* 获取中间件层是否存在可用消息的信息。等待集中每个队列对应一个二进制标志。等待集还用于检测定时器是否到期。

.. image:: ../images/executors_basic_principle.png

单线程执行器也用于运行组件（:doc:`components <./About-Composition>`）的容器进程，也就是在没有显式 main 函数的情况下创建并执行节点的场景。

.. _TypesOfExecutors:

执行器类型
------------

目前，rclcpp 提供三种执行器类型，它们都继承自同一个父类：

.. graphviz::

   digraph Flatland {

      Executor -> SingleThreadedExecutor [dir = back, arrowtail = empty];
      Executor -> MultiThreadedExecutor [dir = back, arrowtail = empty];
      Executor -> StaticSingleThreadedExecutor [dir = back, arrowtail = empty];
      Executor  [shape=polygon,sides=4];
      SingleThreadedExecutor  [shape=polygon,sides=4];
      MultiThreadedExecutor  [shape=polygon,sides=4];
      StaticSingleThreadedExecutor  [shape=polygon,sides=4];

      }

*多线程执行器（Multi-Threaded Executor）* 会创建可配置数量的线程，从而允许并行处理多条消息或多个事件。

*静态单线程执行器（Static Single-Threaded Executor）* 用于优化扫描节点结构（例如订阅、定时器、服务端和动作服务端等）所产生的运行时开销。节点添加到执行器时，它只扫描一次节点结构；另外两种执行器则会定期扫描这些变化。因此，静态单线程执行器只应与在初始化期间就创建好所有订阅、定时器等实体的节点一起使用。

这三种执行器都可以通过对每个节点调用 ``add_node(..)`` 来管理多个节点。

.. code-block:: cpp

   rclcpp::Node::SharedPtr node1 = ...
   rclcpp::Node::SharedPtr node2 = ...
   rclcpp::Node::SharedPtr node3 = ...

   rclcpp::executors::StaticSingleThreadedExecutor executor;
   executor.add_node(node1);
   executor.add_node(node2);
   executor.add_node(node3);
   executor.spin();

在上面的示例中，静态单线程执行器的一个线程同时服务于三个节点。对于多线程执行器，实际并行程度取决于回调组的配置。

回调组
--------

ROS 2 允许将节点的回调函数组织到不同的组中。在 rclcpp 中，可以通过 Node 类的 ``create_callback_group`` 函数创建*回调组（callback group）*。在 rclpy 中，则通过调用特定回调组类型的构造函数来创建。

回调组必须在节点执行期间一直保存（例如作为类成员变量），否则执行器将无法触发其中的回调。创建订阅、定时器等实体时，可以指定所属回调组，例如通过订阅选项指定：

.. tabs::

   .. group-tab:: C++

      .. code-block:: cpp

        my_callback_group = create_callback_group(rclcpp::CallbackGroupType::MutuallyExclusive);

        rclcpp::SubscriptionOptions options;
        options.callback_group = my_callback_group;

        my_subscription = create_subscription<Int32>("/topic", rclcpp::SensorDataQoS(),
                                                     callback, options);
   .. group-tab:: Python

      .. code-block:: python

        my_callback_group = MutuallyExclusiveCallbackGroup()
        my_subscription = self.create_subscription(Int32, "/topic", self.callback, qos_profile=1,
                                                   callback_group=my_callback_group)

创建订阅、定时器等实体时，如果没有指定回调组，它们都会被分配到*默认回调组（default callback group）*。在 rclcpp 中，可以通过 ``NodeBaseInterface::get_default_callback_group()`` 查询默认回调组；在 rclpy 中，可以通过 ``Node.default_callback_group`` 查询。

回调组有两种类型，必须在实例化时指定：

* *互斥型（Mutually exclusive）：* 该组中的回调不能并行执行。
* *可重入型（Reentrant）：* 该组中的回调可以并行执行。

不同回调组中的回调始终可以并行执行。多线程执行器会将线程作为线程池使用，并根据上述条件尽可能并行地处理回调。

有关如何高效使用回调组的建议，请参阅 :doc:`使用回调组 <../../How-To-Guides/Using-callback-groups>`。

rclcpp 中的 Executor 基类还提供 ``add_callback_group(..)`` 函数，允许将不同回调组分配给不同执行器。通过操作系统调度器配置底层线程，可以让某些回调获得比其他回调更高的优先级。

例如，可以让控制循环中的订阅和定时器优先于节点中的其他订阅和普通服务。``examples_rclcpp_cbg_executor`` 软件包提供了这一机制的演示。

调度语义
----------

如果回调处理时间短于消息和事件的产生周期，执行器基本上会按照 FIFO（先进先出）顺序处理它们。

但是，如果某些回调的处理时间较长，消息和事件就会在软件栈的底层排队。等待集机制向执行器报告的队列信息非常有限，具体来说，它只会报告某个话题是否存在待处理消息。

执行器利用这些信息，以轮询（round-robin）的方式处理消息（包括服务和动作），但并不保证按照 FIFO 顺序处理。下图展示了这种调度语义。

.. image:: ../images/executors_scheduling_semantics.png

这种语义最早由 Casini 等人在 2019 年 ECRTS 会议的一篇 `论文 <https://drops.dagstuhl.de/opus/volltexte/2019/10743/pdf/LIPIcs-ECRTS-2019-6.pdf>`_ 中描述。

（注意：该论文还解释了定时器事件曾经比其他消息具有更高优先级。`这一优先级规则已在 Eloquent 中移除。 <https://github.com/ros2/rclcpp/pull/841>`_）

后续发展
----------

rclcpp 的三种执行器能够满足大多数应用的需求，但仍存在一些问题，使其不适用于实时应用。实时应用通常要求明确的执行时间、确定性，以及对执行顺序的自定义控制。主要问题如下：

1. 调度语义复杂且混合。理想情况下，需要定义明确的调度语义，以便进行形式化时序分析。
2. 回调可能发生优先级反转。低优先级回调可能阻塞高优先级回调。
3. 无法显式控制回调的执行顺序。
4. 不具备针对特定话题的内置触发控制机制。

此外，执行器在 CPU 和内存使用方面的开销也相当可观。静态单线程执行器能够显著降低这些开销，但对某些应用而言仍可能不够。

以下开发在一定程度上解决了这些问题：

* `rclcpp WaitSet <https://github.com/ros2/rclcpp/blob/{REPOS_FILE_BRANCH}/rclcpp/include/rclcpp/wait_set.hpp>`_：rclcpp 的 ``WaitSet`` 类允许直接等待订阅、定时器、服务端、动作服务端等实体，而不必使用执行器。它可以用于实现确定性的、由用户定义的处理顺序，也可以将来自不同订阅的多条消息组合起来处理。``examples_rclcpp_wait_set 软件包 <https://github.com/ros2/examples/tree/{REPOS_FILE_BRANCH}/rclcpp/wait_set>`_ 提供了多个用户级等待集机制的示例。
* `rclc Executor <https://github.com/ros2/rclc/blob/master/rclc/include/rclc/executor.h>`_：该执行器来自 C 客户端库 *rclc*，最初为 micro-ROS 开发。它允许用户精细控制回调执行顺序，并支持自定义触发条件来激活回调。此外，它还实现了逻辑执行时间（Logical Execution Time，LET）语义的相关思想。

更多信息
----------

* Michael Pöhnl 等：
  `ROS 2 Executor: How to make it efficient, real-time and deterministic? <https://www.apex.ai/roscon-21>`_。
  ROS World 2021 专题研讨会，线上活动，2021 年 10 月 19 日。
* Ralph Lange：
  `Advanced Execution Management with ROS 2 <https://www.youtube.com/watch?v=Sz-nllmtcc8&t=109s>`_。
  ROS Industrial Conference，线上活动，2020 年 12 月 16 日。
* Daniel Casini、Tobias Blass、Ingo Lütkebohle 和 Björn Brandenburg：
  `Response-Time Analysis of ROS 2 Processing Chains under Reservation-Based Scheduling <https://drops.dagstuhl.de/opus/volltexte/2019/10743/pdf/LIPIcs-ECRTS-2019-6.pdf>`_，发表于第 31 届 ECRTS 会议论文集，德国斯图加特，2019 年 7 月。
