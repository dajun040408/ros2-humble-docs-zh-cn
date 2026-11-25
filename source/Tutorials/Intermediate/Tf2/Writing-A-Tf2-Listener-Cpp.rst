.. redirect-from::

    Tutorials/Tf2/Writing-A-Tf2-Listener-Cpp

编写监听器（C++）
=================

**目标：** 学习如何使用 tf2 获取坐标系变换。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

在前面的教程中，我们创建了 tf2 广播器，将海龟的位姿发布到 tf2。

本教程将创建一个 tf2 监听器，开始使用 tf2 获取坐标系之间的变换。

前置条件
--------

本教程假设你已经完成 :doc:`tf2 静态广播器教程（C++） <./Writing-A-Tf2-Static-Broadcaster-Cpp>` 和 :doc:`tf2 广播器教程（C++） <./Writing-A-Tf2-Broadcaster-Cpp>`。

前面的教程中已经创建了 ``learning_tf2_cpp`` 功能包，本教程会继续在该功能包中进行开发。

任务
----

1. 编写监听器节点
^^^^^^^^^^^^^^^^^

首先创建源文件。进入之前创建的 ``learning_tf2_cpp`` 功能包，在 ``src`` 目录中下载示例监听器代码：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/turtle_tf2_listener.cpp

  .. group-tab:: macOS

    .. code-block:: console

       $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/turtle_tf2_listener.cpp

  .. group-tab:: Windows

    在 Windows 命令提示符中：

    .. code-block:: console

       $ curl -sk https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/turtle_tf2_listener.cpp -o turtle_tf2_listener.cpp

    或在 PowerShell 中：

    .. code-block:: console

       $ curl https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/turtle_tf2_listener.cpp -o turtle_tf2_listener.cpp

使用文本编辑器打开 ``turtle_tf2_listener.cpp``：

.. code-block:: c++

   #include <chrono>
   #include <functional>
   #include <memory>
   #include <string>

   #include "geometry_msgs/msg/transform_stamped.hpp"
   #include "geometry_msgs/msg/twist.hpp"
   #include "rclcpp/rclcpp.hpp"
   #include "tf2/exceptions.h"
   #include "tf2_ros/transform_listener.h"
   #include "tf2_ros/buffer.h"
   #include "turtlesim/srv/spawn.hpp"

   using namespace std::chrono_literals;

   class FrameListener : public rclcpp::Node
   {
   public:
     FrameListener()
     : Node("turtle_tf2_frame_listener"),
       turtle_spawning_service_ready_(false),
       turtle_spawned_(false)
     {
       target_frame_ = this->declare_parameter<std::string>("target_frame", "turtle1");

       tf_buffer_ = std::make_unique<tf2_ros::Buffer>(this->get_clock());
       tf_listener_ = std::make_shared<tf2_ros::TransformListener>(*tf_buffer_);

       spawner_ = this->create_client<turtlesim::srv::Spawn>("spawn");
       publisher_ = this->create_publisher<geometry_msgs::msg::Twist>(
         "turtle2/cmd_vel", 1);

       timer_ = this->create_wall_timer(
         1s, std::bind(&FrameListener::on_timer, this));
     }

   private:
     void on_timer()
     {
       std::string fromFrameRel = target_frame_.c_str();
       std::string toFrameRel = "turtle2";

       if (turtle_spawning_service_ready_) {
         if (turtle_spawned_) {
           geometry_msgs::msg::TransformStamped t;

           try {
             t = tf_buffer_->lookupTransform(
               toFrameRel, fromFrameRel, tf2::TimePointZero);
           } catch (const tf2::TransformException & ex) {
             RCLCPP_INFO(
               this->get_logger(), "Could not transform %s to %s: %s",
               toFrameRel.c_str(), fromFrameRel.c_str(), ex.what());
             return;
           }

           geometry_msgs::msg::Twist msg;
           static const double scaleRotationRate = 1.0;
           msg.angular.z = scaleRotationRate * atan2(
             t.transform.translation.y, t.transform.translation.x);

           static const double scaleForwardSpeed = 0.5;
           msg.linear.x = scaleForwardSpeed * sqrt(
             pow(t.transform.translation.x, 2) +
             pow(t.transform.translation.y, 2));

           publisher_->publish(msg);
         } else {
           RCLCPP_INFO(this->get_logger(), "Successfully spawned");
           turtle_spawned_ = true;
         }
       } else {
         if (spawner_->service_is_ready()) {
           auto request = std::make_shared<turtlesim::srv::Spawn::Request>();
           request->x = 4.0;
           request->y = 2.0;
           request->theta = 0.0;
           request->name = "turtle2";

           using ServiceResponseFuture =
             rclcpp::Client<turtlesim::srv::Spawn>::SharedFuture;
           auto response_received_callback = [this](ServiceResponseFuture future) {
               auto result = future.get();
               if (strcmp(result->name.c_str(), "turtle2") == 0) {
                 turtle_spawning_service_ready_ = true;
               } else {
                 RCLCPP_ERROR(this->get_logger(), "Service callback result mismatch");
               }
             };
           auto result = spawner_->async_send_request(request, response_received_callback);
         } else {
           RCLCPP_INFO(this->get_logger(), "Service is not ready");
         }
       }
     }

     bool turtle_spawning_service_ready_;
     bool turtle_spawned_;
     rclcpp::Client<turtlesim::srv::Spawn>::SharedPtr spawner_{nullptr};
     rclcpp::TimerBase::SharedPtr timer_{nullptr};
     rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_{nullptr};
     std::shared_ptr<tf2_ros::TransformListener> tf_listener_{nullptr};
     std::unique_ptr<tf2_ros::Buffer> tf_buffer_;
     std::string target_frame_;
   };

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<FrameListener>());
     rclcpp::shutdown();
     return 0;
   }

