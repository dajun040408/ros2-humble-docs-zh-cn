.. _First-steps-with-ROS-learning-path:

ROS 入门第一步——学习路径
=========================

ROS（Robot Operating System，机器人操作系统）是一个开源生态系统，提供用于构建、部署、运行和维护机器人应用的框架、工具及软件库。本页面通过一系列文章和动手实践活动介绍 ROS 框架的主要概念。完成这些内容后，你将掌握开始开发 ROS 应用所需的基础知识。

**领域：ROS 框架 | 内容类型：学习路径 | 经验水平：初学者**

.. contents:: 目录
   :depth: 2
   :local:

概述
----

ROS 框架提供了机器人不同组成部分之间通信所需的基础设施，包括消息传递机制、标准接口，以及对多种编程语言和平台的支持。

在使用 ROS 开发或维护应用之前，需要先理解框架的基本概念。turtlesim 工具和本站教程将帮助你快速入门。

前置条件
--------

无。本页面列出的步骤将指导你下载并安装学习 ROS 基础知识所需的全部内容。

学习步骤
--------

1. 了解 ROS 的基本概念
^^^^^^^^^^^^^^^^^^^^^^^

* :doc:`关于 ROS </About-ROS>`
* :doc:`ROS 2 节点 </Concepts/Basic/About-Nodes>`
* :doc:`话题、服务和动作接口 </Concepts/Basic/Interfaces-Topics-Services-Actions>`
* :doc:`参数 </Concepts/Basic/About-Parameters>`

2. 安装 ROS 和 turtlesim
^^^^^^^^^^^^^^^^^^^^^^^^

安装 ROS 时会包含使用 ROS 所需的基础软件包。如果你熟悉 Linux，我们推荐使用 Ubuntu（deb 软件包）作为平台。否则，也可以选择 Windows（二进制包）：:doc:`ROS 安装选项 </Installation>`。

turtlesim 是一款面向初学者的轻量级二维仿真工具。借助它，你可以在简单直观的可视化环境中学习 ROS 核心概念：:doc:`安装并配置 turtlesim </Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim>`。

3. 尝试使用 ROS 框架的主要通信组件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用 turtlesim 熟悉 ROS 框架的主要通信组件，并尝试消息传递。

#. 完成节点教程：:doc:`/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes`
#. 完成话题教程：:doc:`/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics`
#. 完成服务教程：:doc:`/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services`
#. 完成参数教程：:doc:`/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters`
#. 完成动作教程：:doc:`/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions`

4. 学习通过日志进行系统检查
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

系统检查（Introspection）能够帮助你了解系统的运行情况。节点可以通过日志以多种方式输出事件和状态信息。

要通过日志实践系统检查，请完成 rqt_console 教程：:doc:`/Tutorials/Beginner-CLI-Tools/Using-Rqt-Console/Using-Rqt-Console`。

5. 学习使用启动文件
^^^^^^^^^^^^^^^^^^^

启动文件允许你同时启动和配置多个包含 ROS 节点的进程，而不必打开多个终端，并为每个节点重复输入配置细节。

完成启动文件教程：:doc:`/Tutorials/Beginner-CLI-Tools/Launching-Multiple-Nodes/Launching-Multiple-Nodes`。

6. 学习数据录制与回放
^^^^^^^^^^^^^^^^^^^^^

有时需要回放数据，以便重现测试和实验结果、调试机器人行为，或与他人分享工作成果。

完成数据录制与回放教程：:doc:`/Tutorials/Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data`。

后续学习
--------

为了完整掌握 ROS 框架，建议进一步熟悉 ROS 客户端库：:doc:`/Tutorials/Beginner-Client-Libraries`。
