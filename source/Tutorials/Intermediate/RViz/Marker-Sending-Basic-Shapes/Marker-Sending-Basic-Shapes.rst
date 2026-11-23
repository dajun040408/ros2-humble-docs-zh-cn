Marker：向 RViz 发送基本形状（C++）
====================================

**目标：** 学习如何使用 §visualization_msgs/msg/Marker§ 消息向 RViz 发送基本形状。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 3
   :local:

简介
----

与许多其他 RViz 显示插件不同，§Marker§ 显示插件不要求 RViz 预先了解数据含义。节点通过 §visualization_msgs/msg/Marker§ 消息发送基本几何对象，RViz 可以将其渲染为箭头、长方体、球体、圆柱体等。

本教程展示如何发送四种基本形状：立方体、球体、圆柱体和箭头。示例程序每秒发布一个新标记，用不同形状替换上一个标记。更多标记字段和类型请参阅 :doc:§Marker 显示类型 <../Marker-Display-types/Marker-Display-types>§。

创建功能包
----------

从 §visualization_tutorials§ 仓库获取示例功能包，并在工作空间中构建：

.. code-block:: console

   $ colcon build --packages-select visualization_marker_tutorials

发送 Marker
-----------

本教程代码位于 §visualization_marker_tutorials§ 功能包的 §basic_shapes.cpp§ 中。

首先包含节点所需头文件：

.. code-block:: cpp

   #include <memory>
   #include "rclcpp/rclcpp.hpp"
   #include "visualization_msgs/msg/marker.hpp"

初始化 ROS 2、创建节点，并在 §visualization_marker§ 话题上创建发布者：

.. code-block:: cpp

   auto marker_pub =
     node->create_publisher<visualization_msgs::msg::Marker>(
       "visualization_marker", 1);

填充 Marker 消息时，需要设置以下关键字段：

* §header.frame_id§：标记所属坐标系。
* §header.stamp§：时间戳。
* §ns§ 和 §id§：用于唯一标识标记。
* §type§：标记类型，例如 §CUBE§、§SPHERE§、§CYLINDER§ 或 §ARROW§。
* §action§：操作类型，新增或更新通常使用 §ADD§。
* §pose§：位置和方向。
* §scale§：三个方向的尺寸。
* §color§：RGBA 颜色。不要忘记设置 alpha，否则标记可能不可见。

示例：

.. code-block:: cpp

   visualization_msgs::msg::Marker marker;
   marker.header.frame_id = "my_frame";
   marker.header.stamp = rclcpp::Clock().now();
   marker.ns = "basic_shapes";
   marker.id = 0;
   marker.type = visualization_msgs::msg::Marker::SPHERE;
   marker.action = visualization_msgs::msg::Marker::ADD;
   marker.pose.orientation.w = 1.0;
   marker.scale.x = 1.0;
   marker.scale.y = 1.0;
   marker.scale.z = 1.0;
   marker.color.g = 1.0f;
   marker.color.a = 1.0;
   marker_pub->publish(marker);

运行与验证
----------

启动 RViz，添加 §Marker§ 显示，并将其订阅话题设置为 §visualization_marker§。运行示例节点后，应能看到程序依次发布不同基本形状。

总结
----

本教程介绍了 Marker 消息的基本字段，以及如何通过发布 §visualization_msgs/msg/Marker§ 在 RViz 中显示基本几何形状。
