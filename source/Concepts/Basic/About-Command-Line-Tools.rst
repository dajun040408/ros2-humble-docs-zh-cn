.. redirect-from::

    Introspection-with-command-line-tools
    Tutorials/Introspection-with-command-line-tools
    Concepts/About-Command-Line-Tools

使用命令行工具进行系统检查
==========================

.. contents:: 目录
   :local:

ROS 2 提供了一套命令行工具，用于检查和操作 ROS 2 系统。

用法
----

这些工具的主要入口是 `ros2` 命令。该命令包含多个子命令，可用于检查和操作节点、话题、服务等资源。

运行以下命令查看所有可用子命令：

.. code-block:: console

   $ ros2 --help

常见子命令包括：

* `action`：检查和操作 ROS 动作。
* `bag`：录制或播放 rosbag。
* `component`：管理组件容器。
* `daemon`：检查或配置 ROS 2 守护进程。
* `doctor`：检查 ROS 环境设置是否存在潜在问题。
* `interface`：显示 ROS 接口信息。
* `launch`：运行或检查启动文件。
* `lifecycle`：检查和管理具有受控生命周期的节点。
* `multicast`：多播调试命令。
* `node`：检查 ROS 节点。
* `param`：检查或配置节点参数。
* `pkg`：检查 ROS 功能包。
* `plugin`：检查 ROS 插件。
* `run`：运行 ROS 节点。
* `security`：配置安全设置。
* `service`：检查或调用 ROS 服务。
* `test`：运行 ROS launch 测试。
* `topic`：检查或发布 ROS 话题。
* `trace`：跟踪工具，用于获取 ROS 节点执行过程的信息（仅 Linux 可用）。
* `wtf`：`doctor` 命令的别名。

示例
----

要使用命令行工具实现典型的 talker-listener 示例，可以使用 `topic` 子命令在话题上发布和回显消息。

在一个终端中发布消息：

.. code-block:: console

   $ ros2 topic pub /chatter std_msgs/msg/String "data: Hello world"
   publisher: beginning loop
   publishing #1: std_msgs.msg.String(data='Hello world')

   publishing #2: std_msgs.msg.String(data='Hello world')

在另一个终端中回显收到的消息：

.. code-block:: console

   $ ros2 topic echo /chatter
   data: Hello world

   data: Hello world

ROS 2 守护进程：后台发现服务
----------------------------

ROS 2 使用分布式发现过程，使节点能够彼此连接。由于该过程有意不采用集中式发现机制，ROS 节点可能需要一定时间才能发现 ROS 计算图中的所有其他参与者。

为了解决这一问题，ROS 2 会运行一个后台守护进程，维护 ROS 计算图的信息，以便更快地响应查询，例如查询节点名称列表。

首次使用 `ros2 node list`、`ros2 topic list` 或其他系统检查命令行工具时，ROS 2 守护进程会自动启动。如果当前没有守护进程运行，这些工具会先在后台创建一个新的守护进程，然后再执行请求的命令。

守护进程通过 localhost 网络接口（127.0.0.1）进行通信，并使用 :doc:`ROS_DOMAIN_ID <../Intermediate/About-Domain-ID>` 环境变量作为端口号偏移量。这意味着，如果你希望控制某个特定的守护进程实例（例如使用 `ros2 daemon stop`），必须确保当前 :doc:`ROS_DOMAIN_ID <../Intermediate/About-Domain-ID>` 与该守护进程使用的域 ID 一致。不同的 :doc:`ROS_DOMAIN_ID <../Intermediate/About-Domain-ID>` 值会使系统在不同端口上运行独立的守护进程实例。

运行 `ros2 daemon --help` 可以查看与守护进程交互的更多选项，包括启动、停止或检查守护进程状态的命令。

在前台运行守护进程
^^^^^^^^^^^^^^^^^^

在调试时，将 ROS 2 守护进程运行在前台可能很有用，这样它的输出会直接打印到 stdout 和 stderr。可以使用 `_ros2_daemon` 命令启动守护进程进程本身：

.. code-block:: console

   $ _ros2_daemon --ros-domain-id 0 --rmw-implementation rmw_fastrtps_cpp

该命令会启动守护进程，但不会将其转入后台，因此你可以实时观察所有发现活动和 XML-RPC 请求。请根据你的环境替换 `--ros-domain-id` 和 `--rmw-implementation` 的值。

.. note::

   在以前台方式启动守护进程之前，请确保停止任何已经运行的守护进程实例（`ros2 daemon stop`），以避免端口冲突。

实现
----

`ros2` 命令的源代码位于 https://github.com/ros2/ros2cli。

`ros2` 工具采用可通过插件扩展的框架实现。例如，`sros2 <https://github.com/ros2/sros2>`__ 软件包提供了 `security` 子命令。如果安装了 `sros2` 软件包，`ros2` 工具就会自动检测到该子命令。
