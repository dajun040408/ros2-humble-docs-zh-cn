Windows 安装 Webots ROS 2 接口
===============================

**目标：** 安装 webots_ros2 软件包，并在 Windows 上运行仿真示例。

**教程级别：** 高级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

webots_ros2 软件包提供 ROS 2 与 Webots 之间的接口。它包含多个子软件包，其中 webots_ros2_driver 允许 ROS 节点与 Webots 通信。其他子软件包主要是示例，展示如何通过该接口实现不同功能。本教程介绍软件包安装和示例运行。

前置条件
--------

建议先了解 :doc:`初级教程 <../../../../Tutorials>` 中介绍的 ROS 基本概念。特别是 :doc:`创建工作空间 <../../../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace>` 和 :doc:`创建第一个 ROS 2 功能包 <../../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>`。

使用 webots_ros2 软件包前需要安装 Webots。可以按照`安装流程 <https://cyberbotics.com/doc/guide/installation-procedure>`_ 操作，也可以`从源码构建 <https://github.com/cyberbotics/webots/wiki/Windows-installation/>`_。

也可以让 webots_ros2 自动下载 Webots。当启动示例且系统未找到 Webots 安装时，会显示自动安装选项。

多个 Webots 安装版本
^^^^^^^^^^^^^^^^^^^^

如果安装了多个 Webots 版本，ROS 2 会按以下顺序查找：

1. 如果设置了 ROS2_WEBOTS_HOME 环境变量，则使用该目录中的 Webots，不考虑版本。
2. 如果设置了 WEBOTS_HOME 环境变量，则使用该目录中的 Webots，不考虑版本。
3. 如果前两项均未设置，则在兼容版本的默认安装路径 C:\Program Files\Webots 中查找。
4. 如果找不到 Webots，webots_ros2 会显示窗口，提供自动安装最新兼容版本的选项。

任务
----

1. 安装 WSL2
^^^^^^^^^^^^

在 Windows 上，与原生 Windows 安装相比，WSL（Windows Subsystem for Linux）可以改善 ROS 2 使用体验，因为 ROS 2 将运行在 Linux 平台上。

按照`Microsoft 官方教程 <https://learn.microsoft.com/en-us/windows/wsl/install>`_ 安装与当前 ROS 发行版兼容的 Ubuntu，并升级到 WSL2。

2. 在 WSL 中安装 ROS 2
^^^^^^^^^^^^^^^^^^^^^^

按照 :doc:`Ubuntu deb 安装指南 <../../../../Installation/Ubuntu-Install-Debs>` 在 Ubuntu WSL 中安装 ROS 2。

3. 安装 webots_ros2
^^^^^^^^^^^^^^^^^^^

可以安装官方发布的软件包，也可以从 GitHub 最新源码安装：https://github.com/cyberbotics/webots_ros2。

以下命令必须在 WSL 环境中执行。

.. tabs::

    .. group-tab:: 安装已发布的 webots_ros2 软件包

        .. code-block:: console

            $ sudo apt-get install ros-{DISTRO}-webots-ros2

    .. group-tab:: 从源码安装 webots_ros2

        创建工作空间：

        .. code-block:: console

            $ mkdir -p ~/ros2_ws/src

        source ROS 2 环境：

        .. code-block:: console

            $ source /opt/ros/{DISTRO}/setup.bash

        获取源码：

        .. code-block:: console

            $ cd ~/ros2_ws
            $ git clone --recurse-submodules https://github.com/cyberbotics/webots_ros2.git src/webots_ros2

        安装依赖：

        .. code-block:: console

            $ sudo apt install python3-pip python3-rosdep python3-colcon-common-extensions
            $ sudo rosdep init && rosdep update
            $ rosdep install --from-paths src --ignore-src --rosdistro {DISTRO}

        使用 colcon 构建并 source 工作空间：

        .. code-block:: console

            $ colcon build
            $ source install/local_setup.bash

4. 启动 webots_ros2_universal_robot 示例
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

WSL 目前不支持硬件加速。因此，Webots 应安装并运行在 Windows 主机上，而 ROS 2 和 webots_ros2 在 WSL 中运行。请根据上游教程配置 Webots 主机与 WSL 之间的连接，再启动 universal_robot 示例。
