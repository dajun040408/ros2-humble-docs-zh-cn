.. redirect-from::

    Tutorials/URDF/Using-URDF-with-Robot-State-Publisher

.. _URDFPlusRSPPYTHON:

在 Python 中使用 URDF 和 robot_state_publisher
===============================================

**目标：** 仿真 URDF 描述的行走机器人，并在 RViz 中查看。

**教程级别：** 中级

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程将介绍如何构建行走机器人模型，将机器人状态作为 tf2 消息发布，并在 RViz 中查看仿真。

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

创建工作空间目录：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ mkdir -p second_ros2_ws/src

  .. group-tab:: macOS

    .. code-block:: console

       $ mkdir -p second_ros2_ws/src

  .. group-tab:: Windows

    .. code-block:: console

       $ md second_ros2_ws/src

然后创建功能包：

.. code-block:: console

   $ cd second_ros2_ws/src
   $ ros2 pkg create --build-type ament_python --license Apache-2.0 urdf_tutorial_r2d2 --dependencies rclpy
   $ cd urdf_tutorial_r2d2

此时应该会看到 ``urdf_tutorial_r2d2`` 文件夹。接下来需要对其进行一些修改。

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

下载 :download:`URDF 文件 <documents/r2d2.urdf.xml>`，并保存为 ``second_ros2_ws/src/urdf_tutorial_r2d2/urdf/r2d2.urdf.xml``。

下载 :download:`RViz 配置文件 <documents/r2d2.rviz>`，并保存为 ``second_ros2_ws/src/urdf_tutorial_r2d2/urdf/r2d2.rviz``。

3. 发布机器人状态
^^^^^^^^^^^^^^^^^

现在需要一种方法来描述机器人当前的状态。

为此，必须指定三个关节的状态以及整体里程计信息。

使用文本编辑器创建文件 ``second_ros2_ws/src/urdf_tutorial_r2d2/urdf_tutorial_r2d2/state_publisher.py``，并写入以下代码：

.. code-block:: python

   from math import sin, cos, pi
   import rclpy
   from rclpy.node import Node
   from rclpy.qos import QoSProfile
   from geometry_msgs.msg import Quaternion
   from sensor_msgs.msg import JointState
   from tf2_ros import TransformBroadcaster, TransformStamped

   class StatePublisher(Node):

       def __init__(self):
           rclpy.init()
           super().__init__('state_publisher')

           qos_profile = QoSProfile(depth=10)
           self.joint_pub = self.create_publisher(
               JointState, 'joint_states', qos_profile)
           self.broadcaster = TransformBroadcaster(self, qos=qos_profile)
           self.nodeName = self.get_name()
           self.get_logger().info("{0} started".format(self.nodeName))

           degree = pi / 180.0
           loop_rate = self.create_rate(30)

           # 机器人状态
           tilt = 0.
           tinc = degree
           swivel = 0.
           angle = 0.
           height = 0.
           hinc = 0.005

           # 消息声明
           odom_trans = TransformStamped()
           odom_trans.header.frame_id = 'odom'
           odom_trans.child_frame_id = 'axis'
           joint_state = JointState()

           try:
               while rclpy.ok():
                   rclpy.spin_once(self)

                   # 更新 joint_state
                   now = self.get_clock().now()
                   joint_state.header.stamp = now.to_msg()
                   joint_state.name = ['swivel', 'tilt', 'periscope']
                   joint_state.position = [swivel, tilt, height]

                   # 更新坐标变换
                   # 沿半径为 2 米的圆周运动
                   odom_trans.header.stamp = now.to_msg()
                   odom_trans.transform.translation.x = cos(angle) * 2
                   odom_trans.transform.translation.y = sin(angle) * 2
                   odom_trans.transform.translation.z = 0.7
                   odom_trans.transform.rotation = euler_to_quaternion(
                       0, 0, angle + pi / 2)

                   # 发布关节状态和坐标变换
                   self.joint_pub.publish(joint_state)
                   self.broadcaster.sendTransform(odom_trans)

                   # 创建下一时刻的机器人状态
                   tilt += tinc
                   if tilt < -0.5 or tilt > 0.0:
                       tinc *= -1
                   height += hinc
                   if height > 0.2 or height < 0.0:
                       hinc *= -1
                   swivel += degree
                   angle += degree / 4

                   # 根据每次循环调整运行频率
                   loop_rate.sleep()

           except KeyboardInterrupt:
               pass


   def euler_to_quaternion(roll, pitch, yaw):
       qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
       qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
       qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
       qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)
       return Quaternion(x=qx, y=qy, z=qz, w=qw)


   def main():
       node = StatePublisher()


   if __name__ == '__main__':
       main()

4. 创建启动文件
^^^^^^^^^^^^^^^

创建新的 ``second_ros2_ws/src/urdf_tutorial_r2d2/launch`` 文件夹。

使用文本编辑器创建 ``second_ros2_ws/src/urdf_tutorial_r2d2/launch/demo.launch.py``，并写入以下代码：

.. literalinclude:: launch/demo_launch.py
   :language: python

5. 编辑 setup.py
^^^^^^^^^^^^^^^^

需要告诉 ``colcon`` 构建工具如何安装 Python 功能包。

编辑 ``second_ros2_ws/src/urdf_tutorial_r2d2/setup.py``，按以下步骤修改：

首先，添加导入语句：

.. code-block:: python

   import os
   from glob import glob
   from setuptools import setup
   from setuptools import find_packages

然后，在 ``data_files`` 中追加以下两行：

.. code-block:: python

   data_files=[
       # ...
       (os.path.join('share', package_name, 'launch'), glob('launch/*')),
       (os.path.join('share', package_name), glob('urdf/*')),
   ],

最后，修改 ``entry_points`` 表，使之后可以通过命令行运行 ``state_publisher``：

.. code-block:: python

   'console_scripts': [
       'state_publisher = urdf_tutorial_r2d2.state_publisher:main'
   ],

保存修改后的 ``setup.py`` 文件。

6. 安装功能包
^^^^^^^^^^^^^

进入工作空间根目录并构建功能包：

.. code-block:: console

   $ cd second_ros2_ws
   $ colcon build --symlink-install --packages-select urdf_tutorial_r2d2

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

启动功能包：

.. code-block:: console

   $ ros2 launch urdf_tutorial_r2d2 demo.launch.py

打开一个新终端，使用 RViz 配置文件启动 RViz：

.. code-block:: console

   $ rviz2 -d $(ros2 pkg prefix urdf_tutorial_r2d2 --share)/r2d2.rviz

有关 RViz 的详细使用方法，请参阅 `RViz 用户指南 <http://wiki.ros.org/rviz/UserGuide>`_。

总结
----

你已经创建了一个 ``JointState`` 发布节点，并将其与 ``robot_state_publisher`` 结合起来，实现了一个行走机器人的仿真。

本示例代码最初来自 `ros2-migration 仓库 <https://github.com/benbongalon/ros2-migration/tree/master/urdf_tutorial>`_。

部分内容参考了原始的 `ROS 1 URDF 教程 <http://wiki.ros.org/urdf/Tutorials/Using%20urdf%20with%20robot_state_publisher>`_。
