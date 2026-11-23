.. redirect-from::

   Guides/Launch-files-migration-guide
   Tutorials/Launch-files-migration-guide
   How-To-Guides/Launch-files-migration-guide

.. _MigratingLaunch:

迁移启动文件
============

.. contents:: 目录
   :depth: 2
   :local:

ROS 1 的启动文件始终使用 `XML` 文件描述，而 ROS 2 同时支持 XML 和 YAML 文件。ROS 2 还支持 Python 启动脚本，以提供更高的灵活性（参见 `launch 软件包 <https://github.com/ros2/launch/tree/{REPOS_FILE_BRANCH}/launch>`_）。不过，对于典型使用场景，建议优先使用 XML 和 YAML，而不是 Python。

本指南介绍如何编写 ROS 2 XML 启动文件，以便更轻松地从 ROS 1 迁移。

背景知识
--------

有关 ROS 2 启动系统的说明，请参阅 :doc:`Launch 系统教程 <../../../Tutorials/Intermediate/Launch/Launch-system>`。

迁移标签
--------

launch
^^^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/launch>`_。
* `launch` 是 ROS 2 XML 启动文件的根元素。

node
^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/node>`_。
* 用于启动一个新节点。
* 与 ROS 1 相比的差异：

   * `type` 属性现在改为 `exec`。
   * `ns` 属性现在改为 `namespace`。
   * `required="true"` 现在改为 `on_exit="shutdown"`。
   * 以下属性不再提供：`machine`、`respawn_delay`、`clear_params`。

示例
~~~~

.. code-block:: xml

   <launch>
      <node pkg="demo_nodes_cpp" exec="talker"/>
      <node pkg="demo_nodes_cpp" exec="listener"/>
   </launch>

param
^^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/param>`_。
* 用于向节点传递参数。
* ROS 2 中没有全局参数的概念，因此只能嵌套在 `node` 标签中使用。
* ROS 2 不支持部分属性：`type`、`textfile`、`binfile`、`executable`。
* `command` 属性现在写作 `value="$(command '...' )"`。

示例
~~~~

.. code-block:: xml

   <launch>
      <node pkg="demo_nodes_cpp" exec="parameter_event">
         <param name="foo" value="5"/>
      </node>
   </launch>

类型推断规则
~~~~~~~~~~~~

以下是参数的书写示例：

.. code-block:: xml

   <node pkg="my_package" exec="my_executable" name="my_node">
      <!-- 字符串参数，值为 "1" -->
      <param name="a_string" value="'1'"/>
      <!-- 整数参数，值为 1 -->
      <param name="an_int" value="1"/>
      <!-- 浮点数参数，值为 1.0 -->
      <param name="a_float" value="1.0"/>
      <!-- 字符串参数，值为 "asd" -->
      <param name="another_string" value="asd"/>
      <!-- 另一个字符串参数，值为 "asd" -->
      <param name="string_with_same_value_as_above" value="'asd'"/>
      <!-- 字符串参数，值为 "'asd'" -->
      <param name="quoted_string" value="\'asd\'"/>
      <!-- 字符串列表，值为 ["asd", "bsd", "csd"] -->
      <param name="list_of_strings" value="asd, bsd, csd" value-sep=", "/>
      <!-- 整数列表，值为 [1, 2, 3] -->
      <param name="list_of_ints" value="1,2,3" value-sep=","/>
      <!-- 另一个字符串列表，值为 ["1", "2", "3"] -->
      <param name="another_list_of_strings" value="'1';'2';'3'" value-sep=";"/>
      <!-- 使用特殊分隔符的字符串列表，值为 ["1", "2", "3"] -->
      <param name="strange_separator" value="'1'//'2'//'3'" value-sep="//"/>
   </node>

参数分组
~~~~~~~~

在 ROS 2 中，`param` 标签允许嵌套。例如：

.. code-block:: xml

   <node pkg="my_package" exec="my_executable" name="my_node" namespace="/an_absoulute_ns">
      <param name="group1">
         <param name="group2">
            <param name="my_param" value="1"/>
         </param>
         <param name="another_param" value="2"/>
      </param>
   </node>

这将创建两个参数：

* `group1.group2.my_param`，值为 `1`，由节点 `/an_absoulute_ns/my_node` 托管。
* `group1.another_param`，值为 `2`，由节点 `/an_absoulute_ns/my_node` 托管。

也可以直接使用完整参数名称：

.. code-block:: xml

   <node pkg="my_package" exec="my_executable" name="my_node" namespace="/an_absoulute_ns">
      <param name="group1.group2.my_param" value="1"/>
      <param name="group1.another_param" value="2"/>
   </node>

rosparam
^^^^^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/rosparam>`_。
* 用于从 YAML 文件加载参数。
* 在 ROS 2 中由 `param` 标签的 `from` 属性替代。

