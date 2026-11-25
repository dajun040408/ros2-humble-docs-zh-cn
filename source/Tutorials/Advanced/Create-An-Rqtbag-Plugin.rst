创建 rqt_bag 插件
==================

假设你已经有 bag 文件，并希望对其中的数据创建自定义可视化。``rqt_bag`` 可以浏览录制的消息并查看原始消息值。

启动 ``rqt_bag``：

.. code-block:: console

   $ ros2 run rqt_bag rqt_bag ~/path/to/BagFile

也可以直接运行：

.. code-block:: console

   $ rqt_bag ~/path/to/BagFile

默认界面提供统一的消息时间轴和原始消息显示：

.. image:: images/rqtbag_plugin_base.png
   :alt: rqt_bag 默认界面截图

如果希望更直观地显示数据，或者需要对原始消息进行后处理，可以使用 Python 插件系统编写自定义 ``rqt_bag`` 插件。

.. image:: images/rqtbag_plugin_full.png
   :alt: 带有自定义时间轴和侧边面板的 rqt_bag 界面

测试数据
--------

本教程使用 ``diagnostic_msgs/msg/DiagnosticStatus`` 消息中的 ``level`` 字段。可以运行下面的脚本，随机发布不同诊断级别，再录制为 bag 文件；也可以下载 `示例数据 <https://github.com/MetroRobots/rqt_bag_diagnostics_demo/raw/refs/heads/main/SomeDiagnostics.zip>`_，解压后直接使用。

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
           self.publisher = self.create_publisher(DiagnosticStatus, '/diagnostics', 10)
           self.timer = self.create_timer(1, self.callback)

       def callback(self):
           if self.last_status is None:
               # 随机选择初始状态
               status = random.randint(0, len(MODES))
           elif random.randint(0, 5) != 0:
               # 并非每个周期都发布消息
               return
           else:
               # 随机选择一个不同的状态
               delta = random.randint(1, 2)
               status = (self.last_status + delta) % len(MODES)

           self.get_logger().info(f'Publishing {MODES[status]} status')
           self.publisher.publish(DiagnosticStatus(level=bytes(status)))
           self.last_status = status


   def main(args=None):
       rclpy.init(args=args)
       node = DiagnosticPub()
       rclpy.spin(node)


   if __name__ == '__main__':
       main()

创建功能包
----------

本教程将创建一个名为 ``rqt_bag_diagnostics_demo`` 的功能包。

首先创建一个基础的 ``ament_python`` 功能包：

.. code-block:: console

   $ ros2 pkg create --build-type ament_python --dependencies diagnostic_msgs python_qt_binding rqt_bag      --description "rqt_bag plugin for diagnostics_msgs" --license Apache-2.0      --maintainer-name "My Name" --maintainer-email "my@name.robots"      rqt_bag_diagnostics_demo

编辑生成的 ``package.xml``，使相关部分如下：

.. code-block:: xml

   <exec_depend>diagnostic_msgs</exec_depend>
   <exec_depend>python_qt_binding</exec_depend>
   <exec_depend>rqt_bag</exec_depend>
   <export>
     <build_type>ament_python</build_type>
     <rqt_bag plugin="${prefix}/plugins.xml"/>
   </export>

这里声明功能包依赖 ``rqt_bag``、``python_qt_binding`` 和 ``diagnostic_msgs``，并导出一个 XML 文件，用于描述本功能包提供的 rqt_bag 插件。

在 ``setup.py`` 的 ``data_files`` 列表中添加：

.. code-block:: python

   ('share/' + package_name, ['plugins.xml']),

接下来创建 ``plugins.xml``（即 ``package.xml`` 中引用的插件描述文件）。该文件描述本功能包提供的所有插件，一个功能包可以包含多个插件。

.. code-block:: xml

   <library path=".">
     <class name="DiagnosticBagPlugin"
            type="rqt_bag_diagnostics_demo.the_plugin.DiagnosticBagPlugin"
            base_class_type="rqt_bag::Plugin">
       <description>Awesome Diagnostic</description>
     </class>
   </library>

* ``name`` 属性是创建的插件名称。它必须在所有插件中唯一，但不会在其他地方直接使用。
* ``type`` 属性指定 Python 中导入插件类的路径，格式为 ``package_name.module_name.class_name``。

定义插件
--------

现在需要实现 ``the_plugin.py`` Python 模块（即 ``plugins.xml`` 中引用的模块）。

首先，确保 ``rqt_bag_diagnostics_demo`` 子目录中存在一个空文件 ``__init__.py``，使其成为 Python 包。

.. note::

   根据 ROS 当前使用的 Python 包规范，ROS 功能包目录（``rqt_bag_diagnostics_demo``）内部还包含一个同名子目录。因此完整路径应为：

   ``WORKSPACE/src/rqt_bag_diagnostics_demo/rqt_bag_diagnostics_demo/__init__.py``。

