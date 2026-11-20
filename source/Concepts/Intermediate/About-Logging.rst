.. redirect-from::

    Logging
    Concepts/About-Logging

日志记录与 Logger 配置
========================

.. contents:: 目录
   :local:

概述
------

ROS 2 日志子系统旨在将日志消息发送到多种目标位置，包括：

* 控制台（如果已连接控制台）
* 磁盘上的日志文件（如果存在本地存储）
* ROS 2 网络中的 ``/rosout`` 话题

默认情况下，ROS 2 节点的日志消息会同时输出到控制台（stderr）、磁盘上的日志文件，以及 ROS 2 网络中的 ``/rosout`` 话题。每个节点都可以单独启用或禁用上述任意输出目标。

本文其余部分将介绍日志子系统背后的一些设计概念。

严重级别
----------

日志消息带有严重级别（severity level），按级别从低到高依次为：``DEBUG``、``INFO``、``WARN``、``ERROR`` 和 ``FATAL``。

Logger 只会处理严重级别大于或等于其指定级别的日志消息。

每个节点都关联一个 Logger，其名称会自动包含节点名称和命名空间。如果节点名称通过外部重映射修改为与源代码中定义的名称不同，Logger 名称也会反映这一变化。也可以创建不与节点关联、而是使用指定名称的 Logger。

Logger 名称具有层级结构。如果名为 ``abc.def`` 的 Logger 未设置级别，它会继承父级 Logger ``abc`` 的级别；如果父级也未设置级别，则使用默认 Logger 级别。当 ``abc`` 的级别发生变化时，其所有后代 Logger（例如 ``abc.def``、``abc.ghi.jkl``）的级别也会受到影响，除非这些后代已显式设置自己的级别。

API
-----

ROS 2 日志基础设施的最终用户应使用以下 API，按客户端库分别列出。

