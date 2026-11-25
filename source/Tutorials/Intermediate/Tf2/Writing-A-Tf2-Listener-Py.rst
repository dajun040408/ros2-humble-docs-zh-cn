.. redirect-from::

    Tutorials/Tf2/Writing-A-Tf2-Listener-Py

编写监听器（Python）
====================

**目标：** 学习如何使用 tf2 获取坐标系变换。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

在前面的教程中，我们创建了 tf2 广播器，将海龟的位姿发布到 tf2。

本教程将创建一个 tf2 监听器，开始使用 tf2 获取坐标系之间的变换。

前置条件
--------

本教程假设你已经完成 :doc:`tf2 静态广播器教程（Python） <./Writing-A-Tf2-Static-Broadcaster-Py>` 和 :doc:`tf2 广播器教程（Python） <./Writing-A-Tf2-Broadcaster-Py>`。

前面的教程中已经创建了 ``learning_tf2_py`` 功能包，本教程会继续在该功能包中进行开发。

任务
----

1. 编写监听器节点
^^^^^^^^^^^^^^^^^

首先创建源文件。进入之前创建的 ``learning_tf2_py`` 功能包，在 ``src/learning_tf2_py/learning_tf2_py`` 目录中下载示例监听器代码：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/turtle_tf2_listener.py

  .. group-tab:: macOS

    .. code-block:: console

       $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/turtle_tf2_listener.py

  .. group-tab:: Windows

    在 Windows 命令提示符中：

    .. code-block:: console

       $ curl -sk https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/turtle_tf2_listener.py -o turtle_tf2_listener.py

    或在 PowerShell 中：

    .. code-block:: console

       $ curl https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/turtle_tf2_listener.py -o turtle_tf2_listener.py

使用文本编辑器打开 ``turtle_tf2_listener.py``：

.. code-block:: python

   import math

   from geometry_msgs.msg import Twist

   import rclpy
   from rclpy.node import Node

   from tf2_ros import TransformException
   from tf2_ros.buffer import Buffer
   from tf2_ros.transform_listener import TransformListener

   from turtlesim.srv import Spawn


   class FrameListener(Node):

       def __init__(self):
           super().__init__('turtle_tf2_frame_listener')

           self.target_frame = self.declare_parameter(
               'target_frame', 'turtle1').get_parameter_value().string_value

           self.tf_buffer = Buffer()
           self.tf_listener = TransformListener(self.tf_buffer, self)

           self.spawner = self.create_client(Spawn, 'spawn')
           self.turtle_spawning_service_ready = False
           self.turtle_spawned = False

           self.publisher = self.create_publisher(Twist, 'turtle2/cmd_vel', 1)
           self.timer = self.create_timer(1.0, self.on_timer)

       def on_timer(self):
           from_frame_rel = self.target_frame
           to_frame_rel = 'turtle2'

           if self.turtle_spawning_service_ready:
               if self.turtle_spawned:
                   try:
                       t = self.tf_buffer.lookup_transform(
                           to_frame_rel,
                           from_frame_rel,
                           rclpy.time.Time())
                   except TransformException as ex:
                       self.get_logger().info(
                           f'Could not transform {to_frame_rel} to {from_frame_rel}: {ex}')
                       return

                   msg = Twist()
                   scale_rotation_rate = 1.0
                   msg.angular.z = scale_rotation_rate * math.atan2(
                       t.transform.translation.y,
                       t.transform.translation.x)

                   scale_forward_speed = 0.5
                   msg.linear.x = scale_forward_speed * math.sqrt(
                       t.transform.translation.x ** 2 +
                       t.transform.translation.y ** 2)

                   self.publisher.publish(msg)
               else:
                   if self.result.done():
                       self.get_logger().info(
                           f'Successfully spawned {self.result.result().name}')
                       self.turtle_spawned = True
                   else:
                       self.get_logger().info('Spawn is not finished')
           else:
               if self.spawner.service_is_ready():
                   request = Spawn.Request()
                   request.name = 'turtle2'
                   request.x = float(4)
                   request.y = float(2)
                   request.theta = float(0)
                   self.result = self.spawner.call_async(request)
                   self.turtle_spawning_service_ready = True
               else:
                   self.get_logger().info('Service is not ready')


   def main():
       rclpy.init()
       node = FrameListener()
       try:
           rclpy.spin(node)
       except KeyboardInterrupt:
           pass

       rclpy.shutdown()

