.. redirect-from::

    Tutorials/Actions/Writing-a-Cpp-Action-Server-Client

.. _ActionsCpp:

编写 Action 服务端和客户端（C++）
==================================

**目标：** 使用 C++ 实现 Action 服务端和客户端。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

Action 是 ROS 2 中的一种异步通信方式。Action 客户端向 Action 服务端发送目标请求；Action 服务端向客户端发送目标执行反馈和最终结果。

前置条件
--------

需要先完成 :doc:`创建 Action 接口 <../Creating-an-Action>` 教程，并准备 ``action_tutorials_interfaces`` 功能包及其中定义的 ``Fibonacci.action``。

任务
----

1. 创建 action_tutorials_cpp 功能包
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

进入上一个教程创建的工作空间（记得先 source 工作空间），创建 C++ Action 功能包：

.. code-block:: console

   $ cd ~/ros2_ws/src
   $ ros2 pkg create --dependencies action_tutorials_interfaces rclcpp rclcpp_action rclcpp_components -- action_tutorials_cpp

Windows 示例：

.. code-block:: console

   $ cd \dev\ros2_ws\src
   $ ros2 pkg create --dependencies action_tutorials_interfaces rclcpp rclcpp_action rclcpp_components -- action_tutorials_cpp

1.1 添加符号可见性控制
~~~~~~~~~~~~~~~~~~~~~~

为了使功能包能够在 Windows 上编译和运行，需要添加符号可见性控制。详细说明请参阅 :ref:`Windows 符号可见性 <Windows_Symbol_Visibility>`。

打开 ``action_tutorials_cpp/include/action_tutorials_cpp/visibility_control.h``，写入以下代码：

.. code-block:: c++

   #ifndef ACTION_TUTORIALS_CPP__VISIBILITY_CONTROL_H_
   #define ACTION_TUTORIALS_CPP__VISIBILITY_CONTROL_H_

   #ifdef __cplusplus
   extern "C"
   {
   #endif

   #if defined _WIN32 || defined __CYGWIN__
     #ifdef __GNUC__
       #define ACTION_TUTORIALS_CPP_EXPORT __attribute__ ((dllexport))
       #define ACTION_TUTORIALS_CPP_IMPORT __attribute__ ((dllimport))
     #else
       #define ACTION_TUTORIALS_CPP_EXPORT __declspec(dllexport)
       #define ACTION_TUTORIALS_CPP_IMPORT __declspec(dllimport)
     #endif
     #ifdef ACTION_TUTORIALS_CPP_BUILDING_DLL
       #define ACTION_TUTORIALS_CPP_PUBLIC ACTION_TUTORIALS_CPP_EXPORT
     #else
       #define ACTION_TUTORIALS_CPP_PUBLIC ACTION_TUTORIALS_CPP_IMPORT
     #endif
     #define ACTION_TUTORIALS_CPP_PUBLIC_TYPE ACTION_TUTORIALS_CPP_PUBLIC
     #define ACTION_TUTORIALS_CPP_LOCAL
   #else
     #define ACTION_TUTORIALS_CPP_EXPORT __attribute__ ((visibility("default")))
     #define ACTION_TUTORIALS_CPP_IMPORT
     #if __GNUC__ >= 4
       #define ACTION_TUTORIALS_CPP_PUBLIC __attribute__ ((visibility("default")))
       #define ACTION_TUTORIALS_CPP_LOCAL __attribute__ ((visibility("hidden")))
     #else
       #define ACTION_TUTORIALS_CPP_PUBLIC
       #define ACTION_TUTORIALS_CPP_LOCAL
     #endif
     #define ACTION_TUTORIALS_CPP_PUBLIC_TYPE
   #endif

   #ifdef __cplusplus
   }
   #endif

   #endif  // ACTION_TUTORIALS_CPP__VISIBILITY_CONTROL_H_

2. 编写 Action 服务端
^^^^^^^^^^^^^^^^^^^^^

本节实现一个使用前面创建的 Fibonacci Action 接口计算斐波那契数列的服务端。

2.1 编写服务端代码
~~~~~~~~~~~~~~~~~

打开 ``action_tutorials_cpp/src/fibonacci_action_server.cpp``，写入以下代码：

.. literalinclude:: scripts/server.cpp
   :language: c++

文件开头包含编译所需的头文件：

