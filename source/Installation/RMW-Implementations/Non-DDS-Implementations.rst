非 DDS 中间件实现
=================

* :doc:`使用 Zenoh <Non-DDS-Implementations/Working-with-Zenoh>` 介绍如何使用 Zenoh。

.. toctree::
   :hidden:
   :glob:

   Non-DDS-Implementations/*

如果希望使用其他供应商提供的实现，需要在构建 ROS 2 之前单独安装相应软件。ROS 2 构建过程会自动为已正确安装并 source 环境的供应商构建支持组件。

安装新的 RMW 供应商实现后，可以在运行时切换所使用的供应商：:doc:`使用多个 RMW 实现 <../../How-To-Guides/Working-with-multiple-RMW-implementations>`。
