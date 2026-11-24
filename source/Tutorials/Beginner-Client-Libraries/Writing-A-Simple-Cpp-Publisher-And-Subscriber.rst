.. redirect-from::

    Tutorials/Writing-A-Simple-Cpp-Publisher-And-Subscriber

.. _CppPubSub:

编写简单的发布者和订阅者（C++）
===============================

**目标：** 使用 C++ 创建并运行发布者和订阅者节点。

**教程级别：** 初级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

:doc:`节点 <../Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes>` 是通过 ROS 计算图进行通信的可执行进程。本教程中的节点通过 :doc:`话题 <../Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics>` 交换字符串消息。

示例采用简单的 talker 和 listener 系统：一个节点发布数据，另一个节点订阅话题并接收数据。示例代码位于`ros2/examples/rclcpp/topics <https://github.com/ros2/examples/tree/{REPOS_FILE_BRANCH}/rclcpp/topics>`_。

前置条件
--------

此前的教程已经介绍了如何 :doc:`创建工作空间 <./Creating-A-Workspace/Creating-A-Workspace>` 和 :doc:`创建功能包 <./Creating-Your-First-ROS2-Package>`。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

打开新终端并 :doc:`source ROS 2 安装环境 <../Beginner-CLI-Tools/Configuring-ROS2-Environment>`。

进入之前创建的 ros2_ws 工作空间，再进入 src 目录（功能包应创建在 src 中，而不是工作空间根目录），运行：

.. code-block:: console

    $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_pubsub

终端会返回消息，确认 cpp_pubsub 功能包及其文件和目录已创建。

进入 ros2_ws/src/cpp_pubsub/src。CMake 功能包的可执行程序源文件通常放在该目录中。

2. 编写发布者节点
^^^^^^^^^^^^^^^^^

下载示例 talker 代码：

.. code-block:: console

   $ wget -O publisher_member_function.cpp https://raw.githubusercontent.com/ros2/examples/{REPOS_FILE_BRANCH}/rclcpp/topics/minimal_publisher/member_function.cpp

Windows 命令行可以使用 curl：

.. code-block:: console

   $ curl -sk https://raw.githubusercontent.com/ros2/examples/{REPOS_FILE_BRANCH}/rclcpp/topics/minimal_publisher/member_function.cpp -o publisher_member_function.cpp

打开 publisher_member_function.cpp。示例通过继承 rclcpp::Node 创建节点，使用 create_publisher() 创建发布者，并通过定时器周期性发布 std_msgs/msg/String 消息。

.. code-block:: cpp

   class MinimalPublisher : public rclcpp::Node
   {
   public:
     MinimalPublisher()
     : Node("minimal_publisher")
     {
       publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
       timer_ = this->create_wall_timer(
         500ms, std::bind(&MinimalPublisher::timer_callback, this));
     }

   private:
     void timer_callback()
     {
       auto message = std_msgs::msg::String();
       message.data = "Hello, world!";
       RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
       publisher_->publish(message);
     }

     rclcpp::TimerBase::SharedPtr timer_;
     rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
   };

3. 编写订阅者节点
^^^^^^^^^^^^^^^^^

在同一 src 目录中创建 subscriber_member_function.cpp。订阅者节点同样继承 rclcpp::Node，并通过 create_subscription() 订阅 topic 话题。每次收到消息时，回调函数会输出消息内容。

.. code-block:: cpp

   class MinimalSubscriber : public rclcpp::Node
   {
   public:
     MinimalSubscriber()
     : Node("minimal_subscriber")
     {
       subscription_ = this->create_subscription<std_msgs::msg::String>(
         "topic", 10,
         std::bind(&MinimalSubscriber::topic_callback, this, std::placeholders::_1));
     }

   private:
     void topic_callback(const std_msgs::msg::String & msg) const
     {
       RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg.data.c_str());
     }

     rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
   };

4. 配置 CMakeLists.txt
^^^^^^^^^^^^^^^^^^^^^^

在 CMakeLists.txt 中查找 rclcpp 和 std_msgs，并为两个节点添加可执行程序：

.. code-block:: cmake

   find_package(rclcpp REQUIRED)
   find_package(std_msgs REQUIRED)

   add_executable(talker src/publisher_member_function.cpp)
   ament_target_dependencies(talker rclcpp std_msgs)

   add_executable(listener src/subscriber_member_function.cpp)
   ament_target_dependencies(listener rclcpp std_msgs)

   install(TARGETS talker listener DESTINATION lib/cpp_pubsub)

5. 构建并运行
^^^^^^^^^^^^^

在工作空间根目录构建：

.. code-block:: console

   $ colcon build --packages-select cpp_pubsub

打开两个终端，分别 source 工作空间并运行发布者和订阅者：

.. code-block:: console

   $ ros2 run cpp_pubsub talker

.. code-block:: console

   $ ros2 run cpp_pubsub listener

发布者会周期性发布 Hello, world!，订阅者会输出收到的消息。

总结
----

你已经创建并运行了一个 C++ 发布者和订阅者节点，它们通过话题交换字符串消息。