.. include:: ../../../_internal/Rclcpp-Convenience-Header-Note.rst

1.1 理解代码
~~~~~~~~~~~~

要理解生成海龟的服务如何工作，可以参阅 :doc:`编写简单的服务和客户端（C++） <../../Beginner-Client-Libraries/Writing-A-Simple-Cpp-Service-And-Client>` 教程。

现在重点看一下如何访问坐标系变换。``tf2_ros`` 包含 ``TransformListener`` 类，可以简化接收变换的工作：

.. code-block:: c++

   #include "tf2_ros/transform_listener.h"

创建 ``TransformListener`` 对象后，它会自动通过网络接收 tf2 变换，并将其缓存在缓冲区中，默认缓存时间为 10 秒：

.. code-block:: c++

   tf_listener_ = std::make_shared<tf2_ros::TransformListener>(*tf_buffer_);

.. note::

   上面的构造函数 ``TransformListener(*tf_buffer_)`` 是简化形式。它会在内部创建一个独立节点来管理订阅。

   如果编写的是可组合节点（component），或者希望变换监听器遵循当前节点的参数和话题重映射（例如 ``/tf`` 的命名空间或话题重映射），应将 ``this`` 或节点接口传递给构造函数：

   .. code-block:: c++

      tf_listener_ =
        std::make_shared<tf2_ros::TransformListener>(*tf_buffer_, this);

   这样，订阅会创建在现有节点上，并继承其参数和话题配置。

最后，调用 ``lookupTransform()`` 查询特定变换。该方法接收三个参数：

1. 目标坐标系。
2. 源坐标系。
3. 希望查询变换的时间。

提供 ``tf2::TimePointZero`` 表示获取当前缓冲区中最新可用的变换。整个调用使用 try-catch 处理可能出现的异常：

.. code-block:: c++

   t = tf_buffer_->lookupTransform(
     toFrameRel, fromFrameRel,
     tf2::TimePointZero);

