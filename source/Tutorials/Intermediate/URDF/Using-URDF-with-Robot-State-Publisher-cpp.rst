.. redirect-from::

    Tutorials/Intermediate/URDF/Using-URDF-with-Robot-State-Publisher

.. _URDFPlusRSPCPP:

在 C++ 中使用 URDF 和 robot_state_publisher
============================================

**目标：** 仿真 URDF 描述的行走机器人，并在 RViz 中查看。

**教程级别：** 中级

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程将介绍如何构建行走机器人模型，将机器人状态作为 tf2 变换发布，并在 RViz 中查看仿真。

首先创建描述机器人装配结构的 URDF 模型；然后编写一个节点模拟机器人运动，并发布 JointState 和坐标变换；最后使用 ``robot_state_publisher`` 将完整机器人状态发布到 ``/tf``。

.. image:: images/r2d2_rviz_demo.gif

前置条件
--------

* 安装 ``rviz2``，可参阅 `rviz2 安装信息 <https://index.ros.org/p/rviz2/>`_。

与其他教程一样，每次打开新终端时，都不要忘记 :doc:`source ROS 2 环境 <../../Beginner-CLI-Tools/Configuring-ROS2-Environment>`。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

进入 ROS 2 工作空间并创建名为 ``urdf_tutorial_cpp`` 的功能包：

.. code-block:: console

   $ cd src
   $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 urdf_tutorial_cpp --dependencies rclcpp geometry_msgs sensor_msgs tf2_ros tf2_geometry_msgs
   $ cd urdf_tutorial_cpp

此时应该会看到 ``urdf_tutorial_cpp`` 文件夹。接下来需要对其进行一些修改。

2. 创建 URDF 文件
^^^^^^^^^^^^^^^^^

创建用于存放资源文件的目录：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ mkdir -p urdf

  .. group-tab:: macOS

    .. code-block:: console

       $ mkdir -p urdf

  .. group-tab:: Windows

    .. code-block:: console

       $ md urdf

下载 :download:`URDF 文件 <documents/r2d2.urdf.xml>`，并保存为 ``urdf_tutorial_cpp/urdf/r2d2.urdf.xml``。

下载 :download:`RViz 配置文件 <documents/r2d2.rviz>`，并保存为 ``urdf_tutorial_cpp/urdf/r2d2.rviz``。

3. 发布机器人状态
^^^^^^^^^^^^^^^^^

现在需要一种方法来描述机器人当前的状态。

为此，必须指定三个关节的状态以及整个机器人的几何状态。

使用文本编辑器创建文件 ``urdf_tutorial_cpp/src/urdf_tutorial.cpp``，并写入以下代码：

.. code-block:: c++

   #include <rclcpp/rclcpp.hpp>
   #include <geometry_msgs/msg/quaternion.hpp>
   #include <sensor_msgs/msg/joint_state.hpp>
   #include <tf2_ros/transform_broadcaster.h>
   #include <tf2_geometry_msgs/tf2_geometry_msgs.hpp>
   #include <cmath>
   #include <thread>
   #include <chrono>

   using namespace std::chrono;

   class StatePublisher : public rclcpp::Node {
   public:
     StatePublisher(rclcpp::NodeOptions options = rclcpp::NodeOptions())
     : Node("state_publisher", options)
     {
       joint_pub_ =
         this->create_publisher<sensor_msgs::msg::JointState>("joint_states", 10);

       // 创建发布者，将 JointState 信息发送给 robot_state_publisher。
       // robot_state_publisher 会根据这些信息计算关节变换。
       broadcaster = std::make_shared<tf2_ros::TransformBroadcaster>(this);

       // 创建广播器，发布 tf2 状态信息。
       // 该广播器用于确定 axis 坐标系在 odom 坐标系中的位置。
       RCLCPP_INFO(this->get_logger(), "Starting state publisher");

       timer_ = this->create_wall_timer(
         33ms, std::bind(&StatePublisher::publish, this));
     }

   private:
     rclcpp::Publisher<sensor_msgs::msg::JointState>::SharedPtr joint_pub_;
     std::shared_ptr<tf2_ros::TransformBroadcaster> broadcaster;
     rclcpp::TimerBase::SharedPtr timer_;

     // 机器人状态变量（角度使用弧度）
     const double degree = M_PI / 180.0;
     double tilt = 0.0;
     double tinc = degree;
     double swivel = 0.0;
     double angle = 0.0;
     double height = 0.0;
     double hinc = 0.005;

     void publish();
   };

   void StatePublisher::publish()
   {
     // 创建所需消息
     geometry_msgs::msg::TransformStamped t;
     sensor_msgs::msg::JointState joint_state;

     const auto ts = this->get_clock()->now();
     joint_state.header.stamp = ts;

     // 指定 r2d2.urdf.xml 中定义的关节名称及其位置
     joint_state.name = {"swivel", "tilt", "periscope"};
     joint_state.position = {swivel, tilt, height};

     // 添加时间戳
     t.header.stamp = ts;

     // 指定父坐标系和子坐标系
     // odom 是 tf2 的基础坐标系
     t.header.frame_id = "odom";

     // axis 在 r2d2.urdf.xml 中定义，是机器人模型的基础坐标系
     t.child_frame_id = "axis";

     // 设置平移变化
     t.transform.translation.x = cos(angle) * 2;
     t.transform.translation.y = sin(angle) * 2;
     t.transform.translation.z = 0.7;

     tf2::Quaternion q;
     // 将欧拉角转换为四元数，并设置旋转变化
     q.setRPY(0, 0, angle + M_PI / 2);
     t.transform.rotation.x = q.x();
     t.transform.rotation.y = q.y();
     t.transform.rotation.z = q.z();
     t.transform.rotation.w = q.w();

     // 更新下一次循环使用的状态
     tilt += tinc;
     if (tilt < -0.5 || tilt > 0.0) {
       tinc *= -1;
     }

     height += hinc;
     if (height > 0.2 || height < 0.0) {
       hinc *= -1;
     }

     swivel += degree;  // 每次增加 1 度（弧度）
     angle += degree;   // 以较慢的速度改变角度

     // 发布消息
     broadcaster->sendTransform(t);
     joint_pub_->publish(joint_state);

     RCLCPP_INFO_THROTTLE(
       this->get_logger(), *this->get_clock(), 1000, "Publishing joint state");
   }

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<StatePublisher>());
     rclcpp::shutdown();
     return 0;
   }

