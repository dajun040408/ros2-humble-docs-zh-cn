.. redirect-from::

   Guides/Launch-files-migration-guide
   Tutorials/Launch-files-migration-guide
   How-To-Guides/Launch-files-migration-guide

.. _MigratingLaunch:

ROS 1 Launch 文件迁移
======================

.. contents:: 目录
   :depth: 2
   :local:

ROS 1 的 launch 文件始终使用 `XML <https://wiki.ros.org/roslaunch/XML>`__ 文件描述，而 ROS 2 同时支持 XML 和 YAML 文件。ROS 2 还支持 Python launch 脚本，以提供更大的灵活性（参见 `launch 功能包 <https://github.com/ros2/launch/tree/{REPOS_FILE_BRANCH}/launch>`__）。不过，对于常见使用场景，建议优先使用 XML 或 YAML，而不是 Python。

本指南介绍如何编写 ROS 2 XML launch 文件，以便从 ROS 1 平滑迁移。

背景知识
----------

ROS 2 launch 系统的介绍请参阅 :doc:`Launch 系统教程 <../../../Tutorials/Intermediate/Launch/Launch-system>`。


迁移标签
--------------

launch
^^^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/launch>`__.
* ``launch`` 是所有 ROS 2 XML launch 文件的根元素。

node
^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/node>`__.
* 启动一个新节点。
* 与 ROS 1 的区别：

   * ``type`` 属性改为 ``exec``。
   * ``ns`` 属性改为 ``namespace``。
   * ``required="true"`` 改为 ``on_exit="shutdown"``。
   * 以下属性不再支持：``machine``、``respawn_delay``、``clear_params``。

示例
~~~~~~~

.. code-block:: xml

   <launch>
      <node pkg="demo_nodes_cpp" exec="talker"/>
      <node pkg="demo_nodes_cpp" exec="listener"/>
   </launch>

param
^^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/param>`__.
* 用于向节点传递参数。
* ROS 2 中没有全局参数的概念，因此该标签只能嵌套在 ``node`` 标签中使用。ROS 2 不支持部分属性：``type``、``textfile``、``binfile``、``executable``。
* ``command`` 属性现在改为 ``value="$(command '...' )"``。

示例
~~~~~~~

.. code-block:: xml

   <launch>
      <node pkg="demo_nodes_cpp" exec="parameter_event">
         <param name="foo" value="5"/>
      </node>
   </launch>

类型推断规则
~~~~~~~~~~~~~~~~~~~~

以下示例展示了参数的编写方式：

.. code-block:: xml

   <node pkg="my_package" exec="my_executable" name="my_node">
      <!--A string parameter with value "1"-->
      <param name="a_string" value="'1'"/>
      <!--A integer parameter with value 1-->
      <param name="an_int" value="1"/>
      <!--A float parameter with value 1.0-->
      <param name="a_float" value="1.0"/>
      <!--A string parameter with value "asd"-->
      <param name="another_string" value="asd"/>
      <!--Another string parameter, with value "asd"-->
      <param name="string_with_same_value_as_above" value="'asd'"/>
      <!--Another string parameter, with value "'asd'"-->
      <param name="quoted_string" value="\'asd\'"/>
      <!--A list of strings, with value ["asd", "bsd", "csd"]-->
      <param name="list_of_strings" value="asd, bsd, csd" value-sep=", "/>
      <!--A list of ints, with value [1, 2, 3]-->
      <param name="list_of_ints" value="1,2,3" value-sep=","/>
      <!--Another list of strings, with value ["1", "2", "3"]-->
      <param name="another_list_of_strings" value="'1';'2';'3'" value-sep=";"/>
      <!--A list of strings using an strange separator, with value ["1", "2", "3"]-->
      <param name="strange_separator" value="'1'//'2'//'3'" value-sep="//"/>
   </node>

参数分组
~~~~~~~~~~~~~~~~~~

在 ROS 2 中，``param`` 标签允许嵌套。例如：

.. code-block:: xml

   <node pkg="my_package" exec="my_executable" name="my_node" namespace="/an_absoulute_ns">
      <param name="group1">
         <param name="group2">
            <param name="my_param" value="1"/>
         </param>
         <param name="another_param" value="2"/>
      </param>
   </node>

上述配置将创建两个参数：

* 节点 ``/an_absolute_ns/my_node`` 中创建值为 ``1`` 的参数 ``group1.group2.my_param``。
* 节点 ``/an_absolute_ns/my_node`` 中创建值为 ``2`` 的参数 ``group1.another_param``。

也可以直接使用完整参数名称：

.. code-block:: xml

   <node pkg="my_package" exec="my_executable" name="my_node" namespace="/an_absoulute_ns">
      <param name="group1.group2.my_param" value="1"/>
      <param name="group1.another_param" value="2"/>
   </node>

rosparam
^^^^^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/rosparam>`__.
* 从 YAML 文件加载参数。
* 该功能已由 ``param`` 标签中的 ``from`` 属性取代。

