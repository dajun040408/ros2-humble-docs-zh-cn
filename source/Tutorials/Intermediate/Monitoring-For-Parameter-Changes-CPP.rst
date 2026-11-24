.. redirect-from::

    Tutorials/Monitoring-For-Parameter-Changes-CPP

监控参数变化（C++）
===================

**目标：** 学习使用 ``ParameterEventHandler`` 类监控并响应参数变化。

**教程级别：** 中级 | **预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

节点通常需要响应自身参数或其他节点参数的变化。``ParameterEventHandler`` 类可以方便地监听参数变化，并让代码作出响应。本教程介绍如何使用 C++ 版本的 ``ParameterEventHandler`` 监控本节点和其他节点的参数。

前置条件
--------

建议先完成：

* :doc:`理解 ROS 2 参数 <../Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters>`
* :doc:`在类中使用参数（C++） <../Beginner-Client-Libraries/Using-Parameters-In-A-Class-CPP>`

本教程的原始最低平台要求为 Galactic。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

打开新终端并 source ROS 2 环境。创建工作空间 ``ros2_ws``，然后进入 ``src`` 创建功能包：

.. code-block:: console

   $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_parameter_event_handler --dependencies rclcpp

``--dependencies`` 参数会自动在 ``package.xml`` 和 ``CMakeLists.txt`` 中添加必要依赖。仍需在 ``package.xml`` 中填写描述、维护者姓名和邮箱，以及许可证：

.. code-block:: xml

   <description>C++ parameter events client tutorial</description>
   <maintainer email="you@email.com">Your Name</maintainer>
   <license>Apache License 2.0</license>

2. 编写 C++ 节点
^^^^^^^^^^^^^^^^

在 ``ros2_ws/src/cpp_parameter_event_handler/src`` 中创建 ``parameter_event_handler.cpp``。节点首先声明参数，然后创建参数事件处理器：

.. code-block:: cpp

   class SampleNodeWithParameters : public rclcpp::Node
   {
   public:
     SampleNodeWithParameters()
     : Node("node_with_parameters")
     {
       this->declare_parameter("an_int_param", 0);
       param_subscriber_ =
         std::make_shared<rclcpp::ParameterEventHandler>(this);
     }

   private:
     std::shared_ptr<rclcpp::ParameterEventHandler> param_subscriber_;
   };

``ParameterEventHandler`` 可以监听本节点或其他节点的参数事件。通过注册参数回调，可以在指定参数变化时执行自定义逻辑。回调句柄应保存在节点成员变量中，避免其生命周期提前结束。

监控本节点参数
--------------

为本节点的参数注册回调。当参数值被修改时，回调会收到参数信息，可以读取参数名称和值并执行相应操作。

监控其他节点参数
----------------

``ParameterEventHandler`` 也可以监听其他节点的参数变化。注册回调时指定目标节点名称和参数名称，即可监控远程节点的指定参数。

3. 构建和运行
^^^^^^^^^^^^^

在 ``CMakeLists.txt`` 中添加可执行程序并安装，然后构建功能包：

.. code-block:: console

   $ colcon build --packages-select cpp_parameter_event_handler

source 工作空间后运行节点。可使用 ``ros2 param set`` 修改参数，观察注册的回调是否收到参数事件。

总结
----

本教程介绍了如何使用 ``rclcpp::ParameterEventHandler`` 监听本节点或其他节点的参数变化，并在参数更新时执行回调。