在 ``__init__.py`` 旁边创建 ``the_plugin.py``。该文件将包含插件的全部代码。

首先定义核心 Plugin 类：

.. code-block:: python

   from rqt_bag.plugins.plugin import Plugin
   from python_qt_binding.QtCore import Qt
   from diagnostic_msgs.msg import DiagnosticStatus


   def get_color(diagnostic):
       if diagnostic.level == DiagnosticStatus.OK:
           return Qt.green
       elif diagnostic.level == DiagnosticStatus.WARN:
           return Qt.yellow
       else:  # ERROR 或 STALE
           return Qt.red


   class DiagnosticBagPlugin(Plugin):
       def __init__(self):
           pass

       def get_view_class(self):
           # 该方法是必需的，稍后实现
           return None

       def get_renderer_class(self):
           return None

       def get_message_types(self):
           return ['diagnostic_msgs/msg/DiagnosticStatus']

这里包含一些基础导入、稍后会用到的辅助函数，以及一个定义 rqt_bag 插件三个组成部分的类：

1. ``view_class``，也称为 ``TopicMessageView``：用于查看单条消息的独立面板。
2. ``renderer_class``，也称为 ``TimelineView``：用于在 bag 时间轴上绘制内容。
3. ``message_types``：字符串数组，用于指定该插件支持的消息类型。返回 ``['*']`` 表示插件可以应用于所有消息类型。

由于当前两个方法都返回 ``None``，因此这个插件暂时不会执行任何操作。接下来分别实现这两部分功能。

TopicMessageView
----------------

版本 1
^^^^^^

创建一个继承自 ``TopicMessageView`` 的类（仍然放在 ``the_plugin.py`` 中）。

首先添加导入语句：

.. code-block:: python

   from rqt_bag import TopicMessageView

然后定义新类：

.. code-block:: python

   class DiagnosticPanel(TopicMessageView):
       name = 'Awesome Diagnostic'

       def message_viewed(self, bag, entry, ros_message, msg_type_name, topic):
           super(DiagnosticPanel, self).message_viewed(
               bag=bag, entry=entry, ros_message=ros_message,
               msg_type_name=msg_type_name, topic=topic)
           print(f'{topic}: {ros_message}')

这里定义了两项内容：

* ``name`` 类变量定义了用户在 rqt_bag 时间轴中右键单击 ``DiagnosticStatus`` 话题时看到的视图名称。
* ``message_viewed`` 方法定义了用户选择一条消息时要执行的操作。本例暂时只将消息打印到终端。

还需要将该类接入插件系统。为此，在 ``get_view_class`` 方法中返回类对象本身：

.. code-block:: python

   def get_view_class(self):
       return DiagnosticPanel

.. note::

   不要写成 ``return DiagnosticPanel()``（带括号）。正确写法是 ``return DiagnosticPanel``。

要查看效果，使用 bag 文件启动 ``rqt_bag``，然后在诊断话题对应的时间轴上单击鼠标右键。

在 View 菜单下会出现两个选项：Raw 和自定义的 Awesome Diagnostic。单击自定义选项后会打开一个面板，可以滚动浏览消息，并观察消息被打印到终端。

.. image:: images/rqtbag_plugin_panel.png
   :alt: rqt_bag 中显示空白的额外面板

版本 2
^^^^^^

``TopicMessageView`` 本身也是 ``QObject`` 的扩展类，因此可以利用 Qt 提供的丰富功能。

本教程不是 Python Qt 教程，网上有很多相关资料，例如 `Qt 基础绘图示例 <https://doc.qt.io/qtforpython-6/examples/example_widgets_painting_basicdrawing.html>`_。这里仅添加一个简单的 ``QWidget`` 并在其中绘图。

首先添加以下导入：

.. code-block:: python

   from python_qt_binding.QtWidgets import QWidget
   from python_qt_binding.QtGui import QBrush, QPainter

然后将 ``DiagnosticPanel`` 类更新为：

.. code-block:: python

   class DiagnosticPanel(TopicMessageView):
       name = 'Awesome Diagnostic'

       def __init__(self, timeline, parent, topic):
           super(DiagnosticPanel, self).__init__(timeline, parent, topic)
           self.widget = QWidget()
           parent.layout().addWidget(self.widget)
           self.msg = None
           self.widget.paintEvent = self.paintEvent

       def message_viewed(self, bag, entry, ros_message, msg_type_name, topic):
           super(DiagnosticPanel, self).message_viewed(
               bag=bag, entry=entry, ros_message=ros_message,
               msg_type_name=msg_type_name, topic=topic)
           self.msg = ros_message
           self.widget.update()

       def paintEvent(self, event):
           qp = QPainter()
           qp.begin(self.widget)

           rect = event.rect()

           if self.msg is None:
               qp.fillRect(0, 0, rect.width(), rect.height(), Qt.white)
           else:
               color = get_color(self.msg)
               qp.setBrush(QBrush(color))
               qp.drawEllipse(0, 0, rect.width(), rect.height())
           qp.end()

