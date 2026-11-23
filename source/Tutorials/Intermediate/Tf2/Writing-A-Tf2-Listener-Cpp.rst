.. redirect-from::

    Tutorials/Tf2/Writing-A-Tf2-Listener-Cpp

编写监听器（C++）
=================

**目标：** 学习如何使用 tf2 监听坐标变换。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程继续使用 :doc:§tf2 入门 <./Introduction-To-Tf2>§ 和 :doc:§C++ 广播器教程 <./Writing-A-Tf2-Broadcaster-Cpp>§ 中创建的 §learning_tf2_cpp§ 功能包。广播器将海龟位姿发布到 tf2，本教程将编写监听器，查询并使用这些变换。

任务
----

1. 编写监听器节点
^^^^^^^^^^^^^^^^^

在 §src/learning_tf2_cpp/src§ 中创建或下载 §turtle_tf2_listener.cpp§。监听器需要创建 §tf2_ros::Buffer§ 保存接收到的变换，并创建 §tf2_ros::TransformListener§ 接收变换数据。

.. code-block:: cpp

   tf_buffer_ = std::make_unique<tf2_ros::Buffer>(this->get_clock());
   tf_listener_ = std::make_shared<tf2_ros::TransformListener>(*tf_buffer_);

查询变换时调用 §lookupTransform()§：

.. code-block:: cpp

   geometry_msgs::msg::TransformStamped t;
   try {
     t = tf_buffer_->lookupTransform(
       toFrameRel,
       fromFrameRel,
       tf2::TimePointZero);
   } catch (const tf2::TransformException & ex) {
     RCLCPP_INFO(
       this->get_logger(), "Could not transform %s to %s: %s",
       fromFrameRel.c_str(), toFrameRel.c_str(), ex.what());
     return;
   }

§lookupTransform()§ 接受目标坐标系、源坐标系和查询时间。§tf2::TimePointZero§ 表示获取缓冲区中最新可用的变换。若变换尚不可用或查询失败，会抛出 §tf2::TransformException§，因此应使用 try/catch 处理异常。

2. 更新 CMakeLists.txt
^^^^^^^^^^^^^^^^^^^^^^

为监听器可执行程序添加依赖并安装：

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

   install(TARGETS
     turtle_tf2_listener
     DESTINATION lib/${PROJECT_NAME})

3. 运行演示
^^^^^^^^^^^

构建 §learning_tf2_cpp§，source 工作空间后运行对应启动文件。启动后，广播器会发布海龟位姿，监听器通过 tf2 缓冲区查询变换，并使用查询结果控制第二只海龟。

.. code-block:: console

   $ colcon build --packages-select learning_tf2_cpp
   $ . install/setup.bash
   $ ros2 launch learning_tf2_cpp turtle_tf2_demo_launch.py

总结
----

本教程介绍了如何使用 §tf2_ros::Buffer§ 和 §tf2_ros::TransformListener§ 接收并查询变换，以及如何使用 §lookupTransform()§ 获取最新变换。
