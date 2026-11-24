.. redirect-from::

    Tutorials/URDF/Using-Xacro-to-Clean-Up-a-URDF-File

.. _URDFXacro:

使用 Xacro 简化 URDF 代码
=========================

**目标：** 学习如何使用 Xacro 减少 URDF 文件中的重复代码。

**教程级别：** 中级 | **预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

``xacro`` 软件包可以简化机器人描述，主要提供三项功能：常量、简单数学表达式和宏。本教程介绍这些功能，帮助缩短 URDF 文件并提高可读性和可维护性。

使用 Xacro
----------

``xacro`` 是一种面向 XML 的宏语言。程序会执行文件中的宏，并输出处理后的 URDF。典型用法：

.. code-block:: console

   $ xacro model.xacro > model.urdf

也可以在启动文件中自动生成 URDF。这样模型始终保持最新状态，也不需要额外占用磁盘空间，但会增加启动时间。

在启动文件中运行 xacro，可以将 ``Command`` 替换作为参数传递给 ``robot_state_publisher``。也可以使用 ``urdf_launch`` 软件包自动加载 xacro/urdf。

Xacro 文件顶部必须声明命名空间：

.. code-block:: xml

   <?xml version="1.0"?>
   <robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="firefighter">

常量
----

如果视觉和碰撞几何体使用相同尺寸，传统 URDF 需要重复填写数值。Xacro 允许定义 property：

.. code-block:: xml

   <xacro:property name="width" value="0.2" />
   <xacro:property name="bodylen" value="0.6" />
   <link name="base_link">
     <visual>
       <geometry>
         <cylinder radius="${width}" length="${bodylen}"/>
       </geometry>
     </visual>
     <collision>
       <geometry>
         <cylinder radius="${width}" length="${bodylen}"/>
       </geometry>
     </collision>
   </link>

两个值在前面定义，之后通过 ``${}`` 语法引用。处理后的 URDF 与重复填写数值的版本等价。

属性值也可以与其他文本组合：

.. code-block:: xml

   <xacro:property name="robotname" value="marvin" />
   <link name="${robotname}s_leg" />

会生成 ``<link name="marvins_leg" />``。

数学表达式
----------

``${}`` 中不仅可以引用 property，还可以使用数学表达式进行计算。例如，可以通过表达式计算尺寸、偏移量和角度，减少手动计算和重复数值。

宏
--

Xacro 宏可以将重复的 XML 结构封装起来，并通过参数复用。对于包含多个相似连杆、关节或传感器的机器人，可以定义宏并为不同部件传入不同参数。

总结
----

Xacro 通过 property、数学表达式和宏简化 URDF 文件。机器人模型包含大量重复几何体、连杆和关节时，使用 Xacro 可以统一管理参数并提高可维护性。
