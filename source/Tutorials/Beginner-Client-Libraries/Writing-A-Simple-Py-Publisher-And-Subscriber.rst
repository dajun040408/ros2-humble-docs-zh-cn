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

本教程将创建 :doc:`节点 <../Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes>`，让它们通过 :doc:`话题 <../Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics>` 交换字符串消息。

示例采用简单的 talker 和 listener 系统：一个节点发布数据，另一个节点订阅话题并接收数据。示例代码位于 `ros2/examples 仓库 <https://github.com/ros2/examples/tree/{REPOS_FILE_BRANCH}/rclpy/topics>`_。

前置条件
--------

此前的教程已经介绍了如何 :doc:`创建工作空间 <./Creating-A-Workspace/Creating-A-Workspace>` 和 :doc:`创建功能包 <./Creating-Your-First-ROS2-Package>`。

建议具备基本 Python 知识，但不是硬性要求。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

打开新终端并 :doc:`source ROS 2 安装环境 <../Beginner-CLI-Tools/Configuring-ROS2-Environment>`。

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

2.1 理解代码
~~~~~~~~~~~~~

代码首先导入 ``rclpy``，并从 ``rclpy.node`` 导入 ``Node`` 类，以便创建 ROS 2 节点：

.. code-block:: python

   import rclpy
   from rclpy.node import Node

接下来，从 ``std_msgs.msg`` 导入内置的 ``String`` 消息类型。节点使用该类型组织通过话题传递的数据：

.. code-block:: python

   from std_msgs.msg import String

这些导入语句代表节点的依赖项。还需要在 ``package.xml`` 中声明这些依赖，下一节会进行配置。

随后创建 ``MinimalPublisher`` 类，并使其继承 ``Node``。这样，该类就具备 ROS 2 节点的功能。

.. code-block:: python

   class MinimalPublisher(Node):

构造函数中，``super().__init__`` 调用父类 ``Node`` 的构造函数，并将节点命名为 ``minimal_publisher``。

``create_publisher`` 声明该节点通过名为 ``topic`` 的话题发布 ``String`` 类型消息，队列深度为 10。队列深度是 QoS 配置的一部分，用于限制订阅者处理速度不足时积压的消息数量。

随后，``create_timer`` 创建一个每 0.5 秒执行一次的回调。``self.i`` 是回调函数中使用的计数器。

.. code-block:: python

   def __init__(self):
       super().__init__('minimal_publisher')
       self.publisher_ = self.create_publisher(String, 'topic', 10)
       timer_period = 0.5  # seconds
       self.timer = self.create_timer(timer_period, self.timer_callback)
       self.i = 0

``timer_callback`` 创建一条消息，将计数器值写入消息数据，然后发布消息，并使用日志输出当前发布内容。

.. code-block:: python

   def timer_callback(self):
       msg = String()
       msg.data = 'Hello World: %d' % self.i
       self.publisher_.publish(msg)
       self.get_logger().info('Publishing: "%s"' % msg.data)
       self.i += 1

最后定义 ``main`` 函数：先初始化 ``rclpy``，再创建节点并通过 ``rclpy.spin`` 处理节点回调。退出时销毁节点并关闭 ROS 2。

.. code-block:: python

   def main(args=None):
       rclpy.init(args=args)
       minimal_publisher = MinimalPublisher()
       rclpy.spin(minimal_publisher)
       minimal_publisher.destroy_node()
       rclpy.shutdown()

2.2 添加依赖项
~~~~~~~~~~~~~~~~~~~~

返回一级目录 ``ros2_ws/src/py_pubsub``。这里已经为你创建了 ``setup.py``、``setup.cfg`` 和 ``package.xml`` 文件。

使用文本编辑器打开 ``package.xml``。按照 :doc:`创建 ROS 2 功能包 <./Creating-Your-First-ROS2-Package>` 教程中的说明，填写 ``<description>``、``<maintainer>`` 和 ``<license>`` 标签：

.. code-block:: xml

   <description>Examples of minimal publisher/subscriber using rclpy</description>
   <maintainer email="you@email.com">Your Name</maintainer>
   <license>Apache License 2.0</license>

在上述内容后添加与节点导入语句对应的运行时依赖：

.. code-block:: xml

   <exec_depend>rclpy</exec_depend>
   <exec_depend>std_msgs</exec_depend>

这表示该功能包运行时需要 ``rclpy`` 和 ``std_msgs``。保存文件。

2.3 添加入口点
~~~~~~~~~~~~~~~~~~~~

打开 ``setup.py``，确保其中的 ``maintainer``、``maintainer_email``、``description`` 和 ``license`` 字段与 ``package.xml`` 中的信息一致：

.. code-block:: python

   maintainer='YourName',
   maintainer_email='you@email.com',
   description='Examples of minimal publisher/subscriber using rclpy',
   license='Apache License 2.0',

在 ``entry_points`` 字段的 ``console_scripts`` 列表中添加发布者入口点：

.. code-block:: python

   entry_points={
       'console_scripts': [
           'talker = py_pubsub.publisher_member_function:main',
       ],
   },