该节点主要完成两项工作：

* 向 ``/joint_states`` 话题发布 ``JointState`` 消息，使 ``robot_state_publisher`` 能够计算各个关节的变换，并通过 ``/tf`` 广播这些变换。
* 广播一个根变换，将机器人模型（``axis`` 坐标系）放置在世界（``odom`` 坐标系）中，从而使整个机器人沿圆形轨迹移动。

.. include:: ../../../_internal/Rclcpp-Convenience-Header-Note.rst

4. 创建启动文件
^^^^^^^^^^^^^^^

创建新的 ``urdf_tutorial_cpp/launch`` 文件夹。

使用文本编辑器创建 ``urdf_tutorial_cpp/launch/launch.py``，并写入以下代码：

.. literalinclude:: launch/launch.py
   :language: python

5. 编辑 CMakeLists.txt
^^^^^^^^^^^^^^^^^^^^^^

需要告诉 ``colcon`` 构建工具如何构建和安装 C++ 功能包。

编辑 ``CMakeLists.txt``：

.. code-block:: cmake

   cmake_minimum_required(VERSION 3.8)
   project(urdf_tutorial_cpp)

   if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
     add_compile_options(-Wall -Wextra -Wpedantic)
   endif()

   # 查找依赖
   find_package(ament_cmake REQUIRED)
   find_package(geometry_msgs REQUIRED)
   find_package(sensor_msgs REQUIRED)
   find_package(tf2_ros REQUIRED)
   find_package(tf2_geometry_msgs REQUIRED)
   find_package(rclcpp REQUIRED)

   add_executable(urdf_tutorial_cpp src/urdf_tutorial.cpp)

   ament_target_dependencies(urdf_tutorial_cpp
     geometry_msgs
     sensor_msgs
     tf2_ros
     tf2_geometry_msgs
     rclcpp
   )

   install(TARGETS
     urdf_tutorial_cpp
     DESTINATION lib/${PROJECT_NAME}
   )

   install(DIRECTORY
     launch
     DESTINATION share/${PROJECT_NAME}
   )

   install(DIRECTORY
     urdf
     DESTINATION share/${PROJECT_NAME}
   )

   ament_package()

``install(DIRECTORY urdf ...)`` 规则会将 ``r2d2.urdf.xml`` 和 ``r2d2.rviz`` 一起复制到安装目录，以便程序运行时找到这些文件。

6. 构建功能包
^^^^^^^^^^^^^

返回工作空间根目录并构建：

.. code-block:: console

   $ colcon build --symlink-install --packages-select urdf_tutorial_cpp

加载设置文件：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ source install/setup.bash

  .. group-tab:: macOS

    .. code-block:: console

       $ source install/setup.bash

  .. group-tab:: Windows

    .. code-block:: console

       $ call install/setup.bat

7. 查看运行结果
^^^^^^^^^^^^^^^

运行新创建的功能包：

.. code-block:: console

   $ ros2 launch urdf_tutorial_cpp launch.py

为了查看结果，需要打开一个新终端，使用 RViz 配置文件启动 RViz：

.. code-block:: console

   $ rviz2 -d install/urdf_tutorial_cpp/share/urdf_tutorial_cpp/urdf/r2d2.rviz

有关 RViz 的详细使用方法，请参阅 `RViz 用户指南 <http://wiki.ros.org/rviz/UserGuide>`_。

``install/urdf_tutorial_cpp/share/urdf_tutorial_cpp/urdf/r2d2.rviz`` 是 ``r2d2.rviz`` 配置文件安装后的存储目录。

总结
----

恭喜你！你已经创建了一个 ``JointState`` 发布节点，并将其与 ``robot_state_publisher`` 结合起来，实现了一个行走机器人的仿真。
