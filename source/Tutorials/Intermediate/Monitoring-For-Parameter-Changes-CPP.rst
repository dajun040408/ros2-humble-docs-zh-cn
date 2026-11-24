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

打开新终端并 :doc:`source ROS 2 安装环境 <../Beginner-CLI-Tools/Configuring-ROS2-Environment>`，以便使用 ``ros2`` 命令。

按照 :ref:`创建工作空间的说明 <new-directory>` 创建名为 ``ros2_ws`` 的工作空间。功能包应创建在 ``src`` 目录中，而不是工作空间根目录。

进入 ``ros2_ws/src`` 并创建新功能包：

.. code-block:: console

   $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_parameter_event_handler --dependencies rclcpp

终端会返回消息，确认功能包及其必要文件和目录已创建。``--dependencies`` 参数会自动在 ``package.xml`` 和 ``CMakeLists.txt`` 中添加依赖项。

1.1 更新 package.xml
~~~~~~~~~~~~~~~~~~~~~~

由于创建功能包时使用了 ``--dependencies`` 选项，因此无需手动添加依赖。不过，仍需填写功能包描述、维护者姓名和邮箱，以及许可证：

.. code-block:: xml

   <description>C++ parameter events client tutorial</description>
   <maintainer email="you@email.com">Your Name</maintainer>
   <license>Apache License 2.0</license>

2. 编写 C++ 节点
^^^^^^^^^^^^^^^^

在 ``ros2_ws/src/cpp_parameter_event_handler/src`` 目录中创建 ``parameter_event_handler.cpp``，并写入以下代码：

.. code-block:: cpp

   #include <memory>

   #include "rclcpp/rclcpp.hpp"

   class SampleNodeWithParameters : public rclcpp::Node
   {
   public:
     SampleNodeWithParameters()
     : Node("node_with_parameters")
     {
       this->declare_parameter("an_int_param", 0);

       // 创建参数事件订阅器，用于监控本节点和其他节点的参数变化
       param_subscriber_ =
         std::make_shared<rclcpp::ParameterEventHandler>(this);

       // 为本节点的整数参数 an_int_param 设置回调
       auto cb = [this](const rclcpp::Parameter & p) {
           RCLCPP_INFO(
             this->get_logger(),
             "cb: Received an update to parameter \"%s\" of type %s: \"%ld\"",
             p.get_name().c_str(),
             p.get_type_name().c_str(),
             p.as_int());
         };
       cb_handle_ = param_subscriber_->add_parameter_callback("an_int_param", cb);
     }

   private:
     std::shared_ptr<rclcpp::ParameterEventHandler> param_subscriber_;
     std::shared_ptr<rclcpp::ParameterCallbackHandle> cb_handle_;
   };

   int main(int argc, char ** argv)
   {
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<SampleNodeWithParameters>());
     rclcpp::shutdown();

     return 0;
   }

2.1 理解代码
~~~~~~~~~~~~

首先包含 ``<memory>``，以便使用 ``std::make_shared`` 模板。接下来包含 ``rclcpp/rclcpp.hpp``，以使用 rclcpp 接口提供的功能，包括 ``ParameterEventHandler`` 类。

.. include:: ../../_internal/Rclcpp-Convenience-Header-Note.rst

随后定义 ``SampleNodeWithParameters`` 类。构造函数首先声明一个名为 ``an_int_param`` 的整数参数，默认值为 0。

接下来创建 ``ParameterEventHandler``，用于监控参数变化。最后创建一个 lambda 回调函数，并将其注册为 ``an_int_param`` 参数变化时执行的回调：

.. code-block:: cpp

   SampleNodeWithParameters()
   : Node("node_with_parameters")
   {
     this->declare_parameter("an_int_param", 0);

     // 创建参数事件订阅器
     param_subscriber_ = std::make_shared<rclcpp::ParameterEventHandler>(this);

     // 为本节点的整数参数 an_int_param 设置回调
     auto cb = [this](const rclcpp::Parameter & p) {
         RCLCPP_INFO(
           this->get_logger(),
           "cb: Received an update to parameter \"%s\" of type %s: \"%ld\"",
           p.get_name().c_str(),
           p.get_type_name().c_str(),
           p.as_int());
       };
     cb_handle_ = param_subscriber_->add_parameter_callback("an_int_param", cb);
   }

