.. redirect-from::

    Tutorials/Tf2/Adding-A-Frame-Cpp

tf2 添加坐标系（C++）
=====================

**目标：** 学习如何向 tf2 添加额外坐标系。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 3
   :local:

背景
----

在之前的教程中，我们通过编写 :doc:`tf2 广播器 <./Writing-A-Tf2-Broadcaster-Cpp>` 和 :doc:`tf2 监听器 <Writing-A-Tf2-Listener-Cpp>` 重现了海龟演示。本教程介绍如何向变换树添加额外的固定坐标系和动态坐标系。

对于许多坐标变换任务，使用局部坐标系思考会更容易。例如，在激光雷达中心建立坐标系，可以更直观地理解激光扫描测量值。tf2 允许为系统中的每个传感器、连杆或关节定义局部坐标系。当从一个坐标系变换到另一个坐标系时，tf2 会自动处理所有中间坐标系变换。

tf2 变换树
----------

tf2 使用树结构组织坐标系，因此不允许坐标系结构中出现闭环。每个坐标系只能有一个父坐标系，但可以有多个子坐标系。

当前 tf2 树包含三个坐标系：``world``、``turtle1`` 和 ``turtle2``。两个海龟坐标系都是 ``world`` 的子坐标系。若要添加新坐标系，必须选择现有坐标系之一作为父坐标系，新坐标系则成为其子坐标系。

.. image:: images/turtlesim_frames.png

任务
----

1. 编写固定坐标系广播器
^^^^^^^^^^^^^^^^^^^^^^^

在海龟示例中，我们添加一个名为 ``carrot1`` 的新坐标系，它是 ``turtle1`` 的子坐标系，并作为第二只海龟的目标位置。

进入之前教程创建的 ``learning_tf2_cpp`` 功能包，在 ``src`` 目录下载固定坐标系广播器：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/fixed_frame_tf2_broadcaster.cpp

   .. group-tab:: macOS

      .. code-block:: console

         $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/fixed_frame_tf2_broadcaster.cpp

   .. group-tab:: Windows

      .. code-block:: console

         $ curl -sk https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/fixed_frame_tf2_broadcaster.cpp -o fixed_frame_tf2_broadcaster.cpp

打开 ``fixed_frame_tf2_broadcaster.cpp``，写入以下完整代码：

.. code-block:: c++

   #include <memory>

   #include "geometry_msgs/msg/transform_stamped.hpp"
   #include "rclcpp/rclcpp.hpp"
   #include "tf2_ros/static_transform_broadcaster.hpp"

   class FixedFrameBroadcaster : public rclcpp::Node
   {
   public:
     FixedFrameBroadcaster()
     : Node("fixed_frame_tf2_broadcaster")
     {
       tf_static_broadcaster_ =
         std::make_shared<tf2_ros::StaticTransformBroadcaster>(this);

       geometry_msgs::msg::TransformStamped t;
       t.header.stamp = this->get_clock()->now();
       t.header.frame_id = "turtle1";
       t.child_frame_id = "carrot1";
       t.transform.translation.x = 0.0;
       t.transform.translation.y = 2.0;
       t.transform.translation.z = 0.0;
       t.transform.rotation.x = 0.0;
       t.transform.rotation.y = 0.0;
       t.transform.rotation.z = 0.0;
       t.transform.rotation.w = 1.0;

       tf_static_broadcaster_->sendTransform(t);
     }

   private:
     std::shared_ptr<tf2_ros::StaticTransformBroadcaster> tf_static_broadcaster_;
   };

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<FixedFrameBroadcaster>());
     rclcpp::shutdown();
     return 0;
   }

该固定坐标系使用 ``tf2_ros::StaticTransformBroadcaster``，并在构造函数中发布一次。对于相对于父坐标系位姿不会变化的坐标系，应使用静态广播器。对于随时间变化的坐标系，应使用 ``tf2_ros::TransformBroadcaster`` 定期发布。

1.1 理解代码
~~~~~~~~~~~~

代码创建了从父坐标系 ``turtle1`` 到子坐标系 ``carrot1`` 的变换。相对于 ``turtle1``，``carrot1`` 在 y 轴方向偏移 2 米。

.. code-block:: cpp

   geometry_msgs::msg::TransformStamped t;
   t.header.stamp = this->get_clock()->now();
   t.header.frame_id = "turtle1";
   t.child_frame_id = "carrot1";
   t.transform.translation.x = 0.0;
   t.transform.translation.y = 2.0;
   t.transform.translation.z = 0.0;

