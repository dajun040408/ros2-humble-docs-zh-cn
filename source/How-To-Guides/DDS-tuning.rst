.. redirect-from::

  Guides/DDS-tuning
  Troubleshooting/DDS-tuning

DDS 调优指南
============

本页面提供一些参数调优建议。这些建议曾用于解决 Linux 系统上使用不同 DDS 实现时，在真实场景中遇到的问题。我们在 Linux 或某个供应商实现上发现的问题，也可能出现在其他平台和供应商实现中。

以下建议仅作为调优起点。它们在特定系统和环境中有效，但实际调优结果会受到多种因素影响。调试时可能需要根据消息大小、网络拓扑等因素增大或减小参数值。

需要注意，调优参数可能会消耗额外资源，并影响系统中目标改进范围以外的其他部分。应针对每个具体场景，权衡可靠性提升带来的收益与可能产生的负面影响。

.. _cross-vendor-tuning:

跨供应商通用调优
----------------

**问题：** 通过容易丢包的网络（通常是 Wi-Fi）发送数据时，如果部分 IP 分片丢失，接收端内核缓冲区可能被占满，从而导致通信出现问题。

当一个 UDP 数据包至少有一个 IP 分片丢失时，其余已接收的分片会占用内核缓冲区。默认情况下，Linux 内核会等待 30 秒尝试重新组合这些分片。在此期间，内核缓冲区（默认大小为 256 KB）可能被占满，无法接收新的分片，因此连接看起来会长时间“卡住”。

该问题与 DDS 供应商无关，因此解决方法是调整内核参数。

**解决方案：** 使用 Best Effort QoS，而不是 Reliable QoS。

Best Effort 设置可以减少网络流量，因为 DDS 实现不需要承担可靠通信的额外开销。Reliable 通信要求发布者等待订阅者确认消息，并重新发送未被正确接收的样本。

不过，如果 IP 分片缓冲区已经占满，仍然可能出现 30 秒阻塞。因此，该方法可以在不调整参数的情况下缓解问题，但无法彻底解决。

**解决方案：** 减小 ``ipfrag_time`` 参数。

``net.ipv4.ipfrag_time`（路径：``/proc/sys/net/ipv4/ipfrag_time`，默认值：30 秒）表示 IP 分片在内存中保留的时间。

例如，将其减小到 3 秒：

.. code-block:: console

    $ sudo sysctl net.ipv4.ipfrag_time=3

减小该参数可以缩短没有收到完整分片时的等待窗口。该参数对所有传入分片全局生效，因此需要结合具体环境评估是否适合减小。

**解决方案：** 增大 ``ipfrag_high_thresh`` 参数。

``net.ipv4.ipfrag_high_thresh`（路径：``/proc/sys/net/ipv4/ipfrag_high_thresh`，默认值：262144 字节）表示用于重组 IP 分片的最大内存量。

例如，将其增加到 128 MB：

.. code-block:: console

    $ sudo sysctl net.ipv4.ipfrag_high_thresh=134217728     # 128 MB

显著增大该参数，是为了尽量避免缓冲区被完全占满。不过，如果假设每个 UDP 数据包都缺少一个分片，那么要容纳 ``ipfrag_time`` 时间窗口内收到的所有数据，可能需要设置非常大的值。

**问题：** 发送包含大型可变长度非原始类型数组的自定义消息时，会产生较高的序列化/反序列化开销和 CPU 负载。这可能导致 ``publish()`` 花费过多时间，使发布者停滞，并使 ``ros2 topic hz`` 低估实际接收频率。

例如，``builtin_interfaces/Time`` 也被视为非原始类型，会产生更高的序列化开销。因此，将 ROS 1 自定义消息类型直接迁移到 ROS 2 时，如果不考虑这一点，可能会出现明显的性能下降。

**解决方法：** 使用多个原始类型数组替代单个自定义类型数组，或者像 ``PointCloud2`` 消息那样打包到字节数组中。

例如，不要将 ``FooArray`` 定义为：

.. code-block:: text

    Foo[] my_large_array

其中 ``Foo`` 定义为：

.. code-block:: text

    uint64 foo_1
    uint32 foo_2

