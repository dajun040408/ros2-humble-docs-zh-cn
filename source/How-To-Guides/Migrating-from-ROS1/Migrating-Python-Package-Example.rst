ROS 1 Python 功能包迁移示例
============================

本指南展示如何将一个示例 Python 功能包从 ROS 1 迁移到 ROS 2。

.. contents:: 目录
   :depth: 2
   :local:

前置条件
--------

需要一个可正常工作的 ROS 2 安装环境，例如 :doc:`ROS {DISTRO} <../../Installation>`。本指南不需要安装 ROS 1，因为迁移后将使用 ROS 2 的构建工具 `colcon`，而不是 `catkin`。

ROS 1 示例
----------

示例功能包名为 `talker_py`，包含节点 `talker_py_node`。创建 colcon 工作空间：

.. code-block:: console

   $ mkdir -p ~/ros2_talker_py/src

在 `src/talker_py` 中创建 `package.xml`、`CMakeLists.txt`、Python 源码、脚本和 `setup.py`。

ROS 1 的 `package.xml` 依赖 `catkin`、`rospy` 和 `std_msgs`。Python 节点通过 `rospy.init_node()` 初始化节点，使用 `rospy.Publisher` 发布 `std_msgs/String` 消息，并通过 `rospy.Rate` 控制发布频率。

迁移 package.xml
----------------

迁移时先修改构建系统文件，以便在迁移过程中逐步构建和运行代码。首先修改 `package.xml`。

ROS 2 不使用 `catkin`，因此删除：

.. code-block:: xml

   <buildtool_depend>catkin</buildtool_depend>

ROS 2 使用 `rclpy` 替代 `rospy`，因此将相关依赖改为 `rclpy`。消息依赖 `std_msgs` 保持不变。

对于纯 Python 功能包，构建类型应设置为 `ament_python`：

.. code-block:: xml

   <export>
     <build_type>ament_python</build_type>
   </export>

迁移 Python 代码
----------------

ROS 1 使用 `rospy.init_node()` 初始化节点，ROS 2 使用 `rclpy.init()` 和 `rclpy.create_node()`：

.. code-block:: python

   # ROS 1
   rospy.init_node('talker')

   # ROS 2
   rclpy.init(args=None)
   node = rclpy.create_node('talker')

发布者从 `rospy.Publisher` 迁移为 `node.create_publisher()`，日志使用 `node.get_logger()`，循环运行状态使用 `rclpy.ok()`。

ROS 2 发布者示例：

.. code-block:: python

   publisher = node.create_publisher(String, 'chatter', 10)
   msg = String()
   msg.data = 'hello world'
   publisher.publish(msg)

纯 Python 功能包使用标准 `setup.py` 安装机制。若原 ROS 1 功能包仅通过 CMake 调用 setup.py，且不包含消息、服务或动作定义，应迁移为 `ament_python` 功能包，并移除 `CMakeLists.txt`。

构建与运行
----------

在工作空间根目录构建：

.. code-block:: console

   $ colcon build

source 工作空间环境后，使用 `ros2 run` 运行迁移后的节点。

总结
----

本指南介绍了纯 Python 功能包从 ROS 1 迁移到 ROS 2 的主要步骤：将构建类型切换为 `ament_python`，把 `rospy` API 替换为 `rclpy`，并使用标准 `setup.py` 安装机制。
