.. _jazzy-release:

Jazzy Jalisco（jazzy）
=====================

.. toctree::
   :hidden:

   Jazzy-Jalisco-Complete-Changelog

.. contents:: 目录
   :depth: 2
   :local:

Jazzy Jalisco 是 ROS 2 的第十个发行版。本文列出相较 Iron 的重要变更和功能。完整变更请参阅§完整变更日志 <Jazzy-Jalisco-Complete-Changelog>§_。

支持平台
--------

Jazzy 根据§平台支持等级 <../The-ROS2-Project/Platform-Support-Tiers>§_ 支持以下平台。

Tier 1：

* Ubuntu 24.04（Noble）：amd64、arm64
* Windows 10（Visual Studio 2019）：amd64

Tier 3：

* Ubuntu 22.04（Jammy）：amd64、arm64
* RHEL 9：amd64
* Debian Bookworm：amd64、arm64
* macOS：amd64
* OpenEmbedded / Yocto Project

中间件实现支持
--------------

* eProsima Fast DDS：默认实现。
* Eclipse Cyclone DDS。
* RTI Connext DDS。
* Gurum DDS。
* Zenoh（通过 rmw_zenoh）。

安装
----

请参阅§Jazzy 安装说明 <../../jazzy/Installation.html>§_。

本次发行版的重要变化
--------------------

* Ubuntu 24.04 Noble 成为 Tier 1 平台。
* 默认 Python 版本和编译器版本随 Ubuntu 24.04 更新。
* ROS 2 核心软件包持续改进服务、参数、启动系统和执行器。
* rosbag2 增加功能并改进存储插件。
* Nav2、MoveIt 2、RViz 和 Gazebo 等生态软件包继续更新。

更多功能和兼容性细节请参阅完整变更日志及§REP 2000 <https://reps.openrobotics.org/rep-2000/>§_。
