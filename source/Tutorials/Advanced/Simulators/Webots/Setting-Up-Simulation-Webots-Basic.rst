搭建机器人仿真（基础）
======================

**目标：** 搭建机器人仿真，并通过 ROS 2 控制机器人。

**教程级别：** 高级

**预计时间：** 30 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程将使用 Webots 机器人模拟器，搭建并运行一个简单的 ROS 2 仿真场景。

webots_ros2 软件包提供 ROS 2 与 Webots 之间的接口。本教程使用 webots_ros2_driver 子软件包，通过 Python 或 C++ 插件控制仿真机器人。其他子软件包包含不同机器人示例，例如 TurtleBot3。更多示例请参阅`Webots ROS 2 示例 <https://github.com/cyberbotics/webots_ros2/wiki/Examples>`_。

前置条件
--------

建议先了解 :doc:`初级教程 <../../../../Tutorials>` 中介绍的 ROS 基本概念，特别是 turtlesim、话题、工作空间、功能包和 Launch 文件教程。

.. tabs::

    .. group-tab:: Linux

        本教程中的 Linux 和 ROS 命令可以在标准 Linux 终端中运行。请先阅读 :doc:`Ubuntu 安装说明 <./Installation-Ubuntu>`，安装 webots_ros2。

    .. group-tab:: Windows

        本教程中的 Linux 和 ROS 命令必须在 WSL（Windows Subsystem for Linux）环境中运行。请先阅读 :doc:`Windows 安装说明 <./Installation-Windows>`。

    .. group-tab:: macOS

        本教程中的 Linux 和 ROS 命令必须在预先配置的 Linux 虚拟机（VM）中运行。请先阅读 :doc:`macOS 安装说明 <./Installation-MacOS>`。

本教程兼容 webots_ros2 2023.1.0 和 Webots R2023b，以及后续版本。

任务
----

1. 创建功能包结构
^^^^^^^^^^^^^^^^^

首先在自定义 ROS 2 功能包中组织代码。在 ROS 2 工作空间的 src 目录下创建名为 my_package 的新功能包，并将当前终端目录切换到 ros2_ws/src。

.. tabs::

    .. group-tab:: Python

        .. code-block:: console

            $ ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name my_robot_driver my_package --dependencies rclpy geometry_msgs webots_ros2_driver

        --node-name my_robot_driver 会在 my_package 子目录中创建 my_robot_driver.py Python 插件模板，稍后需要修改。--dependencies rclpy geometry_msgs webots_ros2_driver 会将插件所需依赖添加到 package.xml。

        在 my_package 目录中创建 launch 和 worlds 文件夹：

        .. code-block:: console

            $ cd my_package
            $ mkdir launch worlds

    .. group-tab:: C++

        .. code-block:: console

            $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 --node-name my_robot_driver my_package --dependencies rclcpp geometry_msgs webots_ros2_driver

        然后在 my_package 中创建 launch 和 worlds 目录。

2. 创建世界文件
^^^^^^^^^^^^^^^

在 worlds 目录中放置 Webots 世界文件。可以从 Webots 示例中选择一个简单世界，也可以使用 Webots 场景编辑器创建自己的世界。

3. 创建机器人描述和驱动插件
^^^^^^^^^^^^^^^^^^^^^^^^^^^

在机器人 URDF 中描述机器人模型，并使用 webots_ros2_driver 插件连接 Webots 设备与 ROS 2。插件可以通过 URDF 中的 ros2_control 或 device 配置加载。

4. 创建启动文件
^^^^^^^^^^^^^^^

在 launch 目录中创建 Python 启动文件，使用 WebotsLauncher 启动 Webots，并使用 WebotsController 启动机器人控制器。启动文件需要提供世界文件路径和机器人描述。

5. 构建并运行仿真
^^^^^^^^^^^^^^^^^

在工作空间根目录构建：

.. code-block:: console

    $ colcon build

source 工作空间后，通过 ros2 launch 启动自己的仿真启动文件。随后可以使用标准 ROS 2 话题与机器人交互。