示例
~~~~~~~

.. code-block:: xml

   <node pkg="my_package" exec="my_executable" name="my_node" namespace="/an_absoulute_ns">
      <param from="/path/to/file"/>
   </node>

remap（重映射）
^^^^^^^^^^^^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/remap>`__.
* 用于向节点传递重映射规则。
* 该标签只能在 ``node`` 标签内部使用。

示例
~~~~~~~

.. code-block:: xml

   <launch>
      <node pkg="demo_nodes_cpp" exec="talker">
         <remap from="chatter" to="my_topic"/>
      </node>
      <node pkg="demo_nodes_cpp" exec="listener">
         <remap from="chatter" to="my_topic"/>
      </node>
   </launch>

include（包含）
^^^^^^^^^^^^^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/include>`__.
* 用于包含另一个 launch 文件。
* 与 ROS 1 的区别：

   * ROS 1 中可用, included content was scoped.
     In ROS 2, it's not.
     这意味着 ``arg`` 标签的值会传播到被包含的 launch 文件中，效果类似于 ROS 1 中设置 ``pass_all_args="true"``。
     但这种传播只适用于被包含的 launch 文件中具有默认值的参数。
     必需参数必须显式传递。
     若要限制作用域，请将 include 嵌套在 ``group`` 标签中（另请参阅 ``group`` 的 ``scoped`` 和 ``forwarding`` 属性）。
   * 不支持 ``ns`` 属性。解决方法请参阅 ``push_ros_namespace`` 标签示例。
   * 嵌套在 ``include`` 标签中的 ``arg`` 标签现在应使用 ``let``。不过，目前仍然支持 ``arg``。
   * 嵌套在 ``include`` 标签中的 ``let`` 标签不支持条件属性（``if``、``unless``）或 ``description`` 属性。
   * 不支持嵌套的 ``env`` 标签，可以改用 ``set_env`` 和 ``unset_env``。
   * ``clear_params`` 和 ``pass_all_args`` 属性均不受支持。ROS 2 launch 的行为相当于将 ``pass_all_args`` 设置为 true（见上文）。

示例s
~~~~~~~~

请参阅“替换 include 标签”一节。

