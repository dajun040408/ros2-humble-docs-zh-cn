Marker：向 RViz 发送基本形状（C++）
====================================

**目标：** 学习如何使用 ``visualization_msgs/msg/Marker`` 消息向 RViz 发送基本形状。

**教程级别：** 中级

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 3
   :local:

.. note::

   本教程假设你已经熟悉如何编写 ROS 2 C++ 节点，以及如何使用 ``colcon`` 构建功能包。

简介
----

与许多其他 RViz 显示插件不同，``Marker`` 显示插件不要求 RViz 预先了解数据的含义。节点通过 ``visualization_msgs/msg/Marker`` 消息发送基本几何对象，RViz 可以将其渲染为箭头、长方体、球体、圆柱体等。

本教程展示如何发送四种基本形状：立方体、球体、圆柱体和箭头。我们将创建一个程序，每秒发布一个新标记，用不同形状替换上一个标记。

如果希望进一步了解标记消息字段和对象类型，请参阅 :doc:`Marker：显示类型 <../Marker-Display-types/Marker-Display-types>`。

创建功能包
----------

从 `visualization_tutorials 仓库 <https://github.com/ros-visualization/visualization_tutorials>`_ 获取示例功能包，并在工作空间中构建：

.. code-block:: console

   $ colcon build --packages-select visualization_marker_tutorials

发送 Marker
-----------

代码位置
^^^^^^^^

本教程的代码位于 ``visualization_marker_tutorials`` 功能包中。可以在 `basic_shapes.cpp <https://github.com/ros-visualization/visualization_tutorials/blob/ros2/visualization_marker_tutorials/src/basic_shapes.cpp>`_ 中查看完整源码。

代码解析
^^^^^^^^

下面逐段分析代码。

首先包含节点所需的头文件，包括 ``rclcpp`` 和 ``visualization_msgs/msg/Marker`` 消息定义：

.. code-block:: c++

   #include <memory>

   #include "rclcpp/logging.hpp"
   #include "rclcpp/rclcpp.hpp"
   #include "visualization_msgs/msg/marker.hpp"

.. include:: ../../../../_internal/Rclcpp-Convenience-Header-Note.rst

接下来初始化 ROS 2，创建节点，并在 ``visualization_marker`` 话题上创建发布者：

.. code-block:: c++

   rclcpp::init(argc, argv);
   auto node = rclcpp::Node::make_shared("basic_shapes");
   auto marker_pub = node->create_publisher<visualization_msgs::msg::Marker>(
     "visualization_marker", 1);
   rclcpp::Rate loop_rate(1);

对于 RViz 来说，发布者是关键，因为 ``Marker`` 显示插件会订阅相同的话题。

创建一个整数，用于记录接下来要发布的形状。这里使用的四种类型都通过同一个 ``visualization_msgs/msg/Marker`` 消息发布，因此只需切换形状类型，就可以依次展示四种不同的形状：

.. code-block:: c++

   uint32_t shape = visualization_msgs::msg::Marker::CUBE;

接下来创建一个新的 ``visualization_msgs/msg/Marker`` 消息，并开始填充字段。首先设置消息头中的坐标系 ID 和时间戳：

.. code-block:: c++

   visualization_msgs::msg::Marker marker;
   marker.header.frame_id = "my_frame";
   marker.header.stamp = rclcpp::Clock().now();

这里将 ``frame_id`` 设置为 ``my_frame``，仅作为示例。在实际系统中，应将其设置为用于解释标记位姿的坐标系。

由于本教程没有发布坐标变换，因此稍后需要将 RViz 的 Fixed Frame 设置为相同的坐标系。

命名空间和 ID 字段共同构成标记的唯一标识。如果收到另一个具有相同命名空间和 ID 的消息，新标记会替换旧标记：

.. code-block:: c++

   marker.ns = "basic_shapes";
   marker.id = 0;

``type`` 字段指定要发送的标记类型。可用类型列在 ``visualization_msgs/msg/Marker`` 消息定义中。这里将类型设置为 ``shape`` 变量，该变量会在每次循环时改变：

.. code-block:: c++

   marker.type = shape;

