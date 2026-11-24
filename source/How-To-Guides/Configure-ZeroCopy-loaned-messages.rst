.. redirect-from::

  How-To-Guides/Disabling-ZeroCopy-loaned-messages

配置零拷贝借用消息
==================

.. contents:: 目录
   :depth: 2
   :local:

概述
----

ROS 2 的借用消息（loaned messages）和零拷贝数据共享机制旨在通过尽量减少数据复制来提升性能。使用借用消息时，RMW 中间件可以分配和管理消息内存，使发布者和订阅者能够直接共享数据缓冲区。这可以减少内存分配和数据复制带来的开销，从而降低延迟并提高吞吐量。

零拷贝数据共享尤其适用于需要高效传输大量数据的高性能应用。

有关借用消息工作原理的更多信息，请参阅 `Loaned Messages 设计文章 <https://design.ros2.org/articles/zero_copy.html>`_。

RMW 支持情况
------------

借用消息需要 RMW 实现提供支持。

.. list-table:: 借用消息支持状态
   :widths: 25 25 25

   * - RMW 实现
     - 支持状态
     - 文档
   * - rmw_fastrtps
     - 支持
     - `启用零拷贝数据共享 <https://github.com/ros2/rmw_fastrtps?tab=readme-ov-file#enable-zero-copy-data-sharing>`_
   * - rmw_connextdds
     - 不支持
     - 不适用
   * - rmw_cyclonedds
     - 不支持
     - 不适用

安装演示程序
------------

有关 ROS 2 安装详情，请参阅 :doc:`安装说明 <../../Installation>`。

如果你通过软件包安装 ROS 2，请确保已安装 ``ros-{DISTRO}-demo-nodes-cpp``。如果你下载了归档包，或从源码构建了 ROS 2，该演示程序已经包含在安装内容中。

使用借用消息
------------

如果底层 RMW 实现支持借用消息，发布者默认会使用借用消息。如果 RMW 实现不支持，则消息会使用发布者提供的分配器实例进行分配。

``talker_loaned_message`` 示例展示了如何创建 ROS 2 发布者，通过借用消息高效发布数据，而无需复制消息数据。示例源码：`talker_loaned_message.cpp <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/demo_nodes_cpp/src/topics/talker_loaned_message.cpp>`_。

.. code-block:: c++

    #include <chrono>
    #include <cstdio>
    #include <memory>
    #include <utility>

    #include "rclcpp/rclcpp.hpp"
    #include "rclcpp_components/register_node_macro.hpp"

    #include "std_msgs/msg/float64.hpp"
    #include "std_msgs/msg/string.hpp"

    #include "demo_nodes_cpp/visibility_control.h"

    using namespace std::chrono_literals;

    namespace demo_nodes_cpp
    {
    // Create a Talker class that subclasses the generic rclcpp::Node base class.
    // The main function below will instantiate the class as a ROS node.
    class LoanedMessageTalker : public rclcpp::Node
    {
    public:
      DEMO_NODES_CPP_PUBLIC
      explicit LoanedMessageTalker(const rclcpp::NodeOptions & options)
      : Node("loaned_message_talker", options)
      {
        setvbuf(stdout, NULL, _IONBF, BUFSIZ);

        auto publish_message =
          [this]() -> void
          {
            auto pod_loaned_msg = pod_pub_->borrow_loaned_message();
            auto pod_msg_data = static_cast<double>(count_);
            pod_loaned_msg.get().data = pod_msg_data;
            RCLCPP_INFO(this->get_logger(), "Publishing: '%f'", pod_msg_data);
            pod_pub_->publish(std::move(pod_loaned_msg));

            auto non_pod_loaned_msg = non_pod_pub_->borrow_loaned_message();
            auto non_pod_msg_data = "Hello World: " + std::to_string(count_);
            non_pod_loaned_msg.get().data = non_pod_msg_data;
            RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", non_pod_msg_data.c_str());
            non_pod_pub_->publish(std::move(non_pod_loaned_msg));
            count_++;
          };

        rclcpp::QoS qos(rclcpp::KeepLast(7));
        pod_pub_ = this->create_publisher<std_msgs::msg::Float64>("chatter_pod", qos);
        non_pod_pub_ = this->create_publisher<std_msgs::msg::String>("chatter", qos);
        timer_ = this->create_wall_timer(1s, publish_message);
      }

    private:
      size_t count_ = 1;
      rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr pod_pub_;
      rclcpp::Publisher<std_msgs::msg::String>::SharedPtr non_pod_pub_;
      rclcpp::TimerBase::SharedPtr timer_;
    };

    }  // namespace demo_nodes_cpp

本示例尝试通过调用 ``borrow_loaned_message()`` 从 RMW 实现中借用两种类型的消息：一种是普通旧数据（POD）类型 ``std_msgs::msg::Float64``，另一种是非 POD 类型 ``std_msgs::msg::String``。

对于 ``rmw_fastrtps``，借用消息要求消息类型为 POD 类型。

