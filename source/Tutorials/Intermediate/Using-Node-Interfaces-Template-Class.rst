使用 Node 接口模板类
=====================

**目标：** 学习如何使用 rclcpp 提供的 Node 接口，将节点功能组合到独立类中。

**教程级别：** 中级

.. contents:: 目录
   :depth: 2
   :local:

背景
----

§rclcpp::Node§ 提供了发布者、订阅者、参数、日志、时钟和定时器等多种接口。某些类只需要使用其中一部分能力，不一定需要继承完整的 §rclcpp::Node§。

ROS 2 提供了模板化 Node 接口类，使组件可以通过构造函数接收所需接口，而不是直接依赖完整节点对象。这有助于降低组件耦合，并改善代码复用和单元测试能力。

接口使用
--------

常见接口包括：

* §rclcpp::NodeBaseInterface§：节点基础信息及执行器相关接口。
* §rclcpp::NodeTopicsInterface§：创建发布者和订阅者。
* §rclcpp::NodeParametersInterface§：声明、读取和设置参数。
* §rclcpp::NodeLoggingInterface§：获取 logger。
* §rclcpp::NodeClockInterface§：访问节点时钟。
* §rclcpp::NodeTimersInterface§：创建定时器。

组件可以通过模板参数或接口指针接收所需能力，并调用对应接口创建 ROS 实体。应只依赖实际需要的接口，避免不必要地耦合整个 Node。

设计建议
--------

* 对只需要发布订阅功能的类，优先依赖 topics interface。
* 需要参数时再注入 parameters interface。
* 需要记录日志时使用 logging interface。
* 对需要执行器管理的实体，确保基础节点接口和生命周期管理正确。
* 单元测试时可以提供满足接口要求的节点实例，降低测试对完整系统的依赖。

总结
----

Node 接口模板类使 C++ 组件能够按需依赖 ROS 2 节点能力，减少与完整 §rclcpp::Node§ 的耦合，并提高组件可复用性和可测试性。
