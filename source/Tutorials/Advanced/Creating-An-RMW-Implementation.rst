创建 RMW 实现
==============

**目标：** 学习如何为特定中间件创建新的 ``rmw`` 实现，从底层中间件所需的功能到 RMW 实现细节。

**教程级别：** 高级

**预计时间：** 30 分钟以上

.. contents:: 目录
   :local:

简介
----

ROS 2 架构包含两个主要 :doc:`抽象层 <../../Concepts/Advanced/About-Internal-Interfaces>`。从上到下分别是：

#. 客户端库接口 ``rcl``：为面向用户的 :doc:`客户端库 <../../Concepts/Basic/About-Client-Libraries>` 提供支持，例如 ``rclcpp`` 和 ``rclpy``。
#. 中间件接口 ``rmw``：抽象 :doc:`底层中间件实现 <../../Concepts/Intermediate/About-Different-Middleware-Vendors>`，例如特定 DDS 实现、Zenoh 等。

``rmw`` `API 包含函数级文档 <https://docs.ros.org/en/{DISTRO}/p/rmw/generated/index.html#functions>`_，但缺少对接口功能以及底层中间件需要满足哪些要求的高层说明。

本指南面向希望为特定中间件实现 ``rmw`` 接口的开发者。首先介绍接口及其工作方式，然后介绍中间件实现必须支持的主要概念和功能，最后介绍实现细节，包括如何创建实现骨架以及编写接口函数的建议。

.. note::

   ``design.ros2.org`` 上的 ROS 2 设计文章属于历史文档，可能无法反映 ROS 2 当前状态。但在某些情况下，它们仍可提供有价值的背景信息。

RMW 接口
--------

``rmw`` 接口由 ``rmw`` 功能包中的 `C 头文件 <https://github.com/ros2/rmw/tree/{DISTRO}/rmw/include/rmw>`_ 声明。各个 RMW 实现作为独立功能包，为这些 C 函数提供具体实现。例如，``rmw_fastrtps_cpp`` 为 eProsima Fast DDS 实现该接口。

示例实现
^^^^^^^^

以下 :doc:`RMW 实现 <../../Concepts/Advanced/About-Middleware-Implementations>` 可以作为参考。不同实现具有不同的 `支持级别，相关定义见 REP 2000 <https://reps.openrobotics.org/rep-2000/#support-tiers>`_。

#. DDS：

   #. ``rmw_fastrtps_cpp``、``rmw_fastrtps_dynamic_cpp``：`ros2/rmw_fastrtps <https://github.com/ros2/rmw_fastrtps>`_
   #. ``rmw_cyclonedds_cpp``：`ros2/rmw_cyclonedds <https://github.com/ros2/rmw_cyclonedds>`_
   #. ``rmw_connextdds``：`ros2/rmw_connextdds <https://github.com/ros2/rmw_connextdds>`_
   #. ``rmw_gurumdds_cpp``：`ros2/rmw_gurumdds <https://github.com/ros2/rmw_gurumdds>`_

   * 参阅 :ref:`DDS 实现概述 <about-middleware-impls_struct_dds>`。

#. ``rmw_zenoh_cpp``：`ros2/rmw_zenoh <https://github.com/ros2/rmw_zenoh>`_

   * 参阅 `设计文档 <https://github.com/ros2/rmw_zenoh/blob/{DISTRO}/docs/design.md>`_。

#. ``rmw_email_cpp``：基于电子邮件的实现，仓库为 `christophebedard/rmw_email <https://github.com/christophebedard/rmw_email>`_。

   * 参阅 `底层电子邮件中间件设计文档 <https://christophebedard.com/rmw_email/design/email/>`_ 和 `相关背景博客 <https://christophebedard.com/ros-2-over-email/>`_。

.. _rmw-impl-guide_selection-mechanism:

构建时和运行时 RMW 实现选择机制
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

对实际 RMW 实现的依赖通过 ``rmw_implementation`` `功能包 <https://index.ros.org/p/rmw_implementation/#{DISTRO}>`_ 完成。``rcl`` 等 RMW 接口的使用者依赖 ``rmw`` 功能包，以获取接口头文件和工具函数；同时还依赖 ``rmw_implementation``，以获取实际实现。

