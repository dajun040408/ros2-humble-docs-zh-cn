.. redirect-from::

    Tutorials/Tf2/Using-Stamped-Datatypes-With-Tf2-Ros-MessageFilter

.. _UsingStampedDatatypesWithTf2RosMessageFilter:

在 tf2_ros 中使用带时间戳的数据类型和 MessageFilter
===================================================

**目标：** 学习如何使用 ``tf2_ros::MessageFilter`` 处理带时间戳的数据类型。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 3
   :local:

背景
----

本教程介绍如何在 tf2 中使用传感器数据。现实世界中的传感器数据示例包括：

* 单目和双目摄像头。
* 激光扫描仪。

假设创建了一只名为 ``turtle3`` 的新乌龟，但它没有良好的里程计数据。不过，有一个俯视摄像头正在跟踪它的位置，并将其作为 ``PointStamped`` 消息发布在 ``world`` 坐标系中。

``turtle1`` 希望知道 ``turtle3`` 相对于自身的位置。

为此，``turtle1`` 必须订阅发布 ``turtle3`` 位姿的话题，等待目标坐标系所需的变换准备就绪，然后才能执行后续操作。

``tf2_ros::MessageFilter`` 可以简化这一过程。它会订阅任意带有 header 的 ROS 2 消息，并在能够将消息变换到目标坐标系之前缓存该消息。

前置条件
--------

本教程要求安装 ``turtle_tf2_py`` 功能包。

.. tabs::

  .. group-tab:: Ubuntu

    .. code-block:: console

       $ sudo apt install ros-{DISTRO}-turtle-tf2-py

  .. group-tab:: RHEL

    .. code-block:: console

       $ sudo dnf install ros-{DISTRO}-turtle-tf2-py

  .. group-tab:: 从源码构建

    在 ``ros2_ws`` 工作空间的 ``src`` 目录中克隆所需仓库：

    .. code-block:: console

       $ git clone https://github.com/ros/geometry_tutorials.git -b ros2
       $ colcon build --packages-select turtle_tf2_py

任务
----

1. 编写 PointStamped 消息广播器节点
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

本教程将创建一个演示应用，其中包含一个 Python 节点，用于广播 ``turtle3`` 的 ``PointStamped`` 位置消息。

进入前面教程创建的 ``learning_tf2_py`` :doc:`功能包 <./Writing-A-Tf2-Static-Broadcaster-Py>`。在 ``src/learning_tf2_py/learning_tf2_py`` 目录中下载示例传感器消息广播器：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/turtle_tf2_message_broadcaster.py

  .. group-tab:: macOS

    .. code-block:: console

       $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/turtle_tf2_message_broadcaster.py

  .. group-tab:: Windows

    在 Windows 命令提示符中：

    .. code-block:: console

       $ curl -sk https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/turtle_tf2_message_broadcaster.py -o turtle_tf2_message_broadcaster.py

    或在 PowerShell 中：

    .. code-block:: console

       $ curl https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/turtle_tf2_message_broadcaster.py -o turtle_tf2_message_broadcaster.py

打开该文件：

.. code-block:: python

   from geometry_msgs.msg import PointStamped
   from geometry_msgs.msg import Twist

   import rclpy
   from rclpy.node import Node

   from turtlesim.msg import Pose
   from turtlesim.srv import Spawn


   class PointPublisher(Node):

       def __init__(self):
           super().__init__('turtle_tf2_message_broadcaster')

           # 创建一个客户端，用于生成乌龟
           self.spawner = self.create_client(Spawn, 'spawn')
           self.turtle_spawning_service_ready = False
           self.turtle_spawned = False
           self.turtle_pose_cansubscribe = False

           self.timer = self.create_timer(1.0, self.on_timer)

       def on_timer(self):
           if self.turtle_spawning_service_ready:
               if self.turtle_spawned:
                   self.turtle_pose_cansubscribe = True
               else:
                   if self.result.done():
                       self.get_logger().info(
                           f'Successfully spawned {self.result.result().name}')
                       self.turtle_spawned = True
                   else:
                       self.get_logger().info('Spawn is not finished')
           else:
               if self.spawner.service_is_ready():
                   request = Spawn.Request()
                   request.name = 'turtle3'
                   request.x = 4.0
                   request.y = 2.0
                   request.theta = 0.0
                   self.result = self.spawner.call_async(request)
                   self.turtle_spawning_service_ready = True
               else:
                   self.get_logger().info('Service is not ready')

           if self.turtle_pose_cansubscribe:
               self.vel_pub = self.create_publisher(Twist, 'turtle3/cmd_vel', 10)
               self.sub = self.create_subscription(
                   Pose, 'turtle3/pose', self.handle_turtle_pose, 10)
               self.pub = self.create_publisher(
                   PointStamped, 'turtle3/turtle_point_stamped', 10)

       def handle_turtle_pose(self, msg):
           vel_msg = Twist()
           vel_msg.linear.x = 1.0
           vel_msg.angular.z = 1.0
           self.vel_pub.publish(vel_msg)

           ps = PointStamped()
           ps.header.stamp = self.get_clock().now().to_msg()
           ps.header.frame_id = 'world'
           ps.point.x = msg.x
           ps.point.y = msg.y
           ps.point.z = 0.0
           self.pub.publish(ps)


   def main():
       rclpy.init()
       node = PointPublisher()
       try:
           rclpy.spin(node)
       except KeyboardInterrupt:
           pass

       rclpy.shutdown()

