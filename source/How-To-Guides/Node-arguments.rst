.. redirect-from::

    Node-arguments
    Guides/Node-arguments
    Tutorials/Node-arguments

通过命令行向节点传递 ROS 参数
=============================

.. contents:: 目录
   :depth: 2
   :local:

所有 ROS 节点都支持一组参数，用于重新配置各种属性。例如，可以配置节点名称和命名空间、节点使用的话题/服务名称，以及节点参数。

所有 ROS 专用参数都必须放在 ``--ros-args`` 标志之后：

.. code-block:: console

   $ ros2 run my_package node_executable --ros-args ...

更多详细信息请参阅 `ROS 命令行参数设计文档 <https://design.ros2.org/articles/ros_command_line_arguments.html>`__。

名称重映射
----------

可以使用以下语法重映射节点内部的名称（例如话题和服务）：

``-r <old name>:=<new name>``

节点本身的名称和命名空间可以通过以下方式重映射：

* ``-r __node:=<new node name>``
* ``-r __ns:=<new node namespace>``

请注意，这些重映射属于“静态”重映射，在节点整个生命周期内都会生效。节点启动后动态重映射名称的功能目前尚不支持。

有关重映射参数的更多细节（并非所有功能都已实现），请参阅 `静态重映射设计文档 <https://design.ros2.org/articles/static_remapping.html>`__。

示例
^^^^

以下命令会将 ``talker`` 节点的名称设置为 ``my_talker``，并将其发布话题从默认的 ``chatter`` 重映射为 ``my_topic``。

命名空间必须以正斜杠开头。下面的命令将命名空间设置为 ``/demo``，因此话题会创建在该命名空间中（``/demo/my_topic``），而不是创建在全局命名空间（``/my_topic``）中。

.. code-block:: console

  $ ros2 run demo_nodes_cpp talker --ros-args -r __ns:=/demo -r __node:=my_talker -r chatter:=my_topic

向指定节点传递重映射参数
~~~~~~~~~~~~~~~~~~~~~~~~

如果在同一个进程中运行多个节点（例如使用 :doc:`组件组合 <../Concepts/Intermediate/About-Composition>`），可以在重映射参数前添加节点名称前缀，将参数传递给指定节点。

例如，以下命令会将重映射参数分别传递给指定节点：

.. code-block:: console

  $ ros2 run composition manual_composition --ros-args -r talker:__node:=my_talker -r listener:__node:=my_listener

以下示例会同时修改节点名称并重映射话题。请注意，节点名称和命名空间的变更始终先于话题重映射执行：

.. code-block:: console

  $ ros2 run composition manual_composition --ros-args -r talker:__node:=my_talker -r my_talker:chatter:=my_topic -r listener:__node:=my_listener -r my_listener:chatter:=my_topic

Logger 配置
-----------

请参阅 :doc:`日志页面 <../Tutorials/Demos/Logging-and-logger-configuration>` 中 ``--log-level`` 参数的用法。

参数
----

.. _NodeArgsParameters:

直接从命令行设置参数
^^^^^^^^^^^^^^^^^^^^

可以使用以下语法直接从命令行设置参数：

.. code-block:: console

  $ ros2 run package_name executable_name --ros-args -p param_name:=param_value

例如，可以运行：

.. code-block:: console

  $ ros2 run demo_nodes_cpp parameter_blackboard --ros-args -p some_int:=42 -p "a_string:=Hello world" -p "some_lists.some_integers:=[1, 2, 3, 4]" -p "some_lists.some_doubles:=[3.14, 2.718]"

其他节点可以获取这些参数值，例如：

.. code-block:: console

  $ ros2 param list parameter_blackboard
  a_string
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  qos_overrides./parameter_events.publisher.history
  qos_overrides./parameter_events.publisher.reliability
  some_int
  some_lists.some_doubles
  some_lists.some_integers
  use_sim_time

从 YAML 文件设置参数
^^^^^^^^^^^^^^^^^^^^

也可以通过命令行传入 YAML 文件来设置参数。

`YAML 文件语法示例 <https://github.com/ros2/rcl/tree/{REPOS_FILE_BRANCH}/rcl_yaml_param_parser>`__。

例如，将以下内容保存为 ``demo_params.yaml``：

.. code-block:: yaml

  parameter_blackboard:
      ros__parameters:
          some_int: 42
          a_string: "Hello world"
          some_lists:
              some_integers: [1, 2, 3, 4]
              some_doubles : [3.14, 2.718]

  /**:
    ros__parameters:
      wildcard_full: "Full wildcard for any namespaces and any node names"

  /**/parameter_blackboard:
    ros__parameters:
      wildcard_namespace: "Wildcard for a specific node name under any namespace"

  /*:
    ros__parameters:
      wildcard_nodename_root_namespace: "Wildcard for any node names, but only in root namespace"

.. note::

   节点名称和命名空间可以使用通配符：

   * ``*`` 匹配由斜杠（``/``）分隔的单个令牌。
   * ``**`` 匹配零个或多个由斜杠分隔的令牌。
   * 不支持部分匹配，例如 ``foo*``。

然后，需要在节点中声明这些参数，可以使用 `declare_parameter <http://docs.ros.org/en/{DISTRO}/p/rclcpp/generated/classrclcpp_1_1Node.html#_CPPv4N6rclcpp4Node17declare_parameterERKNSt6stringERKN6rclcpp14ParameterValueERKN14rcl_interfaces3msg19ParameterDescriptorEb>`__ 或 `declare_parameters <http://docs.ros.org/en/{DISTRO}/p/rclcpp/generated/classrclcpp_1_1Node.html#_CPPv4I0EN6rclcpp4Node18declare_parametersENSt6vectorI10ParameterTEERKNSt6stringERKNSt3mapINSt6stringENSt4pairI10ParameterTN14rcl_interfaces3msg19ParameterDescriptorEEEEEb>`__。

也可以将节点设置为自动声明通过命令行覆盖传入的参数，参阅 `automatically_declare_parameters_from_overrides <http://docs.ros.org/en/{DISTRO}/p/rclcpp/generated/classrclcpp_1_1NodeOptions.html#_CPPv4NK6rclcpp11NodeOptions47automatically_declare_parameters_from_overridesEv>`__。

然后运行以下命令：

.. code-block:: console

  $ ros2 run demo_nodes_cpp parameter_blackboard --ros-args --params-file demo_params.yaml

其他节点可以获取这些参数值，例如：

.. code-block:: console

  $ ros2 param list parameter_blackboard
  a_string
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  qos_overrides./parameter_events.publisher.history
  qos_overrides./parameter_events.publisher.reliability
  some_int
  some_lists.some_doubles
  some_lists.some_integers
  use_sim_time
  wildcard_full
  wildcard_namespace
  wildcard_nodename_root_namespace
