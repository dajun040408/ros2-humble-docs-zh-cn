ROS 1 接口迁移
==============

.. contents:: 目录
   :depth: 2
   :local:

在 ROS 2 中，消息、服务和动作统称为 interfaces（接口）。

接口定义
--------

消息文件必须以 .msg 结尾，并放在 msg 子目录中。
服务文件必须以 .srv 结尾，并放在 srv 子目录中。
动作文件必须以 .action 结尾，并放在 action 子目录中。

这些文件可能需要更新，以符合 ROS 接口定义规范：http://design.ros2.org/articles/legacy_interface_definition.html。
部分基本类型已被移除；ROS 1 中的内置类型 duration 和 time 已被普通消息定义取代，必须从 builtin_interfaces 功能包中使用：https://github.com/ros2/rcl_interfaces/tree/{REPOS_FILE_BRANCH}/builtin_interfaces。
此外，与 ROS 1 相比，ROS 2 对命名约定的要求更加严格。
更多信息请参阅接口概念说明：https://docs.ros.org/en/humble/Concepts/Basic/About-Interfaces.html。

构建接口
--------

ROS 2 中接口的构建方式与 ROS 1 有较大差异。
接口只能从包含 CMakeLists.txt 的功能包中构建。
如果正在开发纯 Python 功能包，则应将接口放到另一个只包含接口的功能包中（这本身也是最佳实践）。
更多信息请参阅自定义接口教程：https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.html。

将接口功能包迁移到 ROS 2
^^^^^^^^^^^^^^^^^^^^^^^^

在 package.xml 中：

* 添加 <buildtool_depend>rosidl_default_generators</buildtool_depend>。
* 添加 <exec_depend>rosidl_default_runtime</exec_depend>。
* 添加 <member_of_group>rosidl_interface_packages</member_of_group>。
* 对每个依赖的消息功能包，添加 <depend>message_package</depend>。

在 CMakeLists.txt 中：

* 启用 C++17：

.. code-block:: cmake

   set(CMAKE_CXX_STANDARD 17)

* 添加 find_package(rosidl_default_generators REQUIRED)。
* 对每个依赖的消息功能包，添加 find_package(message_package REQUIRED)，并将 CMake 函数调用 generate_messages 替换为 rosidl_generate_interfaces。

这样就可以使用 rosidl_generate_interfaces 替代 add_message_files 和 add_service_files。原先用于列出所有消息和服务文件的语句可以删除。
