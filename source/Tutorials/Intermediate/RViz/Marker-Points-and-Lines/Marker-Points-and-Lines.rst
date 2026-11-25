Marker：点和线（C++）
======================

**目标：** 学习如何使用 ``visualization_msgs/msg/Marker`` 消息向 RViz 发送点和线。

**教程级别：** 中级

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 3
   :local:

.. note::

   本教程假设你已经完成 :doc:`Marker：发送基本形状 <../Marker-Sending-Basic-Shapes/Marker-Sending-Basic-Shapes>`。

简介
----

在 :doc:`Marker：发送基本形状 <../Marker-Sending-Basic-Shapes/Marker-Sending-Basic-Shapes>` 教程中，你已经学习了如何使用可视化 Marker 向 RViz 发送简单形状。除了简单形状，还可以发送其他类型的标记。本教程将介绍 ``POINTS``、``LINE_STRIP`` 和 ``LINE_LIST`` 三种标记类型。完整类型列表请参阅 :doc:`Marker：显示类型 <../Marker-Display-types/Marker-Display-types>`。

点、线条带和线段列表
--------------------

``POINTS``、``LINE_STRIP`` 和 ``LINE_LIST`` 都使用 ``visualization_msgs/msg/Marker`` 消息中的 ``points`` 成员。

* ``POINTS``：在添加的每个点的位置绘制一个点。
* ``LINE_STRIP``：将每个点作为连续线段的顶点，依次连接点 0 到点 1、点 1 到点 2、点 2 到点 3，以此类推。
* ``LINE_LIST``：每两个点组成一条独立线段，例如连接点 0 到点 1、点 2 到点 3，以此类推。不同线段之间不会自动连接。

代码位置
^^^^^^^^

从 `visualization_tutorials 仓库 <https://github.com/ros-visualization/visualization_tutorials>`_ 获取示例功能包。本教程代码位于 ``visualization_marker_tutorials`` 功能包中，可以在 `points_and_lines.cpp <https://github.com/ros-visualization/visualization_tutorials/blob/ros2/visualization_marker_tutorials/src/points_and_lines.cpp>`_ 中查看。

代码解析
^^^^^^^^

下面分析代码，略过前一个教程中已经介绍过的内容。

该程序最终会生成一条旋转的螺旋线，并从每个顶点向上延伸线段。

首先包含节点所需的头文件，包括用于生成螺旋线的 ``cmath``，以及用于 Marker 和点的消息定义：

.. code-block:: c++

   #define _USE_MATH_DEFINES

   #include <chrono>
   #include <cmath>
   #include <memory>

   #include "rclcpp/rclcpp.hpp"
   #include "geometry_msgs/msg/point.hpp"
   #include "visualization_msgs/msg/marker.hpp"

.. include:: ../../../../_internal/Rclcpp-Convenience-Header-Note.rst

接下来初始化 ROS 2，创建节点，在 ``visualization_marker`` 话题上创建发布者，并设置循环频率：

.. code-block:: c++

   rclcpp::init(argc, argv);
   auto node = rclcpp::Node::make_shared("points_and_lines");
   auto marker_pub = node->create_publisher<visualization_msgs::msg::Marker>(
     "visualization_marker", 10);
   rclcpp::Rate loop_rate(30);

另外创建一个浮点数变量，用于控制螺旋线随时间变化的动画相位：

.. code-block:: c++

   float f = 0.0f;

在主循环中，创建三个 ``visualization_msgs/msg/Marker`` 消息，并初始化它们共有的数据。

默认情况下，Marker 消息中的位姿四元数已经初始化为单位姿态，因此本教程只需要设置与示例有关的字段：

.. code-block:: c++

   visualization_msgs::msg::Marker points, line_strip, line_list;
   points.header.frame_id = line_strip.header.frame_id = line_list.header.frame_id = "my_frame";
   points.header.stamp = line_strip.header.stamp = line_list.header.stamp = rclcpp::Clock().now();
   points.ns = line_strip.ns = line_list.ns = "points_and_lines";
   points.action = line_strip.action = line_list.action = visualization_msgs::msg::Marker::ADD;

