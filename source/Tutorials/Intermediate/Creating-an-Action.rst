.. redirect-from::

    Tutorials/Actions/Creating-an-Action

.. _ActionCreate:

创建 Action
===========

**目标：** 在 ROS 2 功能包中定义一个 Action。

**教程级别：** 中级

**预计时间：** 5 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

你已经在 :doc:`理解 ROS 2 Actions <../Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions>` 教程中学习过 Action。与其他通信类型及其接口（话题/msg 和服务/srv）类似，也可以在自己的功能包中自定义 Action。本教程将介绍如何定义并构建 Action，供下一个教程中编写的 Action 服务端和客户端使用。

前置条件
--------

需要安装 :doc:`ROS 2 <../../Installation>` 和 ``colcon`。

创建一个 :doc:`工作空间 <../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace>`，并创建名为 ``action_tutorials_interfaces`` 的功能包。首先要 :doc:`source ROS 2 安装环境 <../Beginner-CLI-Tools/Configuring-ROS2-Environment>`。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ mkdir -p ros2_ws/src
      $ cd ros2_ws/src
      $ ros2 pkg create --build-type ament_cmake action_tutorials_interfaces

  .. group-tab:: macOS

    .. code-block:: console

      $ mkdir -p ros2_ws/src
      $ cd ros2_ws/src
      $ ros2 pkg create --build-type ament_cmake action_tutorials_interfaces

  .. group-tab:: Windows

    .. code-block:: console

      $ md ros2_ws\src
      $ cd ros2_ws\src
      $ ros2 pkg create --build-type ament_cmake action_tutorials_interfaces

``action_tutorials_interfaces`` 是新功能包的名称。注意，该功能包只能是 CMake 类型，但这并不限制 Action 可以在哪种类型的功能包中使用。创建新 ROS 2 功能包时，``--build-type ament_cmake`` 标志在很大程度上是可选的，此处添加它是为了完整说明。你可以在 CMake 功能包中定义自定义接口，然后在 C++ 或 Python 节点中使用它。

.. note::

  良好的实践是将 ``.msg``、``.srv`` 和 ``.action`` 文件放在与使用它们的节点不同的功能包中。这样可以更方便地在多个功能包之间复用接口定义。

任务
----

1. 定义 Action
^^^^^^^^^^^^^^

Action 定义在 ``.action`` 文件中，其结构如下：

.. code-block:: text

    # 请求
    ---
    # 结果
    ---
    # 反馈

一个 Action 定义由三个消息定义组成，它们之间使用 ``---`` 分隔。

* **请求（Request）：** Action 客户端向 Action 服务端发送请求，以启动一个新目标。
* **结果（Result）：** 目标完成时，Action 服务端向客户端发送结果消息。
* **反馈（Feedback）：** Action 服务端定期向客户端发送反馈消息，报告目标执行进度。

Action 的一次执行通常称为一个目标（Goal）。

假设我们希望定义一个名为 ``Fibonacci`` 的新 Action，用于计算`斐波那契数列 <https://en.wikipedia.org/wiki/Fibonacci_number>`_。

在 ``action_tutorials_interfaces`` 功能包中创建 ``action`` 目录：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ cd action_tutorials_interfaces
      $ mkdir action

  .. group-tab:: macOS

    .. code-block:: console

      $ cd action_tutorials_interfaces
      $ mkdir action

  .. group-tab:: Windows

    .. code-block:: console

      $ cd action_tutorials_interfaces
      $ md action

在 ``action`` 目录中创建 ``Fibonacci.action`` 文件，内容如下：

.. code-block:: text

  int32 order
  ---
  int32[] sequence
  ---
  int32[] partial_sequence

目标请求是需要计算的斐波那契数列阶数 ``order``；结果是最终数列 ``sequence``；反馈是目前已经计算出的部分数列 ``partial_sequence``。

2. 构建 Action
^^^^^^^^^^^^^^

在代码中使用新的 Fibonacci Action 类型之前，必须将其定义传递给 rosidl 代码生成流程。

在 ``action_tutorials_interfaces`` 的 ``CMakeLists.txt`` 中、``ament_package()`` 之前添加：

.. code-block:: cmake

    find_package(rosidl_default_generators REQUIRED)

    rosidl_generate_interfaces(${PROJECT_NAME}
      "action/Fibonacci.action"
    )

还需要在 ``package.xml`` 中添加必要依赖：

.. code-block:: xml

    <buildtool_depend>rosidl_default_generators</buildtool_depend>
    <depend>action_msgs</depend>
    <member_of_group>rosidl_interface_packages</member_of_group>

这里需要依赖 ``action_msgs``，因为 Action 定义包含额外的元数据，例如目标 ID。

现在可以构建包含 ``Fibonacci`` Action 定义的功能包：

.. code-block:: console

    $ cd ~/ros2_ws
    $ colcon build

按照约定，Action 类型名称由功能包名称和 ``action`` 组成。因此，新 Action 的完整名称为 ``action_tutorials_interfaces/action/Fibonacci``。

可以使用命令行工具检查 Action 是否构建成功：

.. code-block:: console

   $ . install/setup.bash
   $ ros2 interface show action_tutorials_interfaces/action/Fibonacci

在屏幕上应能看到 Fibonacci Action 的定义。

总结
----

本教程介绍了 Action 定义的结构，以及如何通过 ``CMakeLists.txt`` 和 ``package.xml`` 正确构建新的 Action 接口，并验证构建成功。

后续步骤
--------

接下来，可以使用新定义的 Action 接口创建 Action 服务端和客户端，参见 :doc:`Python 教程 <Writing-an-Action-Server-Client/Py>` 或 :doc:`C++ 教程 <Writing-an-Action-Server-Client/Cpp>`。

相关内容
--------

有关 ROS Actions 的更多详细信息，请参阅`设计文章 <http://design.ros2.org/articles/actions.html>`_。
