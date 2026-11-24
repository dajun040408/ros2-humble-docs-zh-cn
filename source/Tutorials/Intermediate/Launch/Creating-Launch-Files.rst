.. redirect-from::

    Tutorials/Launch-Files/Creating-Launch-Files
    Tutorials/Launch/Creating-Launch-Files

创建启动文件
============

**目标：** 创建一个启动文件，以运行复杂的 ROS 2 系统。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

前置条件
--------

本教程使用 :doc:`rqt_graph 和 turtlesim <../../Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim>` 功能包。

你还需要准备一个文本编辑器。每次打开新终端时，都不要忘记 :doc:`source ROS 2 环境 <../../Beginner-CLI-Tools/Configuring-ROS2-Environment>`。

背景
----

ROS 2 启动系统用于帮助用户描述系统配置，并按照配置启动系统。

系统配置包括：需要运行哪些程序、在哪些位置运行、向程序传递哪些参数，以及如何通过 ROS 特有的约定，让系统中的组件能够在不同配置下复用。

启动系统还负责监控已启动进程的状态，并报告或响应进程状态变化。

使用 XML、YAML 或 Python 编写的启动文件可以启动和停止不同节点，也可以触发并响应各种事件。有关不同格式的说明，请参阅 :doc:`不同格式的启动文件 <../../../How-To-Guides/Launch-file-different-formats>`。

任务
----

1. 准备目录
^^^^^^^^^^^

创建一个新目录，用于存放启动文件：

.. code-block:: console

   $ mkdir launch

2. 编写启动文件
^^^^^^^^^^^^^^^

下面使用 ``turtlesim`` 功能包及其可执行程序创建一个 ROS 2 启动文件。启动文件可以使用 XML、YAML 或 Python 格式。

.. tabs::

  .. group-tab:: XML

    将完整代码复制到 ``launch/turtlesim_mimic_launch.xml``：

    .. literalinclude:: launch/turtlesim_mimic_launch.xml
       :language: xml

  .. group-tab:: YAML

    将完整代码复制到 ``launch/turtlesim_mimic_launch.yaml``：

    .. literalinclude:: launch/turtlesim_mimic_launch.yaml
       :language: yaml

  .. group-tab:: Python

    将完整代码复制到 ``launch/turtlesim_mimic_launch.py``：

    .. literalinclude:: launch/turtlesim_mimic_launch.py
       :language: python

2.1 检查启动文件
~~~~~~~~~~~~~~~~

以上启动文件都会启动三个节点，且这三个节点都来自 ``turtlesim`` 功能包。该系统的目标是启动两个 turtlesim 窗口，并让其中一只乌龟模仿另一只乌龟的运动。

两个 turtlesim 节点最主要的区别是它们使用了不同的命名空间。唯一的命名空间可以避免节点名称和话题名称冲突。两个乌龟都通过相同的话题接收控制命令，并通过相同的话题发布位姿；由于命名空间不同，因此可以区分发往不同乌龟的消息。

这两个 turtlesim 节点还展示了向节点传递参数的不同方式：

* 第一个节点使用 ``args`` 直接向可执行程序传递参数。如果传递 ROS 专用参数，则需要使用 ``--ros-args`` 标志。
* 第二个节点使用 ``ros_args``（Python 中为 ``ros_arguments``），专门用于传递 ROS 参数。

如果需要混合传递 ROS 参数和非 ROS 参数，例如 ``my_custom_arg --ros-args --log-level info``，可以使用 ``args``。如果只传递重映射、参数或日志级别等 ROS 参数，使用 ``ros_args`` 会更加简洁。

最后一个节点同样来自 ``turtlesim`` 功能包，但使用的是另一个可执行程序 ``mimic``。该节点还配置了重映射规则：

* 将 ``mimic`` 的 ``/input/pose`` 话题重映射到 ``/turtlesim1/turtle1/pose``。
* 将 ``mimic`` 的 ``/output/cmd_vel`` 话题重映射到 ``/turtlesim2/turtle1/cmd_vel``。

这意味着 ``mimic`` 会订阅 ``/turtlesim1/sim`` 的位姿话题，并将其重新发布到 ``/turtlesim2/sim`` 的速度命令话题。换句话说，``turtlesim2`` 会模仿 ``turtlesim1`` 的运动。

