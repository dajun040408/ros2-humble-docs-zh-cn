.. redirect-from::

    dummy-robot-demo
    Tutorials/dummy-robot-demo

使用虚拟机器人进行实验
======================

本示例展示一台简单的演示机器人，包含从发布关节状态、发布模拟激光雷达数据，到在 RViz 地图中可视化机器人模型的所有组件。

启动演示
--------

本示例假设你的 ROS 2 安装目录为 `~/ros2_ws`。请根据实际平台修改目录。

要启动演示，请运行演示系统的 bringup 启动文件。下一节将进一步解释该启动文件。终端中应看到类似以下输出：

.. code-block:: console

   $ source ~/ros2_ws/install/setup.bash
   $ ros2 launch dummy_robot_bringup dummy_robot_bringup.launch.py
   [INFO] [launch]: process[dummy_map_server-1]: started with pid [25812]
   [INFO] [launch]: process[robot_state_publisher-2]: started with pid [25813]
   [INFO] [launch]: process[dummy_joint_states-3]: started with pid [25814]
   [INFO] [launch]: process[dummy_laser-4]: started with pid [25815]
   Initialize urdf model from file: /home/mikael/work/ros2/bouncy_ws/install_debug_isolated/dummy_robot_bringup/share/dummy_robot_bringup/launch/single_rrbot.urdf
   Parsing robot urdf xml string.
   Link single_rrbot_link1 had 1 children
   Link single_rrbot_link2 had 1 children
   Link single_rrbot_link3 had 2 children
   Link single_rrbot_camera_link had 0 children
   Link single_rrbot_hokuyo_link had 0 children
   got segment single_rrbot_camera_link
   got segment single_rrbot_hokuyo_link
   got segment single_rrbot_link1
   got segment single_rrbot_link2
   got segment single_rrbot_link3
   got segment world
   Adding fixed segment from world to single_rrbot_link1
   Adding moving segment from single_rrbot_link1 to single_rrbot_link2
   [INFO] [dummy_laser]: angle inc:    0.004363
   [INFO] [dummy_laser]: scan size:    1081
   [INFO] [dummy_laser]: scan time increment:  0.000028
   Adding moving segment from single_rrbot_link2 to single_rrbot_link3
   Adding fixed segment from single_rrbot_link3 to single_rrbot_camera_link
   Adding fixed segment from single_rrbot_link3 to single_rrbot_hokuyo_link

现在，在新终端中打开 RViz2，就可以看到机器人模型。

.. code-block:: console

   $ source <ROS2_INSTALL_FOLDER>/setup.bash
   $ rviz2

这会打开 RViz2。假设 dummy_robot_bringup 仍在运行，你可以添加 TF 显示插件，并将全局坐标系设置为 `world`。完成后，应该能看到类似下图的效果：

.. image:: images/rviz-dummy-robot.png

工作原理
^^^^^^^^

仔细查看启动文件，可以发现它同时启动了几个节点：

* dummy_map_server
* dummy_laser
* dummy_joint_states
* robot_state_publisher

前两个功能包相对简单。`dummy_map_server` 会持续发布空地图，并定期更新。`dummy_laser` 的工作方式类似，会发布模拟的虚假激光扫描数据。

`dummy_joint_states` 节点发布模拟关节状态数据。由于我们发布的是只有两个关节的简单 RRbot，因此该节点会发布这两个关节的状态值。

`robot_state_publisher` 执行了真正重要的工作。它解析给定的 URDF 文件，提取机器人模型并监听接收到的关节状态。利用这些信息，它会发布机器人的 TF 数据，供 RViz 可视化。
