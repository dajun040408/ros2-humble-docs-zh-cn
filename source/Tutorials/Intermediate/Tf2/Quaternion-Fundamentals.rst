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

可以在 `Wikipedia <https://en.wikipedia.org/wiki/Quaternion>`_ 上了解相关数学概念，也可以观看由 `3Blue1Brown <https://www.youtube.com/3blue1brown>`_ 制作的 `Visualizing quaternions <https://eater.net/quaternions>`_ 交互式视频系列。

本教程将介绍 ROS 2 中四元数的工作方式和转换方法。

前置条件
--------

可以参考 `transforms3d <https://github.com/matthew-brett/transforms3d>`_、`scipy.spatial.transform <https://github.com/scipy/scipy/tree/master/scipy/spatial/transform>`_、`pytransform3d <https://github.com/rock-learning/pytransform3d>`_、`numpy-quaternion <https://github.com/moble/quaternion>`_ 或 `blender.mathutils <https://docs.blender.org/api/master/mathutils.html>`_ 等库。这些库并非硬性要求，也可以使用自己熟悉的其他几何变换库。

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

人们很容易理解绕各坐标轴的旋转，但不容易直接理解四元数。建议先使用三个独立旋转量计算目标方向：roll（绕 X 轴旋转）、pitch（绕 Y 轴旋转）和 yaw（绕 Z 轴旋转），然后再将 RPY 转换为四元数。

.. code-block:: python

   # quaternion_from_euler 方法可用于将欧拉角转换为四元数
   q = quaternion_from_euler(1.5707, 0, -1.5707)
   print(f'The quaternion representation is x: {q[0]} y: {q[1]} z: {q[2]} w: {q[3]}.')

这种方法与 `Euler angles <https://en.wikipedia.org/wiki/Euler_angles>`_（欧拉角）有关。欧拉角有多种应用方式。上面介绍的方式是 ROS 2 采用的固定坐标系（或静态坐标系）RPY，意味着三个独立旋转都围绕原始且不移动的坐标轴执行。

这与相对坐标系不同：相对坐标系中的旋转会作用于之前旋转已经改变的坐标轴。

2. 应用四元数旋转
^^^^^^^^^^^^^^^^

要将一个四元数表示的旋转应用到位姿上，只需将表示目标旋转的四元数与位姿原有四元数相乘即可。注意，乘法顺序非常重要。

C++：

.. code-block:: c++

   #include <tf2_geometry_msgs/tf2_geometry_msgs.hpp>

   tf2::Quaternion q_orig, q_rot, q_new;

   q_orig.setRPY(0.0, 0.0, 0.0);
   // 将原有位姿绕 X 轴旋转 180 度
   q_rot.setRPY(3.14159, 0.0, 0.0);
   q_new = q_rot * q_orig;
   q_new.normalize();

Python：

.. code-block:: python

   q_orig = quaternion_from_euler(0, 0, 0)
   # 将原有位姿绕 X 轴旋转 180 度
   q_rot = quaternion_from_euler(3.14159, 0, 0)
   q_new = quaternion_multiply(q_rot, q_orig)

3. 求四元数的逆
^^^^^^^^^^^^^^^

一种简单的四元数求逆方法是将 x、y 和 z 分量取反：

.. code-block:: python

   q[0] = -q[0]
   q[1] = -q[1]
   q[2] = -q[2]

.. note::

   注意，这与将四元数的所有分量全部取反不同。

4. 相对旋转
^^^^^^^^^^^

假设有两个来自同一坐标系的四元数 ``q_1`` 和 ``q_2``。希望找到相对旋转 ``q_r``，使其能够将 ``q_1`` 转换为 ``q_2``：

.. code-block:: c++

   q_2 = q_r * q_1

可以像求解矩阵方程一样求解 ``q_r``：对 ``q_1`` 求逆，并在等式两侧右乘其逆。再次强调，乘法顺序非常重要：

.. code-block:: c++

   q_r = q_2 * q_1_inverse

下面的 Python 示例演示如何计算机器人从上一时刻位姿到当前位姿的相对旋转：

.. code-block:: python

   def quaternion_multiply(q0, q1):
       """
       计算两个四元数的乘积。

       输入：
       q0：包含第一个四元数的 4 元素数组
       q1：包含第二个四元数的 4 元素数组

       输出：
       返回包含最终四元数的 4 元素数组，顺序为 (w, x, y, z)。
       """
       x0 = q0[0]
       y0 = q0[1]
       z0 = q0[2]
       w0 = q0[3]

       x1 = q1[0]
       y1 = q1[1]
       z1 = q1[2]
       w1 = q1[3]

       q0q1_w = w0 * w1 - x0 * x1 - y0 * y1 - z0 * z1
       q0q1_x = w0 * x1 + x0 * w1 + y0 * z1 - z0 * y1
       q0q1_y = w0 * y1 - x0 * z1 + y0 * w1 + z0 * x1
       q0q1_z = w0 * z1 + x0 * y1 - y0 * x1 + z0 * w1

       final_quaternion = np.array([q0q1_w, q0q1_x, q0q1_y, q0q1_z])
       return final_quaternion

   q1_inv[0] = -prev_pose.pose.orientation.x
   q1_inv[1] = -prev_pose.pose.orientation.y
   q1_inv[2] = -prev_pose.pose.orientation.z
   q1_inv[3] = prev_pose.pose.orientation.w

   q2[0] = current_pose.pose.orientation.x
   q2[1] = current_pose.pose.orientation.y
   q2[2] = current_pose.pose.orientation.z
   q2[3] = current_pose.pose.orientation.w

   qr = quaternion_multiply(q2, q1_inv)

总结
----

本教程介绍了四元数的基本概念及其相关数学操作，例如求逆和旋转；还介绍了四元数在 ROS 2 中的使用示例，以及两种不同 Quaternion 类型之间的转换方法。
