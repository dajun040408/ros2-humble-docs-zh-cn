搭建机器人仿真（进阶）
======================

**目标：** 在机器人仿真中添加避障节点。

**教程级别：** 高级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程将在第一部分 :doc:§基础 Webots 仿真 <./Setting-Up-Simulation-Webots-Basic>§ 创建的功能包基础上继续扩展。目标是实现一个 ROS 2 节点，使用机器人的距离传感器检测障碍物并进行避障。本教程重点介绍如何通过 webots_ros2_driver 接口使用机器人设备。

前置条件
--------

本教程是基础仿真教程的延续，必须先完成 :doc:§基础 Webots 仿真 <./Setting-Up-Simulation-Webots-Basic>§，创建自定义功能包和必要文件。

本教程兼容 webots_ros2 2023.1.0 和 Webots R2023b，以及后续版本。

任务
----

1. 更新 my_robot.urdf
^^^^^^^^^^^^^^^^^^^^

如基础教程所述，webots_ros2_driver 包含多个插件，可以直接将大多数 Webots 设备接入 ROS 2。这些插件可以通过机器人 URDF 文件中的 device 标签加载。reference 属性应与 Webots 设备的 name 参数一致。

现有接口及其对应参数列表请参阅§设备参考页面 <https://github.com/cyberbotics/webots_ros2/wiki/References-Devices>§_。

对于未在 URDF 文件中配置的设备，接口会自动创建，并使用 ROS 参数默认值，例如 update rate、topic name 和 frame name。

将 my_robot.urdf 的内容替换为本教程提供的、包含传感器的 URDF 文件。Python 和 C++ 示例分别位于教程资源目录中。

webots_ros2_driver 除了加载自定义插件，还会解析引用 DistanceSensor 节点的 device 标签，并使用 ros 标签中的标准参数启用传感器、设置话题名称。

2. 创建避障 ROS 节点
^^^^^^^^^^^^^^^^^^^^

机器人将使用一个标准 ROS 节点检测墙壁，并发送电机控制命令以避开障碍物。

在 Python 功能包的 my_package/my_package/ 目录中创建 obstacle_avoider.py。该节点会创建速度命令发布者，并订阅距离传感器话题。

收到左侧传感器测量值时，将其保存到成员变量中。收到右侧传感器测量值时，根据两侧传感器数据生成并发布 /cmd_vel 消息。

command_message 至少需要设置 linear.x 前进速度，以便在没有检测到障碍物时机器人能够继续移动。如果任一传感器检测到障碍物，则根据传感器测量值调整速度和转向方向。

3. 构建并运行仿真
^^^^^^^^^^^^^^^^

在工作空间根目录构建功能包，source 工作空间后启动 Webots 仿真。确认机器人能够通过距离传感器检测障碍物，并根据 obstacle_avoider 节点发布的速度命令改变运动方向。
