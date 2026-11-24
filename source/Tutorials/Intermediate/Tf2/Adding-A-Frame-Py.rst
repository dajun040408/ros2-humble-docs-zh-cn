.. redirect-from::

    Tutorials/Tf2/Adding-A-Frame-Py

tf2 添加坐标系（Python）
========================

**目标：** 学习如何向 tf2 添加额外坐标系。

**教程级别：** 中级

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 3
   :local:

背景
----

此前教程中，我们通过编写 :doc:`tf2 广播器 <./Writing-A-Tf2-Broadcaster-Py>` 和 :doc:`tf2 监听器 <Writing-A-Tf2-Listener-Py>` 重现了海龟演示。本教程将介绍如何向变换树添加固定坐标系和动态坐标系。

对于许多与坐标变换有关的任务，在局部坐标系中思考会更容易。例如，在激光雷达中心建立坐标系，可以更直观地理解激光扫描测量值。

tf2 允许为系统中的每个传感器、连杆或关节定义局部坐标系。当需要从一个坐标系变换到另一个坐标系时，tf2 会自动处理所有隐藏的中间坐标系变换。

tf2 变换树
----------

tf2 使用树结构组织坐标系，因此不允许坐标系结构中出现闭环。这意味着每个坐标系只能有一个父坐标系，但可以有多个子坐标系。

当前 tf2 变换树包含三个坐标系：``world``、``turtle1`` 和 ``turtle2``。两只乌龟的坐标系都是 ``world`` 的子坐标系。如果要向 tf2 添加新坐标系，需要从现有三个坐标系中选择一个作为父坐标系，新坐标系则成为它的子坐标系。

.. image:: images/turtlesim_frames.png

任务
----

1. 编写固定坐标系广播器
^^^^^^^^^^^^^^^^^^^^^^^

在海龟示例中，我们将添加一个名为 ``carrot1`` 的新坐标系，它是 ``turtle1`` 的子坐标系，并作为第二只海龟的目标。

首先创建源文件。进入此前教程中创建的 ``learning_tf2_py`` 功能包，在 ``src/learning_tf2_py/learning_tf2_py`` 目录中下载固定坐标系广播器代码：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/fixed_frame_tf2_broadcaster.py

   .. group-tab:: macOS

      .. code-block:: console

         $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/fixed_frame_tf2_broadcaster.py

   .. group-tab:: Windows

      在 Windows 命令提示符中：

      .. code-block:: console

         $ curl -sk https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/fixed_frame_tf2_broadcaster.py -o fixed_frame_tf2_broadcaster.py

      或在 PowerShell 中：

      .. code-block:: console

         $ curl https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/fixed_frame_tf2_broadcaster.py -o fixed_frame_tf2_broadcaster.py

打开 ``fixed_frame_tf2_broadcaster.py``：

.. code-block:: python

   from geometry_msgs.msg import TransformStamped

   import rclpy
   from rclpy.node import Node

   from tf2_ros import TransformBroadcaster


   class FixedFrameBroadcaster(Node):

       def __init__(self):
           super().__init__('fixed_frame_tf2_broadcaster')
           self.tf_broadcaster = TransformBroadcaster(self)
           self.timer = self.create_timer(0.1, self.broadcast_timer_callback)

       def broadcast_timer_callback(self):
           t = TransformStamped()

           t.header.stamp = self.get_clock().now().to_msg()
           t.header.frame_id = 'turtle1'
           t.child_frame_id = 'carrot1'
           t.transform.translation.x = 0.0
           t.transform.translation.y = 2.0
           t.transform.translation.z = 0.0
           t.transform.rotation.x = 0.0
           t.transform.rotation.y = 0.0
           t.transform.rotation.z = 0.0
           t.transform.rotation.w = 1.0

           self.tf_broadcaster.sendTransform(t)


   def main():
       rclpy.init()
       node = FixedFrameBroadcaster()
       try:
           rclpy.spin(node)
       except KeyboardInterrupt:
           pass

       rclpy.shutdown()

这段代码与前面 tf2 广播器教程中的示例非常相似，唯一的区别是这里发布的变换不会随时间变化。

1.1 理解代码
~~~~~~~~~~~~

下面看一下代码中的关键部分。这里创建了一个新的变换，父坐标系是 ``turtle1``，子坐标系是 ``carrot1``。

``carrot1`` 坐标系相对于 ``turtle1`` 坐标系在 y 轴方向偏移 2 米：

.. code-block:: python

   t = TransformStamped()

   t.header.stamp = self.get_clock().now().to_msg()
   t.header.frame_id = 'turtle1'
   t.child_frame_id = 'carrot1'
   t.transform.translation.x = 0.0
   t.transform.translation.y = 2.0
   t.transform.translation.z = 0.0

1.2 添加入口点
~~~~~~~~~~~~~

为了让 ``ros2 run`` 命令能够运行该节点，需要在 ``src/learning_tf2_py`` 目录中的 ``setup.py`` 添加入口点。

