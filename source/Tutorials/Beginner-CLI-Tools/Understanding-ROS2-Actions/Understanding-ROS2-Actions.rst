.. redirect-from::

    Tutorials/Understanding-ROS2-Actions

.. _ROS2Actions:

理解动作
========

**目标：** 检查 ROS 2 中的动作。

**教程级别：** 初学者

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景知识
--------

动作是 ROS 2 中适用于长时间运行任务的一种通信类型，由目标（goal）、反馈（feedback）和结果（result）三部分组成。

动作构建于话题和服务之上。它的功能与服务类似，但可以取消，并且能够持续提供反馈；服务通常只返回一次响应。

动作采用客户端-服务器模型，与发布者-订阅者模型类似（参见 :doc:`话题教程 <../Understanding-ROS2-Topics/Understanding-ROS2-Topics>`）。动作客户端节点向动作服务端节点发送目标，服务端确认目标后持续返回反馈，并在任务完成时返回结果。

.. image:: images/Action-SingleActionClient.gif

前置条件
--------

本教程建立在前面教程介绍的概念之上，例如 :doc:`节点 <../Understanding-ROS2-Nodes/Understanding-ROS2-Nodes>` 和 :doc:`话题 <../Understanding-ROS2-Topics/Understanding-ROS2-Topics>`。

本教程使用 :doc:`turtlesim 功能包 <../Introducing-Turtlesim/Introducing-Turtlesim>`。请记得在每个新终端中 source ROS 2：:doc:`配置 ROS 2 环境 <../Configuring-ROS2-Environment>`。

任务
----

1 启动环境
^^^^^^^^^^

启动两个 turtlesim 节点：``/turtlesim`` 和 ``/teleop_turtle``。

打开两个终端，分别运行：

.. code-block:: console

  $ ros2 run turtlesim turtlesim_node

  $ ros2 run turtlesim turtle_teleop_key

2 使用动作
^^^^^^^^^^

启动 ``/teleop_turtle`` 节点时，终端会显示：

.. code-block:: text

    Use arrow keys to move the turtle.
    Use G|B|V|C|D|E|R|T keys to rotate to absolute orientations. 'F' to cancel a rotation.

第二行对应一个动作。第一行对应 ``cmd_vel`` 话题，前面已经在 :doc:`话题教程 <../Understanding-ROS2-Topics/Understanding-ROS2-Topics>` 中介绍过。

在美式 QWERTY 键盘上，字母键 ``G|B|V|C|D|E|R|T`` 围绕 ``F`` 键形成一个方框。每个按键相对于 ``F`` 的位置，对应 turtlesim 中的一个方向。例如，按下 ``E`` 会使海龟转向左上角。

观察运行 ``/turtlesim`` 节点的终端。每次按下这些按键之一，都会向该节点中的动作服务端发送一个目标，要求海龟旋转到指定方向。完成旋转后，终端会显示：

.. code-block:: console

    [INFO] [turtlesim]: Rotation goal completed successfully

``F`` 键会取消正在执行的目标。尝试先按下 ``C``，然后在旋转完成前按下 ``F``，终端会显示：

.. code-block:: console

    [INFO] [turtlesim]: Rotation goal canceled

客户端可以取消目标，服务端也可以停止目标。当服务端决定停止处理某个目标时，称为中止（abort）该目标。

尝试按下 ``D``，然后在第一次旋转完成前按下 ``G``。终端会显示：

.. code-block:: console

    [WARN] [turtlesim]: Rotation goal received before a previous goal finished. Aborting previous goal

服务端因为收到新目标而中止了第一个目标。它也可以选择拒绝新目标，或等第一个目标完成后再执行第二个目标。不要认为所有动作服务端都会在收到新目标时中止当前目标。

3 ros2 node info
^^^^^^^^^^^^^^^^

要查看 ``/turtlesim`` 节点提供的动作，请运行：

.. code-block:: console

  $ ros2 node info /turtlesim

在输出中找到：

.. code-block:: text

    Action Servers:
      /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
    Action Clients:

``/turtle1/rotate_absolute`` 位于 ``Action Servers`` 下，说明 ``/turtlesim`` 节点会响应该动作并提供反馈。

``/teleop_turtle`` 节点则是该动作的客户端。运行以下命令查看：

