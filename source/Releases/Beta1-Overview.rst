.. redirect-from::

  Beta1-Overview

Beta 1（``Asphalt``）
===================

.. contents:: 目录
   :depth: 2
   :local:

支持的平台
----------

ROS 2 Beta 1 支持三个平台：Ubuntu 16.04（Xenial）、Mac OS X 10.11（El Capitan）以及 Windows 8.1 和 Windows 10。我们为这三个平台都提供二进制软件包和源码编译说明。

功能特性
--------

相较于 Alpha 8 版本的改进
^^^^^^^^^^^^^^^^^^^^^^^^^^

* 支持在编译时、链接时或运行时进行节点组合。
* 为受管理节点提供标准生命周期。
* 改进了服务质量（QoS）调优和测试支持。
* `新增和更新的设计文档 <https://design.ros2.org/>`_。
* 更多 :doc:`教程 <../../Tutorials>` 和 `示例 <https://github.com/ros2/examples>`_。
* 除话题外，还支持与 ROS 1 之间的服务桥接。

此前 Alpha 版本中的部分功能
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

完整列表请参阅 `早期发行说明 <../index>`_。

* ROS 2 客户端库的 C++ 和 Python 实现，包括以下 API：

  * 发布和订阅 ROS 话题。
  * 请求和响应 ROS 服务（同步方式仅支持 C++，同时支持异步方式）。
  * 获取和设置 ROS 参数（仅支持 C++，同时支持同步和异步方式）。
  * 定时器回调。
  * 支持多个 DDS/RTPS 实现之间的互操作。
  * eProsima Fast RTPS 是默认实现，并包含在二进制软件包中。
  * 支持 RTI Connext：可以通过源码构建进行体验。
  * 最初支持 PrismTech OpenSplice，但后来决定停止支持。

* 用于网络事件的计算图 API。
* 分布式发现机制。
* 与兼容 DDS 实现配合时，发布和订阅路径支持实时安全代码（当时仅支持 Connext）。

  * 支持自定义分配器。

* ROS 1 与 ROS 2 之间的动态桥接节点。
* C++ 执行器线程模型。
* 扩展 ``.msg`` 格式，增加以下功能：

  * 有界数组。
  * 默认值。

已知问题
^^^^^^^^

* 我们在多个代码仓库中跟踪问题，主要入口是 `ros2/ros2 Issue 跟踪系统 <https://github.com/ros2/ros2/issues>`_。
* 需要特别指出一个 `已知问题 <https://github.com/ros2/rmw_fastrtps/issues/81>`_：我们正与 eProsima 合作修复 FastRTPS 在处理大型消息时性能显著下降的问题。在运行使用较大图像分辨率的部分演示时，可以观察到这一问题。
