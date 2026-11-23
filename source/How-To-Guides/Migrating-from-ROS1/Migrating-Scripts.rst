脚本与命令行迁移
==================

ROS CLI
-------

在 ROS 1 中，执行不同操作需要使用独立命令，例如 `rosrun`、`rosparam` 等。

在 ROS 2 中，统一使用顶层命令 `ros2`，所有操作都作为它的子命令，例如 `ros2 run`、`ros2 param` 等。

ROS CLI 参数
------------

在 ROS 1 中，节点参数直接写在命令行中。

在 ROS 2 中，参数应放在 `--ros-args` 之后，并以 `--` 结束（如果后面没有其他参数，末尾的双短横线可以省略）。

名称重映射与 ROS 1 类似，采用 `from:=to` 的形式，但必须在前面加上 `--remap`（或 `-r`）标志。例如：

.. code-block:: console

   $ ros2 run some_package some_ros_executable --ros-args -r foo:=bar

参数采用类似语法，使用 `--param`（或 `-p`）标志：

.. code-block:: console

   $ ros2 run some_package some_ros_executable --ros-args -p my_param:=value

注意，这与 ROS 1 中使用前导下划线的方式不同。

要修改节点名称，请使用 `__node`（ROS 1 中对应的是 `__name`）：

.. code-block:: console

   $ ros2 run some_package some_ros_executable --ros-args -r __node:=new_node_name

注意这里使用了 `-r` 标志。修改命名空间 `__ns` 时也需要使用相同的重映射标志：

.. code-block:: console

   $ ros2 run some_package some_ros_executable --ros-args -r __ns:=/new/namespace

ROS 2 中没有与以下 ROS 1 参数对应的功能：

- `__log`（但可以使用 `--log-config-file` 提供 Logger 配置文件）
- `__ip`
- `__hostname`
- `__master`

更多信息请参阅 `设计文档 <https://design.ros2.org/articles/ros_command_line_arguments.html>`_。

快速参考
~~~~~~~~

+------------+-------------+----------------+
| 功能       | ROS 1       | ROS 2          |
+============+=============+================+
| 名称重映射 | foo:=bar    | -r foo:=bar    |
+------------+-------------+----------------+
| 参数       | _foo:=bar   | -p foo:=bar    |
+------------+-------------+----------------+
| 节点名称   | __name:=foo | -r __node:=foo |
+------------+-------------+----------------+
| 命名空间   | __ns:=foo   | -r __ns:=foo   |
+------------+-------------+----------------+