.. tabs::

  .. group-tab:: XML

    前两个动作以不同的参数传递方式启动两个 turtlesim 窗口：

    .. literalinclude:: launch/turtlesim_mimic_launch.xml
       :language: xml
       :lines: 3-4

    最后一个动作启动 mimic 节点并设置重映射规则：

    .. literalinclude:: launch/turtlesim_mimic_launch.xml
       :language: xml
       :lines: 5-8

  .. group-tab:: YAML

    前两个动作以不同的参数传递方式启动两个 turtlesim 窗口：

    .. literalinclude:: launch/turtlesim_mimic_launch.yaml
       :language: yaml
       :lines: 4-16

    最后一个动作启动 mimic 节点并设置重映射规则：

    .. literalinclude:: launch/turtlesim_mimic_launch.yaml
       :language: yaml
       :lines: 18-26

  .. group-tab:: Python

    首先导入所需的 Python launch 模块：

    .. literalinclude:: launch/turtlesim_mimic_launch.py
       :language: python
       :lines: 1-2

    接下来定义启动描述：

    .. literalinclude:: launch/turtlesim_mimic_launch.py
       :language: python
       :lines: 5-6,30

    前两个动作以不同的参数传递方式启动两个 turtlesim 窗口：

    .. literalinclude:: launch/turtlesim_mimic_launch.py
       :language: python
       :lines: 7-20

    最后一个动作启动 mimic 节点并设置重映射规则：

    .. literalinclude:: launch/turtlesim_mimic_launch.py
       :language: python
       :lines: 21-29

3. 使用 ros2 launch
^^^^^^^^^^^^^^^^^^^

要运行上面创建的启动文件，进入之前创建的目录并运行相应命令：

.. tabs::

  .. group-tab:: XML

    .. code-block:: console

       $ cd launch
       $ ros2 launch turtlesim_mimic_launch.xml

  .. group-tab:: YAML

    .. code-block:: console

       $ cd launch
       $ ros2 launch turtlesim_mimic_launch.yaml

  .. group-tab:: Python

    .. code-block:: console

       $ cd launch
       $ ros2 launch turtlesim_mimic_launch.py

.. note::

   可以直接启动一个启动文件，也可以启动由功能包提供的启动文件。使用功能包时，命令格式为：

   .. code-block:: console

      $ ros2 launch <package_name> <launch_file_name>

   有关创建功能包的内容，请参阅 :doc:`创建 ROS 2 功能包 <../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>`。

.. note::

   对于包含启动文件的功能包，建议在 ``package.xml`` 中添加对 ``ros2launch`` 的 ``exec_depend`` 依赖：

   .. code-block:: xml

      <exec_depend>ros2launch</exec_depend>

   这样可以确保构建功能包后 ``ros2 launch`` 命令可用，也能确保所有 :doc:`启动文件格式 <../../../How-To-Guides/Launch-file-different-formats>` 都能被识别。

此时会打开两个 turtlesim 窗口。终端会输出类似以下 ``[INFO]`` 消息，说明启动文件启动了哪些节点：

.. code-block:: console

   [INFO] [launch]: Default logging verbosity is set to INFO
   [INFO] [turtlesim_node-1]: process started with pid [11714]
   [INFO] [turtlesim_node-2]: process started with pid [11715]
   [INFO] [mimic-3]: process started with pid [11716]

要观察系统运行效果，打开一个新终端，在 ``/turtlesim1/turtle1/cmd_vel`` 话题上运行 ``ros2 topic pub`` 命令，让第一只乌龟开始移动：

.. code-block:: console

   $ ros2 topic pub -r 1 /turtlesim1/turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: -1.8}}"

你会看到两只乌龟沿着相同路径移动。

.. image:: images/mimic.png

4. 使用 rqt_graph 检查系统
^^^^^^^^^^^^^^^^^^^^^^^^^

在系统仍然运行时，打开一个新终端并运行 ``rqt_graph``，可以更直观地查看启动文件中各节点之间的关系：

.. code-block:: console

   $ ros2 run rqt_graph rqt_graph

.. image:: images/mimic_graph.png

图中左侧的隐藏节点是刚才运行的 ``ros2 topic pub`` 命令，它向 ``/turtlesim1/turtle1/cmd_vel`` 话题发布数据，该话题由 ``/turtlesim1/sim`` 节点订阅。

图中其余部分展示了前面介绍的关系：``mimic`` 订阅 ``/turtlesim1/sim`` 的位姿话题，并向 ``/turtlesim2/sim`` 的速度命令话题发布数据。

总结
----

启动文件可以简化包含多个节点和特定配置的复杂系统。你可以使用 XML、YAML 或 Python 创建启动文件，并通过 ``ros2 launch`` 命令运行它们。
