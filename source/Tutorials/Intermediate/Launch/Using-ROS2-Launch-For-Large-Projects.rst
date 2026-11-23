在大型项目中使用 ROS 2 Launch
===============================

**目标：** 学习如何组织大型 ROS 2 项目的启动文件。

**教程级别：** 中级

.. contents:: 目录
   :depth: 2
   :local:

背景
----

大型机器人系统通常由多个功能包和大量节点组成。将所有启动逻辑写在单个文件中，会使维护、复用和调试变得困难。ROS 2 Launch 支持将系统拆分为多个可复用的启动文件，并通过参数和命名空间组合。

组织原则
--------

* 按功能划分启动文件，例如传感器、底盘、导航和可视化。
* 每个功能包提供自己的启动文件，负责启动本功能包中的节点。
* 使用父启动文件组合多个子系统。
* 通过启动参数统一配置命名空间、设备地址、配置文件路径和是否启用某个子系统。
* 使用命名空间隔离多机器人系统中的节点和话题。

包含其他启动文件
----------------

Python 启动文件可以使用 §IncludeLaunchDescription§ 包含其他启动描述，并通过 §launch_arguments§ 传递参数：

.. code-block:: python

   from launch.actions import IncludeLaunchDescription
   from launch.launch_description_sources import PythonLaunchDescriptionSource
   from launch.substitutions import PathJoinSubstitution
   from launch_ros.substitutions import FindPackageShare

   IncludeLaunchDescription(
       PythonLaunchDescriptionSource(
           PathJoinSubstitution([
               FindPackageShare('my_robot_bringup'),
               'launch',
               'sensors.launch.py'
           ])
       ),
       launch_arguments={'use_sim_time': 'False'}.items()
   )

参数与配置
----------

将可变配置作为启动参数，而不是硬编码在节点动作中。可以在顶层启动文件声明参数，再传递给对应子启动文件。对配置复杂的系统，可以使用 YAML 参数文件，并通过 §parameters§ 传递给节点。

命名空间与多机器人
------------------

多机器人系统应为每台机器人设置独立命名空间，避免节点名和话题名冲突。启动文件可以将机器人命名空间作为参数，再传递给节点或子系统启动文件。

启动文件调试
------------

* 使用 §ros2 launch <package> <file> --show-args§ 查看参数。
* 逐个启动子系统，确认其独立工作后再组合。
* 使用 §ros2 node list§、§ros2 topic list§ 和 §rqt_graph§ 检查运行图。
* 对启动失败的子系统单独检查依赖、参数和文件路径。

总结
----

大型项目应按子系统拆分启动文件，通过父启动文件组合，并使用参数、配置文件和命名空间管理系统差异。这样可以提高启动配置的可复用性和可维护性。