1.2 修改 CMakeLists.txt
~~~~~~~~~~~~~~~~~~~~~~~

返回 ``learning_tf2_cpp`` 目录，打开 ``CMakeLists.txt``，添加可执行程序：

.. code-block:: cmake

   add_executable(fixed_frame_tf2_broadcaster src/fixed_frame_tf2_broadcaster.cpp)
   ament_target_dependencies(
     fixed_frame_tf2_broadcaster
     geometry_msgs
     rclcpp
     tf2_ros
   )

   install(TARGETS
     fixed_frame_tf2_broadcaster
     DESTINATION lib/${PROJECT_NAME})

1.3 编写启动文件
~~~~~~~~~~~~~~~~

在 ``src/learning_tf2_cpp/launch`` 目录中创建 ``turtle_tf2_fixed_frame_demo_launch`` 启动文件，扩展名可为 ``.py``、``.xml`` 或 ``.yaml``。

.. tabs::

  .. group-tab:: Python

    .. literalinclude:: launch/turtle_tf2_fixed_frame_demo_launch.py
        :language: python

  .. group-tab:: XML

    .. literalinclude:: launch/turtle_tf2_fixed_frame_demo_launch.xml
        :language: xml

  .. group-tab:: YAML

    .. literalinclude:: launch/turtle_tf2_fixed_frame_demo_launch.yaml
        :language: yaml

启动文件会导入所需功能包，并创建 ``demo_nodes`` 变量以保存前面教程启动文件中创建的节点。最后，通过 ``fixed_frame_tf2_broadcaster`` 节点，将固定的 ``carrot1`` 坐标系添加到 turtlesim 世界中。

1.4 构建
~~~~~~~~

在工作空间根目录检查缺失依赖：

.. code-block:: console

   $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

macOS 和 Windows 上 rosdep 不可用，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

构建功能包：

.. code-block:: console

   $ colcon build --packages-select learning_tf2_cpp

Windows 使用：

.. code-block:: console

   $ colcon build --merge-install --packages-select learning_tf2_cpp

打开新终端，进入工作空间根目录并 source 环境：

.. code-block:: console

   $ . install/setup.bash

Windows 命令提示符使用 ``call install\setup.bat``；PowerShell 使用 ``.\install\setup.ps1``。

1.5 运行
~~~~~~~~

启动演示：

.. code-block:: console

   $ ros2 launch learning_tf2_cpp turtle_tf2_fixed_frame_demo_launch.xml

你应该能看到变换树中出现新的 ``carrot1`` 坐标系。

.. image:: images/turtlesim_frames_carrot.png

移动第一只海龟时，行为与上一个教程相同，因为添加额外坐标系不会改变其他坐标系，监听器仍然使用之前定义的坐标系。

如果希望第二只海龟跟随 carrot，而不是第一只海龟，需要修改 ``target_frame``。可以在命令行传入参数：

.. code-block:: console

   $ ros2 launch learning_tf2_cpp turtle_tf2_fixed_frame_demo_launch.xml target_frame:=carrot1

也可以修改启动文件，在 ``launch_arguments`` 中添加 ``'target_frame': 'carrot1'``：

.. code-block:: python

   def generate_launch_description():
       demo_nodes = IncludeLaunchDescription(
           ...,
           launch_arguments={'target_frame': 'carrot1'}.items(),
       )

重新构建并启动后，第二只海龟就会跟随 carrot，而不是第一只海龟。

.. image:: images/carrot_static.png

2. 编写动态坐标系广播器
^^^^^^^^^^^^^^^^^^^^^^^

本教程发布的额外坐标系是固定坐标系，相对于父坐标系不会随时间变化。如果希望发布移动坐标系，可以让广播器随时间改变坐标系位姿。

进入 ``learning_tf2_cpp`` 的 ``src`` 目录，下载动态坐标系广播器：

.. code-block:: console

   $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/dynamic_frame_tf2_broadcaster.cpp

打开 ``dynamic_frame_tf2_broadcaster.cpp``，写入以下完整代码：

