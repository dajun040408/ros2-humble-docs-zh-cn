.. redirect-from::

    Rosbag-with-ROS1-Bridge
    Tutorials/Rosbag-with-ROS1-Bridge

使用 ROS 1 Bridge 录制和回放 rosbag 数据
========================================

本教程是 :doc:§ROS 1 与 ROS 2 之间的桥接通信 <../../How-To-Guides/Using-ros1_bridge-Jammy-upstream>§ 演示的后续内容。假设你已经完成桥接教程，并已构建 §ros1_bridge§。

使用 rosbag 和 ROS 1 Bridge 录制话题数据
---------------------------------------

本示例使用 ROS 2 自带的 §cam2image§ 演示程序，以及一个 Python 脚本模拟类似 TurtleBot 的传感器数据。数据通过 ROS 1 Bridge 转发到 ROS 1，再使用 ROS 1 rosbag 录制。

首先在新终端启动 ROS 1 §roscore§：

.. code-block:: console

   $ . /opt/ros/kinetic/setup.bash
   $ roscore

然后在另一个终端运行 ROS 1 与 ROS 2 之间的 §dynamic_bridge§，并使用 §--bridge-all-topics§ 选项：

.. code-block:: console

   $ . /opt/ros/kinetic/setup.bash
   $ . /opt/ros/ardent/setup.bash
   $ export ROS_MASTER_URI=http://localhost:11311
   $ ros2 run ros1_bridge dynamic_bridge --bridge-all-topics

如果从源码安装 bridge，请根据实际工作空间调整 setup 文件路径。

启动 ROS 2 模拟程序
------------------

现在启动 ROS 2 程序模拟 TurtleBot 传感器数据。首先运行 §cam2image§，使用 §-b§ 参数避免依赖真实摄像头：

.. code-block:: console

   $ ros2 run image_tools cam2image -b

然后启动模拟机器人传感器数据的 Python 节点。由于 bridge 已启用所有话题，ROS 1 侧可以通过 §rostopic list§ 查看桥接后的话题。

录制数据
--------

在 ROS 1 终端中使用 §rosbag record§ 录制桥接话题：

.. code-block:: console

   $ rosbag record -a

录制完成后按 §Ctrl-C§ 停止。生成的 bag 文件可以在 ROS 1 环境中回放，也可以通过桥接机制将数据转发给 ROS 2 节点。

回放数据
--------

停止实时数据发布后，在 ROS 1 终端中运行：

.. code-block:: console

   $ rosbag play <bag_file>

ROS 1 Bridge 会将兼容话题转发到 ROS 2。请确保消息类型已在 bridge 中建立映射，并且 ROS 2 订阅者使用兼容的 QoS 设置。

总结
----

本演示介绍了如何通过 ROS 1 Bridge 将 ROS 2 话题转发到 ROS 1，使用 ROS 1 rosbag 录制数据，再通过桥接回放并供 ROS 2 节点使用。