默认情况下，ROS 2 允许在运行时选择要使用的 RMW 实现。这便于在同一台机器上比较不同实现，也使 ROS 2 能够分发一套兼容多种 RMW 实现的二进制文件。:doc:`运行时选择实现 <../../How-To-Guides/Working-with-multiple-RMW-implementations>` 通过 ``RMW_IMPLEMENTATION`` 环境变量完成。如果没有设置该变量，则加载默认实现。

``rmw_implementation`` 充当实际 RMW 实现的代理。它会创建占位 RMW 函数；当这些函数被调用时，使用 ``dlopen()`` 加载所选实现对应的库，再通过 ``dlsym()`` 查找对应符号并调用。

该功能包可以在构建时配置默认选项，或禁用运行时选择机制。可以通过 CMake 变量 ``RMW_IMPLEMENTATION``（例如 ``-DRMW_IMPLEMENTATION=rmw_other``）或同名环境变量选择默认实现。

如果构建时只有一个可用实现，或者禁用了运行时选择（``-DRMW_IMPLEMENTATION_DISABLE_RUNTIME_SELECTION=ON``），``rmw_implementation`` 目标就会成为该单一实现的简单 ``INTERFACE`` 库。

由于代理机制，如果某个 RMW 实现没有实现接口中的所有函数，通常只会在运行时符号查找失败时才暴露问题；若禁用运行时选择，则可能在链接阶段失败。

功能
----

本节介绍 ``rmw`` 接口的主要功能，即底层中间件必须支持或处理的内容。根据底层中间件的特性，以及它与接口预期功能的相似程度，RMW 实现可能很简单，也可能需要完成大量适配工作。

对于某些非关键功能或配置选项，实现可以通过 ``rmw_feature_supported()`` 表明不支持，或者返回 ``RMW_RET_UNSUPPORTED``。RMW 实现的特殊行为应尽可能写入文档。

话题、发布/订阅和服务
^^^^^^^^^^^^^^^^^^^^^

:doc:`话题 <../../Concepts/Basic/About-Topics>` 是发布/订阅中间件中的常见概念。不过，ROS 2 有自己的话题命名约定，并通过 ``rmw_validate_full_topic_name()`` 进行验证。RMW 实现只需要使用传入的、已经解析的话题名称。

这可能涉及将 ROS 话题名称转换为底层中间件所支持的格式，或调整名称以满足其约束。例如，DDS 实现通常会将 ``/chatter`` 转换为 ``rt/chatter``，使 DDS 中的 ROS 话题能够与普通 DDS 话题区分开来。详情请参阅 `ROS 2 话题和服务名称到 DDS 概念的映射 <https://design.ros2.org/articles/topic_and_service_names.html#mapping-of-ros-2-topic-and-service-names-to-dds-concepts>`_。

对于 Zenoh，域 ID、解析后的话题名称、话题类型名称和类型哈希会 `编码到底层 Zenoh key 中 <https://github.com/ros2/rmw_zenoh/blob/{DISTRO}/docs/design.md#topic-and-service-name-mapping-to-zenoh-key-expressions>`_，以避免不同 ROS 话题名称和类型之间发生通信。

