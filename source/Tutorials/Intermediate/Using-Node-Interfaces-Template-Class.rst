使用 Node 接口模板类（C++）
==============================

**目标：** 学习如何使用 ``rclcpp::NodeInterfaces<>`` 访问 ROS 2 节点信息。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

概述
----

并非所有 ROS 节点都具有相同的继承结构。``rclcpp::Node`` 和 ``rclcpp_lifecycle::LifecycleNode`` 并不属于同一个继承体系。因此，当开发者希望编写一个接收 ROS 节点指针作为参数的函数时，可能会遇到编译期类型问题。

为了解决这个问题，``rclcpp`` 提供了 ``rclcpp::NodeInterfaces<>`` 模板类型。无论传入的是普通节点还是生命周期节点，都可以使用该模板类型作为统一的接口约定。

``rclcpp::NodeInterfaces<>`` 提供了一种简洁、高效的方式来管理 ROS 2 节点接口，尤其适用于同时处理 ``rclcpp::Node`` 和 ``rclcpp_lifecycle::LifecycleNode`` 等不同类型节点的场景。

1. 使用 SharedPtr 访问节点信息
-----------------------------

下面的示例创建一个名为 ``Simple_Node`` 的普通节点，并定义 ``node_info`` 函数。该函数接收 ``Node::SharedPtr``，然后获取并输出节点名称。

.. code-block:: c++

   #include <memory>
   #include "rclcpp/rclcpp.hpp"

   void node_info(rclcpp::Node::SharedPtr node)
   {
     RCLCPP_INFO(node->get_logger(), "Node name: %s", node->get_name());
   }

   class SimpleNode : public rclcpp::Node
   {
   public:
     SimpleNode(const std::string & node_name)
     : Node(node_name)
     {
     }
   };

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     auto node = std::make_shared<SimpleNode>("Simple_Node");
     node_info(node);
   }

输出：

.. code-block:: console

   [INFO] [Simple_Node]: Node name: Simple_Node

.. include:: ../../_internal/Rclcpp-Convenience-Header-Note.rst

这种方式适用于参数类型为 ``rclcpp::Node`` 的情况，但不适用于 ``rclcpp_lifecycle::LifecycleNode`` 等其他节点类型。

2. 显式传递 rclcpp::node_interfaces
----------------------------------

一种更通用的方式是显式地将 ``rclcpp::node_interfaces`` 作为函数参数传入。这样就可以同时适用于不同类型的节点。

下面的示例定义 ``node_info`` 函数，并传入两个节点接口：``NodeBaseInterface`` 和 ``NodeLoggingInterface``。函数通过这两个接口获取并输出节点名称。

.. code-block:: c++

   void node_info(
     std::shared_ptr<rclcpp::node_interfaces::NodeBaseInterface> base_interface,
     std::shared_ptr<rclcpp::node_interfaces::NodeLoggingInterface> logging_interface)
   {
     RCLCPP_INFO(
       logging_interface->get_logger(),
       "Node name: %s",
       base_interface->get_name());
   }

创建一个普通节点和一个生命周期节点：

.. code-block:: c++

   class SimpleNode : public rclcpp::Node
   {
   public:
     SimpleNode(const std::string & node_name)
     : Node(node_name)
     {
     }
   };

   class LifecycleTalker : public rclcpp_lifecycle::LifecycleNode
   {
   public:
     explicit LifecycleTalker(
       const std::string & node_name,
       bool intra_process_comms = false)
     : rclcpp_lifecycle::LifecycleNode(
         node_name,
         rclcpp::NodeOptions().use_intra_process_comms(intra_process_comms))
     {}
   };

在 ``main`` 函数中创建这两种节点，并将它们对应的基础接口和日志接口传入 ``node_info``：

.. code-block:: c++

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::executors::SingleThreadedExecutor exe;

     auto node = std::make_shared<SimpleNode>("Simple_Node");
     auto lc_node = std::make_shared<LifecycleTalker>("Simple_LifeCycle_Node");

     node_info(node->get_node_base_interface(), node->get_node_logging_interface());
     node_info(lc_node->get_node_base_interface(), lc_node->get_node_logging_interface());
   }

输出：

.. code-block:: console

   [INFO] [Simple_Node]: Node name: Simple_Node
   [INFO] [Simple_LifeCycle_Node]: Node name: Simple_LifeCycle_Node

这种方式能够兼容不同节点类型。不过，随着函数功能变得复杂，需要传入的 ``rclcpp::node_interfaces`` 参数也会越来越多，影响代码的可读性和简洁性。

为了让代码更灵活，并兼容不同节点类型，可以使用 ``rclcpp::NodeInterfaces<>``。

3. 使用 rclcpp::NodeInterfaces<>
--------------------------------

推荐通过 Node Interfaces 访问节点信息。

与上一节类似，下面仍然创建一个 ``rclcpp_lifecycle::LifecycleNode`` 和一个 ``rclcpp::Node``。

