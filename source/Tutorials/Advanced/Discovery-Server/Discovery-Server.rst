.. redirect-from::

    Discovery-Server
    Tutorials/Discovery-Server/Discovery-Server

使用 Fast DDS Discovery Server 作为发现协议
===========================================

**目标：** 学习如何使用 Fast DDS Discovery Server 发现 ROS 2 节点。

**教程级别：** 高级 | **预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

从 ROS 2 Eloquent 开始，Fast DDS 提供 Discovery Server 协议，作为默认 DDS 分布式发现机制的替代方案。本教程介绍如何使用 Discovery Server 运行 ROS 2 示例。

默认的 Simple Discovery Protocol 是 DDS 标准定义的发现协议，但在某些场景下存在不足：

* **扩展性问题：** 随着节点数量增加，节点之间交换的数据包数量会显著增长。
* **依赖组播：** 需要网络支持 multicast，在 Wi-Fi 等网络环境中可能无法可靠工作。

Fast DDS Discovery Server 使用客户端-服务器架构。每个 ROS 2 节点作为发现客户端，将自身信息发送给一个或多个发现服务器，并从服务器接收其他节点的发现信息。这样可以减少发现流量，也不再要求网络支持组播。

.. image:: figures/ds_explanation.svg
    :align: center

多个发现服务器可以独立运行、复制或互相连接，以提供网络冗余，避免单点故障。

Fast DDS Discovery Server v2
----------------------------

Fast DDS Discovery Server v2 增加了过滤功能，可以进一步减少发现消息。服务器会根据不同节点发布和订阅的话题，判断两个节点是否可能通信，从而避免不必要的匹配和发现消息。

.. image:: figures/ds1vs2.svg
    :align: center

这种架构能够显著减少服务器与客户端之间的消息数量。有关 Discovery Server v2 的性能数据，请参阅§官方文档 <https://fast-dds.docs.eprosima.com/en/v2.1.0/fastdds/discovery/discovery_server.html#discovery-server>§_。

配置发现服务器
--------------

可以通过 Participant XML 配置发现服务器，也可以使用 §fastdds§ 命令行工具和环境变量。本教程采用环境变量方式。详细配置请参阅§Fast DDS Discovery Server 文档 <https://fast-dds.docs.eprosima.com/en/v2.1.0/fastdds/discovery/discovery_server.html#discovery-server>§_。

前置条件
--------

本教程要求 ROS 2 Foxy 或更新版本。低于 Foxy 的版本可能没有 §fastdds§ 命令行工具。此时可以升级 Fast DDS 版本，或使用 Fast DDS XML QoS 配置来设置 Discovery Server。

运行教程
--------

§talker-listener§ ROS 2 示例会创建一个 §talker§ 节点，每秒发布一条 “hello world” 消息，以及一个订阅这些消息的 §listener§ 节点。

source ROS 2 环境后，可以使用 §fastdds§ 命令行工具配置发现服务器。配置客户端和服务器后，分别启动 talker 和 listener，即可验证通过 Discovery Server 完成节点发现和消息通信。

总结
----

Fast DDS Discovery Server 使用集中式客户端-服务器架构替代默认分布式发现机制，可降低发现流量，并避免对组播的依赖。多服务器配置还可以提供冗余能力。
