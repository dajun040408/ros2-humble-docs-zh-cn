使用 Ros2Supervisor 节点
=========================

**目标：** 在仿真中启用默认 Supervisor 机器人 Ros2Supervisor。

**教程级别：** 高级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程介绍如何启用 Ros2Supervisor 节点。该节点会扩展 Webots 与 ROS 2 的接口，创建额外的话题和服务，以便与仿真交互。例如，可以录制动画，或在仿真运行时直接从 ROS 2 接口生成 Webots 节点。

前置条件
--------

开始本教程前，请确保：

* 了解 :doc:§初级教程 <../../../../Tutorials>§ 中介绍的 ROS 2 节点和话题。
* 了解 Webots、ROS 2 及其接口软件包。
* 熟悉 :doc:§基础 Webots 仿真 <./Setting-Up-Simulation-Webots-Basic>§。

Ros2Supervisor
--------------

Ros2Supervisor 由两个主要部分组成：

* 添加到仿真世界中的 Webots Robot 节点，其 supervisor 字段设置为 TRUE。
* 一个 ROS 2 节点，作为外部控制器连接到 Webots Robot，方式类似于自定义机器人插件。

ROS 2 节点作为控制器调用 Supervisor API 函数，以控制或操作仿真世界。用户主要通过服务和话题与该节点交互。

可以在启动 Webots 时，通过 WebotsLauncher 的 ros2_supervisor 参数自动创建这些节点：

.. code-block:: python

    webots = WebotsLauncher(
        world=PathJoinSubstitution([package_dir, 'worlds', world]),
        mode=mode,
        ros2_supervisor=True
    )

还必须将 webots._supervisor 对象包含在启动文件返回的 LaunchDescription 中：

.. code-block:: python

    return LaunchDescription([
        webots,
        webots._supervisor,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[
                    launch.actions.EmitEvent(event=launch.events.Shutdown())
                ],
            )
        )
    ])

有关 webots_ros2 项目启动文件的更多信息，请参阅 :doc:§基础 Webots 仿真 <./Setting-Up-Simulation-Webots-Basic>§。

clock 话题
----------

Ros2Supervisor 负责获取 Webots 仿真时间，并将其发布到 /clock 话题。如果其他节点将 use_sim_time 参数设置为 true，就必须启动 Ros2Supervisor。

有关 /clock 话题的更多信息，请参阅§ROS Wiki <http://wiki.ros.org/Clock>§_。

导入 Webots 节点
----------------

Ros2Supervisor 还允许通过服务，从字符串中生成 Webots 节点。

服务名称为 /Ros2Supervisor/spawn_node_from_string，类型为 webots_ros2_msgs/srv/SpawnNodeFromString。

SpawnNodeFromString 请求包含 data 字符串，响应包含 success 布尔值。

Supervisor 节点会从输入字符串中读取导入节点的名称，并将其添加到内部列表，以便之后进行移除。
