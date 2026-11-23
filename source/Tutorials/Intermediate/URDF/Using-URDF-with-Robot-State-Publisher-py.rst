.. redirect-from::

    Tutorials/URDF/Using-URDF-with-Robot-State-Publisher

.. _URDFPlusRSPPYTHON:

在 Python 中使用 URDF 和 robot_state_publisher
===============================================

**目标：** 仿真 URDF 描述的行走机器人，并在 RViz 中查看。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程介绍如何构建行走机器人模型，将机器人状态作为 tf2 变换发布，并在 RViz 中查看仿真。首先创建描述机器人装配结构的 URDF 模型；然后编写节点模拟机器人运动并发布 §JointState§ 和变换；最后使用 §robot_state_publisher§ 将完整机器人状态发布到 §/tf§。

.. image:: images/r2d2_rviz_demo.gif

前置条件
--------

需要安装 §rviz2§。每次打开新终端时，都要 source ROS 2 环境，参见 :doc:§配置 ROS 2 环境 <../../Beginner-CLI-Tools/Configuring-ROS2-Environment>§。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

创建工作空间目录并创建 Python 功能包：

.. code-block:: console

   $ mkdir -p second_ros2_ws/src
   $ cd second_ros2_ws/src
   $ ros2 pkg create --build-type ament_python --license Apache-2.0 urdf_tutorial_r2d2 --dependencies rclpy
   $ cd urdf_tutorial_r2d2

2. 创建 URDF 文件
^^^^^^^^^^^^^^^^^

创建资源目录：

.. code-block:: console

   $ mkdir -p urdf

下载 URDF 文件 §r2d2.urdf.xml§，保存到 §second_ros2_ws/src/urdf_tutorial_r2d2/urdf/r2d2.urdf.xml§。同时下载 RViz 配置文件 §r2d2.rviz§，保存到同一目录。

3. 发布机器人状态
^^^^^^^^^^^^^^^^^

需要指定机器人当前状态，包括三个关节和整体里程计信息。创建 §second_ros2_ws/src/urdf_tutorial_r2d2/urdf_tutorial_r2d2/state_publisher.py§。

节点需要发布 §sensor_msgs/msg/JointState§，并通过 §tf2_ros.TransformBroadcaster§ 发布坐标变换。主要结构如下：

.. code-block:: python

   from math import sin, cos, pi
   import rclpy
   from rclpy.node import Node
   from rclpy.qos import QoSProfile
   from sensor_msgs.msg import JointState
   from tf2_ros import TransformBroadcaster, TransformStamped

   class StatePublisher(Node):
       def __init__(self):
           super().__init__('state_publisher')
           qos_profile = QoSProfile(depth=10)
           self.joint_pub = self.create_publisher(
               JointState, 'joint_states', qos_profile)
           self.broadcaster = TransformBroadcaster(self, qos=qos_profile)
           self.timer = self.create_timer(1.0 / 30.0, self.publish_state)

       def publish_state(self):
           now = self.get_clock().now()
           joint_state = JointState()
           joint_state.header.stamp = now.to_msg()
           joint_state.name = ['swivel', 'tilt', 'periscope']
           joint_state.position = [self.swivel, self.tilt, self.height]
           self.joint_pub.publish(joint_state)

定时回调需要更新关节状态，并创建相应的 §TransformStamped§，通过广播器发布机器人底座与里程计坐标系之间的变换。完整示例还会更新关节角度、伸缩高度和机器人沿圆形轨迹移动的位置。

4. 配置功能包
^^^^^^^^^^^^^

在 §package.xml§ 中声明 §rclpy§、§sensor_msgs§、§geometry_msgs§、§tf2_ros§ 和 §robot_state_publisher§ 等运行依赖。将 URDF、RViz 配置文件和启动文件安装到功能包 share 目录，并在 §setup.py§ 中注册状态发布节点入口点。

5. 构建与运行
^^^^^^^^^^^^^

在工作空间根目录构建：

.. code-block:: console

   $ colcon build --packages-select urdf_tutorial_r2d2

source 工作空间环境后启动模型展示文件。启动文件会加载 URDF，运行状态发布节点和 §robot_state_publisher§，并打开 RViz。机器人模型会随着关节状态和 TF 变换更新。

总结
----

本教程介绍了如何使用 Python 发布关节状态和 TF 变换，并通过 §robot_state_publisher§ 将 URDF 机器人模型显示在 RViz 中。
