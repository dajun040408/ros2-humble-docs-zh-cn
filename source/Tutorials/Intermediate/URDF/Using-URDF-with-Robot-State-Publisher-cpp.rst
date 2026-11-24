.. Redirect-from::

    Tutorials/Intermediate/URDF/Using-URDF-with-Robot-State-Publisher

.. _URDFPlusRSPCPP:

在 C++ 中使用 URDF 和 robot_state_publisher
============================================

**目标：** 仿真 URDF 描述的行走机器人，并在 RViz 中查看。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程介绍如何构建行走机器人模型，将机器人状态作为 tf2 变换发布，并在 RViz 中查看仿真。首先创建描述机器人装配结构的 URDF 模型；然后编写节点模拟运动并发布 ``JointState`` 和变换；最后使用 ``robot_state_publisher`` 将完整机器人状态发布到 ``/tf``。

.. image:: images/r2d2_rviz_demo.gif

前置条件
--------

需要安装 ``rviz2``。每次打开新终端时，都要 source ROS 2 环境，参见 :doc:`配置 ROS 2 环境 <../../Beginner-CLI-Tools/Configuring-ROS2-Environment>`。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

进入 ROS 2 工作空间并创建 ``urdf_tutorial_cpp``：

.. code-block:: console

   $ cd src
   $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 urdf_tutorial_cpp --dependencies rclcpp geometry_msgs sensor_msgs tf2_ros tf2_geometry_msgs
   $ cd urdf_tutorial_cpp

2. 创建 URDF 文件
^^^^^^^^^^^^^^^^^

创建资源目录：

.. code-block:: console

   $ mkdir -p urdf

下载 URDF 文件 ``r2d2.urdf.xml`` 并保存到 ``urdf_tutorial_cpp/urdf/r2d2.urdf.xml``。下载 RViz 配置文件 ``r2d2.rviz`` 并保存到 ``urdf_tutorial_cpp/urdf/r2d2.rviz``。

3. 发布机器人状态
^^^^^^^^^^^^^^^^^

需要指定机器人当前状态，包括三个关节和整体机器人几何状态。创建 ``urdf_tutorial_cpp/src/urdf_tutorial.cpp``。

节点需要发布 ``sensor_msgs/msg/JointState``，并通过 ``tf2_ros::TransformBroadcaster`` 发布坐标变换。核心结构如下：

.. code-block:: cpp

   class StatePublisher : public rclcpp::Node
   {
   public:
     StatePublisher()
     : Node("state_publisher")
     {
       joint_pub_ =
         this->create_publisher<sensor_msgs::msg::JointState>("joint_states", 10);
       broadcaster =
         std::make_shared<tf2_ros::TransformBroadcaster>(this);
       timer_ = this->create_wall_timer(
         33ms, std::bind(&StatePublisher::publish, this));
     }

   private:
     rclcpp::Publisher<sensor_msgs::msg::JointState>::SharedPtr joint_pub_;
     std::shared_ptr<tf2_ros::TransformBroadcaster> broadcaster;
     rclcpp::TimerBase::SharedPtr timer_;
     void publish();
   };

在 ``publish()`` 中创建 ``JointState`` 和 ``TransformStamped`` 消息，设置当前时间戳、关节名称和位置，再通过发布者及广播器发布。``robot_state_publisher`` 会订阅 ``joint_states``，根据 URDF 关节结构计算并发布机器人各连杆之间的 TF 变换。

4. 配置构建
^^^^^^^^^^^

在 ``CMakeLists.txt`` 中添加可执行程序，并链接 ``rclcpp``、``geometry_msgs``、``sensor_msgs``、``tf2_ros`` 和 ``tf2_geometry_msgs``。同时安装 URDF 文件、RViz 配置和启动文件。

5. 构建与运行
^^^^^^^^^^^^^

在工作空间根目录构建：

.. code-block:: console

   $ colcon build --packages-select urdf_tutorial_cpp

source 工作空间后运行启动文件。启动文件加载 URDF、启动状态发布节点和 ``robot_state_publisher``，并打开 RViz。机器人模型会根据节点发布的关节状态和 TF 变换更新。

总结
----

本教程介绍了如何在 C++ 中发布关节状态和 TF 变换，并通过 ``robot_state_publisher`` 将 URDF 机器人模型显示在 RViz 中。