在 ``console_scripts`` 列表中添加：

.. code-block:: python

   'fixed_frame_tf2_broadcaster = learning_tf2_py.fixed_frame_tf2_broadcaster:main',

1.3 编写启动文件
~~~~~~~~~~~~~~~

现在为该示例创建启动文件。在 ``src/learning_tf2_py/launch`` 目录中创建名为 ``turtle_tf2_fixed_frame_demo_launch`` 的文件，扩展名可以为 ``.py``、``.xml`` 或 ``.yaml``，并添加以下内容：

.. tabs::

  .. group-tab:: Python

    .. literalinclude:: launch/py_turtle_tf2_fixed_frame_demo_launch.py
       :language: python

  .. group-tab:: XML

    .. literalinclude:: launch/py_turtle_tf2_fixed_frame_demo_launch.xml
       :language: xml

  .. group-tab:: YAML

    .. literalinclude:: launch/py_turtle_tf2_fixed_frame_demo_launch.yaml
       :language: yaml

启动文件会导入所需模块，并创建 ``demo_nodes`` 变量，用于保存前面教程启动文件中创建的节点。

代码的最后部分通过 ``fixed_frame_tf2_broadcaster`` 节点，将固定的 ``carrot1`` 坐标系添加到 turtlesim 世界中。

.. tabs::

  .. group-tab:: Python

    .. literalinclude:: launch/py_turtle_tf2_fixed_frame_demo_launch.py
       :language: python
       :lines: 14-18

  .. group-tab:: XML

    .. literalinclude:: launch/py_turtle_tf2_fixed_frame_demo_launch.xml
       :language: xml
       :lines: 3-4

  .. group-tab:: YAML

    .. literalinclude:: launch/py_turtle_tf2_fixed_frame_demo_launch.yaml
       :language: yaml
       :lines: 6-9

1.4 构建
~~~~~~~~

在工作空间根目录运行 ``rosdep``，检查是否缺少依赖：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

   .. group-tab:: macOS

      ``rosdep`` 仅在 Linux 上运行，因此需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

   .. group-tab:: Windows

      ``rosdep`` 仅在 Linux 上运行，因此需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

仍在工作空间根目录中，构建功能包：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ colcon build --packages-select learning_tf2_py

  .. group-tab:: macOS

    .. code-block:: console

       $ colcon build --packages-select learning_tf2_py

  .. group-tab:: Windows

    .. code-block:: console

       $ colcon build --merge-install --packages-select learning_tf2_py

打开新终端，进入工作空间根目录并加载设置文件：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ . install/setup.bash

  .. group-tab:: macOS

    .. code-block:: console

       $ . install/setup.bash

  .. group-tab:: Windows

    在 Windows 命令提示符中：

    .. code-block:: console

       $ call install\setup.bat

    或在 PowerShell 中：

    .. code-block:: console

       $ .\install\setup.ps1

1.5 运行
~~~~~~~~

现在可以启动海龟广播器演示：

.. code-block:: console

   $ ros2 launch learning_tf2_py turtle_tf2_fixed_frame_demo_launch.xml

也可以使用 ``.py`` 或 ``.yaml`` 扩展名。

此时应该能看到新的 ``carrot1`` 坐标系出现在变换树中：

.. image:: images/turtlesim_frames_carrot.png

如果控制第一只海龟移动，会发现它的行为与前一个教程没有变化。这是因为添加额外坐标系不会影响其他坐标系，而当前监听器仍然使用之前定义的坐标系。

如果希望第二只海龟跟随 carrot，而不是跟随第一只海龟，就需要修改 ``target_frame``。可以通过两种方式实现。

第一种方式是在命令行中直接向启动文件传递 ``target_frame`` 参数：

.. code-block:: console

   $ ros2 launch learning_tf2_py turtle_tf2_fixed_frame_demo_launch.xml target_frame:=carrot1

也可以使用 ``.py`` 或 ``.yaml`` 扩展名。

第二种方式是修改启动文件。打开 ``turtle_tf2_fixed_frame_demo_launch.py``，在 ``launch_arguments`` 参数中添加 ``'target_frame': 'carrot1'``：

.. code-block:: python

   def generate_launch_description():
       demo_nodes = IncludeLaunchDescription(
           ...,
           launch_arguments={'target_frame': 'carrot1'}.items(),
       )

现在重新构建功能包，并重新启动 ``turtle_tf2_fixed_frame_demo_launch.py``，就会看到第二只海龟跟随 carrot，而不是跟随第一只海龟。

.. image:: images/carrot_static.png

2. 编写动态坐标系广播器
^^^^^^^^^^^^^^^^^^^^^^^

本教程发布的额外坐标系是固定坐标系，它相对于父坐标系的位置不会随时间变化。

如果希望发布一个移动坐标系，可以编写广播器，让坐标系随时间变化。现在将 ``carrot1`` 坐标系修改为相对于 ``turtle1`` 随时间移动。

