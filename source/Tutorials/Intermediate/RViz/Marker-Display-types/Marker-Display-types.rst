Marker：显示类型
================

**目标：** 了解基本 Marker 类型及其使用方法。

**教程级别：** 中级

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 3
   :local:

背景
----

Marker 显示插件允许通过发布 `visualization_msgs/msg/Marker <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/Marker.msg>`_ 或 `visualization_msgs/msg/MarkerArray <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/MarkerArray.msg>`_ 消息，以编程方式向三维视图添加各种基本形状。

.. image:: images/marker_overview.png

建议先完成 :doc:`Marker：发送基本形状 <../Marker-Sending-Basic-Shapes/Marker-Sending-Basic-Shapes>`，了解本页所使用 Marker 消息的最小发布示例。

Marker 消息
-----------

1. C++ 使用示例
^^^^^^^^^^^^^^^

首先创建一个简单的发布者节点，将 ``Marker`` 消息发布到 ``visualization_marker`` 话题：

.. code-block:: c++

   auto marker_pub = node->create_publisher<visualization_msgs::msg::Marker>(
     "visualization_marker", 1);

然后填写 `visualization_msgs/msg/Marker <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/Marker.msg>`_ 消息并发布：

.. code-block:: c++

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
   marker.pose.orientation.x = 0.0;
   marker.pose.orientation.y = 0.0;
   marker.pose.orientation.z = 0.0;
   marker.pose.orientation.w = 1.0;

   marker.scale.x = 1.0;
   marker.scale.y = 1.0;
   marker.scale.z = 1.0;

   marker.color.r = 0.0f;
   marker.color.g = 1.0f;
   marker.color.b = 0.0f;
   marker.color.a = 1.0;  // 不要忘记设置 alpha！

   // 仅当使用 MESH_RESOURCE 标记类型时需要设置：
   marker.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae";

   marker.lifetime = rclcpp::Duration::from_nanoseconds(0);

   marker_pub->publish(marker);

此外，还可以使用 `visualization_msgs/msg/MarkerArray <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/MarkerArray.msg>`_ 消息一次发布多个标记。

2. 消息参数
^^^^^^^^^^^

Marker 消息类型定义在 ``visualization_msgs`` 功能包中，属于 `ROS 2 Common Interfaces <https://github.com/ros2/common_interfaces/tree/{DISTRO}/visualization_msgs/msg>`_。该功能包中的消息定义包含字段注释，可以帮助理解各字段的作用。

* ``ns``：

  标记的命名空间。它与 ``id`` 一起构成标记的唯一标识。

* ``id``：

  分配给标记的唯一 ID。需要由发布者确保同一命名空间内的 ID 不重复。

* ``type``：

  标记类型，例如箭头、球体等。可用类型由消息定义指定。

* ``action``：

  对标记执行的操作：

  * ``0``：添加或修改。
  * ``1``：已弃用。
  * ``2``：删除。
  * ``3``：删除所有标记。

* ``pose``：

  标记位姿，包括 x/y/z 位置，以及 x/y/z/w 顺序的四元数方向。

* ``scale``：

  标记的尺寸。在应用位置和方向之前先应用缩放。``[1, 1, 1]`` 表示对象在三个方向上的尺寸均为 1 米。

* ``color``：

  对象颜色，使用 r/g/b/a 表示，各分量取值范围为 ``[0, 1]``。``a``（alpha）表示不透明度：1 表示完全不透明，0 表示完全透明。默认值为 0，也就是完全透明。

  **必须将标记的 alpha 值设置为非零值，否则标记默认是透明的！**

* ``points``：

  用于 ``Points``、``Line strips``、``Line lists`` 以及 ``Cube/Sphere lists`` 等类型。对于 ``Arrow`` 类型，也可以使用该字段指定箭头的起点和终点。

  该字段是 ``geometry_msgs/Point`` 类型的列表，用于指定需要渲染的对象中心点或各个顶点。

* ``colors``：

  仅用于使用 ``points`` 成员的标记。该字段为 ``points`` 中的每个顶点指定 r/g/b 颜色，目前不包含 alpha 分量。

