Ubuntu 安装 Webots ROS 2 接口
==============================

**目标：** 安装 webots_ros2 软件包，并在 Ubuntu 上运行仿真示例。

**教程级别：** 高级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

webots_ros2 软件包提供 ROS 2 与 Webots 之间的接口。它包含多个子软件包，其中 webots_ros2_driver 允许启动 Webots 并与之通信。后续大多数教程都会使用该接口，因此需要提前安装。本教程将介绍软件包安装以及如何运行其中一个示例。

前置条件
--------

建议先了解 :doc:`初级教程 <../../../../Tutorials>` 中介绍的 ROS 基本概念。特别是 :doc:`创建工作空间 <../../../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace>` 和 :doc:`创建第一个 ROS 2 功能包 <../../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>`。

使用 webots_ros2 接口前需要安装 Webots。可以按照`安装流程 <https://cyberbotics.com/doc/guide/installation-procedure>`_ 操作，也可以`从源码构建 <https://github.com/cyberbotics/webots/wiki/Linux-installation/>`_。

另外，也可以让 webots_ros2 自动下载并安装 Webots。当启动软件包示例且系统未找到 Webots 安装时，会显示此选项。

多个 Webots 安装版本
^^^^^^^^^^^^^^^^^^^^

如果计算机中安装了多个 Webots 版本，webots_ros2 会按以下顺序查找：

1. 如果设置了 ROS2_WEBOTS_HOME 环境变量，则使用该目录中的 Webots，不考虑版本。
2. 如果设置了 WEBOTS_HOME 环境变量，则使用该目录中的 Webots，不考虑版本。
3. 如果以上变量均未设置，则在兼容版本的默认安装路径中查找：/usr/local/webots 和 /snap/webots/current/usr/share/webots。
4. 如果找不到 Webots，webots_ros2 会显示窗口，提供自动安装最新兼容版本的选项。

任务
----

1. 安装 webots_ros2
^^^^^^^^^^^^^^^^^^^

可以安装官方发布的软件包，也可以从 GitHub 上的最新源码安装：https://github.com/cyberbotics/webots_ros2。

.. tabs::

    .. group-tab:: 安装已发布的 webots_ros2 软件包

        在终端运行：

        .. code-block:: console

            $ sudo apt-get install ros-{DISTRO}-webots-ros2

    .. group-tab:: 从源码安装 webots_ros2

        创建包含 src 目录的 ROS 2 工作空间：

        .. code-block:: console

            $ mkdir -p ~/ros2_ws/src

        source ROS 2 环境：

        .. code-block:: console

            $ source /opt/ros/{DISTRO}/setup.bash

        从 GitHub 获取源码：

        .. code-block:: console

            $ cd ~/ros2_ws
            $ git clone --recurse-submodules https://github.com/cyberbotics/webots_ros2.git src/webots_ros2

        安装功能包依赖：

        .. code-block:: console

            $ sudo apt install python3-pip python3-rosdep python3-colcon-common-extensions
            $ sudo rosdep init && rosdep update
            $ rosdep install --from-paths src --ignore-src --rosdistro {DISTRO}

        使用 colcon 构建：

        .. code-block:: console

            $ colcon build

        source 工作空间：

        .. code-block:: console

            $ source install/local_setup.bash

2. 启动 webots_ros2_universal_robot 示例
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

以下步骤介绍如何启动提供的示例。

如果尚未执行，请先 source ROS 2 环境：

.. code-block:: console

        $ source /opt/ros/{DISTRO}/setup.bash

设置 WEBOTS_HOME 环境变量可以指定 Webots 安装位置：

.. code-block:: console

        $ export WEBOTS_HOME=/usr/local/webots

如果从源码安装了 webots_ros2，还需要 source ROS 2 工作空间环境。然后按照上游示例启动 webots_ros2_universal_robot。
