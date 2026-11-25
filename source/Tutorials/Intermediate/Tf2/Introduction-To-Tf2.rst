.. redirect-from::

    Tutorials/Tf2/Introduction-To-Tf2

.. _IntroToTf2:

tf2 简介
========

**目标：** 运行 turtlesim 演示，并通过多机器人示例了解 tf2 的功能。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

安装演示程序
------------

首先安装演示软件包及其依赖项。

.. tabs::

   .. group-tab:: Ubuntu 软件包

      .. code-block:: console

         $ sudo apt-get install ros-{DISTRO}-rviz2 ros-{DISTRO}-turtle-tf2-py ros-{DISTRO}-tf2-ros ros-{DISTRO}-tf2-tools ros-{DISTRO}-turtlesim

   .. group-tab:: RHEL 软件包

      .. code-block:: console

         $ sudo dnf install ros-{DISTRO}-rviz2 ros-{DISTRO}-turtle-tf2-py ros-{DISTRO}-tf2-ros ros-{DISTRO}-tf2-tools ros-{DISTRO}-turtlesim

   .. group-tab:: 源码安装

      .. code-block:: console

         $ git clone https://github.com/ros/geometry_tutorials.git -b ros2

运行演示
--------

安装 turtle_tf2_py 教程软件包后，就可以运行演示了。首先打开新终端并 :doc:`source ROS 2 安装环境 <../../Beginner-CLI-Tools/Configuring-ROS2-Environment>`，然后运行：

.. code-block:: console

   $ ros2 launch turtle_tf2_py turtle_tf2_demo.launch.py

你会看到 turtlesim 启动，并出现两只乌龟。

.. image:: images/turtlesim_follow1.png

在第二个终端中输入：

.. code-block:: console

   $ ros2 run turtlesim turtle_teleop_key

启动 turtlesim 后，可以使用键盘方向键控制中央的乌龟。选择第二个终端窗口，使键盘输入能够控制乌龟。

.. image:: images/turtlesim_follow2.png

你会看到另一只乌龟持续跟随你控制的乌龟移动。

发生了什么？
------------

该演示使用 tf2 库创建三个坐标系：world、turtle1 和 turtle2。教程使用 tf2 broadcaster 发布乌龟坐标系，并使用 tf2 listener 计算两个乌龟坐标系之间的差异，从而控制一只乌龟跟随另一只乌龟。

tf2 工具
--------

下面查看 tf2 如何实现该演示。可以使用 tf2_tools 检查 tf2 背后的工作过程。

1. 使用 view_frames
^^^^^^^^^^^^^^^^^^^

view_frames 会生成一张图，显示通过 ROS 由 tf2 广播的坐标系。注意，该工具目前仅适用于 Linux；Windows 用户可以跳到“使用 tf2_echo”。

.. code-block:: console

   $ ros2 run tf2_tools view_frames
   Listening to tf data during 5 seconds...
   Generating graph in frames.pdf file...

tf2 listener 会监听通过 ROS 广播的坐标系，并绘制它们之间的树状关系。使用 PDF 阅读器打开生成的 frames.pdf，即可查看坐标系树。

.. image:: images/turtlesim_frames.png

可以看到 tf2 广播的三个坐标系：world、turtle1 和 turtle2。world 是 turtle1 和 turtle2 的父坐标系。

view_frames 还会报告诊断信息，例如收到最早和最新坐标变换的时间，以及 tf2 坐标变换的发布频率，便于调试。

2. 使用 tf2_echo
^^^^^^^^^^^^^^^^

tf2_echo 会报告 ROS 中广播的任意两个坐标系之间的变换。

用法：

.. code-block:: console

   $ ros2 run tf2_ros tf2_echo [source_frame] [target_frame]

例如，查看 turtle2 坐标系相对于 turtle1 坐标系的变换：

.. code-block:: console

   $ ros2 run tf2_ros tf2_echo turtle2 turtle1

输出包含平移、四元数旋转、RPY 旋转角度以及变换矩阵。

2. 使用 tf2_echo
^^^^^^^^^^^^^^^^

``tf2_echo`` 会报告通过 ROS 广播的任意两个坐标系之间的变换。

用法：

.. code-block:: console

   $ ros2 run tf2_ros tf2_echo [source_frame] [target_frame]

例如，查看 ``turtle2`` 坐标系相对于 ``turtle1`` 坐标系的变换：

.. code-block:: console

   $ ros2 run tf2_ros tf2_echo turtle2 turtle1
   At time 1683385337.850619099
   - Translation: [2.157, 0.901, 0.000]
   - Rotation: in Quaternion [0.000, 0.000, 0.172, 0.985]
   - Rotation: in RPY (radian) [0.000, -0.000, 0.345]
   - Rotation: in RPY (degree) [0.000, -0.000, 19.760]
   - Matrix:
     0.941 -0.338  0.000  2.157
     0.338  0.941  0.000  0.901
     0.000  0.000  1.000  0.000
     0.000  0.000  0.000  1.000

``tf2_echo`` 会显示监听器从 ROS 2 接收到的坐标变换。控制海龟移动时，可以看到两只海龟之间的相对变换随之变化。

rviz2 和 tf2
------------

``rviz2`` 是用于检查 tf2 坐标系的可视化工具。可以使用 ``-d`` 选项指定配置文件启动 RViz，从而查看海龟坐标系：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ ros2 run rviz2 rviz2 -d $(ros2 pkg prefix --share turtle_tf2_py)/rviz/turtle_rviz.rviz

  .. group-tab:: Windows

    .. code-block:: console

       $ for /f "usebackq tokens=*" %a in (`ros2 pkg prefix --share turtle_tf2_py`) do rviz2 -d %a/rviz/turtle_rviz.rviz

.. image:: images/turtlesim_rviz.png

在左侧面板中可以看到 tf2 广播的坐标系。控制海龟移动时，可以看到 RViz 中的坐标系也随之移动。

总结
----

本教程通过 turtlesim 演示介绍了 tf2 的基本功能，并使用 view_frames 和 tf2_echo 检查坐标变换。