示例
~~~~

.. code-block:: xml

   <node pkg="my_package" exec="my_executable" name="my_node" namespace="/an_absoulute_ns">
      <param from="/path/to/file"/>
   </node>

remap
^^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/remap>`_。
* 用于向节点传递重映射规则。
* 只能在 `node` 标签内部使用。

示例
~~~~

.. code-block:: xml

   <launch>
      <node pkg="demo_nodes_cpp" exec="talker">
         <remap from="chatter" to="my_topic"/>
      </node>
      <node pkg="demo_nodes_cpp" exec="listener">
         <remap from="chatter" to="my_topic"/>
      </node>
   </launch>

include
^^^^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/include>`_。
* 用于包含另一个启动文件。
* 与 ROS 1 相比的差异：

   * ROS 1 中被包含的内容具有作用域，而 ROS 2 中没有。这意味着 `arg` 标签的值会传递到被包含的启动文件中，效果相当于 ROS 1 中设置 `pass_all_args="true"`。不过，这种传递只适用于被包含启动文件中具有默认值的参数。必需参数必须显式传递。可以将 include 嵌套在 `group` 标签中进行作用域隔离（另请参阅 `group` 的 `scoped` 和 `forwarding` 属性）。
   * 不支持 `ns` 属性。可以使用 `push_ros_namespace` 标签作为替代方案。
   * 嵌套在 `include` 中的 `arg` 标签现在改为 `let`，但目前仍支持 `arg`。
   * 嵌套在 `include` 中的 `let` 标签不支持条件属性（`if`、`unless`）或 `description` 属性。
   * 不支持嵌套的 `env` 标签，可以改用 `set_env` 和 `unset_env`。
   * 不支持 `clear_params` 和 `pass_all_args` 属性。ROS 2 启动系统的行为相当于 `pass_all_args` 设置为 true（见上文）。

示例
~~~~

请参阅后文的“替换 include 标签”。

arg
^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/arg>`_。
* `arg` 用于声明启动参数，或在使用 `include` 标签时传递参数。
* 与 ROS 1 相比的差异：

   * 不允许使用 `value` 属性，应改用 `let` 标签。
   * `doc` 属性现在改为 `description`。
   * 嵌套在 `include` 标签中时：
      * 使用 `let` 替代 `arg`。
      * 不允许使用 `if`、`unless` 和 `description` 属性。

示例
~~~~

.. code-block:: xml

   <launch>
      <arg name="topic_name" default="chatter"/>
      <node pkg="demo_nodes_cpp" exec="talker">
         <remap from="chatter" to="$(var topic_name)"/>
      </node>
      <node pkg="demo_nodes_cpp" exec="listener">
         <remap from="chatter" to="$(var topic_name)"/>
      </node>
   </launch>

向启动文件传递参数
~~~~~~~~~~~~~~~~~~

在上面的 XML 启动文件中，`topic_name` 默认值为 `chatter`，但可以通过命令行修改。假设配置保存在 `mylaunch.xml` 中，可以这样指定其他话题名称：

.. code-block:: console

   $ ros2 launch mylaunch.xml topic_name:=custom_topic_name

有关传递命令行参数的更多信息，请参阅 :doc:`使用替换 <../../../Tutorials/Intermediate/Launch/Using-Substitutions>`。

env
^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/env>`_。
* 用于设置环境变量。
* 在 ROS 2 中由 `env`、`set_env` 和 `unset_env` 替代：

   * `env` 只能嵌套在 `node` 或 `executable` 标签中使用，不支持 `if` 和 `unless`。
   * `set_env` 可以嵌套在根标签 `launch` 或 `group` 标签中。它接受与 `env` 相同的属性，并额外支持 `if` 和 `unless`。
   * `unset_env` 用于取消设置环境变量。它接受 `name` 属性和条件属性。

