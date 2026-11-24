.. redirect-from::

    Tutorials/Writing-A-Simple-Cpp-Publisher-And-Subscriber

.. _CppPubSub:

编写简单的发布者和订阅者（C++）
===============================

**目标：** 使用 C++ 创建并运行发布者和订阅者节点。

**教程级别：** 初级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

:doc:`节点 <../Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes>` 是通过 ROS 计算图进行通信的可执行进程。本教程中的节点通过 :doc:`话题 <../Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics>` 交换字符串消息。

C++ 发布者和订阅者有多种实现方式。可以查看 `ros2/examples 仓库 <https://github.com/ros2/examples/tree/{REPOS_FILE_BRANCH}/rclcpp/topics>`_ 中的 ``minimal_publisher`` 和 ``minimal_subscriber`` 功能包。

前置条件
--------

此前的教程已经介绍了如何 :doc:`创建工作空间 <./Creating-A-Workspace/Creating-A-Workspace>` 和 :doc:`创建功能包 <./Creating-Your-First-ROS2-Package>`。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

打开新终端并 :doc:`source ROS 2 安装环境 <../Beginner-CLI-Tools/Configuring-ROS2-Environment>`。

进入之前创建的 ros2_ws 工作空间，再进入 src 目录（功能包应创建在 src 中，而不是工作空间根目录），运行：

.. code-block:: console

    $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_pubsub

终端会返回消息，确认 cpp_pubsub 功能包及其文件和目录已创建。

进入 ros2_ws/src/cpp_pubsub/src。CMake 功能包的可执行程序源文件通常放在该目录中。

2. 编写发布者节点
^^^^^^^^^^^^^^^^^

下载示例 talker 代码：

.. code-block:: console

   $ wget -O publisher_member_function.cpp https://raw.githubusercontent.com/ros2/examples/{REPOS_FILE_BRANCH}/rclcpp/topics/minimal_publisher/member_function.cpp

Windows 命令行可以使用 curl：

.. code-block:: console

   $ curl -sk https://raw.githubusercontent.com/ros2/examples/{REPOS_FILE_BRANCH}/rclcpp/topics/minimal_publisher/member_function.cpp -o publisher_member_function.cpp

打开 publisher_member_function.cpp。示例通过继承 rclcpp::Node 创建节点，使用 create_publisher() 创建发布者，并通过定时器周期性发布 std_msgs/msg/String 消息。

.. code-block:: cpp

   #include <chrono>
   #include <functional>
   #include <memory>
   #include <string>

   #include "rclcpp/rclcpp.hpp"
   #include "std_msgs/msg/string.hpp"

   using namespace std::chrono_literals;

   /* This example creates a subclass of Node and uses std::bind() to register a
   * member function as a callback from the timer. */

   class MinimalPublisher : public rclcpp::Node
   {
     public:
       MinimalPublisher()
       : Node("minimal_publisher"), count_(0)
       {
         publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
         timer_ = this->create_wall_timer(
         500ms, std::bind(&MinimalPublisher::timer_callback, this));
       }

     private:
       void timer_callback()
       {
         auto message = std_msgs::msg::String();
         message.data = "Hello, world! " + std::to_string(count_++);
         RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
         publisher_->publish(message);
       }
       rclcpp::TimerBase::SharedPtr timer_;
       rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
       size_t count_;
   };

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<MinimalPublisher>());
     rclcpp::shutdown();
     return 0;
   }

2.1 理解代码
~~~~~~~~~~~~~

代码开头引入了所需的标准 C++ 头文件。随后包含 ``rclcpp/rclcpp.hpp``，以使用 ROS 2 系统中最常用的功能；最后包含 ``std_msgs/msg/string.hpp``，其中定义了本教程用于发布数据的内置消息类型。

.. code-block:: cpp

   #include <chrono>
   #include <functional>
   #include <memory>
   #include <string>

   #include "rclcpp/rclcpp.hpp"
   #include "std_msgs/msg/string.hpp"

   using namespace std::chrono_literals;

这些头文件构成节点的依赖项。还需要在 ``package.xml`` 和 ``CMakeLists.txt`` 中声明这些依赖，下一节会进行配置。

接下来，通过继承 ``rclcpp::Node`` 创建 ``MinimalPublisher`` 节点类。代码中的 ``this`` 均指当前节点。

