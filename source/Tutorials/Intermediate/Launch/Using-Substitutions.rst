.. redirect-from::

    Tutorials/Launch-Files/Using-Substitutions
    Tutorials/Launch/Using-Substitutions

在启动文件中使用替换
====================

**目标：** 学习 ROS 2 启动文件中的替换机制。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

启动文件用于启动节点、服务和进程。这些动作可以接收参数，以改变其行为。替换机制可以在启动描述执行时动态计算参数值，从而使启动文件更灵活、更容易复用。

替换项是在启动描述执行期间才求值的变量，可用于获取启动配置、环境变量，或执行任意 Python 表达式。

前置条件
--------

本教程使用 ``turtlesim``，并假设你熟悉 :doc:`创建功能包 <../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>`。每次打开新终端时都应 source ROS 2 环境。

创建并配置功能包
----------------

创建名为 ``launch_tutorial`` 的功能包：

.. code-block:: console

   $ ros2 pkg create --build-type ament_python --license Apache-2.0 launch_tutorial

也可以创建 C++ 功能包，将构建类型设为 ``ament_cmake``。

在功能包中创建 ``launch`` 目录，并按照 :doc:`创建启动文件教程 <./Creating-Launch-Files>` 将启动文件加入安装规则。

父启动文件
----------

创建一个父启动文件，用于调用另一个启动文件并向其传递参数。可以使用 XML、YAML 或 Python 格式。

父启动文件通过 ``IncludeLaunchDescription``（Python）或对应格式的 include 动作，引用子启动文件，并传递 ``turtlesim_ns``、``use_provided_red`` 和 ``new_background_r`` 等参数。

替换示例启动文件
----------------

在同一目录创建子启动文件，定义启动配置：

* ``turtlesim_ns``：turtlesim 节点的命名空间。
* ``use_provided_red``：是否使用传入的红色背景参数。
* ``new_background_r``：新的背景红色分量。

XML 和 YAML 格式可以使用 ``$(var <name>)`` 获取启动参数值，使用 ``$(eval <python-expression>)`` 计算条件表达式。

Python 格式可以使用 ``LaunchConfiguration`` 获取参数值，使用 ``DeclareLaunchArgument`` 声明参数，并通过 ``PythonExpression`` 和 ``IfCondition`` 实现条件执行。

构建功能包
----------

在工作空间根目录构建：

.. code-block:: console

   $ colcon build

构建完成后 source 工作空间。

运行示例
--------

使用 ``ros2 launch`` 启动父启动文件，例如：

.. code-block:: console

   $ ros2 launch launch_tutorial example_main.launch.py

启动后会创建 turtlesim 节点、生成第二只海龟，并根据启动参数修改背景颜色。

查看启动参数
------------

可以使用 ``--show-args`` 查看启动文件接受的参数及默认值：

.. code-block:: console

   $ ros2 launch launch_tutorial example_substitutions.launch.py --show-args

参数可以通过 ``<name>:=<value>`` 格式传入，例如：

.. code-block:: console

   $ ros2 launch launch_tutorial example_substitutions.launch.py turtlesim_ns:=turtlesim3 use_provided_red:=True new_background_r:=200

总结
----

本教程介绍了启动配置、环境变量和 Python 表达式等替换机制，以及如何利用这些机制构建可复用的启动文件。下一步可以学习 :doc:`在启动文件中使用事件处理器 <./Using-Event-Handlers>`。
