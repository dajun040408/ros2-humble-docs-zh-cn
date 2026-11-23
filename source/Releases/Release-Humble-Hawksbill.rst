.. _humble-release:

Humble Hawksbill（humble）
==========================

.. toctree::
   :hidden:

   Humble-Hawksbill-Complete-Changelog

.. contents:: 目录
   :depth: 2
   :local:

Humble Hawksbill 是 ROS 2 的第八个发行版。本文列出相较 Galactic 的重要变更和功能。所有变更请参阅`完整变更日志 <Humble-Hawksbill-Complete-Changelog>`_。

支持平台
--------

Humble 根据`平台支持等级 <../The-ROS2-Project/Platform-Support-Tiers>`_ 支持以下平台。

Tier 1：

* Ubuntu 22.04（Jammy）：amd64、arm64
* Windows 10（Visual Studio 2019）：amd64

Tier 2：

* RHEL 8：amd64

Tier 3：

* Ubuntu 20.04（Focal）：amd64
* macOS：amd64
* Debian Bullseye：amd64
* OpenEmbedded / Yocto Project：依目标配置而定

目标平台
--------

.. list-table::
   :header-rows: 1

   * - 架构
     - Ubuntu Jammy
     - Windows 10
     - RHEL 8
     - Ubuntu Focal
     - macOS
     - Debian Bullseye
     - OpenEmbedded / Yocto
   * - amd64
     - Tier 1
     - Tier 1
     - Tier 2
     - Tier 3
     - Tier 3
     - Tier 3
     - Tier 3
   * - arm64
     - Tier 1
     -
     -
     - Tier 3
     -
     - Tier 3
     - Tier 3
   * - arm32
     - Tier 3
     -
     -
     - Tier 3
     -
     - Tier 3
     - Tier 3

中间件实现支持
--------------

* Eclipse Cyclone DDS：默认实现。
* eProsima Fast-DDS。
* RTI Connext DDS。
* Gurum DDS。

依赖项包管理器
--------------

* Ubuntu、Debian：apt
* Windows：Chocolatey、pip
* macOS：Homebrew、pip
* RHEL：dnf
* OpenEmbedded：opkg

构建系统支持
------------

* ament_cmake
* cmake
* setuptools

安装
----

请参阅`Humble 安装说明 <../../humble/Installation.html>`_。

补丁版本 1（2022-11-23）
-----------------------

ros2topic
^^^^^^^^^

ros2 topic pub 现在允许使用 now 关键字将 builtin_interfaces.msg.Time 设置为当前时间。类似地，std_msgs.msg.Header 可以通过 auto 关键字自动生成。这与 ROS 1 rostopic 的行为一致。

相关 PR：`ros2/ros2cli#751 <https://github.com/ros2/ros2cli/pull/751>`_。

本次发行版的新功能
------------------

ament_cmake_gen_version_h
^^^^^^^^^^^^^^^^^^^^^^^^^

ament_cmake_gen_version_h 新增 CMake 函数，用于生成包含功能包版本信息的 C/C++ 头文件。详情请参阅`ament/ament_cmake#377 <https://github.com/ament/ament_cmake/pull/377>`_。
