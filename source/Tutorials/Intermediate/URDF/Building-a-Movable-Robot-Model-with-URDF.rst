.. redirect-from::

    Tutorials/URDF/Building-a-Movable-Robot-Model-with-URDF

.. _MoveableURDF:

构建可运动的机器人模型
======================

**目标：** 学习如何在 URDF 中定义可运动关节。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

本教程将修改上一个教程中创建的 R2D2 模型，使其包含可运动关节。之前的模型中，所有关节都是固定的。现在我们将介绍另外三种重要关节：连续关节（continuous）、旋转关节（revolute）和平移关节（prismatic）。

继续之前，请确保已经安装所有前置依赖。所需内容请参阅 :doc:`上一个教程 <./Building-a-Visual-Robot-Model-with-URDF-from-Scratch>`。

本教程中提到的所有机器人模型都可以在 ``urdf_tutorial`` 软件包中找到。

`新的 URDF 文件 <https://github.com/ros/urdf_tutorial/blob/ros2/urdf/06-flexible.urdf>`_ 定义了可活动关节。你可以与上一个版本进行比较，查看所有变化；本教程重点介绍三个关节示例。

运行与上一个教程相同的命令，可视化并控制模型：

.. code-block:: console

  $ ros2 launch urdf_tutorial display.launch.py model:=urdf/06-flexible.urdf

这次还会弹出一个 GUI，可以控制所有非固定关节的数值。尝试拖动滑块，观察模型的运动，然后了解其实现方式。

.. image:: https://raw.githubusercontent.com/ros/urdf_tutorial/ros2/images/flexible.png
  :width: 800
  :alt: 可活动关节模型截图

头部
----

.. code-block:: xml

  <joint name="head_swivel" type="continuous">
    <parent link="base_link"/>
    <child link="head"/>
    <axis xyz="0 0 1"/>
    <origin xyz="0 0 0.3"/>
  </joint>

机身与头部之间使用连续关节连接，这意味着关节角度可以从负无穷变化到正无穷。车轮也采用这种方式建模，因此可以持续向任意方向滚动。

需要添加的额外信息是旋转轴，这里通过 xyz 三元组指定一个向量，表示头部围绕哪个轴旋转。由于希望头部绕 z 轴旋转，因此指定向量 ``0 0 1``。

夹爪
----

.. code-block:: xml

  <joint name="left_gripper_joint" type="revolute">
    <axis xyz="0 0 1"/>
    <limit effort="1000.0" lower="0.0" upper="0.548" velocity="0.5"/>
    <origin rpy="0 0 0" xyz="0.2 0.01 0"/>
    <parent link="gripper_pole"/>
    <child link="left_gripper"/>
  </joint>

左右夹爪关节都建模为旋转关节。它们与连续关节一样可以旋转，但具有严格的角度限制。因此，必须添加 ``limit`` 标签，指定关节的上下限（单位为弧度）。还必须指定最大速度和最大作用力，但在本教程中，这些数值并不重要。

夹爪臂
------

.. code-block:: xml

  <joint name="gripper_extension" type="prismatic">
    <parent link="base_link"/>
    <child link="gripper_pole"/>
    <limit effort="1000.0" lower="-0.38" upper="0" velocity="0.5"/>
    <origin rpy="0 0 0" xyz="0.19 0 0.2"/>
  </joint>

夹爪臂使用另一种关节类型，即平移关节。它沿某个轴移动，而不是绕轴旋转。这种平移运动使机器人能够伸出和收回夹爪臂。

平移关节的限位方式与旋转关节相同，但单位是米，而不是弧度。

其他关节类型
------------

还有另外两种可以在空间中运动的关节。

平移关节只能沿一个维度移动，而平面关节（planar）可以在一个平面内运动，即两个维度。浮动关节（floating）则没有约束，可以在三个维度中自由运动。

这些关节不能只用一个数值描述，因此不包含在本教程中。

指定位姿
--------

在 GUI 中拖动滑块时，Rviz 中的模型会随之运动。这是如何实现的？

首先，``joint_state_publisher_gui`` 会解析 URDF，找到所有非固定关节及其限位。然后，它使用滑块数值发布 ``sensor_msgs/msg/JointState`` 消息。``robot_state_publisher`` 使用这些消息计算不同部件之间的所有变换。最终得到的变换树用于在 Rviz 中显示所有几何形状。

后续步骤
--------

现在已经获得一个可交互的机器人模型，可以继续 :doc:`添加物理属性和碰撞属性 <./Adding-Physical-and-Collision-Properties-to-a-URDF-Model>`，或者 :doc:`使用 xacro 简化 URDF 文件 <./Using-Xacro-to-Clean-Up-a-URDF-File>`。