.. code-block:: cpp

   class MinimalPublisher : public rclcpp::Node

公共构造函数将节点命名为 ``minimal_publisher``，并将计数器 ``count_`` 初始化为 0。在构造函数中，发布者使用 ``String`` 消息类型和 ``topic`` 话题名称创建，队列深度设置为 10，用于在消息积压时限制队列长度。随后初始化 ``timer_``，使 ``timer_callback`` 函数每 500 毫秒执行一次。

.. code-block:: cpp

   public:
     MinimalPublisher()
     : Node("minimal_publisher"), count_(0)
     {
       publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
       timer_ = this->create_wall_timer(
       500ms, std::bind(&MinimalPublisher::timer_callback, this));
     }

``timer_callback`` 函数负责设置消息数据并实际发布消息。``RCLCPP_INFO`` 宏会将每条已发布消息输出到控制台。

.. code-block:: cpp

   private:
     void timer_callback()
     {
       auto message = std_msgs::msg::String();
       message.data = "Hello, world! " + std::to_string(count_++);
       RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
       publisher_->publish(message);
     }

最后声明定时器、发布者和计数器成员变量。

.. code-block:: cpp

   rclcpp::TimerBase::SharedPtr timer_;
   rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
   size_t count_;

``MinimalPublisher`` 类之后是 ``main`` 函数，节点在这里真正开始执行。``rclcpp::init`` 用于初始化 ROS 2，``rclcpp::spin`` 开始处理节点数据，包括定时器触发的回调；退出前调用 ``rclcpp::shutdown`` 关闭 ROS 2。

.. code-block:: cpp

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<MinimalPublisher>());
     rclcpp::shutdown();
     return 0;
   }

2.2 添加依赖项
~~~~~~~~~~~~~~~~~~~~

返回上一级目录 ``ros2_ws/src/cpp_pubsub``。这里已经为你创建了 ``CMakeLists.txt`` 和 ``package.xml`` 文件。

使用文本编辑器打开 ``package.xml``。按照 :doc:`创建 ROS 2 功能包 <./Creating-Your-First-ROS2-Package>` 教程中的说明，确保填写 ``<description>``、``<maintainer>`` 和 ``<license>`` 标签：

.. code-block:: xml

   <description>Examples of minimal publisher/subscriber using rclcpp</description>
   <maintainer email="you@email.com">Your Name</maintainer>
   <license>Apache License 2.0</license>

在 ``ament_cmake`` 构建工具依赖项之后添加以下依赖，它们对应节点源代码中的 include 语句：

.. code-block:: xml

   <depend>rclcpp</depend>
   <depend>std_msgs</depend>

这表示该功能包在构建和运行代码时都需要 ``rclcpp`` 和 ``std_msgs``。保存文件。

2.3 配置 CMakeLists.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

打开 ``CMakeLists.txt``。在已有的 ``find_package(ament_cmake REQUIRED)`` 依赖项下面添加：

.. code-block:: cmake

   find_package(rclcpp REQUIRED)
   find_package(std_msgs REQUIRED)

然后添加可执行程序，并将其命名为 ``talker``，这样就可以通过 ``ros2 run`` 运行节点：

.. code-block:: cmake

   add_executable(talker src/publisher_member_function.cpp)
   ament_target_dependencies(talker rclcpp std_msgs)

最后添加 ``install(TARGETS ...)`` 部分，使 ``ros2 run`` 能够找到该可执行程序：

.. code-block:: cmake

   install(TARGETS
     talker
     DESTINATION lib/${PROJECT_NAME})

可以删除 ``CMakeLists.txt`` 中不必要的部分和注释，使其结构更简洁。订阅者节点创建完成后，还需要将它对应的可执行程序一并加入该文件。

3. 编写订阅者节点
^^^^^^^^^^^^^^^^^

在同一 src 目录中创建 subscriber_member_function.cpp。订阅者节点同样继承 rclcpp::Node，并通过 create_subscription() 订阅 topic 话题。每次收到消息时，回调函数会输出消息内容。

