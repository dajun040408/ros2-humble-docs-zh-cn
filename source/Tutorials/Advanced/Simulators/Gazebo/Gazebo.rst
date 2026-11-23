搭建机器人仿真（Gazebo）
========================

**目标：** 使用 Gazebo 和 ROS 2 启动仿真。

**教程级别：** 高级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

前置条件
--------

首先需要安装 ROS 2 和 Gazebo。可以选择以下方式：

* 通过 deb 软件包安装。可用版本请参阅§版本对照表 <https://github.com/gazebosim/ros_gz>§_。
* 从源码编译：
  * :doc:§ROS 2 安装说明 <../../../../Installation>§。
  * §Gazebo 安装说明 <https://gazebosim.org/docs>§_。

任务
----

1. 启动仿真
^^^^^^^^^^

本演示将在 Gazebo 中模拟一台简单的差速驱动机器人。使用 Gazebo 示例中的 visualize_lidar.sdf 世界文件：https://github.com/gazebosim/gz-sim/blob/main/examples/worlds/visualize_lidar.sdf。

在终端中运行：

.. code-block:: console

    $ ign gazebo -v 4 -r visualize_lidar.sdf

.. image:: Image/gazebo_diff_drive.png

仿真运行后，可以使用 ign 命令行工具查看 Gazebo 提供的话题：

.. code-block:: console

    $ ign topic -l
    /clock
    /gazebo/resource_paths
    /gui/camera/pose
    /gui/record_video/stats
    /model/vehicle_blue/odometry
    /model/vehicle_blue/tf
    /stats
    /world/visualize_lidar_world/clock
    /world/visualize_lidar_world/dynamic_pose/info
    /world/visualize_lidar_world/pose/info
    /world/visualize_lidar_world/scene/deletion
    /world/visualize_lidar_world/scene/info
    /world/visualize_lidar_world/state
    /world/visualize_lidar_world/stats

由于尚未启动 ROS 2 节点，运行 ros2 topic list 时不应看到机器人话题：

.. code-block:: console

    $ ros2 topic list
    /parameter_events
    /rosout

2. 配置 ROS 2
^^^^^^^^^^^^^

要让仿真与 ROS 2 通信，需要使用 ros_gz_bridge 软件包。该软件包提供网络桥接，使 ROS 2 与 Gazebo Transport 之间能够交换消息。

安装桥接软件包：

.. code-block:: console

    $ sudo apt-get install ros-{DISTRO}-ros-ign-bridge

现在可以启动 ROS 与 Gazebo 之间的桥接。本例为 /model/vehicle_blue/cmd_vel 话题创建桥接：

.. code-block:: console

    $ source /opt/ros/{DISTRO}/setup.bash
    $ ros2 run ros_gz_bridge parameter_bridge /model/vehicle_blue/cmd_vel@geometry_msgs/msg/Twist]ignition.msgs.Twist

更多详情请参阅§ros_gz_bridge README <https://github.com/gazebosim/ros_gz/tree/ros2/ros_gz_bridge>§_。

桥接启动后，就可以从 ROS 2 向 Gazebo 发送机器人速度命令。
