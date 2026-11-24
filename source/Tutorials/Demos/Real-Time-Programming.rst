.. redirect-from::

    Real-Time-Programming
    Tutorials/Real-Time-Programming

理解实时编程
============

.. contents:: 目录
   :depth: 2
   :local:

背景
----

实时计算是许多机器人系统的关键特性，尤其适用于自动驾驶汽车、航天器和工业制造等安全关键或任务关键应用。

ROS 2 在设计和原型开发阶段就考虑了实时性能约束。ROS 1 早期开发时并未考虑这一要求，如今再对 ROS 1 进行实时化重构已非常困难。

`本文档 <https://design.ros2.org/articles/realtime_background.html>`_ 概述了实时计算的要求，以及软件工程师应遵循的最佳实践。简而言之：

实时计算系统必须让实时循环按照周期更新，以满足截止时间要求。对于这些截止时间，只能容忍很小的误差范围，也就是最大允许抖动。

为此，必须避免在执行路径中进行非确定性操作，例如缺页事件、动态内存分配/释放，以及可能无限期阻塞的同步原语。

一个经典的实时控制问题是平衡`倒立摆 <https://en.wikipedia.org/wiki/Inverted_pendulum>`_。如果控制器意外阻塞了很长时间，摆杆就会倒下或失去稳定性。但如果控制器能够以高于电机响应速度的稳定频率更新，就可以根据传感器数据及时调整控制量，使倒立摆保持平衡。

了解实时计算的基本概念后，下面运行一个演示程序。

安装并运行演示
--------------

本实时演示面向 Linux 操作系统，因为 ROS 社区中许多实时计算用户采用 Xenomai 或 RT_PREEMPT 作为实时解决方案。

由于演示中用于优化性能的许多操作都与操作系统有关，因此该演示只能在 Linux 系统上构建和运行。**macOS 和 Windows 用户请跳过本节。**

此外，必须从源码构建，并使用静态 DDS API。目前唯一支持的实现是 Connext DDS。

首先，按照 :doc:`Ubuntu 源码安装说明 <../../Installation/Alternatives/Ubuntu-Development-Setup>` 构建 ROS 2，并使用 Connext DDS 作为中间件。

运行测试
^^^^^^^^

**运行前请确保至少有 8 GB 可用内存。启用内存锁定后，swap 将无法继续使用。**

source ROS 2 的 `setup.bash`：

.. code-block:: console

   $ source ./install/setup.bash

运行演示程序。若遇到权限错误，可以尝试使用 `sudo`：

.. code-block:: console

   $ ros2 run pendulum_control pendulum_demo
   Initial major pagefaults: 518
   Initial minor pagefaults: 2139466
   No results filename given, not writing results
   rttest statistics:
   - Minor pagefaults: 0
   - Major pagefaults: 0
   Latency (time after deadline was missed):
      - Min: 1851 ns
      - Max: 166796 ns
      - Mean: 14229.182000 ns
      - Standard deviation: 12288.040996

你可能会在控制台（stderr）看到以下错误：

.. code-block:: console

   mlockall failed: Cannot allocate memory
   Couldn't lock all cached virtual memory.
   Pagefaults from reading pages not yet mapped into RAM will be recorded.

演示程序初始化完成后，会尝试使用 `mlockall` 将所有缓存内存锁定到 RAM 中，并阻止后续动态内存分配，以避免加载大量新内存时发生缺页。更多信息请参阅`实时设计文章中的内存管理部分 <https://design.ros2.org/articles/realtime_background.html#memory-management>`_。

出现上述情况时，演示程序仍会继续运行。你也可能看到以下输出，它表示执行期间发生的缺页次数：

.. code-block:: text

   rttest statistics:
     - Minor pagefaults: 20
     - Major pagefaults: 0

如果希望消除这些缺页，需要调整内存锁定权限。

调整内存锁定权限
^^^^^^^^^^^^^^^^

使用 sudo 编辑 `/etc/security/limits.conf`，添加以下内容：

.. code-block:: text

   <your username>    -   memlock   <limit in kB>

将限制设置为 `-1` 表示不受限制。选择该值时，可能还需要在编辑文件后执行 `ulimit -l unlimited`。

保存文件后，注销并重新登录，再次运行 `pendulum_demo`。

输出文件中应该不再出现缺页；否则可能会看到捕获到 `bad_alloc` 异常的错误。这表示可用于锁定进程内存的空闲 RAM 不足。若希望实现零缺页，需要为计算机增加内存。

