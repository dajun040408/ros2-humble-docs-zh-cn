.. redirect-from::

    About-Topic-Statistics
    Concepts/About-Topic-Statistics

话题统计
========

.. contents:: 目录
   :local:

概述
----

ROS 2 提供了集成式统计测量功能，可以统计任意订阅者接收到的消息。用户收集订阅统计数据后，可以分析系统性能，或辅助诊断当前存在的问题。

提供的测量指标包括接收消息年龄和接收消息周期。对于每项指标，系统都会提供平均值、最大值、最小值、标准差和样本数量。这些统计数据通过滑动窗口计算。

统计数据的计算方式
------------------

每组统计数据都使用 `libstatistics_collector <https://github.com/ros-tooling/libstatistics_collector>`__ 软件包中的工具，以恒定时间和恒定内存开销进行计算。

当订阅者收到一条新消息时，该消息就会成为当前测量窗口中的一个新样本。平均值采用滑动平均算法计算。收到每个新样本时，系统会更新最大值、最小值和样本数量；标准差则使用 Welford 在线算法计算。

计算的统计指标类型
------------------

* 接收消息周期

  * 单位：毫秒。
  * 使用系统时钟测量连续接收消息之间的时间间隔。

* 接收消息年龄

  * 单位：毫秒。
  * 消息必须在 Header 字段中包含时间戳，系统才能计算消息从发布者发送到订阅者接收时的年龄。

行为
----

默认情况下，话题统计测量功能处于禁用状态。

通过订阅配置选项为特定节点启用该功能后，该订阅对应的接收消息年龄和接收消息周期测量都会启用。

统计数据会以可配置的周期（默认 1 秒）发布为 `statistics_msg/msg/MetricsMessage <https://github.com/ros2/rcl_interfaces/blob/{REPOS_FILE_BRANCH}/statistics_msgs/msg/MetricsMessage.msg>`__，并发送到可配置的话题（默认 ``/statistics``）。请注意，发布周期同时也是样本收集窗口的周期。

由于接收消息周期的计算需要使用消息 Header 中的时间戳，如果没有找到时间戳，系统仍会发布数据，但所有统计值都会是 NaN。发布 NaN 而不是完全不发布，可以避免出现信号缺失问题，并明确表示当前无法完成测量。

每个测量窗口中的第一条消息不会产生接收消息周期测量值。这是因为计算该指标需要知道上一条消息的到达时间，因此只有窗口中的后续样本才能产生测量结果。

与 ROS 1 的比较
---------------

与 ROS 1 的 `Topic Statistics <https://wiki.ros.org/Topics#Topic_statistics>`__ 类似，ROS 2 也会计算消息年龄和消息周期，不过这些指标是在订阅端计算的。

ROS 1 中的其他指标（例如丢弃消息数量或流量）目前尚未提供。

支持情况
--------

该功能最初在 ROS 2 Foxy 中仅支持 C++（rclcpp）。后续工作和改进（例如 Python 支持）可在 `相关 Issue <https://github.com/ros2/ros2/issues/917>`__ 中查看。
