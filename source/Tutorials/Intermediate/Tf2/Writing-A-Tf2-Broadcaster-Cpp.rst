.. redirect-from::

    Tutorials/Tf2/Writing-A-Tf2-Broadcaster-Cpp

编写广播器（C++）
=================

**目标：** 学习如何向 tf2 广播机器人的状态。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程将与后续监听器教程一起，重现 :doc:§tf2 入门 <./Introduction-To-Tf2>§ 中的演示。之后还会扩展超时查询和时间旅行等高级 tf2 功能。

前置条件
--------

需要具备 ROS 2 基础知识，并完成 :doc:§tf2 入门教程 <./Introduction-To-Tf2>§ 和 :doc:§C++ 静态广播器教程 <./Writing-A-Tf2-Static-Broadcaster-Cpp>§。本教程使用之前创建的 §learning_tf2_cpp§ 功能包。

任务
----

1. 编写广播器节点
^^^^^^^^^^^^^^^^^

在 §src/learning_tf2_cpp/src§ 目录下载示例代码：

.. code-block:: console

   $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_cpp/src/turtle_tf2_broadcaster.cpp

Windows 可以使用 §curl§ 下载。广播器订阅海龟位姿，并将位姿发布为从 §world§ 到海龟坐标系的变换。

.. code-block:: cpp

   void handle_turtle_pose(const turtlesim::msg::Pose & msg)
   {
     geometry_msgs::msg::TransformStamped t;
     t.header.stamp = this->get_clock()->now();
     t.header.frame_id = "world";
     t.child_frame_id = turtle_name_;
     t.transform.translation.x = msg.x;
     t.transform.translation.y = msg.y;
     t.transform.translation.z = 0.0;

     tf2::Quaternion q;
     q.setRPY(0, 0, msg.theta);
     t.transform.rotation.x = q.x();
     t.transform.rotation.y = q.y();
     t.transform.rotation.z = q.z();
     t.transform.rotation.w = q.w();

     tf_broadcaster_->sendTransform(t);
   }

回调函数读取海龟位姿消息，将其转换为 §TransformStamped§。海龟只在二维平面移动，因此 z 平移为 0；旋转只绕 z 轴发生，因此使用 §setRPY(0, 0, msg.theta)§ 计算四元数。最后调用 §sendTransform()§ 发布变换。

1.1 配置 CMakeLists.txt
~~~~~~~~~~~~~~~~~~~~~~~

为可执行程序添加依赖并安装：

.. code-block:: cmake

   add_executable(turtle_tf2_broadcaster src/turtle_tf2_broadcaster.cpp)
   ament_target_dependencies(
     turtle_tf2_broadcaster
     geometry_msgs
     rclcpp
     tf2
     tf2_ros
     turtlesim
   )

   install(TARGETS
     turtle_tf2_broadcaster
     DESTINATION lib/${PROJECT_NAME})

2. 编写启动文件
^^^^^^^^^^^^^^^

在 §src/learning_tf2_cpp/launch§ 目录创建 §turtle_tf2_demo_launch§，扩展名可以是 §.py§、§.xml§ 或 §.yaml§。

.. tabs::

  .. group-tab:: XML

    .. literalinclude:: launch/turtle_tf2_demo_launch.xml
        :language: xml

  .. group-tab:: YAML

    .. literalinclude:: launch/turtle_tf2_demo_launch.yaml
        :language: yaml

  .. group-tab:: Python

    .. literalinclude:: launch/turtle_tf2_demo_launch.py
        :language: python

3. 构建
^^^^^^^

在工作空间根目录检查依赖：

.. code-block:: console

   $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

macOS 和 Windows 上 rosdep 不可用，需要自行安装 §geometry_msgs§ 和 §turtlesim§ 依赖。

构建功能包：

.. code-block:: console

   $ colcon build --packages-select learning_tf2_cpp

Windows 使用 §--merge-install§。打开新终端并 source 工作空间环境。

4. 运行
^^^^^^^

运行启动文件：

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

在第二个终端运行键盘控制节点：

.. code-block:: console

   $ ros2 run turtlesim turtle_teleop_key

此时 turtlesim 仿真启动，并显示一只可以控制的海龟。

.. image:: images/turtlesim_broadcast.png

使用 §tf2_echo§ 检查海龟位姿是否已经广播到 tf2：

.. code-block:: console

   $ ros2 run tf2_ros tf2_echo world turtle1

该命令会持续显示第一只海龟的位姿。使用方向键移动海龟，终端会输出时间戳、平移和四元数旋转信息。

此时查询 §world§ 到 §turtle2§ 的变换不会有结果，因为第二只海龟尚未创建。后续教程创建第二只海龟后，其位姿也会被广播到 tf2。

总结
----

本教程介绍了如何将机器人的位姿广播到 tf2，以及如何使用 §tf2_echo§ 检查变换。若要使用广播到 tf2 的变换，请继续学习 :doc:§创建 tf2 监听器 <./Writing-A-Tf2-Listener-Cpp>§。
