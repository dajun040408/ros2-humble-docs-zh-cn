.. redirect-from::

    Tutorials/URDF/Using-Xacro-to-Clean-Up-a-URDF-File

.. _URDFXacro:

使用 Xacro 简化 URDF 代码
=========================

**目标：** 学习如何使用 Xacro 减少 URDF 文件中的重复代码。

**教程级别：** 中级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

如果你一直按照教程步骤使用自己的机器人模型，可能已经厌倦了为了让简单的机器人描述正确解析而进行各种计算。

幸运的是，可以使用 `xacro <https://index.ros.org/p/xacro>`_ 功能包简化这一过程。它提供三项非常有用的功能：

* 常量（Constants）
* 简单数学表达式（Simple Math）
* 宏（Macros）

本教程将介绍这些功能，帮助减少 URDF 文件中的代码量，并提高可读性和可维护性。

使用 Xacro
----------

顾名思义，``xacro`` 是一种面向 XML 的宏语言。``xacro`` 程序会执行文件中的宏，并输出处理后的结果。典型用法如下：

.. code-block:: console

   $ xacro model.xacro > model.urdf

也可以在启动文件中自动生成 URDF。这样可以确保模型始终保持最新状态，而且不会额外占用硬盘空间。不过，生成过程需要时间，因此启动文件可能会花费更长时间才能启动。

在启动文件中运行 ``xacro``，需要将 ``Command`` 替换作为参数传递给 ``robot_state_publisher``：

.. code-block:: python

   path_to_urdf = get_package_share_path('turtlebot3_description') / 'urdf' / 'turtlebot3_burger.urdf'
   robot_state_publisher_node = launch_ros.actions.Node(
       package='robot_state_publisher',
       executable='robot_state_publisher',
       parameters=[{
           'robot_description': ParameterValue(
               Command(['xacro ', str(path_to_urdf)]), value_type=str
           )
       }]
   )

更简单的加载机器人模型方式是使用 `urdf_launch <https://github.com/ros/urdf_launch>`_ 功能包，自动加载 xacro/urdf 文件。

.. literalinclude:: launch/urdf_display_launch.py
   :language: python

URDF 文件顶部必须声明命名空间，否则文件无法正确解析。例如，合法的 xacro 文件前两行如下：

.. code-block:: xml

   <?xml version="1.0"?>
   <robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="firefighter">

常量
----

先看一下 R2D2 模型中的 ``base_link``：

.. code-block:: xml

   <link name="base_link">
     <visual>
       <geometry>
         <cylinder length="0.6" radius="0.2"/>
       </geometry>
       <material name="blue"/>
     </visual>
     <collision>
       <geometry>
         <cylinder length="0.6" radius="0.2"/>
       </geometry>
     </collision>
   </link>

这里存在一些冗余信息：圆柱体的长度和半径被重复指定了两次。更麻烦的是，如果想修改尺寸，就必须在两个不同的位置分别修改。

Xacro 允许定义类似常量的 property。可以将上面的代码改写为：

.. code-block:: xml

   <xacro:property name="width" value="0.2" />
   <xacro:property name="bodylen" value="0.6" />
   <link name="base_link">
       <visual>
           <geometry>
               <cylinder radius="${width}" length="${bodylen}"/>
           </geometry>
           <material name="blue"/>
       </visual>
       <collision>
           <geometry>
               <cylinder radius="${width}" length="${bodylen}"/>
           </geometry>
       </collision>
   </link>

这里需要注意：

* 前两行定义了两个值。只要符合 XML 语法，就可以在文件中几乎任意位置定义 property，既可以在使用前，也可以在使用后。通常将它们放在文件顶部。
* 不再直接填写几何体的半径和长度，而是使用美元符号和花括号引用对应的值。
* 处理后的代码与前面展示的代码等价。

``${}`` 结构中的内容会被用于替换对应位置的 ``${}``。因此，也可以将 property 与其他文本组合使用：

.. code-block:: xml

   <xacro:property name="robotname" value="marvin" />
   <link name="${robotname}s_leg" />

这段代码会生成：

.. code-block:: xml

   <link name="marvins_leg" />

不过，``${}`` 中的内容不一定只能是 property，这就引出了下一个功能。

数学表达式
----------

可以在 ``${}`` 结构中构建任意复杂的表达式，支持四种基本运算（+、-、*、/）、一元负号以及括号。

例如：

.. code-block:: xml

   <cylinder radius="${wheeldiam/2}" length="0.1"/>
   <origin xyz="${reflect*(width+.02)} 0 0.25" />

除了基本数学运算，还可以使用 ``sin`` 和 ``cos`` 等函数。

宏
--

