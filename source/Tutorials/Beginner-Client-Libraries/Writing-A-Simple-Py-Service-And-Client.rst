.. redirect-from::

    Tutorials/Writing-A-Simple-Py-Service-And-Client

.. _PySrvCli:

编写简单的服务和客户端（Python）
================================

**目标：** 使用 Python 创建并运行服务端和客户端节点。

**教程级别：** 初级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

当 :doc:`节点 <../Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes>` 使用 :doc:`服务 <../Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services>` 通信时，发送数据请求的节点称为客户端节点，响应请求的节点称为服务端节点。请求和响应的数据结构由 .srv 文件定义。

本示例是一个简单的整数加法系统：一个节点请求两个整数的和，另一个节点返回计算结果。

前置条件
--------

此前的教程已经介绍了如何 :doc:`创建工作空间 <./Creating-A-Workspace/Creating-A-Workspace>` 和 :doc:`创建功能包 <./Creating-Your-First-ROS2-Package>`。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

打开新终端并 :doc:`source ROS 2 安装环境 <../Beginner-CLI-Tools/Configuring-ROS2-Environment>`。

进入 ros2_ws/src 并创建功能包：

.. code-block:: console

  $ ros2 pkg create --build-type ament_python --license Apache-2.0 py_srvcli --dependencies rclpy example_interfaces

``--dependencies`` 参数会自动在 ``package.xml`` 中添加必要的依赖项。``example_interfaces`` 软件包包含用于定义请求和响应的 `AddTwoInts.srv 文件 <https://github.com/ros2/example_interfaces/blob/{REPOS_FILE_BRANCH}/srv/AddTwoInts.srv>`_：

.. code-block:: text

    int64 a
    int64 b
    ---
    int64 sum

横线之前的两行是请求参数，横线之后是响应内容。

在 package.xml 中填写描述、维护者信息和许可证：

.. code-block:: xml

  <description>Python client server tutorial</description>
  <maintainer email="you@email.com">Your Name</maintainer>
  <license>Apache License 2.0</license>

同时在 setup.py 中填写相同信息：

.. code-block:: python

    maintainer='Your Name',
    maintainer_email='you@email.com',
    description='Python client server tutorial',
    license='Apache License 2.0',

1.1 更新 package.xml
~~~~~~~~~~~~~~~~~~~~~~

由于创建功能包时使用了 ``--dependencies`` 选项，因此无需手动向 ``package.xml`` 添加依赖项。

不过，仍需在 ``package.xml`` 中填写功能包描述、维护者邮箱和姓名，以及许可证信息：

.. code-block:: xml

   <description>Python client server tutorial</description>
   <maintainer email="you@email.com">Your Name</maintainer>
   <license>Apache License 2.0</license>

1.2 更新 setup.py
~~~~~~~~~~~~~~~~~~~~

在 ``setup.py`` 文件中，为 ``maintainer``、``maintainer_email``、``description`` 和 ``license`` 字段填写与 ``package.xml`` 相同的信息：

.. code-block:: python

   maintainer='Your Name',
   maintainer_email='you@email.com',
   description='Python client server tutorial',
   license='Apache License 2.0',

2. 编写服务端节点
^^^^^^^^^^^^^^^^^

在 ros2_ws/src/py_srvcli/py_srvcli 目录中创建 service_member_function.py：

