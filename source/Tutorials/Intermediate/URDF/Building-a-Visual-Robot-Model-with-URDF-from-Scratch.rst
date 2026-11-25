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

.. code-block:: console

   $ ros2 launch urdf_tutorial display.launch.py model:=urdf/02-multipleshapes.urdf

.. image:: https://raw.githubusercontent.com/ros/urdf_tutorial/ros2/images/multipleshapes.png
   :width: 800
   :alt: 多个形状

两个形状会发生重叠，因为它们共享相同的原点。如果希望它们不再重叠，就必须定义更多原点。

原点（Origins）
---------------

R2D2 的腿连接在躯干上半部分的侧面，因此需要将关节原点设置在该位置。

此外，关节并不是连接在腿部的中心，而是连接在腿部上端，因此还需要偏移腿部可视化元素的原点。同时，需要旋转腿部，使其保持直立。

完整示例可参阅 ¤03-origins.urdf 源码 <https://github.com/ros/urdf_tutorial/blob/ros2/urdf/03-origins.urdf>¤_：

.. code-block:: xml

   <?xml version="1.0"?>
   <robot name="origins">
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
         <origin rpy="0 1.57075 0" xyz="0 0 -0.3"/>
       </visual>
     </link>

     <joint name="base_to_right_leg" type="fixed">
       <parent link="base_link"/>
       <child link="right_leg"/>
       <origin xyz="0 -0.22 0.25"/>
     </joint>
   </robot>

这里需要理解两个不同的原点：

* 先看关节的原点。它是相对于父连杆参考坐标系定义的。示例中，关节沿 y 轴偏移 -0.22 米，沿 z 轴偏移 0.25 米。这意味着子连杆原点会向上、向右移动，而不受子连杆 visual 原点标签的影响。由于没有指定 rpy（roll、pitch、yaw）属性，子坐标系默认与父坐标系保持相同方向。
* 再看腿部 visual 的原点。它同时设置了 xyz 和 rpy 偏移，用于定义可视化元素中心相对于其原点的位置。为了让腿部连接在躯干上端，将 z 偏移设置为 -0.3 米。为了让腿部较长的方向与 z 轴平行，将可视化部分绕 Y 轴旋转 PI/2。

运行示例：

.. code-block:: console

   $ ros2 launch urdf_tutorial display.launch.py model:=urdf/03-origins.urdf

.. image:: https://raw.githubusercontent.com/ros/urdf_tutorial/ros2/images/origins.png
   :width: 800
   :alt: 原点设置示意图

还需要注意：

* 启动文件会运行相关节点，根据 URDF 为模型中的每个连杆创建 TF 坐标系。RViz 使用这些信息确定每个形状的显示位置。
* 如果某个 URDF 连杆不存在对应的 TF 坐标系，它就会被放置在原点，并以白色显示。更多说明可参阅 ¤相关问题 <http://answers.ros.org/question/207947/how-do-you-use-externally-defined-materials-in-a-urdfxacro-file/>¤_。

材质（Materials）
-----------------

目前模型已经有了基本形状，但还不能方便地为不同部件指定颜色。接下来介绍 §material§ 标签。

完整示例可参阅 ¤04-materials.urdf 源码 <https://github.com/ros/urdf_tutorial/blob/ros2/urdf/04-materials.urdf>¤_：

.. code-block:: xml

   <?xml version="1.0"?>
   <robot name="materials">

     <material name="blue">
       <color rgba="0 0 0.8 1"/>
     </material>

     <material name="white">
       <color rgba="1 1 1 1"/>
     </material>

     <link name="base_link">
       <visual>
         <geometry>
           <cylinder length="0.6" radius="0.2"/>
         </geometry>
         <material name="blue"/>
       </visual>
     </link>

     <link name="right_leg">
       <visual>
         <geometry>
           <box size="0.6 0.1 0.2"/>
         </geometry>
         <origin rpy="0 1.57075 0" xyz="0 0 -0.3"/>
         <material name="white"/>
       </visual>
     </link>

     <joint name="base_to_right_leg" type="fixed">
       <parent link="base_link"/>
       <child link="right_leg"/>
       <origin xyz="0 -0.22 0.25"/>
     </joint>

     <link name="left_leg">
       <visual>
         <geometry>
           <box size="0.6 0.1 0.2"/>
         </geometry>
         <origin rpy="0 1.57075 0" xyz="0 0 -0.3"/>
         <material name="white"/>
       </visual>
     </link>

     <joint name="base_to_left_leg" type="fixed">
       <parent link="base_link"/>
       <child link="left_leg"/>
       <origin xyz="0 0.22 0.25"/>
     </joint>
   </robot>

这里可以看到：

* 躯干现在是蓝色的。我们定义了名为 §blue§ 的新材质，其红、绿、蓝和 alpha 通道分别为 0、0、0.8 和 1。所有数值都可以在 §[0, 1]§ 范围内取值。随后在 §base_link§ 的 visual 元素中引用该材质。白色材质采用相同方式定义。
* 也可以直接在 visual 元素内部定义 material 标签，并在其他连杆中引用。即使重新定义同名材质，解析器也不会因此报错。
* 还可以使用纹理指定图像文件，为对象表面着色。