保存文件。

2.4 检查 setup.cfg
~~~~~~~~~~~~~~~~~~~~

``setup.cfg`` 文件通常会在创建 Python 功能包时自动正确生成，其内容应类似于：

.. code-block:: ini

   [develop]
   script_dir=$base/lib/py_pubsub
   [install]
   install_scripts=$base/lib/py_pubsub

该配置告诉 setuptools 将可执行程序安装到 ``lib`` 目录，因为 ``ros2 run`` 会在该目录中查找它们。

现在可以先构建并运行发布者，但为了观察完整的发布者/订阅者系统，先继续创建订阅者节点。

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

3.1 理解代码
~~~~~~~~~~~~~

订阅者节点的代码与发布者节点非常相似。构造函数使用 ``create_subscription`` 创建订阅，并传入与发布者相同的话题名称和消息类型。发布者与订阅者必须使用一致的话题名称和消息类型才能通信。

.. code-block:: python

   self.subscription = self.create_subscription(
       String,
       'topic',
       self.listener_callback,
       10)

订阅者的构造函数和回调函数都不需要定时器，因为它不需要周期性执行任务。只要收到消息，回调函数就会被调用。

回调函数将收到的消息数据输出到控制台：

.. code-block:: python

   def listener_callback(self, msg):
       self.get_logger().info('I heard: "%s"' % msg.data)

``main`` 函数与发布者的 ``main`` 基本相同，只是创建并 spin 的对象换成了 ``MinimalSubscriber``：

.. code-block:: python

   minimal_subscriber = MinimalSubscriber()
   rclpy.spin(minimal_subscriber)

由于该节点与发布者具有相同的依赖项，因此无需在 ``package.xml`` 中添加新依赖。``setup.cfg`` 文件也不需要修改。

3.2 添加入口点
~~~~~~~~~~~~~~~~~~~~

重新打开 ``setup.py``，在发布者入口点下面添加订阅者入口点。``entry_points`` 字段现在应如下所示：

.. code-block:: python

   entry_points={
       'console_scripts': [
           'talker = py_pubsub.publisher_member_function:main',
           'listener = py_pubsub.subscriber_member_function:main',
       ],
   },

保存文件后，发布者/订阅者系统就准备好了。

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

通常，``rclpy`` 和 ``std_msgs`` 已经随 ROS 2 安装。构建之前，建议在工作空间根目录 ``ros2_ws`` 中运行 ``rosdep``，检查是否缺少依赖：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

   .. group-tab:: macOS

      ``rosdep`` 仅在 Linux 上运行，可以跳过此步骤。

   .. group-tab:: Windows

      ``rosdep`` 仅在 Linux 上运行，可以跳过此步骤。

仍在工作空间根目录 ``ros2_ws`` 中，构建新功能包：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ colcon build --packages-select py_pubsub

   .. group-tab:: macOS

      .. code-block:: console

         $ colcon build --packages-select py_pubsub

   .. group-tab:: Windows

      .. code-block:: console

         $ colcon build --merge-install --packages-select py_pubsub

打开一个新终端，进入 ``ros2_ws`` 并加载设置文件：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ source install/setup.bash

   .. group-tab:: macOS

      .. code-block:: console

         $ . install/setup.bash

   .. group-tab:: Windows

      .. code-block:: console

         $ call install/setup.bat

现在运行 talker 节点。终端应每隔 0.5 秒输出一次发布日志：

.. code-block:: console

   $ ros2 run py_pubsub talker
   [INFO] [minimal_publisher]: Publishing: "Hello World: 0"
   [INFO] [minimal_publisher]: Publishing: "Hello World: 1"
   [INFO] [minimal_publisher]: Publishing: "Hello World: 2"
   ...

再打开一个终端，在 ``ros2_ws`` 中重新加载设置文件，然后启动 listener 节点。listener 会从发布者当前的计数位置开始输出收到的消息：

.. code-block:: console

   $ ros2 run py_pubsub listener
   [INFO] [minimal_subscriber]: I heard: "Hello World: 10"
   [INFO] [minimal_subscriber]: I heard: "Hello World: 11"
   [INFO] [minimal_subscriber]: I heard: "Hello World: 12"

在两个终端中分别按 ``Ctrl+C``，停止节点。

总结
----

你创建了两个节点，通过话题发布和订阅数据。在运行节点之前，你还在功能包配置文件中添加了依赖项和入口点。

下一步
------

接下来，你将创建另一个使用服务/客户端模型的简单 ROS 2 功能包。你可以选择使用 :doc:`C++ <./Writing-A-Simple-Cpp-Service-And-Client>` 或 :doc:`Python <./Writing-A-Simple-Py-Service-And-Client>` 编写。

相关内容
--------

Python 发布者和订阅者有多种实现方式。可以查看 `ros2/examples 仓库 <https://github.com/ros2/examples/tree/{REPOS_FILE_BRANCH}/rclpy/topics>`_ 中的 ``minimal_publisher`` 和 ``minimal_subscriber`` 功能包。
