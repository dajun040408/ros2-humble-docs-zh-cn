.. redirect-from::

    Topic-Statistics-Tutorial
    Tutorials/Topics/Topic-Statistics-Tutorial

启用话题统计信息（C++）
=======================

**目标：** 启用 ROS 2 话题统计功能，并查看发布的统计数据。

**教程级别：** 高级

**预计时间：** 10 分钟

.. contents:: 目录
   :local:

背景
----

本教程介绍如何在 ROS 2 中启用话题统计，并使用命令行工具查看发布的统计输出。相关工具请参阅 :doc:`ros2 topic <../../Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics>`。

ROS 2 提供对订阅者接收消息统计信息的集成测量功能，称为 Topic Statistics（话题统计）。启用订阅者的话题统计后，可以分析系统性能，或使用统计数据帮助诊断当前存在的问题。

更多详情请参阅 :doc:`话题统计概念页面 <../../../Concepts/Intermediate/About-Topic-Statistics>`。

前置条件
--------

需要安装 ROS 2（二进制或源码均可）。

此前的教程已经介绍了如何 :doc:`创建工作空间 <../../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace>`、:doc:`创建功能包 <../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>`，以及创建 :doc:`C++ 发布者和订阅者 <../../Beginner-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber>`。

本教程假设仍然保留此前创建的 ``cpp_pubsub`` 功能包。

任务
----

1. 编写启用统计功能的订阅者节点
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

进入此前教程创建的 ``ros2_ws/src/cpp_pubsub/src`` 目录，并下载示例订阅者代码：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ wget -O member_function_with_topic_statistics.cpp https://raw.githubusercontent.com/ros2/examples/{REPOS_FILE_BRANCH}/rclcpp/topics/minimal_subscriber/member_function_with_topic_statistics.cpp

   .. group-tab:: macOS

      .. code-block:: console

         $ wget -O member_function_with_topic_statistics.cpp https://raw.githubusercontent.com/ros2/examples/{REPOS_FILE_BRANCH}/rclcpp/topics/minimal_subscriber/member_function_with_topic_statistics.cpp

   .. group-tab:: Windows

      右键点击以下链接并选择“另存为”，文件名设为 ``member_function_with_topic_statistics.cpp``：

      https://raw.githubusercontent.com/ros2/examples/{REPOS_FILE_BRANCH}/rclcpp/topics/minimal_subscriber/member_function_with_topic_statistics.cpp

现在会出现 ``member_function_with_topic_statistics.cpp`` 文件。使用文本编辑器打开该文件。

.. code-block:: c++

   #include <chrono>
   #include <memory>

   #include "rclcpp/rclcpp.hpp"
   #include "rclcpp/subscription_options.hpp"
   #include "std_msgs/msg/string.hpp"

   class MinimalSubscriberWithTopicStatistics : public rclcpp::Node
   {
   public:
     MinimalSubscriberWithTopicStatistics()
     : Node("minimal_subscriber_with_topic_statistics")
     {
       // 通过订阅选项手动启用话题统计
       auto options = rclcpp::SubscriptionOptions();
       options.topic_stats_options.state = rclcpp::TopicStatisticsState::Enable;

       // 配置统计收集窗口和发布周期（默认 1 秒）
       options.topic_stats_options.publish_period = std::chrono::seconds(10);

       // 配置统计话题名称（默认 /statistics）
       // options.topic_stats_options.publish_topic = "/topic_statistics";

       auto callback = [this](const std_msgs::msg::String & msg) {
         this->topic_callback(msg);
       };

       subscription_ = this->create_subscription<std_msgs::msg::String>(
         "topic", 10, callback, options);
     }

   private:
     void topic_callback(const std_msgs::msg::String & msg) const
     {
       RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg.data.c_str());
     }

     rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
   };

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<MinimalSubscriberWithTopicStatistics>());
     rclcpp::shutdown();
     return 0;
   }

.. include:: ../../../_internal/Rclcpp-Convenience-Header-Note.rst

1.1 理解代码
~~~~~~~~~~~~

与 :doc:`C++ 发布者和订阅者教程 <../../Beginner-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber>` 一样，这里创建了一个订阅者节点，通过 ``topic_callback`` 函数接收 ``topic`` 话题上的字符串消息。

不同之处在于，我们增加了订阅选项结构体 ``rclcpp::SubscriptionOptions``，用来启用话题统计：

.. code-block:: c++

   // 通过订阅选项手动启用话题统计
   auto options = rclcpp::SubscriptionOptions();
   options.topic_stats_options.state = rclcpp::TopicStatisticsState::Enable;

还可以选择配置统计数据的收集/发布周期，以及发布统计数据所使用的话题名称：

.. code-block:: c++

   // 配置统计收集窗口和发布周期（默认 1 秒）
   options.topic_stats_options.publish_period = std::chrono::seconds(10);

   // 配置统计话题名称（默认 /statistics）
   // options.topic_stats_options.publish_topic = "/my_topic";

可配置字段如下：

.. list-table:: 订阅选项中的话题统计配置
   :header-rows: 1
   :widths: 35 65

   * - 配置字段
     - 用途
   * - ``topic_stats_options.state``
     - 启用或禁用话题统计，默认值为 ``rclcpp::TopicStatisticsState::Disable``。
   * - ``topic_stats_options.publish_period``
     - 收集统计数据并发布统计消息的周期，默认值为 ``1s``。
   * - ``topic_stats_options.publish_topic``
     - 发布统计数据的话题，默认值为 ``/statistics``。

1.2 修改 CMakeLists.txt
~~~~~~~~~~~~~~~~~~~~~~~

