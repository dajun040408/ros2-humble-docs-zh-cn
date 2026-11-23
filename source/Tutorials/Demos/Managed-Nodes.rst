.. redirect-from::

    Managed-Nodes
    Tutorials/Managed-Nodes

节点生命周期管理示例
====================

节点的受管理生命周期可以让你更好地控制 ROS 系统的状态。本示例使用一组简单的 talker/listener 受管理节点，展示如何实现和使用受管理生命周期。你可以通过该示例理解并实践这种节点管理方式。

**领域：ROS 框架 | 内容类型：示例 | 经验水平：专家**

.. contents:: 目录
   :depth: 2
   :local:

概要
----

ROS 2 引入了受管理节点（Managed Nodes），也称为生命周期节点（Lifecycle Nodes）。这类节点能够确保资源在节点切换生命周期状态时，按照正确流程完成初始化、激活、停用和清理。

一种常见使用场景是硬件控制节点：摄像头、激光雷达、电机驱动器以及其他传感器和执行器等设备，都必须按照受控顺序启动、配置和关闭。

使用生命周期节点有助于确保硬件只在准备就绪后才进行初始化，并在关闭或错误恢复期间安全释放资源。以下软件包支持实现受管理节点：`rclcpp_lifecycle <https://index.ros.org/p/rclcpp_lifecycle/>`_（实现库）和 `lifecycle_msgs <https://index.ros.org/p/lifecycle_msgs/>`_（接口定义）。

前置条件
--------

有关 ROS 2 安装详情，请参阅 :doc:`安装说明 <../../Installation>`。

示例
----

获取示例
^^^^^^^^

有关如何运行示例的信息，请参阅 `lifecycle_demo_launch.py <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/lifecycle_py/launch/lifecycle_demo_launch.py>`_。

说明
^^^^

有关运行方式及其工作过程的更多信息，请参阅 `lifecycle README <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/lifecycle/README.rst>`_。

相关内容
--------

软件包/参考资料：

* `rclcpp_lifecycle <https://index.ros.org/p/rclcpp_lifecycle/>`_（实现库）：包含生命周期实现原型的软件包。
* `lifecycle_msgs <https://index.ros.org/p/lifecycle_msgs/>`_（接口定义）：包含生命周期相关消息和服务定义的软件包。
* `lifecycle <https://docs.ros.org/en/{DISTRO}/p/lifecycle/>`_：包含生命周期实现演示的软件包。
