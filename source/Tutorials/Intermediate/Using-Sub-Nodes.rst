ROS 2 子节点（C++）
====================

**目标：** 学习如何在 ``rclcpp`` 中创建和使用子节点（``create_sub_node``），以层次化组织话题和服务。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

概要
----

* **子节点（sub-node）** 是通过现有 ``rclcpp::Node`` 的 ``create_sub_node()`` 方法创建的次级节点实例。
* 子节点共享父节点底层的 context、执行器回调、参数接口、日志接口和 ROS 计算图身份。
* 子节点定义额外的相对**子命名空间**，通过子节点创建的话题发布者、订阅者、服务客户端和服务端等实体都会受到该命名空间约束。
* 在 ROS 1 中，开发者通常使用 ``ros::NodeHandle`` 为内部辅助类设置命名空间；在 ROS 2 中，``create_sub_node()`` 为节点内部的 C++ 组件提供类似功能。

概述
----

在 ROS 2 中，标准节点代表计算图中的一个实体。但复杂节点通常包含内部辅助库、设备子驱动或模块化算法，这些组件需要在各自的命名空间下发布或订阅话题。

如果为每个内部子组件创建独立节点，会产生额外开销：每个节点都拥有自己的中间件 participant 和发现实体，需要单独管理执行器或线程调度，还会使节点图变得复杂。

为解决这一问题，``rclcpp::Node`` 提供了 ``create_sub_node()`` 方法。子节点允许单个 ROS 2 节点进程中的内部组件封装各自相对的话题和服务命名空间，同时复用父节点底层资源。

子节点的工作方式
----------------

命名空间与名称
^^^^^^^^^^^^^^

创建子节点时，需要提供一个相对的子命名空间字符串：

.. code-block:: cpp

   auto node = std::make_shared<rclcpp::Node>("my_node", "/my_ns");
   auto sub_node = node->create_sub_node("sub_ns");

节点提供三个与命名空间相关的查询方法：

* ``get_namespace()``：返回父节点的基础命名空间，例如 ``"/my_ns"``。
* ``get_sub_namespace()``：返回累计的相对子命名空间，例如 ``"sub_ns"``。
* ``get_effective_namespace()``：返回基础命名空间与累计子命名空间的组合，例如 ``"/my_ns/sub_ns"``。

子节点还可以按层级嵌套：

.. code-block:: cpp

   auto sub_node2 = sub_node->create_sub_node("nested");
   // sub_node2->get_sub_namespace()       -> "sub_ns/nested"
   // sub_node2->get_effective_namespace() -> "/my_ns/sub_ns/nested"

实体命名空间规则
^^^^^^^^^^^^^^^^

使用子节点创建发布者、订阅者、服务客户端或服务端时：

* **相对名称：** 不以 ``/`` 开头的相对话题或服务名称，会相对于子节点的有效命名空间解析。例如，有效命名空间为 ``/my_ns/sub_ns`` 的子节点创建 ``chatter`` 发布者，最终话题名称为 ``/my_ns/sub_ns/chatter``。
* **绝对名称：** 以 ``/`` 开头的绝对名称会绕过所有命名空间，直接解析为全局名称。
* **相对名称要求：** 传递给 ``create_sub_node()`` 的子命名空间必须是相对名称，不能以 ``/`` 开头，也不能为空。传入绝对或空子命名空间会抛出 ``rclcpp::exceptions::NameValidationError``。

共享资源与作用域行为
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - 项目
     - 行为
   * - 计算图身份
     - 共享。子节点共享父节点的 ``rclcpp::node_interfaces::NodeBaseInterface``，不会作为独立节点出现在 ``ros2 node list`` 中。
   * - 节点名称
     - 共享。``sub_node->get_name()`` 返回父节点名称。
   * - 执行器与回调
     - 共享。子节点实体的回调由父节点的执行器调度。应 spin 父节点，而不是子节点。
   * - 参数
     - 共享。子节点共享父节点的 ``rclcpp::node_interfaces::NodeParametersInterface``，参数声明和查询都作用于父节点参数存储。
   * - 日志
     - 共享。子节点共享父节点的 ``rclcpp::node_interfaces::NodeLoggingInterface`` 和 logger。
   * - 时钟与定时器
     - 共享。定时器和时钟接口与父节点共享。
   * - 实体命名空间
     - 独立作用域。相对名称的发布者、订阅者和服务使用子节点的有效命名空间。

C++ 示例
--------

下面的示例创建一个父节点和两个子节点，分别发布两个传感器的遥测数据：

.. code-block:: cpp

   #include <chrono>
   #include <memory>
   #include <string>

   #include "rclcpp/rclcpp.hpp"
   #include "std_msgs/msg/string.hpp"

   using namespace std::chrono_literals;

   class RobotSystemNode : public rclcpp::Node
   {
   public:
     RobotSystemNode()
     : Node("robot_system", "robot")
     {
       imu_subnode_ = this->create_sub_node("imu");
       camera_subnode_ = this->create_sub_node("camera");

       imu_pub_ = imu_subnode_->create_publisher<std_msgs::msg::String>("data", 10);
       camera_pub_ = camera_subnode_->create_publisher<std_msgs::msg::String>("status", 10);

       timer_ = this->create_wall_timer(
         1000ms, std::bind(&RobotSystemNode::publish_data, this));
     }

   private:
     void publish_data()
     {
       auto imu_msg = std_msgs::msg::String();
       imu_msg.data = "imu_ok";
       imu_pub_->publish(imu_msg);

       auto cam_msg = std_msgs::msg::String();
       cam_msg.data = "camera_streaming";
       camera_pub_->publish(cam_msg);
     }

     rclcpp::Node::SharedPtr imu_subnode_;
     rclcpp::Node::SharedPtr camera_subnode_;
     rclcpp::Publisher<std_msgs::msg::String>::SharedPtr imu_pub_;
     rclcpp::Publisher<std_msgs::msg::String>::SharedPtr camera_pub_;
     rclcpp::TimerBase::SharedPtr timer_;
   };

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     auto node = std::make_shared<RobotSystemNode>();
     rclcpp::spin(node);
     rclcpp::shutdown();
     return 0;
   }

使用 CLI 工具验证行为
---------------------

运行节点时，可以通过标准命令行工具验证子节点在 ROS 2 计算图中的表现。

1. 列出活动节点：

   .. code-block:: console

      $ ros2 node list
      /robot/robot_system

   计算图中只会显示父节点 ``/robot/robot_system``。子节点不会注册为独立节点。

2. 列出活动话题：

   .. code-block:: console

      $ ros2 topic list
      /parameter_events
      /robot/camera/status
      /robot/imu/data
      /rosout

   子节点发布的话题会根据各自有效命名空间，正确位于 ``/robot/camera/`` 和 ``/robot/imu/`` 下。

何时使用子节点
--------------

* 如果正在开发单个可执行程序内部的模块化 C++ 类或辅助库，希望每个组件管理自己的话题或服务命名空间，同时避免创建额外 ROS 2 节点的开销，可以使用子节点。
* 如果组件代表独立计算单元，需要被单独发现、在启动或运行时动态加载到组件容器，或组合到不同进程中，应使用可组合节点（components）。
* 如果组件需要独立操作系统进程、不同生命周期，或跨机器物理隔离，应使用独立节点。
