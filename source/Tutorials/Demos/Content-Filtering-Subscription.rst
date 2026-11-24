.. redirect-from::

    Content-Filtering-Subscription
    Tutorials/Content-Filtering-Subscription

创建内容过滤订阅
================

**目标：** 创建内容过滤订阅。

**教程级别：** 高级

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 1
   :local:

概述
----

ROS 2 应用通常通过话题将发布者的数据传递给订阅者。通常，订阅者会接收发布者在话题上发布的所有数据。但有时订阅者只对其中一部分数据感兴趣。内容过滤订阅允许应用程序只接收自己需要的数据。

本演示将介绍如何创建内容过滤订阅，以及它的工作方式。

RMW 支持情况
------------

内容过滤订阅需要 RMW 实现提供支持。

.. list-table:: 内容过滤订阅支持状态
   :widths: 25 25

   * - RMW 实现
     - 支持状态
   * - rmw_fastrtps
     - 支持
   * - rmw_connextdds
     - 支持
   * - rmw_cyclonedds
     - 不支持
   * - rmw_zenoh_cpp
     - 不支持

目前，支持内容过滤订阅的 RMW 实现都基于 DDS。这意味着支持的过滤表达式和参数也取决于 DDS。详细信息请参阅 DDS 规范中的 Annex B - Syntax for Queries and Filters：https://www.omg.org/spec/DDS/1.4/PDF。

安装演示程序
------------

有关安装 ROS 2 的详情，请参阅 :doc:`安装说明 <../../Installation>`。

如果通过软件包安装 ROS 2，请确保安装了 ros-{DISTRO}-demo-nodes-cpp。如果下载了归档包或从源码构建 ROS 2，该演示程序已经包含在安装内容中。

温度过滤演示
------------

本演示展示如何使用内容过滤订阅，只接收超出可接受温度范围的温度值，以便检测紧急情况。内容过滤订阅会过滤掉不感兴趣的温度数据，因此不会触发订阅回调。

发布者节点 ContentFilteringPublisher 的源码位于：
https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/demo_nodes_cpp/src/topics/content_filtering_publisher.cpp

该节点每秒发布一次模拟温度数据，温度从 -100.0 开始，以 10.0 为步长递增，到 150.0 后重新开始。

先 source 环境设置文件，然后运行发布者：

.. code-block:: console

    $ ros2 run demo_nodes_cpp content_filtering_publisher

订阅者节点 ContentFilteringSubscriber 的源码位于：
https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/demo_nodes_cpp/src/topics/content_filtering_subscriber.cpp

订阅者通过 SubscriptionOptions 设置过滤表达式和表达式参数。它只接收温度低于 -30.0 或高于 100.0 的消息。应用程序还可以通过 is_cft_enabled 方法检查订阅是否实际启用了内容过滤。

过滤表达式如下：

.. code-block:: cpp

    sub_options.content_filter_options.filter_expression = "data < %0 OR data > %1";
    sub_options.content_filter_options.expression_parameters = {
      std::to_string(-30.0f),
      std::to_string(100.0f)
    };

运行订阅者：

.. code-block:: console

    $ ros2 run demo_nodes_cpp content_filtering_subscriber

你应该看到订阅者输出已使用的内容过滤选项，并且只在温度低于 -30.0 或高于 100.0 时输出收到的消息。

内容过滤订阅是否可用取决于 RMW 实现。应用程序可以使用 is_cft_enabled 方法检查订阅是否真正启用了该功能。

如果底层 RMW 不支持内容过滤，订阅仍会创建，但不会启用过滤。可以使用 Cyclone DDS 验证这一点：

.. code-block:: console

    $ RMW_IMPLEMENTATION=rmw_cyclonedds_cpp ros2 run demo_nodes_cpp content_filtering_subscriber

此时会看到 Content filter is not enabled since it is not supported 警告，但演示仍会成功创建普通订阅并接收所有温度数据。

相关内容
--------

* 内容过滤示例：https://github.com/ros2/examples/blob/{REPOS_FILE_BRANCH}/rclcpp/topics/minimal_subscriber/content_filtering.cpp，涵盖内容过滤订阅的所有接口。
* 内容过滤设计 PR：https://github.com/ros2/design/pull/282
