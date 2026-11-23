DDS 中间件实现
===============

以下是当前可用的 DDS 实现：

* :doc:`使用 Eclipse Cyclone DDS <DDS-Implementations/Working-with-Eclipse-CycloneDDS>` 介绍如何使用 Cyclone DDS。
* :doc:`使用 eProsima Fast DDS <DDS-Implementations/Working-with-eProsima-Fast-DDS>` 介绍如何使用 Fast DDS。
* :doc:`使用 RTI Connext DDS <DDS-Implementations/Working-with-RTI-Connext-DDS>` 介绍如何使用 RTI Connext DDS。
* :doc:`使用 GurumNetworks GurumDDS <DDS-Implementations/Working-with-GurumNetworks-GurumDDS>` 介绍如何使用 GurumDDS。

.. toctree::
   :hidden:
   :glob:

   DDS-Implementations/*

如果希望使用其他供应商的实现，需要在构建 ROS 2 之前单独安装其软件。ROS 2 构建过程会自动为已正确安装并 source 环境的供应商构建支持组件。

安装新的 RMW 供应商实现后，可以在运行时切换所使用的供应商：:doc:`使用多个 RMW 实现 <../../How-To-Guides/Working-with-multiple-RMW-implementations>`。