1.1 理解代码
~~~~~~~~~~~~

首先，在 ``on_timer`` 回调函数中，当生成乌龟的服务已经就绪时，通过异步调用 turtlesim 的 ``Spawn`` 服务生成 ``turtle3``，并将其初始位置设置为 (4, 2, 0)：

.. code-block:: python

   request = Spawn.Request()
   request.name = 'turtle3'
   request.x = 4.0
   request.y = 2.0
   request.theta = 0.0
   self.result = self.spawner.call_async(request)

随后，节点发布 ``turtle3/cmd_vel`` 和 ``turtle3/turtle_point_stamped`` 话题，并订阅 ``turtle3/pose`` 话题。每当收到位姿消息时，都会调用 ``handle_turtle_pose``：

.. code-block:: python

   self.vel_pub = self.create_publisher(Twist, 'turtle3/cmd_vel', 10)
   self.sub = self.create_subscription(
       Pose, 'turtle3/pose', self.handle_turtle_pose, 10)
   self.pub = self.create_publisher(
       PointStamped, 'turtle3/turtle_point_stamped', 10)

最后，在 ``handle_turtle_pose`` 回调函数中，初始化 ``turtle3`` 的 ``Twist`` 消息并发布，使乌龟沿圆形轨迹移动。随后将收到的 ``Pose`` 消息填入 ``PointStamped`` 消息并发布：

.. code-block:: python

   vel_msg = Twist()
   vel_msg.linear.x = 1.0
   vel_msg.angular.z = 1.0
   self.vel_pub.publish(vel_msg)

   ps = PointStamped()
   ps.header.stamp = self.get_clock().now().to_msg()
   ps.header.frame_id = 'world'
   ps.point.x = msg.x
   ps.point.y = msg.y
   ps.point.z = 0.0
   self.pub.publish(ps)

1.2 编写启动文件
~~~~~~~~~~~~~~~~~

为了运行该演示，需要在 ``learning_tf2_py`` 功能包的 ``launch`` 子目录中创建名为 ``turtle_tf2_sensor_message_launch`` 的启动文件，扩展名可以为 ``.py``、``.xml`` 或 ``.yaml``：

.. tabs::

  .. group-tab:: Python

    .. literalinclude:: launch/turtle_tf2_sensor_message_launch.py
       :language: python

  .. group-tab:: XML

    .. literalinclude:: launch/turtle_tf2_sensor_message_launch.xml
       :language: xml

  .. group-tab:: YAML

    .. literalinclude:: launch/turtle_tf2_sensor_message_launch.yaml
       :language: yaml

1.3 添加入口点
~~~~~~~~~~~~~~

为了让 ``ros2 run`` 命令能够运行该节点，需要在 ``src/learning_tf2_py`` 目录中的 ``setup.py`` 添加入口点：

.. code-block:: python

   'turtle_tf2_message_broadcaster = learning_tf2_py.turtle_tf2_message_broadcaster:main',

1.4 添加数据文件
~~~~~~~~~~~~~~~~~

为了让 ``ros2 launch`` 命令能够找到启动文件，需要将启动文件添加到 ``setup.py`` 的数据文件列表中。

在 ``setup.py`` 文件顶部导入：

.. code-block:: python

   import os
   from glob import glob

在 ``data_files`` 列表中添加：

.. code-block:: python

   data_files=[
       # ...
       (os.path.join('share', package_name, 'launch'), glob('launch/*')),
   ],

