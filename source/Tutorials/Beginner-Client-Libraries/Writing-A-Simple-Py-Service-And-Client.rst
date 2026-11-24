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

example_interfaces 软件包包含 AddTwoInts.srv，用于定义请求和响应：

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

返回工作空间根目录并构建：

.. code-block:: console

   $ colcon build --packages-select py_srvcli

打开一个终端，source 工作空间并启动服务端：

.. code-block:: console

   $ ros2 run py_srvcli service

打开另一个终端，运行客户端并传入两个整数：

.. code-block:: console

   $ ros2 run py_srvcli client 2 3

客户端会收到并输出两个整数的和。

总结
----

你已经创建并运行了一个 Python 服务端和客户端。客户端发送两个整数，服务端计算并返回它们的和。
