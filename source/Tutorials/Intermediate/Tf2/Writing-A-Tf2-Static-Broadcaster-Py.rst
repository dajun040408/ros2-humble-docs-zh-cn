.. redirect-from::

    Tutorials/Tf2/Writing-A-Tf2-Static-Broadcaster-Py

编写静态广播器（Python）
========================

**目标：** 学习如何向 tf2 广播静态坐标系。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

发布静态变换有助于定义机器人底座与传感器或其他固定部件之间的关系。例如，在激光雷达中心建立坐标系，可以更直观地理解激光扫描测量值。

本教程独立介绍静态变换基础知识，分为两部分：第一部分编写代码向 tf2 发布静态变换；第二部分介绍如何使用 ``tf2_ros`` 中的命令行工具 ``static_transform_publisher``。

前置条件
--------

此前教程已经介绍了如何 :doc:`创建工作空间 <../../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace>` 和 :doc:`创建功能包 <../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>`。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

创建本教程及后续教程使用的 ``learning_tf2_py`` 功能包。该功能包依赖 ``geometry_msgs``、``python3-numpy``、``rclpy``、``tf2_ros_py`` 和 ``turtlesim``。

示例代码：`static_turtle_tf2_broadcaster.py <https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/static_turtle_tf2_broadcaster.py>`_。

打开新终端并 :doc:`source ROS 2 环境 <../../Beginner-CLI-Tools/Configuring-ROS2-Environment>`，然后进入工作空间的 ``src`` 目录创建功能包：

.. code-block:: console

   $ ros2 pkg create --build-type ament_python --license Apache-2.0 -- learning_tf2_py

终端会输出信息，确认 ``learning_tf2_py`` 功能包及其所需文件和目录已经创建。

2. 编写静态广播器节点
^^^^^^^^^^^^^^^^^^^^^

在 ``src/learning_tf2_py/learning_tf2_py`` 目录下载示例代码：

.. code-block:: console

   $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/static_turtle_tf2_broadcaster.py

Windows 命令提示符可以使用 ``curl -sk URL -o static_turtle_tf2_broadcaster.py``；PowerShell 可以使用 ``curl URL -o static_turtle_tf2_broadcaster.py``。

打开 ``static_turtle_tf2_broadcaster.py``。核心实现如下：

.. code-block:: python

   from geometry_msgs.msg import TransformStamped
   import rclpy
   from rclpy.node import Node
   from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster

   class StaticFramePublisher(Node):
       def __init__(self, transformation):
           super().__init__('static_turtle_tf2_broadcaster')
           self.tf_static_broadcaster = StaticTransformBroadcaster(self)
           self.make_transforms(transformation)

       def make_transforms(self, transformation):
           t = TransformStamped()
           t.header.stamp = self.get_clock().now().to_msg()
           t.header.frame_id = 'world'
           t.child_frame_id = transformation[1]
           t.transform.translation.x = float(transformation[2])
           t.transform.translation.y = float(transformation[3])
           t.transform.translation.z = float(transformation[4])
           quat = quaternion_from_euler(
               float(transformation[5]), float(transformation[6]), float(transformation[7]))
           t.transform.rotation.x = quat[0]
           t.transform.rotation.y = quat[1]
           t.transform.rotation.z = quat[2]
           t.transform.rotation.w = quat[3]
           self.tf_static_broadcaster.sendTransform(t)

该节点在启动时只发布一次变换，适合发布永远不会改变的静态坐标系。

2.1 理解代码
~~~~~~~~~~~~

首先导入 ``TransformStamped``，它提供了向变换树发布的消息模板：

.. code-block:: python

   from geometry_msgs.msg import TransformStamped

随后导入 ``rclpy``，以使用其 ``Node`` 类：

.. code-block:: python

   import rclpy
   from rclpy.node import Node

``tf2_ros`` 提供 ``StaticTransformBroadcaster``，用于简化静态变换发布：

.. code-block:: python

   from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster

``StaticFramePublisher`` 构造函数将节点命名为 ``static_turtle_tf2_broadcaster``，然后创建静态广播器，并在启动时发布一次静态变换。

创建 ``TransformStamped`` 对象后，需要填写元数据：

* 为变换设置时间戳，本例使用当前时间 ``self.get_clock().now()``。
* 设置父坐标系名称，本例为 ``world``。
* 设置新建子坐标系的名称。

.. code-block:: python

   t = TransformStamped()
   t.header.stamp = self.get_clock().now().to_msg()
   t.header.frame_id = 'world'
   t.child_frame_id = transformation[1]

随后填写海龟的六自由度位姿，即平移和旋转：

.. code-block:: python

   t.transform.translation.x = float(transformation[2])
   t.transform.translation.y = float(transformation[3])
   t.transform.translation.z = float(transformation[4])
   quat = quaternion_from_euler(
       float(transformation[5]), float(transformation[6]), float(transformation[7]))
   t.transform.rotation.x = quat[0]
   t.transform.rotation.y = quat[1]
   t.transform.rotation.z = quat[2]
   t.transform.rotation.w = quat[3]

