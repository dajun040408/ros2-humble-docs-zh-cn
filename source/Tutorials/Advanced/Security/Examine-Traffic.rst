.. redirect-from::

    Tutorials/Security/Examine-Traffic

.. _Examine-Traffic:

检查网络流量
============

**目标：** 捕获并检查原始 ROS 2 网络流量。

**教程级别：** 高级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

概述
----

ROS 2 通信安全的核心目标是保护节点之间的通信。前面的教程已经启用了安全机制，但如何实际确认网络流量是否已加密？本教程将捕获实时网络流量，展示加密和未加密流量之间的区别。

.. note::

  rmw_fastrtps_cpp 默认使用共享内存传输，以提升同一主机上端点之间的传输性能。安全 enclave 仍然会生效，数据也仍然会加密，但由于数据不会经过网络接口，因此无法捕获实时网络流量。

  如果使用 rmw_fastrtps_cpp，需要让发布者和订阅者运行在不同主机上，或者通过启用 UDP 传输和 Fast-DDS XML 配置禁用共享内存传输。参考：https://fast-dds.docs.eprosima.com/en/latest/fastdds/transport/udp/udp.html#enabling-udp-transport 和 https://github.com/ros2/rmw_fastrtps#full-qos-configuration。

前置条件
--------

本指南仅适用于 Linux，并假设已经 :doc:`安装 ROS 2 <../../../Installation>`。

运行演示
--------

安装 tcpdump
^^^^^^^^^^^^

首先在新终端窗口中安装 tcpdump。这是一个用于捕获和显示网络流量的命令行工具。本教程使用 tcpdump 命令进行说明，也可以使用 Wireshark 等图形化工具捕获和分析流量。

.. code-block:: console

  $ sudo apt update
  $ sudo apt install tcpdump

通过多个 ssh 会话在同一台机器上运行以下命令。

启动 talker 和 listener
^^^^^^^^^^^^^^^^^^^^^^^

分别在两个终端中启动 talker 和 listener。此时不设置安全环境变量，因此这些会话未启用安全功能。

终端 1：

.. code-block:: console

  $ unset ROS_SECURITY_ENABLE
  $ ros2 run demo_nodes_cpp talker --ros-args --enclave /talker_listener/talker

终端 2：

.. code-block:: console

  $ unset ROS_SECURITY_ENABLE
  $ ros2 run demo_nodes_cpp listener --ros-args --enclave /talker_listener/listener

显示未加密的发现数据包
^^^^^^^^^^^^^^^^^^^^^^

talker 和 listener 运行后，打开另一个终端，启动 tcpdump 查看网络流量。读取原始网络流量属于特权操作，因此需要使用 sudo。

下面的命令使用 -X 打印数据包内容，使用 -i 监听所有网络接口，并且只捕获 UDP 7400 端口的流量。

.. code-block:: console

  $ sudo tcpdump -X -i any udp port 7400

这是一个发现数据报，表示 talker 正在查找订阅者。数据包中可以看到节点名称和 enclave 名称都是以明文传输的。还应该看到 listener 节点发送的类似发现数据报。

典型发现数据包的其他特征：

* 目标地址为 239.255.0.1，这是一个组播 IP 地址；ROS 2 默认使用组播流量进行发现。
* 根据 DDS-RTPS 规范，UDP 目标端口为 7400。
* 数据包包含 RTPS 标记，该标记同样由 DDS-RTPS 规范定义。规范地址：https://www.omg.org/spec/DDSI-RTPS/About-DDSI-RTPS/。

显示未加密的数据包
^^^^^^^^^^^^^^^^^^

使用 tcpdump 捕获非发现类 RTPS 数据包，可以过滤 UDP 7400 以上的端口：

.. code-block:: console

  $ sudo tcpdump -i any -X udp portrange 7401-7500

可以看到消息内容 Hello World: 2135 以明文发送。源地址和目标地址均为 localhost，因为两个节点运行在同一台机器上，并通过 localhost 接口发现了彼此。

启用加密
^^^^^^^^

停止 talker 和 listener 节点。设置安全环境变量后重新启动两个节点，以启用加密。

终端 1：

.. code-block:: console

  $ export ROS_SECURITY_KEYSTORE=~/sros2_demo/demo_keystore
  $ export ROS_SECURITY_ENABLE=true
  $ export ROS_SECURITY_STRATEGY=Enforce
  $ ros2 run demo_nodes_cpp talker --ros-args --enclave /talker_listener/talker

终端 2：

.. code-block:: console

  $ export ROS_SECURITY_KEYSTORE=~/sros2_demo/demo_keystore
  $ export ROS_SECURITY_ENABLE=true
  $ export ROS_SECURITY_STRATEGY=Enforce
  $ ros2 run demo_nodes_cpp listener --ros-args --enclave /talker_listener/listener

显示已加密的发现数据包
^^^^^^^^^^^^^^^^^^^^^^

再次运行前面使用的 tcpdump 命令，检查启用加密后的发现流量。典型发现数据包会明显更大，并包含可用于在 ROS 节点之间建立加密连接的信息。其中实际上包含启用安全功能时创建的部分安全配置文件。

更多背景请参阅论文 Network Reconnaissance and Vulnerability Excavation of Secure DDS Systems：https://arxiv.org/abs/1908.05310。

显示已加密的数据包
^^^^^^^^^^^^^^^^^^

现在使用 tcpdump 捕获数据包：

.. code-block:: console

  $ sudo tcpdump -i any -X udp portrange 7401-7500

该 RTPS 数据包中的数据已经全部加密。除了数据包本身，还应该看到包含节点名称和 enclave 名称的其他数据包。这些数据包支持参数和服务等 ROS 功能。可以通过安全策略控制这些数据包的加密选项。
