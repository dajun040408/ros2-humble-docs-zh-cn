.. redirect-from::

    Tutorials/Launch-Files/Using-ROS2-Launch-for-Large-Projects
    Tutorials/Launch/Using-ROS2-Launch-for-Large-Projects

管理大型项目
============

**目标：** 学习使用 ROS 2 启动文件管理大型项目的最佳实践。

**教程级别：** 中级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 3
   :local:

背景
----

本教程介绍编写大型项目启动文件的一些技巧，重点是如何组织启动文件，使其能够在不同场景下尽可能复用。

此外，还会介绍 ROS 2 启动工具的多种用法，包括参数、YAML 文件、重映射、命名空间、默认参数和 RViz 配置等。

前置条件
--------

本教程使用 :doc:`turtlesim <../../Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim>` 和 :doc:`turtle_tf2_py <../Tf2/Introduction-To-Tf2>` 功能包。

还假设你已经按照 :doc:`创建 ROS 2 功能包 <../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>` 教程创建了一个名为 ``launch_tutorial``、构建类型为 ``ament_python`` 的新功能包。

简介
----

机器人上的大型应用通常由多个相互连接的节点组成，每个节点还可能包含多个参数。

在 turtlesim 中模拟多只乌龟就是一个很好的例子。该仿真由多个乌龟节点、世界配置，以及 TF 广播器和监听器节点组成。这些节点有大量 ROS 参数，会影响节点的行为和外观。

ROS 2 启动文件允许我们在一个地方启动所有节点并设置对应参数。

本教程最终会在 ``launch_tutorial`` 功能包中创建 ``launch_turtlesim_launch`` 启动文件。该文件将启动两个 turtlesim 仿真世界、TF 广播器和监听器、mimic 节点、固定坐标系广播器以及 RViz。

本教程会逐步介绍该启动文件及其使用的相关功能。

.. attention::

   启动文件可以使用 XML、YAML 或 Python 格式编写。本教程会通过标签页展示这三种格式。你可以选择自己喜欢的格式，它们在功能上是等价的。文中出现 ``launch_turtlesim_launch`` 等文件名时，请根据所选格式使用正确扩展名：Python 使用 ``.py``，XML 使用 ``.xml``，YAML 使用 ``.yaml``。

编写启动文件
------------

1. 顶层组织
^^^^^^^^^^^

编写启动文件时，一个重要目标是尽可能提高复用性。可以将相关节点和配置归类到不同的启动文件中，再编写一个专门用于特定配置的顶层启动文件。

这样，在相同机器人之间切换时通常无需修改启动文件。即使从真实机器人切换到仿真环境，也只需做少量调整。

下面先创建一个顶层启动文件，用于调用其他启动文件。在 ``launch_tutorial`` 功能包的 ``launch`` 目录中创建 ``launch_turtlesim_launch`` 文件。

.. attention::

   较早版本的启动系统可能不支持在 ``include`` 语句中使用 ``let``，而需要使用 ``arg``。两者语法相同，``name`` 和 ``value`` 属性保持不变，例如：``<arg name="target_frame" value="carrot1" />``。

.. tabs::

  .. group-tab:: XML

    将完整代码复制到 ``launch/launch_turtlesim_launch.xml``：

    .. literalinclude:: launch/launch_turtlesim_launch.xml
       :language: xml

  .. group-tab:: YAML

    将完整代码复制到 ``launch/launch_turtlesim_launch.yaml``：

    .. literalinclude:: launch/launch_turtlesim_launch.yaml
       :language: yaml

  .. group-tab:: Python

    将完整代码复制到 ``launch/launch_turtlesim_launch.py``：

    .. literalinclude:: launch/launch_turtlesim_launch.py
       :language: python

该启动文件包含多个其他启动文件。每个被包含的启动文件都负责系统的一个子部分，其中可以包含节点、参数以及嵌套的 include。

具体来说，顶层启动文件会启动两个 turtlesim 仿真世界、TF 广播器、TF 监听器、mimic 节点、固定坐标系广播器和 RViz 节点。

.. note::

   设计建议：顶层启动文件应尽量简短，主要由对应应用子系统的 include 组成，并保留经常需要修改的参数。

按这种方式编写启动文件，可以轻松替换系统中的某个子部分。不过，出于性能或使用方面的原因，有时仍需要单独启动某些节点或启动文件。

.. note::

   设计建议：规划顶层启动文件数量时，需要充分考虑复用性和维护成本之间的权衡。

2. 参数
^^^^^^^

2.1 在启动文件中设置参数
~~~~~~~~~~~~~~~~~~~~~~~~~

首先编写一个启动文件，用于启动第一个 turtlesim 仿真。创建 ``turtlesim_world_1_launch`` 文件。