1.5 构建
~~~~~~~~

在工作空间根目录运行 ``rosdep`` 检查缺失依赖：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

  .. group-tab:: macOS

    ``rosdep`` 仅在 Linux 上运行，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

  .. group-tab:: Windows

    ``rosdep`` 仅在 Linux 上运行，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

然后构建功能包：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ colcon build --packages-select learning_tf2_py

  .. group-tab:: macOS

    .. code-block:: console

       $ colcon build --packages-select learning_tf2_py

  .. group-tab:: Windows

    .. code-block:: console

       $ colcon build --merge-install --packages-select learning_tf2_py

2. 编写消息过滤器/监听器节点
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

现在，为了可靠地获取 ``turtle3`` 在 ``turtle1`` 坐标系中的连续 ``PointStamped`` 数据，需要创建消息过滤器/监听器节点。

进入前面教程创建的 ``learning_tf2_cpp`` :doc:`功能包 <./Writing-A-Tf2-Static-Broadcaster-Cpp>`。在 ``src/learning_tf2_cpp/src`` 目录中下载 ``turtle_tf2_message_filter.cpp``：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/turtle_tf2_message_filter.cpp

  .. group-tab:: macOS

    .. code-block:: console

       $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/turtle_tf2_message_filter.cpp

  .. group-tab:: Windows

    在 Windows 命令提示符中：

    .. code-block:: console

       $ curl -sk https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/turtle_tf2_message_filter.cpp -o turtle_tf2_message_filter.cpp

    或在 PowerShell 中：

    .. code-block:: console

       $ curl https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/turtle_tf2_message_filter.cpp -o turtle_tf2_message_filter.cpp

打开该文件：

.. code-block:: c++

   #include <chrono>
   #include <memory>
   #include <string>

   #include "geometry_msgs/msg/point_stamped.hpp"
   #include "message_filters/subscriber.h"
   #include "rclcpp/rclcpp.hpp"
   #include "tf2_ros/buffer.h"
   #include "tf2_ros/create_timer_ros.h"
   #include "tf2_ros/message_filter.h"
   #include "tf2_ros/transform_listener.h"
   #ifdef TF2_CPP_HEADERS
     #include "tf2_geometry_msgs/tf2_geometry_msgs.hpp"
   #else
     #include "tf2_geometry_msgs/tf2_geometry_msgs.h"
   #endif

   using namespace std::chrono_literals;

   class PoseDrawer : public rclcpp::Node
   {
   public:
     PoseDrawer()
     : Node("turtle_tf2_pose_drawer")
     {
       target_frame_ = this->declare_parameter<std::string>("target_frame", "turtle1");

       std::chrono::duration<int> buffer_timeout(1);

       tf2_buffer_ = std::make_shared<tf2_ros::Buffer>(this->get_clock());
       auto timer_interface = std::make_shared<tf2_ros::CreateTimerROS>(
         this->get_node_base_interface(),
         this->get_node_timers_interface());
       tf2_buffer_->setCreateTimerInterface(timer_interface);
       tf2_listener_ =
         std::make_shared<tf2_ros::TransformListener>(*tf2_buffer_);

       point_sub_.subscribe(this, "/turtle3/turtle_point_stamped");
       tf2_filter_ = std::make_shared<tf2_ros::MessageFilter<geometry_msgs::msg::PointStamped>>(
         point_sub_, *tf2_buffer_, target_frame_, 100,
         this->get_node_logging_interface(),
         this->get_node_clock_interface(), buffer_timeout);
       tf2_filter_->registerCallback(&PoseDrawer::msgCallback, this);
     }

   private:
     void msgCallback(const geometry_msgs::msg::PointStamped::SharedPtr point_ptr)
     {
       geometry_msgs::msg::PointStamped point_out;
       try {
         tf2_buffer_->transform(*point_ptr, point_out, target_frame_);
         RCLCPP_INFO(
           this->get_logger(),
           "Point of turtle3 in frame of turtle1: x:%f y:%f z:%f",
           point_out.point.x,
           point_out.point.y,
           point_out.point.z);
       } catch (const tf2::TransformException & ex) {
         RCLCPP_WARN(this->get_logger(), "Failure %s", ex.what());
       }
     }

     std::string target_frame_;
     std::shared_ptr<tf2_ros::Buffer> tf2_buffer_;
     std::shared_ptr<tf2_ros::TransformListener> tf2_listener_;
     message_filters::Subscriber<geometry_msgs::msg::PointStamped> point_sub_;
     std::shared_ptr<tf2_ros::MessageFilter<geometry_msgs::msg::PointStamped>> tf2_filter_;
   };

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<PoseDrawer>());
     rclcpp::shutdown();
     return 0;
   }

