.. redirect-from::

    About-ROS-2-Parameters
    Concepts/About-ROS-2-Parameters

参数
====

.. contents:: 目录
   :local:

概述
----

ROS 2 参数与单个节点关联。参数用于在节点启动时或运行过程中配置节点，而无需修改代码。参数的生命周期与节点的生命周期绑定（不过，节点也可以实现某种持久化机制，以便在重启后重新加载参数值）。

参数通过节点名称、节点命名空间、参数名称和参数命名空间进行寻址。参数命名空间是可选的。

每个参数由键（key）、值（value）和描述符（descriptor）组成。键是字符串，值可以是以下类型之一：``bool``、``int64``、``float64``、``string``、``byte[]``、``bool[]``、``int64[]``、``float64[]`` 或 ``string[]``。默认情况下，参数描述符为空，但也可以包含参数说明、取值范围、类型信息及其他约束。

有关 ROS 参数的动手教程，请参阅 :doc:`理解 ROS 2 参数教程 <../../Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters>`。

参数背景知识
------------

声明参数
^^^^^^^^

默认情况下，节点需要*声明（declare）*其生命周期内允许使用的所有参数。这样可以在节点启动时明确参数的类型和名称，从而降低后续发生配置错误的可能性。有关如何在节点中声明和使用参数的教程，请参阅 :doc:`C++ 参数教程 <../../Tutorials/Beginner-Client-Libraries/Using-Parameters-In-A-Class-CPP>` 或 :doc:`Python 参数教程 <../../Tutorials/Beginner-Client-Libraries/Using-Parameters-In-A-Class-Python>`。

对于某些类型的节点，无法提前确定所有参数。在这种情况下，可以在实例化节点时将 ``allow_undeclared_parameters`` 设置为 ``true``，这样即使参数尚未声明，也可以在节点上获取和设置这些参数。

参数类型
^^^^^^^^

ROS 2 节点上的每个参数都具有概述中列出的某一种预定义参数类型。默认情况下，运行时尝试更改已声明参数的类型会失败。这可以避免常见错误，例如将布尔值写入整数类型的参数。

如果某个参数确实需要支持多种类型，并且使用该参数的代码能够处理这些类型，则可以修改默认行为。声明参数时，应使用 ``ParameterDescriptor``，并将其成员变量 ``dynamic_typing`` 设置为 ``true``。

参数回调
^^^^^^^^

ROS 2 节点可以注册两种不同类型的回调，以便在参数发生变化时收到通知。这两种回调都是可选的。

第一种称为“设置参数（set parameter）”回调，可以通过节点 API 中的 ``add_on_set_parameters_callback`` 注册。回调接收一个由不可变 ``Parameter`` 对象组成的列表，并返回 ``rcl_interfaces/msg/SetParametersResult``。这种回调的主要用途是检查即将发生的参数变更，并明确拒绝不符合要求的变更。

.. note::

   “设置参数”回调不应产生副作用。由于多个“设置参数”回调可以串联执行，单个回调无法知道后续回调是否会拒绝此次更新。例如，如果某个回调修改了所属类的内部状态，而后续回调拒绝了参数更新，就可能导致类内部状态与实际参数值不一致。若要在参数成功变更后执行回调，请参阅下面介绍的第二种回调。

第二种称为“参数事件（on parameter event）”回调，可以通过参数客户端 API 中的 ``on_parameter_event`` 设置。该回调接收一个 ``rcl_interfaces/msg/ParameterEvent`` 对象，不返回任何内容。当输入事件中的所有参数完成声明、修改或删除后，就会调用此回调。它的主要用途是在参数变更成功后，让用户能够对已接受的变更作出响应。

与参数交互
----------

ROS 2 节点可以通过节点 API 执行参数操作，具体可参阅 :doc:`C++ 参数教程 <../../Tutorials/Beginner-Client-Libraries/Using-Parameters-In-A-Class-CPP>` 或 :doc:`Python 参数教程 <../../Tutorials/Beginner-Client-Libraries/Using-Parameters-In-A-Class-Python>`。

外部进程则可以通过节点实例化时默认创建的参数服务执行参数操作。默认创建的服务如下：

* ``/node_name/describe_parameters``：服务类型为 ``rcl_interfaces/srv/DescribeParameters``。给定一组参数名称，返回与这些参数关联的描述符列表。
* ``/node_name/get_parameter_types``：服务类型为 ``rcl_interfaces/srv/GetParameterTypes``。给定一组参数名称，返回这些参数对应的类型列表。
* ``/node_name/get_parameters``：服务类型为 ``rcl_interfaces/srv/GetParameters``。给定一组参数名称，返回这些参数的值列表。
* ``/node_name/list_parameters``：服务类型为 ``rcl_interfaces/srv/ListParameters``。给定可选的参数前缀列表，返回具有相应前缀的可用参数。如果前缀列表为空，则返回全部参数。
* ``/node_name/set_parameters``：服务类型为 ``rcl_interfaces/srv/SetParameters``。给定参数名称和值列表，尝试在节点上设置这些参数，并逐项返回设置结果；部分参数可能成功，部分参数可能失败。
* ``/node_name/set_parameters_atomically``：服务类型为 ``rcl_interfaces/srv/SetParametersAtomically``。给定参数名称和值列表，尝试一次性设置全部参数，并返回一个整体结果。如果其中一个参数设置失败，则全部参数设置都会失败。

运行节点时设置初始参数值
------------------------

运行节点时，可以通过单独的命令行参数或 YAML 文件设置初始参数值。示例请参阅 :ref:`NodeArgsParameters`。

启动节点时设置初始参数值
------------------------

通过 ROS 2 启动系统运行节点时，也可以设置初始参数值。有关如何在 launch 中指定参数，请参阅 :doc:`相关文档 <../../Tutorials/Intermediate/Launch/Using-ROS2-Launch-For-Large-Projects>`。

运行时修改参数值
----------------

对于已经运行的节点，通常使用 ``ros2 param`` 命令与参数交互。``ros2 param`` 使用上文介绍的参数服务 API 执行各种操作。具体用法请参阅 :doc:`参数命令应用指南 <../../How-To-Guides/Using-ros2-param>`。

从 ROS 1 迁移
-------------

:doc:`Launch 文件迁移指南 <../../How-To-Guides/Migrating-from-ROS1/Migrating-Launch-Files>` 介绍如何将 ROS 1 中的 ``param`` 和 ``rosparam`` launch 标签迁移到 ROS 2。

:doc:`参数迁移指南 <../../How-To-Guides/Migrating-from-ROS1/Migrating-Parameters>` 介绍如何将 ROS 1 参数迁移到 ROS 2。
