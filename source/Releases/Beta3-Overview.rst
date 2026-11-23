.. redirect-from::

  Beta3-Overview

Beta 3（`r2b3`）
===============

.. contents:: 目录
   :depth: 2
   :local:

支持的平台
----------

ROS 2 Beta 3 支持三个平台：Ubuntu 16.04（Xenial）、macOS 10.12（Sierra）和 Windows 10。我们为这三个平台都提供二进制软件包和源码编译说明，参见 :doc:`安装说明 <../../Installation>` 以及 `Beta 3 文档 <https://docs.ros2.org/beta3/>`_。

功能特性
--------

相较于 Beta 2 的改进
^^^^^^^^^^^^^^^^^^^^

* Python 执行模型得到改进，并修复了 Python C 扩展中的许多内存管理问题。
* 对 `ros_control <https://github.com/ros2/ros2_control>`_ 进行了实验性重写。
* 向用户公开 DDS 实现专用符号（Fast RTPS 和 Connext），参见`示例 <https://github.com/ros2/demos/blob/6363be2efe2fea799d92bc22a66e776b2ca9c5d0/demo_nodes_cpp_native/src/talker.cpp>`_。
* 在 Python 中提供日志 `API <https://github.com/ros2/rclpy/blob/1ef2924ef8e154c0553edf0fdba4840b08b728f8/rclpy/rclpy/logging.py>`_。
* 修复多个软件包中的内存泄漏和竞态条件。
* 重新加入 PrismTech 提供的 OpenSplice 支持（目前适用于 Linux 和 Windows）。
* 使用 Bloom（无需补丁）发布 ROS 2。

新增演示应用
^^^^^^^^^^^^

* `HSR 演示 <https://github.com/ruffsl/hsr_demo>`_：

  * 使用 ROS 2 手柄控制器远程控制 HSR 机器人。
  * 由于该机器人运行在 Ubuntu Trusty 上的 ROS 1，因此在 HSR 的 Docker 容器中运行 `ros1_bridge`。
  * 运行 ROS 2 开发版本的 `rviz <https://github.com/ros2/rviz>`_，可视化机器人的传感器数据等。参见`视频 <https://vimeo.com/237016358>`_。

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
  * PrismTech OpenSplice：请参阅下文的限制说明。

* 用于网络事件的计算图 API。
* 分布式发现机制。
* 与兼容 DDS 实现配合时，发布和订阅路径支持实时安全代码（当时仅支持 Connext）。

  * 支持自定义分配器。

* ROS 1 与 ROS 2 之间的动态桥接节点。
* C++ 和 Python 执行器线程模型。
* 在编译、链接或运行时组合节点的组件模型。
* 使用标准生命周期管理组件。
* 扩展 `.msg` 格式，增加以下功能：

  * 有界数组。
  * 默认值。

已知问题
--------

* 在 Windows 上，尝试使用 `Ctrl-C` 终止 Python 启动文件时，启动进程可能会挂起。参见`相关 Issue <https://github.com/ros2/launch/issues/64>`_。如果命令挂起并阻塞 Shell，可以使用进程监视器结束挂起的 Python 进程，以便继续使用该 Shell。
* macOS 目前不支持 OpenSplice。此外，`native handles` 访问功能尚未实现，参见`相关 Issue <https://github.com/ros2/rmw_opensplice/issues/182>`_。
* 使用 Connext 时，两个基础名称相同但命名空间不同的话题，目前不能使用不同的数据类型。参见`相关 Issue <https://github.com/ros2/rmw_connext/issues/234>`_。
