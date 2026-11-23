.. redirect-from::

   Concepts/About-Composition

组件组合（Composition）
=======================

.. contents:: 目录
   :local:

ROS 1：节点与 Nodelet
----------------------

在 ROS 1 中，你可以将代码编写为 `ROS 节点 <https://wiki.ros.org/Nodes>`__ 或 `ROS nodelet <https://wiki.ros.org/nodelet>`__。

ROS 1 节点会被编译为可执行文件。ROS 1 nodelet 则会被编译为共享库，然后在运行时由一个容器进程加载。

ROS 2：统一 API
----------------

在 ROS 2 中，推荐的代码编写方式与 nodelet 类似，我们将其称为 Component（组件）。这种方式便于向现有代码添加生命周期等通用概念（参见 `节点生命周期设计 <https://design.ros2.org/articles/node_lifecycle.html>`__）。

ROS 1 中使用不同 API 是其最大的缺点之一，而 ROS 2 避免了这一问题，因为两种运行方式都使用相同的 API。

.. note::

   仍然可以采用类似节点的方式“自行编写 main 函数”，但对于常见使用场景，不推荐这样做。

将进程布局作为部署时的决策，可以让用户在以下两种方式之间进行选择：

* 将多个节点运行在不同进程中，从而获得进程隔离和故障隔离的好处，并且更容易单独调试每个节点。
* 将多个节点运行在同一个进程中，从而降低开销，并且可以选择使用效率更高的通信方式（参见 :doc:`进程内通信 <../../Tutorials/Demos/Intra-Process-Communication>`）。

此外，还可以使用 ``ros2 launch`` 通过专门的启动动作自动完成这些操作。

.. _ComponentContainer:

组件容器
----------

组件容器（Component Container）是一个宿主进程，允许你在同一个进程空间中于运行时加载和管理多个组件。

目前提供以下通用组件容器类型：

* `component_container <https://github.com/ros2/rclcpp/blob/{REPOS_FILE_BRANCH}/rclcpp_components/src/component_container.cpp>`__

  * 最通用的组件容器，使用单个 ``SingleThreadedExecutor`` 执行所有组件。

* `component_container_mt <https://github.com/ros2/rclcpp/blob/{REPOS_FILE_BRANCH}/rclcpp_components/src/component_container_mt.cpp>`__

  * 使用单个 ``MultiThreadedExecutor`` 执行组件的容器。

* `component_container_isolated <https://github.com/ros2/rclcpp/blob/{REPOS_FILE_BRANCH}/rclcpp_components/src/component_container_isolated.cpp>`__

  * 为每个组件使用独立执行器的容器。执行器可以是 ``SingleThreadedExecutor``（默认）或 ``MultiThreadedExecutor``。

有关执行器类型的更多信息，请参阅 :ref:`执行器类型 <TypesOfExecutors>`。有关每种组件容器的选项，请参阅组件组合教程中的 :ref:`ComponentContainerTypes`。

编写组件
----------

组件只会被构建为共享库，因此它没有 ``main`` 函数（参见 `Talker 源代码 <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/composition/src/talker_component.cpp>`__）。

组件通常是 ``rclcpp::Node`` 的子类。由于组件本身不控制线程，因此不应在构造函数中执行耗时较长或阻塞的任务。相反，可以使用定时器定期触发处理逻辑。此外，组件还可以创建发布者、订阅者、服务端和客户端。

要让一个类成为组件，一个重要步骤是：该类需要使用 ``rclcpp_components`` 软件包中的宏注册自身（参见源代码的最后一行）。这样，当组件库被加载到正在运行的进程中时，系统就可以发现该组件；这一注册机制相当于组件的入口点。

此外，组件创建后，还必须将其注册到索引中，以便相关工具能够发现它。

.. code-block:: cmake

   add_library(talker_component SHARED src/talker_component.cpp)
   rclcpp_components_register_nodes(talker_component "composition::Talker")
   # To register multiple components in the same shared library, use multiple calls
   # rclcpp_components_register_nodes(talker_component "composition::Talker2")

示例请参阅 :doc:`可组合节点教程 <../../Tutorials/Intermediate/Writing-a-Composable-Node>`。

.. note::

   为了让 component_container 能够找到所需组件，必须从已经 source 对应工作空间的 Shell 中执行或启动该容器。

CMake 注册宏
--------------

ROS 2 提供两个用于注册组件的 CMake 宏，它们的用途不同。

``rclcpp_components_register_node``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
该宏注册一个组件，并生成一个独立可执行文件。如果你既希望组件能够被组合加载，也希望节点可以作为独立进程运行，请使用此宏。

.. code-block:: cmake

   add_library(talker_component SHARED src/talker_component.cpp)
   rclcpp_components_register_node(talker_component
     PLUGIN "composition::Talker"
     EXECUTABLE talker)

``rclcpp_components_register_nodes``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
该宏注册一个或多个组件，供运行时进行组件组合，**但不会创建独立可执行文件**。如果你希望构建纯组件库，并在运行时将其加载到组件容器中，请使用此宏。

.. code-block:: cmake

   add_library(talker_component SHARED src/talker_component.cpp)
   rclcpp_components_register_nodes(talker_component "composition::Talker")

使用组件
----------

`composition <https://github.com/ros2/demos/tree/{REPOS_FILE_BRANCH}/composition>`__ 软件包包含几种不同的组件使用方式。最常见的三种方式如下：

#. 启动一个 `通用容器进程 <https://github.com/ros2/rclcpp/blob/{REPOS_FILE_BRANCH}/rclcpp_components/src/component_container.cpp>`__ ，然后调用容器提供的 ROS 服务 `load_node <https://github.com/ros2/rcl_interfaces/blob/{REPOS_FILE_BRANCH}/composition_interfaces/srv/LoadNode.srv>`__。该 ROS 服务会根据传入的功能包名称和库名称加载指定组件，并在正在运行的进程中启动它。除了通过程序调用 ROS 服务外，也可以使用 `命令行工具 <https://github.com/ros2/ros2cli/tree/{REPOS_FILE_BRANCH}/ros2component>`__ ，通过命令行参数调用该服务。
#. 创建一个 `自定义可执行文件 <https://github.com/ros2/demos/blob/{REPOS_FILE_BRANCH}/composition/src/manual_composition.cpp>`__ ，其中包含多个在编译时就已确定的节点。与第一种方式不同，这种方式要求每个组件都提供头文件（第一种方式并非严格要求头文件）。
#. 创建启动文件，并使用 ``ros2 launch`` 启动一个容器进程，同时加载多个组件。

实际应用
----------

请尝试运行 :doc:`组件组合演示 <../../Tutorials/Intermediate/Composition>`。
