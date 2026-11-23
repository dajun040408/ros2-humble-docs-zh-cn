.. redirect-from::

    Tutorials/Tf2/Writing-A-Tf2-Static-Broadcaster-Cpp

编写静态广播器（C++）
=====================

**目标：** 学习如何向 tf2 广播静态坐标系。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

发布静态变换有助于定义机器人底座与传感器或其他固定部件之间的关系。例如，在激光雷达中心建立坐标系，可以更直观地理解激光扫描测量值。

本教程分为两部分：首先编写代码向 tf2 发布静态变换，然后介绍如何使用 §tf2_ros§ 中的 §static_transform_publisher§ 命令行工具。后续教程将基于此处创建的功能包重现 :doc:§tf2 入门演示 <./Introduction-To-Tf2>§。

前置条件
--------

此前教程已经介绍了如何 :doc:§创建工作空间 <../../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace>§ 和 :doc:§创建功能包 <../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>§。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

本教程及后续教程使用 §learning_tf2_cpp§ 功能包，依赖 §geometry_msgs§、§rclcpp§、§tf2§、§tf2_ros§ 和 §turtlesim§。

.. code-block:: console

   $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 --dependencies geometry_msgs rclcpp tf2 tf2_ros turtlesim -- learning_tf2_cpp

2. 编写静态广播器节点
^^^^^^^^^^^^^^^^^^^^^

在 §src/learning_tf2_cpp/src§ 目录下载示例代码：

.. code-block:: console

   $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/static_turtle_tf2_broadcaster.cpp

Windows 命令提示符可使用 §curl -sk URL -o static_turtle_tf2_broadcaster.cpp§；PowerShell 可使用 §curl URL -o static_turtle_tf2_broadcaster.cpp§。

核心实现如下：

.. code-block:: cpp

   class StaticFramePublisher : public rclcpp::Node
   {
   public:
     explicit StaticFramePublisher(char * transformation[])
     : Node("static_turtle_tf2_broadcaster")
     {
       tf_static_broadcaster_ =
         std::make_shared<tf2_ros::StaticTransformBroadcaster>(this);
       this->make_transforms(transformation);
     }

   private:
     void make_transforms(char * transformation[])
     {
       geometry_msgs::msg::TransformStamped t;
       t.header.stamp = this->get_clock()->now();
       t.header.frame_id = "world";
       t.child_frame_id = transformation[1];
       t.transform.translation.x = atof(transformation[2]);
       t.transform.translation.y = atof(transformation[3]);
       t.transform.translation.z = atof(transformation[4]);
       tf2::Quaternion q;
       q.setRPY(
         atof(transformation[5]),
         atof(transformation[6]),
         atof(transformation[7]));
       t.transform.rotation.x = q.x();
       t.transform.rotation.y = q.y();
       t.transform.rotation.z = q.z();
       t.transform.rotation.w = q.w();
       tf_static_broadcaster_->sendTransform(t);
     }

     std::shared_ptr<tf2_ros::StaticTransformBroadcaster> tf_static_broadcaster_;
   };

   int main(int argc, char * argv[])
   {
     auto logger = rclcpp::get_logger("logger");
     if (argc != 8) {
       RCLCPP_INFO(logger, "Invalid number of parameters");
       return 1;
     }
     if (strcmp(argv[1], "world") == 0) {
       RCLCPP_INFO(logger, "Your static turtle name cannot be 'world'");
       return 1;
     }
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<StaticFramePublisher>(argv));
     rclcpp::shutdown();
     return 0;
   }

2.1 理解代码
~~~~~~~~~~~~

首先包含 §geometry_msgs/msg/transform_stamped.hpp§，以使用发布到变换树的 §TransformStamped§ 消息类型；包含 §rclcpp/rclcpp.hpp§ 以使用 §rclcpp::Node§。

§tf2::Quaternion§ 是四元数类，提供欧拉角与四元数之间的转换函数。§tf2_ros/static_transform_broadcaster.h§ 则提供 §StaticTransformBroadcaster§，用于简化静态变换发布。

§StaticFramePublisher§ 构造函数将节点命名为 §static_turtle_tf2_broadcaster§，创建 §StaticTransformBroadcaster§，并在启动时发布一次静态变换。

创建 §TransformStamped§ 后，需要设置时间戳、父坐标系名称和子坐标系名称。本例父坐标系为 §world§，子坐标系由命令行参数指定。随后使用参数填写海龟的六自由度位姿（平移和旋转），最后调用 §sendTransform()§ 发布变换。

