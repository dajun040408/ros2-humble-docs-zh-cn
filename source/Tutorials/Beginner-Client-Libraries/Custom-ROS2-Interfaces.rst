.. redirect-from::

    Tutorials/Custom-ROS2-Interfaces

.. _CustomInterfaces:

创建自定义 msg 和 srv 文件
==========================

**目标：** 定义自定义接口文件（.msg 和 .srv），并在 Python 和 C++ 节点中使用。

**教程级别：** 初级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

此前的教程已经使用消息和服务接口学习 :doc:`话题 <../Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics>`、:doc:`服务 <../Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services>`，以及简单的发布者/订阅者和服务端/客户端节点。

虽然优先使用预定义接口是很好的实践，但有时仍需要定义自己的消息和服务。本教程介绍创建自定义接口定义的基本方法。

前置条件
--------

需要一个 :doc:`ROS 2 工作空间 <./Creating-A-Workspace/Creating-A-Workspace>`。本教程还会使用此前创建的 C++ 和 Python 发布者/订阅者、服务端/客户端功能包测试新接口。

任务
----

1. 创建新功能包
^^^^^^^^^^^^^^^

本教程将在独立功能包中创建自定义 .msg 和 .srv 文件，然后在另一个功能包中使用它们。两个功能包应位于同一个工作空间中。

进入 ros2_ws/src 并创建新功能包：

.. code-block:: console

  $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 tutorial_interfaces

tutorial_interfaces 是新功能包的名称。自定义接口功能包必须使用 ament_cmake，但这不限制其他类型功能包使用其中的消息和服务。你可以在 ament_cmake 功能包中定义接口，然后在 C++ 或 Python 节点中使用。

.msg 和 .srv 文件必须分别放在名为 msg 和 srv 的目录中：

.. code-block:: console

  $ mkdir msg srv

2. 创建自定义定义
^^^^^^^^^^^^^^^^^

2.1 msg 定义
~~~~~~~~~~~~

在 tutorial_interfaces/msg 中创建 Num.msg，内容为：

.. code-block:: text

    int64 num

该自定义消息传递一个名为 num 的 64 位整数。

再创建 Sphere.msg：

.. code-block:: text

    geometry_msgs/Point center
    float64 radius

该消息使用了其他消息功能包中的类型，这里使用 geometry_msgs/Point。

2.2 srv 定义
~~~~~~~~~~~~

在 tutorial_interfaces/srv 中创建 AddThreeInts.srv：

.. code-block:: text

    int64 a
    int64 b
    int64 c
    ---
    int64 sum

该服务请求三个整数 a、b、c，并返回一个名为 sum 的整数。

3. 配置 CMakeLists.txt
^^^^^^^^^^^^^^^^^^^^^^

为了将接口转换为 C++、Python 等语言可用的代码，在 CMakeLists.txt 中添加：

.. code-block:: cmake

  find_package(geometry_msgs REQUIRED)
  find_package(rosidl_default_generators REQUIRED)

  rosidl_generate_interfaces(${PROJECT_NAME}
    "msg/Num.msg"
    "msg/Sphere.msg"
    "srv/AddThreeInts.srv"
    DEPENDENCIES geometry_msgs
  )

注意：rosidl_generate_interfaces 的第一个参数（库名称）必须以功能包名称开头，例如 ${PROJECT_NAME} 或 ${PROJECT_NAME}_suffix。详情参阅`相关问题 <https://github.com/ros2/rosidl/issues/441#issuecomment-591025515>`_。

4. 配置 package.xml
^^^^^^^^^^^^^^^^^^^

接口生成依赖 rosidl_default_generators，因此需要声明构建工具依赖。rosidl_default_runtime 是运行阶段依赖。rosidl_interface_packages 是该功能包所属的接口依赖组，需要通过 member_of_group 标签声明。

在 package.xml 的 package 元素中添加：

.. code-block:: xml

  <depend>geometry_msgs</depend>
  <buildtool_depend>rosidl_default_generators</buildtool_depend>
  <exec_depend>rosidl_default_runtime</exec_depend>
  <member_of_group>rosidl_interface_packages</member_of_group>