运行示例：

.. code-block:: console

   $ ros2 launch urdf_tutorial display.launch.py model:=urdf/04-materials.urdf

.. image:: https://raw.githubusercontent.com/ros/urdf_tutorial/ros2/images/materials.png
   :width: 800
   :alt: 材质设置示意图

完成模型（Finishing the Model）
--------------------------------

现在继续为模型添加一些形状：脚部、车轮和头部。最值得注意的是，我们会添加一个球体和一些网格模型。此外，还会添加后续教程中需要使用的其他部件。

完整示例可参阅 ¤05-visual.urdf 源码 <https://github.com/ros/urdf_tutorial/blob/ros2/urdf/05-visual.urdf>¤_：

.. code-block:: xml

   <?xml version="1.0"?>
   <robot name="visual">

     <material name="blue">
       <color rgba="0 0 0.8 1"/>
     </material>
     <material name="black">
       <color rgba="0 0 0 1"/>
     </material>
     <material name="white">
       <color rgba="1 1 1 1"/>
     </material>

     <link name="base_link">
       <visual>
         <geometry>
           <cylinder length="0.6" radius="0.2"/>
         </geometry>
         <material name="blue"/>
       </visual>
     </link>

     <link name="right_leg">
       <visual>
         <geometry>
           <box size="0.6 0.1 0.2"/>
         </geometry>
         <origin rpy="0 1.57075 0" xyz="0 0 -0.3"/>
         <material name="white"/>
       </visual>
     </link>

     <joint name="base_to_right_leg" type="fixed">
       <parent link="base_link"/>
       <child link="right_leg"/>
       <origin xyz="0 -0.22 0.25"/>
     </joint>

     <link name="right_base">
       <visual>
         <geometry>
           <box size="0.4 0.1 0.1"/>
         </geometry>
         <material name="white"/>
       </visual>
     </link>

     <joint name="right_base_joint" type="fixed">
       <parent link="right_leg"/>
       <child link="right_base"/>
       <origin xyz="0 0 -0.6"/>
     </joint>

     <link name="right_front_wheel">
       <visual>
         <origin rpy="1.57075 0 0" xyz="0 0 0"/>
         <geometry>
           <cylinder length="0.1" radius="0.035"/>
         </geometry>
         <material name="black"/>
       </visual>
     </link>
     <joint name="right_front_wheel_joint" type="fixed">
       <parent link="right_base"/>
       <child link="right_front_wheel"/>
       <origin rpy="0 0 0" xyz="0.133333333333 0 -0.085"/>
     </joint>

     <link name="right_back_wheel">
       <visual>
         <origin rpy="1.57075 0 0" xyz="0 0 0"/>
         <geometry>
           <cylinder length="0.1" radius="0.035"/>
         </geometry>
         <material name="black"/>
       </visual>
     </link>
     <joint name="right_back_wheel_joint" type="fixed">
       <parent link="right_base"/>
       <child link="right_back_wheel"/>
       <origin rpy="0 0 0" xyz="-0.133333333333 0 -0.085"/>
     </joint>

     <link name="left_leg">
       <visual>
         <geometry>
           <box size="0.6 0.1 0.2"/>
         </geometry>
         <origin rpy="0 1.57075 0" xyz="0 0 -0.3"/>
         <material name="white"/>
       </visual>
     </link>

     <joint name="base_to_left_leg" type="fixed">
       <parent link="base_link"/>
       <child link="left_leg"/>
       <origin xyz="0 0.22 0.25"/>
     </joint>

     <link name="left_base">
       <visual>
         <geometry>
           <box size="0.4 0.1 0.1"/>
         </geometry>
         <material name="white"/>
       </visual>
     </link>

     <joint name="left_base_joint" type="fixed">
       <parent link="left_leg"/>
       <child link="left_base"/>
       <origin xyz="0 0 -0.6"/>
     </joint>

     <link name="left_front_wheel">
       <visual>
         <origin rpy="1.57075 0 0" xyz="0 0 0"/>
         <geometry>
           <cylinder length="0.1" radius="0.035"/>
         </geometry>
         <material name="black"/>
       </visual>
     </link>
     <joint name="left_front_wheel_joint" type="fixed">
       <parent link="left_base"/>
       <child link="left_front_wheel"/>
       <origin rpy="0 0 0" xyz="0.133333333333 0 -0.085"/>
     </joint>

     <link name="left_back_wheel">
       <visual>
         <origin rpy="1.57075 0 0" xyz="0 0 0"/>
         <geometry>
           <cylinder length="0.1" radius="0.035"/>
         </geometry>
         <material name="black"/>
       </visual>
     </link>
     <joint name="left_back_wheel_joint" type="fixed">
       <parent link="left_base"/>
       <child link="left_back_wheel"/>
       <origin rpy="0 0 0" xyz="-0.133333333333 0 -0.085"/>
     </joint>

     <joint name="gripper_extension" type="fixed">
       <parent link="base_link"/>
       <child link="gripper_pole"/>
       <origin rpy="0 0 0" xyz="0.19 0 0.2"/>
     </joint>

     <link name="gripper_pole">
       <visual>
         <geometry>
           <cylinder length="0.2" radius="0.01"/>
         </geometry>
         <origin rpy="0 1.57075 0 " xyz="0.1 0 0"/>
       </visual>
     </link>

     <joint name="left_gripper_joint" type="fixed">
       <origin rpy="0 0 0" xyz="0.2 0.01 0"/>
       <parent link="gripper_pole"/>
       <child link="left_gripper"/>
     </joint>

     <link name="left_gripper">
       <visual>
         <origin rpy="0.0 0 0" xyz="0 0 0"/>
         <geometry>
           <mesh filename="package://urdf_tutorial/meshes/l_finger.dae"/>
         </geometry>
       </visual>
     </link>

     <joint name="left_tip_joint" type="fixed">
       <parent link="left_gripper"/>
       <child link="left_tip"/>
     </joint>

     <link name="left_tip">
       <visual>
         <origin rpy="0.0 0 0" xyz="0.09137 0.00495 0"/>
         <geometry>
           <mesh filename="package://urdf_tutorial/meshes/l_finger_tip.dae"/>
         </geometry>
       </visual>
     </link>

     <joint name="right_gripper_joint" type="fixed">
       <origin rpy="0 0 0" xyz="0.2 -0.01 0"/>
       <parent link="gripper_pole"/>
       <child link="right_gripper"/>
     </joint>

     <link name="right_gripper">
       <visual>
         <origin rpy="-3.1415 0 0" xyz="0 0 0"/>
         <geometry>
           <mesh filename="package://urdf_tutorial/meshes/l_finger.dae"/>
         </geometry>
       </visual>
     </link>

     <joint name="right_tip_joint" type="fixed">
       <parent link="right_gripper"/>
       <child link="right_tip"/>
     </joint>

     <link name="right_tip">
       <visual>
         <origin rpy="-3.1415 0 0" xyz="0.09137 0.00495 0"/>
         <geometry>
           <mesh filename="package://urdf_tutorial/meshes/l_finger_tip.dae"/>
         </geometry>
       </visual>
     </link>

     <link name="head">
       <visual>
         <geometry>
           <sphere radius="0.2"/>
         </geometry>
         <material name="white"/>
       </visual>
     </link>
     <joint name="head_swivel" type="fixed">
       <parent link="base_link"/>
       <child link="head"/>
       <origin xyz="0 0 0.3"/>
     </joint>

     <link name="box">
       <visual>
         <geometry>
           <box size="0.08 0.08 0.08"/>
         </geometry>
         <material name="blue"/>
       </visual>
     </link>

     <joint name="tobox" type="fixed">
       <parent link="head"/>
       <child link="box"/>
       <origin xyz="0.1814 0 0.1414"/>
     </joint>
   </robot>

