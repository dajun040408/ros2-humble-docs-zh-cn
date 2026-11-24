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

1.1 更新 package.xml
~~~~~~~~~~~~~~~~~~~~~~

由于创建功能包时已经使用了 ``--dependencies`` 选项，因此无需再手动向 ``package.xml`` 或 ``CMakeLists.txt`` 添加依赖项。

不过，仍需按照惯例在 ``package.xml`` 中填写功能包描述、维护者邮箱和姓名，以及许可证信息：

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

2.1 理解代码
~~~~~~~~~~~~~

最开始的两个 ``#include`` 语句引入了该功能包的依赖项。

``add`` 函数从请求中读取两个整数并计算它们的和，将结果写入响应，同时通过日志向控制台输出处理状态：

.. code-block:: cpp

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

``main`` 函数依次完成以下工作：

* 初始化 ROS 2 C++ 客户端库：

  .. code-block:: cpp

     rclcpp::init(argc, argv);

* 创建名为 ``minimal_service`` 的节点：

  .. code-block:: cpp

     auto node = rclcpp::Node::make_shared("minimal_service");

* 为该节点创建名为 ``add_two_ints`` 的服务，并将 ``add`` 函数注册为请求处理回调：

  .. code-block:: cpp

     auto service = node->create_service<example_interfaces::srv::AddTwoInts>(
       "add_two_ints", &add);

* 输出服务已经准备就绪的日志：

  .. code-block:: cpp

     RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Ready to add two ints.");

* 通过 spin 让节点持续运行，使服务保持可用：

  .. code-block:: cpp

     rclcpp::spin(node);

2.2 添加可执行程序
~~~~~~~~~~~~~~~~~~

``add_executable`` 宏会生成一个可通过 ``ros2 run`` 运行的可执行程序。在 ``CMakeLists.txt`` 的依赖项配置之后添加以下内容，创建名为 ``server`` 的可执行程序：

.. code-block:: cmake

   add_executable(server src/add_two_ints_server.cpp)
   ament_target_dependencies(server rclcpp example_interfaces)

为了让 ``ros2 run`` 能够找到该可执行程序，在文件末尾的 ``ament_package()`` 之前添加：

.. code-block:: cmake

   install(TARGETS
     server
     DESTINATION lib/${PROJECT_NAME})

现在可以构建功能包、加载本地环境并运行服务端。不过，为了观察完整的服务/客户端系统，先继续创建客户端节点。

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

3.1 理解代码
~~~~~~~~~~~~~

与服务端节点类似，下面的代码先创建节点，再为该节点创建客户端：

.. code-block:: cpp

   auto node = rclcpp::Node::make_shared("minimal_client");
   auto client = node->create_client<example_interfaces::srv::AddTwoInts>(
     "add_two_ints");

接下来创建请求对象。请求的数据结构由前面介绍的 ``.srv`` 文件定义：

.. code-block:: cpp

   auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
   request->a = std::atoll(argv[1]);
   request->b = std::atoll(argv[2]);

``while`` 循环每次等待 1 秒，尝试在网络中查找提供该服务的节点。如果没有找到，就继续等待。

.. code-block:: cpp

   RCLCPP_INFO(rclcpp::get_logger("rclcpp"),
     "Service not available, waiting again...");

如果客户端被取消（例如，你在终端中按下 ``Ctrl+C``），程序会输出错误日志，说明等待服务的过程被中断。

.. code-block:: cpp

   RCLCPP_ERROR(rclcpp::get_logger("rclcpp"),
     "Interrupted while waiting for the service. Exiting.");

找到服务后，客户端发送请求，并让节点持续运行，直到收到响应或调用失败。

3.2 添加可执行程序
~~~~~~~~~~~~~~~~~~

返回 ``CMakeLists.txt``，为新的客户端节点添加可执行程序和构建目标。删除自动生成文件中不必要的模板内容后，``CMakeLists.txt`` 可以整理为：

.. code-block:: cmake

   cmake_minimum_required(VERSION 3.5)
   project(cpp_srvcli)

   find_package(ament_cmake REQUIRED)
   find_package(rclcpp REQUIRED)
   find_package(example_interfaces REQUIRED)

   add_executable(server src/add_two_ints_server.cpp)
   ament_target_dependencies(server rclcpp example_interfaces)

   add_executable(client src/add_two_ints_client.cpp)
   ament_target_dependencies(client rclcpp example_interfaces)

   install(TARGETS
     server
     client
     DESTINATION lib/${PROJECT_NAME})

   ament_package()

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

你已经创建了两个节点，通过服务请求和响应数据。你还在功能包配置文件中添加了它们的依赖项和可执行程序，最终构建并运行了一个完整的服务/客户端系统。

下一步
------

在前面的几个教程中，你已经使用接口在话题和服务之间传递数据。接下来将学习如何 :doc:`创建自定义接口 <./Custom-ROS2-Interfaces>`。

相关内容
--------

C++ 服务端和客户端有多种实现方式。可以查看 ``ros2/examples`` 仓库中的 ``minimal_service`` 和 ``minimal_client`` 功能包：`https://github.com/ros2/examples/tree/{REPOS_FILE_BRANCH}/rclcpp/services`_。
