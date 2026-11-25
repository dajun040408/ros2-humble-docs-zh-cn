使用 ros2_tracing 跟踪并分析应用程序
====================================

本教程介绍如何使用 `ros2_tracing <https://github.com/ros2/ros2_tracing>`_ 跟踪和分析 ROS 2 应用程序。本教程使用的示例应用是 `performance_test <https://gitlab.com/ApexAI/performance_test>`_。

概述
----

本教程包括：

#. 安装跟踪工具，并构建启用了核心插桩的 ROS 2。
#. 运行并跟踪 ``performance_test`` 实验。
#. 使用 `tracetools_analysis <https://github.com/ros-tracing/tracetools_analysis>`_ 分析跟踪数据，并使用 `Jupyter Notebook <https://jupyter.org/>`_ 绘制回调持续时间。

前置条件
--------

本教程面向实时 Linux 系统。请先参阅 :doc:`实时系统配置教程 <../Miscellaneous/Building-Realtime-rt_preempt-kernel-for-ROS-2>`。非实时 Linux 系统也可以运行本教程，但无法使用实时优先级相关功能。

安装与构建
----------

.. note::

   本教程原则上适用于所有受支持的 Linux 发行版，但部分命令可能需要根据系统调整。

按照 :doc:`Linux 源码安装说明 <../../Installation/Alternatives/Ubuntu-Development-Setup>` 安装 ROS 2 所需依赖，但先不要执行“构建工作空间中的代码”部分。

安装 `LTTng <https://lttng.org/docs/v2.13/>`_ 和 Babeltrace：

.. code-block:: console

   $ sudo apt-get update
   $ sudo apt-get install -y lttng-tools liblttng-ust-dev python3-lttng python3-babeltrace babeltrace

然后创建工作空间，导入 ROS 2 Humble 源码，并克隆 ``performance_test`` 和 ``tracetools_analysis``：

.. code-block:: console

   $ cd ~/
   $ mkdir -p tracing_ws/src
   $ cd tracing_ws/
   $ vcs import src/ --input https://raw.githubusercontent.com/ros2/ros2/humble/ros2.repos
   $ cd src/
   $ git clone https://gitlab.com/ApexAI/performance_test.git
   $ git clone https://github.com/ros-tracing/tracetools_analysis.git -b humble
   $ cd ..

使用 rosdep 安装依赖：

.. code-block:: console

   $ rosdep update
   $ rosdep install --rosdistro humble --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-6.0.1 urdfdom_headers"

接下来构建 ROS 2 到 ``performance_test`` 所需的包，并按照 ``performance_test`` 文档配置测试程序。详情参阅 `performance_test 文档 <https://gitlab.com/ApexAI/performance_test/-/tree/master/performance_test#performance_test>`_。

还需要构建 ``ros2trace``，以便使用 ``ros2 trace`` 命令配置跟踪，并构建 ``tracetools_analysis`` 来分析数据：

.. code-block:: console

   $ colcon build --packages-up-to ros2trace ros2run tracetools_analysis performance_test --cmake-args -DPERFORMANCE_TEST_RCLCPP_ENABLED=ON

加载工作空间环境，并确认跟踪功能已启用：

.. code-block:: console

   $ source install/setup.bash
   $ ros2 run tracetools status

如果输出中出现 ``Tracing enabled``，说明 LTTng 已被正确检测，并且编译进 ROS 2 核心代码的插桩功能已经启用。

接下来运行 ``performance_test`` 实验并跟踪其执行过程。

跟踪
----

步骤 1：启动跟踪
^^^^^^^^^^^^^^^^

在第一个终端中加载工作空间环境并启动跟踪设置。执行命令时，会打印 ROS 2 用户态事件列表，以及跟踪结果的保存目录（位于 ``~/.ros/tracing`` 下）。

终端 1：

.. code-block:: console

   $ cd ~/tracing_ws
   $ source install/setup.bash
   $ ros2 trace --session-name perf-test --list

按 Enter 键开始跟踪。

步骤 2：运行应用程序
^^^^^^^^^^^^^^^^^^^^

在第二个终端中加载工作空间环境，然后运行 ``performance_test`` 实验（也可以替换为自己的应用程序）。本例创建一个实验：一个节点以尽可能快的速度向另一个节点发布约 1 MB 的消息，持续 60 秒，并使用第二高的实时优先级，以避免干扰关键内核线程。

为了使用实时优先级，需要以 root 身份运行 ``performance_test``。

终端 2：

