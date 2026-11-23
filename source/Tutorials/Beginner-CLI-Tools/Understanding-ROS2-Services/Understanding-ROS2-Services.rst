.. redirect-from::

    Tutorials/Services/Understanding-ROS2-Services

.. _ROS2Services:

理解服务
========

**目标：** 使用命令行工具学习 ROS 2 中的服务。

**教程级别：** 初学者

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景知识
--------

服务是 ROS 计算图中节点之间的另一种通信方式。与话题采用的发布者-订阅者模型不同，服务采用请求-响应模型。话题允许节点订阅数据流并持续接收更新，而服务只有在客户端明确发起调用时才会提供数据。

.. image:: images/Service-SingleServiceClient.gif

.. image:: images/Service-MultipleServiceClient.gif

前置条件
--------

本系列前面的教程已经介绍了本教程涉及的一些概念，例如 :doc:`节点 <../Understanding-ROS2-Nodes/Understanding-ROS2-Nodes>`` 和 :doc:``话题 <../Understanding-ROS2-Topics/Understanding-ROS2-Topics>`。

你需要安装 :doc:`turtlesim 功能包 <../Introducing-Turtlesim/Introducing-Turtlesim>`。

与往常一样，请记得在每个新打开的终端中 source ROS 2：:doc:`配置 ROS 2 环境 <../Configuring-ROS2-Environment>`。

任务
----

1 启动环境
^^^^^^^^^^

启动两个 turtlesim 节点：``/turtlesim`` 和 ``/teleop_turtle``。

打开一个新终端并运行：

.. code-block:: console

  $ ros2 run turtlesim turtlesim_node

再打开另一个终端并运行：

.. code-block:: console

  $ ros2 run turtlesim turtle_teleop_key

2 ros2 service list
^^^^^^^^^^^^^^^^^^^

在新终端中运行 ``ros2 service list`` 命令，会返回系统中当前所有活跃服务的列表：

.. code-block:: console

  $ ros2 service list
  /clear
  /kill
  /reset
  /spawn
  /teleop_turtle/describe_parameters
  /teleop_turtle/get_parameter_types
  /teleop_turtle/get_parameters
  /teleop_turtle/list_parameters
  /teleop_turtle/set_parameters
  /teleop_turtle/set_parameters_atomically
  /turtle1/set_pen
  /turtle1/teleport_absolute
  /turtle1/teleport_relative
  /turtlesim/describe_parameters
  /turtlesim/get_parameter_types
  /turtlesim/get_parameters
  /turtlesim/list_parameters
  /turtlesim/set_parameters
  /turtlesim/set_parameters_atomically

你会发现，两个节点都具有相同的六个名称中包含 ``parameters`` 的服务。ROS 2 中几乎每个节点都有这些基础设施服务，参数功能正是基于这些服务实现的。下一篇教程会进一步介绍参数。在本教程中，我们暂时不讨论这些参数服务。

现在重点关注 turtlesim 专用的服务：``/clear``、``/kill``、``/reset``、``/spawn``、``/turtle1/set_pen``、``/turtle1/teleport_absolute`` 和 ``/turtle1/teleport_relative``。你可能还记得，在 :doc:`使用 turtlesim、ros2 和 rqt <../Introducing-Turtlesim/Introducing-Turtlesim>` 教程中，已经通过 rqt 调用过其中一些服务。

3 ros2 service type
^^^^^^^^^^^^^^^^^^^

服务类型描述了服务请求数据和响应数据的结构。服务类型的定义方式与话题类型类似，但服务类型包含两部分：一条消息用于请求，另一条消息用于响应。

要查看某个服务的类型，请使用：

.. code-block:: console

  $ ros2 service type <service_name>

下面查看 turtlesim 的 ``/clear`` 服务。在新终端中输入：

.. code-block:: console

  $ ros2 service type /clear
  std_srvs/srv/Empty

``Empty`` 类型表示调用该服务时，请求不发送任何数据，接收响应时也不会收到任何数据。

3.1 ros2 service list -t
~~~~~~~~~~~~~~~~~~~~~~~~

如果希望一次查看所有活跃服务的类型，可以在 ``list`` 命令后添加 ``--show-types`` 选项，简写为 ``-t``：