.. tabs::

  .. group-tab:: XML

    将完整代码复制到 ``launch/turtlesim_world_1_launch.xml``：

    .. literalinclude:: launch/turtlesim_world_1_launch.xml
       :language: xml

  .. group-tab:: YAML

    将完整代码复制到 ``launch/turtlesim_world_1_launch.yaml``：

    .. literalinclude:: launch/turtlesim_world_1_launch.yaml
       :language: yaml

  .. group-tab:: Python

    将完整代码复制到 ``launch/turtlesim_world_1_launch.py``：

    .. literalinclude:: launch/turtlesim_world_1_launch.py
       :language: python

该启动文件会启动 ``turtlesim_node`` 节点，并将仿真配置参数传递给节点。

2.2 从 YAML 文件加载参数
~~~~~~~~~~~~~~~~~~~~~~~~

第二个启动文件将启动另一个使用不同配置的 turtlesim 仿真。创建 ``turtlesim_world_2_launch`` 文件。

.. tabs::

  .. group-tab:: XML

    将完整代码复制到 ``launch/turtlesim_world_2_launch.xml``：

    .. literalinclude:: launch/turtlesim_world_2_launch.xml
       :language: xml

  .. group-tab:: YAML

    将完整代码复制到 ``launch/turtlesim_world_2_launch.yaml``：

    .. literalinclude:: launch/turtlesim_world_2_launch.yaml
       :language: yaml

  .. group-tab:: Python

    将完整代码复制到 ``launch/turtlesim_world_2_launch.py``：

    .. literalinclude:: launch/turtlesim_world_2_launch.py
       :language: python

该启动文件会启动相同的 ``turtlesim_node``，但参数值直接从 YAML 配置文件中加载。

在 YAML 文件中定义参数，可以方便地保存和加载大量变量。需要注意，YAML 文件本身不是另一个启动文件，而是供 ``turtlesim_node`` 使用的参数配置文件。

还可以从当前 ``ros2 param`` 列表导出 YAML 文件。详情请参阅 :doc:`理解 ROS 2 参数 <../../Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters>` 教程。

在功能包的 ``config`` 目录中创建 ``turtlesim.yaml``，内容如下：

.. code-block:: yaml

   /turtlesim2/sim:
     ros__parameters:
       background_b: 255
       background_g: 86
       background_r: 150

有关参数和 YAML 文件的更多信息，请参阅 :doc:`理解 ROS 2 参数 <../../Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters>` 教程。

2.3 在 YAML 文件中使用通配符
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

有时需要为多个节点设置相同参数。这些节点可能具有不同的名称或命名空间，但参数相同。

如果为每个节点分别创建 YAML 文件并显式指定命名空间和节点名称，效率会很低。此时可以使用通配符，将参数应用于多个节点。

现在创建 ``turtlesim_world_3_launch`` 文件。它与 ``turtlesim_world_2_launch`` 类似，但会在新的 ``turtlesim3`` 命名空间中再启动一个 ``turtlesim_node``。

.. tabs::

  .. group-tab:: XML

    将完整代码复制到 ``launch/turtlesim_world_3_launch.xml``：

    .. literalinclude:: launch/turtlesim_world_3_launch.xml
       :language: xml
       :emphasize-lines: 3

  .. group-tab:: YAML

    将完整代码复制到 ``launch/turtlesim_world_3_launch.yaml``：

    .. literalinclude:: launch/turtlesim_world_3_launch.yaml
       :language: yaml
       :emphasize-lines: 7

  .. group-tab:: Python

    将完整代码复制到 ``launch/turtlesim_world_3_launch.py``：

    .. literalinclude:: launch/turtlesim_world_3_launch.py
       :language: python
       :emphasize-lines: 12

但是，如果继续加载原来的 YAML 文件，第三个 turtlesim 世界的外观不会发生变化。这是因为它的参数位于另一个命名空间中：

.. code-block:: text

   /turtlesim3/sim:
     background_b
     background_g
     background_r