5. 构建 tutorial_interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^

在工作空间根目录运行：

.. code-block:: console

  $ colcon build --packages-select tutorial_interfaces

Windows 使用：

.. code-block:: console

  $ colcon build --merge-install --packages-select tutorial_interfaces

构建后，其他 ROS 2 功能包就可以发现这些接口。

6. 确认 msg 和 srv 已创建
^^^^^^^^^^^^^^^^^^^^^^^^^

打开新终端，在工作空间中 source 设置文件：

.. code-block:: console

  $ source install/setup.bash

Windows 使用：

.. code-block:: console

  $ call install/setup.bat

使用 ros2 interface show 检查接口：

.. code-block:: console

  $ ros2 interface show tutorial_interfaces/msg/Num
  int64 num

.. code-block:: console

  $ ros2 interface show tutorial_interfaces/msg/Sphere
  geometry_msgs/Point center
          float64 x
          float64 y
          float64 z
  float64 radius

.. code-block:: console

  $ ros2 interface show tutorial_interfaces/srv/AddThreeInts
  int64 a
  int64 b
  int64 c
  ---
  int64 sum

7. 测试新接口
^^^^^^^^^^^^^

本步骤可以使用此前教程中创建的功能包。只需对节点源代码、``CMakeLists.txt`` 和 ``package.xml`` 做少量修改，就可以使用新定义的接口。

7.1 使用 pub/sub 测试 Num.msg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

修改此前创建的发布者/订阅者功能包（:doc:`C++ <./Writing-A-Simple-Cpp-Publisher-And-Subscriber>` 或 :doc:`Python <./Writing-A-Simple-Py-Publisher-And-Subscriber>`），即可测试 ``Num.msg``。由于消息类型从标准字符串变成了数值类型，因此输出也会有所不同。

**发布者**

.. tabs::

  .. group-tab:: C++

    .. code-block:: c++

       #include <chrono>
       #include <memory>

       #include "rclcpp/rclcpp.hpp"
       #include "tutorial_interfaces/msg/num.hpp"

       using namespace std::chrono_literals;

       class MinimalPublisher : public rclcpp::Node
       {
       public:
         MinimalPublisher()
         : Node("minimal_publisher"), count_(0)
         {
           publisher_ = this->create_publisher<tutorial_interfaces::msg::Num>("topic", 10);
           timer_ = this->create_wall_timer(
             500ms, std::bind(&MinimalPublisher::timer_callback, this));
         }

       private:
         void timer_callback()
         {
           auto message = tutorial_interfaces::msg::Num();
           message.num = this->count_++;
           RCLCPP_INFO_STREAM(this->get_logger(), "Publishing: '" << message.num << "'");
           publisher_->publish(message);
         }
         rclcpp::TimerBase::SharedPtr timer_;
         rclcpp::Publisher<tutorial_interfaces::msg::Num>::SharedPtr publisher_;
         size_t count_;
       };

       int main(int argc, char * argv[])
       {
         rclcpp::init(argc, argv);
         rclcpp::spin(std::make_shared<MinimalPublisher>());
         rclcpp::shutdown();
         return 0;
       }

    .. include:: ../../_internal/Rclcpp-Convenience-Header-Note.rst

  .. group-tab:: Python

    .. code-block:: python

       import rclpy
       from rclpy.node import Node

       from tutorial_interfaces.msg import Num


       class MinimalPublisher(Node):

           def __init__(self):
               super().__init__('minimal_publisher')
               self.publisher_ = self.create_publisher(Num, 'topic', 10)
               timer_period = 0.5
               self.timer = self.create_timer(timer_period, self.timer_callback)
               self.i = 0

           def timer_callback(self):
               msg = Num()
               msg.num = self.i
               self.publisher_.publish(msg)
               self.get_logger().info('Publishing: "%d"' % msg.num)
               self.i += 1


       def main(args=None):
           rclpy.init(args=args)
           minimal_publisher = MinimalPublisher()
           rclpy.spin(minimal_publisher)
           minimal_publisher.destroy_node()
           rclpy.shutdown()


       if __name__ == '__main__':
           main()

