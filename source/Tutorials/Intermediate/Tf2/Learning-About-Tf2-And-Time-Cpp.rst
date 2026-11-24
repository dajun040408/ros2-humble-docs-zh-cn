.. redirect-from::

    Tutorials/Tf2/Learning-About-Tf2-And-Time-Cpp

.. _LearningAboutTf2AndTimeCpp:

使用时间（C++）
===============

**目标：** 学习如何使用 ``lookupTransform()`` 函数获取特定时间的坐标变换，并等待 tf2 变换树中出现可用变换。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

在之前的教程中，我们通过编写 :doc:`tf2 广播器 </Tutorials/Intermediate/Tf2/Writing-A-Tf2-Broadcaster-Cpp>` 和 :doc:`tf2 监听器 </Tutorials/Intermediate/Tf2/Writing-A-Tf2-Listener-Cpp>` 重现了海龟演示。我们还学习了如何 :doc:`向变换树添加新坐标系 </Tutorials/Intermediate/Tf2/Adding-A-Frame-Cpp>`，以及 tf2 如何维护坐标系树。

该树会随时间变化，tf2 会为每个变换保存一个时间快照（默认最长保存 10 秒）。此前，我们使用 ``lookupTransform()`` 获取 tf2 变换树中最新可用的变换，而没有指定该变换记录的时间。本教程将介绍如何获取特定时间的变换。

任务
----

1. 更新监听器节点
^^^^^^^^^^^^^^^^^

回到 :doc:`添加坐标系教程 <Adding-A-Frame-Cpp>` 的最后一步，进入 ``learning_tf2_cpp`` 功能包，打开 ``turtle_tf2_listener.cpp`` ，查看 ``lookupTransform()`` 调用：

.. code-block:: cpp

   t = tf_buffer_->lookupTransform(
      toFrameRel,
      fromFrameRel,
      tf2::TimePointZero);

这里通过 ``tf2::TimePointZero`` 指定了时间 0。

.. note::

   ``tf2`` 软件包有自己的时间类型 ``tf2::TimePoint`` ，它不同于 ``rclcpp::Time`` 。``tf2_ros`` 中的许多 API 会自动在 ``rclcpp::Time`` 和 ``tf2::TimePoint`` 之间转换。

   这里也可以使用 ``rclcpp::Time(0, 0, this->get_clock()->get_clock_type())`` ，但最终仍会被转换为 ``tf2::TimePointZero`` 。

对于 tf2，时间 0 表示缓冲区中“最新可用”的变换。现在修改这行代码，获取当前时间 ``this->get_clock()->now()`` 对应的变换：

.. code-block:: cpp

   rclcpp::Time now = this->get_clock()->now();
   t = tf_buffer_->lookupTransform(
      toFrameRel,
      fromFrameRel,
      now);

现在尝试运行启动文件：

.. code-block:: console

   $ ros2 launch learning_tf2_cpp turtle_tf2_demo_launch.xml
   [INFO] [1629873136.345688064] [listener]: Could not transform turtle2 to turtle1: Lookup would
   require extrapolation into the future. Requested time 1629873136.345539 but the latest data
   is at time 1629873136.338804, when looking up transform from frame [turtle1] to frame [turtle2]

输出表明，坐标系可能不存在，或者请求的数据时间位于未来。

要理解原因，需要了解缓冲区的工作方式。首先，每个监听器都有自己的缓冲区，用于存储来自不同 tf2 广播器的坐标变换。其次，广播器发送变换后，该变换需要一定时间才能进入缓冲区（通常为几毫秒）。因此，当请求“当前时刻”的坐标变换时，应等待几毫秒，让数据到达。

2. 修复监听器节点
^^^^^^^^^^^^^^^^^

tf2 提供了一个便捷机制，可以等待变换变为可用状态。只需向 ``lookupTransform()`` 添加超时参数即可。修改代码如下（添加最后一个超时参数）：

.. code-block:: cpp

   rclcpp::Time now = this->get_clock()->now();
   t = tf_buffer_->lookupTransform(
      toFrameRel,
      fromFrameRel,
      now,
      50ms);

``lookupTransform()`` 可以接受四个参数，最后一个参数为可选超时时间。调用会阻塞指定时长，直到变换可用或超时。

3. 检查结果
^^^^^^^^^^^

现在可以运行启动文件：

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

你会发现，``lookupTransform()`` 会一直阻塞，直到两只海龟之间的变换可用（通常只需几毫秒）。只有当超时时间到达（本例为 50 毫秒）且变换仍不可用时，才会抛出异常。

总结
----

本教程介绍了如何获取指定时间戳的坐标变换，以及使用 ``lookupTransform()`` 等待 tf2 变换树中的变换变为可用状态。
