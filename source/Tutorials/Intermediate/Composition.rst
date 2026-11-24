.. redirect-from::

    Composition
    Tutorials/Composition

在单个进程中组合多个节点
========================

**目标：** 将多个 ROS 2 节点组合到同一个进程中运行。

**教程级别：** 中级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

有关节点组合的概念，请参阅 :doc:`节点组合概念 <../../Concepts/Intermediate/About-Composition>`。

有关如何编写可组合节点，请参阅 :doc:`编写可组合节点教程 <Writing-a-Composable-Node>`。

前置条件
--------

本教程使用 ``rclcpp_components``、``ros2component``、``composition`` 和 ``image_tools`` 等功能包中的可执行程序。如果已经按照平台对应的 :doc:`ROS 2 安装说明 <../../Installation>` 完成安装，这些功能包通常也已经安装。

运行示例
--------

发现可用组件
^^^^^^^^^^^^

要查看当前工作空间中已注册并可用的组件，在终端中运行：

.. code-block:: console

   $ ros2 component types
   (... 此处省略其他功能包的组件)
   composition
     composition::Talker
     composition::Listener
     composition::NodeLikeListener
     composition::Server
     composition::Client
   (... 此处省略其他功能包的组件)

使用 ROS 服务进行运行时组合：发布者和订阅者
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

首先打开一个终端，启动组件容器：

.. code-block:: console

   $ ros2 run rclcpp_components component_container

打开第二个终端，确认容器正在运行：

.. code-block:: console

   $ ros2 component list
   /ComponentManager

在第二个终端中加载 talker 组件。其源代码可参阅 `talker 组件源码`_ <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/composition/src/talker_component.cpp>。

.. code-block:: console

   $ ros2 component load /ComponentManager composition composition::Talker
   Loaded component 1 into '/ComponentManager' container node as '/talker'

命令会返回已加载组件的唯一 ID，以及该组件在容器中对应的节点名称。第一个终端应该显示组件已加载，并持续输出发布消息的日志。

接着加载 listener 组件。其源代码可参阅 `listener 组件源码`_ <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/composition/src/listener_component.cpp>。

.. code-block:: console

   $ ros2 component load /ComponentManager composition composition::Listener
   Loaded component 2 into '/ComponentManager' container node as '/listener'

查看容器状态：

.. code-block:: console

   $ ros2 component list
   /ComponentManager
      1  /talker
      2  /listener

此时，第一个终端应该持续输出接收到的消息。

使用 ROS 服务进行运行时组合：服务端和客户端
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

服务端和客户端的示例与发布者/订阅者非常相似。

在第一个终端中启动组件容器：

.. code-block:: console

   $ ros2 run rclcpp_components component_container

在第二个终端中加载服务端和客户端。可以分别查看 `server 组件源码`_ <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/composition/src/server_component.cpp> 和 `client 组件源码`_ <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/composition/src/client_component.cpp>。

.. code-block:: console

   $ ros2 component load /ComponentManager composition composition::Server
   $ ros2 component load /ComponentManager composition composition::Client

客户端会向服务端发送请求，服务端处理请求并返回响应，客户端最终输出收到的响应。

使用硬编码节点进行编译时组合
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

本示例展示另一种方式：复用相同的共享库，在编译时将多个组件组合到一个可执行程序中运行，而不使用 ROS 服务接口加载组件。

该可执行程序包含前面介绍的四个组件：talker、listener、server 和 client。它们在 ``main`` 函数中被直接创建。

运行以下命令。相关代码可参阅 `manual_composition.cpp 源码`_ <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/composition/src/manual_composition.cpp>。

.. code-block:: console

   $ ros2 run composition manual_composition

应该能看到两组通信持续输出消息：talker 与 listener，以及 server 与 client。

.. note::

   手动组合的组件不会显示在 ``ros2 component list`` 命令的输出中。

使用 dlopen 进行运行时组合
^^^^^^^^^^^^^^^^^^^^^^^^^^

