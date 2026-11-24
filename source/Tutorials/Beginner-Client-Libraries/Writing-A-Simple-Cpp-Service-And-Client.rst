.. redirect-from::

    Tutorials/Writing-A-Simple-Cpp-Service-And-Client

.. _CppSrvCli:

编写简单的服务和客户端（C++）
=============================

**目标：** 使用 C++ 创建并运行服务端和客户端节点。

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

  $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_srvcli --dependencies rclcpp example_interfaces

--dependencies 参数会自动在 package.xml 和 CMakeLists.txt 中添加必要依赖。example_interfaces 软件包包含本教程使用的 AddTwoInts.srv：

.. code-block:: text

    int64 a
    int64 b
    ---
    int64 sum

横线之前的两行是请求参数，横线之后是响应内容。

在 package.xml 中填写描述、维护者信息和许可证：

.. code-block:: xml

  <description>C++ client server tutorial</description>
  <maintainer email="you@email.com">Your Name</maintainer>
  <license>Apache License 2.0</license>

2. 编写服务端节点
^^^^^^^^^^^^^^^^^

在 ros2_ws/src/cpp_srvcli/src 目录中创建 add_two_ints_server.cpp：

.. code-block:: cpp

    #include "rclcpp/rclcpp.hpp"
    #include "example_interfaces/srv/add_two_ints.hpp"
    #include <memory>

    void add(
      const std::shared_ptr<example_interfaces::srv::AddTwoInts::Request> request,
      std::shared_ptr<example_interfaces::srv::AddTwoInts::Response> response)
    {
      response->sum = request->a + request->b;
      RCLCPP_INFO(rclcpp::get_logger("rclcpp"),
        "Incoming request: a=%ld b=%ld", request->a, request->b);
      RCLCPP_INFO(rclcpp::get_logger("rclcpp"),
        "Sending back response: [%ld]", response->sum);
    }

    int main(int argc, char ** argv)
    {
      rclcpp::init(argc, argv);
      auto node = rclcpp::Node::make_shared("minimal_service");
      auto service = node->create_service<example_interfaces::srv::AddTwoInts>(
        "add_two_ints", &add);
      RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Ready to add two ints.");
      rclcpp::spin(node);
      rclcpp::shutdown();
      return 0;
    }

3. 编写客户端节点
^^^^^^^^^^^^^^^^^

在同一目录中创建 add_two_ints_client.cpp。客户端通过 create_client() 创建服务客户端，构造请求并调用 async_send_request() 发送请求。

.. code-block:: cpp

    #include "rclcpp/rclcpp.hpp"
    #include "example_interfaces/srv/add_two_ints.hpp"
    #include <cstdlib>
    #include <memory>

    int main(int argc, char ** argv)
    {
      rclcpp::init(argc, argv);
      if (argc != 3) {
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"),
          "Usage: add_two_ints_client X Y");
        return 1;
      }

      auto node = rclcpp::Node::make_shared("minimal_client");
      auto client = node->create_client<example_interfaces::srv::AddTwoInts>(
        "add_two_ints");

      auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
      request->a = std::atoll(argv[1]);
      request->b = std::atoll(argv[2]);

      while (!client->wait_for_service(std::chrono::seconds(1))) {
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
          "Failed to call service add_two_ints");
      }

      rclcpp::shutdown();
      return 0;
    }

4. 配置并构建
^^^^^^^^^^^^^

在 CMakeLists.txt 中查找依赖并添加两个可执行程序：

.. code-block:: cmake

   find_package(rclcpp REQUIRED)
   find_package(example_interfaces REQUIRED)

   add_executable(server src/add_two_ints_server.cpp)
   ament_target_dependencies(server rclcpp example_interfaces)

   add_executable(client src/add_two_ints_client.cpp)
   ament_target_dependencies(client rclcpp example_interfaces)

   install(TARGETS server client DESTINATION lib/cpp_srvcli)

在工作空间根目录构建：

.. code-block:: console

   $ colcon build --packages-select cpp_srvcli

5. 运行服务和客户端
^^^^^^^^^^^^^^^^^^^

打开一个终端，source 工作空间并启动服务端：

.. code-block:: console

   $ ros2 run cpp_srvcli server

打开另一个终端并运行客户端，传入两个整数：

.. code-block:: console

   $ ros2 run cpp_srvcli client 2 3

客户端会收到并输出两个整数的和。

总结
----

你已经创建并运行了一个 C++ 服务端和客户端。客户端发送两个整数，服务端计算并返回它们的和。
