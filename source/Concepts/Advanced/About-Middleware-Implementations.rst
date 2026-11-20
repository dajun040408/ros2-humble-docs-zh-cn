.. redirect-from::

   Concepts/About-Middleware-Implementations

ROS 2 中间件实现
==================

.. contents:: 目录
   :local:

.. include:: ../../../global_substitutions.txt

ROS 中间件实现是一组功能包，用于实现 ROS 内部接口的一部分，例如 ``rmw``、``rcl`` 和 ``rosidl`` API。

有关 ROS 2 如何集成不同中间件实现的实践性深入介绍，请参阅 :doc:`中间件实现教程 <../../Tutorials/Advanced/Creating-An-RMW-Implementation>`。

DDS 中间件功能包的通用组件
----------------------------

当前所有 ROS 中间件实现都基于完整或部分 DDS 实现。例如，有一种中间件实现使用 RTI Connext DDS，另一种实现使用 eProsima Fast DDS。因此，大多数基于 DDS 的中间件实现会共享一些功能包。

在 GitHub 上的 `ros2/rosidl_dds <https://github.com/ros2/rosidl_dds>`__ 仓库中，包含以下功能包：

* ``rosidl_generator_dds_idl``：提供从 ``rosidl`` 文件生成 DDS ``.idl`` 文件的工具，例如从 ``.msg``、``.srv`` 文件生成 DDS IDL 文件。

对于包含消息的功能包中定义的每个 ``rosidl`` 文件，``rosidl_generator_dds_idl`` 都会生成对应的 DDS ``.idl`` 文件。目前，基于 DDS 的 ROS 中间件实现会使用这些输出文件，生成特定于 DDS 供应商的预编译类型支持代码。

.. _about-middleware-impls_struct_dds:

ROS 中间件实现的结构
----------------------

ROS 中间件实现通常由同一个代码仓库中的几个功能包组成：

* ``<implementation_name>_cmake_module``：包含用于发现和公开所需依赖项的 CMake 模块。
* ``rmw_<implementation_name>_<language>``：以特定语言（通常为 C++）实现 ``rmw`` API。
* ``rosidl_typesupport_<implementation_name>_<language>``：包含为 ``rosidl`` 文件生成静态类型支持代码的工具，针对特定实现和语言（通常为 C 或 C++）进行定制。

``<implementation_name>_cmake_module`` 功能包包含查找中间件实现所需依赖项的 CMake 模块和函数。例如，``rti_connext_dds_cmake_module`` 会对 RTI Connext DDS 提供的 CMake 模块进行封装，确保所有依赖该模块的功能包选择同一个 RTI Connext DDS 安装版本。类似地，``fastrtps_cmake_module`` 包含用于查找 eProsima Fast DDS 的 CMake 模块，``gurumdds_cmake_module`` 则包含用于查找 GurumNetworks GurumDDS 的 CMake 模块。

并非所有实现都需要这样的功能包。例如，Eclipse Cyclone DDS 已经提供了 CMake 模块，其 RMW 实现可以直接使用，无需额外封装。

``rmw_<implementation_name>_<language>`` 功能包使用特定语言实现 ``rmw`` C API。实现本身可以使用 C++ 编写，但必须将头文件中的符号以 ``extern "C"`` 形式公开，以便 C 应用程序能够链接。

``rosidl_typesupport_<implementation_name>_<language>`` 功能包提供生成特定语言 DDS 代码的生成器。它使用 ``rosidl_generator_dds_idl`` 生成的 ``.idl`` 文件，以及 DDS 供应商提供的 DDS IDL 代码生成器，生成 ROS 消息结构与 DDS 消息结构之间的转换代码。

该生成器还负责为正在使用的消息功能包创建共享库。该共享库与消息功能包中的消息类型以及所使用的 DDS 供应商相关。

如前所述，如果某个 RMW 实现支持消息的运行时解释，则可以使用 ``rosidl_typesupport_introspection_<language>``，而不是供应商专用的类型支持功能包。这种无需提前生成代码、即可通过话题以编程方式发送和接收类型的能力，是通过支持 `DDS X-Types Dynamic Data 标准 <https://www.omg.org/spec/DDS-XTypes/>`__ 实现的。因此，RMW 实现可以提供 X-Types 标准支持，和/或提供针对其 DDS 实现、在编译时生成的类型支持功能包。

以下是一些 RMW 实现代码仓库示例：

* Eclipse Cyclone DDS：`ros2/rmw_cyclonedds <https://github.com/ros2/rmw_cyclonedds>`__。
* Fast DDS：`ros2/rmw_fastrtps_cpp <https://github.com/ros2/rmw_fastrtps_cpp>`__。
* Connext DDS：`ros2/rmw_connextdds <https://github.com/ros2/rmw_connextdds>`__。
* GurumDDS：`ros/rmw_gurumdds <https://github.com/ros/rmw_gurumdds>`__。