本示例展示另一种运行时组合方式：创建一个通用容器进程，并显式传入需要加载的库，而不通过 ROS 服务接口加载组件。

该进程会打开每个库，并为库中每个 ``rclcpp::Node`` 派生类创建一个实例。相关代码可参阅 `dlopen_composition.cpp 源码`_ <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/composition/src/dlopen_composition.cpp>。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ ros2 run composition dlopen_composition <talker_component.so> <listener_component.so>

  .. group-tab:: macOS

    .. code-block:: console

       $ ros2 run composition dlopen_composition <talker_component.dylib> <listener_component.dylib>

  .. group-tab:: Windows

    首先使用 ``ros2 pkg prefix composition`` 获取 composition 功能包的安装路径，然后将路径替换到以下命令中：

    .. code-block:: console

       $ ros2 run composition dlopen_composition <path_to_composition_install>\bin\talker_component.dll <path_to_composition_install>\bin\listener_component.dll

此时，终端应该持续输出发送和接收的消息。

.. note::

   使用 dlopen 组合的组件不会显示在 ``ros2 component list`` 命令的输出中。

使用 launch 动作进行组合
^^^^^^^^^^^^^^^^^^^^^^^^

命令行工具适合调试和诊断组件配置，但很多时候更方便的方式是一次启动一组组件。

可以使用 `launch 文件`_ <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/composition/launch/composition_demo.launch.py> 自动完成该操作：

.. code-block:: console

   $ ros2 launch composition composition_demo.launch.py

高级主题
--------

了解组件的基本运行方式后，下面介绍一些更高级的主题。

组件容器类型
^^^^^^^^^^^^

不同组件容器具有不同的执行器配置，可以根据实际需求选择合适的容器类型。

* ``component_container``：使用单线程执行器，不提供额外参数配置。

  .. code-block:: console

     $ ros2 run rclcpp_components component_container

* ``component_container_mt``：使用多线程执行器，默认包含 4 个线程。

  * 可以通过 ``thread_num`` 参数指定多线程执行器的线程数量。

  .. code-block:: console

     $ ros2 run rclcpp_components component_container_mt --ros-args -p thread_num:=4

* ``component_container_isolated``：为每个组件使用独立的多线程执行器。

  * 使用 ``--use_multi_threaded_executor`` 参数，将每个组件使用的执行器指定为多线程执行器。

  .. code-block:: console

     $ ros2 run rclcpp_components component_container_isolated --use_multi_threaded_executor

卸载组件
^^^^^^^^

首先启动组件容器：

.. code-block:: console

   $ ros2 run rclcpp_components component_container

确认容器正在运行：

.. code-block:: console

   $ ros2 component list
   /ComponentManager

加载 talker 和 listener：

.. code-block:: console

   $ ros2 component load /ComponentManager composition composition::Talker
   Loaded component 1 into '/ComponentManager' container node as '/talker'
   $ ros2 component load /ComponentManager composition composition::Listener
   Loaded component 2 into '/ComponentManager' container node as '/listener'

加载组件时会输出该组件的唯一 ID。组件加载后，也可以通过列出组件来查看所有唯一 ID：

.. code-block:: console

   $ ros2 component list
   /ComponentManager
     1  /talker
     2  /listener

使用唯一 ID 可以从组件容器中卸载组件：

.. code-block:: console

   $ ros2 component unload /ComponentManager 1 2
   Unloaded component 1 from '/ComponentManager' container
   Unloaded component 2 from '/ComponentManager' container

回到第一个终端，确认 talker 和 listener 不再持续输出消息。

重映射容器名称和命名空间
^^^^^^^^^^^^^^^^^^^^^^^^

可以通过标准命令行参数重映射组件管理器的节点名称和命名空间：

.. code-block:: console

   $ ros2 run rclcpp_components component_container --ros-args -r __node:=MyContainer -r __ns:=/ns

在第二个终端中，可以使用更新后的容器名称加载组件：

.. code-block:: console

   $ ros2 component load /ns/MyContainer composition composition::Listener

