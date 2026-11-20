.. redirect-from::

    Tutorials/Understanding-ROS2-Nodes

.. _ROS2Nodes:

理解节点
========

**目标：** 了解 ROS 2 中节点的作用，以及与节点交互的工具。

**教程级别：** 初学者

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景知识
--------

1 ROS 2 计算图
^^^^^^^^^^^^^^

在接下来的几个教程中，你将学习一系列构成“ROS（2）计算图”的 ROS 2 核心概念。

ROS 计算图是一个由 ROS 2 元素组成的网络，这些元素同时处理数据。它涵盖所有可执行程序及其相互连接关系。如果将这些程序和连接全部映射并可视化，就能得到 ROS 计算图。

2 ROS 2 中的节点
^^^^^^^^^^^^^^^^

ROS 中的每个节点都应该负责一个独立、模块化的功能，例如控制车轮电机，或发布激光测距传感器的数据。每个节点都可以通过话题、服务、动作或参数与其他节点收发数据。

.. image:: images/Nodes-TopicandService.gif

一个完整的机器人系统由许多协同工作的节点组成。在 ROS 2 中，一个可执行程序（C++ 程序、Python 程序等）可以包含一个或多个节点。

前置条件
--------

:doc:`上一个教程 <../Introducing-Turtlesim/Introducing-Turtlesim>` 介绍了如何安装本教程使用的 ``turtlesim`` 功能包。

与往常一样，不要忘记在 :doc:`每个新打开的终端中加载 ROS 2 环境 <../Configuring-ROS2-Environment>`。

任务
----

1 ros2 run
^^^^^^^^^^

``ros2 run`` 命令用于运行某个功能包中的可执行程序。

.. code-block:: console

  $ ros2 run <package_name> <executable_name>

要运行 turtlesim，请打开一个新终端并输入以下命令：

.. code-block:: console

  $ ros2 run turtlesim turtlesim_node

此时会打开 turtlesim 窗口，与你在 :doc:`上一个教程 <../Introducing-Turtlesim/Introducing-Turtlesim>` 中看到的一样。

这里的功能包名称是 ``turtlesim``，可执行程序名称是 ``turtlesim_node``。

不过，我们还不知道节点名称。可以使用 ``ros2 node list`` 查找节点名称。

2 ros2 node list
^^^^^^^^^^^^^^^^

``ros2 node list`` 会显示所有正在运行的节点名称。当你希望与某个节点交互，或者系统中运行着许多节点、需要跟踪它们时，这个命令尤其有用。

保持 turtlesim 在另一个终端中运行，再打开一个新终端并输入以下命令。终端会返回节点名称：

.. code-block:: console

  $ ros2 node list
  /turtlesim

再打开一个新终端，运行以下命令启动 teleop 节点：

.. code-block:: console

  $ ros2 run turtlesim turtle_teleop_key

这里仍然使用 ``turtlesim`` 功能包，但这次运行的可执行程序是 ``turtle_teleop_key``。

回到之前运行 ``ros2 node list`` 的终端，再次执行该命令。现在可以看到两个活动节点的名称：

.. code-block:: console

  $ ros2 node list
  /turtlesim
  /teleop_turtle

2.1 重映射
~~~~~~~~~~

`重映射 <https://design.ros2.org/articles/ros_command_line_arguments.html#name-remapping-rules>`__ 允许你将节点名称、话题名称、服务名称等默认属性重新指定为自定义值。

在上一个教程中，你使用重映射修改了 ``turtle_teleop_key`` 的 ``cmd_vel`` 话题，并将目标设置为 **turtle2**。

现在，我们来重新指定 ``/turtlesim`` 节点的名称。在一个新终端中运行以下命令：

.. code-block:: console

  $ ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle

由于再次运行了 turtlesim 的 ``ros2 run`` 命令，因此会打开另一个 turtlesim 窗口。

现在回到之前运行 ``ros2 node list`` 的终端，再次执行该命令，会看到三个节点名称：

.. code-block:: console

    /my_turtle
    /turtlesim
    /teleop_turtle

3 ros2 node info
^^^^^^^^^^^^^^^^

现在你已经知道节点名称，可以使用以下命令获取更多节点信息：

.. code-block:: console

  $ ros2 node info <node_name>

要检查最新创建的节点 ``my_turtle``，运行以下命令：

.. code-block:: console

  $ ros2 node info /my_turtle
  /my_turtle
    Subscribers:
      /parameter_events: rcl_interfaces/msg/ParameterEvent
      /turtle1/cmd_vel: geometry_msgs/msg/Twist
    Publishers:
      /parameter_events: rcl_interfaces/msg/ParameterEvent
      /rosout: rcl_interfaces/msg/Log
      /turtle1/color_sensor: turtlesim/msg/Color
      /turtle1/pose: turtlesim/msg/Pose
    Service Servers:
      /clear: std_srvs/srv/Empty
      /kill: turtlesim/srv/Kill
      /my_turtle/describe_parameters: rcl_interfaces/srv/DescribeParameters
      /my_turtle/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
      /my_turtle/get_parameters: rcl_interfaces/srv/GetParameters
      /my_turtle/list_parameters: rcl_interfaces/srv/ListParameters
      /my_turtle/set_parameters: rcl_interfaces/srv/SetParameters
      /my_turtle/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
      /reset: std_srvs/srv/Empty
      /spawn: turtlesim/srv/Spawn
      /turtle1/set_pen: turtlesim/srv/SetPen
      /turtle1/teleport_absolute: turtlesim/srv/TeleportAbsolute
      /turtle1/teleport_relative: turtlesim/srv/TeleportRelative
    Service Clients:

    Action Servers:
      /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
    Action Clients:

``ros2 node info`` 会返回该节点的订阅者、发布者、服务和动作列表，也就是与该节点交互的 ROS 计算图连接关系。

现在尝试对 ``/teleop_turtle`` 节点运行相同命令，观察它与 ``my_turtle`` 节点的连接关系有何不同。

在接下来的教程中，你将进一步学习 ROS 计算图连接相关概念，包括消息类型。

总结
----

节点是 ROS 2 的基本组成元素，在机器人系统中负责单一、模块化的功能。

在本教程中，你通过运行 ``turtlesim`` 功能包中的 ``turtlesim_node`` 和 ``turtle_teleop_key`` 可执行程序，使用了节点。

你学习了如何使用 ``ros2 node list`` 查找活动节点名称，以及如何使用 ``ros2 node info`` 检查单个节点的信息。这些工具对于理解复杂真实机器人系统中的数据流非常重要。

下一步
------

现在你已经了解 ROS 2 中的节点，可以继续学习 :doc:`话题教程 <../Understanding-ROS2-Topics/Understanding-ROS2-Topics>`。话题是连接节点的一种通信方式。

相关内容
--------

:doc:`核心概念 <../../../Concepts>` 页面提供了有关节点概念的更多细节。
