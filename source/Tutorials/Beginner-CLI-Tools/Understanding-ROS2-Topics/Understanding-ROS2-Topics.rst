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
  Topic type hash: RIHS01_9c45bf16fe0983d80e3cfe750d6835843d265a9a6c46bd2e609fcddde6fb8d2a
  Endpoint type: PUBLISHER
  GID: 24.ba.3e.e7.c1.51.bb.46.21.41.de.36.1b.14.73.5e
  QoS profile:
    Reliability: RELIABLE
    History (Depth): KEEP_LAST (7)
    Durability: VOLATILE
    Lifespan: Infinite
    Deadline: Infinite
    Liveliness: AUTOMATIC
    Liveliness lease duration: Infinite

  Subscription count: 2

  Node name: _ros2cli_300492
  Node namespace: /
  Topic type: geometry_msgs/msg/Twist
  Topic type hash: RIHS01_9c45bf16fe0983d80e3cfe750d6835843d265a9a6c46bd2e609fcddde6fb8d2a
  Endpoint type: SUBSCRIPTION
  GID: cc.4d.98.79.29.91.fe.25.8a.0a.c9.03.db.1a.ec.81
  QoS profile:
    Reliability: RELIABLE
    History (Depth): KEEP_LAST (5)
    Durability: VOLATILE
    Lifespan: Infinite
    Deadline: Infinite
    Liveliness: AUTOMATIC
    Liveliness lease duration: Infinite

  Node name: turtlesim
  Node namespace: /
  Topic type: geometry_msgs/msg/Twist
  Topic type hash: RIHS01_9c45bf16fe0983d80e3cfe750d6835843d265a9a6c46bd2e609fcddde6fb8d2a
  Endpoint type: SUBSCRIPTION
  GID: 9c.33.59.38.b2.f2.42.47.69.1b.7f.0e.5e.1d.86.f5
  QoS profile:
    Reliability: RELIABLE
    History (Depth): KEEP_LAST (7)
    Durability: VOLATILE
    Lifespan: Infinite
    Deadline: Infinite
    Liveliness: AUTOMATIC
    Liveliness lease duration: Infinite

6. ros2 interface show
^^^^^^^^^^^^^^^^^^^^^^

节点通过话题发送数据时使用消息。发布者和订阅者必须发送和接收相同类型的消息，才能彼此通信。

之前运行 ``ros2 topic list -t`` 时看到的话题类型，说明了每个话题使用的消息类型。回顾一下，``cmd_vel`` 话题的类型是：

.. code-block:: console

    geometry_msgs/msg/Twist

这表示在 ``geometry_msgs`` 功能包中存在一个名为 ``Twist`` 的消息（``msg``）。

现在可以对该类型运行 ``ros2 interface show <msg_type>``，查看它的详细信息，特别是消息所要求的数据结构：

.. code-block:: console

    $ ros2 interface show geometry_msgs/msg/Twist

命令将返回：

.. code-block:: text

    # This expresses velocity in free space broken into its linear and angular parts.
        Vector3  linear
                float64 x
                float64 y
                float64 z
        Vector3  angular
                float64 x
                float64 y
                float64 z

这说明 ``/turtlesim`` 节点期望接收一条包含两个向量的消息：``linear`` 和 ``angular``，每个向量都包含三个元素。

回顾之前通过 ``echo`` 命令看到的 ``/teleop_turtle`` 发送给 ``/turtlesim`` 的数据，可以发现它具有相同的结构：

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

7. ros2 topic pub
^^^^^^^^^^^^^^^^^

了解消息结构后，就可以直接从命令行向话题发布数据：

.. code-block:: console

    $ ros2 topic pub <topic_name> <msg_type> '<args>'

其中 ``'<args>'`` 参数是实际发送到话题的数据，其结构应与上一节查看到的消息结构一致。

乌龟（以及它所模拟的真实机器人）需要持续接收指令流才能连续运行。因此，要让乌龟开始移动并持续移动，可以使用以下命令。需要注意，该参数必须使用 YAML 语法。

输入完整命令：

.. code-block:: console

  $ ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"

如果不添加命令行选项，``ros2 topic pub`` 将以 1 Hz 的频率持续发布命令。

.. image:: images/pub_stream.png

有时，你可能只希望向话题发布一次数据，而不是持续发布。此时可以添加 ``--once`` 选项：

.. code-block:: console

  $ ros2 topic pub --once -w 2 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"

``--once`` 是一个可选参数，表示“发布一条消息后退出”。

``-w 2`` 也是一个可选参数，表示“等待两个匹配的订阅者”。由于 turtlesim 和话题 echo 节点都订阅了该话题，因此这里需要等待两个订阅者。

