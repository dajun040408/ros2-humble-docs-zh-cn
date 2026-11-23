.. _SinglePkgInterface:

.. redirect-from::

    Rosidl-Tutorial
    Tutorials/Single-Package-Define-And-Use-Interface

在单个功能包中定义和使用自定义接口
==================================

**目标：** 学习在 ROS 2 中实现自定义接口的其他方式。

**教程级别：** 初级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

在 :doc:§此前的教程 <./Custom-ROS2-Interfaces>§ 中，你已经学习了如何创建自定义 msg 和 srv 接口。

最佳实践是将接口定义放在独立接口功能包中，但有时也可以在同一个功能包中声明、创建和使用接口。

目前接口只能在 CMake 功能包中定义。不过，CMake 功能包也可以通过 §ament_cmake_python§ 包含 Python 库和节点。因此，可以在一个功能包中同时定义接口和 Python 节点。本教程为简化说明，使用 CMake 功能包和 C++ 节点。

本教程重点介绍 msg 接口，但相同步骤也适用于其他接口类型。

前置条件
--------

建议先阅读 :doc:§自定义 ROS 2 接口基础教程 <./Custom-ROS2-Interfaces>§。还需要安装 ROS 2、创建工作空间，并了解如何创建功能包。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

在工作空间的 §src§ 目录中创建 §more_interfaces§ 功能包，并创建消息目录：

.. code-block:: console

   $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 more_interfaces
   $ mkdir more_interfaces/msg

2. 创建 msg 文件
^^^^^^^^^^^^^^^^

在 §more_interfaces/msg§ 中创建 §AddressBook.msg§：

.. code-block:: text

   uint8 PHONE_TYPE_HOME=0
   uint8 PHONE_TYPE_WORK=1
   uint8 PHONE_TYPE_MOBILE=2

   string first_name
   string last_name
   string phone_number
   uint8 phone_type

该消息包含以下字段：

* §first_name§：string 类型。
* §last_name§：string 类型。
* §phone_number§：string 类型。
* §phone_type§：uint8 类型，并定义了多个命名常量。

消息定义中的字段也可以设置默认值。更多接口定制方式请参阅 :doc:§接口概念 <../../Concepts/Basic/About-Interfaces>§。

2.1 构建 msg 文件
~~~~~~~~~~~~~~~~~

在 §package.xml§ 中添加：

.. code-block:: xml

   <buildtool_depend>rosidl_default_generators</buildtool_depend>
   <exec_depend>rosidl_default_runtime</exec_depend>
   <member_of_group>rosidl_interface_packages</member_of_group>

构建阶段需要 §rosidl_default_generators§，运行阶段需要 §rosidl_default_runtime§。

在 §CMakeLists.txt§ 中查找消息代码生成包：

.. code-block:: cmake

   find_package(rosidl_default_generators REQUIRED)

然后使用 §rosidl_generate_interfaces()§ 注册消息文件：

.. code-block:: cmake

   rosidl_generate_interfaces(${PROJECT_NAME}
     "msg/AddressBook.msg"
   )

2.2 在同一功能包中使用接口
~~~~~~~~~~~~~~~~~~~~~~~~~~

接口生成后，可以在同一功能包的 C++ 节点中包含生成的头文件，并使用对应命名空间访问消息类型。生成的 C++ 类型命名空间由功能包名称和 §msg§ 组成，例如 §more_interfaces::msg::AddressBook§。

在 §CMakeLists.txt§ 中，使用 §rosidl_get_typesupport_target§ 获取类型支持 target，并将其链接到使用接口的可执行程序。确保生成接口的配置位于 §ament_package()§ 之前。

3. 构建和运行
^^^^^^^^^^^^^

在工作空间根目录构建：

.. code-block:: console

   $ colcon build --packages-up-to more_interfaces

source 工作空间后，可以使用：

.. code-block:: console

   $ ros2 interface show more_interfaces/msg/AddressBook

检查生成的接口定义。

总结
----

本教程介绍了如何在单个 CMake 功能包中创建 msg 接口、配置 rosidl 生成流程，并在同一功能包的节点中使用生成的接口。
