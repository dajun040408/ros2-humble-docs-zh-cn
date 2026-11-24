.. redirect-from::

    Tutorials/Tf2/Time-Travel-With-Tf2-Cpp

.. _TimeTravelWithTf2Cpp:

tf2 时间旅行（C++）
===================

**目标：** 学习 tf2 的高级时间旅行功能。

**教程级别：** 中级 | **预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

在上一个教程中，我们讨论了 :doc:§tf2 与时间的基础知识 <./Learning-About-Tf2-And-Time-Cpp>§。本教程进一步介绍 tf2 的一项强大功能：时间旅行。tf2 不仅能够在空间中变换数据，还能够在时间维度上变换数据。

这项功能可用于长时间监控机器人位姿，或构建跟随机器人，让跟随者沿着领航者过去走过的轨迹行驶。本教程将使用时间旅行功能查询过去的变换，并让 §turtle2§ 跟随 5 秒前 §carrot1§ 所在的位置。

时间旅行
--------

回到 :doc:§使用时间 <./Learning-About-Tf2-And-Time-Cpp>§ 教程的最后一步，进入 §learning_tf2_cpp§ 功能包。

现在不再让第二只海龟前往 carrot 当前的位置，而是让它前往 carrot 5 秒前的位置。编辑 §turtle_tf2_listener.cpp§ 中的 §lookupTransform()§ 调用：

.. code-block:: cpp

   rclcpp::Time when = this->get_clock()->now() - rclcpp::Duration(5, 0);
   t = tf_buffer_->lookupTransform(
       toFrameRel,
       fromFrameRel,
       when,
       50ms);

运行启动文件：

.. tabs::

  .. group-tab:: XML

    .. code-block:: console

        $ ros2 launch learning_tf2_cpp turtle_tf2_fixed_frame_demo_launch.xml

  .. group-tab:: YAML

    .. code-block:: console

        $ ros2 launch learning_tf2_cpp turtle_tf2_fixed_frame_demo_launch.yaml

  .. group-tab:: Python

    .. code-block:: console

        $ ros2 launch learning_tf2_cpp turtle_tf2_fixed_frame_demo_launch.py

.. image:: images/turtlesim_delay1.png

你可能会发现，海龟像截图中一样失控地移动。原因如下：

#. 代码向 tf2 询问：“5 秒前，相对于 5 秒前的 §turtle2§，§carrot1§ 的位姿是什么？”这意味着第二只海龟的控制依据不仅是 carrot 5 秒前的位置，也是 §turtle2§ 自己 5 秒前的位置。
#. 但真正希望询问的是：“5 秒前 §carrot1§ 的位姿，相对于 §turtle2§ 当前的位置是什么？”

lookupTransform() 的高级 API
----------------------------

为了提出上述问题，需要使用高级 API，显式指定获取各个变换的时间。修改代码如下：

.. code-block:: cpp

   rclcpp::Time now = this->get_clock()->now();
   rclcpp::Time when = now - rclcpp::Duration(5, 0);
   t = tf_buffer_->lookupTransform(
       toFrameRel,
       now,
       fromFrameRel,
       when,
       "world",
       50ms);

§lookupTransform()§ 的高级 API 接受六个参数：

#. 目标坐标系。
#. 目标坐标系变换到的时间。
#. 源坐标系。
#. 评估源坐标系的时间。
#. 不随时间变化的坐标系，本例为 §world§。
#. 等待目标坐标系变为可用状态的时间。

在后台，tf2 会先计算过去时刻 §carrot1§ 到 §world§ 的变换；然后在 §world§ 坐标系中从过去“穿越”到当前时刻；最后在当前时刻计算 §world§ 到 §turtle2§ 的变换。

检查结果
--------

再次运行仿真，这次使用高级时间旅行 API：

.. tabs::

  .. group-tab:: XML

    .. code-block:: console

        $ ros2 launch learning_tf2_cpp turtle_tf2_fixed_frame_demo_launch.xml

  .. group-tab:: YAML

    .. code-block:: console

        $ ros2 launch learning_tf2_cpp turtle_tf2_fixed_frame_demo_launch.yaml

  .. group-tab:: Python

    .. code-block:: console

        $ ros2 launch learning_tf2_cpp turtle_tf2_fixed_frame_demo_launch.py

.. image:: images/turtlesim_delay2.png

此时，第二只海龟会朝向第一只海龟的 carrot 在 5 秒前所在的位置。

总结
----

本教程介绍了 tf2 的一项高级功能。tf2 能够在时间维度上变换数据，并通过 turtlesim 示例展示了如何实现。借助高级 §lookupTransform()§ API，tf2 可以回到过去，在海龟过去和当前的位姿之间执行坐标变换。
