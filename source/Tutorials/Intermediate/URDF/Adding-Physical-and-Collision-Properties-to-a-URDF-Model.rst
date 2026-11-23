.. redirect-from::

    Tutorials/URDF/Adding-Physical-and-Collision-Properties-to-a-URDF-Model

.. _URDFProperties:

添加物理属性和碰撞属性
======================

**目标：** 学习如何为连杆添加碰撞和惯性属性，以及为关节添加动力学属性。

**教程级别：** 中级 | **预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

碰撞属性
--------

此前，我们只为连杆指定了 §visual§ 子元素，用于定义机器人外观。但若要进行碰撞检测或机器人仿真，还需要定义 §collision§ 元素。

§collision§ 是 §link§ 的直接子元素，与 §visual§ 位于同一层级。其形状通过 §geometry§ 标签定义，格式与 §visual§ 相同，也可以指定 §origin§。

.. code-block:: xml

   <link name="base_link">
     <visual>
       <geometry>
         <cylinder length="0.6" radius="0.2"/>
       </geometry>
       <material name="blue">
         <color rgba="0 0 .8 1"/>
       </material>
     </visual>
     <collision>
       <geometry>
         <cylinder length="0.6" radius="0.2"/>
       </geometry>
     </collision>
   </link>

很多情况下，碰撞几何体与视觉几何体相同，但也有两种情况需要区分：

* **提高处理效率：** 两个网格之间的碰撞检测比两个简单几何体之间的检测复杂得多，因此可以在 §collision§ 中使用简单几何体替代复杂网格。
* **设置安全区域：** 对敏感设备附近的运动进行限制。例如，可以为 R2D2 的头部定义一个包围头部的圆柱体，避免其他物体过于靠近。

物理属性
--------

为了让物理引擎（例如 Gazebo）正确仿真机器人，需要定义机器人的物理属性。

惯性
^^^^

每个参与仿真的 §link§ 都需要包含 §inertial§ 标签：

.. code-block:: xml

   <link name="base_link">
     <visual>
       <geometry>
         <cylinder length="0.6" radius="0.2"/>
       </geometry>
     </visual>
     <collision>
       <geometry>
         <cylinder length="0.6" radius="0.2"/>
       </geometry>
     </collision>
     <inertial>
       <mass value="10"/>
       <inertia ixx="1e-3" ixy="0.0" ixz="0.0"
                iyy="1e-3" iyz="0.0" izz="1e-3"/>
     </inertial>
   </link>

§inertial§ 同样是 §link§ 的子元素。质量通过 §mass§ 指定，单位为千克；§inertia§ 定义 3×3 转动惯量矩阵。由于该矩阵对称，只需指定 6 个独立元素：§ixx§、§ixy§、§ixz§、§iyy§、§iyz§ 和 §izz§。

MeshLab 等建模工具可以提供惯性信息。圆柱体、长方体和球体等基本几何体的惯性张量也可以根据质量和形状计算。惯性张量取决于物体质量及质量分布，初步建模时可假设质量均匀分布。

关节动力学
----------

URDF 还允许在关节中指定动力学属性，例如阻尼和摩擦。这些参数可用于改善物理仿真中的运动表现，应依据实际机构和仿真需求设置。

总结
----

本教程介绍了 URDF 中的 §collision§ 和 §inertial§ 元素，以及碰撞几何体简化、安全区域、质量和转动惯量等基本概念。参与物理仿真的连杆需要合理的物理参数。
