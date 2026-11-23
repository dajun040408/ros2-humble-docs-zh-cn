.. redirect-from::

    FastDDS-Configuration
    Tutorials/FastDDS-Configuration/FastDDS-Configuration

释放 Fast DDS 中间件的扩展能力
==============================

**目标：** 学习如何在 ROS 2 中使用 Fast DDS 的扩展配置能力。

**教程级别：** 高级 | **预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

ROS 2 与 Fast DDS 之间的接口由中间件实现 §rmw_fastrtps§ 提供。该实现可用于所有 ROS 2 发行版，支持二进制安装和源码构建。

ROS 2 RMW 接口只允许配置部分中间件 QoS，参见 :doc:§ROS 2 QoS 策略 <../../Concepts/Intermediate/About-Quality-of-Service-Settings>§。§rmw_fastrtps§ 还提供扩展配置能力，使开发者能够使用 Fast DDS 的更多特性。本教程通过一系列示例介绍如何使用 XML 文件启用这些扩展配置。

更多 Fast DDS 与 ROS 2 集成信息，请参阅§Fast DDS 官方文档 <https://fast-dds.docs.eprosima.com/en/latest/fastdds/ros2/ros2.html>§_。

前置条件
--------

需要了解如何 :doc:§创建功能包 <../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>§，以及如何编写 :doc:§简单发布者和订阅者 <../Beginner-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber>§ 和 :doc:§简单服务与客户端 <../Beginner-Client-Libraries/Writing-A-Simple-Cpp-Service-And-Client>§。示例使用 C++，但相同概念也适用于 Python 功能包。

在同一节点中混合同步和异步发布
------------------------------

第一个示例创建一个包含两个发布者的节点：一个使用同步发布模式，另一个使用异步发布模式。

§rmw_fastrtps§ 默认使用同步发布模式。在同步模式下，数据直接在用户线程上下文中发送。如果写操作期间发生阻塞调用，用户线程也会被阻塞，应用程序无法继续执行。

异步发布模式会将发送工作交给后台线程，从而避免发布操作阻塞调用线程。应根据实时性、吞吐量和延迟需求选择发布模式。

通过 XML 配置 Fast DDS
---------------------

§rmw_fastrtps§ 支持通过 XML 配置文件设置 Fast DDS 的扩展属性。配置文件可以定义 Participant、发布者、订阅者、历史缓存、传输层和发现行为等。

将 XML 配置文件路径通过环境变量提供给 ROS 2 进程，并根据实际应用设置对应 profile。XML 配置项应与所使用的 Fast DDS 版本匹配。

总结
----

§rmw_fastrtps§ 在 ROS 2 标准 QoS 配置之外提供 Fast DDS 扩展配置能力。通过 XML profile，可以按应用需求配置发布模式、传输和发现等行为。