在构造函数中创建 ``QWidget``，并重写它的 ``paintEvent`` 方法。

收到 ``message_viewed`` 回调后，保存消息并更新控件。Qt 会在需要时调用 ``paintEvent``。

不要手动调用 ``paintEvent``，该方法应该由 Qt 负责调用。

在选择消息之前，面板会绘制白色矩形。选择消息后，则根据诊断级别调用辅助函数获取颜色，并绘制对应颜色的圆形。

.. image:: images/rqtbag_plugin_circle.png
   :alt: rqt_bag 额外面板中绘制的圆形

TimelineRenderer
----------------

版本 1
^^^^^^

要在时间轴上绘图，需要扩展 ``TimelineRenderer`` 类（仍然放在 ``the_plugin.py`` 中）。

首先添加导入：

.. code-block:: python

   from rqt_bag import TimelineRenderer

然后添加新类：

.. code-block:: python

   class DiagnosticTimeline(TimelineRenderer):
       def __init__(self, timeline, height=80):
           TimelineRenderer.__init__(self, timeline, msg_combine_px=height)

       def draw_timeline_segment(
           self, painter: QPainter, topic, start: float, end: float,
           x: float, y: int, width: float, height: int):
           painter.setBrush(QBrush(Qt.blue))
           painter.drawRect(int(x), y, int(width), height)

可以通过 ``msg_combine_px`` 参数自定义消息在时间轴中占用的高度。

需要重写的关键方法是 ``draw_timeline_segment()``，它会提供时间轴中需要绘制的区段。本例暂时只在每个区段上绘制蓝色矩形。

与消息视图类似，也需要修改插件类，使其返回自定义渲染器：

.. code-block:: python

   def get_renderer_class(self):
       return DiagnosticTimeline

要查看效果，需要在 rqt_bag GUI 中启用 ``Thumbnails`` 选项（这个名称可能有些误导）。

.. image:: images/rqtbag_plugin_blue.png
   :alt: rqt_bag 时间轴中绘制的蓝色矩形

版本 2
^^^^^^

现在希望根据消息内容自定义时间轴中的绘制效果。为此，需要从 bag 文件中读取并反序列化消息。

首先添加以下导入：

.. code-block:: python

   from python_qt_binding.QtGui import QPen
   from rclpy.time import Time
   from rclpy.serialization import deserialize_message
   from rqt_bag.bag_helper import to_sec

然后更新 ``draw_timeline_segment()``：

.. code-block:: python

   def draw_timeline_segment(
       self, painter: QPainter, topic, start: float, end: float,
       x: float, y: int, width: float, height: int):
       bag_timeline = self.timeline.scene()
       start_t = Time(seconds=start)
       end_t = Time(seconds=end)

       for bag, entry in bag_timeline.get_entries_with_bags([topic], start_t, end_t):
           topic, raw_data, t = bag_timeline.read_message(bag, entry.timestamp, topic)
           msg = deserialize_message(raw_data, DiagnosticStatus)
           color = get_color(msg)
           painter.setBrush(QBrush(color))
           painter.setPen(QPen(color, 5))

           t_float = to_sec(Time(nanoseconds=t))
           p_x = int(self.timeline.map_stamp_to_x(t_float))
           painter.drawLine(p_x, y, p_x, y + height - 1)

使用该方法的 ``topic``、``start`` 和 ``end`` 参数，可以获取当前时间轴区段对应的 bag 条目。

随后读取实际消息并进行反序列化，再根据诊断级别获取颜色并绘制对应的线条。

``map_stamp_to_x()`` 方法可以将以秒为单位的时间转换为控件像素位置，从而自动计算消息在时间轴中的水平位置。

.. image:: images/rqtbag_plugin_timeline.png
   :alt: rqt_bag 时间轴中根据诊断级别绘制的不同颜色线条

如果在时间轴中计算消息表示的过程比较耗费计算资源，应使用 `Timeline Cache <https://github.com/ros-visualization/rqt_bag/blob/rolling/rqt_bag/src/rqt_bag/timeline_cache.py>`_，例如 `ImageTimelineViewer <https://github.com/ros-visualization/rqt_bag/blob/rolling/rqt_bag_plugins/src/rqt_bag_plugins/image_timeline_renderer.py>`_ 就采用了这种方式。具体实现留作读者练习。