.. include:: ../../../_internal/Rclcpp-Convenience-Header-Note.rst

2.1 理解代码
~~~~~~~~~~~~

首先，需要包含 ``tf2_ros::MessageFilter`` 相关头文件，以及此前使用的 tf2 和 ROS 2 头文件。

.. code-block:: c++

   #include "geometry_msgs/msg/point_stamped.hpp"
   #include "message_filters/subscriber.h"
   #include "rclcpp/rclcpp.hpp"
   #include "tf2_ros/buffer.h"
   #include "tf2_ros/create_timer_ros.h"
   #include "tf2_ros/message_filter.h"
   #include "tf2_ros/transform_listener.h"

其次，需要持久保存 ``tf2_ros::Buffer``、``tf2_ros::TransformListener`` 和 ``tf2_ros::MessageFilter`` 实例：

.. code-block:: c++

   std::string target_frame_;
   std::shared_ptr<tf2_ros::Buffer> tf2_buffer_;
   std::shared_ptr<tf2_ros::TransformListener> tf2_listener_;
   message_filters::Subscriber<geometry_msgs::msg::PointStamped> point_sub_;
   std::shared_ptr<tf2_ros::MessageFilter<geometry_msgs::msg::PointStamped>> tf2_filter_;

第三，需要初始化 ROS 2 的 ``message_filters::Subscriber``，并指定订阅话题。随后使用该订阅对象初始化 ``tf2_ros::MessageFilter``。

``MessageFilter`` 构造函数中的其他重要参数包括 ``target_frame`` 和回调函数：

* ``target_frame`` 是目标坐标系。MessageFilter 会确保数据在能够转换到该目标坐标系后才调用回调。
* 回调函数是在所需变换已经可用时调用的函数。

.. code-block:: c++

   PoseDrawer()
   : Node("turtle_tf2_pose_drawer")
   {
     target_frame_ = this->declare_parameter<std::string>("target_frame", "turtle1");

     std::chrono::duration<int> buffer_timeout(1);

     tf2_buffer_ = std::make_shared<tf2_ros::Buffer>(this->get_clock());
     auto timer_interface = std::make_shared<tf2_ros::CreateTimerROS>(
       this->get_node_base_interface(),
       this->get_node_timers_interface());
     tf2_buffer_->setCreateTimerInterface(timer_interface);
     tf2_listener_ =
       std::make_shared<tf2_ros::TransformListener>(*tf2_buffer_);

     point_sub_.subscribe(this, "/turtle3/turtle_point_stamped");
     tf2_filter_ = std::make_shared<tf2_ros::MessageFilter<geometry_msgs::msg::PointStamped>>(
       point_sub_, *tf2_buffer_, target_frame_, 100,
       this->get_node_logging_interface(),
       this->get_node_clock_interface(), buffer_timeout);
     tf2_filter_->registerCallback(&PoseDrawer::msgCallback, this);
   }

最后，回调函数会在数据准备就绪时调用 ``tf2_buffer_->transform``，并将转换后的坐标输出到控制台：

.. code-block:: c++

   void msgCallback(const geometry_msgs::msg::PointStamped::SharedPtr point_ptr)
   {
     geometry_msgs::msg::PointStamped point_out;
     try {
       tf2_buffer_->transform(*point_ptr, point_out, target_frame_);
       RCLCPP_INFO(
         this->get_logger(),
         "Point of turtle3 in frame of turtle1: x:%f y:%f z:%f",
         point_out.point.x,
         point_out.point.y,
         point_out.point.z);
     } catch (const tf2::TransformException & ex) {
       RCLCPP_WARN(this->get_logger(), "Failure %s", ex.what());
     }
   }

2.2 添加依赖
~~~~~~~~~~~~

在构建 ``learning_tf2_cpp`` 功能包之前，需要在该功能包的 ``package.xml`` 中添加两个依赖项：

.. code-block:: xml

   <depend>message_filters</depend>
   <depend>tf2_geometry_msgs</depend>

2.3 配置 CMakeLists.txt
~~~~~~~~~~~~~~~~~~~~~~~~

在 ``CMakeLists.txt`` 中现有依赖项下面添加：

