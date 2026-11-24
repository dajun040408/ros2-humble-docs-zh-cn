.. redirect-from::

  Beta2-Overview

Beta 2（``r2b2``）
========================================

.. contents:: 目录
   :depth: 2
   :local:

支持的平台
----------

ROS 2 Beta 2 支持三个平台：Ubuntu 16.04（Xenial）、macOS 10.12（Sierra）和 Windows 10。我们为这三个平台都提供二进制软件包和源码编译说明，参见 :doc:`安装说明 <../../Installation>` 以及 `Beta 2 文档 <https://docs.ros2.org/beta2/>`_。

功能特性
--------

相较于 Beta 1 的改进
^^^^^^^^^^^^^^^^^^^^

* 支持 DDS_Security（也称为 SROS2，参见 `sros2 <https://github.com/ros2/sros2>`_）。
* 提供适用于 Ubuntu Xenial 的 Debian 软件包。
* 重新设计 Typesupport，使用户只需构建一个可执行程序，即可通过设置环境变量在可用的 RMW 实现之间进行选择。参见 :doc:`相关文档 <../../How-To-Guides/Working-with-multiple-RMW-implementations>`。
* 支持节点和话题的命名空间，参见 `设计文章 <https://design.ros2.org/articles/topic_and_service_names.html>`_。另请参阅下文已知问题。
* 提供一组使用可扩展 ``ros2`` 命令的命令行工具，参见 :doc:`概念说明 <../../Concepts/Basic/About-Command-Line-Tools>`。
* 提供一组用于在 C/C++ 中记录日志的宏，参见 `rcutils API 文档 <https://docs.ros2.org/beta2/api/rcutils/index.html>`_。

新增演示应用
^^^^^^^^^^^^

* `Turtlebot 2 演示 <https://github.com/ros2/turtlebot2_demo>`_：使用以下已经部分移植到 ROS 2 的仓库（仅 Linux）：

  * `ros_astra_camera <https://github.com/ros2/ros_astra_camera.git>`_
  * `depthimage_to_laserscan <https://github.com/ros2/depthimage_to_laserscan.git>`_
  * `pcl_conversions <https://github.com/ros2/pcl_conversions.git>`_
  * `cartographer <https://github.com/ros2/cartographer.git>`_
  * `cartographer_ros <https://github.com/ros2/cartographer_ros.git>`_
  * `ceres-solver <https://github.com/ros2/ceres-solver.git>`_
  * `navigation <https://github.com/ros2/navigation.git>`_
  * `teleop_twist_keyboard <https://github.com/ros2/teleop_twist_keyboard.git>`_
  * `joystick_drivers <https://github.com/ros2/joystick_drivers.git>`_
  * `teleop_twist_joy <https://github.com/ros2/teleop_twist_joy.git>`_

* `虚拟机器人演示 <../Tutorials/Demos/dummy-robot-demo>`：

  * `robot_model <https://github.com/ros2/robot_model>`_
  * `robot_state_publisher <https://github.com/ros2/robot_state_publisher>`_

此前 Alpha/Beta 版本中的部分功能
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

完整列表请参阅`早期发行说明 <../index>`_。

* ROS 2 客户端库的 C++ 和 Python 实现，包括以下 API：

  * 发布和订阅 ROS 话题。
  * 请求和响应 ROS 服务（C++ 仅支持同步方式，同时支持异步方式）。
  * 获取和设置 ROS 参数（仅支持 C++，同时支持同步和异步方式）。
  * 定时器回调。

* 支持多个 DDS/RTPS 实现之间的互操作：

  * eProsima Fast RTPS 是默认实现，并包含在二进制软件包中。
  * 支持 RTI Connext：可以通过源码构建进行体验。
  * 最初支持 PrismTech OpenSplice，但目前暂时停止支持。

* 用于网络事件的计算图 API。
* 分布式发现机制。
* 与兼容 DDS 实现配合时，发布和订阅路径支持实时安全代码（当时仅支持 Connext）。

  * 支持自定义分配器。

* ROS 1 与 ROS 2 之间的动态桥接节点。
* C++ 执行器线程模型。
* 在编译、链接或运行时组合节点的组件模型。
* 使用标准生命周期管理组件。
* 扩展 ``.msg`` 格式，增加以下功能：

  * 有界数组。
  * 默认值。

已知问题
^^^^^^^^

* 我们在多个代码仓库中跟踪问题，主要入口是 `ros2/ros2 Issue 跟踪系统 <https://github.com/ros2/ros2/issues>`_。
* 需要特别指出一个`已知问题 <https://github.com/ros2/rmw_connext/issues/234>`_：使用 ``rmw_connext_cpp`` 时，两个基础名称相同但命名空间不同的话题，不能使用不同的数据类型。
* Fast-RTPS 无法正常处理响应较长的服务。虽然修复尚未包含在 Beta 2 中，但上游已经提供了修复。因此，可以通过从 Fast-RTPS master 分支源码构建来绕过此问题。