示例
~~~~

.. code-block:: xml

   <launch>
      <set_env name="MY_ENV_VAR" value="MY_VALUE" if="CONDITION_A"/>
      <set_env name="ANOTHER_ENV_VAR" value="ANOTHER_VALUE" unless="CONDITION_B"/>
      <set_env name="SOME_ENV_VAR" value="SOME_VALUE"/>
      <node pkg="MY_PACKAGE" exec="MY_EXECUTABLE" name="MY_NODE">
         <env name="NODE_ENV_VAR" value="SOME_VALUE"/>
      </node>
      <unset_env name="MY_ENV_VAR" if="CONDITION_A"/>
      <node pkg="ANOTHER_PACKAGE" exec="ANOTHER_EXECUTABLE" name="ANOTHER_NODE"/>
      <unset_env name="ANOTHER_ENV_VAR" unless="CONDITION_B"/>
      <unset_env name="SOME_ENV_VAR"/>
   </launch>

group
^^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/group>`_。
* 用于限制启动配置的作用域。通常与 `let`、`include` 和 `push_ros_namespace` 标签一起使用。
* 与 ROS 1 相比的差异：

   * 没有 `ns` 属性，可以使用新的 `push_ros_namespace` 标签替代。
   * 不提供 `clear_params` 属性。
   * 不接受 `remap` 或 `param` 标签作为子元素。
   * 新增两个属性：`scoped` 和 `forwarding`（默认都为 true）。如果 `scoped` 为 false，组不会引入新的变量作用域，因此组内对变量执行的操作也会影响外部变量。如果 `forwarding` 为 false，则外部启动配置（`arg`）不会在组内生效。这对于隔离被包含的启动文件、避免参数名称冲突很有用。

.. _launch-prefix-example:

示例
~~~~

`launch-prefix` 配置会同时影响 `executable` 和 `node` 标签的操作。以下示例仅在 `use_time_prefix_in_talker` 参数为 `1` 时，为 talker 添加 `time` 前缀：

.. code-block:: xml

   <launch>
      <arg name="use_time_prefix_in_talker" default="0"/>
      <group>
         <let name="launch-prefix" value="time" if="$(var use_time_prefix_in_talker)"/>
         <node pkg="demo_nodes_cpp" exec="talker"/>
      </group>
      <node pkg="demo_nodes_cpp" exec="listener"/>
   </launch>

machine
^^^^^^^

目前不支持。

test
^^^^

目前不支持。

ROS 2 新增标签
--------------

set_env 和 unset_env
^^^^^^^^^^^^^^^^^^^^

请参阅前文 `env` 标签说明。

push_ros_namespace
^^^^^^^^^^^^^^^^^^

`include` 和 `group` 标签不接受 `ns` 属性。可以使用以下操作作为替代方案：

.. code-block:: xml

   <!-- 其他标签 -->
   <group>
      <push_ros_namespace namespace="my_ns"/>
      <!-- 此处的节点使用命名空间 my_ns。 -->
      <!-- 如果此处包含 include 操作，其节点也会使用该命名空间。 -->
      <push_ros_namespace namespace="another_ns"/>
      <!-- 此处的节点使用命名空间 another_ns/my_ns。 -->
      <push_ros_namespace namespace="/absolute_ns"/>
      <!-- 此处的节点使用命名空间 /absolute_ns。 -->
      <!-- 以下节点使用绝对命名空间，因此会忽略此前推入的其他命名空间。 -->
      <!-- 节点完整路径为 /asd/my_node。 -->
      <node pkg="my_pkg" exec="my_executable" name="my_node" namespace="/asd"/>
   </group>
   <!-- group 操作之外的节点不会使用上述命名空间。 -->
   <!-- 其他标签 -->

let
^^^

`let` 是带有 `value` 属性的 `arg` 标签的替代方案：

.. code-block:: xml

   <let name="foo" value="asd"/>

在 ROS 2 中，`let` 和 `arg` 用途不同：

* `let` 设置一个启动配置值。
* `arg` 声明启动参数/配置，并可选地提供默认值。该值可以通过命令行或包含该启动文件时单独设置。如果未设置值，则使用已提供的默认值；如果没有默认值，则会报告错误。

executable
^^^^^^^^^^

该标签允许运行任意可执行程序。

示例
~~~~

.. code-block:: xml

   <executable cmd="ls -las" cwd="/var/log" name="my_exec" launch-prefix="something" output="screen" shell="true">
      <env name="LD_LIBRARY" value="/lib/some.so"/>
   </executable>

替换 include 标签
-----------------

如果希望像 ROS 1 一样在某个**命名空间**下包含启动文件，必须将 `include` 标签嵌套在 `group` 标签中：

.. code-block:: xml

   <group>
      <include file="another_launch_file"/>
   </group>

然后，不再使用 `ns` 属性，而是添加 `push_ros_namespace` 操作标签指定命名空间：

.. code-block:: xml

   <group>
      <push_ros_namespace namespace="my_ns"/>
      <include file="another_launch_file"/>
   </group>

只有在需要指定命名空间时，才必须将 `include` 标签嵌套在 `group` 标签中。

替换表达式
----------

有关 ROS 1 替换表达式的文档，请参阅 `roslaunch XML wiki <https://wiki.ros.org/roslaunch/XML>`_。替换表达式语法没有改变，仍然采用 `$(substitution-name arg1 arg2 ...)` 的形式。不过，与 ROS 1 相比有以下变化：