.. note::

   非常重要的一点是：必须保存 ``add_parameter_callback()`` 返回的回调句柄。否则，回调将无法正确注册并保持有效。

``SampleNodeWithParameters`` 类之后是常规的 ``main`` 函数：初始化 ROS 2，启动示例节点并处理回调，最后关闭 ROS 2。

.. code-block:: cpp

   int main(int argc, char ** argv)
   {
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<SampleNodeWithParameters>());
     rclcpp::shutdown();

     return 0;
   }

2.2 添加可执行程序
~~~~~~~~~~~~~~~~~~

打开 ``CMakeLists.txt``，在 ``find_package(rclcpp REQUIRED)`` 之后添加：

.. code-block:: cmake

   add_executable(parameter_event_handler src/parameter_event_handler.cpp)
   ament_target_dependencies(parameter_event_handler rclcpp)

   install(TARGETS
     parameter_event_handler
     DESTINATION lib/${PROJECT_NAME}
   )

3. 构建和运行
^^^^^^^^^^^^^

构建之前，建议在工作空间根目录 ``ros2_ws`` 中运行 ``rosdep``，检查是否缺少依赖：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y

  .. group-tab:: macOS

    ``rosdep`` 仅在 Linux 上运行，可以跳过此步骤。

  .. group-tab:: Windows

    ``rosdep`` 仅在 Linux 上运行，可以跳过此步骤。

返回工作空间根目录并构建新功能包：

.. code-block:: console

   $ colcon build --packages-select cpp_parameter_event_handler

打开新终端，进入 ``ros2_ws`` 并加载设置文件：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ . install/setup.bash

  .. group-tab:: macOS

    .. code-block:: console

       $ . install/setup.bash

  .. group-tab:: Windows

    .. code-block:: console

       $ call install/setup.bat

现在运行节点：

.. code-block:: console

   $ ros2 run cpp_parameter_event_handler parameter_event_handler

节点启动后会等待参数变化。打开另一个终端，source ROS 2 环境并执行：

.. code-block:: console

   $ ros2 param set node_with_parameters an_int_param 43

运行节点的终端会显示类似以下消息：

.. code-block:: console

   [INFO] [node_with_parameters]: cb: Received an update to parameter "an_int_param" of type integer: "43"

这说明之前注册的回调已经被调用，并输出了更新后的参数值。可以在运行节点的终端中按 ``Ctrl+C`` 结束程序。

扩展
----

到目前为止，已经创建并测试了一个监控本节点单个参数的程序。下面介绍 ``ParameterEventHandler`` 的另外两种使用方式。

监控其他节点的参数变化
^^^^^^^^^^^^^^^^^^^^^^

``ParameterEventHandler`` 也可以监控其他节点的参数变化。下面使用 ``parameter_blackboard`` 示例节点提供一个 double 参数，并监控该参数的更新。

首先，在 ``SampleNodeWithParameters`` 构造函数现有代码后面添加：

.. code-block:: cpp

   // 监控远程节点的参数变化。这里需要指定远程节点名称。
   auto cb2 = [this](const rclcpp::Parameter & p) {
       RCLCPP_INFO(
         this->get_logger(),
         "cb2: Received an update to parameter \"%s\" of type: %s: \"%.02lf\"",
         p.get_name().c_str(),
         p.get_type_name().c_str(),
         p.as_double());
     };

   auto remote_node_name = std::string("parameter_blackboard");
   auto remote_param_name = std::string("a_double_param");
   cb_handle2_ = param_subscriber_->add_parameter_callback(
     remote_param_name, cb2, remote_node_name);

然后增加第二个回调句柄成员变量 ``cb_handle2_``：

.. code-block:: cpp

   private:
     std::shared_ptr<rclcpp::ParameterEventHandler> param_subscriber_;
     std::shared_ptr<rclcpp::ParameterCallbackHandle> cb_handle_;
     std::shared_ptr<rclcpp::ParameterCallbackHandle> cb_handle2_;

回到工作空间根目录，重新构建功能包：

.. code-block:: console

   $ colcon build --packages-select cpp_parameter_event_handler

然后重新 source 工作空间环境，并运行 ``parameter_event_handler``：

.. code-block:: console

   $ ros2 run cpp_parameter_event_handler parameter_event_handler

接下来，在另一个已经 source ROS 2 环境的终端中运行 ``parameter_blackboard`` 示例节点：