* ``lifetime``：

  使用 `持续时间消息 <https://github.com/ros2/common_interfaces/blob/{DISTRO}/builtin_interfaces/msg/Duration.msg>`_ 表示标记的自动删除时间。若在生命周期结束前收到相同 ``namespace`` 和 ``id`` 的新标记，倒计时会重新开始。

* ``frame_locked``：

  如果不设置 ``frame_locked``，标记会根据当前坐标变换放置，并在之后保持在该位置，即使指定坐标系的变换发生变化也是如此。

  设置该参数后，RViz 会在每次更新周期中重新应用变换，使标记跟随指定坐标系的最新位置。

* ``text``：

  用于 ``TEXT_VIEW_FACING`` 类型标记的文本字符串。

* ``mesh_resource``：

  用于 ``MESH_RESOURCE`` 类型标记的资源位置。可以使用 RViz 支持的网格格式，例如 ``.stl``、Ogre ``.mesh``，以及 COLLADA ``.dae``。

  资源位置采用 `resource_retriever <https://github.com/ros/resource_retriever/tree/{DISTRO}>`_ 使用的 URI 格式，包括 ``package://`` 语法。

3. 对象类型
^^^^^^^^^^^

.. _RVizMarkerObjectTypes:

3.1 箭头（ARROW=0）
~~~~~~~~~~~~~~~~~~~

.. image:: images/ArrowMarker.png

箭头类型提供两种指定箭头起点和终点的方式。

* 位置/方向（Position/Orientation）：

  * 旋转支点位于箭尾尖端附近。
  * 单位方向表示箭头沿 +X 轴指向。
  * ``scale.x`` 表示箭头长度，``scale.y`` 表示箭头宽度，``scale.z`` 表示箭头高度。

* 起点/终点（Start/End Points）：

  * 也可以通过 ``points`` 成员指定箭头的起点和终点。如果 ``points`` 中包含点，RViz 就会采用这种方式。
  * 索引 0 的点作为起点，索引 1 的点作为终点。
  * ``scale.x`` 表示箭杆直径，``scale.y`` 表示箭头头部直径。
  * 如果 ``scale.z`` 不为 0，则表示箭头头部的长度。

3.2 立方体（CUBE=1）
~~~~~~~~~~~~~~~~~~~~

.. image:: images/CubeMarker.png

立方体的旋转支点位于立方体中心。

3.3 球体（SPHERE=2）
~~~~~~~~~~~~~~~~~~~

.. image:: images/SphereMarker.png

球体的旋转支点位于球心。

``scale.x``、``scale.y`` 和 ``scale.z`` 分别表示 x、y、z 方向上的直径。如果三个值不同，渲染结果将是椭球体，而不是球体。

3.4 圆柱体（CYLINDER=3）
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/CylinderMarker.png

圆柱体的旋转支点位于圆柱体中心。

``scale.x`` 和 ``scale.y`` 分别表示 x、y 方向上的直径。如果两个值不同，圆柱体的横截面将变成椭圆。``scale.z`` 用于指定圆柱体高度。

3.5 线条带（LINE_STRIP=4）
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/LineStripMarker.png

线条带使用 `visualization_msgs/msg/Marker <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/Marker.msg>`_ 消息的 ``points`` 成员。

它会连接每两个连续的点，例如 0-1、1-2、2-3、3-4、4-5，以此类推。

线条带对缩放有特殊处理：只使用 ``scale.x``，该值用于控制线段宽度。

注意，``pose`` 仍然会生效：线条中的点会受到该位姿变换，最终线条相对于消息头中指定的 ``frame_id`` 正确显示。

3.6 线段列表（LINE_LIST=5）
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/LineListMarker.png

线段列表使用 `visualization_msgs/msg/Marker <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/Marker.msg>`_ 消息的 ``points`` 成员。

它会将每一对点绘制为一条线段，例如 0-1、2-3、4-5，以此类推。不同线段之间互不连接。

线段列表对缩放也有特殊处理：只使用 ``scale.x``，该值用于控制线段宽度。

注意，``pose`` 仍然会生效：线段中的点会受到该位姿变换，最终线段相对于消息头中指定的 ``frame_id`` 正确显示。

3.7 立方体列表（CUBE_LIST=6）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/CubeListMarker.png

立方体列表由多个立方体组成，除位置外，所有立方体都具有相同属性。