1.1 理解代码
~~~~~~~~~~~~

要理解生成海龟的服务如何工作，可以参阅 :doc:`编写简单的服务和客户端（Python） <../../Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client>` 教程。

现在重点看一下如何访问坐标系变换。``tf2_ros`` 包提供了 ``TransformListener`` 类，可以简化接收变换的工作：

.. code-block:: python

   from tf2_ros.transform_listener import TransformListener

创建 ``TransformListener`` 对象后，它会自动接收 tf2 变换，并将其缓存在缓冲区中，默认缓存时间为 10 秒：

.. code-block:: python

   self.tf_listener = TransformListener(self.tf_buffer, self)

最后，调用 ``lookup_transform()`` 查询特定变换。该方法接收三个参数：

1. 目标坐标系。
2. 源坐标系。
3. 希望查询变换的时间。

提供 ``rclpy.time.Time()`` 表示获取当前缓冲区中最新可用的变换。整个调用使用 try-except 处理可能出现的异常：

.. code-block:: python

   t = self.tf_buffer.lookup_transform(
       to_frame_rel,
       from_frame_rel,
       rclpy.time.Time())

1.2 添加入口点
~~~~~~~~~~~~~~

为了让 ``ros2 run`` 命令能够运行该节点，需要在 ``src/learning_tf2_py`` 目录中的 ``setup.py`` 添加入口点。

在 ``console_scripts`` 列表中添加：

.. code-block:: python

   'turtle_tf2_listener = learning_tf2_py.turtle_tf2_listener:main',

2. 更新启动文件
^^^^^^^^^^^^^^^

使用文本编辑器打开 ``src/learning_tf2_py/launch`` 目录中的 ``turtle_tf2_demo_launch`` 启动文件，扩展名可以是 ``.py``、``.xml`` 或 ``.yaml``。

添加两个新节点、一个启动参数以及所需的导入语句。最终文件应如下所示：

.. tabs::

  .. group-tab:: XML

    .. literalinclude:: launch/listener_py_launch.xml
       :language: xml

  .. group-tab:: YAML

    .. literalinclude:: launch/listener_py_launch.yaml
       :language: yaml

  .. group-tab:: Python

    .. literalinclude:: launch/listener_py_launch.py
       :language: python

启动文件会声明 ``target_frame`` 参数，启动第二只海龟的广播器，并启动一个订阅这些变换的监听器。

3. 构建
^^^^^^^

在工作空间根目录运行 ``rosdep`` 检查依赖：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

  .. group-tab:: macOS

    ``rosdep`` 仅在 Linux 上运行，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

  .. group-tab:: Windows

    ``rosdep`` 仅在 Linux 上运行，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

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

4. 运行
^^^^^^^

现在可以启动完整的海龟演示：

.. tabs::

  .. group-tab:: XML

    .. code-block:: console

       $ ros2 launch learning_tf2_py turtle_tf2_demo_launch.xml

  .. group-tab:: YAML

    .. code-block:: console

       $ ros2 launch learning_tf2_py turtle_tf2_demo_launch.yaml

  .. group-tab:: Python

    .. code-block:: console

       $ ros2 launch learning_tf2_py turtle_tf2_demo_launch.py

此时应该能看到包含两只海龟的 turtlesim 窗口。在第二个终端中运行：

.. code-block:: console

   $ ros2 run turtlesim turtle_teleop_key

使用方向键控制第一只海龟（确保终端窗口处于活动状态，而不是仿真窗口），就会看到第二只海龟跟随第一只海龟移动。

总结
----

本教程介绍了如何使用 tf2 获取坐标系变换，并完成了一个能够让第二只海龟跟随第一只海龟的 turtlesim 演示。
