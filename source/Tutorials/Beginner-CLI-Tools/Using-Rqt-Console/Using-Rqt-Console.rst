.. redirect-from::

    Tutorials/Rqt-Console/Using-Rqt-Console

.. _rqt_console:

使用 rqt_console 查看日志
=========================

**目标：** 了解用于检查日志消息的工具 rqt_console。

**教程级别：** 初级

**预计时间：** 5 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

rqt_console 是一个用于检查 ROS 2 日志消息的 GUI 工具。通常，日志消息会显示在终端中。使用 rqt_console，可以持续收集这些消息，以更有条理的方式查看、筛选和保存消息，还可以重新加载已保存的文件，在其他时间检查日志。

节点使用日志以多种方式输出事件和状态信息，其内容通常用于向用户提供信息。

前置条件
--------

需要安装 :doc:§rqt_console 和 turtlesim <../Introducing-Turtlesim/Introducing-Turtlesim>§。每次打开新终端时，都不要忘记 source ROS 2 环境。

任务
----

1. 启动
^^^^^^^

在新终端中运行以下命令启动 rqt_console：

.. code-block:: console

    $ ros2 run rqt_console rqt_console

rqt_console 窗口将打开：

.. image:: images/console.png

控制台的第一个区域用于显示系统中的日志消息。

中间区域可以通过排除严重级别来筛选消息。也可以点击右侧的加号按钮添加更多排除筛选器。

底部区域用于高亮包含指定字符串的消息，也可以在此区域添加更多筛选器。

现在在新终端中运行 turtlesim：

.. code-block:: console

    $ ros2 run turtlesim turtlesim_node

2. 在 rqt_console 中查看消息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

要生成供 rqt_console 显示的日志消息，可以让乌龟撞到墙上。在新终端中输入以下 ros2 topic pub 命令（详见 :doc:§话题教程 <../Understanding-ROS2-Topics/Understanding-ROS2-Topics>§）：

.. code-block:: console

    $ ros2 topic pub -r 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}"

由于上面的命令以固定频率发布话题，乌龟会持续撞向墙壁。在 rqt_console 中，你会反复看到同一条 Warn 严重级别的消息。

.. image:: images/warn.png

在运行 ros2 topic pub 命令的终端中按 Ctrl+C，停止乌龟继续撞墙。

3. 日志级别
^^^^^^^^^^^

ROS 2 日志级别按照严重程度排序如下：

1. Fatal（致命）
2. Error（错误）
3. Warn（警告）
4. Info（信息）
5. Debug（调试）

虽然每个级别没有严格统一的定义，但通常可以这样理解：

* Fatal：系统将终止运行，以避免受到进一步损害。
* Error：出现重大问题，不一定会损坏系统，但会阻止系统正常运行。
* Warn：出现意外活动或非理想结果，可能意味着存在更深层问题，但尚未直接影响功能。
* Info：事件和状态更新，用于确认系统是否按预期运行。
* Debug：详细记录系统执行的逐步过程。

默认级别为 Info。你只能看到默认严重程度及比它更严重的消息。

通常只有 Debug 消息被隐藏，因为它是唯一比 Info 更低的级别。例如，将默认级别设置为 Warn 后，只会看到 Warn、Error 和 Fatal 消息。

3.1 设置默认日志级别
~~~~~~~~~~~~~~~~~~~~

可以在首次运行 /turtlesim 节点时通过重映射设置默认日志级别。在终端中输入：

.. code-block:: console

    $ ros2 run turtlesim turtlesim_node --ros-args --log-level WARN

此时将看不到上次启动 turtlesim 时出现的初始 Info 消息，因为 Info 的优先级低于新的默认级别 Warn。

总结
----

如果需要仔细检查系统日志，rqt_console 会非常有用。通常可以通过日志查找问题发生的位置，以及导致问题的一系列事件。

下一步
------

下一篇教程将介绍如何使用 :doc:§ROS 2 Launch <../Launching-Multiple-Nodes/Launching-Multiple-Nodes>§ 一次启动多个节点。
