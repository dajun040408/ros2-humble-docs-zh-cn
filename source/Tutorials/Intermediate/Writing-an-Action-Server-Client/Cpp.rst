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

需要先完成 :doc:§创建 Action 接口 <../Creating-an-Action>§ 教程，并准备 §action_tutorials_interfaces§ 功能包及其中定义的 §Fibonacci.action§。

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

为了使功能包能够在 Windows 上编译和运行，需要添加符号可见性控制。详细说明请参阅 :ref:§Windows 符号可见性 <Windows_Symbol_Visibility>§。

在 §include/action_tutorials_cpp/visibility_control.h§ 中定义导入和导出宏，以便 Windows DLL 正确导出组件符号。

2. 编写 Action 服务端
^^^^^^^^^^^^^^^^^^^^^

服务端使用 §rclcpp_action::Server§ 创建 Action 服务。服务端需要提供目标请求处理、取消请求处理和目标接受后的执行回调。

执行回调负责计算 Fibonacci 数列，并通过反馈消息定期向客户端报告当前计算进度。目标完成后，将最终数列放入结果消息，并调用目标句柄的成功完成方法。

核心代码结构如下：

.. code-block:: cpp

   using Fibonacci = action_tutorials_interfaces::action::Fibonacci;

   class FibonacciActionServer : public rclcpp::Node
   {
   public:
     explicit FibonacciActionServer(
       const rclcpp::NodeOptions & options = rclcpp::NodeOptions())
     : Node("fibonacci_action_server", options)
     {
       using namespace std::placeholders;
       this->action_server_ = rclcpp_action::create_server<Fibonacci>(
         this,
         "fibonacci",
         std::bind(&FibonacciActionServer::handle_goal, this, _1, _2),
         std::bind(&FibonacciActionServer::handle_cancel, this, _1),
         std::bind(&FibonacciActionServer::handle_accepted, this, _1));
     }
   };

服务端创建时需要提供节点、Action 名称、目标请求回调、取消请求回调和目标接受回调。执行逻辑通常在接受回调中启动，并在计算过程中发布反馈。

3. 编写 Action 客户端
^^^^^^^^^^^^^^^^^^^^^

客户端使用 §rclcpp_action::Client§ 创建 Action 客户端，并向 §fibonacci§ Action 发送目标请求。客户端可以注册目标响应、反馈和最终结果回调。

发送目标前，可以等待服务端可用；目标发送后，客户端通过反馈回调接收中间结果，并在结果回调中处理成功、取消或中止状态。

4. 构建和运行
^^^^^^^^^^^^^

在工作空间根目录构建：

.. code-block:: console

   $ colcon build --packages-up-to action_tutorials_cpp

source 工作空间后，分别运行 Action 服务端和客户端。客户端发送 Fibonacci 目标后，服务端会计算数列并持续发布反馈，最后返回结果。

总结
----

本教程介绍了如何使用 §rclcpp_action§ 创建 C++ Action 服务端和客户端，包括目标请求、取消请求、反馈和最终结果处理。