:doc:`服务 <../../Concepts/Basic/About-Services>` 并不总是由底层中间件原生支持。基于 DDS 的实现通常在发布/订阅之上构建服务：一个请求话题和一个响应话题。[#fn_dds_rpc]_ Zenoh 原生支持通过 `queryables <https://github.com/ros2/rmw_zenoh/blob/{DISTRO}/docs/design.md#service-servers>`_ 实现服务，因此 ``rmw_zenoh_cpp`` 使用该机制。

注意：虽然服务属于 ``rmw`` 接口的一部分，但 :doc:`动作 <../../Concepts/Basic/About-Actions>` 并不属于该接口。动作是 ``rcl`` 层的概念，由 ``rcl_action`` 功能包在服务和发布/订阅之上实现。

节点
^^^^

:doc:`节点 <../../Concepts/Basic/About-Nodes>` 主要是 ROS 的概念。DDS 和 Zenoh 都没有与之对应的原生概念，因此节点在 ``rmw`` 实现中主要是逻辑概念。

如果需要，``rcl`` 会在创建发布/订阅对象时，使用节点命名空间和名称解析话题名称，然后再将其传递给 ``rmw``。RMW 实现只需要确保节点信息被包含在 :ref:`图信息 <rmw-impl-guide_introspection>` 中。

.. _rmw-impl-guide_waitsets:

等待集与等待机制
^^^^^^^^^^^^^^^^

:doc:`执行器 <../../Concepts/Intermediate/About-Executors>` 负责在收到新消息时触发用户提供的回调函数。执行器在客户端库层（``rclcpp``、``rclpy``）实现，但依赖底层中间件通过轮询机制等待新消息。

等待集（wait sets）允许以标准方式同时等待不同实体，例如订阅者、服务客户端和服务端。``rmw_wait()`` `函数 <https://docs.ros.org/en/{DISTRO}/p/rmw/generated/function_rmw_8h_1a5f480dd59075e80288fb596b2951be2b.html>`_ 接收要等待的实体列表以及实现相关的等待集对象。

该函数会将所有实体添加到等待集中，并等待至少一个实体有新数据可用，或者等待超时。随后执行器检查实体列表，确定哪些实体有新数据，并触发相应回调。

关键机制是能够检查某个实体是否就绪，例如订阅者是否有新消息。等待过程就是持续逐个检查实体，直到某个实体就绪或等待超时。

可以查看 ``rmw_email_cpp`` 如何 `实现等待集和等待机制 <https://github.com/christophebedard/rmw_email/blob/72742241d55f306d1dddcaf5dd6a5d6c2d402433/rmw_email_cpp/src/rmw_wait.cpp#L133>`_，并进一步查看底层中间件 ``email``。该中间件较为简单，适合作为理解示例。

获取数据
^^^^^^^^

当 :ref:`执行器完成等待 <rmw-impl-guide_waitsets>`，并且有新消息、请求或响应时，它会从中间件中获取数据，然后触发对应回调。例如，``rmw_take()`` 接收一个订阅者，以及一个类型擦除指针，该指针指向要写入数据的消息实例。

``rmw_email_cpp`` 会从底层电子邮件中间件订阅对象中获取新消息（YAML 字符串），将其转换为 ROS 消息，并写入提供的消息对象。

元数据：GID、时间戳和序列号
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

除了用户指定的数据外，消息发布、服务请求和响应等还会携带相关元数据：

* GID：全局唯一标识符，用于识别实体，例如发布者、订阅者、客户端和服务端。

  * 一个实体的 GID 在 ROS 域内应该是唯一的，并且在本地和远端报告时保持一致。例如，发布者发布消息时的 GID，应与订阅者收到消息时报告的发布者 GID 相同。[#fn_gid_remote_matching]_

* 源时间戳和接收时间戳：分别表示消息发布时间和订阅者接收时间。
* 发布序列号和接收序列号。

服务请求元数据包含发起请求的客户端 GID 和请求序列号。服务响应元数据也包含客户端 GID 和它所响应请求的序列号。

这些元数据通过结构体提供：订阅消息使用 ``rmw_take_with_info()``，服务请求和响应使用 ``rmw_take_request()`` 与 ``rmw_take_response()``。客户端库会对这些信息进行封装，并传递给用户回调。

其中一部分元数据可能由底层中间件原生支持，另一部分则可能需要由 ``rmw`` 实现与应用数据一起封装和传输。例如，DDS 通过 sample info 原生支持发布/订阅的全部元数据，但客户端请求元数据需要由 ``rmw`` 实现与服务响应数据一起封装。

``email`` 中间件原生支持所有这些元数据，并将其包含在标准电子邮件头中，而不是邮件正文中。

.. _rmw-impl-guide_typesupport:

类型支持（Type Support）
^^^^^^^^^^^^^^^^^^^^^^^^

为了连接 ROS 2 :doc:`接口 <../../Concepts/Basic/About-Interfaces>`（尤其是 :doc:`自定义接口 <../Beginner-Client-Libraries/Custom-ROS2-Interfaces>`）与底层中间件，需要一些适配代码。这称为 :ref:`类型支持 <Type Specific Interfaces>`。

发布 ``std_msgs/msg/String`` 消息时，``rmw_publish()`` 只接收一个 ``void *`` 指针。该指针可能指向 C++ 实例、C 实例等。具体如何解释该指针，取决于创建发布者时提供的类型支持信息。

首先，系统会针对每种接口类型和面向用户的语言生成代码，而不依赖底层中间件。例如，对于 ``std_msgs/msg/String``，会生成以下数据结构：

#. C++：``std_msgs/msg/string.hpp`` 头文件，其中包含由 ``rosidl_generator_cpp`` 生成的 ``std_msgs::msg::String`` 类。
#. C：``std_msgs/msg/string.h`` 头文件，其中包含由 ``rosidl_generator_c`` 生成的 ``std_msgs__msg__String`` 结构体。
#. Python：``std_msgs`` 模块，其中包含由 ``rosidl_generator_py`` 生成的 ``std_msgs.msg.String`` 类（它实际上是 C 结构体的包装器）。
#. 其他语言，例如 Rust，也会生成对应结构。

其次，底层中间件需要知道如何解释面向用户的数据结构。这是 ``rmw`` 实现中最关键的部分之一。有两种选择：:ref:`静态类型支持 <internal-interfaces_static-type-support>` 和 :ref:`动态类型支持 <internal-interfaces_dynamic-type-support>`。

静态类型支持会为每种接口生成特定于中间件的代码。例如，``rosidl_typesupport_fastrtps_cpp`` 使用 `Fast CDR <https://github.com/eProsima/Fast-CDR>`_ 将每种接口类型的 C++ 类序列化/反序列化为 CDR，然后由 ``rmw_fastrtps_cpp`` 传递给 Fast DDS。[#fn_ts_fastrtps]_ ``rmw_connextdds`` 和 ``rmw_zenoh_cpp`` 也使用 CDR 进行序列化，因此同样使用该类型支持包。

动态类型支持会生成一小部分与中间件无关的代码，提供每种接口类型的通用信息。[#fn_ts_dynamic]_ 这些信息可以在运行时由任何 ``rmw`` 实现使用，以解释类型擦除的数据指针：字段名称和类型、按字段类型读取或写入字段的函数、获取数组字段大小的函数等。

对于 C++，这就是 ``rosidl_typesupport_introspection_cpp``。例如，``rmw_fastrtps_dynamic_cpp`` 就使用该方式（名称中的 dynamic 即来源于此）。

动态类型支持在运行时通常比静态类型支持慢，因为它需要遍历每个消息字段，判断字段类型并执行处理，例如序列化。静态类型支持则通过为每种接口类型生成代码，提前确定消息处理方式。因此，大多数 ``rmw`` 实现采用静态类型支持。

不过，动态类型支持不需要生成特定于中间件的代码。选择静态还是动态类型支持，是一个与 ``rmw`` 实现本身正交的决定。

``rmw_email_cpp`` 使用动态类型支持，将消息转换为 YAML 字符串，再通过电子邮件发送。它会获取类型支持的内省信息，并将其与消息一起传递给外部/实验性软件包 `dynmsg <https://github.com/osrf/dynamic_message_introspection/>`_，由该软件包将消息转换为 YAML 对象，再转换为字符串，通过底层中间件发送。收到消息时，YAML 字符串会再转换回消息对象。

域 ID
^^^^^

:doc:`域 ID <../../Concepts/Intermediate/About-Domain-ID>` 是在同一物理网络上创建多个独立逻辑网络的一种方式。这是 DDS 的原生功能，但 Zenoh 并不原生支持。

DDS 通过将域 ID 作为网络端口偏移量实现该功能；Zenoh 则将域 ID 作为内部 Zenoh key 的第一个组成部分，该 key 对应每个 ROS 2 话题。

服务质量（QoS）
^^^^^^^^^^^^^^^

ROS 2 的 :doc:`服务质量设置 <../../Concepts/Intermediate/About-Quality-of-Service-Settings>` 很大程度上源自 DDS。基本 QoS 策略（例如 history、depth 和 durability）与 ROS 1 相同，但更高级的策略来自 DDS。不同实现可以选择忽略某些设置。例如，``rmw_zenoh_cpp`` 不实现 deadline 和 lifespan QoS 策略。

两个 QoS 配置文件（例如发布者和订阅者的配置文件）可能不兼容，导致它们无法通信。具体由实现通过 ``rmw_qos_profile_check_compatible()`` 判断。基于 DDS 的实现依赖 ``rmw_dds_common::qos_profile_check_compatible()``，因为 `QoS 配置文件兼容性 <https://github.com/ros2/ros2_documentation/blob/{DISTRO}/source/Concepts/Intermediate/About-Quality-of-Service-Settings.rst>`_ 在 DDS 中是标准功能。

在 Zenoh 中，`QoS 设置基本上不会出现不兼容情况 <https://github.com/ros2/rmw_zenoh/blob/{DISTRO}/docs/design.md#quality-of-service>`_。

为了支持通用的“默认”行为，QoS 策略包含 ``*_SYSTEM_DEFAULT`` 设置（例如 ``rmw_qos_reliability_policy_t`` 的 ``RMW_QOS_POLICY_RELIABILITY_SYSTEM_DEFAULT``），将具体值交由中间件实现决定。之后，可以通过 ``rmw_*_get_actual_qos()`` 函数获取实现实际使用的 QoS 配置。

.. _rmw-impl-guide_introspection:

ROS 图信息内省
^^^^^^^^^^^^^^

节点可以获取其他节点、话题等信息列表。例如，发布者可以知道是否存在订阅其话题的订阅者。ROS 2 CLI 中列出 :doc:`节点 <../Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes>`、:doc:`话题 <../Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics>` 等命令，也使用了相同机制，例如 ``ros2 node list``、``ros2 topic list``。

这由一系列 ``rmw`` 函数支持，例如 ``rmw_get_node_names()``、``rmw_get_topic_names_and_types()``、``rmw_publisher_count_matched_subscriptions()`` 等。

虽然接口没有规定具体实现方式，但 RMW 实现通常会维护 ROS 图缓存。创建新实体（例如节点、发布者、订阅者、服务、客户端）时，实现会将其记录在内部图缓存中，并通过特定于中间件的机制通知其他参与者，以便它们也将该实体添加到缓存中。

图缓存属于 ``rmw`` context，因此会在调用 ``rmw_init()`` 时初始化。该 context 间接属于 ``rclcpp`` context（例如通过 ``rclcpp::init()`` 初始化），因此一个进程中通常只有一个图缓存。

基于 DDS 的 ``rmw`` 实现通过 ``rmw_dds_common`` `功能包 <https://github.com/ros2/rmw_dds_common>`_ 共享图缓存实现。该功能包使用内部话题（通常为 ``ros_discovery_info``）共享新实体信息。

``rmw_zenoh_cpp`` 则会 `创建 Zenoh liveliness token <https://github.com/ros2/rmw_zenoh/blob/{DISTRO}/docs/design.md#graph-cache>`_，其中包含实体类型和信息，并与其他参与者共享。

事件
^^^^

用户可以为发布者和订阅者提供回调函数。当中间件发生某些事件（``rmw_event_type_t``）时，会触发这些回调（实际由客户端库执行）。例如，:ref:`QoS 相关事件 <about-qos_qos-events>` 和发布/订阅匹配事件都可以触发回调。其中一些事件可能由图缓存中的相关变化触发。

安全
^^^^

:doc:`安全 <../../Concepts/Intermediate/About-Security>` 并未在 ``rmw`` 接口中得到完整规范，大部分内容由 :doc:`SROS2 <../Advanced/Security/Introducing-ros2-security>` 规范。接口只在 context 初始化选项 ``rmw_init_options_t`` 中定义了少量安全选项：

#. ``rmw_security_options_t``：包含安全策略（enforce/permissive）以及存放安全工件（即 keystore）的目录路径。这些值由 ``rcl`` 根据 ``ROS_SECURITY_ENABLE``、``ROS_SECURITY_STRATEGY`` 和 ``ROS_SECURITY_KEYSTORE`` 环境变量设置。
#. 要用于当前进程的 keystore 安全 enclave 名称。例如，使用 ``ros2 run`` 运行节点时，可以通过 ``--enclave`` 选项设置。

不过，:doc:`keystore <./Security/The-Keystore>` 目录及其安全 enclave 的结构，实际上基于 DDS Security 规范。因此，通过 ``sros2`` 软件包生成的 :doc:`安全工件 <./Security/Introducing-ros2-security>` 只能直接用于基于 DDS 的 ``rmw`` 实现。

对于 ``rmw_zenoh_cpp``，可以使用 ``zenoh_security_tools`` 软件包，根据 ``sros2`` 生成的工件 `生成 Zenoh 专用安全配置文件 <https://github.com/ros2/rmw_zenoh/tree/{DISTRO}/zenoh_security_tools>`_，并通过 ``ZENOH_SESSION_CONFIG_URI`` 环境变量提供，而不是使用 ``ROS_SECURITY_*`` 环境变量。

实现
----

实现骨架
^^^^^^^^

本节介绍创建新实现功能包所需的基础文件和目录，包括 ``package.xml`` 和 ``CMakeLists.txt`` 中需要进行的特殊配置。

首先按照 :doc:`创建功能包教程 <../../Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>` 创建一个空功能包，然后进行以下修改。

1. ``package.xml``

   1. 定义功能包/实现名称。

      功能包名称也是 RMW 实现名称。它用于通过 ``RMW_IMPLEMENTATION`` 环境变量或 CMake 选项选择实现。名称通常以 ``rmw_`` 开头，后面跟底层中间件名称。大多数 ROS 2 生态系统实现还会添加 ``_cpp`` 后缀，表示使用 C++ 编写，但这并非强制要求。

      示例：``rmw_fastrtps_cpp``、``rmw_cyclonedds_cpp``、``rmw_connextdds``、``rmw_zenoh_cpp`` 和 ``rmw_email_cpp``。

      .. code-block:: xml

         <!-- 替换为实际实现名称 -->
         <name>rmw_IMPLEMENTATION_NAME_cpp</name>

   2. 声明对 ``rmw`` 的依赖，因为该功能包要实现 ``rmw`` 功能包中声明的接口，并使用其中的一些工具函数。

      .. code-block:: xml

         <depend>rmw</depend>

   3. 声明对所需类型支持功能包的依赖。详情请参阅 :ref:`类型支持 <rmw-impl-guide_typesupport>` 部分。

      .. code-block:: xml

         <!-- 根据需要保留或添加 -->
         <depend>rosidl_typesupport_fastrtps_c</depend>
         <depend>rosidl_typesupport_fastrtps_cpp</depend>
         <depend>rosidl_typesupport_introspection_c</depend>
         <depend>rosidl_typesupport_introspection_cpp</depend>

   4. 声明属于 ``rmw_implementation_packages`` 功能包组。

      这样 ``rmw_implementation`` 功能包就可以 `依赖该实现 <https://github.com/ros2/rmw_implementation/blob/4dd5d571a5bfa1a67183acf271dfa442932c7572/rmw_implementation/package.xml#L38>`_，使其与其他实现一起构建。由于没有其他功能包会显式依赖某个 ``rmw`` 实现，因此该机制确保实现能够被构建、发现并在选中时使用。

      .. code-block:: xml

         <member_of_group>rmw_implementation_packages</member_of_group>

2. ``CMakeLists.txt``

   1. 创建库目标。该库必须是共享库。它应依赖 ``rmw`` 以获取头文件和工具函数，还应依赖所需类型支持包以及底层中间件。

      .. code-block:: cmake

         add_library(${PROJECT_NAME} SHARED
           src/file.cpp
           # ...
         )
         target_link_libraries(${PROJECT_NAME} PUBLIC
           rmw::rmw
         )
         target_link_libraries(${PROJECT_NAME} PRIVATE
           rosidl_typesupport_fastrtps_c::rosidl_typesupport_fastrtps_c
           rosidl_typesupport_fastrtps_cpp::rosidl_typesupport_fastrtps_cpp
           rosidl_typesupport_introspection_c::rosidl_typesupport_introspection_c
           rosidl_typesupport_introspection_cpp::rosidl_typesupport_introspection_cpp
           # TODO 添加实现专用依赖，例如底层中间件
         )

   2. 配置实现库目标。

      这一步主要是默认隐藏符号，以隐藏内部符号（即非 ``rmw`` 接口符号）。如果实现使用 C 语言编写（并不常见），需要指定 ``LANGUAGE "C"``。

      .. code-block:: cmake

         configure_rmw_library(${PROJECT_NAME})

   3. 注册 ``rmw`` 实现。

      这会在 :ref:`ament index <ament-cmake-doc_adding-resources>` 中注册该实现，使其能够在构建时（``get_available_rmw_implementations()``、``get_rmw_typesupport()``）或运行时（``ament_index_cpp::get_resources("rmw_typesupport")``）被发现，同时注册该实现支持的语言和类型支持包列表。

      例如，如果该实现只对 C 和 C++ 消息使用类型支持内省（即动态而非静态类型支持），可以这样注册：

      .. code-block:: cmake

         register_rmw_implementation(
           "c:rosidl_typesupport_introspection_c"
           "cpp:rosidl_typesupport_introspection_cpp"
         )

   4. 安装并导出目标。

      .. code-block:: cmake

         install(
           TARGETS ${PROJECT_NAME}
           EXPORT ${PROJECT_NAME}
           ARCHIVE DESTINATION lib
           LIBRARY DESTINATION lib
           RUNTIME DESTINATION bin
         )

         ament_export_targets(${PROJECT_NAME})
         # ament_export_libraries(${PROJECT_NAME})  # 旧式 CMake

实现接口函数
^^^^^^^^^^^^

第一步是定义 ``rmw`` 头文件中声明的 C 接口函数。可以先创建空函数，让它们只返回 ``RMW_RET_OK``，然后按照运行时可能被调用的顺序逐个实现，例如 ``rmw_init()``、``rmw_create_node()``、``rmw_create_publisher()``、``rmw_create_subscription()`` 等。这样可以逐步构建、运行和测试实现。

大多数 ``rmw`` 函数都需要执行输入验证，具体要求由函数文档定义。可以使用一些工具宏简化该工作，例如 ``RMW_CHECK_ARGUMENT_FOR_NULL()`` 和 ``RMW_CHECK_TYPE_IDENTIFIERS_MATCH()``。

``rmw`` 结构体通常包含一个类型擦除指针（有时是 opaque 指针），用于保存 RMW 实现专用数据。例如，``rmw_publisher_t`` 包含一个 ``void * data`` 字段。实现可以在其中保存任意数据，例如指向内部对象的指针。该对象可以封装底层中间件的发布者对象以及类型支持等信息。之后调用 ``rmw_publish()`` 时，就可以通过对应的 ``rmw_publisher_t`` 获取并使用这些数据。

为了避免不同 ``rmw`` 实现错误解释该数据，``rmw_publisher_t`` 还包含 ``implementation_identifier`` 字段，用于记录实现名称。

类型支持
^^^^^^^^

类型支持结构体可能比较难以理解。下面以发布者/订阅者使用的消息类型支持为例。

创建发布者时会调用 ``rmw_create_publisher()``，该函数接收一个类型支持信息句柄：``const rosidl_message_type_support_t *``。这是基础的、与语言相关的类型支持：``rosidl_typesupport_c`` 或 ``rosidl_typesupport_cpp``。

根据可用的类型支持，可以从该句柄获取具体的类型支持句柄，例如 ``rosidl_typesupport_fastrtps_c``、``rosidl_typesupport_fastrtps_cpp``、``rosidl_typesupport_introspection_c`` 和 ``rosidl_typesupport_introspection_cpp``。容易让人困惑的是，这些具体句柄的类型同样是 ``const rosidl_message_type_support_t *``；但真正包含有用信息的是具体类型支持句柄。

可以参考 `示例函数 <https://github.com/christophebedard/rmw_email/blob/f5e622bab24edaad8e0da054c7dbc698c6fb809c/rmw_email_cpp/src/type_support.cpp#L29-L62>`_，它会根据基础类型支持句柄（``rosidl_typesupport_{c,cpp}``），提取具体的 C 或 C++ 动态消息类型支持句柄（``rosidl_typesupport_introspection_{c,cpp}``）。

由 ``rclcpp`` 创建的发布者会使用 C++ 类型支持；由 ``rclpy`` 创建的发布者会使用 C 类型支持，因为 Python 消息会被转换为 C 消息。``/rosout`` 发布者由使用 C 编写的 ``rcl`` 管理，因此使用 C 类型支持。

然后，通过具体类型支持句柄中的类型擦除指针 ``const void * data``，可以获取类型支持专用信息。例如，对于 C++ 动态类型支持，该指针会指向 ``const rosidl_typesupport_introspection_cpp::MessageMembers *``，其中包含消息各个字段的信息。

可以参考 `示例函数 <https://github.com/christophebedard/rmw_email/blob/f5e622bab24edaad8e0da054c7dbc698c6fb809c/rmw_email_cpp/src/conversion.cpp#L116-L153>`_，它展示了如何从具体类型支持句柄中提取与语言相关的类型支持信息。服务类型支持也类似，但 ``rosidl_service_type_support_t`` 会分别指向请求和响应消息类型的类型支持信息。

测试
----

``rmw`` 功能包包含一些测试，但它们主要针对工具函数（例如获取零初始化结构体）以及与具体实现无关的函数，例如话题、节点名称和命名空间验证。

对于新的 ``rmw`` 实现，``test_rmw_implementation`` `功能包包含针对接口的测试 <https://github.com/ros2/rmw_implementation/tree/{DISTRO}/test_rmw_implementation/test>`_。测试可执行程序首先被定义，然后由 CMake 函数为指定实现创建测试目标，并设置 ``RMW_IMPLEMENTATION`` 环境变量。

``rmw_implementation_cmake`` 的 ``call_for_each_rmw_implementation()`` 会调用该 CMake 函数，并遍历每个可用实现。可以参阅 `CMakeLists.txt 文件 <https://github.com/ros2/rmw_implementation/blob/{DISTRO}/test_rmw_implementation/CMakeLists.txt>`_。

许多其他功能包（包括仅用于测试的 ``test_rclcpp`` 功能包）也 `使用该机制 <https://github.com/ros2/system_tests/blob/{DISTRO}/test_rclcpp/CMakeLists.txt>`_，以便针对所有可用 RMW 实现运行测试。否则，测试只会使用默认实现。功能包也可以使用 ``get_available_rmw_implementations()`` 获取实际可用的实现列表。

一些测试包含特定于实现的代码，原因可能包括某些接口子集不受支持。此类测试可以使用 ``rmw`` 的 ``rmw_get_implementation_identifier()`` `函数 <https://docs.ros.org/en/{DISTRO}/p/rmw/generated/function_rmw_8h_1aeb8a815b9be5eb3f38ab28363ef63920.html>`_ 获取当前实现标识符。

中间件和 RMW 实现专用配置
-------------------------

``rmw`` 接口允许通过 ``rmw_publisher_options_t`` 和 ``rmw_subscription_options_t`` 中类型擦除的 ``rmw_specific_publisher_payload`` / ``rmw_specific_subscription_payload`` 字段，为发布者和订阅者提供任意的实现专用配置数据。用户可以通过 ``rclcpp`` 中的 ``RMWImplementationSpecificPublisherPayload`` 和 ``RMWImplementationSpecificSubscriptionPayload`` 设置这些字段。

这是一项高级且不可移植的功能，目前尚未被任何 Tier 1 实现使用。

为了获得更大的灵活性，一些实现会使用环境变量，例如 ``RMW_FASTRTPS_*``、``RMW_CONNEXT_*`` 等。底层中间件本身也可能通过环境变量进行配置，例如 ``FASTDDS_*``、``ZENOH_*``、``CYCLONEDDS_*``、``EMAIL_*`` 等。

例如，如果使用相应中间件，可以通过 ``CYCLONEDDS_URI``、``FASTRTPS_DEFAULT_PROFILES_FILE`` 和 ``ZENOH_SESSION_CONFIG_URI`` 环境变量，指定完整配置文件的路径。

脚注
----

.. [#fn_dds_rpc]
   目前已经有 DDS RPC 规范，但在 ROS 2 最初设计时，`该规范尚未定稿，DDS 厂商也没有实现 <https://design.ros2.org/articles/ros_on_dds.html#services-and-actions>`_。由于 ``rmw`` 接口正式保持 DDS 无关，因此服务由具体 ``rmw`` 实现负责。这也解释了为什么 :ref:`跨 DDS 厂商通信并不保证 <different-middleware-vendors-cross-vendor-communication>`，即使发布/订阅通常可以正常工作。

.. [#fn_gid_remote_matching]
   实际上并非总是如此，因此这一要求在一定程度上有所放宽。详情请参阅 `ros2/rmw_cyclonedds#377 <https://github.com/ros2/rmw_cyclonedds/issues/377>`_。

.. [#fn_ts_fastrtps]
   例如，``std_msgs/msg/Header`` 的 C++ 消息 Fast CDR 序列化/反序列化代码，位于构建目录下的 ``std_msgs/rosidl_typesupport_fastrtps_cpp/std_msgs/msg/detail/dds_fastrtps/header__type_support.cpp``。

.. [#fn_ts_dynamic]
   例如，``std_msgs/msg/Header`` 的 C++ 消息内省代码，位于构建目录下的 ``std_msgs/rosidl_typesupport_introspection_cpp/std_msgs/msg/detail/header__type_support.cpp``。