.. redirect-from::

   Concepts/About-Domain-ID

ROS 域 ID
=========

.. contents:: 目录
   :local:

ROS 2 使用 DDS（Data Distribution Service，数据分发服务）作为其中间件。DDS 使用域（Domain）将 ROS 2 网络逻辑隔离开来。域中的节点可以相互发现并通信，而不同域中的节点不会发现彼此，也不会直接通信。

默认情况下，ROS 2 节点使用域 ID 0。若要更改节点所属的域，可以设置环境变量 ``ROS_DOMAIN_ID``。

.. code-block:: console

   export ROS_DOMAIN_ID=<your_domain_id>

选择域 ID 时，需要考虑操作系统对端口号的限制。DDS 使用 UDP 端口进行通信，域 ID 会参与端口号计算，因此并非所有整数都适合作为域 ID。

对于 Linux 系统，建议使用 0 到 101 之间的域 ID。该范围可以降低与系统临时端口范围发生冲突的风险。

.. note::

   如果在同一台计算机上运行多个 ROS 2 应用，并且希望它们互相隔离，可以为每个应用设置不同的 ``ROS_DOMAIN_ID``。如果希望它们互相通信，则必须使用相同的域 ID。

在多台计算机之间通信时，所有希望互相发现的 ROS 2 节点也必须使用相同的域 ID，并且网络配置必须允许 DDS 发现流量通过。

更多信息请参阅 `ROS 2 域 ID 设计说明 <https://design.ros2.org/articles/ros_domain_id.html>`__。