.. code-block:: cmake

   find_package(message_filters REQUIRED)
   find_package(tf2_geometry_msgs REQUIRED)

下面的代码用于处理不同 ROS 发行版之间的头文件差异：

.. code-block:: cmake

   if(TARGET tf2_geometry_msgs::tf2_geometry_msgs)
     get_target_property(_include_dirs tf2_geometry_msgs::tf2_geometry_msgs INTERFACE_INCLUDE_DIRECTORIES)
   else()
     set(_include_dirs ${tf2_geometry_msgs_INCLUDE_DIRS})
   endif()

   find_file(TF2_CPP_HEADERS
     NAMES tf2_geometry_msgs.hpp
     PATHS ${_include_dirs}
     NO_CACHE
     PATH_SUFFIXES tf2_geometry_msgs
   )

然后添加可执行程序，并命名为 ``turtle_tf2_message_filter``，之后可以使用 ``ros2 run`` 运行：

.. code-block:: cmake

   add_executable(turtle_tf2_message_filter src/turtle_tf2_message_filter.cpp)
   ament_target_dependencies(
     turtle_tf2_message_filter
     geometry_msgs
     message_filters
     rclcpp
     tf2
     tf2_geometry_msgs
     tf2_ros
   )

   if(EXISTS ${TF2_CPP_HEADERS})
     target_compile_definitions(turtle_tf2_message_filter PUBLIC -DTF2_CPP_HEADERS)
   endif()

最后添加 ``install(TARGETS ...)`` 部分：

.. code-block:: cmake

   install(TARGETS
     turtle_tf2_message_filter
     DESTINATION lib/${PROJECT_NAME})

2.4 构建
~~~~~~~~

在工作空间根目录运行 ``rosdep`` 检查依赖：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

  .. group-tab:: macOS

    ``rosdep`` 仅在 Linux 上运行，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

  .. group-tab:: Windows

    ``rosdep`` 仅在 Linux 上运行，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

然后重新构建功能包：

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

3. 运行
^^^^^^^

首先启动多个节点（包括 PointStamped 消息广播器节点），运行 ``turtle_tf2_sensor_message_launch`` 启动文件：

.. tabs::

  .. group-tab:: XML

    .. code-block:: console

       $ ros2 launch learning_tf2_py turtle_tf2_sensor_message_launch.xml

  .. group-tab:: YAML

    .. code-block:: console

       $ ros2 launch learning_tf2_py turtle_tf2_sensor_message_launch.yaml

  .. group-tab:: Python

    .. code-block:: console

       $ ros2 launch learning_tf2_py turtle_tf2_sensor_message_launch.py

此时会启动 turtlesim 窗口，其中有两只乌龟。``turtle3`` 沿圆形轨迹移动，而 ``turtle1`` 起初不会移动。

可以在另一个终端中运行 ``turtle_teleop_key``，控制 ``turtle1``：

.. code-block:: console

   $ ros2 run turtlesim turtle_teleop_key

.. image:: images/turtlesim_messagefilter.png

现在可以使用 ``ros2 topic echo`` 查看 ``turtle3/turtle_point_stamped`` 话题：

.. code-block:: console

   $ ros2 topic echo /turtle3/turtle_point_stamped
   header:
     stamp:
       sec: 1629877510
       nanosec: 902607040
     frame_id: world
   point:
     x: 4.989276885986328
     y: 3.073937177658081
     z: 0.0
   ---

当演示运行时，打开另一个终端并运行消息过滤器/监听器节点：

.. code-block:: console

   $ ros2 run learning_tf2_cpp turtle_tf2_message_filter

应该能看到类似以下输出：

.. code-block:: console

   [INFO] [turtle_tf2_pose_drawer]: Point of turtle3 in frame of turtle1: x:-6.493231 y:-2.961614 z:0.000000
   [INFO] [turtle_tf2_pose_drawer]: Point of turtle3 in frame of turtle1: x:-6.472169 y:-3.004742 z:0.000000
   [INFO] [turtle_tf2_pose_drawer]: Point of turtle3 in frame of turtle1: x:-6.479420 y:-2.990479 z:0.000000

总结
----

本教程介绍了如何在 tf2 中使用传感器数据和消息。

具体来说，你学习了如何在话题上发布 ``PointStamped`` 消息，以及如何订阅该话题，并使用 ``tf2_ros::MessageFilter`` 将 ``PointStamped`` 消息转换到目标坐标系。