.. code-block:: c++

   #include <chrono>
   #include <functional>
   #include <memory>

   #include "geometry_msgs/msg/transform_stamped.hpp"
   #include "rclcpp/rclcpp.hpp"
   #include "tf2_ros/transform_broadcaster.h"

   using namespace std::chrono_literals;

   const double PI = 3.141592653589793238463;

   class DynamicFrameBroadcaster : public rclcpp::Node
   {
   public:
     DynamicFrameBroadcaster()
     : Node("dynamic_frame_tf2_broadcaster")
     {
       tf_broadcaster_ = std::make_shared<tf2_ros::TransformBroadcaster>(this);
       timer_ = this->create_wall_timer(
         100ms, std::bind(&DynamicFrameBroadcaster::broadcast_timer_callback, this));
     }

   private:
     void broadcast_timer_callback()
     {
       rclcpp::Time now = this->get_clock()->now();
       double x = now.seconds() * PI;

       geometry_msgs::msg::TransformStamped t;
       t.header.stamp = now;
       t.header.frame_id = "turtle1";
       t.child_frame_id = "carrot1";
       t.transform.translation.x = 10 * sin(x);
       t.transform.translation.y = 10 * cos(x);
       t.transform.translation.z = 0.0;
       t.transform.rotation.x = 0.0;
       t.transform.rotation.y = 0.0;
       t.transform.rotation.z = 0.0;
       t.transform.rotation.w = 1.0;

       tf_broadcaster_->sendTransform(t);
     }

     rclcpp::TimerBase::SharedPtr timer_;
     std::shared_ptr<tf2_ros::TransformBroadcaster> tf_broadcaster_;
   };

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<DynamicFrameBroadcaster>());
     rclcpp::shutdown();
     return 0;
   }

2.1 理解代码
~~~~~~~~~~~~

与固定坐标系不同，动态坐标系需要持续发布变换。本例创建一个 100 毫秒周期定时器，每次回调时获取当前 ROS 时间，并根据时间计算坐标偏移：

.. code-block:: c++

   rclcpp::Time now = this->get_clock()->now();
   double x = now.seconds() * PI;

   t.transform.translation.x = 10 * sin(x);
   t.transform.translation.y = 10 * cos(x);

由于 x 和 y 偏移量会随时间变化，``carrot1`` 就会相对于 ``turtle1`` 沿圆形轨迹移动。每次回调都会通过 ``TransformBroadcaster`` 发布最新变换。

2.2 修改 CMakeLists.txt
~~~~~~~~~~~~~~~~~~~~~~~

添加动态广播器可执行程序：

.. code-block:: cmake

   add_executable(dynamic_frame_tf2_broadcaster src/dynamic_frame_tf2_broadcaster.cpp)
   ament_target_dependencies(
     dynamic_frame_tf2_broadcaster
     geometry_msgs
     rclcpp
     tf2_ros
   )

   install(TARGETS
     dynamic_frame_tf2_broadcaster
     DESTINATION lib/${PROJECT_NAME})

2.3 编写启动文件
~~~~~~~~~~~~~~~~

在 ``src/learning_tf2_cpp/launch`` 中创建 ``turtle_tf2_dynamic_frame_demo_launch``，可使用 Python、XML 或 YAML 格式。

.. tabs::

  .. group-tab:: Python

    .. literalinclude:: launch/turtle_tf2_dynamic_frame_demo_launch.py
        :language: python

  .. group-tab:: XML

    .. literalinclude:: launch/turtle_tf2_dynamic_frame_demo_launch.xml
        :language: xml

  .. group-tab:: YAML

    .. literalinclude:: launch/turtle_tf2_dynamic_frame_demo_launch.yaml
        :language: yaml

2.4 构建
~~~~~~~~

在工作空间根目录检查缺失依赖：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

         $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

   .. group-tab:: macOS

      rosdep 仅在 Linux 上运行，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

   .. group-tab:: Windows

      rosdep 仅在 Linux 上运行，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

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

         $ call install\\setup.bat

      或在 PowerShell 中：

      .. code-block:: console

         $ .\\install\\setup.ps1

2.5 运行
~~~~~~~~

启动动态坐标系演示：

.. code-block:: console

   $ ros2 launch learning_tf2_cpp turtle_tf2_dynamic_frame_demo_launch.xml

也可以使用 ``.py`` 或 ``.yaml`` 扩展名。

此时第二只海龟应跟随不断变化位置的 carrot。

.. image:: images/carrot_dynamic.png

总结
----

本教程介绍了 tf2 变换树的结构和特性，说明了使用局部坐标系进行思考的优势，并展示了如何为局部坐标系添加额外的固定坐标系和动态坐标系。