**订阅者**

.. tabs::

  .. group-tab:: C++

    .. code-block:: c++

       #include <functional>
       #include <memory>

       #include "rclcpp/rclcpp.hpp"
       #include "tutorial_interfaces/msg/num.hpp"

       using std::placeholders::_1;

       class MinimalSubscriber : public rclcpp::Node
       {
       public:
         MinimalSubscriber()
         : Node("minimal_subscriber")
         {
           subscription_ = this->create_subscription<tutorial_interfaces::msg::Num>(
             "topic", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
         }

       private:
         void topic_callback(const tutorial_interfaces::msg::Num & msg) const
         {
           RCLCPP_INFO_STREAM(this->get_logger(), "I heard: '" << msg.num << "'");
         }
         rclcpp::Subscription<tutorial_interfaces::msg::Num>::SharedPtr subscription_;
       };

       int main(int argc, char * argv[])
       {
         rclcpp::init(argc, argv);
         rclcpp::spin(std::make_shared<MinimalSubscriber>());
         rclcpp::shutdown();
         return 0;
       }

  .. group-tab:: Python

    .. code-block:: python

       import rclpy
       from rclpy.node import Node

       from tutorial_interfaces.msg import Num


       class MinimalSubscriber(Node):

           def __init__(self):
               super().__init__('minimal_subscriber')
               self.subscription = self.create_subscription(
                   Num,
                   'topic',
                   self.listener_callback,
                   10)
               self.subscription

           def listener_callback(self, msg):
               self.get_logger().info('I heard: "%d"' % msg.num)


       def main(args=None):
           rclpy.init(args=args)
           minimal_subscriber = MinimalSubscriber()
           rclpy.spin(minimal_subscriber)
           minimal_subscriber.destroy_node()
           rclpy.shutdown()


       if __name__ == '__main__':
           main()

**CMakeLists.txt**

仅适用于 C++。添加以下内容：

.. code-block:: cmake

   find_package(ament_cmake REQUIRED)
   find_package(rclcpp REQUIRED)
   find_package(tutorial_interfaces REQUIRED)

   add_executable(talker src/publisher_lambda_function.cpp)
   ament_target_dependencies(talker rclcpp tutorial_interfaces)

   add_executable(listener src/subscriber_lambda_function.cpp)
   ament_target_dependencies(listener rclcpp tutorial_interfaces)

   install(TARGETS
     talker
     listener
     DESTINATION lib/${PROJECT_NAME})

   ament_package()

**package.xml**

根据语言添加依赖：

.. tabs::

  .. group-tab:: C++

    .. code-block:: xml

       <depend>tutorial_interfaces</depend>

  .. group-tab:: Python

    .. code-block:: xml

       <exec_depend>tutorial_interfaces</exec_depend>

保存修改后，构建使用自定义接口的功能包：

.. tabs::

  .. group-tab:: C++

    Linux/macOS：

    .. code-block:: console

       $ colcon build --packages-select cpp_pubsub

    Windows：

    .. code-block:: console

       $ colcon build --merge-install --packages-select cpp_pubsub

  .. group-tab:: Python

    Linux/macOS：

    .. code-block:: console

       $ colcon build --packages-select py_pubsub

    Windows：

    .. code-block:: console

       $ colcon build --merge-install --packages-select py_pubsub

然后打开两个新终端，分别加载 ``ros2_ws`` 工作空间环境，并运行：

.. tabs::

  .. group-tab:: C++

    .. code-block:: console

       $ ros2 run cpp_pubsub talker

    .. code-block:: console

       $ ros2 run cpp_pubsub listener

  .. group-tab:: Python

    .. code-block:: console

       $ ros2 run py_pubsub talker

    .. code-block:: console

       $ ros2 run py_pubsub listener

由于 ``Num.msg`` 只传递整数，talker 发布的应是整数值，而不是此前发布的字符串。终端输出应类似：

.. code-block:: console

   [INFO] [minimal_publisher]: Publishing: '0'
   [INFO] [minimal_publisher]: Publishing: '1'
   [INFO] [minimal_publisher]: Publishing: '2'

7.2 使用服务/客户端测试 AddThreeInts.srv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

修改此前教程中创建的服务/客户端功能包（:doc:`C++ <./Writing-A-Simple-Cpp-Service-And-Client>` 或 :doc:`Python <./Writing-A-Simple-Py-Service-And-Client>`），即可测试 ``AddThreeInts.srv``。

原来的服务请求包含两个整数，现在改为三个整数，因此输出也会有所不同。

**服务端**

.. tabs::

  .. group-tab:: C++

    .. code-block:: c++

       #include "rclcpp/rclcpp.hpp"
       #include "tutorial_interfaces/srv/add_three_ints.hpp"

       #include <memory>

       void add(
         const std::shared_ptr<tutorial_interfaces::srv::AddThreeInts::Request> request,
         std::shared_ptr<tutorial_interfaces::srv::AddThreeInts::Response> response)
       {
         response->sum = request->a + request->b + request->c;
         RCLCPP_INFO(rclcpp::get_logger("rclcpp"),
           "Incoming request a=%ld b=%ld c=%ld",
           request->a, request->b, request->c);
         RCLCPP_INFO(rclcpp::get_logger("rclcpp"),
           "Sending back response: [%ld]", static_cast<long int>(response->sum));
       }

       int main(int argc, char ** argv)
       {
         rclcpp::init(argc, argv);
         auto node = rclcpp::Node::make_shared("add_three_ints_server");
         auto service =
           node->create_service<tutorial_interfaces::srv::AddThreeInts>(
             "add_three_ints", &add);
         RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Ready to add three ints.");
         rclcpp::spin(node);
         rclcpp::shutdown();
         return 0;
       }

  .. group-tab:: Python

    .. code-block:: python

       from tutorial_interfaces.srv import AddThreeInts

       import rclpy
       from rclpy.node import Node


       class MinimalService(Node):

           def __init__(self):
               super().__init__('minimal_service')
               self.srv = self.create_service(
                   AddThreeInts, 'add_three_ints', self.add_three_ints_callback)

           def add_three_ints_callback(self, request, response):
               response.sum = request.a + request.b + request.c
               self.get_logger().info(
                   'Incoming request: a=%d b=%d c=%d' %
                   (request.a, request.b, request.c))
               return response


       def main(args=None):
           rclpy.init(args=args)
           minimal_service = MinimalService()
           rclpy.spin(minimal_service)
           rclpy.shutdown()


       if __name__ == '__main__':
           main()

**客户端**

.. tabs::

  .. group-tab:: C++

    .. code-block:: c++

       #include "rclcpp/rclcpp.hpp"
       #include "tutorial_interfaces/srv/add_three_ints.hpp"

       #include <chrono>
       #include <cstdlib>
       #include <memory>

       using namespace std::chrono_literals;

       int main(int argc, char ** argv)
       {
         rclcpp::init(argc, argv);

         if (argc != 4) {
           RCLCPP_INFO(rclcpp::get_logger("rclcpp"),
             "usage: add_three_ints_client X Y Z");
           return 1;
         }

         auto node = rclcpp::Node::make_shared("add_three_ints_client");
         auto client =
           node->create_client<tutorial_interfaces::srv::AddThreeInts>("add_three_ints");

         auto request =
           std::make_shared<tutorial_interfaces::srv::AddThreeInts::Request>();
         request->a = std::atoll(argv[1]);
         request->b = std::atoll(argv[2]);
         request->c = std::atoll(argv[3]);

         while (!client->wait_for_service(1s)) {
           if (!rclcpp::ok()) {
             RCLCPP_ERROR(rclcpp::get_logger("rclcpp"),
               "Interrupted while waiting for the service. Exiting.");
             return 0;
           }
           RCLCPP_INFO(rclcpp::get_logger("rclcpp"),
             "Service not available, waiting again...");
         }

         auto result = client->async_send_request(request);
         if (rclcpp::spin_until_future_complete(node, result) ==
           rclcpp::FutureReturnCode::SUCCESS)
         {
           RCLCPP_INFO(rclcpp::get_logger("rclcpp"),
             "Sum: %ld", result.get()->sum);
         } else {
           RCLCPP_ERROR(rclcpp::get_logger("rclcpp"),
             "Failed to call service add_three_ints");
         }

         rclcpp::shutdown();
         return 0;
       }

  .. group-tab:: Python

    .. code-block:: python

       from tutorial_interfaces.srv import AddThreeInts
       import sys
       import rclpy
       from rclpy.node import Node


       class MinimalClientAsync(Node):

           def __init__(self):
               super().__init__('minimal_client_async')
               self.cli = self.create_client(AddThreeInts, 'add_three_ints')
               while not self.cli.wait_for_service(timeout_sec=1.0):
                   self.get_logger().info('service not available, waiting again...')
               self.req = AddThreeInts.Request()

           def send_request(self):
               self.req.a = int(sys.argv[1])
               self.req.b = int(sys.argv[2])
               self.req.c = int(sys.argv[3])
               self.future = self.cli.call_async(self.req)


       def main(args=None):
           rclpy.init(args=args)
           minimal_client = MinimalClientAsync()
           minimal_client.send_request()

           while rclpy.ok():
               rclpy.spin_once(minimal_client)
               if minimal_client.future.done():
                   try:
                       response = minimal_client.future.result()
                   except Exception as e:
                       minimal_client.get_logger().info(
                           'Service call failed %r' % (e,))
                   else:
                       minimal_client.get_logger().info(
                           'Result of add_three_ints: %d + %d + %d = %d' %
                           (minimal_client.req.a, minimal_client.req.b,
                            minimal_client.req.c, response.sum))
                   break

           minimal_client.destroy_node()
           rclpy.shutdown()


       if __name__ == '__main__':
           main()

**CMakeLists.txt**

仅适用于 C++。添加接口依赖，并将其链接到服务端和客户端目标：

.. code-block:: cmake

   find_package(ament_cmake REQUIRED)
   find_package(rclcpp REQUIRED)
   find_package(tutorial_interfaces REQUIRED)

   add_executable(server src/add_two_ints_server.cpp)
   ament_target_dependencies(server rclcpp tutorial_interfaces)

   add_executable(client src/add_two_ints_client.cpp)
   ament_target_dependencies(client rclcpp tutorial_interfaces)

   install(TARGETS
     server
     client
     DESTINATION lib/${PROJECT_NAME})

   ament_package()

**package.xml**

.. tabs::

  .. group-tab:: C++

    .. code-block:: xml

       <depend>tutorial_interfaces</depend>

  .. group-tab:: Python

    .. code-block:: xml

       <exec_depend>tutorial_interfaces</exec_depend>

保存所有修改后，构建使用自定义接口的功能包：

.. tabs::

  .. group-tab:: C++

    Linux/macOS：

    .. code-block:: console

       $ colcon build --packages-select cpp_srvcli

    Windows：

    .. code-block:: console

       $ colcon build --merge-install --packages-select cpp_srvcli

  .. group-tab:: Python

    Linux/macOS：

    .. code-block:: console

       $ colcon build --packages-select py_srvcli

    Windows：

    .. code-block:: console

       $ colcon build --merge-install --packages-select py_srvcli

然后打开两个新终端，分别加载 ``ros2_ws`` 工作空间环境并运行：

.. tabs::

  .. group-tab:: C++

    .. code-block:: console

       $ ros2 run cpp_srvcli server

    .. code-block:: console

       $ ros2 run cpp_srvcli client 2 3 1

  .. group-tab:: Python

    .. code-block:: console

       $ ros2 run py_srvcli service

    .. code-block:: console

       $ ros2 run py_srvcli client 2 3 1

总结
----

本教程介绍了如何在独立功能包中创建自定义接口，并在其他功能包中使用这些接口。

本教程只介绍了自定义接口定义的一部分内容。更多信息请参阅 :doc:`ROS 2 接口概念 <../../Concepts/Basic/About-Interfaces>`。

下一步
------

下一篇教程 :doc:`单功能包中定义和使用接口 <./Single-Package-Define-And-Use-Interface>` 将介绍 ROS 2 中使用接口的其他方式。
