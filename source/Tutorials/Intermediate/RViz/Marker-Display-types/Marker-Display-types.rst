Marker：显示类型
================

**目标：** 了解基本 Marker 类型及其使用方法。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

Markers 显示插件允许通过发布 ``visualization_msgs/msg/Marker`` 或 ``visualization_msgs/msg/MarkerArray`` 消息，以编程方式向三维视图添加各种基本形状。

.. image:: images/marker_overview.png

建议先完成 :doc:`Marker：发送基本形状 <../Marker-Sending-Basic-Shapes/Marker-Sending-Basic-Shapes>`，了解 Marker 消息的最小发布示例。

Marker 消息
-----------

C++ 示例
^^^^^^^^

创建一个发布 ``Marker`` 消息的节点，并将消息发布到 ``visualization_marker`` 话题：

.. code-block:: cpp

   auto marker_pub =
     node->create_publisher<visualization_msgs::msg::Marker>(
       "visualization_marker", 1);

填充 ``visualization_msgs/msg/Marker`` 消息并发布：

.. code-block:: cpp

   visualization_msgs::msg::Marker marker;
   marker.header.frame_id = "/my_frame";
   marker.header.stamp = rclcpp::Clock().now();
   marker.ns = "basic_shapes";
   marker.id = 0;
   marker.type = visualization_msgs::msg::Marker::SPHERE;
   marker.action = visualization_msgs::msg::Marker::ADD;
   marker.pose.position.x = 0;
   marker.pose.position.y = 0;
   marker.pose.position.z = 0;
   marker.pose.orientation.w = 1.0;
   marker.scale.x = 1.0;
   marker.scale.y = 1.0;
   marker.scale.z = 1.0;
   marker.color.r = 0.0f;
   marker.color.g = 1.0f;
   marker.color.b = 0.0f;
   marker.color.a = 1.0;
   marker_pub->publish(marker);

关键字段
--------

* ``header``：定义标记所使用的坐标系和时间戳。
* ``ns``：标记命名空间。
* ``id``：同一命名空间中的标记 ID。
* ``type``：标记类型，例如箭头、立方体、球体、圆柱体、线条、点、文本或网格资源。
* ``action``：对标记执行的操作，例如 ``ADD``、``DELETE`` 或 ``DELETEALL``。
* ``pose``：标记的位置和方向。
* ``scale``：标记尺寸或线宽。
* ``color``：RGBA 颜色。alpha 值为 0 表示完全透明。
* ``lifetime``：标记的生命周期，超过时间后可自动删除。
* ``frame_locked``：是否在每次更新时重新应用坐标变换。

使用 MarkerArray
----------------

当需要一次发布多个标记时，可以使用 ``visualization_msgs/msg/MarkerArray``，将多个 Marker 放入同一个数组消息中，再发布到对应话题。

总结
----

Marker 消息允许节点向 RViz 动态添加、更新和删除三维对象。正确设置坐标系、ID、类型、位姿、尺寸和颜色，是确保标记正确显示的关键。