.. include:: ../../../_internal/Rclcpp-Convenience-Header-Note.rst

接下来创建一个继承自 ``rclcpp::Node`` 的类：

.. code-block:: c++

   class FibonacciActionServer : public rclcpp::Node

``FibonacciActionServer`` 构造函数将节点名称初始化为 ``fibonacci_action_server``。构造函数还会创建一个新的 Action 服务端：

.. code-block:: c++

   this->action_server_ = rclcpp_action::create_server<Fibonacci>(
     this,
     "fibonacci",
     std::bind(&FibonacciActionServer::handle_goal, this, _1, _2),
     std::bind(&FibonacciActionServer::handle_cancel, this, _1),
     std::bind(&FibonacciActionServer::handle_accepted, this, _1));

创建 Action 服务端需要提供以下内容：

1. 模板 Action 类型：``Fibonacci``。
2. 要添加 Action 的 ROS 2 节点：``this``。
3. Action 名称：``fibonacci``。
4. 处理目标请求的回调函数：``handle_goal``。
5. 处理取消请求的回调函数：``handle_cancel``。
6. 处理目标接受事件的回调函数：``handle_accepted``。

接下来实现这些回调函数。所有回调都应尽快返回，否则可能导致执行器中的其他回调得不到调度。

首先是处理新目标请求的回调：

.. literalinclude:: scripts/server.cpp
   :language: c++
   :lines: 37-44

这个实现会接受所有目标请求。

接下来是处理取消请求的回调：

.. literalinclude:: scripts/server.cpp
   :language: c++
   :lines: 46-52

这个实现会告知客户端，服务端接受了取消请求。

最后一个回调负责接受新目标并开始执行：

.. literalinclude:: scripts/server.cpp
   :language: c++
   :lines: 54-59

由于目标执行是一个耗时较长的操作，因此这里会创建一个新线程执行实际任务，然后尽快从 ``handle_accepted`` 返回，避免阻塞执行器。

后续的处理和状态更新都在新线程中的 ``execute`` 方法里完成：

.. literalinclude:: scripts/server.cpp
   :language: c++
   :lines: 61-95

该工作线程每秒计算一个斐波那契数列元素，并在每一步发布反馈。当计算完成后，服务端将目标标记为成功并退出执行线程。

至此，Action 服务端代码已经完成。接下来配置构建并运行。

2.2 编译 Action 服务端
~~~~~~~~~~~~~~~~~~~~~

将服务端代码加入项目后，还需要配置 ``CMakeLists.txt``，使其参与编译。

打开 ``action_tutorials_cpp/CMakeLists.txt``，在各个 ``find_package`` 调用之后添加：

.. code-block:: cmake

   add_library(action_server SHARED
     src/fibonacci_action_server.cpp)
   target_include_directories(action_server PRIVATE
     $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
     $<INSTALL_INTERFACE:include>)
   target_compile_definitions(action_server
     PRIVATE "ACTION_TUTORIALS_CPP_BUILDING_DLL")
   ament_target_dependencies(action_server
     "action_tutorials_interfaces"
     "rclcpp"
     "rclcpp_action"
     "rclcpp_components")
   rclcpp_components_register_node(
     action_server
     PLUGIN "action_tutorials_cpp::FibonacciActionServer"
     EXECUTABLE fibonacci_action_server)
   install(TARGETS
     action_server
     ARCHIVE DESTINATION lib
     LIBRARY DESTINATION lib
     RUNTIME DESTINATION bin)

现在可以编译功能包。进入 ``ros2_ws`` 工作空间根目录并运行：

.. code-block:: console

   $ colcon build

该命令会构建整个工作空间，其中包括 ``action_tutorials_cpp`` 功能包中的 ``fibonacci_action_server``。

2.3 运行 Action 服务端
~~~~~~~~~~~~~~~~~~~~

服务端构建完成后，source 刚刚构建的 ``ros2_ws`` 工作空间，并运行：

.. code-block:: console

   $ ros2 run action_tutorials_cpp fibonacci_action_server

3. 编写 Action 客户端
^^^^^^^^^^^^^^^^^^^^^

3.1 编写客户端代码
~~~~~~~~~~~~~~~~~

打开 ``action_tutorials_cpp/src/fibonacci_action_client.cpp``，写入以下代码：

.. literalinclude:: scripts/client.cpp
   :language: c++