进入此前创建的 ``learning_tf2_py`` 功能包，在 ``src/learning_tf2_py/learning_tf2_py`` 目录中下载动态坐标系广播器：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/dynamic_frame_tf2_broadcaster.py

   .. group-tab:: macOS

      .. code-block:: console

         $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/dynamic_frame_tf2_broadcaster.py

   .. group-tab:: Windows

      在 Windows 命令提示符中：

      .. code-block:: console

         $ curl -sk https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/dynamic_frame_tf2_broadcaster.py -o dynamic_frame_tf2_broadcaster.py

      或在 PowerShell 中：

      .. code-block:: console

         $ curl https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/dynamic_frame_tf2_broadcaster.py -o dynamic_frame_tf2_broadcaster.py

打开 ``dynamic_frame_tf2_broadcaster.py``：

.. code-block:: python

   import math

   from geometry_msgs.msg import TransformStamped

   import rclpy
   from rclpy.node import Node

   from tf2_ros import TransformBroadcaster


   class DynamicFrameBroadcaster(Node):

       def __init__(self):
           super().__init__('dynamic_frame_tf2_broadcaster')
           self.tf_broadcaster = TransformBroadcaster(self)
           self.timer = self.create_timer(0.1, self.broadcast_timer_callback)

       def broadcast_timer_callback(self):
           seconds, _ = self.get_clock().now().seconds_nanoseconds()
           x = seconds * math.pi

           t = TransformStamped()
           t.header.stamp = self.get_clock().now().to_msg()
           t.header.frame_id = 'turtle1'
           t.child_frame_id = 'carrot1'
           t.transform.translation.x = 10 * math.sin(x)
           t.transform.translation.y = 10 * math.cos(x)
           t.transform.translation.z = 0.0
           t.transform.rotation.x = 0.0
           t.transform.rotation.y = 0.0
           t.transform.rotation.z = 0.0
           t.transform.rotation.w = 1.0

           self.tf_broadcaster.sendTransform(t)


   def main():
       rclpy.init()
       node = DynamicFrameBroadcaster()
       try:
           rclpy.spin(node)
       except KeyboardInterrupt:
           pass

       rclpy.shutdown()

2.1 理解代码
~~~~~~~~~~~~

与固定坐标系不同，这里不再使用固定的 x、y 偏移量，而是根据当前时间使用 ``sin()`` 和 ``cos()`` 函数计算偏移量，因此 ``carrot1`` 的位置会持续变化：

.. code-block:: python

   seconds, _ = self.get_clock().now().seconds_nanoseconds()
   x = seconds * math.pi

   t.transform.translation.x = 10 * math.sin(x)
   t.transform.translation.y = 10 * math.cos(x)

2.2 添加入口点
~~~~~~~~~~~~~

为了让 ``ros2 run`` 命令能够运行该节点，需要在 ``setup.py`` 的 ``console_scripts`` 列表中添加：

.. code-block:: python

   'dynamic_frame_tf2_broadcaster = learning_tf2_py.dynamic_frame_tf2_broadcaster:main',

2.3 编写启动文件
~~~~~~~~~~~~~~~

在 ``src/learning_tf2_py/launch`` 目录中创建 ``turtle_tf2_dynamic_frame_demo_launch`` 文件，扩展名可以为 ``.py``、``.xml`` 或 ``.yaml``：

.. tabs::

  .. group-tab:: Python

    .. literalinclude:: launch/py_turtle_tf2_dynamic_frame_demo_launch.py
       :language: python

  .. group-tab:: XML

    .. literalinclude:: launch/py_turtle_tf2_dynamic_frame_demo_launch.xml
       :language: xml

  .. group-tab:: YAML

    .. literalinclude:: launch/py_turtle_tf2_dynamic_frame_demo_launch.yaml
       :language: yaml

2.4 构建
~~~~~~~~

在工作空间根目录运行 ``rosdep`` 检查依赖。macOS 和 Windows 需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。随后构建：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ rosdep install -i --from-path src --rosdistro {DISTRO} -y
       $ colcon build --packages-select learning_tf2_py

  .. group-tab:: macOS

    .. code-block:: console

       $ colcon build --packages-select learning_tf2_py

  .. group-tab:: Windows

    .. code-block:: console

       $ colcon build --merge-install --packages-select learning_tf2_py

打开新终端，加载工作空间设置文件：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ . install/setup.bash

  .. group-tab:: macOS

    .. code-block:: console

       $ . install/setup.bash

  .. group-tab:: Windows

    .. code-block:: console

       $ call install\setup.bat

2.5 运行
~~~~~~~~

启动动态坐标系演示：

.. code-block:: console

   $ ros2 launch learning_tf2_py turtle_tf2_dynamic_frame_demo_launch.xml

也可以使用 ``.py`` 或 ``.yaml`` 扩展名。

此时应该能看到第二只海龟跟随不断移动的 carrot。

.. image:: images/carrot_dynamic.png

总结
----

本教程介绍了 tf2 变换树的结构，以及如何在 Python 中为局部坐标系添加固定和动态坐标系。
