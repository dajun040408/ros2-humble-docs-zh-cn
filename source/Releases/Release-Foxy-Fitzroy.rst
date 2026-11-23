Foxy Fitzroy（foxy）
====================

.. contents:: 目录
   :depth: 2
   :local:

Foxy Fitzroy 是 ROS 2 的第六个发行版。

支持平台
--------

Foxy 根据`平台支持等级 <../The-ROS2-Project/Platform-Support-Tiers>`_ 支持以下平台。

Tier 1：

* Ubuntu 20.04（Focal）：amd64、arm64
* macOS 10.14（Mojave）
* Windows 10（Visual Studio 2019）

Tier 3：

* Ubuntu 20.04（Focal）：arm32
* Debian Buster（10）：amd64、arm64、arm32
* OpenEmbedded Thud（2.6）/ webOS OSE：arm32、x86

目标平台
--------

.. list-table::
   :header-rows: 1

   * - 架构
     - Ubuntu Focal
     - macOS Mojave
     - Windows 10
     - Debian Buster
     - OpenEmbedded / webOS OSE
   * - amd64
     - Tier 1
     - Tier 1
     - Tier 1
     - Tier 3
     -
   * - arm64
     - Tier 1
     -
     -
     - Tier 3
     - Tier 3
   * - arm32
     - Tier 3
     -
     -
     - Tier 3
     - Tier 3

中间件实现支持
--------------

* eProsima Fast-RTPS：默认实现。
* Eclipse Cyclone DDS：Tier 1。
* RTI Connext。
* Gurum DDS。

依赖项包管理器
--------------

* Ubuntu、Debian：apt
* macOS：Homebrew、pip
* Windows：Chocolatey、pip
* OpenEmbedded：opkg

构建系统支持
------------

* ament_cmake
* cmake
* setuptools

安装
----

请参阅`Foxy 安装说明 <../../foxy/Installation.html>`_。

本次发行版的新功能
------------------

Foxy 开发期间的高层任务和功能进度可参阅`Foxy meta-ticket <https://github.com/ros2/ros2/issues/830>`_。

补丁版本 8（2022-09-28）
-----------------------

Launch GroupAction 环境变量作用域
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SetEnvironmentVariable 操作现在会限制在其所属的 GroupAction 作用域中。

例如，启动文件先设置 my_env_var=1，再在 GroupAction 内设置 my_env_var=2。补丁版本 8 之前，节点 foo 会以 my_env_var=2 启动；现在它会以 my_env_var=1 启动。

如果希望退出新行为，可以在 GroupAction 上设置 scoped=False。

相关问题：

* `ros2#1244 <https://github.com/ros2/ros2/issues/1244>`_
* `launch#630 <https://github.com/ros2/launch/pull/630>`_

补丁版本 7（2022-02-08）
-----------------------

Launch set_env 前端行为变更
^^^^^^^^^^^^^^^^^^^^^^^^^^^

launch#468 曾意外改变前端启动文件中 set_env 操作的作用域。set_env 对环境变量的修改不再限制于父 group，而是全局生效。由于该变更被回移植，因此也影响 Foxy。本次变更被视为回归问题，计划在后续补丁版本中修复。