构建并显示完整模型：

.. code-block:: console

   $ ros2 launch urdf_tutorial display.launch.py model:=urdf/05-visual.urdf

.. image:: https://raw.githubusercontent.com/ros/urdf_tutorial/ros2/images/visual.png
   :width: 800
   :alt: 完整可视化模型

添加球体的方式比较直观：

.. code-block:: xml

   <link name="head">
     <visual>
       <geometry>
         <sphere radius="0.2"/>
       </geometry>
       <material name="white"/>
     </visual>
   </link>

这里使用的网格模型来自 PR2。它们是独立文件，需要指定文件路径。建议使用 §package://包名/路径§ 的格式。

本教程使用的网格文件位于 §urdf_tutorial§ 功能包的 §meshes§ 目录中：

.. code-block:: xml

   <link name="left_gripper">
     <visual>
       <origin rpy="0.0 0 0" xyz="0 0 0"/>
       <geometry>
         <mesh filename="package://urdf_tutorial/meshes/l_finger.dae"/>
       </geometry>
     </visual>
   </link>

关于网格模型，还需要注意：

* 网格模型可以使用多种文件格式。STL 比较常见，渲染引擎也支持 DAE。DAE 文件可以包含自身的颜色数据，因此不一定需要额外指定颜色或材质。通常这些颜色信息位于单独的文件中，示例网格会引用 meshes 目录中的 §.tif§ 文件。
* 可以通过相对缩放参数或包围盒尺寸调整网格模型大小。
* 网格模型也可以引用完全不同功能包中的资源。

至此，一个类似 R2D2 的 URDF 可视化模型就完成了。

接下来可以继续学习 :doc:`让模型运动 <./Building-a-Movable-Robot-Model-with-URDF>`。


后续教程会继续介绍如何设置连杆原点、材质和可运动关节，并逐步构建完整的 R2D2 模型。