arg
^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/arg>`__.
* ``arg`` 用于声明 launch 参数，或在使用 ``include`` 标签时传递参数。
* 与 ROS 1 的区别：

   * 不允许使用 ``value`` 属性，应改用 ``let`` 标签。
   * ``doc`` 改为 ``description``。
   * 当嵌套在 ``include`` 标签中时：

      * 使用 ``let`` 替代 ``arg``。
      * 不允许使用 ``if``、``unless`` 和 ``description`` 属性。

示例
~~~~~~~

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

向 launch 文件传递参数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在上面的 XML launch 文件中，``topic_name`` 的默认值为 ``chatter``，但可以通过命令行配置。假设上述配置保存在 ``mylaunch.xml`` 文件中，可以使用以下命令指定不同的话题名称：

.. code-block:: console

   $ ros2 launch mylaunch.xml topic_name:=custom_topic_name

有关传递命令行参数的更多信息，请参阅 :doc:`使用替换 <../../../Tutorials/Intermediate/Launch/Using-Substitutions>`。

env
^^^

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/env>`__.
* 设置环境变量。
* 该功能已由 ``env``、``set_env`` 和 ``unset_env`` 替代：

   * ``env`` 只能嵌套在 ``node`` 或 ``executable`` 标签中，且不支持 ``if`` 和 ``unless``。
   * ``set_env`` 可以嵌套在根标签 ``launch`` 或 ``group`` 标签中。它接受与 ``env`` 相同的属性，也支持 ``if`` 和 ``unless``。
   * ``unset_env`` 用于取消设置环境变量。它接受 ``name`` 属性和条件判断。

示例
~~~~~~~

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

* `ROS 1 中可用 <https://wiki.ros.org/roslaunch/XML/group>`__.
* 用于限制 launch 配置的作用域，通常与 ``let``、``include`` 和 ``push_ros_namespace`` 标签配合使用。
* 与 ROS 1 的区别：

   * 没有 ``ns`` 属性，可使用新增的 ``push_ros_namespace`` 标签作为替代方案。
   * 不提供 ``clear_params`` 属性。
   * 不接受 ``remap`` 或 ``param`` 标签作为子元素。
   * 新增两个属性：``scoped`` 和 ``forwarding``（默认均为 true）。如果 ``scoped`` 为 false，则 group 不会创建新的变量作用域，因此在 group 内对变量执行的操作也会影响外部变量。如果 ``forwarding`` 为 false，则 group 内无法访问外部 launch 配置（``arg``）。这可用于隔离被包含的 launch 文件，避免参数名称冲突。

.. _launch-prefix-example:

示例
~~~~~~~

``launch-prefix`` configuration affects both ``executable`` and ``node`` tags' actions.
在此示例中，如果参数 ``use_time_prefix_in_talker`` 的值为 ``1``，则只会为 talker 节点添加 ``time`` 前缀。

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

目前尚不支持。

test
^^^^

目前尚不支持。

ROS 2 中新增的标签
------------------

set_env 和 unset_env
^^^^^^^^^^^^^^^^^^^^^

请参阅 ``env`` 标签的说明。

push_ros_namespace（推送 ROS 命名空间）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``include`` 和 ``group`` 标签均不接受 ``ns`` 属性。可以使用以下 action 作为替代方案：

.. code-block:: xml

   <!-Other tags-->
   <group>
      <push_ros_namespace namespace="my_ns"/>
      <!--Nodes here are namespaced with "my_ns".-->
      <!--If there is an include action here, its nodes will also be namespaced.-->
      <push_ros_namespace namespace="another_ns"/>
      <!--Nodes here are namespaced with "another_ns/my_ns".-->
      <push_ros_namespace namespace="/absolute_ns"/>
      <!--Nodes here are namespaced with "/absolute_ns".-->
      <!--The following node receives an absolute namespace, so it will ignore the others previously pushed.-->
      <!--The full path of the node will be /asd/my_node.-->
      <node pkg="my_pkg" exec="my_executable" name="my_node" namespace="/asd"/>
   </group>
   <!--Nodes outside the group action won't be namespaced.-->
   <!-Other tags-->

let
^^^

它用于替代带有 value 属性的 ``arg`` 标签。

.. code-block:: xml

   <let name="foo" value="asd"/>

在 ROS 2 中，``let`` 和 ``arg`` 用途不同：

* ``let`` 用于设置 launch 配置值。
* ``arg`` 用于声明 launch 参数/配置，并可选择提供默认值。该值也可以通过 CLI 或包含该 launch 文件时单独设置。如果没有设置参数值，则使用提供的默认值；如果没有默认值，则会报告错误。