.. code-block:: c++

   #include <memory>
   #include <string>
   #include <thread>

   #include "lifecycle_msgs/msg/transition.hpp"
   #include "rclcpp/rclcpp.hpp"
   #include "rclcpp_lifecycle/lifecycle_node.hpp"
   #include "rclcpp_lifecycle/lifecycle_publisher.hpp"
   #include "rclcpp/node_interfaces/node_interfaces.hpp"

   using MyNodeInterfaces =
     rclcpp::node_interfaces::NodeInterfaces<
       rclcpp::node_interfaces::NodeBaseInterface,
       rclcpp::node_interfaces::NodeLoggingInterface>;

   void node_info(MyNodeInterfaces interfaces)
   {
     auto base_interface = interfaces.get_node_base_interface();
     auto logging_interface = interfaces.get_node_logging_interface();

     RCLCPP_INFO(
       logging_interface->get_logger(),
       "Node name: %s",
       base_interface->get_name());
   }

   class SimpleNode : public rclcpp::Node
   {
   public:
     SimpleNode(const std::string & node_name)
     : Node(node_name)
     {
     }
   };

   class LifecycleTalker : public rclcpp_lifecycle::LifecycleNode
   {
   public:
     explicit LifecycleTalker(
       const std::string & node_name,
       bool intra_process_comms = false)
     : rclcpp_lifecycle::LifecycleNode(
         node_name,
         rclcpp::NodeOptions().use_intra_process_comms(intra_process_comms))
     {}
   };

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::executors::SingleThreadedExecutor exe;

     auto node = std::make_shared<SimpleNode>("Simple_Node");
     auto lc_node = std::make_shared<LifecycleTalker>("Simple_LifeCycle_Node");

     node_info(*node);
     node_info(*lc_node);
   }

输出：

.. code-block:: console

   [INFO] [Simple_Node]: Node name: Simple_Node
   [INFO] [Simple_LifeCycle_Node]: Node name: Simple_LifeCycle_Node

3.1 代码解析
~~~~~~~~~~~~

首先定义一个类型别名 ``MyNodeInterfaces``，它由两个节点接口组成：``NodeBaseInterface`` 和 ``NodeLoggingInterface``。

.. code-block:: c++

   using MyNodeInterfaces =
     rclcpp::node_interfaces::NodeInterfaces<
       rclcpp::node_interfaces::NodeBaseInterface,
       rclcpp::node_interfaces::NodeLoggingInterface>;

与接收 ``SharedPtr`` 或单独节点接口不同，``node_info`` 函数接收一个 ``rclcpp::node_interfaces::NodeInterfaces`` 对象的引用或实例。

这种方式的另一个优势是支持节点类对象的隐式转换。因此，可以将任何满足接口要求的 node-like 对象直接传递给接收 ``rclcpp::node_interfaces::NodeInterfaces`` 的函数。

函数从接口对象中提取：

* ``NodeBaseInterface``：提供节点基础功能。
* ``NodeLoggingInterface``：提供日志记录能力。

随后获取节点名称并输出日志。

下面的代码分别创建一个 ``rclcpp::Node`` 和一个 ``rclcpp_lifecycle::LifecycleNode``：

.. code-block:: c++

   class SimpleNode : public rclcpp::Node
   {
   public:
     SimpleNode(const std::string & node_name)
     : Node(node_name)
     {
     }
   };

   class LifecycleTalker : public rclcpp_lifecycle::LifecycleNode
   {
   public:
     explicit LifecycleTalker(
       const std::string & node_name,
       bool intra_process_comms = false)
     : rclcpp_lifecycle::LifecycleNode(
         node_name,
         rclcpp::NodeOptions().use_intra_process_comms(intra_process_comms))
     {}
   };

``rclcpp_lifecycle::LifecycleNode`` 通常包含 ``Unconfigured``、``Inactive``、``Active`` 和 ``Finalized`` 等状态转换功能。本示例为了突出节点接口的用法，没有展示这些状态转换操作。

在 ``main`` 函数中，分别创建普通节点和生命周期节点的 ``SharedPtr``，并将两个节点对象依次传递给 ``node_info``：

.. code-block:: c++

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::executors::SingleThreadedExecutor exe;

     auto node = std::make_shared<SimpleNode>("Simple_Node");
     auto lc_node = std::make_shared<LifecycleTalker>("Simple_LifeCycle_Node");

     node_info(*node);
     node_info(*lc_node);
   }

.. note::

   这里需要对 ``SharedPtr`` 解引用，因为模板接收的是 ``NodeT`` 对象的引用。

总结
----

``rclcpp::NodeInterfaces<>`` 为不同类型的 ROS 2 节点提供统一的接口访问方式。相比直接依赖 ``rclcpp::Node::SharedPtr``，它能够兼容普通节点和生命周期节点，并减少函数对具体节点类型的耦合。
