.. _galactic-release:

Galactic Geochelone（galactic）
===============================

.. toctree::
   :hidden:

   Galactic-Geochelone-Complete-Changelog

.. contents:: 目录
   :depth: 2
   :local:

Galactic Geochelone 是 ROS 2 的第七个发行版。本文列出相较上一发行版的重要变更和功能。自 Foxy 以来的全部变更，请参阅`完整变更日志 <Galactic-Geochelone-Complete-Changelog>`_。

支持平台
--------

Galactic 根据`平台支持等级 <../The-ROS2-Project/Platform-Support-Tiers>`_ 支持以下平台。

Tier 1：

* Ubuntu 20.04（Focal）：amd64、arm64
* Windows 10（Visual Studio 2019）：amd64

Tier 2：

* RHEL 8：amd64

Tier 3：

* Ubuntu 20.04（Focal）：arm32
* Debian Bullseye（11）：amd64、arm64、arm32
* OpenEmbedded Thud（2.6）/ webOS OSE：arm32、arm64
* macOS 10.14（Mojave）：amd64

目标平台
--------

.. list-table::
   :header-rows: 1

   * - 架构
     - Ubuntu Focal
     - Windows 10
     - RHEL 8
     - macOS
     - Debian Bullseye
     - OpenEmbedded / webOS OSE
   * - amd64
     - Tier 1
     - Tier 1
     - Tier 2
     - Tier 3
     - Tier 3
     -
   * - arm64
     - Tier 1
     -
     -
     -
     - Tier 3
     - Tier 3
   * - arm32
     - Tier 3
     -
     -
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

请参阅`Galactic 安装说明 <../../galactic/Installation.html>`_。

本次发行版的新功能
------------------

按 Logger 设置日志级别
^^^^^^^^^^^^^^^^^^^^^^

现在可以在命令行中为不同 Logger 指定不同日志级别：

.. code-block:: console

   $ ros2 run demo_nodes_cpp talker --ros-args --log-level WARN --log-level talker:=DEBUG

上面的命令将全局日志级别设置为 WARN，但将 talker 节点日志级别设置为 DEBUG。--log-level 命令行选项可以多次传入，为每个 Logger 设置不同级别。

通过环境变量配置日志目录
^^^^^^^^^^^^^^^^^^^^^^^^

现在可以通过 ROS_LOG_DIR 和 ROS_HOME 两个环境变量配置日志目录：

* 如果 ROS_LOG_DIR 已设置且非空，则使用 ROS_LOG_DIR。
* 否则使用 ROS_HOME/log；如果 ROS_HOME 未设置或为空，则使用 ~/.ros/log。

因此默认目录保持不变：~/.ros/log。

例如：

.. code-block:: bash

  ROS_LOG_DIR=/tmp/foo ros2 run demo_nodes_cpp talker

会将所有日志保存到 /tmp/foo。

.. code-block:: bash

  ROS_HOME=/path/to/home ros2 run demo_nodes_cpp talker

会将所有日志保存到 /path/to/home/log。

在 CMake 之外调用 rosidl 流程
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

现在可以在 CMake 之外直接调用 rosidl 接口生成流程。源代码生成器和接口定义转换器可通过统一命令行接口访问。