.. code-block:: console

  $ ros2 node info /teleop_turtle

输出中会包含：

.. code-block:: text

    Action Servers:

    Action Clients:
      /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute

4 ros2 action list
^^^^^^^^^^^^^^^^^^

要列出 ROS 计算图中的所有动作，请运行：

.. code-block:: console

  $ ros2 action list
  /turtle1/rotate_absolute

目前只有这一个动作，用于控制海龟旋转。前面已经看到，该动作有一个客户端（属于 ``/teleop_turtle``）和一个服务端（属于 ``/turtlesim``）。

4.1 ros2 action list -t
~~~~~~~~~~~~~~~~~~~~~~~

动作也有类型。要查找 ``/turtle1/rotate_absolute`` 的类型，请运行：

.. code-block:: console

  $ ros2 action list -t
  /turtle1/rotate_absolute [turtlesim/action/RotateAbsolute]

方括号中显示的类型为 ``turtlesim/action/RotateAbsolute``。从命令行或代码执行动作时，需要使用该类型。

5 ros2 action info
^^^^^^^^^^^^^^^^^^

可以使用以下命令进一步检查该动作：

.. code-block:: console

  $ ros2 action info /turtle1/rotate_absolute
  Action: /turtle1/rotate_absolute
  Action clients: 1
      /teleop_turtle
  Action servers: 1
      /turtlesim

这与前面对两个节点运行 ``ros2 node info`` 得到的结果一致。

6 ros2 interface show
^^^^^^^^^^^^^^^^^^^^^

发送动作目标之前，还需要了解动作类型的结构。运行：

.. code-block:: console

  $ ros2 interface show turtlesim/action/RotateAbsolute

命令会返回：

.. code-block:: text

  # The desired heading in radians
  float32 theta
  ---
  # The angular displacement in radians to the starting position
  float32 delta
  ---
  # The remaining rotation in radians
  float32 remaining

第一条 ``---`` 之前是目标请求的结构；第二部分是结果结构；最后一部分是反馈结构。

7 ros2 action send_goal
^^^^^^^^^^^^^^^^^^^^^^^

可以使用以下语法从命令行发送动作目标：

.. code-block:: console

  $ ros2 action send_goal <action_name> <action_type> <values>

``<values>`` 必须使用 YAML 格式。观察 turtlesim 窗口，并运行：

.. code-block:: console

  $ ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}"
  Waiting for an action server to become available...
  Sending goal:
     theta: 1.57

  Goal accepted with ID: f8db8f44410849eaa93d3feb747dd444

  Result:
    delta: -1.568000316619873

  Goal finished with status: SUCCEEDED

你应该能看到海龟正在旋转。每个目标都有唯一 ID，会显示在返回消息中。结果字段 ``delta`` 表示相对于起始位置的角位移。

如果要查看目标反馈，可以在 ``ros2 action send_goal`` 命令中添加 ``--feedback``：

.. code-block:: console

  $ ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: -1.57}" --feedback
  Sending goal:
     theta: -1.57

  Goal accepted with ID: e6092c831f994afda92f0086f220da27

  Feedback:
    remaining: -3.1268222332000732

  Feedback:
    remaining: -3.1108222007751465

  …

  Result:
    delta: 3.1200008392333984

  Goal finished with status: SUCCEEDED

在目标完成之前，你会持续收到反馈，其中 ``remaining`` 表示剩余旋转角度，单位为弧度。

总结
----

动作类似于服务，但适用于长时间运行的任务，能够定期提供反馈，并且可以取消。机器人系统通常会使用动作执行导航任务：动作目标可以要求机器人移动到某个位置；在移动过程中，机器人持续发送反馈，到达目标后发送最终结果。

turtlesim 提供了一个动作服务端，动作客户端可以向它发送海龟旋转目标。本教程检查了 ``/turtle1/rotate_absolute`` 动作，以了解动作的概念和工作方式。

后续步骤
--------

现在，你已经学习了所有 ROS 2 核心概念。本系列最后几篇教程将介绍一些实用工具和技巧，首先从 :doc:`使用 rqt_console <../Using-Rqt-Console/Using-Rqt-Console>` 开始。

相关内容
--------

你可以在 ``ROS 2 动作设计文档 <https://design.ros2.org/articles/actions.html>``_ 中阅读更多关于动作设计决策的信息。
