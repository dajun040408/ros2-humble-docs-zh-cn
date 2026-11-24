.. redirect-from::

    Tutorials/Launch-Files/Using-Event-Handlers
    Tutorials/Launch/Using-Event-Handlers

使用事件处理器
==============

**目标：** 学习 ROS 2 启动文件中的事件处理器。

**教程级别：** 中级

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

ROS 2 Launch 是一个用于执行和管理用户定义进程的系统。它负责监控所启动进程的状态，并报告和响应进程状态的变化。这些变化称为事件，可以通过向启动系统注册事件处理器来处理。

事件处理器可以针对特定事件注册，用于监控进程状态。此外，还可以通过事件处理器定义复杂规则，以动态修改启动文件。

本教程展示如何在 ROS 2 启动文件中使用事件处理器。

前置条件
--------

本教程使用 :doc:`turtlesim <../../Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim>` 软件包，并假设你已经创建了一个构建类型为 ``ament_python``、名称为 ``launch_tutorial`` 的新功能包，参见 :doc:`创建 ROS 2 功能包 <../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>`。

本教程基于 :doc:`在启动文件中使用替换 <./Using-Substitutions>` 教程中的代码继续展开。

使用事件处理器
--------------

1. 事件处理器示例启动文件
^^^^^^^^^^^^^^^^^^^^^^^^^

在 ``launch_tutorial`` 功能包的 ``launch`` 文件夹中创建名为 ``example_event_handlers.launch.py`` 的新文件。

.. literalinclude:: launch/example_event_handlers_launch.py
    :language: python

启动描述中定义了多个 ``RegisterEventHandler`` 操作，分别处理 ``OnProcessStart``、``OnProcessIO``、``OnExecutionComplete``、``OnProcessExit`` 和 ``OnShutdown`` 事件。

``OnProcessStart`` 事件处理器用于注册一个回调函数，在 turtlesim 节点启动时执行。它会向控制台输出日志，并在 turtlesim 节点启动时执行 ``spawn_turtle`` 操作。

.. literalinclude:: launch/example_event_handlers_launch.py
    :language: python
    :lines: 98-106

``OnProcessIO`` 事件处理器用于注册一个回调函数，在 ``spawn_turtle`` 操作向标准输出写入内容时执行，并记录生成请求的结果。

.. literalinclude:: launch/example_event_handlers_launch.py
    :language: python
    :lines: 107-115

``OnExecutionComplete`` 事件处理器用于注册一个回调函数，在 ``spawn_turtle`` 操作完成时执行。它会输出日志，并在生成操作完成后执行 ``change_background_r`` 和 ``change_background_r_conditioned`` 操作。

.. literalinclude:: launch/example_event_handlers_launch.py
    :language: python
    :lines: 116-128

``OnProcessExit`` 事件处理器用于注册一个回调函数，在 turtlesim 节点退出时执行。它会输出日志，并执行 ``EmitEvent`` 操作发出 ``Shutdown`` 事件。这意味着关闭 turtlesim 窗口时，整个启动进程也会关闭。

.. literalinclude:: launch/example_event_handlers_launch.py
    :language: python
    :lines: 129-139

最后，``OnShutdown`` 事件处理器用于注册一个回调函数，在启动文件被要求关闭时执行。它会记录启动文件关闭的原因，例如 turtlesim 窗口关闭，或用户按下 :kbd:``ctrl-c`` 发出的信号。

.. literalinclude:: launch/example_event_handlers_launch.py
    :language: python
    :lines: 140-146

构建功能包
----------

进入工作空间根目录并构建功能包：

.. code-block:: console

  $ colcon build

构建完成后，记得 source 工作空间。

启动示例
--------

现在可以使用 ``ros2 launch`` 命令运行 ``example_event_handlers.launch.py``：

.. code-block:: console

    $ ros2 launch launch_tutorial example_event_handlers.launch.py turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200

该启动文件将执行以下操作：

#. 启动一个蓝色背景的 turtlesim 节点。
#. 生成第二只海龟。
#. 将背景颜色改为紫色。
#. 如果 ``background_r`` 参数为 ``200`` 且 ``use_provided_red`` 参数为 ``True``，则在两秒后将背景颜色改为粉色。
#. 关闭 turtlesim 窗口时，关闭启动文件。

此外，在以下事件发生时，控制台会输出日志：

#. turtlesim 节点启动。
#. 执行生成海龟操作。
#. 执行 ``change_background_r`` 操作。
#. 执行 ``change_background_r_conditioned`` 操作。
#. turtlesim 节点退出。
#. 启动进程收到关闭请求。

文档
----

`Launch 文档 <https://github.com/ros2/launch/blob/{REPOS_FILE_BRANCH}/launch/doc/source/architecture.rst>`_ 提供了可用事件处理器的详细信息。

总结
----

本教程介绍了如何在启动文件中使用事件处理器，包括其语法和使用示例，以及如何定义复杂规则来动态修改启动文件。
