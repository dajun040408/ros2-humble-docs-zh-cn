.. redirect-from::

    Logging-and-logger-configuration
    Tutorials/Logging-and-logger-configuration

日志记录
========

.. contents:: 目录
   :depth: 2
   :local:

有关可用功能的详细信息，请参阅 :doc:§日志记录页面 <../../Concepts/Intermediate/About-Logging>§。

在代码中使用日志语句
--------------------

基本日志
^^^^^^^^

以下代码会让 ROS 2 节点输出 DEBUG 级别的日志消息：

.. tabs::

    .. group-tab:: C++

        .. code-block:: cpp

            // printf 风格
            RCLCPP_DEBUG(node->get_logger(), "My log message %d", 4);

            // C++ stream 风格
            RCLCPP_DEBUG_STREAM(node->get_logger(), "My log message " << 4);

    .. group-tab:: Python

        .. code-block:: python

            node.get_logger().debug('My log message %d' % (4))

注意，两种情况下都不会添加末尾换行符，因为日志基础设施会自动添加换行符。

只记录第一次
^^^^^^^^^^^^

以下代码会让 ROS 2 节点输出 INFO 级别的日志消息，但只在第一次执行到该语句时输出：

.. tabs::

    .. group-tab:: C++

        .. code-block:: cpp

            RCLCPP_INFO_ONCE(node->get_logger(), "My log message %d", 4);
            RCLCPP_INFO_STREAM_ONCE(node->get_logger(), "My log message " << 4);

    .. group-tab:: Python

        .. code-block:: python

            num = 4
            node.get_logger().info(f'My log message {num}', once=True)

跳过第一次
^^^^^^^^^^

以下代码会让 ROS 2 节点输出 WARN 级别的日志消息，但第一次执行时不会输出：

.. tabs::

    .. group-tab:: C++

        .. code-block:: cpp

            RCLCPP_WARN_SKIPFIRST(node->get_logger(), "My log message %d", 4);
            RCLCPP_WARN_STREAM_SKIPFIRST(node->get_logger(), "My log message " << 4);

    .. group-tab:: Python

        .. code-block:: python

            num = 4
            node.get_logger().warning('My log message {0}'.format(num), skip_first=True)

节流日志
^^^^^^^^

以下代码会输出 ERROR 级别的日志消息，但每秒最多输出一次。

指定消息间隔的参数以毫秒为单位，应使用整数类型，以便转换为 rcutils_duration_value_t（int64_t）：

.. tabs::

    .. group-tab:: C++

        .. code-block:: cpp

            RCLCPP_ERROR_THROTTLE(node->get_logger(), *node->get_clock(), 1000, "My log message %d", 4);
            RCLCPP_ERROR_STREAM_THROTTLE(node->get_logger(), *node->get_clock(), 1000, "My log message " << 4);

    .. group-tab:: Python

        .. code-block:: python

            num = 4
            node.get_logger().error(f'My log message {num}', throttle_duration_sec=1)

跳过第一次的节流日志
^^^^^^^^^^^^^^^^^^^^

以下代码会输出 DEBUG 级别日志，每秒最多一次，并跳过第一次执行：

.. tabs::

    .. group-tab:: C++

        .. code-block:: cpp

            RCLCPP_DEBUG_SKIPFIRST_THROTTLE(node->get_logger(), *node->get_clock(), 1000, "My log message %d", 4);

    .. group-tab:: Python

        .. code-block:: python

            num = 4
            node.get_logger().debug(f'My log message {num}', skip_first=True, throttle_duration_sec=1.0)

日志演示
--------

该演示展示不同类型的日志调用，以及如何在本地和外部配置不同 Logger 的严重级别。

启动演示：

.. code-block:: console

   $ ros2 run logging_demo logging_demo_main

