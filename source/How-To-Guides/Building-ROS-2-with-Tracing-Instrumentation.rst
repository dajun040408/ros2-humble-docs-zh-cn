构建带有跟踪插桩的 ROS 2
=========================

.. contents:: 目录
   :depth: 2
   :local:

本指南介绍如何构建带有 ``ros2_tracing`` 提供的跟踪插桩（tracing instrumentation）的 ROS 2。更多信息请参阅 `ros2_tracing 代码仓库 <https://github.com/ros2/ros2_tracing>`_。

跟踪插桩已经包含在 ROS 2 源代码中。但是，无论使用二进制软件包还是从源码构建，默认情况下都不会实际触发跟踪点（tracepoints）。要启用跟踪点，需要安装 LTTng tracer，然后从源码重新构建 ROS 2 的部分组件。

.. note::

   本指南仅适用于 Linux 系统，并假设使用 Ubuntu。

前置条件
--------

请先配置系统，使其能够从源码构建 ROS 2。更多信息请参阅 :doc:`源码安装页面 <../Installation/Alternatives/Ubuntu-Development-Setup>`。

安装跟踪器
----------

安装 `LTTng tracer <https://lttng.org/docs>`_ 及相关工具和依赖项：

.. code-block:: bash

   sudo apt-get update
   sudo apt-get install -y lttng-tools liblttng-ust-dev python3-lttng python3-babeltrace babeltrace

这里仅安装 LTTng 用户空间跟踪器，不安装 LTTng 内核跟踪器，因为跟踪 ROS 2 应用程序不需要后者。

构建
----

此步骤取决于你是从源码构建 ROS 2，还是使用 ROS 2 二进制软件包。

源码安装
^^^^^^^^

如果你在安装 LTTng 之前已经 :doc:`从源码构建过 ROS 2 <../Installation/Alternatives/Ubuntu-Development-Setup>`，则至少需要重新构建到 ``tracetools`` 软件包：

.. code-block:: bash

   cd ~/ws
   colcon build --packages-up-to tracetools --cmake-force-configure

二进制安装
^^^^^^^^^^

如果你使用 ROS 2 二进制软件包（:doc:`deb 软件包 <../Installation/Ubuntu-Install-Debs>`` 或 :doc:``“fat” 归档包 <../Installation/Alternatives/Ubuntu-Install-Binary>`），则需要将 ``ros2_tracing`` 仓库克隆到工作空间，并至少构建到 ``tracetools`` 软件包：

.. code-block:: bash

   cd ~/ws/src
   git clone https://github.com/ros2/ros2_tracing.git
   cd ../
   colcon build --packages-up-to tracetools

验证
----

source 工作空间并验证跟踪功能是否启用：

.. code-block:: bash

   cd ~/ws
   source install/setup.bash
   ros2 run tracetools status

预期输出：

.. code-block:: bash

   Tracing enabled

如果输出其他内容，则说明配置过程中出现了问题。

禁用跟踪
--------

如果安装并检测到 LTTng 用户空间跟踪器，构建 ``tracetools`` 时会自动启用跟踪功能。

也可以通过将 CMake 选项 ``TRACETOOLS_DISABLED`` 设置为 ``ON``，在构建时彻底移除 ROS 2 中的跟踪点和跟踪插桩：

.. code-block:: bash

   colcon build --cmake-args -DTRACETOOLS_DISABLED=ON --no-warn-unused-cli