而应将 ``FooArray`` 定义为：

.. code-block:: text

    uint64[] foo_1_array
    uint32[] foo_2_array

Fast RTPS 调优
--------------

**问题：** Fast RTPS 在 Wi-Fi 网络中运行时，如果发送大型数据或高频数据，可能会产生大量网络流量。

请参阅 :ref:`跨供应商通用调优 <cross-vendor-tuning>` 中的解决方案。

.. _cyclonedds-tuning:

Cyclone DDS 调优
----------------

**问题：** 即使使用 Reliable 设置并通过有线网络传输，Cyclone DDS 仍无法可靠传递大型消息。

该问题预计会在 `后续版本中解决 <https://github.com/eclipse-cyclonedds/cyclonedds/issues/484>`_。在此之前，我们通过 `测试程序 <https://github.com/jacobperron/pc_pipe>`_ 调试并提出以下解决方案。

**解决方案：** 增大 Linux 内核最大接收缓冲区大小，以及 Cyclone 请求的最小套接字接收缓冲区大小。

针对 9 MB 消息的调整方式：

运行以下命令设置最大接收缓冲区 ``rmem_max``：

.. code-block:: console

    $ sudo sysctl -w net.core.rmem_max=2147483647

也可以编辑 ``/etc/sysctl.d/10-cyclone-max.conf`` 文件，永久设置：

.. code-block:: bash

    net.core.rmem_max=2147483647

接下来，创建 Cyclone 启动时使用的配置文件，以设置 Cyclone 请求的最小套接字接收缓冲区大小：

.. code-block:: xml

  <?xml version="1.0" encoding="UTF-8" ?>
  <CycloneDDS xmlns="https://cdds.io/config" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://cdds.io/config
  https://raw.githubusercontent.com/eclipse-cyclonedds/cyclonedds/master/etc/cyclonedds.xsd">
      <Domain id="any">
          <Internal>
              <SocketReceiveBufferSize min="10MB"/>
          </Internal>
      </Domain>
  </CycloneDDS>

之后，每次启动节点时设置以下环境变量：

.. code-block:: bash

    CYCLONEDDS_URI=file:///absolute/path/to/config_file.xml

RTI Connext 调优
----------------

**问题：** 即使使用 Reliable 设置并通过有线网络传输，Connext 仍无法可靠传递大型消息。

**解决方案：** 使用 `Connext QoS 配置文件 <https://github.com/jacobperron/pc_pipe/blob/master/etc/ROS2TEST_QOS_PROFILES.xml>`_，并增大 ``rmem_max`` 参数。

运行以下命令设置最大接收缓冲区 ``rmem_max``：

.. code-block:: console

    $ sudo sysctl -w net.core.rmem_max=4194304

通过将 Linux 内核的 ``net.core.rmem_max`` 调整到 4 MB，该 QoS 配置文件可以实现真正可靠的通信。

该配置已经在 SHMEM|UDPv4 以及单机 UDPv4 场景中验证能够可靠传递消息。还测试了两台通过 1 Gbps 以太网连接的计算机，在 ``rmem_max`` 分别为 4 MB 和 20 MB 时，均未丢失消息，平均消息传输时间分别为 700 ms 和 371 ms。

如果不配置内核 ``rmem_max``，相同的 Connext QoS 配置文件可能需要最多 12 秒才能完成数据传输，但最终仍能够完成传递。

**解决方案：** 也可以使用 `Connext QoS 配置文件 <https://github.com/jacobperron/pc_pipe/blob/master/etc/ROS2TEST_QOS_PROFILES.xml>`_，但不调整 ``rmem_max``。

``ROS2TEST_QOS_PROFILES.xml`` 文件根据 RTI 关于 `配置流量控制器 <https://community.rti.com/forum-topic/transfering-large-data-over-dds>`_ 的文档配置，包含慢速、中速和快速三种流量控制器（可在 Connext QoS 配置文件中查看）。

在我们的测试场景中，中速流量控制器效果最好。不过，仍需根据具体机器、网络和环境进行调优。Connext 流量控制器可用于调节带宽和发送数据的积极程度；一旦超过特定配置的带宽能力，性能就会开始下降。
