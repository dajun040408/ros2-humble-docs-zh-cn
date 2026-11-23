.. redirect-from::

    Tutorials/Parameters/Understanding-ROS2-Parameters

.. _ROS2Params:

理解参数
========

**目标：** 学习如何在 ROS 2 中获取、设置、保存和重新加载参数。

**教程级别：** 初学者

**预计时间：** 5 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景知识
--------

参数是节点的配置值，可以将其理解为节点设置。节点可以将参数保存为整数、浮点数、布尔值、字符串和列表。在 ROS 2 中，每个节点都维护自己的参数。有关参数的更多背景知识，请参阅 :doc:`参数概念文档 <../../../Concepts/Basic/About-Parameters>`。

前置条件
--------

本教程使用 :doc:`turtlesim 功能包 <../Introducing-Turtlesim/Introducing-Turtlesim>`。请记得在每个新打开的终端中 source ROS 2：:doc:`配置 ROS 2 环境 <../Configuring-ROS2-Environment>`。

任务
----

1 启动环境
^^^^^^^^^^

启动两个 turtlesim 节点：``/turtlesim`` 和 ``/teleop_turtle``。

打开两个终端，分别运行：

.. code-block:: console

    $ ros2 run turtlesim turtlesim_node

    $ ros2 run turtlesim turtle_teleop_key

2 ros2 param list
^^^^^^^^^^^^^^^^^

要查看节点所属的参数，请打开新终端并输入：

.. code-block:: console

  $ ros2 param list
  /teleop_turtle:
    qos_overrides./parameter_events.publisher.depth
    qos_overrides./parameter_events.publisher.durability
    qos_overrides./parameter_events.publisher.history
    qos_overrides./parameter_events.publisher.reliability
    scale_angular
    scale_linear
    use_sim_time
  /turtlesim:
    background_b
    background_g
    background_r
    qos_overrides./parameter_events.publisher.depth
    qos_overrides./parameter_events.publisher.durability
    qos_overrides./parameter_events.publisher.history
    qos_overrides./parameter_events.publisher.reliability
    use_sim_time

每个节点都有 ``use_sim_time`` 参数，并非只有 turtlesim 才有。

从参数名称可以看出，``/turtlesim`` 的参数似乎通过 RGB 颜色值控制 turtlesim 窗口的背景颜色。

要确定参数的类型，可以使用 ``ros2 param get`` 命令。

3 ros2 param get
^^^^^^^^^^^^^^^^

要显示参数的类型和当前值，请使用：

.. code-block:: console

  $ ros2 param get <node_name> <parameter_name>

查看 ``/turtlesim`` 节点的 ``background_g`` 参数当前值：

.. code-block:: console

  $ ros2 param get /turtlesim background_g
  Integer value is: 86

由此可知，``background_g`` 保存的是整数值。

如果对 ``background_r`` 和 ``background_b`` 运行相同命令，将分别得到 ``69`` 和 ``255``。

4 ros2 param set
^^^^^^^^^^^^^^^^

要在运行时修改参数值，请使用：

.. code-block:: console

  $ ros2 param set <node_name> <parameter_name> <value>

下面修改 ``/turtlesim`` 的背景颜色：

.. code-block:: console

  $ ros2 param set /turtlesim background_r 150
  Set parameter successful

turtlesim 窗口的背景颜色应该会发生变化：

.. image:: images/set.png

使用 ``set`` 命令设置参数只会修改当前会话中的参数值，不会永久保存。不过，你可以保存当前设置，并在下次启动节点时重新加载。

5 ros2 param dump
^^^^^^^^^^^^^^^^^

使用以下命令可以查看节点当前的所有参数值：

.. code-block:: console

  $ ros2 param dump <node_name>

默认情况下，命令会将内容打印到标准输出（stdout）；也可以将参数值重定向到文件，以便之后使用。

要将 ``/turtlesim`` 的当前参数配置保存到 ``turtlesim.yaml`` 文件中，请运行：

.. code-block:: console

  $ ros2 param dump /turtlesim > turtlesim.yaml

当前 Shell 所在工作目录中会生成一个新文件。打开该文件，可以看到以下内容：

.. code-block:: yaml

  /turtlesim:
    ros__parameters:
      background_b: 255
      background_g: 86
      background_r: 150
      qos_overrides:
        /parameter_events:
          publisher:
            depth: 1000
            durability: volatile
            history: keep_last
            reliability: reliable
      use_sim_time: false

导出参数后，就可以在将来重新加载节点时恢复相同的参数配置。

6 ros2 param load
^^^^^^^^^^^^^^^^^

可以使用以下命令从文件向当前正在运行的节点加载参数：

.. code-block:: console

  $ ros2 param load <node_name> <parameter_file>

要将通过 ``ros2 param dump`` 生成的 ``turtlesim.yaml`` 文件加载到 ``/turtlesim`` 节点，请输入：

.. code-block:: console

  $ ros2 param load /turtlesim turtlesim.yaml
  Set parameter background_b successful
  Set parameter background_g successful
  Set parameter background_r successful
  Set parameter qos_overrides./parameter_events.publisher.depth failed: parameter 'qos_overrides./parameter_events.publisher.depth' cannot be set because it is read-only
  Set parameter qos_overrides./parameter_events.publisher.durability failed: parameter 'qos_overrides./parameter_events.publisher.durability' cannot be set because it is read-only
  Set parameter qos_overrides./parameter_events.publisher.history failed: parameter 'qos_overrides./parameter_events.publisher.history' cannot be set because it is read-only
  Set parameter qos_overrides./parameter_events.publisher.reliability failed: parameter 'qos_overrides./parameter_events.publisher.reliability' cannot be set because it is read-only
  Set parameter use_sim_time successful

.. note::

   只读参数只能在节点启动时修改，运行过程中无法修改。因此，加载时会对 ``qos_overrides`` 参数给出一些警告。

7 在节点启动时加载参数文件
^^^^^^^^^^^^^^^^^^^^^^^^^^

如果希望使用保存的参数值启动同一个节点，可以使用：

.. code-block:: console

  $ ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>

这与平时启动 turtlesim 的命令相同，只是增加了 ``--ros-args`` 和 ``--params-file`` 标志，后面跟随要加载的文件名。

停止当前运行的 turtlesim 节点，然后使用保存的参数重新启动：

.. code-block:: console

  $ ros2 run turtlesim turtlesim_node --ros-args --params-file turtlesim.yaml

turtlesim 窗口应该会像往常一样出现，但背景颜色会变成之前设置的紫色。

.. note::

   在节点启动时使用参数文件，会更新所有参数，包括只读参数。

总结
----

节点使用参数定义默认配置值。你可以从命令行获取（``get``）和设置（``set``）参数值，也可以将参数设置保存到文件中，以便在之后的会话中重新加载。

后续步骤
--------

回到 ROS 2 通信方式，下一篇教程将介绍 :doc:`动作 <../Understanding-ROS2-Actions/Understanding-ROS2-Actions>`。
