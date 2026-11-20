.. redirect-from::

    DDS-and-ROS-middleware-implementations
    Concepts/About-Different-Middleware-Vendors

不同的 ROS 2 中间件供应商
=========================

.. contents:: 目录
   :local:

ROS 2 构建于 DDS/RTPS 中间件之上，该中间件提供发现、序列化和传输功能。`本文 <https://design.ros2.org/articles/ros_on_dds.html>`__ 详细解释了使用 DDS 实现和/或 DDS 的 RTPS 线协议的设计动机。简而言之，DDS 是一种端到端中间件，提供了与 ROS 系统密切相关的功能，例如分布式发现（不同于 ROS 1 的集中式发现），以及对不同传输服务质量（QoS）选项的控制。

`DDS <https://www.omg.org/omg-dds-portal>`__ 是一项行业标准，由多家供应商实现，例如 RTI 的 `Connext DDS <https://www.rti.com/products/>`__、eProsima 的 `Fast DDS <https://fast-dds.docs.eprosima.com/>`__、Eclipse 的 `Cyclone DDS <https://projects.eclipse.org/projects/iot.cyclonedds>`__，以及 GurumNetworks 的 `GurumDDS <https://gurum.cc/index_eng>`__。RTPS（也称为 `DDSI-RTPS <https://www.omg.org/spec/DDSI-RTPS/About-DDSI-RTPS/>`__）是 DDS 用于网络通信的线协议。

ROS 2 支持多种 DDS/RTPS 实现，因为选择中间件供应商或实现时，并不存在适用于所有场景的唯一方案。选择中间件实现时，需要考虑许多因素：例如许可证等部署因素，以及平台可用性、计算资源占用等技术因素。供应商可能会提供多种 DDS 或 RTPS 实现，以满足不同需求。例如，RTI 的 Connext 有多个不同用途的版本，其中一个专门面向微控制器，另一个面向需要特殊安全认证的应用（目前 ROS 2 只支持其标准桌面版本）。

要在 ROS 2 中使用 DDS/RTPS 实现，需要创建一个“ROS Middleware Interface”（ROS 中间件接口，简称 ``rmw``）功能包，通过 DDS 或 RTPS 实现提供的 API 和工具来实现 ROS 抽象中间件接口。实现和维护支持不同 DDS 实现的 RMW 功能包需要大量工作，但支持至少几种实现非常重要，这样 ROS 2 代码库就不会绑定到某一种特定实现，用户可以根据项目需求切换实现。

支持的 RMW 实现
---------------

.. list-table::
   :header-rows: 1

   * - 产品名称
     - 许可证
     - RMW 实现
     - 状态
   * - eProsima Fast DDS
     - Apache 2
     - ``rmw_fastrtps_cpp``
     - 完整支持；默认 RMW；随二进制发行包提供。
   * - Eclipse Cyclone DDS
     - Eclipse Public License v2.0
     - ``rmw_cyclonedds_cpp``
     - 完整支持；随二进制发行包提供。
   * - RTI Connext DDS
     - 商业、研究
     - ``rmw_connextdds``
     - 完整支持；二进制中包含支持，但需要单独安装 Connext。
   * - GurumNetworks GurumDDS
     - 商业
     - ``rmw_gurumdds_cpp``
     - 社区支持；二进制中包含支持，但需要单独安装 GurumDDS。

实际使用多种 RMW 实现的说明，请参阅 :doc:`使用多个 RMW 实现 <../../How-To-Guides/Working-with-multiple-RMW-implementations>`。

多个 RMW 实现
-------------

当前仍受支持的 ROS 2 发行版，其二进制发行包内置支持多种 RMW 实现，包括 Fast DDS、RTI Connext Pro、Eclipse Cyclone DDS 和 GurumNetworks GurumDDS。默认实现是 Fast DDS，因为它随二进制软件包一起分发，无需额外安装。

Cyclone DDS、Connext 或 GurumDDS 等其他 RMW 实现，可以通过 :doc:`安装额外软件包 <../../Installation/RMW-Implementations>` 启用，无需重新构建或替换已有软件包。

从源码构建的 ROS 2 工作空间可以同时构建并安装多个 RMW 实现。在编译 ROS 2 核心代码时，只要相关 DDS/RTPS 实现已正确安装，且配置了相应环境变量，构建系统就会构建检测到的 RMW 实现。例如，如果工作空间中包含 `RTI Connext DDS 的 RMW 功能包 <https://github.com/ros2/rmw_connextdds>`__，并且系统能够找到 RTI Connext Pro 安装，就会构建该功能包。

在许多情况下，使用不同 RMW 实现的节点能够互相通信，但并非所有情况下都可以。以下跨供应商通信配置不受支持：

* Fast DDS 与 Connext

  * Fast DDS 发布的 ``WString`` 在 macOS 上无法被 Connext 正确接收。

* Connext 与 Cyclone DDS

  * 不支持针对 ``WString`` 的发布/订阅通信。

默认 RMW 实现
-------------

如果 ROS 2 工作空间中安装了多个 RMW 实现，并且 Fast DDS 可用，则默认选择 Fast DDS。如果未安装 Fast DDS RMW 实现，则按字母顺序选择标识符最靠前的 RMW 实现。实现标识符就是提供该实现的 ROS 软件包名称，例如 ``rmw_cyclonedds_cpp``。

例如，如果同时安装了 ``rmw_cyclonedds_cpp`` 和 ``rmw_connextdds`` 软件包，则默认使用 ``rmw_connextdds``。如果安装了 ``rmw_fastrtps_cpp``，则默认使用 Fast DDS。

有关运行 ROS 2 示例时如何指定 RMW 实现，请参阅 :doc:`相关指南 <../../How-To-Guides/Working-with-multiple-RMW-implementations>`。

.. _different-middleware-vendors-cross-vendor-communication:

跨供应商通信
------------

不同 RMW 实现之间可能在有限情况下兼容，但不能保证始终兼容。因此，建议用户确保分布式系统中的所有部分都使用相同的 ROS 版本和相同的 RMW 实现。
