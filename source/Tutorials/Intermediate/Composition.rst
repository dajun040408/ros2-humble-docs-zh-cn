.. redirect-from::

    Tutorials/Composition

节点组合
========

**目标：** 学习如何将多个 ROS 2 节点加载到同一进程中运行。

**教程级别：** 中级

.. contents:: 目录
   :depth: 2
   :local:

背景
----

ROS 2 支持将多个节点组合到一个进程中运行。与每个节点单独运行在独立进程的方式相比，节点组合可以减少进程数量，并在适当配置时使用进程内通信，降低消息传输开销。

组件
----

可组合节点通常实现为共享库，并通过 ``rclcpp_components`` 注册。组件类通常继承自 ``rclcpp::Node``，构造函数接受 ``rclcpp::NodeOptions``：

.. code-block:: cpp

   class Talker : public rclcpp::Node
   {
   public:
     explicit Talker(const rclcpp::NodeOptions & options)
     : Node("talker", options)
     {
       // 初始化发布者、订阅者和定时器
     }
   };

通过注册宏导出组件：

.. code-block:: cpp

   #include <rclcpp_components/register_node_macro.hpp>
   RCLCPP_COMPONENTS_REGISTER_NODE(Talker)

构建组件
--------

在 ``CMakeLists.txt`` 中查找组件依赖，将源文件编译为共享库，并注册节点：

.. code-block:: cmake

   find_package(rclcpp_components REQUIRED)
   add_library(talker_component SHARED src/talker.cpp)
   ament_target_dependencies(talker_component rclcpp rclcpp_components)
   rclcpp_components_register_nodes(talker_component "Talker")

运行组件
--------

ROS 2 提供组件容器可执行程序。可以通过命令行将组件加载到容器：

.. code-block:: console

   $ ros2 run rclcpp_components component_container

另一个终端中使用组件加载命令，将组件加入容器。也可以在 launch 文件中使用 ``ComposableNodeContainer`` 和 ``ComposableNode`` 描述容器及其组件。

进程内通信
----------

如果组件在同一进程中运行，可以通过 ``use_intra_process_comms`` 参数启用进程内通信：

.. code-block:: python

   ComposableNode(
       package='composition',
       plugin='composition::Talker',
       name='talker',
       extra_arguments=[{'use_intra_process_comms': True}],
   )

选择容器
--------

* ``component_container``：单线程执行器容器。
* ``component_container_mt``：多线程执行器容器。

如果组件需要多线程回调调度，应选择多线程容器，并合理配置回调组和线程安全机制。

总结
----

节点组合允许多个 ROS 2 组件共享一个进程。通过共享库、组件注册宏、组件容器和 launch 描述，可以在运行时动态加载和管理节点，并按需启用进程内通信。
