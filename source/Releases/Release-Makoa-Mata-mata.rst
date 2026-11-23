.. _upcoming-release:

.. _makoa-release:

Makoa Mata-mata（代号 `makoa`；2027 年 5 月）
=============================================

.. toctree::
   :hidden:

   makoa/release-timeline.rst
   makoa/supported-platforms.rst

*Makoa Mata-mata* 是 ROS 2 的第十三个发行版。这是一个常规发行版，支持周期持续至 2028 年 12 月。

* 安装文档：待补充
* :doc:`Makoa 发布时间表 <makoa/release-timeline>`
* :doc:`Makoa 支持的平台 <makoa/supported-platforms>`

Makoa 新功能
------------

待补充

自 Lyrical 发行版以来的变更
---------------------------

移除 Fast DDS 动态类型支持的 RMW 实现
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`rmw_fastrtps_dynamic_cpp` 软件包已被移除。这意味着用户将无法再选择 `RMW_IMPLEMENTATION=rmw_fastrtps_dynamic_cpp`。建议用户改用 `RMW_IMPLEMENTATION=rmw_fastrtps_cpp`。