与使用 `visualization_msgs/msg/MarkerArray <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/MarkerArray.msg>`_ 相比，使用该类型可以让 RViz 对渲染进行批处理，因此渲染速度更快。

需要注意，列表中的所有立方体必须具有相同的尺寸。

`visualization_msgs/msg/Marker <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/Marker.msg>`_ 消息的 ``points`` 成员用于指定每个立方体的位置。

3.8 球体列表（SPHERE_LIST=7）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/SphereListMarker.png

球体列表由多个球体组成，除位置外，所有球体都具有相同属性。

与使用 `visualization_msgs/msg/MarkerArray <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/MarkerArray.msg>`_ 相比，使用该类型可以让 RViz 对渲染进行批处理，因此渲染速度更快。

需要注意，列表中的所有球体必须具有相同的尺寸。

`visualization_msgs/msg/Marker <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/Marker.msg>`_ 消息的 ``points`` 成员用于指定每个球体的位置。

``pose`` 仍然会生效：``points`` 中的点会受到该位姿变换，最终对象相对于消息头中指定的 ``frame_id`` 正确显示。

3.9 点（POINTS=8）
~~~~~~~~~~~~~~~~~~

.. image:: images/PointsMarker.png

该类型使用 `visualization_msgs/msg/Marker <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/Marker.msg>`_ 消息的 ``points`` 成员。

``POINTS`` 对缩放有特殊处理：``scale.x`` 表示点的宽度，``scale.y`` 表示点的高度。

注意，``pose`` 仍然会生效：``points`` 中的点会受到该位姿变换，最终点相对于消息头中指定的 ``frame_id`` 正确显示。

3.10 面向视角的文本（TEXT_VIEW_FACING=9）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/text_view_facing_marker.png

该标记会在三维场景中的指定位置显示文本。文本始终会调整方向，使 RViz 用户能够正确阅读。

文本内容通过 Marker 的 ``text`` 字段设置。

该类型只使用 ``scale.z``，用于指定大写字母“A”的高度。

3.11 网格资源（MESH_RESOURCE=10）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/mesh_resource_marker.png

该类型使用 Marker 的 ``mesh_resource`` 字段。

可以使用 RViz 支持的网格格式，例如二进制 ``.stl``、Ogre ``.mesh``，以及 COLLADA（``.dae``）。

资源位置采用 `resource_retriever <https://github.com/ros/resource_retriever/tree/{DISTRO}>`_ 使用的 URI 格式，包括 ``package://`` 语法。

下面是一个网格资源标记的示例：

.. code-block:: c++

   marker.type = visualization_msgs::msg::Marker::MESH_RESOURCE;
   marker.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae";

网格缩放采用相对比例：

* ``(1.0, 1.0, 1.0)`` 表示按照网格文件中定义的原始尺寸显示。
* ``(1.0, 1.0, 2.0)`` 表示高度变为原来的两倍，宽度和深度保持不变。

如果 ``mesh_use_embedded_materials`` 标志设置为 true，并且网格格式支持内嵌材质（例如 COLLADA），RViz 就会使用网格文件中定义的材质，而不是 Marker 中定义的颜色。

从版本 1.8 开始，即使 ``mesh_use_embedded_materials`` 为 true，如果 Marker 的 ``color`` 不全为零（即 r、g、b、a 不全为 0），Marker 的颜色和 alpha 仍会用于对内嵌材质进行着色。

3.12 三角形列表（TRIANGLE_LIST=11）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/triangle_list_marker.png

该类型使用 ``points`` 成员，也可以选择使用 ``colors`` 成员。

每组三个点会被视为一个三角形，例如索引 0-1-2、3-4-5，以此类推。

注意，``pose`` 和 ``scale`` 仍然会生效：``points`` 中的点会受到这些变换，最终图形相对于消息头中指定的 ``frame_id`` 正确显示。

4. 渲染复杂度说明
^^^^^^^^^^^^^^^^^

与发布大量独立标记相比，使用单个 Marker 通常具有更低的渲染开销。

例如，单个立方体列表可以处理数千个立方体，而逐个发布数千个独立立方体标记，RViz 可能无法高效渲染。

因此，如果需要显示大量属性相同、位置不同的对象，优先考虑使用 ``CUBE_LIST`` 或 ``SPHERE_LIST`` 等列表类型。