.. code-block:: console

  $ ros2 service list -t
  /clear [std_srvs/srv/Empty]
  /kill [turtlesim/srv/Kill]
  /reset [std_srvs/srv/Empty]
  /spawn [turtlesim/srv/Spawn]
  ...
  /turtle1/set_pen [turtlesim/srv/SetPen]
  /turtle1/teleport_absolute [turtlesim/srv/TeleportAbsolute]
  /turtle1/teleport_relative [turtlesim/srv/TeleportRelative]
  ...

4 ros2 service find
^^^^^^^^^^^^^^^^^^^

如果要查找所有指定类型的服务，可以使用：

.. code-block:: console

  $ ros2 service find <type_name>

例如，可以这样查找所有 ``Empty`` 类型的服务：

.. code-block:: console

  $ ros2 service find std_srvs/srv/Empty
  /clear
  /reset

5 ros2 interface show
^^^^^^^^^^^^^^^^^^^^^

你可以从命令行调用服务，但首先需要了解输入参数的数据结构。

.. code-block:: console

  $ ros2 interface show <type_name>

尝试查看 ``/clear`` 服务的类型 ``Empty``：

.. code-block:: console

  $ ros2 interface show std_srvs/srv/Empty
  ---

``---`` 用于分隔请求结构（上方）和响应结构（下方）。但正如前面所学，``Empty`` 类型既不发送也不接收任何数据，因此它的结构自然是空的。

接下来检查一个能够发送和接收数据的服务类型，例如 ``/spawn``。从 ``ros2 service list -t`` 的结果可知，``/spawn`` 的类型是 ``turtlesim/srv/Spawn``。

要查看 ``/spawn`` 服务请求和响应的参数，请运行：

.. code-block:: console

  $ ros2 interface show turtlesim/srv/Spawn
  float32 x
  float32 y
  float32 theta
  string name # Optional. A unique name will be created and returned if this is empty
  ---
  string name

``---`` 上方的信息告诉我们调用 ``/spawn`` 所需的参数。``x``、``y`` 和 ``theta`` 决定新生成海龟的二维位姿，而 ``name`` 显然是可选参数。

分隔线下方的信息在本例中不是调用服务时需要关注的内容，但它有助于理解服务调用返回的响应数据类型。

6 ros2 service call
^^^^^^^^^^^^^^^^^^^

现在你已经了解服务类型、如何查找服务类型，以及如何查看该类型参数的结构，可以使用以下命令调用服务：

.. code-block:: console

  $ ros2 service call <service_name> <service_type> <arguments>

其中 ``<arguments>`` 部分是可选的。例如，你已经知道 ``Empty`` 类型的服务不需要任何参数：

.. code-block:: console

  $ ros2 service call /clear std_srvs/srv/Empty

该命令会清空 turtlesim 窗口中海龟绘制的所有轨迹。

.. image:: images/clear.png

现在，通过调用 ``/spawn`` 服务并设置参数来生成一只新海龟。从命令行调用服务时，``<arguments>`` 必须使用 YAML 语法。

输入以下命令：

.. code-block:: console

  $ ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"
  requester: making request: turtlesim.srv.Spawn_Request(x=2.0, y=2.0, theta=0.2, name='')

  response:
  turtlesim.srv.Spawn_Response(name='turtle2')

终端会先以类似方法调用的形式显示请求内容，然后显示服务响应。

turtlesim 窗口会立即更新，显示刚刚生成的新海龟：

.. image:: images/spawn.png

总结
----

ROS 2 节点可以使用服务进行通信。与话题这种单向通信模式不同——一个节点发布信息，其他一个或多个订阅者可以接收这些信息——服务采用请求/响应模式：客户端向提供服务的节点发送请求，服务端处理请求并生成响应。

通常不建议使用服务进行连续调用；对于这类场景，话题甚至动作可能更合适。

在本教程中，你使用命令行工具识别、检查并调用了服务。

后续步骤
--------

在下一篇教程 :doc:`理解参数 <../Understanding-ROS2-Parameters/Understanding-ROS2-Parameters>` 中，你将学习如何配置节点设置。

相关内容
--------

还可以查看 `这篇教程 <https://discourse.ubuntu.com/t/call-services-in-ros-2/15261>`_。该教程通过一个 Robotis 机械臂展示了 ROS 服务的实际应用。
