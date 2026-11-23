.. redirect-from::

    Installation/DDS-Implementations

RMW 中间件实现
==============

默认情况下，ROS 2 使用 DDS 作为其中间件，相关设计请参阅 `ROS on DDS <https://design.ros2.org/articles/ros_on_dds.html>`_。ROS 2 兼容多种 DDS 或 RTPS（DDS 线协议）供应商。目前支持 eProsima Fast DDS、RTI Connext DDS、Eclipse Cyclone DDS 和 GurumNetworks GurumDDS。

ROS 2 也支持非 DDS 的 RMW 实现，例如 Zenoh。

有关各发行版支持的 RMW 供应商，请参阅 `REP-2000 <https://reps.openrobotics.org/rep-2000/>`_。

默认的 RMW 供应商是 eProsima Fast DDS。

请查看以下可选方案：

.. toctree::
   :hidden:
   :glob:

   RMW-Implementations/*

* :doc:`DDS 实现 <RMW-Implementations/DDS-Implementations>` 介绍如何使用 DDS。
* :doc:`非 DDS 实现 <RMW-Implementations/Non-DDS-Implementations>` 介绍如何使用非 DDS 实现。