查看输出
^^^^^^^^

要查看更多输出，需要运行 `pendulum_logger` 节点。

在一个已经 source `install/setup.bash` 的 Shell 中运行：

.. code-block:: console

   $ ros2 run pendulum_control pendulum_logger

应该看到以下输出：

.. code-block:: text

   Logger node initialized.

在另一个已经 source `setup.bash` 的 Shell 中，再次运行 `pendulum_demo`。

程序启动后，另一个 Shell 会持续输出：

.. code-block:: text

   Commanded motor angle: 1.570796
   Actual motor angle: 1.570796
   Mean latency: 210144.000000 ns
   Min latency: 4805 ns
   Max latency: 578137 ns
   Minor pagefaults during execution: 0
   Major pagefaults during execution: 0

该演示控制一个非常简单的倒立摆仿真。倒立摆仿真在线程中计算自身位置。一个 ROS 节点模拟电机编码器传感器并发布摆杆位置；另一个 ROS 节点充当简单的 PID 控制器，计算下一条控制命令消息。

logger 节点会定期输出摆杆状态，以及演示程序执行阶段的运行性能统计信息。

`pendulum_demo` 结束后，需要按 `Ctrl-C` 退出 logger 节点。

延迟
^^^^

`pendulum_demo` 执行结束时，会输出最终统计信息：

.. code-block:: text

   rttest statistics:
     - Minor pagefaults: 0
     - Major pagefaults: 0
     Latency (time after deadline was missed):
       - Min: 3354 ns
       - Max: 2752187 ns
       - Mean: 19871.8 ns
       - Standard deviation: 1.35819e+08

   PendulumMotor received 985 messages
   PendulumController received 987 messages

延迟字段显示更新循环的最小、最大和平均延迟，单位为纳秒。这里的延迟是指更新操作超过预期执行时间的时长。

实时系统的具体要求取决于应用场景。假设本演示采用 1 kHz（1 毫秒）的更新循环，并将最大允许延迟设为更新周期的 5%。

本次运行的平均延迟表现很好，但最大延迟不可接受，因为它甚至超过了整个更新周期。为什么会这样？

问题可能来自非确定性调度器。如果运行的是未安装 RT_PREEMPT 内核的普通 Linux 系统，可能无法满足设定的实时目标，因为 Linux 调度器不允许用户级线程任意抢占。

更多信息请参阅`实时设计文章中的多线程编程与同步部分 <https://design.ros2.org/articles/realtime_background.html#multithreaded-programming-and-synchronization>`_。

演示程序会尝试设置适合实时性能的调度器和线程优先级。如果操作失败，会看到错误信息 `Couldn't set scheduling priority and policy: Operation not permitted`。按照下一节说明调整权限，可以获得略好的性能。

设置调度器权限
^^^^^^^^^^^^^^

使用 sudo 编辑 `/etc/security/limits.conf`，添加：

.. code-block:: text

   <your username>    -   rtprio   98

``rtprio``（实时优先级）的范围为 0 到 99。但**不要**将限制设置为 99，否则进程可能干扰以最高优先级运行的重要系统进程，例如 watchdog。

本演示会尝试将控制循环设置为优先级 98。

绘制结果
^^^^^^^^

演示运行结束后，可以绘制收集到的延迟和缺页统计信息。

由于代码使用 `rttest <https://github.com/ros2/rttest>`_ 进行了插桩，因此提供了一些有用的命令行参数：

.. list-table::
   :header-rows: 1
   :widths: 15 60 25

   * - 参数
     - 说明
     - 默认值
   * - `-i`
     - 指定实时循环运行的迭代次数。
     - 1000
   * - `-u`
     - 指定更新周期，默认单位为微秒。可使用 `s`、`ms`、`us` 和 `ns` 后缀分别表示秒、毫秒、微秒和纳秒。
     - 1ms
   * - `-f`
     - 指定保存收集数据的文件名。
     -

再次运行演示，并指定文件名保存结果：

.. code-block:: console

   $ ros2 run pendulum_control pendulum_demo -f pendulum_demo_results

然后对结果文件运行 `rttest_plot` 脚本：

.. code-block:: console

   $ ros2 run rttest rttest_plot pendulum_demo_results
   Writing results to file: pendulum_demo_results
   ...

该脚本会生成三个文件：

.. code-block:: text

   pendulum_demo_results_plot_latency.svg
   pendulum_demo_results_plot_majflts.svg
   pendulum_demo_results_plot_minflts.svg

可以使用任意图像查看器打开这些图表。
