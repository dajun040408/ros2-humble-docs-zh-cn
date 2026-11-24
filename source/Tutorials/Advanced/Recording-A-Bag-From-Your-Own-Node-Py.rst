.. redirect-from::

    Tutorials/Ros2bag/Recording-A-Bag-From-Your-Own-Node-Python

.. _ROS2BagOwnNodePython:

从节点录制 bag（Python）
========================

**目标：** 将自己的 Python 节点数据录制到 bag。

**教程级别：** 高级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

rosbag2 不仅提供 ros2 bag 命令行工具，还提供 Python API，可以在自己的源代码中读取和写入 bag。这样可以订阅话题，并在执行其他数据处理的同时，将收到的数据保存到 bag。

例如，可以同时保存话题数据及其处理结果，而不必为了录制处理结果专门再通过话题发送数据。由于 bag 可以记录任意数据，也可以保存来自非话题来源的数据，例如用于训练集的合成数据。这对于快速生成大量样本、覆盖较长回放时间范围尤其有用。

前置条件
--------

常规 ROS 2 安装中应已包含 rosbag2。如果通过 Linux deb 软件包安装，通常默认已安装；如果没有，可以运行：

.. code-block:: console

  $ sudo apt install ros-{DISTRO}-rosbag2

请先完成 :doc:§ROS 2 bag 基础教程 <../Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data>§。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

打开新终端并 :doc:§source ROS 2 安装环境 <../Beginner-CLI-Tools/Configuring-ROS2-Environment>§。

按照 :ref:§创建工作空间说明 <new-directory>§ 创建名为 ros2_ws 的工作空间。在 ros2_ws/src 目录中创建新功能包：

.. code-block:: console

  $ ros2 pkg create --build-type ament_python --license Apache-2.0 bag_recorder_nodes_py --dependencies rclpy rosbag2_py example_interfaces std_msgs

--dependencies 参数会自动将依赖项添加到 package.xml。本例使用 rosbag2_py 和 rclpy，消息定义还需要 example_interfaces。

在 package.xml 中填写描述、维护者信息和许可证：

.. code-block:: xml

  <description>Python bag writing tutorial</description>
  <maintainer email="you@email.com">Your Name</maintainer>
  <license>Apache License 2.0</license>

同时在 setup.py 中填写相同信息：

.. code-block:: python

   maintainer='Your Name',
   maintainer_email='you@email.com',
   description='Python bag writing tutorial',
   license='Apache License 2.0',

2. 编写 Python 节点
^^^^^^^^^^^^^^^^^^^

在 ros2_ws/src/bag_recorder_nodes_py/bag_recorder_nodes_py 目录中创建 simple_bag_recorder.py：

.. code-block:: python

   import rclpy
   from rclpy.node import Node
   from rclpy.serialization import serialize_message
   from std_msgs.msg import String

   import rosbag2_py

   class SimpleBagRecorder(Node):
       def __init__(self):
           super().__init__('simple_bag_recorder')
           self.writer = rosbag2_py.SequentialWriter()

           storage_options = rosbag2_py.StorageOptions(
               uri='my_bag',
               storage_id='sqlite3')
           converter_options = rosbag2_py.ConverterOptions('', '')
           self.writer.open(storage_options, converter_options)

           topic_info = rosbag2_py.TopicMetadata(
               name='chatter',
               type='std_msgs/msg/String',
               serialization_format='cdr')
           self.writer.create_topic(topic_info)

           self.subscription = self.create_subscription(
               String, 'chatter', self.topic_callback, 10)

       def topic_callback(self, msg):
           self.writer.write(
               'chatter',
               serialize_message(msg),
               self.get_clock().now().nanoseconds)


   def main(args=None):
       rclpy.init(args=args)
       sbr = SimpleBagRecorder()
       rclpy.spin(sbr)
       rclpy.shutdown()


   if __name__ == '__main__':
       main()

2.1 理解代码
~~~~~~~~~~~~

文件顶部的 import 语句对应功能包依赖项。这里导入 rosbag2_py，以使用 bag 文件相关函数和结构。

构造函数首先创建 SequentialWriter。它会按照消息收到的顺序将消息写入 bag。rosbag2 中还可能提供其他具有不同处理行为的 writer。

然后打开 bag，指定 URI 和存储格式 sqlite3。默认转换选项不会进行转换，而是按照收到消息时的序列化格式保存。

接下来创建 TopicMetadata 对象，并通过 writer.create_topic 注册话题。元数据包括话题名称、数据类型和序列化格式。

订阅者回调接收未序列化的 ROS 消息（这是 rclpy API 的标准行为），而 writer 需要序列化消息，因此需要调用 serialize_message() 后再写入 bag。写入时还要指定话题名称和时间戳。

2.2 添加入口点
~~~~~~~~~~~~~~

打开 bag_recorder_nodes_py 功能包中的 setup.py，为节点添加入口点：

.. code-block:: python

   entry_points={
       'console_scripts': [
           'simple_bag_recorder = bag_recorder_nodes_py.simple_bag_recorder:main',
       ],
   },

3. 构建并运行
^^^^^^^^^^^^^