executable（可执行程序）
^^^^^^^^^^^^^^^^^^^^^^^^

用于运行任意可执行程序。

示例
~~~~~~~

.. code-block:: xml

   <executable cmd="ls -las" cwd="/var/log" name="my_exec" launch-prefix="something" output="screen" shell="true">
      <env name="LD_LIBRARY" value="/lib/some.so"/>
   </executable>

替换 include 标签
------------------------

如果希望像 ROS 1 一样在**命名空间**下包含 launch 文件，则必须将 ``include`` 标签嵌套在 ``group`` 标签中。

.. code-block:: xml

   <group>
      <include file="another_launch_file"/>
   </group>

接下来，不再使用 ``ns`` 属性，而是添加 ``push_ros_namespace`` action 标签来指定命名空间：

.. code-block:: xml

   <group>
      <push_ros_namespace namespace="my_ns"/>
      <include file="another_launch_file"/>
   </group>

只有在指定命名空间时，才需要将 ``include`` 标签嵌套在 ``group`` 标签中。

替换表达式
-------------

Documentation about ROS 1's substitutions can be found in `roslaunch XML wiki <https://wiki.ros.org/roslaunch/XML>`__.
替换表达式的语法没有变化，仍采用 ``$(substitution-name arg1 arg2 ...)`` 的形式。
There are, however, some changes w.r.t. ROS 1:

* ``env`` 和 ``optenv`` 已统一由 ``env`` 替代。如果环境变量不存在，``$(env <NAME>)`` 会失败。``$(env <NAME> '')`` 的行为与 ROS 1 的 ``$(optenv <NAME>)`` 相同。``$(env <NAME> <DEFAULT>)`` 的行为与 ROS 1 的 ``$(env <NAME> <DEFAULT>)`` 或 ``$(optenv <NAME> <DEFAULT>)`` 相同。
* ``find`` 已替换为 ``find-pkg-share``（用于替换为已安装功能包的 share 目录）。此外，``find-pkg-prefix`` 可返回已安装功能包的根目录。
* 新增 ``exec-in-pkg`` 替换表达式，例如：``$(exec-in-pkg <exec_name> <package_name>)``。
* 新增 ``find-exec`` 替换表达式。
* ``arg`` 已替换为 ``var``。它会查找通过 ``arg`` 或 ``let`` 标签定义的配置。
* ``eval`` 和 ``dirname`` 替换表达式中的字符串值需要使用转义字符，例如 ``if="$(eval '\'$(var variable)\' == \'val1\'')"``。也可以使用 ``&quot;`` 等 HTML 转义字符。
* ``eval`` 不会将配置（``arg``）作为局部 Python 变量传入，必须通过 ``$(var name)`` 访问。
* 在 ROS 2 中，``eval`` 的参数必须是带引号的字符串。因此，表达式内部的引号也必须转义。

类型推断规则
--------------------

``param`` 标签“类型推断规则”小节中介绍的规则适用于任何属性。
例如：

.. code-block:: xml

   <!--Setting a string value to an attribute expecting an int will raise an error.-->
   <tag1 attr-expecting-an-int="'1'"/>
   <!--Correct version.-->
   <tag1 attr-expecting-an-int="1"/>
   <!--Setting an integer in an attribute expecting a string will raise an error.-->
   <tag2 attr-expecting-a-str="1"/>
   <!--Correct version.-->
   <tag2 attr-expecting-a-str="'1'"/>
   <!--Setting a list of strings in an attribute expecting a string will raise an error.-->
   <tag3 attr-expecting-a-str="asd, bsd" str-attr-sep=", "/>
   <!--Correct version.-->
   <tag3 attr-expecting-a-str="don't use a separator"/>

部分属性接受多种类型，例如 ``param`` 标签的 ``value`` 属性。通常，``int``（或 ``float``）类型的参数也接受 ``str``，之后 action 会先执行替换，再尝试将其转换为 ``int``（或 ``float``）。