.. code-block:: console

   $ cd ~/tracing_ws
   $ source install/setup.bash
   $ sudo ./install/performance_test/lib/performance_test/perf_test -c rclcpp-single-threaded-executor -p 1 -s 1 -r 0 -m Array1m --reliability RELIABLE --max-runtime 60 --use-rt-prio 98

如果上述命令因共享库加载错误而无法运行，可以尝试下面的命令。这是因为出于安全原因，需要手动传递部分 ``*PATH`` 环境变量，才能找到共享库。详情参阅 `相关说明 <https://unix.stackexchange.com/a/251374>`_。

终端 2：

.. code-block:: console

   $ sudo env PATH="$PATH" LD_LIBRARY_PATH="$LD_LIBRARY_PATH" ./install/performance_test/lib/performance_test/perf_test -c rclcpp-single-threaded-executor -p 1 -s 1 -r 0 -m Array1m --reliability RELIABLE --max-runtime 60 --use-rt-prio 98

.. note::

   如果使用的不是实时内核，可以不使用 root 权限和实时优先级参数：

   .. code-block:: console

      $ ./install/performance_test/lib/performance_test/perf_test -c rclcpp-single-threaded-executor -p 1 -s 1 -r 0 -m Array1m --reliability RELIABLE --max-runtime 60

步骤 3：验证跟踪结果
^^^^^^^^^^^^^^^^^^^^

实验完成后，在第一个终端中再次按 Enter 键停止跟踪。然后使用 ``babeltrace`` 快速查看生成的跟踪数据：

.. code-block:: console

   $ babeltrace ~/.ros/tracing/perf-test | less

上述命令会将原始通用跟踪格式（Common Trace Format，CTF）数据转换为人类可读的文本。输出内容是一系列跟踪事件，每个事件都包含时间戳、事件类型、生成事件的进程信息，以及对应事件类型的字段值。

可以使用方向键滚动查看，按 ``q`` 退出。

接下来分析跟踪数据。

分析
----

`tracetools_analysis <https://github.com/ros-tracing/tracetools_analysis>`_ 提供 Python API，便于分析跟踪数据。可以在 `Jupyter Notebook <https://jupyter.org/>`_ 中使用 `Bokeh <https://docs.bokeh.org/en/latest/index.html>`_ 绘制数据。

``tracetools_analysis`` 仓库包含 `多个示例 Notebook <https://github.com/ros-tracing/tracetools_analysis/tree/humble/tracetools_analysis/analysis>`_，其中包括一个用于分析订阅回调持续时间的 `Notebook <https://github.com/ros-tracing/tracetools_analysis/blob/humble/tracetools_analysis/analysis/callback_duration.ipynb>`_。

本教程将绘制订阅者节点中订阅回调的执行持续时间。

安装 Bokeh，然后打开示例 Notebook：

.. code-block:: console

   $ pip3 install bokeh
   $ jupyter notebook ~/tracing_ws/src/tracetools_analysis/tracetools_analysis/analysis/callback_duration.ipynb

浏览器会打开 Notebook 页面。

将第二个单元格中的 ``path`` 变量修改为跟踪目录路径：

.. code-block:: python

   path = '~/.ros/tracing/perf-test'

点击每个单元格的 Run 按钮运行 Notebook。首次执行跟踪数据处理单元格可能需要几分钟，之后再次运行会快得多。

最终得到的图表应与下图类似：

.. image:: ./images/ros2_tracing_guide_result_plot.png
   :alt: 回调持续时间分析结果图
   :align: center

从图中可以看到，大多数回调的执行时间小于 0.01 毫秒，但也存在少量异常值，执行时间超过 0.02 或 0.03 毫秒。

总结
----

本教程介绍了如何安装跟踪工具，并构建启用了跟踪插桩的 ROS 2；随后使用 `ros2_tracing <https://github.com/ros2/ros2_tracing>`_ 跟踪 `performance_test <https://gitlab.com/ApexAI/performance_test>`_ 实验，并通过 `tracetools_analysis <https://github.com/ros-tracing/tracetools_analysis>`_ 绘制回调持续时间。

如需进行更多跟踪分析，可以查看 `其他示例 Notebook <https://github.com/ros-tracing/tracetools_analysis/tree/humble/tracetools_analysis/analysis>`_ 和 `tracetools_analysis API 文档 <https://ros-tracing.gitlab.io/tracetools_analysis-api/master/tracetools_analysis/>`_。`ros2_tracing 设计文档 <https://github.com/ros2/ros2_tracing/blob/humble/doc/design_ros_2.md>`_ 也包含大量相关信息。