为三个标记分别设置不同的 ID。使用 ``points_and_lines`` 命名空间可以避免它们与其他 Marker 发布者发布的标记发生冲突：

.. code-block:: c++

   points.id = 0;
   line_strip.id = 1;
   line_list.id = 2;

然后设置三个标记的类型，分别为 ``POINTS``、``LINE_STRIP`` 和 ``LINE_LIST``：

.. code-block:: c++

   points.type = visualization_msgs::msg::Marker::POINTS;
   line_strip.type = visualization_msgs::msg::Marker::LINE_STRIP;
   line_list.type = visualization_msgs::msg::Marker::LINE_LIST;

``scale`` 成员对于不同标记类型具有不同含义：

* ``POINTS`` 使用 ``x`` 和 ``y`` 分量分别设置点的宽度和高度。
* ``LINE_STRIP`` 和 ``LINE_LIST`` 只使用 ``x`` 分量，用于设置线宽。

尺寸单位为米：

.. code-block:: c++

   points.scale.x = 0.2;
   points.scale.y = 0.2;

   line_strip.scale.x = 0.1;
   line_list.scale.x = 0.1;

接下来分别将点设置为绿色、线条带设置为蓝色、线段列表设置为红色。与其他 Marker 一样，alpha 通道必须设置为非零值：

.. code-block:: c++

   points.color.g = 1.0f;
   points.color.a = 1.0;

   line_strip.color.b = 1.0;
   line_strip.color.a = 1.0;

   line_list.color.r = 1.0;
   line_list.color.a = 1.0;

现在创建点和线的顶点。这里使用正弦和余弦函数生成螺旋线。

``POINTS`` 和 ``LINE_STRIP`` 标记每个顶点只需要一个点，而 ``LINE_LIST`` 标记的每条线段需要两个点：

.. code-block:: c++

   for (uint32_t i = 0; i < 100; ++i) {
     float y = 5 * sin(f + i / 100.0f * 2 * M_PI);
     float z = 5 * cos(f + i / 100.0f * 2 * M_PI);

     geometry_msgs::msg::Point p;
     p.x = static_cast<int32_t>(i) - 50;
     p.y = y;
     p.z = z;

     points.points.push_back(p);
     line_strip.points.push_back(p);

     // 线段列表中的每条线段需要两个点
     line_list.points.push_back(p);
     p.z += 1.0;
     line_list.points.push_back(p);
   }

填充完三个 Marker 消息后，分别发布它们：

.. code-block:: c++

   marker_pub->publish(points);
   marker_pub->publish(line_strip);
   marker_pub->publish(line_list);

最后休眠，推进动画相位，然后回到循环开头：

.. code-block:: c++

   loop_rate.sleep();
   f += 0.04f;

查看标记
^^^^^^^^

在工作空间中构建功能包：

.. code-block:: console

   $ colcon build --packages-select visualization_marker_tutorials

然后加载工作空间环境并运行节点：

.. code-block:: console

   $ source install/setup.bash
   $ ros2 run visualization_marker_tutorials points_and_lines

现在启动 RViz：

.. code-block:: console

   $ source install/setup.bash
   $ ros2 run rviz2 rviz2

如果之前没有使用过 RViz，可以先阅读 :doc:`RViz 用户指南 <../RViz-User-Guide/RViz-User-Guide>`。

按照上一个教程中的方式配置 RViz。由于本例没有设置坐标变换，因此需要将 ``Fixed Frame`` 设置为 ``my_frame``，然后添加一个 ``Marker`` 显示插件。

默认话题 ``visualization_marker`` 与节点发布的话题相同。

现在应该可以看到一条旋转的螺旋线，效果类似下图：

.. image:: images/points_and_lines_marker_tutorial.png

下一步
------

有关 RViz 支持的标记和选项，请继续阅读 :doc:`Marker：显示类型 <../Marker-Display-types/Marker-Display-types>`，并尝试使用其他标记类型。
