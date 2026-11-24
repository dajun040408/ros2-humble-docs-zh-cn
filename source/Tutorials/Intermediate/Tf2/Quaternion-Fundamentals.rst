.. redirect-from::

    Tutorials/Tf2/Quaternion-Fundamentals

.. _QuaternionFundamentals:

四元数基础
==========

**目标：** 学习 ROS 2 中四元数的基本用法。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

四元数是用于表示方向的四元组，比旋转矩阵更加简洁。在涉及三维旋转的场景中，四元数非常适合进行计算。四元数广泛应用于机器人学、量子力学、计算机视觉和 3D 动画。

可以在§Wikipedia <https://en.wikipedia.org/wiki/Quaternion>§_ 上了解相关数学概念，也可以观看§Visualizing quaternions <https://eater.net/quaternions>§_ 视频系列。

本教程将介绍 ROS 2 中四元数的工作方式和转换方法。

前置条件
--------

可以参考 transforms3d、scipy.spatial.transform、pytransform3d、numpy-quaternion 或 blender.mathutils 等库。它们并非硬性要求，也可以使用自己熟悉的其他几何变换库。

四元数的组成
------------

ROS 2 使用四元数跟踪和应用旋转。一个四元数包含 4 个分量 (x, y, z, w)。ROS 2 中 w 位于最后，但在 Eigen 等库中，w 可能位于第一个位置。

常用的单位四元数 (0, 0, 0, 1) 表示绕 x、y、z 轴均没有旋转，可以通过以下方式创建：

.. code-block:: cpp

   #include <tf2/LinearMath/Quaternion.h>

   tf2::Quaternion q;
   // 根据 roll/pitch/yaw（弧度）创建四元数
   q.setRPY(0, 0, 0);
   // 输出四元数分量 (0, 0, 0, 1)
   RCLCPP_INFO(this->get_logger(), "%f %f %f %f",
               q.x(), q.y(), q.z(), q.w());

四元数的模长应始终为 1。如果数值误差导致四元数模长不为 1，ROS 2 会输出警告。为避免这些警告，应对四元数进行归一化：

.. code-block:: cpp

   q.normalize();

ROS 2 中的四元数类型
--------------------

ROS 2 使用两种四元数数据类型：tf2::Quaternion 及其等价类型 geometry_msgs::msg::Quaternion。

在 C++ 中，可以使用 tf2_geometry_msgs 提供的方法进行转换：

.. code-block:: cpp

   #include <tf2_geometry_msgs/tf2_geometry_msgs.hpp>

   tf2::Quaternion tf2_quat, tf2_quat_from_msg;
   tf2_quat.setRPY(roll, pitch, yaw);

   // tf2::Quaternion 转换为 geometry_msgs::msg::Quaternion
   geometry_msgs::msg::Quaternion msg_quat = tf2::toMsg(tf2_quat);

   // geometry_msgs::msg::Quaternion 转换为 tf2::Quaternion
   tf2::convert(msg_quat, tf2_quat_from_msg);
   // 或者
   tf2::fromMsg(msg_quat, tf2_quat_from_msg);

Python 中没有 tf2::Quaternion 的等价类型，而是使用内置 list：

.. code-block:: python

   from geometry_msgs.msg import Quaternion

   # 创建与 tf2 四元数方法兼容的浮点数列表
   quat_tf = [0.0, 1.0, 0.0, 0.0]

   # 将列表转换为 geometry_msgs.msg.Quaternion
   msg_quat = Quaternion(
       x=quat_tf[0], y=quat_tf[1], z=quat_tf[2], w=quat_tf[3])

四元数操作
----------

1. 先使用 RPY 思考，再转换为四元数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

人们很容易理解绕各坐标轴的旋转，但不容易直接理解四元数。建议先使用三个独立旋转量计算目标方向：

* roll：绕 X 轴旋转。
* pitch：绕 Y 轴旋转。
* yaw：绕 Z 轴旋转。

然后再将 RPY 转换为四元数。

.. code-block:: python

   # 可使用 quaternion_from_euler 方法将欧拉角转换为四元数

2. 四元数归一化
^^^^^^^^^^^^^^^

在进行旋转计算时，应确保四元数为单位四元数。若经过计算后出现数值误差，可以调用 normalize() 对其归一化。

3. 注意分量顺序
^^^^^^^^^^^^^^^

在 ROS 2 消息中，四元数分量顺序为 x、y、z、w。使用其他库时，应确认其分量顺序，避免将不同约定的数据直接混用。
