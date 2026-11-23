.. redirect-from::

  Features

.. _Features:

功能特性状态
============

以下列出了当前 ROS 2 发行版提供的功能。除非另有说明，这些功能均适用于所有受支持的平台（Ubuntu 22.04 Jammy、Windows 10）、DDS 实现（eProsima Fast DDS、RTI Connext DDS 和 Eclipse Cyclone DDS）以及客户端编程语言库（C++ 和 Python）。

未来计划开发的功能，请参阅 :doc:`路线图 <Roadmap>`。

.. list-table::
   :header-rows: 1

   * - 功能
     - 链接
     - 补充说明
   * - 基于 DDS 的发现、传输和序列化
     - `设计文章 <https://design.ros2.org/articles/ros_on_dds.html>`_
     -
   * - 支持多种 DDS 实现，并可在运行时选择
     - :doc:`概念 <../Concepts/Intermediate/About-Different-Middleware-Vendors>`、:doc:`使用指南 <../How-To-Guides/Working-with-multiple-RMW-implementations>`
     - 目前完整支持 Eclipse Cyclone DDS、eProsima Fast DDS 和 RTI Connext DDS。
   * - 通用核心客户端库，并由特定编程语言的客户端库封装
     - :doc:`详细说明 <../Concepts/Basic/About-Client-Libraries>`
     -
   * - 通过话题进行发布/订阅
     - `示例代码 <https://github.com/ros2/examples>`_、`设计文章 <https://design.ros2.org/articles/topic_and_service_names.html>`_
     -
   * - 客户端和服务
     - `示例代码 <https://github.com/ros2/examples>`_
     -
   * - 设置/获取参数
     - `示例代码 <https://github.com/ros2/demos/tree/0.5.1/demo_nodes_cpp/src/parameters>`_
     -
   * - ROS 1 与 ROS 2 通信桥接
     - `教程 <https://github.com/ros2/ros1_bridge/blob/master/README.md>`_
     - 支持话题和服务，暂不支持动作。
   * - 用于处理非理想网络的服务质量（QoS）设置
     - :doc:`演示 <../Tutorials/Demos/Quality-of-Service>`
     -
   * - 使用相同 API 支持进程间和进程内通信
     - :doc:`演示 <../Tutorials/Demos/Intra-Process-Communication>`
     - 目前仅支持 C++。
   * - 在编译、链接、加载或运行时组合节点组件
     - :doc:`演示 <../Tutorials/Intermediate/Composition>`
     - 目前仅支持 C++。
   * - 同一节点中支持多个执行器（回调组级别）
     - `演示 <https://github.com/ros2/examples/tree/{DISTRO}/rclcpp/executors/cbg_executor>`_
     - 仅支持 C++。
   * - 支持具有受管理生命周期的节点
     - :doc:`演示 <../Tutorials/Demos/Managed-Nodes>`
     - 目前仅支持 C++。
   * - DDS-Security 支持
     - `演示 <https://github.com/ros2/sros2>`_
     -
   * - 基于可扩展框架的命令行内省工具
     - :doc:`概念 <../Concepts/Basic/About-Command-Line-Tools>`
     -
   * - 用于协调多个节点的启动系统
     - :doc:`教程 <../Tutorials/Intermediate/Launch/Launch-system>`
     -
   * - 节点和话题的命名空间支持
     - `设计文章 <https://design.ros2.org/articles/topic_and_service_names.html>`_
     -
   * - ROS 名称的静态重映射
     - :doc:`使用指南 <../How-To-Guides/Node-arguments>`
     -
   * - 完整 ROS 2 移动机器人的演示
     - `演示 <https://github.com/ros2/turtlebot2_demo>`_
     -
   * - 初步支持实时程序
     - :doc:`演示 <../Tutorials/Demos/Real-Time-Programming>`、:doc:`演示 <../Tutorials/Advanced/Allocator-Template-Tutorial>`
     - 仅支持 Linux，不支持 Fast RTPS。
   * - 初步支持裸机微控制器
     - `Wiki <https://github.com/ros2/freertps/wiki>`_
     -
   * - 内容过滤订阅
     - :doc:`演示 <../Tutorials/Demos/Content-Filtering-Subscription>`
     - 目前仅支持 C++。

除了平台核心功能外，ROS 的主要影响力还来自其丰富的软件包。以下是最新发行版中一些重要的软件包：

* `gazebo_ros_pkgs <https://index.ros.org/r/gazebo_ros_pkgs/>`_
* `image_transport <https://index.ros.org/r/image_common>`_
* `navigation2 <https://index.ros.org/r/navigation2/>`_
* `rosbag2 <https://index.ros.org/r/rosbag2/>`_
* `RQt <https://index.ros.org/r/rqt/>`_
* `RViz2 <https://index.ros.org/r/rviz/>`_