运行一段时间后，会看到各种具有不同属性的日志调用输出。初始情况下，只会显示 INFO 及以上严重级别（WARN、ERROR、FATAL）的消息。第一条消息只会记录一次，即使程序每次迭代都会执行到该行，这是该日志调用本身的行为。

日志目录配置
------------

可以通过两个环境变量配置日志目录：ROS_LOG_DIR 和 ROS_HOME。规则如下：

* 如果 ROS_LOG_DIR 已设置且非空，则使用 ROS_LOG_DIR。
* 否则使用 ROS_HOME/log；如果 ROS_HOME 未设置或为空，则使用 ~/.ros/log。

例如，将日志目录设置为 ~/my_logs：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ export ROS_LOG_DIR=~/my_logs
      $ ros2 run logging_demo logging_demo_main

  .. group-tab:: macOS

    .. code-block:: console

      $ export ROS_LOG_DIR=~/my_logs
      $ ros2 run logging_demo logging_demo_main

  .. group-tab:: Windows

    .. code-block:: console

      $ set "ROS_LOG_DIR=~/my_logs"
      $ ros2 run logging_demo logging_demo_main

之后可以在 ~/my_logs/ 下找到日志。

也可以设置 ROS_HOME，日志目录将相对于该目录，即 $ROS_HOME/log。ROS_HOME 旨在为需要基础目录的工具提供统一位置。注意，此时 ROS_LOG_DIR 必须未设置或为空。

例如，将 ROS_HOME 设置为 ~/my_ros_home：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ export ROS_HOME=~/my_ros_home
      $ ros2 run logging_demo logging_demo_main

  .. group-tab:: macOS

    .. code-block:: console

      $ export ROS_HOME=~/my_ros_home
      $ ros2 run logging_demo logging_demo_main

  .. group-tab:: Windows

    .. code-block:: console

      $ set "ROS_HOME=~/my_ros_home"
      $ ros2 run logging_demo logging_demo_main

之后可以在 ~/my_ros_home/log/ 下找到日志。

Logger 级别配置：程序内
------------------------

运行 10 次迭代后，演示会将 Logger 级别设置为 DEBUG，因此会输出更多消息。

部分调试消息会触发额外函数或表达式的计算，而这些计算在 DEBUG 日志调用未启用时会被跳过。有关演示中日志调用的详细说明，请参阅§源码 <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/logging_demo/src/logger_usage_component.cpp>§_，完整的日志调用列表请参阅 rclcpp 日志文档。

Logger 级别配置：外部配置
-------------------------

未来将提供通用方式，在运行时从外部配置 Logger（类似 ROS 1 中通过远程过程调用配置 Logger 的 rqt_logger_level）。**目前 ROS 2 尚未正式支持这一通用概念。**

在此期间，本演示提供了一个示例服务，可以从外部请求配置进程中已知名称的 Logger 级别。

前面启动的演示已经运行了该服务。要将演示 Logger 的级别重新设置为 INFO，可以调用：

.. code-block:: console

   $ ros2 service call /config_logger logging_demo/srv/ConfigLogger "{logger_name: 'logger_usage_demo', level: INFO}"

只要知道 Logger 名称，该服务就可以配置进程中运行的任意 Logger，包括 ROS 2 核心中的 Logger，例如通用客户端库 rcl。要为 rcl 启用 DEBUG 日志，调用：

.. code-block:: console

   $ ros2 service call /config_logger logging_demo/srv/ConfigLogger "{logger_name: 'rcl', level: DEBUG}"

此时应该能看到 rcl 开始输出调试信息。

使用 Logger 配置组件
^^^^^^^^^^^^^^^^^^^^

响应 Logger 配置请求的服务器被开发为一个组件，因此可以将其添加到现有的基于组合的系统中。

例如，如果使用容器运行节点，为了配置 Logger，只需请求容器额外加载 logging_demo::LoggerConfig 组件。

先正常启动组件容器：

Shell 1：

.. code-block:: console

   $ ros2 run rclcpp_components component_container

