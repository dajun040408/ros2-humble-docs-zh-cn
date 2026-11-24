Webots 安装（macOS）
====================

**目标：** 在 macOS 上安装 ``webots_ros2`` 并运行仿真示例。

**教程级别：** 高级 | **预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

``webots_ros2`` 功能包提供 ROS 2 与 Webots 之间的接口，包含 ``webots_ros2_driver`` 等子功能包，用于启动 Webots 并与其通信。其他子功能包主要提供不同接口用法的示例。

前置条件
--------

建议了解 ROS 基本概念，尤其是 :doc:`创建工作空间 <../../../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace>` 和 :doc:`创建功能包 <../../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>`。

必须在 macOS 主机上原生安装 Webots，才能按本教程的方式从虚拟机中的 ROS 2 使用 ``webots_ros2``。可以按照`官方安装流程 <https://cyberbotics.com/doc/guide/installation-procedure>`_ 安装，也可以`从源码构建 <https://github.com/cyberbotics/webots/wiki/macOS-installation/>`_。

任务
----

在 macOS 上，一种较好的方案是使用 UTM 虚拟机运行 Linux 版 ROS 2，而 Webots 则原生安装在 macOS 主机上。这样 Webots 可以使用主机的 3D 硬件加速，同时 ROS 2 和 RViz 在 Linux 虚拟机中运行。

虚拟机通过 TCP 与 macOS 主机通信以启动 Webots。共享文件夹用于将虚拟机中的世界文件和资源传递给主机上的 Webots。

1. 创建虚拟机
^^^^^^^^^^^^^

在 macOS 上安装 UTM，下载 Ubuntu 22.04 ISO 镜像并创建 Linux 虚拟机。按照 UTM 的向导完成系统安装，并配置网络和共享目录。

2. 安装 ROS 2 和 webots_ros2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在虚拟机中安装 ROS 2，并安装 ``webots_ros2`` 发布软件包。也可以从源码构建 ``webots_ros2``。

3. 配置主机 Webots
^^^^^^^^^^^^^^^^^^

在 macOS 主机上安装 Webots，并确保虚拟机能够通过网络访问主机。配置共享目录，使虚拟机中的 ROS 2 启动文件能够将 Webots 世界文件和资源传递给主机。

4. 运行示例
^^^^^^^^^^^

在虚拟机中 source ROS 2 环境并启动 ``webots_ros2`` 示例。ROS 节点运行在 Linux 虚拟机中，Webots GUI 则运行在 macOS 主机上。

总结
----

macOS 上可以采用“主机原生运行 Webots、Linux 虚拟机运行 ROS 2”的方式使用 ``webots_ros2``，从而兼顾 macOS 图形加速和 Linux ROS 2 开发环境。
