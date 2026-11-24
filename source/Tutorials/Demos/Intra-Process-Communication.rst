.. redirect-from::

    Intra-Process-Communication
    Tutorials/Intra-Process-Communication

配置高效的进程内通信
====================

.. contents:: 目录
   :depth: 2
   :local:

背景
----

ROS 应用通常由多个独立节点组合而成。每个节点负责范围较窄的任务，并与系统其他部分解耦。这有助于隔离故障、加快开发、提高模块化程度并复用代码，但通常会带来性能开销。

ROS 1 开发后期，节点高效组合的需求逐渐明显，因此引入了 Nodelet。ROS 2 希望通过重新设计节点，解决 Nodelet 的一些根本问题，进一步改进该设计。

本演示展示如何手动组合节点：分别定义节点，再将它们组合到不同进程布局中，而无需修改节点代码或限制其能力。

安装演示程序
------------

有关安装 ROS 2 的详情，请参阅 :doc:`安装说明 <../../Installation>`。

如果通过软件包安装 ROS 2，请确保安装 ros-{DISTRO}-intra-process-demo。如果下载归档包或从源码构建 ROS 2，该演示程序已经包含在安装内容中。

运行并理解演示
--------------

本演示包含多个示例：一些是用于展示进程内通信功能的简单示例，另一些是使用 OpenCV 的端到端示例，展示如何重新组合节点。

双节点流水线演示
^^^^^^^^^^^^^^^^

该演示用于展示：当发布者和订阅者使用 std::unique_ptr 发布和订阅消息时，进程内发布/订阅连接可以实现零拷贝传输。

示例源码：

https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/intra_process_demo/src/two_node_pipeline/two_node_pipeline.cpp

关键点是创建节点时启用进程内通信：

.. code-block:: cpp

   rclcpp::NodeOptions().use_intra_process_comms(true)

发布者使用 unique_ptr 发布消息，订阅者可以直接接收该消息所有权，从而避免额外复制。

可以使用以下命令运行演示：

.. code-block:: console

   $ ros2 run intra_process_demo two_node_pipeline

在终端中可以观察消息经过流水线节点的过程。

进程内通信与进程间通信
----------------------

ROS 2 支持在同一进程中组合多个节点，也支持将节点分别运行在不同进程中。启用进程内通信后，位于同一进程的发布者和订阅者可以使用优化的数据传递路径。

如果节点位于不同进程，消息仍通过底层 RMW 中间件传输。

性能与消息所有权
----------------

进程内通信是否能够避免复制，取决于消息所有权和订阅者数量。使用 std::unique_ptr 可以将消息所有权从发布者转移给订阅者；如果有多个订阅者或需要保留消息，则可能需要复制。

相关示例
--------

完整示例代码和其他进程内通信场景请参阅`intra_process_demo <https://github.com/ros2/demos/tree/{REPOS_FILE_BRANCH}/intra_process_demo>`_。
