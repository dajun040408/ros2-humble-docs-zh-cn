Marker：点和线（C++）
======================

**目标：** 学习如何使用 ``visualization_msgs/msg/Marker`` 消息向 RViz 发送点和线。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 3
   :local:

.. note::

   本教程假设你已经完成 :doc:`Marker：发送基本形状 <../Marker-Sending-Basic-Shapes/Marker-Sending-Basic-Shapes>`。

简介
----

此前的教程介绍了如何使用可视化 Marker 向 RViz 发送简单形状。本教程介绍三种其他标记类型：``POINTS``、``LINE_STRIP`` 和 ``LINE_LIST``。完整类型列表请参阅 :doc:`Marker：显示类型 <../Marker-Display-types/Marker-Display-types>`。

点、线条带和线段列表
--------------------

``POINTS``、``LINE_STRIP`` 和 ``LINE_LIST`` 都使用 ``visualization_msgs/msg/Marker`` 消息中的 ``points`` 成员。

* ``POINTS``：在添加的每个点位置绘制一个点。
* ``LINE_STRIP``：将每个点作为连续线段的顶点，依次连接点 0 到点 1、点 1 到点 2，以此类推。
* ``LINE_LIST``：每两个点组成一条独立线段，例如连接点 0 到点 1、点 2 到点 3，不会自动连接不同线段。

代码
----

本教程代码位于 ``visualization_tutorials`` 仓库的 ``visualization_marker_tutorials`` 功能包中，文件为 ``points_and_lines.cpp``。

代码说明
--------

示例最终会生成一个旋转的螺旋线，并从每个顶点向上延伸线段。节点创建 Marker 发布者后，需要设置坐标系、时间戳、命名空间、ID、类型和动作。

对于点和线，核心是向 ``marker.points`` 添加几何点：

.. code-block:: cpp

   visualization_msgs::msg::Marker marker;
   marker.header.frame_id = "my_frame";
   marker.header.stamp = node->get_clock()->now();
   marker.ns = "points_and_lines";
   marker.id = 0;
   marker.action = visualization_msgs::msg::Marker::ADD;
   marker.type = visualization_msgs::msg::Marker::LINE_STRIP;

   geometry_msgs::msg::Point p;
   p.x = 0.0;
   p.y = 0.0;
   p.z = 0.0;
   marker.points.push_back(p);

对于 ``POINTS``，每个点独立显示；对于 ``LINE_STRIP``，点按顺序连接；对于 ``LINE_LIST``，每两个点构成一条独立线段。线宽和点尺寸通过 ``scale`` 设置，颜色通过 ``color`` 或 ``colors`` 设置。

总结
----

本教程介绍了 Marker 的 ``points`` 字段，以及如何使用 ``POINTS``、``LINE_STRIP`` 和 ``LINE_LIST`` 在 RViz 中绘制点和线。