2.2 更新 package.xml
~~~~~~~~~~~~~~~~~~~~

返回 §src/learning_tf2_cpp§，打开 §package.xml§，填写 §<description>§、§<maintainer>§ 和 §<license>§：

.. code-block:: xml

   <description>Learning tf2 with rclcpp</description>
   <maintainer email="you@email.com">Your Name</maintainer>
   <license>Apache License 2.0</license>

2.3 修改 CMakeLists.txt
~~~~~~~~~~~~~~~~~~~~~~

添加可执行程序：

.. code-block:: cmake

   add_executable(static_turtle_tf2_broadcaster src/static_turtle_tf2_broadcaster.cpp)
   ament_target_dependencies(
      static_turtle_tf2_broadcaster
      geometry_msgs
      rclcpp
      tf2
      tf2_ros
   )

   install(TARGETS
      static_turtle_tf2_broadcaster
      DESTINATION lib/${PROJECT_NAME})

3. 构建
^^^^^^^

建议在工作空间根目录检查缺失依赖：

.. code-block:: console

   $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

macOS 和 Windows 上 rosdep 不可用，需要自行安装 §geometry_msgs§ 和 §turtlesim§ 依赖。

构建功能包：

.. code-block:: console

   $ colcon build --packages-select learning_tf2_cpp

Windows 使用 §colcon build --merge-install --packages-select learning_tf2_cpp§。

打开新终端，进入工作空间根目录并 source 环境：

.. code-block:: console

   $ . install/setup.bash

Windows 命令提示符使用 §call install\setup.bat§；PowerShell 使用 §.\install\setup.ps1§。

4. 运行
^^^^^^^

运行 §static_turtle_tf2_broadcaster§ 节点：

.. code-block:: console

   $ ros2 run learning_tf2_cpp static_turtle_tf2_broadcaster mystaticturtle 0 0 1 0 0 0

该命令会广播 §mystaticturtle§ 的位姿，使其位于地面上方 1 米处。

可以通过 echo §tf_static§ 话题检查静态变换是否已经发布：

.. code-block:: console

   $ ros2 topic echo /tf_static

如果一切正常，应看到一条静态变换，父坐标系为 §world§，子坐标系为 §mystaticturtle§，平移量为 §(0, 0, 1)§，旋转四元数为 §(0, 0, 0, 1)§。

正确发布静态变换的方式
----------------------

本教程旨在展示如何使用 §StaticTransformBroadcaster§ 发布静态变换。在实际开发中，通常不需要自行编写这段代码，而应使用 §tf2_ros§ 提供的专用工具 §static_transform_publisher§。它既可以作为命令行工具使用，也可以作为节点加入启动文件。

以下命令在 §world§ 和 §mystaticturtle§ 之间发布 z 轴偏移 1 米、无旋转的静态变换。ROS 2 中 roll/pitch/yaw 分别表示绕 x/y/z 轴旋转：

.. code-block:: console

   $ ros2 run tf2_ros static_transform_publisher --x 0 --y 0 --z 1 --yaw 0 --pitch 0 --roll 0 --frame-id world --child-frame-id mystaticturtle

也可以使用四元数表示旋转：

.. code-block:: console

   $ ros2 run tf2_ros static_transform_publisher --x 0 --y 0 --z 1 --qx 0 --qy 0 --qz 0 --qw 1 --frame-id world --child-frame-id mystaticturtle

§static_transform_publisher§ 既适合手动命令行调用，也适合在 §launch§ 文件中设置静态变换：

.. tabs::

   .. group-tab:: XML

      .. literalinclude:: launch/static_transform_publisher_launch.xml
         :language: xml

   .. group-tab:: YAML

      .. literalinclude:: launch/static_transform_publisher_launch.yaml
         :language: yaml

   .. group-tab:: Python

      .. literalinclude:: launch/static_transform_publisher_launch.py
         :language: python

除 §--frame-id§ 和 §--child-frame-id§ 外，所有参数都是可选的。未指定的参数会采用单位变换对应的默认值。

总结
----

本教程介绍了静态变换的用途，例如定义 §mystaticturtle§ 相对于 §world§ 的固定关系。静态变换也有助于理解激光雷达等传感器数据，将其关联到共同坐标系。最后，我们编写了自己的节点发布静态变换，并学习了如何使用 §static_transform_publisher§ 和启动文件发布所需变换。