打开 ``CMakeLists.txt``，添加可执行程序，并命名为 ``listener_with_topic_statistics``，这样就可以通过 ``ros2 run`` 运行该节点：

.. code-block:: cmake

   add_executable(listener_with_topic_statistics src/member_function_with_topic_statistics.cpp)
   ament_target_dependencies(listener_with_topic_statistics rclcpp std_msgs)

   install(TARGETS
     talker
     listener
     listener_with_topic_statistics
     DESTINATION lib/${PROJECT_NAME})

保存文件。启用了话题统计的发布/订阅系统现在已经可以构建和运行。

2. 构建并运行
^^^^^^^^^^^^^

构建方法可参阅发布/订阅教程中的 :ref:`构建并运行 <cpppubsub-build-and-run>` 部分。

运行启用了统计功能的订阅者节点：

.. code-block:: console

   $ ros2 run cpp_pubsub listener_with_topic_statistics

然后运行 talker 发布者节点：

.. code-block:: console

   $ ros2 run cpp_pubsub talker
   [INFO] [minimal_publisher]: Publishing: "Hello World: 0"
   [INFO] [minimal_publisher]: Publishing: "Hello World: 1"
   [INFO] [minimal_publisher]: Publishing: "Hello World: 2"
   [INFO] [minimal_publisher]: Publishing: "Hello World: 3"
   [INFO] [minimal_publisher]: Publishing: "Hello World: 4"

订阅者会从发布者当前的消息计数开始接收消息，并在终端中输出类似信息：

.. code-block:: console

   [INFO] [minimal_subscriber_with_topic_statistics]: I heard: "Hello World: 10"
   [INFO] [minimal_subscriber_with_topic_statistics]: I heard: "Hello World: 11"
   [INFO] [minimal_subscriber_with_topic_statistics]: I heard: "Hello World: 12"
   [INFO] [minimal_subscriber_with_topic_statistics]: I heard: "Hello World: 13"
   [INFO] [minimal_subscriber_with_topic_statistics]: I heard: "Hello World: 14"

现在订阅者节点已经开始接收消息，并会周期性地发布统计消息。下一节将查看这些消息。

3. 查看发布的统计数据
^^^^^^^^^^^^^^^^^^^^^

在节点运行期间，打开一个新的终端窗口。执行以下命令，列出当前所有活动话题：

.. code-block:: console

   $ ros2 topic list
   /parameter_events
   /rosout
   /statistics
   /topic

如果在前面的教程中修改了 ``topic_stats_options.publish_topic`` 字段，这里将显示你指定的话题名称，而不是 ``/statistics``。

刚刚创建的订阅者节点正在为 ``topic`` 话题发布统计数据，输出话题为 ``/statistics``。

可以使用 :doc:`RQt <../../../Concepts/Intermediate/About-RQt>` 将统计数据可视化：

.. image:: images/topic_stats_rqt.png

也可以通过以下命令查看该话题发布的统计数据。由于前面将 ``topic_stats_options.publish_period`` 设置为 10 秒，因此终端每 10 秒会收到一组统计消息：

.. code-block:: console

   $ ros2 topic echo /statistics
   ---
   measurement_source_name: minimal_subscriber_with_topic_statistics
   metrics_source: message_age
   unit: ms
   window_start:
     sec: 1594856666
     nanosec: 931527366
   window_stop:
     sec: 1594856676
     nanosec: 930797670
   statistics:
   - data_type: 1
     data: 0.5522003000000001
   - data_type: 3
     data: 0.756992
   - data_type: 2
     data: 0.269039
   - data_type: 5
     data: 20.0
   - data_type: 4
     data: 0.16441001797065166
   ---
   measurement_source_name: minimal_subscriber_with_topic_statistics
   metrics_source: message_period
   unit: ms
   window_start:
     sec: 1594856666
     nanosec: 931527366
   window_stop:
     sec: 1594856676
     nanosec: 930797670
   statistics:
   - data_type: 1
     data: 499.2746365105009
   - data_type: 3
     data: 500.0
   - data_type: 2
     data: 499.0
   - data_type: 5
     data: 619.0
   - data_type: 4
     data: 0.4463309283488427

根据 `statistics_msgs 消息定义 <https://github.com/ros2/rcl_interfaces/tree/{REPOS_FILE_BRANCH}/statistics_msgs>`_，``data_type`` 的含义如下：

.. list-table:: 统计数据类型
   :header-rows: 1
   :widths: 25 75

   * - data_type 数值
     - 统计量
   * - 1
     - 平均值（average）
   * - 2
     - 最小值（minimum）
   * - 3
     - 最大值（maximum）
   * - 4
     - 标准差（standard deviation）
   * - 5
     - 样本数量（sample count）

这里可以看到，针对 ``minimal_publisher`` 发布到 ``/topic`` 的 ``std_msgs::msg::String`` 消息，目前计算了两类统计信息：

* ``message_age``：消息年龄，即消息从发布到被订阅者接收所经历的时间。
* ``message_period``：消息周期，即连续两条消息到达订阅者之间的时间间隔。

总结
----

你创建了一个启用了话题统计功能的订阅者节点。该节点接收 C++ 发布者节点发布的消息，并发布相应统计数据。你还编译并运行了该节点，并在运行期间观察了统计数据。

相关内容
--------

如需了解 ``message_age`` 统计量的计算方式，请参阅 `ROS 2 Topic Statistics 演示 <https://github.com/ros2/demos/tree/{REPOS_FILE_BRANCH}/topic_statistics_demo>`_。