.. code-block:: console

   $ ros2 run demo_nodes_cpp parameter_blackboard

最后，在第三个终端中设置 ``parameter_blackboard`` 节点的参数：

.. code-block:: console

   $ ros2 param set parameter_blackboard a_double_param 3.45

执行该命令后，``parameter_event_handler`` 终端应显示回调被调用的日志，内容类似：

.. code-block:: console

   [INFO] [node_with_parameters]: cb2: Received an update to parameter "a_double_param" of type: double: "3.45"

同时监控所有节点的参数变化
^^^^^^^^^^^^^^^^^^^^^^^^^^

如果需要同时监控多个节点或多个参数，逐个调用 ``add_parameter_callback`` 会比较繁琐。

此时可以使用 ``add_parameter_event_callback`` 注册一个统一回调。只要任意节点的任意参数发生变化，该回调就会被触发。

首先，在 ``SampleNodeWithParameters`` 构造函数中声明另一个 double 参数，并注册事件回调：

.. code-block:: cpp

   this->declare_parameter("another_double_param", 0.0);

   auto event_cb = [this](
     const rcl_interfaces::msg::ParameterEvent & parameter_event) {
       RCLCPP_INFO(
         this->get_logger(),
         "Received parameter event from node \"%s\"",
         parameter_event.node.c_str());

       for (const auto & p : parameter_event.changed_parameters) {
         RCLCPP_INFO(
           this->get_logger(),
           "Inside event: \"%s\" changed to %s",
           p.name.c_str(),
           rclcpp::Parameter::from_parameter_msg(p).value_to_string().c_str());
       }
     };

   event_cb_handle_ = param_subscriber_->add_parameter_event_callback(event_cb);

这里声明了新的 double 参数 ``another_double_param``，并添加一个事件回调来监控两个参数。注意，``parameter_event`` 的类型是 ``rcl_interfaces/msg/ParameterEvent``。虽然本教程没有演示，但事件回调也可以用于监控参数的新增和删除。

最后，将事件回调句柄添加为私有成员：

.. code-block:: cpp

   private:
     // ...
     std::shared_ptr<rclcpp::ParameterEventCallbackHandle> event_cb_handle_;

回到工作空间根目录，重新构建功能包：

.. code-block:: console

   $ colcon build --packages-select cpp_parameter_event_handler

重新 source 工作空间环境，然后运行节点：

.. code-block:: console

   $ ros2 run cpp_parameter_event_handler parameter_event_handler

在另一个已经 source ROS 2 环境的终端中，修改原来的整数参数：

.. code-block:: console

   $ ros2 param set node_with_parameters an_int_param 44

此时应该同时看到单参数回调和事件回调被触发：

.. code-block:: console

   [INFO] [node_with_parameters]: cb: Received an update to parameter "an_int_param" of type integer: "44"
   [INFO] [node_with_parameters]: Received parameter event from node "/node_with_parameters"
   [INFO] [node_with_parameters]: Inside event: "an_int_param" changed to 44

再设置新的 double 参数：

.. code-block:: console

   $ ros2 param set node_with_parameters another_double_param 4.4

由于没有通过 ``add_parameter_callback`` 为该 double 参数单独注册回调，因此这里只会触发事件回调：

.. code-block:: console

   [INFO] [node_with_parameters]: Received parameter event from node "/node_with_parameters"
   [INFO] [node_with_parameters]: Inside event: "another_double_param" changed to 4.400000

.. note::

   一次设置多个参数时，建议使用 ``set_parameters_atomically``，详情请参阅 :doc:`ROS 2 参数概念 <../../Concepts/Basic/About-Parameters>`。这样事件回调只会触发一次。

总结
----

本教程创建了一个包含参数的节点，并使用 ``ParameterEventHandler`` 注册回调来监控该参数的变化。

还使用同一个类监控了远程节点的参数，以及通过单个事件回调监控所有参数。``ParameterEventHandler`` 为参数变化监控提供了方便的方式，使程序能够根据更新后的参数值作出响应。

相关内容
--------

如果希望了解如何将 ROS 1 参数文件迁移到 ROS 2，请参阅 :doc:`将 ROS 1 YAML 参数文件迁移到 ROS 2 <../../How-To-Guides/Migrating-from-ROS1/Migrating-Parameters>` 教程。
