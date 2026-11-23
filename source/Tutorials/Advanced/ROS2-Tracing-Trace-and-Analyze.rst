使用 ros2_tracing 跟踪并分析应用程序
====================================

本教程介绍如何使用 §ros2_tracing§ 跟踪和分析 ROS 2 应用程序。示例应用为 §performance_test§。

概述
----

本教程包括：

1. 安装跟踪工具，并构建启用了核心插桩的 ROS 2。
2. 运行并跟踪 §performance_test§。
3. 使用 §tracetools_analysis§ 和 Jupyter Notebook 分析跟踪数据，并绘制回调持续时间。

前置条件
--------

本教程面向实时 Linux 系统。建议先完成 :doc:§实时系统配置教程 <../Miscellaneous/Building-Realtime-rt_preempt-kernel-for-ROS-2>§。非实时 Linux 系统也可以运行本教程。

安装与构建
----------

按照 :doc:§Ubuntu 源码安装说明 <../../Installation/Alternatives/Ubuntu-Development-Setup>§ 安装 ROS 2 Linux 依赖，但先不要执行“构建工作空间中的代码”部分。

安装 LTTng 和 Babeltrace：

.. code-block:: console

   $ sudo apt-get update
   $ sudo apt-get install -y lttng-tools liblttng-ust-dev python3-lttng python3-babeltrace babeltrace

创建工作空间，导入 ROS 2 Humble 源码，并克隆 §performance_test§ 和 §tracetools_analysis§：

.. code-block:: console

   $ mkdir -p ~/tracing_ws/src
   $ cd ~/tracing_ws
   $ vcs import src/ --input https://raw.githubusercontent.com/ros2/ros2/humble/ros2.repos
   $ cd src
   $ git clone https://gitlab.com/ApexAI/performance_test.git
   $ git clone https://github.com/ros-tracing/tracetools_analysis.git -b humble
   $ cd ..

使用 rosdep 安装依赖：

.. code-block:: console

   $ rosdep update
   $ rosdep install --rosdistro humble --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-6.0.1 urdfdom_headers"

构建时需要启用 ROS 2 tracing 插桩，并根据 §performance_test§ 文档配置测试程序。

运行与跟踪
----------

运行应用程序时启用 LTTng 跟踪会话，收集 ROS 2 事件。跟踪完成后，使用 §tracetools_analysis§ 读取 trace 数据，并在 Jupyter Notebook 中分析回调执行时间、调度延迟和消息处理路径。

分析结果
--------

跟踪数据可以帮助定位回调执行时间、消息传递延迟和执行器调度行为。对于实时系统，可将跟踪数据与系统负载、线程优先级和调度策略结合分析。

总结
----

§ros2_tracing§ 通过 LTTng 收集 ROS 2 运行时事件，§tracetools_analysis§ 则用于解析和分析 trace 数据。两者结合可用于性能分析和实时性问题排查。
