.. redirect-from::

    Tutorials/Tf2/Writing-A-Tf2-Listener-Py

编写监听器（Python）
====================

**目标：** 学习如何使用 tf2 监听坐标变换。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程继续使用 :doc:`tf2 入门 <./Introduction-To-Tf2>`、:doc:`Python 静态广播器 <./Writing-A-Tf2-Static-Broadcaster-Py>` 和 :doc:`Python 广播器 <./Writing-A-Tf2-Broadcaster-Py>` 中创建的 ``learning_tf2_py`` 功能包。

任务
----

1. 编写监听器节点
^^^^^^^^^^^^^^^^^

在 ``src/learning_tf2_py/learning_tf2_py`` 目录创建 ``turtle_tf2_listener.py``。监听器使用 ``tf2_ros`` 的 ``Buffer`` 保存变换，并使用 ``TransformListener`` 接收广播器发布的数据。

.. code-block:: python

   import rclpy
   from rclpy.node import Node
   from tf2_ros import TransformException
   from tf2_ros.buffer import Buffer
   from tf2_ros.transform_listener import TransformListener

   class FrameListener(Node):
       def __init__(self):
           super().__init__('turtle_tf2_listener')
           self.tf_buffer = Buffer()
           self.tf_listener = TransformListener(self.tf_buffer, self)
           self.timer = self.create_timer(1.0, self.on_timer)

       def on_timer(self):
           from_frame_rel = 'turtle1'
           to_frame_rel = 'world'
           try:
               now = rclpy.time.Time()
               trans = self.tf_buffer.lookup_transform(
                   to_frame_rel, from_frame_rel, now)
           except TransformException as ex:
               self.get_logger().info(
                   f'Could not transform {to_frame_rel} to {from_frame_rel}: {ex}')
               return

监听器周期性查询 ``world`` 与 ``turtle1`` 之间的变换。``lookup_transform()`` 使用目标坐标系、源坐标系和查询时间；``rclpy.time.Time()`` 表示查询最新可用变换。若变换尚不可用，``TransformException`` 会被捕获并记录日志。

2. 添加入口点
^^^^^^^^^^^^^

在 ``setup.py`` 的 ``console_scripts`` 中添加监听器入口点：

.. code-block:: python

   'turtle_tf2_listener = learning_tf2_py.turtle_tf2_listener:main',

3. 构建与运行
^^^^^^^^^^^^^

在工作空间根目录构建：

.. code-block:: console

   $ colcon build --packages-select learning_tf2_py

Windows 使用 ``--merge-install``。source 工作空间后运行启动文件：

.. code-block:: console

   $ ros2 launch learning_tf2_py turtle_tf2_demo_launch.py

广播器会将海龟位姿发布到 tf2，监听器则从缓冲区查询变换。若查询失败，节点会输出错误日志，而不会因异常直接终止。

总结
----

本教程介绍了如何在 Python 中使用 ``Buffer`` 和 ``TransformListener`` 接收变换，并通过 ``lookup_transform()`` 查询最新可用的坐标变换。