因此，与其为相同节点创建多个配置文件，不如使用通配符。``/**`` 表示匹配任意节点名称和命名空间，可以将参数应用到多个节点。

将 ``config/turtlesim.yaml`` 更新为：

.. code-block:: yaml

   /**:
     ros__parameters:
       background_b: 255
       background_g: 86
       background_r: 150

现在，在顶层启动文件中包含 ``turtlesim_world_3_launch``。使用该配置文件后，``background_b``、``background_g`` 和 ``background_r`` 参数会被应用到 ``turtlesim3/sim`` 和 ``turtlesim2/sim`` 节点。

3. 命名空间
^^^^^^^^^^^

你可能已经注意到，我们在 ``turtlesim_world_2_launch`` 文件中定义了 turtlesim 世界的命名空间。

唯一的命名空间可以让系统同时启动多个相似节点，而不会产生节点名称或话题名称冲突。

.. code-block:: python

   namespace='turtlesim2',

但是，如果启动文件包含大量节点，逐个为它们定义命名空间会非常繁琐。可以使用 ``PushRosNamespace`` 动作，为启动文件描述中的所有节点设置全局命名空间。嵌套节点会自动继承该命名空间。

.. attention::

   ``PushRosNamespace`` 必须是动作列表中的第一个动作，后续动作才能应用该命名空间。

首先，从 ``turtlesim_world_2_launch`` 文件中删除 ``namespace='turtlesim2'``。然后更新 ``launch_turtlesim_launch``，将 include 语句修改为：

.. tabs::

  .. group-tab:: XML

    .. code-block:: xml

       <group>
         <push_ros_namespace namespace="turtlesim2" />
         <include file="$(find-pkg-share launch_tutorial)/launch/turtlesim_world_2_launch.xml" />
       </group>

  .. group-tab:: YAML

    .. code-block:: yaml

       - group:
           - push_ros_namespace:
               namespace: "turtlesim2"
           - include:
               file: "$(find-pkg-share launch_tutorial)/launch/turtlesim_world_2_launch.yaml"

  .. group-tab:: Python

    .. code-block:: python

       from launch.actions import GroupAction
       from launch_ros.actions import PushRosNamespace

       GroupAction(
         actions=[
           PushRosNamespace('turtlesim2'),
           IncludeLaunchDescription(
             PathJoinSubstitution([launch_dir, 'turtlesim_world_2_launch.py'])),
         ]
       )

这样，``turtlesim_world_2_launch`` 启动描述中的每个节点都会自动获得 ``turtlesim2`` 命名空间。

4. 复用节点
^^^^^^^^^^^

现在创建 ``broadcaster_listener_launch`` 文件。

.. tabs::

  .. group-tab:: XML

    将完整代码复制到 ``launch/broadcaster_listener_launch.xml``：

    .. literalinclude:: launch/broadcaster_listener_launch.xml
       :language: xml

  .. group-tab:: YAML

    将完整代码复制到 ``launch/broadcaster_listener_launch.yaml``：

    .. literalinclude:: launch/broadcaster_listener_launch.yaml
       :language: yaml

  .. group-tab:: Python

    将完整代码复制到 ``launch/broadcaster_listener_launch.py``：

    .. literalinclude:: launch/broadcaster_listener_launch.py
       :language: python

该文件声明了 ``target_frame`` 启动参数，默认值为 ``turtle1``。启动文件可以接收外部传入的参数；如果没有提供参数，就会将默认值传递给节点。

随后，启动文件使用不同的名称和参数启动两次 ``turtle_tf2_broadcaster`` 节点。这样可以在不发生冲突的情况下复用同一个节点。

此外，还会启动 ``turtle_tf2_listener`` 节点，并将前面声明的 ``target_frame`` 参数传递给它。

5. 参数覆盖
^^^^^^^^^^^

回顾顶层启动文件，其中包含了 ``broadcaster_listener_launch``，并向其传递了 ``target_frame`` 启动参数。

.. tabs::

  .. group-tab:: XML

    .. literalinclude:: launch/launch_turtlesim_launch.xml
       :language: xml
       :lines: 5-7

  .. group-tab:: YAML

    .. literalinclude:: launch/launch_turtlesim_launch.yaml
       :language: yaml
       :lines: 8-12

  .. group-tab:: Python

    .. literalinclude:: launch/launch_turtlesim_launch.py
       :language: python
       :lines: 16-19

这种语法可以将默认目标坐标系修改为 ``carrot1``。

如果希望 ``turtle2`` 跟随 ``turtle1``，而不是跟随 ``carrot1``，只需删除传递 ``target_frame`` 参数的那一行。这样就会使用该参数的默认值 ``turtle1``。

6. 重映射
^^^^^^^^^

现在创建 ``mimic_launch`` 文件。

.. tabs::

  .. group-tab:: XML

    将完整代码复制到 ``launch/mimic_launch.xml``：

    .. literalinclude:: launch/mimic_launch.xml
       :language: xml

  .. group-tab:: YAML

    将完整代码复制到 ``launch/mimic_launch.yaml``：

    .. literalinclude:: launch/mimic_launch.yaml
       :language: yaml

  .. group-tab:: Python

    将完整代码复制到 ``launch/mimic_launch.py``：

    .. literalinclude:: launch/mimic_launch.py
       :language: python

该启动文件会启动 ``mimic`` 节点，让一只 turtlesim 乌龟跟随另一只乌龟。

该节点默认从 ``/input/pose`` 话题接收目标位姿。本例希望将 ``/turtle2/pose`` 话题的数据重映射到该输入话题。

最后，将 ``/output/cmd_vel`` 话题重映射到 ``/turtlesim2/turtle1/cmd_vel``。这样，第二个仿真世界中的 ``turtle1`` 就会跟随第一个仿真世界中的 ``turtle2``。

7. 配置文件
^^^^^^^^^^^

创建 ``turtlesim_rviz_launch`` 文件。

.. tabs::

  .. group-tab:: XML

    将完整代码复制到 ``launch/turtlesim_rviz_launch.xml``：

    .. literalinclude:: launch/turtlesim_rviz_launch.xml
       :language: xml

  .. group-tab:: YAML

    将完整代码复制到 ``launch/turtlesim_rviz_launch.yaml``：

    .. literalinclude:: launch/turtlesim_rviz_launch.yaml
       :language: yaml

  .. group-tab:: Python

    将完整代码复制到 ``launch/turtlesim_rviz_launch.py``：

    .. literalinclude:: launch/turtlesim_rviz_launch.py
       :language: python

该启动文件会启动 RViz，并加载 ``turtle_tf2_py`` 功能包中定义的配置文件。该 RViz 配置会设置世界坐标系、启用 TF 可视化，并使用俯视视角启动 RViz。

8. 环境变量
^^^^^^^^^^^

在功能包中创建最后一个启动文件 ``fixed_broadcaster_launch``。

.. tabs::

  .. group-tab:: XML

    将完整代码复制到 ``launch/fixed_broadcaster_launch.xml``：

    .. literalinclude:: launch/fixed_broadcaster_launch.xml
       :language: xml

  .. group-tab:: YAML

    将完整代码复制到 ``launch/fixed_broadcaster_launch.yaml``：

    .. literalinclude:: launch/fixed_broadcaster_launch.yaml
       :language: yaml

  .. group-tab:: Python

    将完整代码复制到 ``launch/fixed_broadcaster_launch.py``：

    .. literalinclude:: launch/fixed_broadcaster_launch.py
       :language: python

该启动文件展示如何在启动文件中读取环境变量。环境变量可以用于定义或推送命名空间，以区分不同计算机或不同机器人上的节点。

.. note::

   如果运行启动文件的环境中没有定义 ``USER`` 环境变量（例如某些 ROS Docker 镜像），可以将上述环境变量替换为任意其他字符串。

运行启动文件
------------

1. 更新 setup.py
^^^^^^^^^^^^^^^^

打开 ``setup.py``，添加以下内容，以便安装 ``launch/`` 目录中的启动文件，以及 ``config/`` 目录中的配置文件。

``data_files`` 字段应类似于：

.. code-block:: python

   import os
   from glob import glob
   from setuptools import setup

   # ...

   data_files=[
       # ...
       (os.path.join('share', package_name, 'launch'), glob('launch/*')),
       (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
       (os.path.join('share', package_name, 'rviz'), glob('config/*.rviz')),
   ],

2. 构建并运行
^^^^^^^^^^^^^

构建功能包，然后使用以下命令启动顶层启动文件：

.. tabs::

  .. group-tab:: XML

    .. code-block:: console

       $ ros2 launch launch_tutorial launch_turtlesim_launch.xml

  .. group-tab:: YAML

    .. code-block:: console

       $ ros2 launch launch_tutorial launch_turtlesim_launch.yaml

  .. group-tab:: Python

    .. code-block:: console

       $ ros2 launch launch_tutorial launch_turtlesim_launch.py

此时会启动两个 turtlesim 仿真世界。第一个世界中有两只乌龟，第二个世界中有一只乌龟。

在第一个仿真世界中，``turtle2`` 会生成在世界左下方。它的目标是到达相对于 ``turtle1`` 坐标系在 x 轴方向上距离 5 米的 ``carrot1`` 坐标系。

第二个仿真世界中的 ``turtlesim2/turtle1`` 会模拟 ``turtle2`` 的运动行为。

如果希望控制 ``turtle1``，可以运行键盘遥操作节点：

.. code-block:: console

   $ ros2 run turtlesim turtle_teleop_key

运行后应看到类似的仿真画面：

.. image:: images/turtlesim_worlds.png

此外，RViz 也应该已经启动。它会显示相对于 ``world`` 坐标系的所有乌龟坐标系，其中 ``world`` 原点位于仿真世界的左下角。

.. image:: images/turtlesim_rviz.png

总结
----

本教程介绍了使用 ROS 2 启动文件管理大型项目的多种技巧和实践，包括顶层启动文件组织、参数、YAML 配置、通配符、命名空间、节点复用、参数覆盖、重映射、RViz 配置和环境变量。
