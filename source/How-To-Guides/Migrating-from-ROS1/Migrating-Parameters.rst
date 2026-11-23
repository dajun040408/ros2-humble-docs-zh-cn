ROS 1 参数迁移
==============

.. redirect-from::

   Guides/Parameters-YAML-files-migration-guide
   Tutorials/Parameters-YAML-files-migration-guide
   How-To-Guides/Parameters-YAML-files-migration-guide

.. contents:: 目录
   :depth: 2
   :local:

在 ROS 1 中，参数关联到中央服务器，节点可以通过网络 API 在运行时获取参数。
在 ROS 2 中，参数按节点管理，并通过 ROS 服务在运行时进行配置。

* 系统模型细节请参阅 ROS 2 参数设计文档：https://design.ros2.org/articles/ros_parameters.html
* CLI 工具的工作方式及其与 ROS 1 工具的区别，请参阅 ROS 2 参数 CLI 教程。

全局参数服务器
--------------

在 ROS 1 中，roscore 充当全局参数黑板，所有节点都可以从中获取和设置参数。
由于 ROS 2 中不存在中央 roscore，因此这一功能不再以相同方式提供。
ROS 2 推荐使用按节点管理的参数，使参数与使用它们的节点紧密关联。

如果仍然需要全局参数黑板，可以为此创建专用节点。
ROS 2 在 ros-{DISTRO}-demo-nodes-cpp 软件包中提供了名为 parameter_blackboard 的节点，可以通过以下命令运行：

.. code-block:: console

   $ ros2 run demo_nodes_cpp parameter_blackboard

该节点源代码位于 https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/demo_nodes_cpp/src/parameters/parameter_blackboard.cpp。

迁移 YAML 参数文件
------------------

本指南介绍如何将 ROS 1 参数文件调整为 ROS 2 格式。

YAML 文件示例
^^^^^^^^^^^^^

ROS 1 和 ROS 2 都使用 YAML 编写参数文件。
ROS 2 的主要区别在于，必须使用节点名称指定参数所属节点。
除了完整限定的节点名称外，还需要使用 ros__parameters 键标识该节点参数的起始位置。

例如，下面是 ROS 1 中的参数文件：

.. code-block:: yaml

   lidar_name: foo
   lidar_id: 10
   ports: [11312, 11311, 21311]
   debug: true

假设前两个参数属于 /lidar_ns/lidar_node_name 节点，下一个参数属于 /imu 节点，而最后一个参数需要同时设置到这两个节点上。对应的 ROS 2 参数文件如下：

.. code-block:: yaml

   /lidar_ns:
     lidar_node_name:
       ros__parameters:
         lidar_name: foo
         id: 10
   imu:
     ros__parameters:
       ports: [2438, 2439, 2440]
   /**:
     ros__parameters:
       debug: true

通配符 /** 表示参数 debug 应设置到任意命名空间中的所有节点。

功能对等性
^^^^^^^^^^

ROS 1 参数文件中的部分功能在 ROS 2 中尚不存在：

- 暂不支持列表中包含混合类型，参见 https://github.com/ros2/rcl/issues/463。
- 不支持 deg 和 rad 替换语法。

参数原子操作
------------

将 ROS 1 中的参数组迁移到 ROS 2 时，需要注意两者的重要区别。
在 ROS 1 中，dynamic_reconfigure 会以原子方式处理参数组，即一次重新配置请求中的所有参数都在同一个回调中处理。
在 ROS 2 中，set_parameters 服务会逐个处理参数，这可能导致多次调用回调函数。

为了在迁移时保持 dynamic_reconfigure 的原子行为，应使用 set_parameters_atomically 服务。该服务会将所有参数作为一个整体进行校验和应用。如果任意参数未通过校验，则不会更新任何参数。
