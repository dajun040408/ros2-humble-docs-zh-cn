接口迁移
========

.. contents:: 目录
   :depth: 2
   :local:

在 ROS 2 中，消息、服务和动作统称为接口（interfaces）。

接口定义
--------

消息文件必须以 `.msg` 结尾，并放在 `msg` 子目录中。服务文件必须以 `.srv` 结尾，并放在 `srv` 子目录中。动作文件必须以 `.action` 结尾，并放在 `action` 子目录中。

这些文件可能需要更新，以符合 `ROS 接口定义规范 <http://design.ros2.org/articles/legacy_interface_definition.html>`_。部分原始类型已被移除；ROS 1 中的内置类型 `duration` 和 `time` 已被普通消息定义替代，必须使用 `builtin_interfaces` 软件包中的对应类型。

此外，ROS 2 的部分命名约定比 ROS 1 更严格。更多信息请参阅 :doc:`接口概念文章 <../../Concepts/Basic/About-Interfaces>`。

构建接口
--------

ROS 2 中构建接口的方式与 ROS 1 有很大区别。接口只能从包含 `CMakeLists.txt` 的功能包中构建。

如果你正在开发纯 Python 功能包，则应将接口放在另一个专门包含接口的功能包中（这本身也是一种推荐实践）。更多信息请参阅 :doc:`自定义 ROS 2 接口教程 <../../Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces>`。

将接口功能包迁移到 ROS 2
^^^^^^^^^^^^^^^^^^^^^^^^^

在 `package.xml` 中：

* 添加 `<buildtool_depend>rosidl_default_generators</buildtool_depend>`。
* 添加 `<exec_depend>rosidl_default_runtime</exec_depend>`。
* 添加 `<member_of_group>rosidl_interface_packages</member_of_group>`。
* 对每个依赖的消息功能包，添加 `<depend>message_package</depend>`。

在 `CMakeLists.txt` 中：

* 启用 C++17：

.. code-block:: cmake

   set(CMAKE_CXX_STANDARD 17)

* 添加 `find_package(rosidl_default_generators REQUIRED)`。
* 对每个依赖的消息功能包，添加 `find_package(message_package REQUIRED)`，并将 `generate_messages` 替换为 `rosidl_generate_interfaces`。

这样就可以替代 `add_message_files` 和 `add_service_files` 对所有消息及服务文件的逐项列举，因此这些声明可以删除。
