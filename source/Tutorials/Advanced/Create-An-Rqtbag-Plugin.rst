创建 rqt_bag 插件
==================

如果已经有 bag 文件，并希望对其中的数据进行自定义可视化，可以使用 §rqt_bag§。它允许用户浏览录制的消息并查看原始消息值。

运行 §rqt_bag§：

.. code-block:: console

   $ ros2 run rqt_bag rqt_bag ~/path/to/BagFile

也可以使用：

.. code-block:: console

   $ rqt_bag ~/path/to/BagFile

默认界面提供统一的消息时间轴和消息内容显示。

.. image:: images/rqtbag_plugin_base.png
   :alt: rqt_bag 默认界面截图

如果希望更直观地显示数据，或需要对原始消息进行后处理，可以使用 Python 插件系统编写自定义 §rqt_bag§ 插件。

.. image:: images/rqtbag_plugin_full.png
   :alt: 带有自定义时间轴和侧边面板的 rqt_bag 界面

测试数据
--------

本教程使用 §diagnostic_msgs/msg/DiagnosticStatus§ 消息中的 §level§ 字段。可以编写简单 Python 节点，随机发布不同诊断级别，再录制为 bag 文件；也可以使用教程提供的示例数据。

.. code-block:: python

   from diagnostic_msgs.msg import DiagnosticStatus
   import random
   import rclpy
   from rclpy.node import Node

   MODES = ['OK', 'WARN', 'ERROR']

   class DiagnosticPub(Node):
       def __init__(self):
           super().__init__('diagnostic_pub')
           self.last_status = None
           self.publisher = self.create_publisher(
               DiagnosticStatus, '/diagnostics', 10)
           self.timer = self.create_timer(1, self.callback)

       def callback(self):
           if self.last_status is None:
               status = random.randint(0, len(MODES) - 1)
           elif random.randint(0, 5) != 0:
               return
           else:
               delta = random.randint(1, 2)
               status = (self.last_status + delta) % len(MODES)

           self.get_logger().info(f'Publishing {MODES[status]} status')
           self.publisher.publish(DiagnosticStatus(level=status))
           self.last_status = status

插件开发
--------

自定义 rqt_bag 插件可以访问 bag 中的消息和时间戳，并在时间轴或侧边面板中绘制专用可视化。插件通过 rqt 的 Python 插件机制注册，并实现消息加载、时间轴绘制和播放位置更新等功能。

总结
----

rqt_bag 插件允许开发者扩展 bag 文件的可视化方式。对于诊断状态、传感器事件和自定义消息，可以使用插件呈现比原始消息更直观的信息。
