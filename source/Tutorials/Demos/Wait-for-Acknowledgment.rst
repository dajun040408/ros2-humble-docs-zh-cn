等待消息确认
============

**目标：** 等待发布者发送的消息获得确认。

**教程级别：** 高级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 1
   :local:

概述
----

在发布者-订阅者架构中，消息由发布者发送给订阅者，但发布者没有内置机制确认订阅者是否已经收到消息。

此功能允许发布者等待其发送的消息获得确认。当发布者必须确保订阅者已收到消息后才能继续执行后续操作时，例如继续发送消息或执行其他操作，该功能非常有用。

RMW 支持情况
------------

等待确认功能需要 RMW 实现提供支持。

.. list-table:: 等待确认功能支持状态
   :widths: 25 25

   * - RMW 实现
     - 支持状态
   * - rmw_fastrtps
     - 支持
   * - rmw_connextdds
     - 支持
   * - rmw_cyclonedds
     - 支持

要使用等待确认功能，发布者的 :doc:`QoS 可靠性策略 <../../Concepts/Intermediate/About-Quality-of-Service-Settings>` 必须设置为 ``RELIABLE`` ，否则发布者不会等待确认。

安装演示程序
------------

ROS 2 安装详情请参阅 :doc:`安装说明 <../../Installation>`。

如果通过软件包安装 ROS 2，请确保已安装 ``ros-{DISTRO}-examples-rclcpp-minimal-publisher`` 和 ``ros-{DISTRO}-examples-rclcpp-minimal-subscriber`` 。如果下载了归档包或从源码构建 ROS 2，这些示例已经包含在安装内容中。

运行演示
--------

本演示展示如何在发布者中使用等待确认功能，确保发布者发送的消息都已被所有订阅者确认。

示例源码：`member_function_with_wait_for_all_acked.cpp <https://github.com/ros2/examples/blob/{REPOS_FILE_BRANCH}/rclcpp/topics/minimal_publisher/member_function_with_wait_for_all_acked.cpp>`_。

发布者可以使用 ``wait_for_all_acked`` 方法，在收到关闭信号之前，于指定超时时间内等待消息确认。

先 source 环境设置文件，然后运行 ``examples_rclcpp_minimal_publisher`` 软件包中的 ``publisher_wait_for_all_acked`` 和 ``subscriber_member_function`` 可执行程序。

在一个终端中启动订阅者：

.. code-block:: console

    $ ros2 run examples_rclcpp_minimal_subscriber subscriber_member_function
    [INFO] [1743121567.030751270] [minimal_subscriber]: I heard: 'Hello, world! 0'
    [INFO] [1743121567.530981660] [minimal_subscriber]: I heard: 'Hello, world! 1'
    [INFO] [1743121568.031032935] [minimal_subscriber]: I heard: 'Hello, world! 2'
    ...

然后在另一个终端中启动发布者：

.. code-block:: console

    $ ros2 run examples_rclcpp_minimal_publisher publisher_wait_for_all_acked
    [INFO] [1743121567.030353553] [minimal_publisher_with_wait_for_all_acked]: Publishing: 'Hello, world! 0'
    [INFO] [1743121567.530420788] [minimal_publisher_with_wait_for_all_acked]: Publishing: 'Hello, world! 1'
    [INFO] [1743121568.030461599] [minimal_publisher_with_wait_for_all_acked]: Publishing: 'Hello, world! 2'
    ...
    ^C[INFO] [1743121570.344981639] [rclcpp]: signal_handler(signum=2)
    [INFO] [1743121570.345398788] [minimal_publisher_with_wait_for_all_acked]: All subscribers acknowledge messages

当发布者终止时（例如按下 ``Ctrl-C`` ），它会等待关闭前发送的所有消息获得确认。如果所有订阅者都确认了消息，发布者就会输出所有订阅者均已确认的提示；否则，会输出未能在指定超时时间内获得全部确认的提示。

相关内容
--------

* `rclpy 等待确认示例 <https://github.com/ros2/examples/blob/{REPOS_FILE_BRANCH}/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function_with_wait_for_all_acked.py>`_。
