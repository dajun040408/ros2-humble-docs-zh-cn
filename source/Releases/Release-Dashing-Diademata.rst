Dashing Diademata（dashing）
===========================

.. contents:: 目录
   :depth: 2
   :local:

Dashing Diademata 是 ROS 2 的第四个发行版。

支持平台
--------

Dashing 根据`平台支持等级 <../The-ROS2-Project/Platform-Support-Tiers>`_ 支持以下平台。

Tier 1：

* Ubuntu 18.04（Bionic）：amd64、arm64
* macOS 10.12（Sierra）
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
     - macOS Sierra
     - Windows 10
     - Debian Stretch
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

交付方式说明：

* Debian 软件包：向 rosdistro 提交的软件包会在对应平台提供 Debian 包。
* 二进制归档包：每个平台提供一个归档包，包含 Dashing ROS 2 repos 文件中的所有软件包。
* 源码编译：可从源码构建。

中间件实现支持
--------------

* rmw_fastrtps_cpp：eProsima Fast-RTPS，Tier 1。
* rmw_connext_cpp：RTI Connext。
* rmw_opensplice_cpp：ADLINK OpenSplice。

依赖项与构建系统
----------------

依赖项版本表仅记录首次发布时的最低版本，不会随发行版生命周期内的依赖升级而更新。

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

请参阅`Dashing 安装说明 <../../dashing/Installation.html>`_。

本次发行版的新功能
------------------

* 组件（Components）成为推荐的节点开发方式。组件既可以独立运行，也可以组合在同一进程中，并且 launch 文件同时支持这两种方式。
* 改进 C++ 进程内通信，降低延迟并减少数据复制。
* Python 客户端库进一步对齐 C++ API，并改进内存使用和性能。
* 参数功能现在可以完整替代 ROS 1 的 dynamic_reconfigure，包括范围约束和只读属性。
* 消息生成流程开始依赖 IDL 4.2 的部分功能，除了 .msg、.srv 和 .action，还可以使用 .idl 文件。
* 支持普通字符串的可选 UTF-8 编码，以及 UTF-16 多字节字符串。
* 增加 actions 和 components 相关命令行工具。
* 支持 Deadline、Lifespan 和 Liveliness QoS 策略。
* MoveIt 2 发布 Alpha 版本。

更多信息请参阅`Dashing meta ticket <https://github.com/ros2/ros2/issues/607>`_。

自 Crystal 以来的变更
---------------------

参数声明
^^^^^^^^

从 Dashing 开始，参数必须先声明，然后才能访问或设置。

在 Dashing 之前，可以直接调用 get_parameter(name)，如果参数此前已设置就返回其值，否则返回 PARAMETER_NOT_SET。也可以在任何时候调用 set_parameter(name, value)，即使参数尚未声明。

从 Dashing 开始，如果尝试获取或设置未声明的参数，将抛出 ParameterNotDeclaredException 等异常，或返回失败结果。

