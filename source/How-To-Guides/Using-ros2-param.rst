使用 ``ros2 param`` 命令行工具
===============================

.. contents:: 目录
   :depth: 1
   :local:

ROS 2 参数可以通过一组服务进行获取、设置、列出和描述，具体请参阅 :doc:`参数概念文档 <../Concepts/Basic/About-Parameters>`。``ros2 param`` 命令行工具是对这些服务调用的封装，使用户能够方便地在命令行中操作参数。

``ros2 param list``
---------------------

该命令会列出指定节点上的所有可用参数。如果未指定节点，则列出系统中所有可发现节点的参数。

列出指定节点上的所有参数：

.. code-block:: console

  $ ros2 param list /my_node

列出系统中所有节点上的参数（在复杂网络中，这可能需要较长时间）：

.. code-block:: console

  $ ros2 param list

``ros2 param get``
--------------------

该命令用于获取指定节点上某个参数的值。

获取节点上的参数值：

.. code-block:: console

  $ ros2 param get /my_node use_sim_time

``ros2 param set``
--------------------

该命令用于设置指定节点上某个参数的值。对于大多数参数，新值的类型必须与已有参数类型相同。

设置节点上的参数值：

.. code-block:: console

  $ ros2 param set /my_node use_sim_time false

命令行传入的值采用 YAML 格式，因此可以使用任意 YAML 表达式。不过，这也意味着某些表达式的解析结果可能与预期不同。

例如，如果节点 ``my_node`` 上的参数 ``my_string`` 类型为字符串，下面的命令将无法正常工作：

.. code-block:: console

  $ ros2 param set /my_node my_string off

这是因为 YAML 会将 ``off`` 解释为布尔值，而 ``my_string`` 的类型是字符串。

可以使用 YAML 显式指定字符串的语法解决这一问题，例如：

.. code-block:: console

  $ ros2 param set /my_node my_string '!!str off'

此外，YAML 支持异构列表，例如同时包含字符串、布尔值和整数。但 ROS 2 参数不支持异构列表，因此任何包含多种类型的 YAML 列表都会被解释为字符串。

假设节点 ``my_node`` 上的参数 ``my_int_array`` 类型为整数数组，以下命令将无法正常工作：

.. code-block:: console

  $ ros2 param set /my_node my_int_array '[foo,off,1]'

如果目标参数是字符串类型，则以下命令可以正常工作：

.. code-block:: console

  $ ros2 param set /my_node my_string '[foo,off,1]'

``ros2 param delete``
-----------------------

该命令用于从指定节点中删除参数。但请注意，它只能删除动态参数，不能删除已声明的参数。更多信息请参阅 :doc:`参数概念文档 <../Concepts/Basic/About-Parameters>`。

.. code-block:: console

  $ ros2 param delete /my_node my_string

``ros2 param describe``
--------------------------

该命令用于显示指定节点上某个参数的文本描述：

.. code-block:: console

  $ ros2 param describe /my_node use_sim_time

``ros2 param dump``
----------------------

该命令会以 YAML 文件格式输出指定节点上的所有参数。之后可以使用该输出文件，以相同参数重新运行节点：

.. code-block:: console

  $ ros2 param dump /my_node

``ros2 param load``
----------------------

该命令会将 YAML 文件中的参数值加载到指定节点。也就是说，可以在运行时重新加载之前通过 ``ros2 param dump`` 导出的参数值：

.. code-block:: console

  $ ros2 param load /my_node my_node.yaml
