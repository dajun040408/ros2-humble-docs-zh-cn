.. redirect-from::

    Tutorials/Topics/Understanding-ROS2-Topics

.. _ROS2Topics:

理解话题
========

**目标：** 使用 rqt_graph 和命令行工具检查 ROS 2 话题。

**教程级别：** 初级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

ROS 2 将复杂系统拆分为许多模块化节点。话题是 ROS 计算图的重要组成部分，充当节点之间交换消息的总线。

.. image:: images/Topic-SinglePublisherandSingleSubscriber.gif

一个节点可以向任意数量的话题发布数据，同时也可以订阅任意数量的话题。

.. image:: images/Topic-MultiplePublisherandMultipleSubscriber.gif

话题是节点之间以及系统不同部分之间传递数据的主要方式之一。

前置条件
--------

:doc:`上一篇教程 <../Understanding-ROS2-Nodes/Understanding-ROS2-Nodes>` 介绍了节点的相关背景知识，本教程将在此基础上继续学习。

每次打开新终端时，都不要忘记 source ROS 2 环境。

任务
----

1. 启动
^^^^^^^

打开一个新终端并运行：

.. code-block:: console

    $ ros2 run turtlesim turtlesim_node

打开另一个终端并运行：

.. code-block:: console

    $ ros2 run turtlesim turtle_teleop_key

回顾上一篇教程，默认情况下这两个节点的名称分别是 /turtlesim 和 /teleop_turtle。

2. rqt_graph
^^^^^^^^^^^^

在本教程中，我们将使用 rqt_graph 可视化节点和话题的变化，以及它们之间的连接关系。

:doc:`turtlesim 教程 <../Introducing-Turtlesim/Introducing-Turtlesim>` 介绍了如何安装 rqt 及其所有插件，包括 rqt_graph。

打开一个新终端并输入以下命令运行 rqt_graph：

.. code-block:: console

    $ ros2 run rqt_graph rqt_graph

也可以打开 rqt，然后选择 Plugins > Introspection > Node Graph。

.. image:: images/rqt_graph.png

你应该能看到上述节点和话题，以及计算图外围的两个动作（暂时先忽略它们）。将鼠标悬停在图中央的话题上，可以看到类似上图的颜色高亮效果。

该图展示了 /turtlesim 和 /teleop_turtle 节点如何通过话题进行通信。/teleop_turtle 节点将数据（你输入的、用于控制乌龟移动的按键指令）发布到 /turtle1/cmd_vel 话题，而 /turtlesim 节点订阅该话题以接收数据。

当检查包含大量节点和话题的复杂系统时，rqt_graph 的高亮功能非常有用。

rqt_graph 是一个图形化内省工具。接下来介绍一些用于检查话题的命令行工具。

3. ros2 topic list
^^^^^^^^^^^^^^^^^^

在新终端中运行 ros2 topic list，可以列出系统当前所有活动话题：

.. code-block:: console

  $ ros2 topic list
  /parameter_events
  /rosout
  /turtle1/cmd_vel
  /turtle1/color_sensor
  /turtle1/pose

运行 ros2 topic list -t 会返回相同的话题列表，并在括号中附加话题类型：

.. code-block:: console

  $ ros2 topic list -t
  /parameter_events [rcl_interfaces/msg/ParameterEvent]
  /rosout [rcl_interfaces/msg/Log]
  /turtle1/cmd_vel [geometry_msgs/msg/Twist]
  /turtle1/color_sensor [turtlesim/msg/Color]
  /turtle1/pose [turtlesim/msg/Pose]

这些属性，尤其是类型，是节点判断彼此是否正在通过话题交换相同类型信息的依据。

如果想知道这些话题在 rqt_graph 中的位置，可以取消勾选 Hide 下的所有选项。为了避免混淆，目前仍建议保持这些选项处于勾选状态。

4. ros2 topic echo
^^^^^^^^^^^^^^^^^^

要查看话题上发布的数据，请使用：

.. code-block:: console

    $ ros2 topic echo <topic_name>

我们已经知道 /teleop_turtle 通过 /turtle1/cmd_vel 话题向 /turtlesim 发布数据，因此可以使用 echo 检查该话题：

.. code-block:: console

    $ ros2 topic echo /turtle1/cmd_vel

最初该命令不会返回任何数据，因为它正在等待 /teleop_turtle 发布消息。

回到运行 turtle_teleop_key 的终端，使用方向键移动乌龟。同时观察运行 ros2 topic echo 的终端，就会看到每次移动都会发布对应的速度数据：

.. code-block:: console

  linear:
    x: 2.0
    y: 0.0
    z: 0.0
  angular:
    x: 0.0
    y: 0.0
    z: 0.0
    ---

现在回到 rqt_graph，取消勾选 Debug 选项。

.. image:: images/debug.png

/_ros2cli_26646 是刚才运行 echo 命令时创建的节点（编号可能不同）。现在可以看到发布者通过 cmd_vel 话题发布数据，并且有两个订阅者订阅了该话题。

5. ros2 topic info
^^^^^^^^^^^^^^^^^^

话题通信不一定是一对一，也可以是一对多、多对一或多对多。

运行以下命令查看：

.. code-block:: console

  $ ros2 topic info /turtle1/cmd_vel
  Type: geometry_msgs/msg/Twist
  Publisher count: 1
  Subscription count: 2

5.1 ros2 topic info --verbose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

要查看话题的更多详细信息，可以使用 --verbose（或 -v）标志：

.. code-block:: console

  $ ros2 topic info /turtle1/cmd_vel --verbose

输出还会包含发布者和订阅者的节点名称及命名空间、话题类型和 QoS 配置文件等信息。

.. code-block:: console

  Type: geometry_msgs/msg/Twist

  Publisher count: 1

  Node name: teleop_turtle
  Node namespace: /
  Topic type: geometry_msgs/msg/Twist
  Endpoint type: PUBLISHER
  QoS profile:
    Reliability: RELIABLE
    History (Depth): KEEP_LAST (7)
    Durability: VOLATILE
    Lifespan: Infinite
    Deadline: Infinite
    Liveliness: AUTOMATIC
    Liveliness lease duration: Infinite