返回 ros2_ws 工作空间根目录并构建：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ colcon build --packages-select bag_recorder_nodes_py

  .. group-tab:: macOS

    .. code-block:: console

      $ colcon build --packages-select bag_recorder_nodes_py

  .. group-tab:: Windows

    .. code-block:: console

      $ colcon build --merge-install --packages-select bag_recorder_nodes_py

打开新终端并 source 设置文件：

.. code-block:: console

   $ source install/setup.bash

Windows 使用：

.. code-block:: console

   $ call install/setup.bat

运行节点：

.. code-block:: console

   $ ros2 run bag_recorder_nodes_py simple_bag_recorder

在第二个终端中运行 Python talker：

.. code-block:: console

   $ ros2 run demo_nodes_py talker

talker 会在 chatter 话题上发布数据，bag 录制节点会将接收到的数据写入 my_bag。若 my_bag 目录已存在，需要先删除，因为 rosbag2 默认不会覆盖已有 bag。

停止两个节点后，在一个终端中启动 listener：

.. code-block:: console

   $ ros2 run demo_nodes_py listener

在另一个终端中回放 bag：

.. code-block:: console

   $ ros2 bag play my_bag

listener 节点应该能够接收到 bag 中的消息。如果希望再次运行录制节点，需要先删除 my_bag 目录。

4. 从节点录制合成数据
^^^^^^^^^^^^^^^^^^^^^

bag 不仅可以记录话题数据，也可以记录任意数据。常见场景是生成并保存合成数据。本节介绍两种方式：第一种使用带定时器的节点，适用于从硬件读取数据等场景；第二种不使用节点，适用于不需要 ROS 基础设施功能的情况。

4.1 编写 Python 节点
~~~~~~~~~~~~~~~~~~~~

在功能包目录中创建 data_generator_node.py：

.. code-block:: python

   import rclpy
   from rclpy.node import Node
   from rclpy.serialization import serialize_message
   from example_interfaces.msg import Int32
   import rosbag2_py

   class DataGeneratorNode(Node):
       def __init__(self):
           super().__init__('data_generator_node')
           self.data = Int32()
           self.data.data = 0
           self.writer = rosbag2_py.SequentialWriter()

           storage_options = rosbag2_py.StorageOptions(
               uri='timed_synthetic_bag',
               storage_id='sqlite3')
           converter_options = rosbag2_py.ConverterOptions('', '')
           self.writer.open(storage_options, converter_options)

           topic_info = rosbag2_py.TopicMetadata(
               name='synthetic',
               type='example_interfaces/msg/Int32',
               serialization_format='cdr')
           self.writer.create_topic(topic_info)

           self.timer = self.create_timer(1, self.timer_callback)

       def timer_callback(self):
           self.writer.write(
               'synthetic',
               serialize_message(self.data),
               self.get_clock().now().nanoseconds)
           self.data.data += 1


   def main(args=None):
       rclpy.init(args=args)
       dgn = DataGeneratorNode()
       rclpy.spin(dgn)
       rclpy.shutdown()


   if __name__ == '__main__':
       main()

4.2 理解代码
~~~~~~~~~~~~

与前一个示例相比，主要变化是将订阅者替换为定时器。定时器每秒触发一次，并调用指定回调函数。

回调中生成（或从串口连接的硬件等外部设备读取）需要写入 bag 的数据。与前一个示例一样，消息尚未序列化，因此写入前需要调用 serialize_message()。

4.3 添加入口点
~~~~~~~~~~~~~~

在 setup.py 中增加入口点：

.. code-block:: python

   entry_points={
       'console_scripts': [
           'simple_bag_recorder = bag_recorder_nodes_py.simple_bag_recorder:main',
           'data_generator_node = bag_recorder_nodes_py.data_generator_node:main',
       ],
   },

4.4 构建并运行
~~~~~~~~~~~~~~

构建功能包并 source 工作空间后，运行：

.. code-block:: console

   $ ros2 run bag_recorder_nodes_py data_generator_node

等待约 30 秒，然后按 Ctrl+C 终止节点。回放生成的 bag：

.. code-block:: console

   $ ros2 bag play timed_synthetic_bag

在另一个终端中查看 /synthetic 话题：

.. code-block:: console

   $ ros2 topic echo /synthetic

你会看到生成并保存的数据以每秒一条的速率输出。

5. 从可执行程序录制合成数据
^^^^^^^^^^^^^^^^^^^^^^^^^^^

现在已经能够将非话题数据写入 bag，接下来学习如何从不使用 ROS 节点的可执行程序生成并录制合成数据。这种方式代码更简单，也能够快速生成大量数据。

可执行程序可以使用循环生成数据，并为每条消息指定时间戳。bag 回放时会根据这些时间戳确定播放速率，因此可以控制默认回放速度。即使相邻样本的时间间隔为一秒，程序也不必真的等待一秒再生成下一条消息。

总结
----

你创建了一个订阅话题并将收到的数据写入 bag 的 Python 节点，并通过回放验证了录制结果。随后还创建了生成合成数据并保存到 bag 的节点。对于训练数据集等场景，这种方式尤其有用。
