.. redirect-from::

    Tutorials/Turtlesim/Introducing-Turtlesim

.. _Turtlesim:

使用 turtlesim、ros2 和 rqt
===========================

**目标：** 安装并使用 turtlesim 软件包和 rqt 工具，为后续教程做准备。

**教程级别：** 初级

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

Turtlesim 是一个轻量级模拟器，用于学习 ROS 2。它以最基础的方式展示 ROS 2 的工作原理，帮助你理解以后在真实机器人或机器人仿真中将要完成的工作。

ros2 工具用于管理、检查和交互 ROS 系统。它支持多种命令，针对系统的不同方面及其运行状态执行操作。例如，可以使用它启动节点、设置参数、监听话题等。ros2 工具属于 ROS 2 核心安装内容。

rqt 是 ROS 2 的图形用户界面（GUI）工具。所有在 rqt 中完成的操作都可以通过命令行实现，但 rqt 提供了更加友好的方式来操作 ROS 2 的各项元素。

本教程会涉及节点、话题和服务等 ROS 2 核心概念。后续教程会详细介绍这些概念；本教程的重点是安装工具并初步了解其用法。

前置条件
--------

上一篇 :doc:§环境配置教程 <../Configuring-ROS2-Environment>§ 介绍了如何配置环境。

任务
----

1. 安装 turtlesim
^^^^^^^^^^^^^^^^^

与往常一样，先在新终端中 source 设置文件，具体方法参阅 :doc:§上一篇教程 <../Configuring-ROS2-Environment>§。

为当前 ROS 2 发行版安装 turtlesim 软件包：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        $ sudo apt update
        $ sudo apt install ros-{DISTRO}-turtlesim

   .. group-tab:: macOS

      如果安装 ROS 2 时使用的归档包包含 ros_tutorials 仓库，那么应该已经安装 turtlesim。

   .. group-tab:: Windows

      如果安装 ROS 2 时使用的归档包包含 ros_tutorials 仓库，那么应该已经安装 turtlesim。

要检查软件包是否已安装，运行以下命令。该命令应返回 turtlesim 的可执行程序列表：

.. code-block:: console

  $ ros2 pkg executables turtlesim
  turtlesim draw_square
  turtlesim mimic
  turtlesim turtle_teleop_key
  turtlesim turtlesim_node

2. 启动 turtlesim
^^^^^^^^^^^^^^^^^

在终端中输入以下命令启动 turtlesim：

.. code-block:: console

  $ ros2 run turtlesim turtlesim_node

命令下方会显示节点日志。你可以看到默认乌龟的名称，以及它生成时所在的坐标。

模拟器窗口应该会出现，窗口中央会有一只乌龟。

.. image:: images/turtlesim.png

3. 使用 turtlesim
^^^^^^^^^^^^^^^^^

打开一个新终端，再次 source ROS 2 环境。

现在运行一个新节点，控制第一个节点中的乌龟：

.. code-block:: console

  $ ros2 run turtlesim turtle_teleop_key

此时应该打开三个窗口：运行 turtlesim_node 的终端、运行 turtle_teleop_key 的终端，以及 turtlesim 窗口。调整窗口位置，使你既能看到 turtlesim 窗口，又能让运行 turtle_teleop_key 的终端保持活动状态。

使用键盘方向键控制乌龟。乌龟会在屏幕上移动，并使用附带的画笔绘制经过的路径。

.. note::

  按下方向键只会让乌龟移动一小段距离，然后停止。这是因为在真实场景中，如果操作员失去与机器人的连接，就不希望机器人继续执行之前的指令。

可以使用相应命令的 list 子命令查看节点及其关联的话题、服务和动作：

.. code-block:: console

  $ ros2 node list
  $ ros2 topic list
  $ ros2 service list
  $ ros2 action list

后续教程会进一步介绍这些概念。本教程的目标只是概览 turtlesim，因此接下来使用 rqt 调用部分 turtlesim 服务，并与 turtlesim_node 交互。

4. 安装 rqt
^^^^^^^^^^^

打开一个新终端，安装 rqt 及其插件：

.. tabs::

   .. group-tab:: Ubuntu Linux

      .. code-block:: console

        $ sudo apt update
        $ sudo apt install ros-{DISTRO}-rqt ros-{DISTRO}-rqt-common-plugins

   .. group-tab:: macOS

      macOS 的标准 ROS 2 安装归档包包含 rqt 及其插件，因此通常已经安装。

   .. group-tab:: Windows

      Windows 的标准 ROS 2 安装归档包包含 rqt 及其插件，因此通常已经安装。

运行 rqt：

.. code-block:: console

  $ rqt

5. 使用 rqt
^^^^^^^^^^^

首次运行 rqt 时，窗口可能是空白的。无需担心，只需在顶部菜单栏选择 Plugins > Services > Service Caller。

.. note::

  rqt 查找所有插件可能需要一些时间。如果点击 Plugins 后看不到 Services 或其他选项，请关闭 rqt，并在终端中运行 rqt --force-discover。

.. image:: images/rqt.png

点击 Service 下拉列表左侧的刷新按钮，确保 turtlesim 节点的所有服务均已加载。

点击 Service 下拉列表查看 turtlesim 的服务，并选择 /spawn 服务。

5.1 尝试 spawn 服务
~~~~~~~~~~~~~~~~~~~

使用 rqt 调用 /spawn 服务。根据名称可以猜到，/spawn 会在 turtlesim 窗口中创建另一只乌龟。

在 Expression 列中双击两个单引号之间的空白处，为新乌龟指定唯一名称，例如 turtle2。可以看到，该表达式对应 name 字段，类型为 string。

接下来输入有效的生成坐标，例如 x = 1.0、y = 1.0。

.. image:: images/spawn.png
