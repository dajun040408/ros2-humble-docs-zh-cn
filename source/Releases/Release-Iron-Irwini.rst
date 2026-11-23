.. _iron-release:

Iron Irwini（iron）
===================

.. toctree::
   :hidden:

   Iron-Irwini-Complete-Changelog

.. contents:: 目录
   :depth: 2
   :local:

Iron Irwini 是 ROS 2 的第九个发行版。本文列出相较 Humble 的重要变更和功能。完整变更请参阅`完整变更日志 <Iron-Irwini-Complete-Changelog>`_。

支持平台
--------

Iron 根据`平台支持等级 <../The-ROS2-Project/Platform-Support-Tiers>`_ 支持以下平台。

Tier 1：

* Ubuntu 22.04（Jammy）：amd64、arm64
* Windows 10（Visual Studio 2019）：amd64

Tier 2：

* RHEL 9：amd64

Tier 3：

* macOS：amd64
* Debian Bullseye：amd64
* OpenEmbedded / Yocto Project

目标平台
--------

.. list-table::
   :header-rows: 1

   * - 架构
     - Ubuntu Jammy
     - Windows 10
     - RHEL 9
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

* eProsima Fast-DDS：默认实现。
* Eclipse Cyclone DDS。
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

请参阅`Iron 安装说明 <../../iron/Installation.html>`_。

本次发行版的新功能
------------------

Python 功能包 API 文档生成
^^^^^^^^^^^^^^^^^^^^^^^^^^

此前 ROS 2 已经为 C++ 功能包自动生成 API 文档。Iron 开始支持自动生成 Python 功能包 API 文档。

更多信息请参阅`rosdoc2 相关 PR <https://github.com/ros-infrastructure/rosdoc2/pull/28>`_、`PR 49 <https://github.com/ros-infrastructure/rosdoc2/pull/49>`_、`PR 51 <https://github.com/ros-infrastructure/rosdoc2/pull/51>`_ 和 `PR 52 <https://github.com/ros-infrastructure/rosdoc2/pull/52>`_。

服务内省
^^^^^^^^

现在可以针对单个服务启用服务内省。启用后，用户可以查看与服务调用相关的元数据，包括客户端请求、服务端接收请求、服务端发送响应以及客户端接收响应等事件。也可以选择内省客户端和服务端请求/响应的具体内容。

所有信息都会发布到由服务名称生成的隐藏话题中。例如，服务名称为 /myservice 时，事件会发布到 /myservice/_service_event。

该功能默认禁用。创建服务客户端或服务端后，需要调用 configure_introspection 启用。示例请参阅`C++ 服务示例 <https://github.com/ros2/demos/tree/iron/demo_nodes_cpp/src/services>`_ 和`Python 服务示例 <https://github.com/ros2/demos/blob/iron/demo_nodes_py/demo_nodes_py/services/introspection.py>`_。

更多信息请参阅`REP 2012 <https://github.com/ros-infrastructure/rep/pull/360>`_ 和`跟踪问题 <https://github.com/ros2/ros2/issues/1285>`_。

参数设置前后回调
^^^^^^^^^^^^^^^^

此前，用户可以注册参数变更回调，检查外部实体（例如 ros2 param set）对节点参数的修改，并根据参数类型和值决定是否接受整个参数集合。

Iron 新增 pre 和 post 两种回调，执行顺序如下：

* pre 参数设置回调：可以根据任意条件修改参数列表。
* set 参数设置回调：不能修改参数列表，只能根据参数类型和值接受或拒绝参数。这是已有回调。
* post 参数设置回调：只有前两个回调均成功后才执行，可以据此修改节点状态。