宏是 Xacro 功能中最重要、最有用的组成部分。

简单宏
^^^^^^

先来看一个简单但没有实际用途的宏：

.. code-block:: xml

   <xacro:macro name="default_origin">
       <origin xyz="0 0 0" rpy="0 0 0"/>
   </xacro:macro>
   <xacro:default_origin />

这个宏本身没有实际必要，因为如果不指定 origin，其默认值也与这里相同。处理后会生成：

.. code-block:: xml

   <origin rpy="0 0 0" xyz="0 0 0"/>

需要注意：

* ``name`` 并不是技术上必需的元素，但必须指定名称才能调用该宏。
* 每个 ``<xacro:$NAME />`` 实例都会被替换为对应 ``xacro:macro`` 标签中的内容。
* 虽然生成结果中两个属性的顺序发生了变化，但生成的 XML 在语义上等价。
* 如果找不到指定名称的 xacro 宏，该宏不会被展开，也不会产生错误。

参数化宏
^^^^^^^^

还可以为宏设置参数，使其每次调用时生成不同的内容。与数学表达式功能结合使用时，参数化宏会更加强大。

先看一个 R2D2 模型中使用的简单宏：

.. code-block:: xml

   <xacro:macro name="default_inertial" params="mass">
       <inertial>
               <mass value="${mass}" />
               <inertia ixx="1e-3" ixy="0.0" ixz="0.0"
                    iyy="1e-3" iyz="0.0"
                    izz="1e-3" />
       </inertial>
   </xacro:macro>

可以通过下面的代码调用：

.. code-block:: xml

   <xacro:default_inertial mass="10"/>

宏的参数与 property 类似，也可以在表达式中使用。

还可以将完整的 XML 代码块作为宏参数传递：

.. code-block:: xml

   <xacro:macro name="blue_shape" params="name *shape">
       <link name="${name}">
           <visual>
               <geometry>
                   <xacro:insert_block name="shape" />
               </geometry>
               <material name="blue"/>
           </visual>
           <collision>
               <geometry>
                   <xacro:insert_block name="shape" />
               </geometry>
           </collision>
       </link>
   </xacro:macro>

   <xacro:blue_shape name="base_link">
       <cylinder radius=".42" length=".01" />
   </xacro:blue_shape>

需要注意：

* 要声明代码块参数，需要在参数名称前添加星号。
* 可以使用 ``insert_block`` 命令插入代码块。
* 同一个代码块可以按需插入多次。

实际应用
--------

Xacro 语言非常灵活。除了前面介绍的默认惯性宏，下面还介绍 R2D2 模型中的一些实用写法。

可以使用与前面教程相同的命令，查看 xacro 文件生成的机器人模型：

.. code-block:: console

   $ ros2 launch urdf_tutorial display.launch.py model:=urdf/08-macroed.urdf.xacro

（启动文件一直在运行 xacro 命令，只是此前没有宏需要展开，因此没有明显区别。）

腿部宏
^^^^^^

通常需要在不同位置创建多个外观相似的对象。可以使用宏和简单数学运算减少代码量，例如 R2D2 的两条腿：

.. code-block:: xml

   <xacro:macro name="leg" params="prefix reflect">
       <link name="${prefix}_leg">
           <visual>
               <geometry>
                   <box size="${leglen} 0.1 0.2"/>
               </geometry>
               <origin xyz="0 0 -${leglen/2}" rpy="0 ${pi/2} 0"/>
               <material name="white"/>
           </visual>
           <collision>
               <geometry>
                   <box size="${leglen} 0.1 0.2"/>
               </geometry>
               <origin xyz="0 0 -${leglen/2}" rpy="0 ${pi/2} 0"/>
           </collision>
           <xacro:default_inertial mass="10"/>
       </link>

       <joint name="base_to_${prefix}_leg" type="fixed">
           <parent link="base_link"/>
           <child link="${prefix}_leg"/>
           <origin xyz="0 ${reflect*(width+.02)} 0.25" />
       </joint>
       <!-- 此处省略其他内容 -->
   </xacro:macro>

   <xacro:leg prefix="right" reflect="1" />
   <xacro:leg prefix="left" reflect="-1" />

这里使用了几个常见技巧：

* 技巧 1：使用名称前缀创建两个名称相似的对象。
* 技巧 2：使用数学表达式计算关节原点。如果修改机器人尺寸，只需修改 property，并通过数学表达式计算关节偏移量，可以避免大量手动调整。
* 技巧 3：使用 ``reflect`` 参数，并分别设置为 1 或 -1。通过 ``base_to_${prefix}_leg`` 关节的 origin 表达式，可以将两条腿分别放置在机器人主体的两侧。
