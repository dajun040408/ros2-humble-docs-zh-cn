Eloquent Elusor（eloquent）
===========================

.. contents:: 目录
   :depth: 2
   :local:

Eloquent Elusor 是 ROS 2 的第五个发行版。

支持平台
--------

Eloquent 根据`平台支持等级 <../The-ROS2-Project/Platform-Support-Tiers>`_ 支持以下平台。

Tier 1：

* Ubuntu 18.04（Bionic）：amd64、arm64
* macOS 10.14（Mojave）
* Windows 10（Visual Studio 2019）

Tier 2：

* Ubuntu 18.04（Bionic）：arm32

Tier 3：

* Debian Stretch（9）：amd64、arm64、arm32
* OpenEmbedded Thud（2.6）/ webOS OSE：arm32、x86

目标平台
--------

.. list-table::
   :header-rows: 1

   * - 架构
     - Ubuntu Bionic
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
     - Tier 2
     -
     -
     - Tier 3
     - Tier 3

中间件实现支持
--------------

* eProsima Fast-RTPS：默认实现。
* RTI Connext。
* Eclipse Cyclone DDS：Tier 2。
* ADLINK OpenSplice。

依赖项与构建系统
----------------

依赖项包管理器：

* Ubuntu、Debian：apt
* macOS：Homebrew、pip
* Windows：Chocolatey、pip
* OpenEmbedded：opkg

构建系统支持：

* ament_cmake
* cmake
* setuptools

安装
----

请参阅`Eloquent 安装说明 <../../eloquent/Installation.html>`_。

本次发行版的新功能
------------------

* 支持基于标记语言的启动文件（XML/YAML）。
* 改进基于 launch 的测试。
* 命令行支持传递键值形式的参数。
* 支持 stream logging 宏。
* 支持按节点记录日志，节点的 stdout/stderr 输出会保存到 ~/.ros。
* 引入 ros2doctor。
* 改进环境设置文件的 source 性能。
* RViz 增加交互标记、扭矩环和 TF message filters。
* RQt 增加参数插件、TF 树插件和机器人转向插件。
* 改进 turtlesim。
* RMW 支持借用消息（loaned message），为零拷贝传输提供基础。
* 新增 Tier 2 中间件实现 rmw_cyclonedds。
* 增加 ROS_LOCALHOST_ONLY 环境变量，用于限制通信仅在 localhost 上进行。
* 支持 macOS Mojave。
* 为 rcl 和 rclcpp 增加 tracing 插桩。

更多信息请参阅`Eloquent meta ticket <https://github.com/ros2/ros2/issues/734>`_。

自 Dashing 以来的变更
---------------------

geometry_msgs
^^^^^^^^^^^^^

geometry_msgs/msg/Quaternion.msg 现在会默认初始化为有效四元数：

.. math::

    x = 0 \
    y = 0 \
    z = 0 \
    w = 1
