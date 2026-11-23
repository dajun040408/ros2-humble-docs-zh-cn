MVSim 入门
==========

**目标：** 独立运行 MVSim 演示世界，或通过 ROS 2 启动演示，并学习如何与仿真机器人交互。

**教程级别：** 高级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

MVSim 提供了一组演示世界，展示多机器人仿真、传感器配置、地形类型、行人、关节车辆和环境布局等功能。

可以使用 mvsim 命令行工具独立运行这些演示，也可以将 MVSim 作为 ROS 2 节点运行，通过标准 ROS 2 话题发布传感器数据并接收速度指令。

.. image:: Image/mvsim_demos_screenshot.jpg
   :alt: MVSim 演示截图

前置条件
--------

请按照 :doc:§MVSim 安装教程 <Installation-Ubuntu>§ 安装 MVSim。

任务
----

1. 使用独立命令行启动演示世界
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MVSim 包含一个独立启动器，不需要 ROS 2。它适合快速测试世界文件或在非 ROS 场景中使用。

启动仓库演示：

.. code-block:: console

    $ mvsim launch ~/ros2_ws/src/mvsim/mvsim_tutorial/demo_warehouse.world.xml

如果通过二进制软件包安装，演示文件通常位于 /opt/ros/{DISTRO}/share/mvsim/mvsim_tutorial/。

还可以尝试以下演示世界：

* demo_turtlebot_world.world.xml：经典 ROS 风格环境中的 TurtleBot3，包含障碍物。
* demo_2robots.world.xml：两台机器人在家具障碍物之间移动。
* demo_elevation_map.world.xml：Jackal 机器人在带高程数据的地形上行驶。
* demo_greenhouse.world.xml：复杂温室环境，展示通过 XML 循环生成场景内容。

2. 控制机器人
^^^^^^^^^^^^^

世界启动后，可以通过以下方式控制机器人：

* 键盘：按 W/S 前进或后退，A/D 左转或右转，按空格停止。如果世界中有多台机器人，请先在 GUI 中点击选择机器人。
* 手柄：如果连接了游戏手柄，系统会自动检测。

.. image:: Image/mvsim_gui_controls.jpg
   :alt: MVSim GUI 控制说明

GUI 还提供摄像机视角、仿真速度和可视化选项。可以切换正交/透视视图，并在 3D 窗口中显示传感器数据。摄像头传感器会在 GUI 中显示实时预览。

可以在世界文件的 gui 配置中设置 show_gui_panels=false，以便启动时隐藏 GUI 子窗口；也可以为每个传感器设置 preview_depth=false，禁用 RGBD 摄像头的深度预览。

3. 通过 ROS 2 启动
^^^^^^^^^^^^^^^^^^

要将 MVSim 作为 ROS 2 节点启动，请使用提供的 launch 文件：

.. code-block:: console

    $ source /opt/ros/{DISTRO}/setup.bash
    $ ros2 launch mvsim demo_warehouse.launch.py

这会启动仿真器，并为每辆车和传感器创建 ROS 2 话题。

4. 检查 ROS 2 话题
^^^^^^^^^^^^^^^^^^

演示运行后，打开新终端并列出可用话题：

.. code-block:: console

    $ ros2 topic list

你应该能看到类似以下话题：

* /robot1/cmd_vel：发送 geometry_msgs/msg/Twist 速度命令，控制机器人。
* /robot1/odom：来自车轮编码器的里程计数据，类型为 nav_msgs/msg/Odometry。
* /robot1/base_pose_ground_truth：精确的真实位姿。
* /robot1/<sensor_name>：传感器专用话题，例如 /robot1/lidar1_points（3D LiDAR 点云）和 /robot1/laser1（2D 激光扫描）。
* /tf 和 /tf_static：遵循 REP-105 的 TF2 坐标变换，map → odom → base_link。

可以从命令行发送速度指令：

.. code-block:: console

    $ ros2 topic pub /robot1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5}, angular: {z: 0.3}}"

也可以使用 teleop_twist_keyboard 进行交互式控制：

.. code-block:: console

    $ ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/robot1/cmd_vel

5. 在 RViz2 中可视化
^^^^^^^^^^^^^^^^^^^^

可以在 RViz2 中查看 MVSim 传感器数据。部分 launch 文件提供 use_rviz 选项：

.. code-block:: console

    $ ros2 launch mvsim demo_warehouse.launch.py use_rviz:=True

也可以手动启动 RViz2，并添加相应的显示项。