你将在终端中看到以下输出：

.. code-block:: console

  Waiting for at least 2 matching subscription(s)...
  publisher: beginning loop
  publishing #1: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=2.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=1.8))

随后会看到乌龟移动：

.. image:: images/pub_once.png

刷新 rqt_graph，也可以从图形界面查看当前发生的情况。你会看到 ``ros2 topic pub ...`` 节点（``/_ros2cli_30358``）正在通过 ``/turtle1/cmd_vel`` 话题发布数据，而这些数据同时被 ``ros2 topic echo ...`` 节点（``/_ros2cli_26646``）和 ``/turtlesim`` 节点接收。

.. image:: images/rqt_graph2.png

最后，可以对 ``pose`` 话题运行 ``echo``，然后再次检查 rqt_graph：

.. code-block:: console

  $ ros2 topic echo /turtle1/pose

.. image:: images/rqt_graph3.png

可以看到，``/turtlesim`` 节点也在向 ``pose`` 话题发布数据，而新创建的 ``echo`` 节点订阅了该话题。

发布包含时间戳的消息时，``pub`` 有两种方法可以自动填入当前时间。

对于包含 ``std_msgs/msg/Header`` 的消息，可以将 header 字段设置为 ``auto``，以自动填充 ``stamp`` 字段：

.. code-block:: console

  $ ros2 topic pub /pose geometry_msgs/msg/PoseStamped '{header: "auto", pose: {position: {x: 1.0, y: 2.0, z: 3.0}}}'

如果消息没有使用完整的 header，而只是包含一个类型为 ``builtin_interfaces/msg/Time`` 的字段，则可以将该字段设置为 ``now``：

.. code-block:: console

  $ ros2 topic pub /reference sensor_msgs/msg/TimeReference '{header: "auto", time_ref: "now", source: "dumy"}'

8. ros2 topic hz
^^^^^^^^^^^^^^^^

还可以使用以下命令查看数据的发布频率：

.. code-block:: console

    $ ros2 topic hz /turtle1/pose
    average rate: 59.354
      min: 0.005s max: 0.027s std dev: 0.00284s window: 58

该命令会返回 ``/turtlesim`` 节点向 ``pose`` 话题发布数据的频率信息。

回顾之前的操作，你曾使用 ``ros2 topic pub --rate 1`` 将 ``turtle1/cmd_vel`` 的发布频率设置为稳定的 1 Hz。如果将上述命令中的 ``turtle1/pose`` 替换为 ``turtle1/cmd_vel``，就会看到与该频率相对应的平均值。

.. note::

  这里显示的频率反映的是由 ``ros2 topic hz`` 命令创建的订阅端实际接收消息的频率。该值可能受到平台资源和 QoS 配置的影响，因此不一定与发布者的发布频率完全一致。

9. ros2 topic bw
^^^^^^^^^^^^^^^^

可以使用以下命令查看话题占用的带宽：

.. code-block:: console

    $ ros2 topic bw /turtle1/pose
    Subscribed to [/turtle1/pose]
    1.51 KB/s from 62 messages
        Message size mean: 0.02 KB min: 0.02 KB max: 0.02 KB

该命令会返回 ``/turtle1/pose`` 话题的带宽使用情况，以及发布的消息数量。

.. note::

  这里显示的带宽反映的是由 ``ros2 topic bw`` 命令创建的订阅端实际接收数据的速率。该值可能受到平台资源和 QoS 配置的影响，因此不一定与发布者的带宽完全一致。

10. ros2 topic find
^^^^^^^^^^^^^^^^^^^

要列出指定类型的所有可用话题，可以使用：

.. code-block:: console

    $ ros2 topic find <topic_type>

回顾一下，``cmd_vel`` 话题的类型为：

.. code-block:: console

    geometry_msgs/msg/Twist

使用 ``find`` 命令并指定消息类型，即可查找可用话题：

.. code-block:: console

    $ ros2 topic find geometry_msgs/msg/Twist
    /turtle1/cmd_vel

11. 清理环境
^^^^^^^^^^^^

此时，你可能已经启动了许多节点。请在每个终端中按 ``Ctrl+C``，停止这些节点。

总结
----

节点通过话题发布信息，其他任意数量的节点都可以订阅并访问这些信息。

在本教程中，你使用 rqt_graph 和命令行工具检查了多个节点之间通过话题建立的连接。现在，你应该已经对 ROS 2 系统中的数据流动方式有了较好的理解。

下一步
------

接下来，你将在 :doc:`../Understanding-ROS2-Services/Understanding-ROS2-Services` 教程中学习 ROS 计算图中的另一种通信类型。
