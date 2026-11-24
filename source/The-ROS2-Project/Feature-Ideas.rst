.. redirect-from::

  Feature-Ideas

.. _FeatureIdeas:

功能特性构想
============

.. contents:: 目录
   :depth: 2
   :local:

以下按非特定顺序列出一些功能构想。这些功能被认为对 ROS 2 很重要，也适合作为社区贡献。

在着手开发新功能之前，:doc:`请先联系我们 <../Contact>`。我们可以提供指导，并帮助你联系其他开发者。

设计/概念
---------

* IDL 格式

  * 利用新特性，例如将常量分组到枚举中。
  * 扩展 ``.idl`` 文件的使用场景，使其只包含常量，和/或支持声明具有取值范围的参数。
  * 重新审视 IDL 接口命名约束，参见 `ros2/design#220 <https://github.com/ros2/design/pull/220>`_。

* 制定 ROS 1 到 ROS 2 的迁移计划。
* 节点名称唯一性，参见 `ros2/design#187 <https://github.com/ros2/design/issues/187>`_。
* 使用描述性格式定义节点的特定 API，例如话题、服务等，参见 `ros2/design#266 <https://github.com/ros2/design/pull/266>`_。

基础设施与工具
--------------

* 构建

  * 整合 <https://build.ros2.org>_ 和 <https://ci.ros2.org>_。
  * 提供 macOS 构建资源。
  * 提供 Windows 和 macOS 软件包。
  * 支持 `colcon` 配置文件。

* 文档

  * 弃用 <https://design.ros2.org>_。相关内容应迁移到 REP、<https://github.com/ros2/ros2_documentation>_，或删除。
  * 修复单软件包文档构建器，使其能够记录构建产物，例如消息、服务和动作。
  * 让 <https://docs.ros.org/en/ros2_documentation>_ 能够在 <https://github.com/ros2/ros2_documentation>_ 发生变更时自动重新构建。
  * 完善 ``ament`` 文档。
  * 添加 ROS 2 与 Jupyter Notebook 配合使用的文档示例。
  * 添加实现新 RMW 的文档。
  * 提供三种不同类型的内容：

    * **演示（demos）：** 展示功能，并通过测试覆盖这些功能。
    * **示例（examples）：** 展示简单、最小化的用法，同一任务可能有多种实现方式。
    * **教程（tutorials）：** 包含更多注释和 Wiki 锚点，讲解一种推荐的实现方式。

新功能
------

条目末尾的星号表示大致工作量：1 颗星为小型，2 颗星为中型，3 颗星为大型。

* 日志改进 ``[* / **]``

  * 通过文件指定配置。
  * 支持按 Logger 单独配置（例如启用 ``rqt_logger_level``）。

* 时间相关

  * 支持基于时钟的频率控制和休眠。

* 计算图 API 扩展 ``[** / ***]``

  * 查询所有话题（尤其是远程话题）的 QoS 设置。
  * 类似 ROS 1 Master API：<https://wiki.ros.org/ROS/Master_API>_。
  * 基于事件的通知。
  * 需要了解并扩展 RMW 接口。

* 执行器

  * 性能改进，主要集中在 waitset。
  * 确定性排序（公平调度）。
  * 解耦 waitable。

* 消息生成

  * 为默认不支持的语言补充消息生成能力。
  * 对消息字段名称进行重整，避免与特定语言的关键字冲突。
  * 通过在同一个 Python 解释器中运行生成器来提升生成性能。

* Launch

  * 支持启动多节点可执行程序（即手动组合）。
  * 扩展 Launch XML/YAML 支持：事件和事件处理器、标签命名空间及别名。

* Rosbag

  * 支持录制服务（以及动作）。

* ros1_bridge

  * 支持桥接动作。

* RMW 配置

  * 提供统一、标准化的中间件配置方式。

* 重映射 ``[** / ***]``

  * 通过 Service 接口实现动态重映射和别名。

* 类型伪装 ``[***]``

  * 类似 ROS 1 的消息 traits：<https://wiki.ros.org/roscpp/Overview/MessagesSerializationAndAdaptingTypes>_。
  * 需要了解 typesupport 系统。

* 扩展实时安全能力 ``[***]``

  * 覆盖服务、客户端和参数。
  * 暴露更多与实时性能相关的 QoS 参数。
  * 实时安全的进程内消息传递。

* 多机器人支持功能和演示 ``[***]``

  * 不希望所有机器人上的节点都共享同一个 Domain 并相互发现。
  * 设计系统分区机制。

* 支持更多 DDS/RTPS 实现：

  * RTI Connext DDS Micro（已实现，但默认未启用，也未获得官方支持）。

* 安全性改进：

  * 提供更细粒度的安全配置（例如仅启用身份验证，或同时启用身份验证和加密等）``[*]``。
  * 集成 DDS-Security 日志插件，以统一方式聚合安全事件，并通过 ROS 接口报告给用户 ``[**]``。
  * 密钥存储安全性改进（目前密钥直接存储在文件系统中）``[**]``。
  * 提供更易用的配置界面，简化安全配置。可以考虑 Qt GUI，也可以通过 GUI 辅助密钥分发 ``[***]``。
  * 提供一种机制，让用户可以对正在运行的系统执行“启用安全保护”操作，并自动为当前运行的所有节点生成密钥和策略 ``[***]``。
  * 如果存在用于保护密钥或加速消息加密/签名的硬件专用功能，也可以考虑将其集成到尚未支持这些功能的 DDS/RTPS 实现中。

减少技术债务
------------

* 修复 <https://ci.ros2.org/view/nightly>_ 中不稳定的测试。
* 支持使用 Valgrind、clang-tidy、Clang 静态分析（scan-build）、ASAN、TSAN、UBSAN 等工具运行（全部）单元测试。
* 审查 API，特别是 `rclcpp` 和 ``rclpy`` 中面向用户的 API。
* 将 `rclcpp` API 重构为多个职责单一的软件包，同时继续由 `rclcpp` 提供组合后的用户 API。
* 重新审视消息分配器，考虑使用 `std::pmr::polymorphic_allocator` 解决相关问题。
* 同步并协调 `设计文档 <https://design.ros2.org>`__ 与实际实现。
* 处理并分类尚未解决的 Issue。
* 处理代码和文档中的 TODO。
* 移除对 tinyxml 的依赖。
