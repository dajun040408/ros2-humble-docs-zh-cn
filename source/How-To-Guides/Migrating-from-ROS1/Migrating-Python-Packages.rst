ROS 1 Python 功能包迁移参考
==============================

.. redirect-from::

   Migration-Guide-Python
   The-ROS2-Project/Contributing/Migration-Guide-Python

本页面介绍如何将 Python 功能包从 ROS 1 迁移到 ROS 2。
如果这是第一次迁移 Python 功能包，请先按照示例 Python 功能包迁移指南完成示例迁移。

.. contents:: 目录
   :depth: 2
   :local:

构建工具
--------

ROS 2 不再使用 catkin_make、catkin_make_isolated 或 catkin build，而是使用命令行工具 colcon 构建和安装一组功能包。
入门教程请参阅 ROS 2 官方 Colcon 教程。

构建系统
--------

对于纯 Python 功能包，ROS 2 使用 Python 开发者熟悉的标准 setup.py 安装机制。

更新文件以使用 setup.py
^^^^^^^^^^^^^^^^^^^^^^^^

如果 ROS 1 功能包仅使用 CMake 调用 setup.py，且除 Python 代码外不包含其他内容（例如消息、服务等），则应将其转换为 ROS 2 中的纯 Python 功能包：

* 在 package.xml 文件中更新或添加构建类型：

  .. code-block:: xml

     <export>
       <build_type>ament_python</build_type>
     </export>

* 删除 CMakeLists.txt 文件。
* 将 setup.py 文件更新为标准 Python 安装脚本。

ROS 2 仅支持 Python 3。
每个功能包可以选择同时支持 Python 2，但如果使用其他 ROS 2 功能包提供的 API，则必须使用 Python 3 调用可执行程序。

更新源代码
----------

节点初始化
^^^^^^^^^^

ROS 1：

.. code-block:: python

   rospy.init_node('asdf')

   rospy.loginfo('Created node')

ROS 2：

.. code-block:: python

   rclpy.init(args=sys.argv)
   node = rclpy.create_node('asdf')

   node.get_logger().info('Created node')

ROS 参数
^^^^^^^^

ROS 1：

.. code-block:: python

   port = rospy.get_param('port', '/dev/ttyUSB0')
   assert isinstance(port, str), 'port parameter must be a str'

   baudrate = rospy.get_param('baudrate', 115200)
   assert isinstance(baudrate, int), 'baudrate parameter must be an integer'

   rospy.logwarn('port: ' + port)

ROS 2：

.. code-block:: python

   port = node.declare_parameter('port', '/dev/ttyUSB0').value
   assert isinstance(port, str), 'port parameter must be a str'

   baudrate = node.declare_parameter('baudrate', 115200).value
   assert isinstance(baudrate, int), 'baudrate parameter must be an integer'

   node.get_logger().warn('port: ' + port)

创建发布者
^^^^^^^^^^

ROS 1：

.. code-block:: python

   pub = rospy.Publisher('chatter', String)
   # or
   pub = rospy.Publisher('chatter', String, queue_size=10)

ROS 2：

.. code-block:: python

   pub = node.create_publisher(String, 'chatter', rclpy.qos.QoSProfile())
   # or
   pub = node.create_publisher(String, 'chatter', 10)

创建订阅者
^^^^^^^^^^

ROS 1：

.. code-block:: python

   sub = rospy.Subscriber('chatter', String, callback)
   # or
   sub = rospy.Subscriber('chatter', String, callback, queue_size=10)

ROS 2：

.. code-block:: python

   sub = node.create_subscription(String, 'chatter', callback, rclpy.qos.QoSProfile())
   # or
   sub = node.create_subscription(String, 'chatter', callback, 10)

创建服务端
^^^^^^^^^^

ROS 1：

.. code-block:: python

   srv = rospy.Service('add_two_ints', AddTwoInts, add_two_ints_callback)

ROS 2：

.. code-block:: python

   srv = node.create_service(AddTwoInts, 'add_two_ints', add_two_ints_callback)

创建服务客户端
^^^^^^^^^^^^^^

ROS 1：

.. code-block:: python

   rospy.wait_for_service('add_two_ints')
   add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
   resp = add_two_ints(req)

ROS 2：

.. code-block:: python

   add_two_ints = node.create_client(AddTwoInts, 'add_two_ints')
   while not add_two_ints.wait_for_service(timeout_sec=1.0):
       node.get_logger().info('service not available, waiting again...')
   resp = add_two_ints.call_async(req)
   rclpy.spin_until_future_complete(node, resp)

.. warning::

   不要在 ROS 2 回调函数中使用 rclpy.spin_until_future_complete。
   更多详情请参阅同步与异步调用死锁说明。