.. note::

   容器的命名空间重映射不会影响已经加载的组件。

重映射组件名称和命名空间
^^^^^^^^^^^^^^^^^^^^^^^^

可以通过组件加载命令的参数调整组件节点名称和命名空间。

启动组件容器：

.. code-block:: console

   $ ros2 run rclcpp_components component_container

重映射节点名称：

.. code-block:: console

   $ ros2 component load /ComponentManager composition composition::Talker --node-name talker2

重映射命名空间：

.. code-block:: console

   $ ros2 component load /ComponentManager composition composition::Talker --node-namespace /ns

同时重映射节点名称和命名空间：

.. code-block:: console

   $ ros2 component load /ComponentManager composition composition::Talker --node-name talker3 --node-namespace /ns2

查看结果：

.. code-block:: console

   $ ros2 component list
   /ComponentManager
      1  /talker2
      2  /ns/talker
      3  /ns2/talker3

.. note::

   容器的命名空间重映射不会影响已经加载的组件。

向组件传递参数值
^^^^^^^^^^^^^^^^

``ros2 component load`` 命令支持在构造节点时向组件传递任意参数。

例如，可以将 ``image_tools::Cam2Image`` 组件的 ``burger_mode`` 参数设置为 true：

.. code-block:: console

   $ ros2 component load /ComponentManager image_tools image_tools::Cam2Image -p burger_mode:=true
   $ ros2 run rqt_image_view rqt_image_view

运行图像查看工具后，可以看到汉堡图像动画，而不是摄像头图像。

向组件传递额外参数
^^^^^^^^^^^^^^^^^^

``ros2 component load`` 命令还支持向组件管理器传递特定选项，以便在构造节点时使用。

下面的示例展示如何使用 ``use_intra_process_comms`` 和 ``forward_global_arguments`` 两个额外参数：

.. code-block:: console

   $ ros2 component load /ComponentManager composition composition::Talker -e use_intra_process_comms:=true -e forward_global_arguments:=false

目前支持以下额外参数：

.. list-table:: 组件管理器支持的额外参数
   :widths: 20 15 15 50
   :header-rows: 1

   * - 参数
     - 类型
     - 默认值
     - 说明
   * - ``forward_global_arguments``
     - 布尔值
     - True
     - 加载组件时，是否将全局参数应用到组件节点。
   * - ``use_intra_process_comms``
     - 布尔值
     - False
     - 是否为组件节点启用进程内通信。

将可组合节点作为共享库
----------------------

如果希望将可组合节点作为共享库从一个功能包中导出，并在另一个功能包中进行链接时组合，需要在 CMake 文件中添加代码，以便下游功能包导入实际的 target。

随后安装生成的文件，并导出该文件。

实际示例可参阅 `ROS Discourse：共享库的 Ament 最佳实践`_ <https://discourse.openrobotics.org/t/ament-best-practice-for-sharing-libraries/3602>。

组合非 Node 派生组件
-------------------

在 ROS 2 中，组件可以更高效地使用系统资源，还提供了一项强大功能：创建不与特定节点绑定的可复用功能。

组件的一个优势是，可以将非 Node 派生的功能实现为独立可执行程序或共享库，并在需要时加载到 ROS 系统中。

创建不继承 Node 的组件时，需要遵循以下要求：

1. 实现一个构造函数，并将 ``const rclcpp::NodeOptions&`` 作为参数。
2. 实现 ``get_node_base_interface()`` 方法，该方法应返回 ``NodeBaseInterface::SharedPtr``。可以在构造函数中创建一个节点，并通过该节点的 ``get_node_base_interface()`` 方法返回对应接口。

可以参考 `node_like_listener_component 示例源码`_ <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/composition/src/node_like_listener_component.cpp>。该组件并不直接继承 Node，但能够订阅 ROS 话题。

更多信息请参阅 `相关讨论`_ <https://github.com/ros2/rclcpp/issues/2110#issuecomment-1454228192>。
