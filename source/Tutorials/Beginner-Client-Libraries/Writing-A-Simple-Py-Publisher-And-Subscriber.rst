.. redirect-from::

    Tutorials/Writing-A-Simple-Py-Publisher-And-Subscriber

.. _PyPubSub:

编写简单的发布者和订阅者（Python）
==================================

**目标：** 使用 Python 创建并运行发布者和订阅者节点。

**教程级别：** 初级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程将创建 :doc:§节点 <../Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes>§，让它们通过 :doc:§话题 <../Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics>§ 交换字符串消息。

示例采用简单的 talker 和 listener 系统：一个节点发布数据，另一个节点订阅话题并接收数据。示例代码位于§ros2/examples/rclpy/topics <https://github.com/ros2/examples/tree/{REPOS_FILE_BRANCH}/rclpy/topics>§_。

前置条件
--------

此前的教程已经介绍了如何 :doc:§创建工作空间 <./Creating-A-Workspace/Creating-A-Workspace>§ 和 :doc:§创建功能包 <./Creating-Your-First-ROS2-Package>§。

建议具备基本 Python 知识，但不是硬性要求。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

打开新终端并 :doc:§source ROS 2 安装环境 <../Beginner-CLI-Tools/Configuring-ROS2-Environment>§。

进入 ros2_ws/src 并创建功能包：

.. code-block:: console

  $ ros2 pkg create --build-type ament_python --license Apache-2.0 py_pubsub

终端会返回消息，确认 py_pubsub 功能包及其文件和目录已创建。

2. 编写发布者节点
^^^^^^^^^^^^^^^^^

进入 ros2_ws/src/py_pubsub/py_pubsub。该目录是一个与 ROS 2 功能包同名的 Python 包。

下载示例 talker 代码：

.. code-block:: console

   $ wget https://raw.githubusercontent.com/ros2/examples/{REPOS_FILE_BRANCH}/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py

Windows 命令行可以使用 curl 下载同一文件。

打开 publisher_member_function.py。示例会继承 rclpy.node.Node 创建 MinimalPublisher，通过 create_publisher() 创建 std_msgs.msg.String 发布者，并通过定时器周期性发布消息。

.. code-block:: python

    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String

    class MinimalPublisher(Node):
        def __init__(self):
            super().__init__('minimal_publisher')
            self.publisher_ = self.create_publisher(String, 'topic', 10)
            self.timer = self.create_timer(0.5, self.timer_callback)
            self.i = 0

        def timer_callback(self):
            msg = String()
            msg.data = 'Hello World: %d' % self.i
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.i += 1

    def main(args=None):
        rclpy.init(args=args)
        node = MinimalPublisher()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()

3. 编写订阅者节点
^^^^^^^^^^^^^^^^^

在同一 Python 包目录中创建 subscriber_member_function.py。订阅者通过 create_subscription() 订阅 topic 话题，并在回调函数中输出收到的字符串消息。

.. code-block:: python

    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String

    class MinimalSubscriber(Node):
        def __init__(self):
            super().__init__('minimal_subscriber')
            self.subscription = self.create_subscription(
                String, 'topic', self.listener_callback, 10)

        def listener_callback(self, msg):
            self.get_logger().info('I heard: "%s"' % msg.data)

    def main(args=None):
        rclpy.init(args=args)
        node = MinimalSubscriber()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()

4. 添加入口点
^^^^^^^^^^^^^

打开 setup.py，在 console_scripts 中为发布者和订阅者添加入口点：

.. code-block:: python

    entry_points={
        'console_scripts': [
            'talker = py_pubsub.publisher_member_function:main',
            'listener = py_pubsub.subscriber_member_function:main',
        ],
    },

5. 构建并运行
^^^^^^^^^^^^^

返回工作空间根目录并构建：

.. code-block:: console

   $ colcon build --packages-select py_pubsub

打开两个终端，分别 source 工作空间并运行发布者和订阅者：

.. code-block:: console

   $ ros2 run py_pubsub talker

.. code-block:: console

   $ ros2 run py_pubsub listener

发布者会周期性发布 Hello World 字符串，订阅者会输出接收到的消息。

总结
----

你已经创建并运行了一个 Python 发布者和订阅者节点，它们通过话题交换字符串消息。
