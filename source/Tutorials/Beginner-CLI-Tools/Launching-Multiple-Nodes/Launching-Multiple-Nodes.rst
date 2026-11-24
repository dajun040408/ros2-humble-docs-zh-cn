.. redirect-from::

    Tutorials/Launch/CLI-Intro

.. _ROS2Launch:

启动多个节点
============

**目标：** 使用命令行工具一次启动多个节点。

**教程级别：** 初级

**预计时间：** 5 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

在大多数入门教程中，每运行一个新节点都需要打开一个新终端。随着系统变得更加复杂，同时运行的节点越来越多，反复打开终端和重新输入配置会变得繁琐。

启动文件允许你同时启动和配置多个包含 ROS 2 节点的可执行程序。

使用 ros2 launch 运行一个启动文件，就可以一次启动整个系统，包括所有节点及其配置。

前置条件
--------

开始本教程之前，请按照 ROS 2 :doc:`安装说明 <../../../Installation/>` 安装 ROS 2。

本教程中的命令假设你按照操作系统对应的二进制软件包安装指南完成安装（Linux 使用 deb 软件包）。如果从源码构建，也可以继续学习，但环境设置文件的路径可能不同。从源码安装时，也不能使用 sudo apt install ros-<distro>-<package> 命令。

如果使用 Linux 且不熟悉 Shell，可以参考`Bash 入门教程 <https://www.linux.com/training-tutorials/bash-101-working-cli/>`_。

与往常一样，每次打开新终端时都要 source ROS 2 环境。

任务
----

运行启动文件
^^^^^^^^^^^^

打开一个新终端并运行：

.. code-block:: console

   $ ros2 launch turtlesim multisim.launch.py

该命令将运行以下启动文件：

.. literalinclude:: launch/multisim.launch.py
   :language: python

.. note::

  上面的启动文件使用 Python 编写，但也可以使用 XML 和 YAML 创建启动文件。不同 ROS 2 启动文件格式的比较，请参阅 :doc:`启动文件不同格式 <../../../How-To-Guides/Launch-file-different-formats>`。

该命令会运行两个 turtlesim 节点：

.. image:: images/turtlesim_multisim.png

现在暂时不必关心启动文件的具体内容。有关 ROS 2 launch 的更多信息，请参阅 :doc:`ROS 2 Launch 教程 <../../Intermediate/Launch/Launch-Main>`。

（可选）控制 Turtlesim 节点
^^^^^^^^^^^^^^^^^^^^^^^^^^^

这些节点启动后，可以像控制其他 ROS 2 节点一样控制它们。例如，打开另外两个终端，运行以下命令，让两只乌龟朝相反方向旋转。

第二个终端：

.. code-block:: console

   $ ros2 topic pub /turtlesim1/turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"

第三个终端：

.. code-block:: console

   $ ros2 topic pub /turtlesim2/turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: -1.8}}"

运行这些命令后，应该能看到类似下面的效果：

.. image:: images/turtlesim_multisim_spin.png

总结
----

到目前为止，你已经通过一条命令启动了两个 turtlesim 节点。学会编写自己的启动文件后，就可以使用 ros2 launch 以类似方式启动多个节点并设置其配置。

更多 ROS 2 启动文件教程，请参阅 :doc:`Launch 主教程页面 <../../Intermediate/Launch/Launch-Main>`。

下一步
------

下一篇教程 :doc:`录制和回放数据 <../Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data>` 将介绍另一个实用工具 ros2 bag。