返回的变换表示目标海龟相对于 ``turtle2`` 的位置和方向。随后根据两只海龟之间的角度计算速度命令，使目标海龟能够跟随另一只海龟。

更多 tf2 通用信息，请参阅 :doc:`tf2 概念 <../../../Concepts/Intermediate/About-Tf2>`。

1.2 配置 CMakeLists.txt
~~~~~~~~~~~~~~~~~~~~~~~

返回 ``learning_tf2_cpp`` 目录，打开 ``CMakeLists.txt``，添加监听器可执行程序：

.. code-block:: cmake

   add_executable(turtle_tf2_listener src/turtle_tf2_listener.cpp)
   ament_target_dependencies(
     turtle_tf2_listener
     geometry_msgs
     rclcpp
     tf2
     tf2_ros
     turtlesim
   )

最后添加安装规则，使 ``ros2 run`` 能够找到该可执行程序：

.. code-block:: cmake

   install(TARGETS
     turtle_tf2_listener
     DESTINATION lib/${PROJECT_NAME})

2. 更新启动文件
^^^^^^^^^^^^^^^

使用文本编辑器打开 ``src/learning_tf2_cpp/launch`` 目录中的 ``turtle_tf2_demo_launch`` 启动文件，扩展名可以是 ``.py``、``.xml`` 或 ``.yaml``。

添加两个新节点、一个启动参数以及所需的导入语句。最终文件应如下所示：

.. tabs::

  .. group-tab:: Python

    .. literalinclude:: launch/listener_cpp_launch.py
       :language: python

  .. group-tab:: XML

    .. literalinclude:: launch/listener_cpp_launch.xml
       :language: xml

  .. group-tab:: YAML

    .. literalinclude:: launch/listener_cpp_launch.yaml
       :language: yaml

启动文件会声明 ``target_frame`` 参数，启动第二只海龟的广播器，并启动一个订阅这些变换的监听器。

3. 构建
^^^^^^^

在工作空间根目录运行 ``rosdep`` 检查依赖：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

   .. group-tab:: macOS

      ``rosdep`` 仅在 Linux 上运行，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

   .. group-tab:: Windows

      ``rosdep`` 仅在 Linux 上运行，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

仍在工作空间根目录中，构建功能包：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ colcon build --packages-select learning_tf2_cpp

   .. group-tab:: macOS

      .. code-block:: console

         $ colcon build --packages-select learning_tf2_cpp

   .. group-tab:: Windows

      .. code-block:: console

         $ colcon build --merge-install --packages-select learning_tf2_cpp

打开新终端，进入工作空间根目录并加载设置文件：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ . install/setup.bash

   .. group-tab:: macOS

      .. code-block:: console

         $ . install/setup.bash

   .. group-tab:: Windows

      在 Windows 命令提示符中：

      .. code-block:: console

         $ call install\setup.bat

      或在 PowerShell 中：

      .. code-block:: console

         $ .\install\setup.ps1

4. 运行
^^^^^^^

现在可以启动完整的海龟演示：

.. tabs::

  .. group-tab:: XML

    .. code-block:: console

       $ ros2 launch learning_tf2_cpp turtle_tf2_demo_launch.xml

  .. group-tab:: YAML

    .. code-block:: console

       $ ros2 launch learning_tf2_cpp turtle_tf2_demo_launch.yaml

  .. group-tab:: Python

    .. code-block:: console

       $ ros2 launch learning_tf2_cpp turtle_tf2_demo_launch.py

此时应该能看到包含两只海龟的 turtlesim 窗口。在第二个终端中运行：

.. code-block:: console

   $ ros2 run turtlesim turtle_teleop_key

使用方向键控制第一只海龟（确保终端窗口处于活动状态，而不是仿真窗口），就会看到第二只海龟跟随第一只海龟移动。

总结
----

本教程介绍了如何使用 tf2 获取坐标系变换，并完成了一个能够让第二只海龟跟随第一只海龟的 turtlesim 演示。