.. tabs::

  .. group-tab:: C++

    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}``：每次执行到该行时，输出给定的 printf 风格消息。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_ONCE``：仅在第一次执行到该行时输出给定的 printf 风格消息。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_EXPRESSION``：仅当给定表达式为 true 时，输出给定的 printf 风格消息。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_FUNCTION``：仅当给定函数返回 true 时，输出给定的 printf 风格消息。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_SKIPFIRST``：除第一次执行外，每次执行到该行时都输出给定的 printf 风格消息。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_THROTTLE``：按照给定的整数毫秒间隔限制输出频率，不会超过指定频率。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_SKIPFIRST_THROTTLE``：按照给定的整数毫秒间隔限制输出频率，并跳过第一次输出。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_STREAM``：每次执行到该行时，输出给定的 C++ stream 风格消息。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_STREAM_ONCE``：仅在第一次执行到该行时输出给定的 C++ stream 风格消息。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_STREAM_EXPRESSION``：仅当给定表达式为 true 时，输出给定的 C++ stream 风格消息。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_STREAM_FUNCTION``：仅当给定函数返回 true 时，输出给定的 C++ stream 风格消息。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_STREAM_SKIPFIRST``：除第一次执行外，每次执行到该行时都输出给定的 C++ stream 风格消息。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_STREAM_THROTTLE``：按照给定的整数毫秒间隔限制 C++ stream 风格消息的输出频率。
    * ``RCLCPP_{DEBUG,INFO,WARN,ERROR,FATAL}_STREAM_SKIPFIRST_THROTTLE``：按照给定的整数毫秒间隔限制输出频率，并跳过第一次输出。

    上述每个 API 都将 ``rclcpp::Logger`` 对象作为第一个参数。可以通过节点 API 调用 `node->get_logger()`` 获取（推荐方式），也可以单独构造 ``rclcpp::Logger`` 对象。

    * ``rcutils_logging_set_logger_level``：将指定名称 Logger 的日志级别设置为给定的严重级别。
    * ``rcutils_logging_get_logger_effective_level``：根据 Logger 名称返回其实际生效的日志级别（该级别可能尚未设置）。

  .. group-tab:: Python

    * ``logger.{debug,info,warning,error,fatal}``：将给定的 Python 字符串输出到日志基础设施。调用时可以使用以下关键字参数控制行为：

      * ``throttle_duration_sec``：如果不为 None，则表示节流间隔，单位为浮点秒。
      * ``skip_first``：如果为 True，则除第一次执行外，每次执行到该行时都输出消息。
      * ``once``：如果为 True，则仅在第一次执行到该行时输出消息。

    * ``rclpy.logging.set_logger_level``：将指定名称 Logger 的日志级别设置为给定的严重级别。
    * ``rclpy.logging.get_logger_effective_level``：根据 Logger 名称返回其实际生效的日志级别（该级别可能尚未设置）。

配置
------

由于 ``rclcpp`` 和 ``rclpy`` 使用相同的底层日志基础设施，因此它们的配置选项相同。

环境变量
^^^^^^^^^^

以下环境变量可以控制 ROS 2 Logger 的部分行为。请注意，这些环境设置都是进程级设置，因此会作用于该进程中的所有节点。

* ``ROS_LOG_DIR``：控制日志文件（如果启用了磁盘日志记录）的写入目录。如果该变量非空，则使用变量中指定的目录。如果为空，则使用 ``ROS_HOME`` 环境变量构造 ``$ROS_HOME/.log`` 形式的路径。在所有情况下，``~`` 字符都会展开为用户的 HOME 目录。
* ``ROS_HOME``：控制 ROS 各类文件所使用的主目录，包括日志文件和配置文件。在日志记录场景中，该变量用于构造日志文件目录路径。如果该变量非空，则使用其内容作为 ROS_HOME 路径。在所有情况下，``~`` 字符都会展开为用户的 HOME 目录。
* ``RCUTILS_LOGGING_USE_STDOUT``：控制日志消息输出到哪个流。如果未设置或值为 0，则使用 stderr；如果值为 1，则使用 stdout。
* ``RCUTILS_LOGGING_BUFFERED_STREAM``：控制日志输出流（由 ``RCUTILS_LOGGING_USE_STDOUT`` 配置）采用行缓冲还是无缓冲。如果未设置，则使用输出流默认行为（通常 stdout 为行缓冲，stderr 为无缓冲）。如果值为 0，则强制使用无缓冲；如果值为 1，则强制使用行缓冲。
* ``RCUTILS_COLORIZED_OUTPUT``：控制输出日志消息时是否使用颜色。如果未设置，则根据平台和控制台是否为 TTY 自动判断。如果值为 0，则强制禁用颜色；如果值为 1，则强制启用颜色。
* ``RCUTILS_CONSOLE_OUTPUT_FORMAT``：控制每条日志消息输出哪些字段。可用字段如下：

  * ``{severity}``：严重级别。
  * ``{name}``：Logger 名称（可能为空）。
  * ``{message}``：日志消息（可能为空）。
  * ``{function_name}``：调用日志 API 的函数名称（可能为空）。
  * ``{file_name}``：调用日志 API 的文件名称（可能为空）。
  * ``{time}``：从 epoch 起经过的秒数。
  * ``{time_as_nanoseconds}``：从 epoch 起经过的纳秒数。
  * ``{line_number}``：调用日志 API 的代码行号（可能为空）。

  如果未指定格式，则使用默认格式 ``[{severity}] [{time}] [{name}]: {message}``。

节点创建
^^^^^^^^^^

初始化 ROS 2 节点时，可以通过节点选项控制部分行为。由于这些选项是按节点设置的，即使多个节点组合在同一个进程中，也可以为不同节点设置不同选项。

* ``log_levels``：设置当前节点中某个组件使用的日志级别。示例：``ros2 run demo_nodes_cpp talker --ros-args --log-level talker:=DEBUG``。
* ``external_log_config_file``：用于配置后端 Logger 的外部文件。如果为 NULL，则使用默认配置。注意，该文件的格式取决于后端实现（当前默认的 spdlog 后端尚未实现该功能）。示例：``ros2 run demo_nodes_cpp talker --ros-args --log-config-file log-config.txt``。
* ``log_stdout_disabled``：是否禁用向控制台写入日志消息。示例：``ros2 run demo_nodes_cpp talker --ros-args --disable-stdout-logs``。
* ``log_rosout_disabled``：是否禁用向 ``/rosout`` 写入日志消息。禁用后可以显著节省网络带宽，但外部观察者将无法监控日志。示例：``ros2 run demo_nodes_cpp talker --ros-args --disable-rosout-logs``。
* ``log_ext_lib_disabled``：是否完全禁用外部 Logger。某些情况下这样可以提高速度，但日志将不会写入磁盘。示例：``ros2 run demo_nodes_cpp talker --ros-args --disable-external-lib-logs``。

日志子系统设计
----------------

下图展示了日志子系统的五个主要组成部分，以及它们之间的交互关系。

.. figure:: ../images/ros2_logging_architecture.png
   :alt: ROS 2 日志架构
   :width: 550px
   :align: center

rcutils
^^^^^^^^^

``rcutils`` 提供日志实现，可以按照指定格式（参见上文“配置”部分）格式化日志消息，并将其输出到控制台。

``rcutils`` 实现了一套完整的日志解决方案，同时允许更高层级的组件通过依赖注入模型接入日志基础设施。下面介绍 ``rcl`` 层时，这一点会更加明显。

请注意，这是一个*进程级*日志实现，因此在这一层配置的任何内容都会影响整个进程，而不仅仅是单个节点。

rcl_logging_spdlog
^^^^^^^^^^^^^^^^^^^^

``rcl_logging_spdlog`` 实现了 ``rcl_logging_interface`` API，因此可以向 ``rcl`` 层提供外部日志服务。具体来说，``rcl_logging_spdlog`` 会接收格式化后的日志消息，并使用 ``spdlog`` 库将其写入磁盘上的日志文件，通常位于 ``~/.ros/log``（该路径可以配置，参见上文“配置”部分）。

rcl
^^^^^

``rcl`` 中的日志子系统使用 ``rcutils`` 和 ``rcl_logging_spdlog`` 提供 ROS 2 日志服务的主要功能。

收到日志消息时，``rcl`` 会决定将其发送到哪里。日志消息主要可以发送到以下三个位置；每个节点可以启用其中任意组合：

* 通过 ``rcutils`` 层输出到控制台。
* 通过 ``rcl_logging_spdlog`` 层写入磁盘。
* 通过 RMW 层发布到 ROS 2 网络中的 ``/rosout`` 话题。

rclcpp
^^^^^^^^

这是构建在 ``rcl`` API 之上的 ROS 2 C++ 主要 API。

在日志记录方面，``rclcpp`` 提供 ``RCLCPP_`` 日志宏；完整列表请参阅上文“API”部分。执行 ``RCLCPP_`` 宏时，会将节点当前的严重级别与宏指定的严重级别进行比较。如果宏的严重级别大于或等于节点的严重级别，就会格式化消息，并输出到当前已配置的所有目标位置。

请注意，``rclcpp`` 在日志调用时使用全局互斥锁，因此同一进程中的所有日志调用最终都会以单线程方式执行。

rclpy
^^^^^^^

这是构建在 ``rcl`` API 之上的 ROS 2 Python 主要 API。

在日志记录方面，``rclpy`` 提供 ``logger.debug`` 风格的函数；完整列表请参阅上文“API”部分。执行 ``logger.debug`` 等函数时，会将节点当前的严重级别与函数指定的严重级别进行比较。如果函数的严重级别大于或等于节点的严重级别，就会格式化消息，并输出到当前已配置的所有目标位置。

日志使用示例
--------------

.. tabs::

  .. group-tab:: C++

    * 查看 `rclcpp 日志演示 <https://github.com/ros2/demos/tree/{REPOS_FILE_BRANCH}/logging_demo>`__，了解一些简单示例。
    * 查看 :doc:`日志演示教程 <../../Tutorials/Demos/Logging-and-logger-configuration>`，了解具体用法。
    * 查看 `rclcpp 文档 <https://docs.ros2.org/latest/api/rclcpp/logging_8hpp.html>`__ ，了解完整功能列表。

  .. group-tab:: Python

    * 查看 `rclpy 示例 <https://github.com/ros2/examples/blob/{REPOS_FILE_BRANCH}/rclpy/services/minimal_client/examples_rclpy_minimal_client/client.py>`__ ，了解如何使用节点的 Logger。
    * 查看 `rclpy 测试 <https://github.com/ros2/rclpy/blob/{REPOS_FILE_BRANCH}/rclpy/test/test_logging.py>`__ ，了解关键字参数（例如 ``skip_first``、``once``）的使用方法。