.. code-block:: cpp

   #include <memory>

   #include "rclcpp/rclcpp.hpp"
   #include "std_msgs/msg/string.hpp"
   using std::placeholders::_1;

   class MinimalSubscriber : public rclcpp::Node
   {
     public:
       MinimalSubscriber()
       : Node("minimal_subscriber")
       {
         subscription_ = this->create_subscription<std_msgs::msg::String>(
         "topic", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
       }

     private:
       void topic_callback(const std_msgs::msg::String & msg) const
       {
         RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg.data.c_str());
       }
       rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
   };

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<MinimalSubscriber>());
     rclcpp::shutdown();
     return 0;
   }

3.1 理解代码
~~~~~~~~~~~~~

订阅者节点的代码与发布者节点非常相似。这里节点名称为 ``minimal_subscriber``，构造函数使用节点的 ``create_subscription`` 方法创建订阅，并注册回调函数。

订阅者不需要定时器，因为只要 ``topic`` 话题上发布了数据，它就会作出响应。

.. code-block:: cpp

   public:
     MinimalSubscriber()
     : Node("minimal_subscriber")
     {
       subscription_ = this->create_subscription<std_msgs::msg::String>(
       "topic", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
     }

回顾 :doc:`话题教程 <../Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics>`：发布者和订阅者使用的话题名称及消息类型必须一致，才能相互通信。

``topic_callback`` 函数接收通过话题发布的字符串消息，并使用 ``RCLCPP_INFO`` 宏将其输出到控制台。

该类唯一需要声明的成员变量是订阅对象：

.. code-block:: cpp

   private:
     void topic_callback(const std_msgs::msg::String & msg) const
     {
       RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg.data.c_str());
     }
     rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;

``main`` 函数与发布者节点基本相同，区别在于这里 spin 的是 ``MinimalSubscriber`` 节点。对于发布者，spin 会启动定时器；对于订阅者，spin 则使节点准备好随时接收消息。

由于该节点与发布者节点具有相同的依赖项，因此无需在 ``package.xml`` 中添加新的依赖。

3.2 更新 CMakeLists.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

重新打开 ``CMakeLists.txt``，在发布者节点对应的配置下面添加订阅者节点的可执行程序和目标：

.. code-block:: cmake

   add_executable(listener src/subscriber_member_function.cpp)
   ament_target_dependencies(listener rclcpp std_msgs)

   install(TARGETS
     talker
     listener
     DESTINATION lib/${PROJECT_NAME})

保存文件后，发布者/订阅者系统的配置就完成了。

4. 配置 CMakeLists.txt
^^^^^^^^^^^^^^^^^^^^^^

在 CMakeLists.txt 中查找 rclcpp 和 std_msgs，并为两个节点添加可执行程序：

.. code-block:: cmake

   find_package(rclcpp REQUIRED)
   find_package(std_msgs REQUIRED)

   add_executable(talker src/publisher_member_function.cpp)
   ament_target_dependencies(talker rclcpp std_msgs)

   add_executable(listener src/subscriber_member_function.cpp)
   ament_target_dependencies(listener rclcpp std_msgs)

   install(TARGETS talker listener DESTINATION lib/cpp_pubsub)

5. 构建并运行
^^^^^^^^^^^^^

在工作空间根目录构建：

.. code-block:: console

   $ colcon build --packages-select cpp_pubsub

打开两个终端，分别 source 工作空间并运行发布者和订阅者：

.. code-block:: console

   $ ros2 run cpp_pubsub talker

.. code-block:: console

   $ ros2 run cpp_pubsub listener

发布者会周期性发布 Hello, world!，订阅者会输出收到的消息。

总结
----

你已经创建了两个节点，并通过话题发布和订阅数据。在编译和运行节点之前，你还在功能包配置文件中添加了所需依赖项和可执行程序。

下一步
------

接下来，你将创建另一个使用服务/客户端模型的简单 ROS 2 功能包。你可以选择使用 :doc:`C++ <./Writing-A-Simple-Cpp-Service-And-Client>` 或 :doc:`Python <./Writing-A-Simple-Py-Service-And-Client>` 编写。

相关内容
--------

C++ 发布者和订阅者有多种实现方式。可以查看 `ros2/examples 仓库 <https://github.com/ros2/examples/tree/{REPOS_FILE_BRANCH}/rclcpp/topics>`_ 中的 ``minimal_publisher`` 和 ``minimal_subscriber`` 功能包。