.. code-block:: python

    from example_interfaces.srv import AddTwoInts
    import rclpy
    from rclpy.node import Node

    class MinimalService(Node):
        def __init__(self):
            super().__init__('minimal_service')
            self.srv = self.create_service(
                AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

        def add_two_ints_callback(self, request, response):
            response.sum = request.a + request.b
            self.get_logger().info(
                'Incoming request: a=%d b=%d' % (request.a, request.b))
            return response

    def main(args=None):
        rclpy.init(args=args)
        node = MinimalService()
        rclpy.spin(node)
        rclpy.shutdown()

    if __name__ == '__main__':
        main()

2.1 理解代码
~~~~~~~~~~~~~

第一个 import 语句从 ``example_interfaces`` 功能包导入 ``AddTwoInts`` 服务类型。接下来的 import 语句导入 ROS 2 Python 客户端库及其中的 ``Node`` 类。

.. code-block:: python

   from example_interfaces.srv import AddTwoInts

   import rclpy
   from rclpy.node import Node

``MinimalService`` 类的构造函数将节点命名为 ``minimal_service``，随后创建服务，并指定服务类型、服务名称和处理请求的回调函数。

.. code-block:: python

   def __init__(self):
       super().__init__('minimal_service')
       self.srv = self.create_service(
           AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

服务回调函数接收请求数据，将两个整数相加，把结果写入响应并返回：

.. code-block:: python

   def add_two_ints_callback(self, request, response):
       response.sum = request.a + request.b
       self.get_logger().info(
           'Incoming request: a=%d b=%d' % (request.a, request.b))
       return response

最后，``main`` 函数初始化 ROS 2 Python 客户端库，实例化 ``MinimalService`` 创建服务节点，并通过 ``rclpy.spin`` 让节点持续处理回调。

2.2 添加入口点
~~~~~~~~~~~~~~~~~~~~

为了让 ``ros2 run`` 能够运行服务端节点，需要在 ``setup.py``（位于 ``ros2_ws/src/py_srvcli``）中添加入口点。

在 ``console_scripts`` 列表中添加：

.. code-block:: python

   'service = py_srvcli.service_member_function:main',

3. 编写客户端节点
^^^^^^^^^^^^^^^^^

创建 client_member_function.py。客户端使用 create_client() 创建服务客户端，等待服务可用后发送请求，并读取响应结果。

.. code-block:: python

    import sys
    import rclpy
    from rclpy.node import Node
    from example_interfaces.srv import AddTwoInts

    class MinimalClient(Node):
        def __init__(self):
            super().__init__('minimal_client')
            self.cli = self.create_client(AddTwoInts, 'add_two_ints')
            while not self.cli.wait_for_service(timeout_sec=1.0):
                self.get_logger().info('service not available, waiting again...')
            self.req = AddTwoInts.Request()

        def send_request(self):
            self.req.a = int(sys.argv[1])
            self.req.b = int(sys.argv[2])
            return self.cli.call_async(self.req)

    def main(args=None):
        rclpy.init(args=args)
        client = MinimalClient()
        future = client.send_request()
        rclpy.spin_until_future_complete(client, future)
        response = future.result()
        client.get_logger().info('Result of add_two_ints: %d' % response.sum)
        client.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()

3.1 理解代码
~~~~~~~~~~~~~

与服务端代码一样，首先导入所需的库：

.. code-block:: python

   import sys

   from example_interfaces.srv import AddTwoInts
   import rclpy
   from rclpy.node import Node

``MinimalClient`` 类的构造函数将节点命名为 ``minimal_client``。随后创建客户端，并使用与服务端相同的服务类型和名称。客户端和服务端的类型、名称必须匹配，才能正常通信。

构造函数中的 ``while`` 循环每隔 1 秒检查一次是否存在与客户端类型和名称匹配的服务。最后创建一个新的 ``AddTwoInts`` 请求对象。

.. code-block:: python

   def __init__(self):
       super().__init__('minimal_client')
       self.cli = self.create_client(AddTwoInts, 'add_two_ints')
       while not self.cli.wait_for_service(timeout_sec=1.0):
           self.get_logger().info('service not available, waiting again...')
       self.req = AddTwoInts.Request()

``send_request`` 方法将两个整数写入请求对象，并异步发送请求。它返回一个 future 对象，用于在请求完成后获取响应。

.. code-block:: python

   def send_request(self):
       self.req.a = int(sys.argv[1])
       self.req.b = int(sys.argv[2])
       return self.cli.call_async(self.req)

最后，``main`` 函数创建 ``MinimalClient`` 对象，发送请求，并通过 ``rclpy.spin_until_future_complete`` 等待结果，随后将计算结果写入日志。

.. code-block:: python

   client = MinimalClient()
   future = client.send_request()
   rclpy.spin_until_future_complete(client, future)
   response = future.result()
   client.get_logger().info(
       'Result of add_two_ints: %d' % response.sum)

.. warning::

   不要在 ROS 2 回调函数中使用 ``rclpy.spin_until_future_complete``，否则可能导致死锁。更多信息请参阅 :doc:`同步与异步客户端 <../../../How-To-Guides/Sync-Vs-Async>`。

3.2 添加入口点
~~~~~~~~~~~~~~~~~~~~

与服务端节点一样，客户端节点也需要在 ``setup.py`` 中添加入口点。

``setup.py`` 中的 ``entry_points`` 字段应如下所示：

.. code-block:: python

   entry_points={
       'console_scripts': [
           'service = py_srvcli.service_member_function:main',
           'client = py_srvcli.client_member_function:main',
       ],
   },

4. 添加入口点
^^^^^^^^^^^^^

打开 setup.py，在 console_scripts 中添加服务端和客户端入口点：

.. code-block:: python

    entry_points={
        'console_scripts': [
            'service = py_srvcli.service_member_function:main',
            'client = py_srvcli.client_member_function:main',
        ],
    },

5. 构建并运行
^^^^^^^^^^^^^

构建之前，建议在工作空间根目录 ``ros2_ws`` 中运行 ``rosdep``，检查是否缺少依赖：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

   .. group-tab:: macOS

      ``rosdep`` 仅在 Linux 上运行，可以跳过此步骤。

   .. group-tab:: Windows

      ``rosdep`` 仅在 Linux 上运行，可以跳过此步骤。

返回工作空间根目录 ``ros2_ws``，构建新功能包：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ colcon build --packages-select py_srvcli

   .. group-tab:: macOS

      .. code-block:: console

         $ colcon build --packages-select py_srvcli

   .. group-tab:: Windows

      .. code-block:: console

         $ colcon build --merge-install --packages-select py_srvcli

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

总结
----

你创建了两个节点，通过服务请求和响应数据。你还在功能包配置文件中添加了依赖项和入口点，以便构建和运行完整的服务/客户端系统。

下一步
------

在前面的几个教程中，你已经使用接口在话题和服务之间传递数据。接下来将学习如何 :doc:`创建自定义接口 <./Custom-ROS2-Interfaces>`。

相关内容
--------

Python 服务端和客户端有多种实现方式。可以查看 `ros2/examples 仓库 <https://github.com/ros2/examples/tree/{REPOS_FILE_BRANCH}/rclpy/services>`_ 中的 ``minimal_client`` 和 ``minimal_service`` 功能包。

本教程在客户端节点中使用 ``call_async()`` API 调用服务。Python 还提供另一种同步服务调用 API。虽然不建议使用同步调用，但如果希望进一步了解，可以阅读 :doc:`同步与异步客户端指南 <../../How-To-Guides/Sync-Vs-Async>`。