最后调用 ``sendTransform()`` 广播静态变换：

.. code-block:: python

   self.tf_static_broadcaster.sendTransform(t)

2.2 更新 package.xml
~~~~~~~~~~~~~~~~~~~~

返回 ``src/learning_tf2_py`` 目录，打开 ``package.xml``。按照 :doc:`创建功能包教程 <../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>` 的说明，填写 ``<description>``、``<maintainer>`` 和 ``<license>`` 标签：

.. code-block:: xml

   <description>Learning tf2 with rclpy</description>
   <maintainer email="you@email.com">Your Name</maintainer>
   <license>Apache License 2.0</license>

然后添加与节点导入语句对应的依赖：

.. code-block:: xml

   <exec_depend>geometry_msgs</exec_depend>
   <exec_depend>python3-numpy</exec_depend>
   <exec_depend>rclpy</exec_depend>
   <exec_depend>tf2_ros_py</exec_depend>
   <exec_depend>turtlesim</exec_depend>

这会声明代码运行时所需的依赖项。

2.3 添加入口点
~~~~~~~~~~~~~~

为了让 ``ros2 run`` 能够运行节点，需要在 ``src/learning_tf2_py/setup.py`` 中添加入口点。在 ``'console_scripts':`` 对应列表中添加：

.. code-block:: python

   'static_turtle_tf2_broadcaster = learning_tf2_py.static_turtle_tf2_broadcaster:main',

3. 构建
^^^^^^^

建议在工作空间根目录运行 rosdep，检查构建前是否缺少依赖：

.. code-block:: console

   $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

macOS 和 Windows 上 rosdep 不可用，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

构建功能包：

.. code-block:: console

   $ colcon build --packages-select learning_tf2_py

Windows 使用：

.. code-block:: console

   $ colcon build --merge-install --packages-select learning_tf2_py

打开新终端，进入工作空间根目录并 source 环境：

.. code-block:: console

   $ . install/setup.bash

Windows 命令提示符使用 ``call install\setup.bat``；PowerShell 使用 ``.\install\setup.ps1``。

4. 运行
^^^^^^^

运行 ``static_turtle_tf2_broadcaster`` 节点：

.. code-block:: console

   $ ros2 run learning_tf2_py static_turtle_tf2_broadcaster mystaticturtle 0 0 1 0 0 0

该命令会广播 ``mystaticturtle`` 的位姿，使其位于地面上方 1 米处。

可以通过 echo ``tf_static`` 话题检查静态变换是否已经发布：

.. code-block:: console

   $ ros2 topic echo /tf_static
   transforms:
   - header:
       stamp:
         sec: 1622908754
         nanosec: 208515730
       frame_id: world
     child_frame_id: mystaticturtle
     transform:
       translation:
         x: 0.0
         y: 0.0
         z: 1.0
       rotation:
         x: 0.0
         y: 0.0
         z: 0.0
         w: 1.0

正确发布静态变换的方式
----------------------

本教程旨在展示如何使用 ``StaticTransformBroadcaster`` 发布静态变换。在实际开发中，通常不需要自行编写这段代码，而应使用 ``tf2_ros`` 提供的专用工具。

``tf2_ros`` 提供名为 ``static_transform_publisher`` 的可执行程序，既可以作为命令行工具使用，也可以作为节点加入启动文件。

以下命令在 ``world`` 和 ``mystaticturtle`` 坐标系之间发布静态变换，z 轴偏移 1 米且无旋转。ROS 2 中 roll/pitch/yaw 分别表示绕 x/y/z 轴旋转，单位为弧度：

.. code-block:: console

   $ ros2 run tf2_ros static_transform_publisher --x 0 --y 0 --z 1 --yaw 0 --pitch 0 --roll 0 --frame-id world --child-frame-id mystaticturtle

也可以使用四元数表示旋转，发布相同的静态变换：

.. code-block:: console

   $ ros2 run tf2_ros static_transform_publisher --x 0 --y 0 --z 1 --qx 0 --qy 0 --qz 0 --qw 1 --frame-id world --child-frame-id mystaticturtle

``static_transform_publisher`` 既适合手动命令行调用，也适合在 ``launch`` 文件中设置静态变换。

.. tabs::

   .. group-tab:: XML

      .. literalinclude:: launch/static_transform_publisher_launch.xml
         :language: xml

   .. group-tab:: YAML

      .. literalinclude:: launch/static_transform_publisher_launch.yaml
         :language: yaml

   .. group-tab:: Python

      .. literalinclude:: launch/static_transform_publisher_launch.py
         :language: python

除 ``--frame-id`` 和 ``--child-frame-id`` 外，所有参数都是可选的。未指定的参数会采用单位变换对应的默认值。

总结
----

本教程介绍了静态变换的用途，例如定义 ``mystaticturtle`` 相对于 ``world`` 的固定关系。静态变换也有助于理解激光雷达等传感器数据，将其关联到共同坐标系。最后，我们编写了自己的节点发布静态变换，并学习了如何使用 ``static_transform_publisher`` 可执行程序和启动文件发布所需变换。