* `env` 和 `optenv` 已由 `env` 替代。`$(env <NAME>)` 在环境变量不存在时会失败。`$(env <NAME> '')` 等价于 ROS 1 的 `$(optenv <NAME>)`。`$(env <NAME> <DEFAULT>)` 等价于 ROS 1 的 `$(env <NAME> <DEFAULT>)` 或 `$(optenv <NAME> <DEFAULT>)`。
* `find` 已由 `find-pkg-share` 替代，用于获取已安装软件包的 share 目录。也可以使用 `find-pkg-prefix` 获取已安装软件包的根目录。
* 新增 `exec-in-pkg` 替换表达式，例如 `$(exec-in-pkg <exec_name> <package_name>)`。
* 新增 `find-exec` 替换表达式。
* `arg` 已由 `var` 替代。它会查找通过 `arg` 或 `let` 标签定义的配置。
* `eval` 和 `dirname` 替换表达式中的字符串值需要使用转义字符，例如 `if="$(eval ''$(var variable)' == 'val1'')"`。也可以使用 HTML 转义字符，例如 `&quot;`。
* `eval` 不会将配置（`arg`）作为本地 Python 变量传递，必须通过 `$(var name)` 访问。
* `eval` 的参数必须是带引号的字符串。因此，表达式内部的引号也必须转义。

类型推断规则
------------

前文 `param` 标签小节中介绍的类型推断规则适用于任何属性。例如：

.. code-block:: xml

   <!-- 为期望整数的属性设置字符串值，会引发错误。 -->
   <tag1 attr-expecting-an-int="'1'"/>
   <!-- 正确写法。 -->
   <tag1 attr-expecting-an-int="1"/>
   <!-- 为期望字符串的属性设置整数，会引发错误。 -->
   <tag2 attr-expecting-a-str="1"/>
   <!-- 正确写法。 -->
   <tag2 attr-expecting-a-str="'1'"/>
   <!-- 为期望字符串的属性设置字符串列表，会引发错误。 -->
   <tag3 attr-expecting-a-str="asd, bsd" str-attr-sep=", "/>
   <!-- 正确写法。 -->
   <tag3 attr-expecting-a-str="don't use a separator"/>

某些属性可以接受多种类型，例如 `param` 标签的 `value` 属性。通常，`int`（或 `float`）类型的参数也可以接受 `str`，之后再由相应操作进行替换，并尝试将其转换为 `int`（或 `float`）。
