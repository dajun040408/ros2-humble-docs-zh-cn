.. redirect-from::

    Tutorials/URDF/Building-a-Visual-Robot-Model-with-URDF-from-Scratch

.. _BuildingURDF:

从零开始构建可视化机器人模型
============================

**目标：** 学习如何构建可在 RViz 中查看的机器人可视化模型。

**教程级别：** 中级 | **预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

.. note:: 本教程假设你了解格式规范的 XML 编写方式。

本教程将构建一个外形类似 R2D2 的机器人可视化模型。后续教程会介绍如何 :doc:`添加可运动关节 <./Building-a-Movable-Robot-Model-with-URDF>`、:doc:`添加物理属性 <./Adding-Physical-and-Collision-Properties-to-a-URDF-Model>`，以及 :doc:`使用 xacro 简化代码 <./Using-Xacro-to-Clean-Up-a-URDF-File>`。

前置条件
--------

请确保已安装 ``joint_state_publisher``。如果通过二进制方式安装 ``urdf_tutorial``，通常已经包含该依赖；否则请更新安装，并使用 rosdep 检查依赖。

一个形状
--------

下面是一个最简单的 URDF：

.. code-block:: xml

    <?xml version="1.0"?>
    <robot name="myfirst">
      <link name="base_link">
        <visual>
          <geometry>
            <cylinder length="0.6" radius="0.2"/>
          </geometry>
        </visual>
      </link>
    </robot>

这段 XML 定义了一个名为 ``myfirst`` 的机器人，其中只有一个连杆 ``base_link``。该连杆的可视化部分是一个长度为 0.6 米、半径为 0.2 米的圆柱体。

运行 ``display.launch.py`` 查看模型：

.. code-block:: console

  $ ros2 launch urdf_tutorial display.launch.py model:=urdf/01-myfirst.urdf

该启动文件会加载指定模型并将其作为参数传递给 ``robot_state_publisher``，启动发布 ``JointState`` 和 TF 的节点，并使用配置文件启动 RViz。

.. image:: https://raw.githubusercontent.com/ros/urdf_tutorial/ros2/images/myfirst.png
  :width: 800
  :alt: 第一个 URDF 模型

需要注意，Fixed Frame 是网格中心所在的变换坐标系，本例由 ``base_link`` 定义。``visual`` 元素的原点默认位于几何体中心，因此圆柱体有一半位于网格平面以下。

多个形状
--------

如果只在 URDF 中增加更多 ``link`` 元素，解析器并不知道应该将它们放在哪里，因此必须添加关节。先从固定关节开始：

.. code-block:: xml

    <?xml version="1.0"?>
    <robot name="multipleshapes">
      <link name="base_link">
        <visual>
          <geometry>
            <cylinder length="0.6" radius="0.2"/>
          </geometry>
        </visual>
      </link>
      <link name="right_leg">
        <visual>
          <geometry>
            <box size="0.6 0.1 0.2"/>
          </geometry>
        </visual>
      </link>
      <joint name="base_to_right_leg" type="fixed">
        <parent link="base_link"/>
        <child link="right_leg"/>
      </joint>
    </robot>

这里定义了一个尺寸为 ``0.6m × 0.1m × 0.2m`` 的长方体。关节通过父连杆和子连杆定义。URDF 本质上是一棵只有一个根连杆的树，因此腿部的位置取决于 ``base_link`` 的位置。

后续内容
--------

后续教程会继续介绍如何设置连杆原点、材质和可运动关节，并逐步构建完整的 R2D2 模型。