运行以下可执行程序即可启动演示（请记得先 source 环境设置文件）：

.. code-block:: console

    $ ros2 run demo_nodes_cpp talker_loaned_message
    [INFO] [1741063656.446278828] [loaned_message_talker]: Publishing: '1.000000'
    [INFO] [1741063656.446705580] [rclcpp]: Currently used middleware cannot loan messages. Local allocator will be used.
    [INFO] [1741063656.446754794] [loaned_message_talker]: Publishing: 'Hello World: 1'
    [INFO] [1741063657.446232119] [loaned_message_talker]: Publishing: '2.000000'
    [INFO] [1741063657.446401820] [loaned_message_talker]: Publishing: 'Hello World: 2'
    [...]

如果 RMW 实现不支持借用消息，所有消息都会使用发布者提供的分配器实例进行分配。可以通过以下命令进行验证：

.. code-block:: console

    $ RMW_IMPLEMENTATION=rmw_cyclonedds_cpp ros2 run demo_nodes_cpp talker_loaned_message

.. code-block:: console

    $ RMW_IMPLEMENTATION=rmw_cyclonedds_cpp ros2 run demo_nodes_cpp talker_loaned_message
    [INFO] [1741064109.676860153] [rclcpp]: Currently used middleware cannot loan messages. Local allocator will be used.
    [INFO] [1741064109.677043250] [loaned_message_talker]: Publishing: '1.000000'
    [INFO] [1741064109.677185724] [rclcpp]: Currently used middleware cannot loan messages. Local allocator will be used.
    [INFO] [1741064109.677224058] [loaned_message_talker]: Publishing: 'Hello World: 1'
    [INFO] [1741064110.676842111] [loaned_message_talker]: Publishing: '2.000000'
    [INFO] [1741064110.677008774] [loaned_message_talker]: Publishing: 'Hello World: 2'
    [...]

可以看到，两条消息都成功发布，但由于 RMW 实现不支持借用消息，因此消息使用发布者提供的本地分配器实例进行分配。

如何禁用借用消息
----------------

发布者
^^^^^^

默认情况下，借用消息会尝试从底层中间件借用内存（前提是中间件支持借用消息）。

可以使用 ``ROS_DISABLE_LOANED_MESSAGES`` 环境变量禁用借用消息，并回退到普通发布者行为，无需修改代码或中间件配置。运行以下命令设置环境变量：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        $ export ROS_DISABLE_LOANED_MESSAGES=1

      如果希望在不同 Shell 会话之间保持此设置，可以将命令添加到 Shell 启动脚本：

      .. code-block:: console

        $ echo "export ROS_DISABLE_LOANED_MESSAGES=1" >> ~/.bashrc

   .. group-tab:: macOS

      .. code-block:: console

        $ export ROS_DISABLE_LOANED_MESSAGES=1

      如果希望在不同 Shell 会话之间保持此设置，可以将命令添加到 Shell 启动脚本：

      .. code-block:: console

        $ echo "export ROS_DISABLE_LOANED_MESSAGES=1" >> ~/.bash_profile

   .. group-tab:: Windows

      .. code-block:: console

        $ set ROS_DISABLE_LOANED_MESSAGES=1

      如果希望在不同 Shell 会话之间永久生效，还可以运行：

      .. code-block:: console

        $ setx ROS_DISABLE_LOANED_MESSAGES 1

订阅者
^^^^^^

目前，在订阅端使用借用消息并不安全。更多详情请参阅 `rmw issue <https://github.com/ros2/rmw_cyclonedds/issues/469>`_ 和 `rclcpp issue <https://github.com/ros2/rclcpp/issues/2401>`_。

因此，即使底层中间件支持借用消息，订阅端默认也会禁用该功能（参见 `默认启用禁用借用消息的变更 <https://github.com/ros2/rcl/pull/1110>`_）。

如果希望在订阅端启用借用消息，需要显式将环境变量 ``ROS_DISABLE_LOANED_MESSAGES`` 设置为 ``0``。

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        $ export ROS_DISABLE_LOANED_MESSAGES=0

      如果希望在不同 Shell 会话之间保持此设置，可以将命令添加到 Shell 启动脚本：

      .. code-block:: console

        $ echo "export ROS_DISABLE_LOANED_MESSAGES=0" >> ~/.bashrc

   .. group-tab:: macOS

      .. code-block:: console

        $ export ROS_DISABLE_LOANED_MESSAGES=0

      如果希望在不同 Shell 会话之间保持此设置，可以将命令添加到 Shell 启动脚本：

      .. code-block:: console

        $ echo "export ROS_DISABLE_LOANED_MESSAGES=0" >> ~/.bash_profile

   .. group-tab:: Windows

      .. code-block:: console

        $ set ROS_DISABLE_LOANED_MESSAGES=0

      如果希望在不同 Shell 会话之间永久生效，还可以运行：

      .. code-block:: console

        $ setx ROS_DISABLE_LOANED_MESSAGES 0
