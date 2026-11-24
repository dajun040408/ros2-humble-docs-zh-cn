.. redirect-from::

    Topic-Statistics-Tutorial
    Tutorials/Topics/Topic-Statistics-Tutorial

启用话题统计信息（C++）
=======================

**目标：** 启用 ROS 2 话题统计功能，并查看发布的统计数据。

**教程级别：** 高级

**预计时间：** 10 分钟

.. contents:: 目录
   :local:

背景
----

本教程简要介绍如何在 ROS 2 中启用话题统计，并使用命令行工具查看发布的统计输出。相关工具请参阅 :doc:`ros2 topic <../../Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics>`。

ROS 2 提供对订阅者接收消息统计信息的集成测量功能，称为 Topic Statistics（话题统计）。

启用订阅者的话题统计后，可以分析系统性能，或使用统计数据帮助诊断当前存在的问题。

更多详情请参阅 :doc:`话题统计概念页面 <../../../Concepts/Intermediate/About-Topic-Statistics>`。

前置条件
--------

需要安装 ROS 2（二进制或源码均可）。

此前的教程已经介绍了如何 :doc:`创建工作空间 <../../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace>`、:doc:`创建功能包 <../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>`，以及创建 :doc:`C++ 发布者和订阅者 <../../Beginner-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber>`。

本教程假设仍然保留此前创建的 cpp_pubsub 功能包。

任务
----

1. 编写启用统计功能的订阅者节点
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

进入此前教程创建的 ros2_ws/src/cpp_pubsub/src 目录，并下载示例订阅者代码：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

            $ wget -O member_function_with_topic_statistics.cpp https://raw.githubusercontent.com/ros2/examples/{REPOS_FILE_BRANCH}/rclcpp/topics/minimal_subscriber/member_function_with_topic_statistics.cpp

   .. group-tab:: macOS

      .. code-block:: console

            $ wget -O member_function_with_topic_statistics.cpp https://raw.githubusercontent.com/ros2/examples/{REPOS_FILE_BRANCH}/rclcpp/topics/minimal_subscriber/member_function_with_topic_statistics.cpp

   .. group-tab:: Windows

      右键点击以下链接并选择“另存为”，文件名设为 publisher_member_function.cpp：

      https://raw.githubusercontent.com/ros2/examples/{REPOS_FILE_BRANCH}/rclcpp/topics/minimal_subscriber/member_function_with_topic_statistics.cpp

现在会出现 member_function_with_topic_statistics.cpp 文件。使用文本编辑器打开该文件。

订阅选项中可以通过 topic_stats_options.state 启用话题统计。统计数据会通过统计话题发布，可使用 ros2 topic list 查看。

2. 构建并运行
^^^^^^^^^^^^^

在 cpp_pubsub 功能包中更新 CMakeLists.txt，将该源文件添加为可执行程序，并确保已查找 rclcpp 和 std_msgs 依赖。

在工作空间根目录构建：

.. code-block:: console

   $ colcon build --packages-select cpp_pubsub

source 工作空间后运行订阅者节点，并在另一个终端运行发布者节点。随后检查话题列表，查看统计消息：

.. code-block:: console

   $ ros2 topic list

话题统计消息包含订阅接收消息的统计信息，例如消息年龄（message age）和消息周期（message period）。可以通过 ros2 topic echo 查看对应统计话题的数据。
