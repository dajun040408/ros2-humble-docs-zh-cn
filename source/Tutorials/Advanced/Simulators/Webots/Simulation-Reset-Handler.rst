配置仿真重置处理器
==================

**目标：** 为机器人仿真添加重置处理器，在按下 Webots 重置按钮时重新启动节点。

**教程级别：** 高级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程介绍如何在 Webots 机器人仿真中实现重置处理器。

Webots 重置按钮会将世界恢复到初始状态，并重新启动控制器。这种方式可以快速重置仿真，但在 ROS 2 环境中，机器人控制器并不会自动重新启动，导致仿真停止。

重置处理器允许你在 Webots 重置按钮被按下时重新启动指定节点或执行其他操作，无需完全重启整个 ROS 系统。

前置条件
--------

开始本教程前，请确保：

* 了解 :doc:`初级教程 <../../../../Tutorials>` 中介绍的 ROS 2 节点和话题。
* 了解 Webots、ROS 2 及其接口软件包。
* 熟悉 :doc:`基础 Webots 仿真 <./Setting-Up-Simulation-Webots-Basic>`。

简单场景的重置处理器（仅控制器）
--------------------------------

在功能包的启动文件中添加 respawn 参数：

.. code-block:: python

  def generate_launch_description():
      robot_driver = WebotsController(
          robot_name='my_robot',
          parameters=[
              {'robot_description': robot_description_path}
          ],
          # 每次重置仿真时自动重新启动控制器
          respawn=True
      )

      # 启动 Webots
      webots = WebotsLauncher(world=PathJoinSubstitution([package_dir, 'worlds', world]))

      return LaunchDescription([
          webots,
          robot_driver
      ])

重置时，Webots 会终止所有驱动节点。因此，需要将驱动节点的 respawn 属性设置为 True，以便重置后自动重新启动。

多个节点的重置处理器（无需关闭系统）
------------------------------------

如果还有其他节点需要与驱动节点一起启动，例如 ros2_control 节点，可以使用 OnProcessExit 事件处理器：

.. code-block:: python

  def get_ros2_control_spawners(*args):
      # 在此声明仿真重置时需要重新启动的节点
      ros_control_node = Node(
          package='controller_manager',
          executable='spawner',
          arguments=['diffdrive_controller']
      )
      return [
          ros_control_node
      ]

  def generate_launch_description():
      robot_driver = WebotsController(
          robot_name='my_robot',
          parameters=[
              {'robot_description': robot_description_path}
          ],
          respawn=True
      )

      webots = WebotsLauncher(world=PathJoinSubstitution([package_dir, 'worlds', world]))

      # 注册重置处理器：当 robot_driver 退出时重新启动相关节点
      reset_handler = launch.actions.RegisterEventHandler(
          event_handler=launch.event_handlers.OnProcessExit(
              target_action=robot_driver,
              on_exit=get_ros2_control_spawners()
          )
      )

      return LaunchDescription([
          webots,
          robot_driver,
          reset_handler
      ])

通过监听驱动节点退出事件，可以在 Webots 重置时重新启动其他依赖节点。