文件开头包含编译所需的头文件。

接下来创建一个继承自 ``rclcpp::Node`` 的类：

.. code-block:: c++

   class FibonacciActionClient : public rclcpp::Node

``FibonacciActionClient`` 构造函数将节点名称初始化为 ``fibonacci_action_client``，并创建一个新的 Action 客户端：

.. code-block:: c++

   this->client_ptr_ = rclcpp_action::create_client<Fibonacci>(
     this,
     "fibonacci");

创建 Action 客户端需要提供三个内容：

1. 模板 Action 类型：``Fibonacci``。
2. 要添加 Action 客户端的 ROS 2 节点：``this``。
3. Action 名称：``fibonacci``。

构造函数还会创建一个 ROS 定时器，用于触发唯一一次 ``send_goal`` 调用：

.. code-block:: c++

   this->timer_ = this->create_wall_timer(
     std::chrono::milliseconds(500),
     std::bind(&FibonacciActionClient::send_goal, this));

定时器到期后会调用 ``send_goal``：

.. literalinclude:: scripts/client.cpp
   :language: c++
   :lines: 32-57

该函数依次完成以下工作：

1. 取消定时器，确保该函数只执行一次。
2. 等待 Action 服务端启动并可用。
3. 创建一个新的 ``Fibonacci::Goal`` 目标对象。
4. 设置目标响应、反馈和结果回调函数。
5. 将目标发送给服务端。

服务端接收并接受目标后，会向客户端发送响应。该响应由 ``goal_response_callback`` 处理：

.. literalinclude:: scripts/client.cpp
   :language: c++
   :lines: 62-71

如果服务端接受了目标，就会开始执行。客户端收到的反馈由 ``feedback_callback`` 处理：

.. literalinclude:: scripts/client.cpp
   :language: c++
   :lines: 72-83

服务端完成处理后，会向客户端返回结果。结果由 ``result_callback`` 处理：

.. literalinclude:: scripts/client.cpp
   :language: c++
   :lines: 84-107

至此，Action 客户端代码已经完成。接下来配置构建并运行。

3.2 编译 Action 客户端
~~~~~~~~~~~~~~~~~~~~~

打开 ``action_tutorials_cpp/CMakeLists.txt``，在各个 ``find_package`` 调用之后添加：

.. code-block:: cmake

   add_library(action_client SHARED
     src/fibonacci_action_client.cpp)
   target_include_directories(action_client PRIVATE
     $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
     $<INSTALL_INTERFACE:include>)
   target_compile_definitions(action_client
     PRIVATE "ACTION_TUTORIALS_CPP_BUILDING_DLL")
   ament_target_dependencies(action_client
     "action_tutorials_interfaces"
     "rclcpp"
     "rclcpp_action"
     "rclcpp_components")
   rclcpp_components_register_node(
     action_client
     PLUGIN "action_tutorials_cpp::FibonacciActionClient"
     EXECUTABLE fibonacci_action_client)
   install(TARGETS
     action_client
     ARCHIVE DESTINATION lib
     LIBRARY DESTINATION lib
     RUNTIME DESTINATION bin)

然后进入 ``ros2_ws`` 工作空间根目录并编译：

.. code-block:: console

   $ colcon build

该命令会构建整个工作空间，其中包括 ``action_tutorials_cpp`` 功能包中的 ``fibonacci_action_client``。

3.3 运行 Action 客户端
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

确保另一个终端中已经运行 Action 服务端。然后 source 刚刚构建的 ``ros2_ws`` 工作空间，并运行客户端：

.. code-block:: console

   $ ros2 run action_tutorials_cpp fibonacci_action_client

你应该能看到目标被接受、反馈不断输出，以及最终结果返回的日志。

总结
----

本教程逐步实现了一个 C++ Action 服务端和客户端，并配置它们交换目标请求、反馈和最终结果。

相关内容
--------

C++ Action 服务端和客户端还有其他实现方式。可以查看 ``ros2/examples`` 仓库中的 ``minimal_action_server`` 和 ``minimal_action_client`` 功能包：`https://github.com/ros2/examples/tree/{REPOS_FILE_BRANCH}/rclcpp`_。

有关 ROS 2 Actions 的更多详细信息，请参阅 `ROS 2 Actions 设计文章 <http://design.ros2.org/articles/actions.html>`_。