``action`` 字段指定对标记执行的操作。ROS 2 中使用的值包括 ``ADD``、``DELETE`` 和 ``DELETEALL``。其中 ``ADD`` 的含义不只是添加，还包括创建或修改已有标记：

.. code-block:: c++

   marker.action = visualization_msgs::msg::Marker::ADD;

接下来设置标记的位姿。这是相对于消息头中指定的坐标系和时间的完整六自由度位姿。本例将标记放在坐标系原点，并使用单位四元数表示无旋转：

.. code-block:: c++

   marker.pose.position.x = 0;
   marker.pose.position.y = 0;
   marker.pose.position.z = 0;
   marker.pose.orientation.x = 0.0;
   marker.pose.orientation.y = 0.0;
   marker.pose.orientation.z = 0.0;
   marker.pose.orientation.w = 1.0;

现在设置标记的尺寸。对于这些基本形状，三个方向的比例均设置为 ``1.0``，表示每个方向的尺寸为 1 米：

.. code-block:: c++

   marker.scale.x = 1.0;
   marker.scale.y = 1.0;
   marker.scale.z = 1.0;

颜色使用 RGBA 表示，各分量的取值范围为 ``[0, 1]``。本例使用不透明的绿色。

特别注意 alpha 通道：如果 ``a`` 保持默认值 0，标记将完全透明，因此可能看不到标记：

.. code-block:: c++

   marker.color.r = 0.0f;
   marker.color.g = 1.0f;
   marker.color.b = 0.0f;
   marker.color.a = 1.0;

``lifetime`` 字段控制标记在自动删除前保留多长时间。持续时间为 0 表示不会因生命周期到期而自动删除：

.. code-block:: c++

   marker.lifetime = rclcpp::Duration::from_nanoseconds(0);

完成消息字段设置后，发布 Marker 消息：

.. code-block:: c++

   marker_pub->publish(marker);

只需要发布一条 Marker 消息，就可以展示四种形状。程序根据当前形状设置下一次循环要发布的形状：

.. code-block:: c++

   switch (shape) {
     case visualization_msgs::msg::Marker::CUBE:
       shape = visualization_msgs::msg::Marker::SPHERE;
       break;
     case visualization_msgs::msg::Marker::SPHERE:
       shape = visualization_msgs::msg::Marker::ARROW;
       break;
     case visualization_msgs::msg::Marker::ARROW:
       shape = visualization_msgs::msg::Marker::CYLINDER;
       break;
     case visualization_msgs::msg::Marker::CYLINDER:
       shape = visualization_msgs::msg::Marker::CUBE;
       break;
   }

最后休眠一秒，然后回到循环开头：

.. code-block:: c++

   loop_rate.sleep();

构建代码
^^^^^^^^

在工作空间中构建 ``visualization_marker_tutorials``：

.. code-block:: console

   $ colcon build --packages-select visualization_marker_tutorials

运行代码
^^^^^^^^

加载工作空间环境并运行节点：

.. code-block:: console

   $ source install/setup.bash
   $ ros2 run visualization_marker_tutorials basic_shapes

查看标记
--------

节点开始发布标记后，启动 RViz 查看它们：

.. code-block:: console

   $ source install/setup.bash
   $ ros2 run rviz2 rviz2

如果之前没有使用过 RViz，可以先阅读 :doc:`RViz 用户指南 <../RViz-User-Guide/RViz-User-Guide>`。

由于本教程没有设置任何坐标变换，首先需要将 RViz 中的 ``Fixed Frame`` 设置为 Marker 消息使用的坐标系 ``my_frame``。然后添加一个 ``Marker`` 显示插件。

注意，默认话题 ``visualization_marker`` 与节点发布的话题相同。

现在应该可以在坐标系原点看到一个标记，并且它每秒都会切换一次形状。

.. image:: images/basic_shapes_tutorial.png

更多信息
--------

下一个 Marker 教程是 :doc:`Marker：点和线 <../Marker-Points-and-Lines/Marker-Points-and-Lines>`。

有关 Marker 消息字段以及本教程所示四种形状之外的其他标记类型，请参阅 :doc:`Marker：显示类型 <../Marker-Display-types/Marker-Display-types>`。

完整源码请参阅 `visualization_tutorials 仓库 <https://github.com/ros-visualization/visualization_tutorials>`_。
