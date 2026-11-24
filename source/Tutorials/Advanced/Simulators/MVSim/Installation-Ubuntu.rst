在 Ubuntu 上安装 MVSim
======================

**目标：** 在 Ubuntu 上安装 ``mvsim`` 软件包，并验证其是否正常工作。

**教程级别：** 高级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景知识
--------

`MVSim <https://mvsimulator.readthedocs.io/>`__ （MultiVehicle Simulator，多车辆仿真器）是一款轻量级开源移动机器人仿真器。它提供基于物理的二维仿真和三维可视化，支持差速驱动与阿克曼转向车辆、多种传感器类型（激光雷达、摄像头、IMU、GPS），并通过标准消息类型原生集成 ROS 2。

MVSim 使用 BSD 3-Clause 许可证。

前置条件
--------

建议先了解初学者 :doc:`教程 <../../../../Tutorials>`` 中介绍的 ROS 基础概念。特别建议先完成 :doc:``创建工作空间 <../../../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace>`。

你需要有一个可正常工作的 ROS 2 安装环境。如有需要，请按照 :doc:`ROS 2 安装说明 <../../../../Installation>` 操作。

任务
----

1 安装 ``mvsim``
^^^^^^^^^^^^^^

你可以安装已发布的二进制软件包，也可以从源码构建。

.. tabs::

    .. group-tab:: 从 ROS 二进制软件包安装

        在终端中运行：

        .. code-block:: console

            $ sudo apt install ros-{DISTRO}-mvsim

    .. group-tab:: 从源码构建

        如果尚未创建 ROS 2 工作空间，请先创建：

        .. code-block:: console

            $ mkdir -p ~/ros2_ws/src

        source ROS 2 环境：

        .. code-block:: console

            $ source /opt/ros/{DISTRO}/setup.bash

        克隆 MVSim 仓库：

        .. code-block:: console

            $ cd ~/ros2_ws/src
            $ git clone https://github.com/MRPT/mvsim.git --recursive

        使用 ``rosdep`` 安装依赖项：

        .. code-block:: console

            $ cd ~/ros2_ws
            $ rosdep install --from-paths src --ignore-src -r -y

        构建软件包：

        .. code-block:: console

            $ colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release

        source 工作空间：

        .. code-block:: console

            $ source install/setup.bash

2 验证安装
^^^^^^^^^^

检查 ``mvsim`` 命令行工具是否可用：

.. code-block:: console

    $ mvsim --version

终端应打印已安装的版本号。

.. warning::

   ``mvsim`` 软件包提供两个可执行程序：

   - ``mvsim``：独立运行仿真器的主要命令行工具。
   - ``mvsim_node``：ROS 2 节点封装，用于运行仿真器并将其连接到其他 ROS 2 节点。

3 启动演示
^^^^^^^^^^

要快速验证所有功能是否正常，可以通过 ROS 2 启动仓库演示：

.. code-block:: console

    $ ros2 launch mvsim demo_warehouse.launch.py

你应该会看到 MVSim GUI 窗口打开，并显示仓库环境中的 Jackal 机器人。可以使用键盘上的 W/A/S/D 键控制机器人。

总结
----

你已经安装了 MVSim，并通过启动演示场景验证其能够正常运行。下一篇教程将介绍如何启动不同的演示场景，以及如何通过 ROS 2 话题与其交互。