Shell 2：

.. code-block:: console

   $ ros2 component load /ComponentManager composition composition::Talker

需要启用调试日志时，在 Shell 2 中加载 LoggerConfig 组件：

.. code-block:: console

   $ ros2 component load /ComponentManager logging_demo logging_demo::LoggerConfig

最后，通过空名称的 Logger 配置所有尚未设置级别的 Logger。已经显式配置严重级别的 Logger 不会受到影响。

.. code-block:: console

   $ ros2 service call /config_logger logging_demo/srv/ConfigLogger "{logger_name: '', level: DEBUG}"

此时，进程中此前尚未设置级别的 Logger（包括 ROS 2 核心）都应该开始输出调试信息。

Logger 级别配置：命令行
-----------------------

从 ROS 2 Bouncy 版本开始，可以通过命令行配置尚未显式设置严重级别的 Logger。使用以下参数重新启动演示：

.. code-block:: console

   $ ros2 run logging_demo logging_demo_main --ros-args --log-level debug

该命令会将所有未设置 Logger 的默认严重级别设为 DEBUG。你应该能看到演示本身和 ROS 2 核心 Logger 输出调试信息。

从 ROS 2 Galactic 版本开始，也可以通过命令行配置单个 Logger 的严重级别：

.. code-block:: console

   $ ros2 run logging_demo logging_demo_main --ros-args --log-level logger_usage_demo:=debug

控制台输出格式
--------------

如果希望输出格式包含更多或更少的信息，可以使用 RCUTILS_CONSOLE_OUTPUT_FORMAT 环境变量。例如，要额外输出时间戳和日志调用位置，请停止演示并设置该环境变量后重新启动：

.. code-block:: console

   $ export RCUTILS_CONSOLE_OUTPUT_FORMAT="[{severity} {time}] [{name}]: {message} ({function_name}() at {file_name}:{line_number})"
   $ ros2 run logging_demo logging_demo_main

每条消息都会额外显示时间戳、函数名、文件名和行号。time 选项仅从 ROS 2 Bouncy 版本开始支持。

控制台输出着色
--------------

默认情况下，输出目标为终端时会启用颜色。如果希望强制启用或禁用着色，可以使用 RCUTILS_COLORIZED_OUTPUT 环境变量。例如：

.. code-block:: console

   $ export RCUTILS_COLORIZED_OUTPUT=0
   $ ros2 run logging_demo logging_demo_main

设置为 1 可强制启用颜色。现在应该能看到 debug、warn、error 和 fatal 日志不再着色。

.. note::

   在 Linux 和 macOS 上强制启用颜色后，如果将输出重定向到文件，ANSI 转义颜色代码也会写入文件。Windows 使用控制台 API 实现着色，强制启用失败时会产生警告。默认行为会自动检查输出是否为控制台，因此不建议强制启用颜色。

.. note::

   如果通过 ros2 launch 启动多个节点，默认情况下没有节点连接到活动终端（除非设置 emulate_tty=True）。因此，要让 ros2 launch 输出彩色日志，需要显式设置 RCUTILS_COLORIZED_OUTPUT=1。

控制台输出默认流
----------------

在 Foxy 及更新版本中，所有调试级别的输出默认写入 stderr。可以将 RCUTILS_LOGGING_USE_STDOUT 环境变量设置为 1，强制将所有输出写入 stdout：

.. code-block:: console

   $ export RCUTILS_LOGGING_USE_STDOUT=1

控制台行缓冲输出
----------------

默认情况下，所有日志输出均不缓冲。可以将 RCUTILS_LOGGING_BUFFERED_STREAM 环境变量设置为 1，强制启用缓冲：

.. code-block:: console

   $ export RCUTILS_LOGGING_BUFFERED_STREAM=1

然后运行：

.. code-block:: console

    $ ros2 run logging_demo logging_demo_main
