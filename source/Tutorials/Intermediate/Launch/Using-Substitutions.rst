.. redirect-from::

    Tutorials/Launch-Files/Using-Substitutions
    Tutorials/Launch/Using-Substitutions

在启动文件中使用替换
====================

**目标：** 了解 ROS 2 启动文件中的替换机制。

**教程级别：** 中级

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

启动文件用于启动节点、服务和执行进程。这些操作可以接收参数，以影响其行为。

替换（Substitutions）可以在启动操作的参数中使用，使启动文件更灵活、更容易复用。替换表达式只会在启动描述执行时求值，可以用于获取启动配置、环境变量等信息，也可以执行任意 Python 表达式。

本教程通过示例介绍如何在 ROS 2 启动文件中使用替换。

前置条件
--------

本教程使用 :doc:`turtlesim <../../Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim>` 功能包，并假设你已经了解如何 :doc:`创建功能包 <../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>`。

每次打开新终端时，都不要忘记 :doc:`source ROS 2 环境 <../../Beginner-CLI-Tools/Configuring-ROS2-Environment>`。

使用替换
--------

1. 创建并配置功能包
^^^^^^^^^^^^^^^^^^^

首先创建一个名为 ``launch_tutorial`` 的新功能包：

.. tabs::

  .. group-tab:: Python 功能包

    创建 ``ament_python`` 构建类型的功能包：

    .. code-block:: console

       $ ros2 pkg create --build-type ament_python --license Apache-2.0 launch_tutorial

  .. group-tab:: C++ 功能包

    创建 ``ament_cmake`` 构建类型的功能包：

    .. code-block:: console

       $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 launch_tutorial

在功能包中创建名为 ``launch`` 的目录：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ mkdir launch_tutorial/launch

  .. group-tab:: macOS

    .. code-block:: console

       $ mkdir launch_tutorial/launch

  .. group-tab:: Windows

    .. code-block:: console

       $ md launch_tutorial/launch

最后，确保安装 launch 文件。

.. tabs::

  .. group-tab:: Python 功能包

    在功能包的 ``setup.py`` 中添加以下内容：

    .. code-block:: python

       import os
       from glob import glob
       from setuptools import find_packages, setup

       package_name = 'launch_tutorial'

       setup(
           # 其他参数……
           data_files=[
               # 其他数据文件……
               (os.path.join('share', package_name, 'launch'), glob('launch/*'))
           ]
       )

  .. group-tab:: C++ 功能包

    在 ``CMakeLists.txt`` 的 ``ament_package()`` 之前追加：

    .. code-block:: cmake

       install(DIRECTORY
         launch
         DESTINATION share/${PROJECT_NAME}/
       )

2. 父启动文件
^^^^^^^^^^^^^

创建一个启动文件，用于调用另一个启动文件并向其传递参数。启动文件可以使用 YAML、XML 或 Python 格式。

在 ``launch_tutorial`` 功能包的 ``launch`` 目录中创建以下文件。

.. tabs::

  .. group-tab:: XML

    将完整代码复制到 ``launch/example_main_launch.xml``：

    .. literalinclude:: launch/example_main_launch.xml
       :language: xml

    ``$(find-pkg-share launch_tutorial)`` 替换用于查找 ``launch_tutorial`` 功能包的路径，再与 ``example_substitutions_launch.xml`` 文件名拼接，得到被包含启动文件的路径。

    .. literalinclude:: launch/example_main_launch.xml
       :language: xml
       :lines: 4

    ``include`` 操作接收 ``background_r``、``turtlesim_ns`` 和 ``use_provided_red`` 等参数。``$(var background_r)`` 替换会读取 ``background_r`` 的值，并将其作为 ``new_background_r`` 参数传递。

    .. literalinclude:: launch/example_main_launch.xml
       :language: xml
       :lines: 5-7

  .. group-tab:: YAML

    将完整代码复制到 ``launch/example_main_launch.yaml``：

    .. literalinclude:: launch/example_main_launch.yaml
       :language: yaml

    ``$(find-pkg-share launch_tutorial)`` 替换用于查找 ``launch_tutorial`` 功能包的路径，再与 ``example_substitutions_launch.yaml`` 文件名拼接。

    .. literalinclude:: launch/example_main_launch.yaml
       :language: yaml
       :lines: 8

    ``include`` 操作接收 ``background_r``、``turtlesim_ns`` 和 ``use_provided_red`` 等参数。``$(var background_r)`` 替换会读取 ``background_r`` 的值，并将其作为 ``new_background_r`` 参数传递。

    .. literalinclude:: launch/example_main_launch.yaml
       :language: yaml
       :lines: 9-15

  .. group-tab:: Python

    将完整代码复制到 ``launch/example_main_launch.py``：

    .. literalinclude:: launch/example_main_launch.py
       :language: python

    ``FindPackageShare`` 替换用于查找 ``launch_tutorial`` 功能包的路径，``PathJoinSubstitution`` 则将该路径与 ``example_substitutions.launch.py`` 文件名拼接。

    .. literalinclude:: launch/example_main_launch.py
       :language: python
       :lines: 14-18

    ``launch_arguments`` 字典中的 ``turtlesim_ns`` 和 ``use_provided_red`` 等参数会传递给 ``IncludeLaunchDescription`` 操作。

    .. literalinclude:: launch/example_main_launch.py
       :language: python
       :lines: 19-23

3. 替换示例启动文件
^^^^^^^^^^^^^^^^^^^

现在在同一目录中创建用于演示替换的启动文件。

.. tabs::

  .. group-tab:: XML

    创建 ``launch/example_substitutions_launch.xml``，并写入以下代码：

    .. literalinclude:: launch/example_substitutions_launch.xml
       :language: xml

    这里定义了 ``turtlesim_ns``、``use_provided_red`` 和 ``new_background_r`` 三个启动配置。它们用于保存启动参数的值，并将这些值传递给相应的启动操作。之后可以通过 ``$(var <name>)`` 替换，在启动描述的任意位置获取启动参数的值。

    ``arg`` 标签用于声明启动参数。该参数既可以由父启动文件传入，也可以在命令行中指定。

    .. literalinclude:: launch/example_substitutions_launch.xml
       :language: xml
       :lines: 3-5

    接下来定义 ``turtlesim_node`` 节点，并使用 ``$(var <name>)`` 替换将其命名空间设置为 ``turtlesim_ns`` 的值。

    .. literalinclude:: launch/example_substitutions_launch.xml
       :language: xml
       :lines: 7

    随后定义 ``executable`` 操作及其 ``cmd`` 标签。该命令会调用 turtlesim 节点的 spawn 服务，并使用 ``$(var <name>)`` 替换获取 ``turtlesim_ns`` 参数值，构造命令字符串。

    .. literalinclude:: launch/example_substitutions_launch.xml
       :language: xml
       :lines: 8

    后续的 ``ros2 param`` executable 操作采用相同方式修改 turtlesim 背景的红色分量。区别在于，定时器中的第二个操作只有在 ``new_background_r`` 等于 200，且 ``use_provided_red`` 为 True 时才会执行。``if`` 条件使用 ``$(eval <python-expression>)`` 替换进行求值。

    .. literalinclude:: launch/example_substitutions_launch.xml
       :language: xml
       :lines: 9-13

  .. group-tab:: YAML

    创建 ``launch/example_substitutions_launch.yaml``，并写入以下代码：

    .. literalinclude:: launch/example_substitutions_launch.yaml
       :language: yaml

    这里定义了 ``turtlesim_ns``、``use_provided_red`` 和 ``new_background_r`` 三个启动配置。它们用于保存启动参数的值，并将这些值传递给相应的启动操作。之后可以通过 ``$(var <name>)`` 替换，在启动描述的任意位置获取启动参数的值。

    ``arg`` 标签用于声明启动参数，该参数既可以由父启动文件传入，也可以在命令行中指定。

    .. literalinclude:: launch/example_substitutions_launch.yaml
       :language: yaml
       :lines: 4-12

    接下来定义 ``turtlesim_node`` 节点，并使用 ``$(var <name>)`` 替换将其命名空间设置为 ``turtlesim_ns`` 的值。

    .. literalinclude:: launch/example_substitutions_launch.yaml
       :language: yaml
       :lines: 14-18

    随后定义 ``executable`` 操作及其 ``cmd`` 标签。该命令会调用 turtlesim 节点的 spawn 服务，并使用 ``$(var <name>)`` 替换获取 ``turtlesim_ns`` 参数值，构造命令字符串。

    .. literalinclude:: launch/example_substitutions_launch.yaml
       :language: yaml
       :lines: 19-20

    后续的 ``ros2 param`` executable 操作采用相同方式修改 turtlesim 背景的红色分量。区别在于，定时器中的第二个操作只有在 ``new_background_r`` 等于 200，且 ``use_provided_red`` 为 True 时才会执行。``if`` 条件使用 ``$(eval <python-expression>)`` 替换进行求值。

    .. literalinclude:: launch/example_substitutions_launch.yaml
       :language: yaml
       :lines: 21-28

  .. group-tab:: Python

    创建 ``launch/example_substitutions.launch.py``，并写入以下代码：

    .. literalinclude:: launch/example_substitutions_launch.py
       :language: python

    这里定义了 ``turtlesim_ns``、``use_provided_red`` 和 ``new_background_r`` 三个启动配置。``LaunchConfiguration`` 替换用于表示启动参数的值，并允许在启动描述的任意位置获取这些值。

    ``DeclareLaunchArgument`` 用于声明启动参数。该参数既可以由父启动文件传入，也可以在命令行中指定。

    .. literalinclude:: launch/example_substitutions_launch.py
       :language: python
       :lines: 14-25

    接下来定义 ``turtlesim_node`` 节点，并将其命名空间设置为 ``turtlesim_ns`` 对应的 ``LaunchConfiguration`` 替换。

    .. literalinclude:: launch/example_substitutions_launch.py
       :language: python
       :lines: 26-31

    随后使用 ``ExecuteProcess`` 操作，并通过 ``cmd`` 参数调用 turtlesim 节点的 spawn 服务。``LaunchConfiguration`` 替换用于在命令字符串中提供 ``turtlesim_ns`` 参数值。

    .. literalinclude:: launch/example_substitutions_launch.py
       :language: python
       :lines: 32-41

    后续的 ``change_background_r`` 和 ``change_background_r_conditioned`` 操作采用相同方式修改 turtlesim 背景的红色分量。区别在于，第二个操作只有在 ``new_background_r`` 等于 200，且 ``use_provided_red`` 为 True 时才会执行。``IfCondition`` 中的表达式使用 ``PythonExpression`` 替换进行求值。

    .. literalinclude:: launch/example_substitutions_launch.py
       :language: python
       :lines: 51-72

4. 构建功能包
^^^^^^^^^^^^^

进入工作空间根目录并构建功能包：

.. code-block:: console

   $ colcon build

构建完成后，记得 source 工作空间环境。

运行示例
--------

现在可以使用 ``ros2 launch`` 命令启动示例。

.. tabs::

  .. group-tab:: YAML

    .. code-block:: console

       $ ros2 launch launch_tutorial example_main.launch.yaml

  .. group-tab:: XML

    .. code-block:: console

       $ ros2 launch launch_tutorial example_main_launch.xml

  .. group-tab:: Python

    .. code-block:: console

       $ ros2 launch launch_tutorial example_main.launch.py

启动后会执行以下操作：

#. 启动一个蓝色背景的 turtlesim 节点。
#. 生成第二只乌龟。
#. 将背景颜色改为紫色。
#. 如果 ``background_r`` 参数为 200 且 ``use_provided_red`` 为 True，则在两秒后将背景颜色改为粉色。

修改启动参数
------------

.. tabs::

  .. group-tab:: YAML

    可以直接修改 ``example_main.launch.yaml`` 中的 ``background_r`` 变量，也可以使用指定参数启动 ``example_substitutions.launch.yaml``。

    查看启动文件支持的参数：

    .. code-block:: console

       $ ros2 launch launch_tutorial example_substitutions.launch.yaml --show-args

  .. group-tab:: XML

    可以直接修改 ``example_main_launch.xml`` 中的 ``background_r`` 变量，也可以使用指定参数启动 ``example_substitutions_launch.xml``。

    查看启动文件支持的参数：

    .. code-block:: console

       $ ros2 launch launch_tutorial example_substitutions_launch.xml --show-args

  .. group-tab:: Python

    可以修改 ``example_main.launch.py`` 中 ``launch_arguments`` 字典里的参数，也可以使用指定参数启动 ``example_substitutions.launch.py``。

    查看启动文件支持的参数：

    .. code-block:: console

       $ ros2 launch launch_tutorial example_substitutions.launch.py --show-args

命令会显示启动文件支持的参数及其默认值：

.. code-block:: console

   Arguments (pass arguments as '<name>:=<value>'):

       'turtlesim_ns':
           no description given
           (default: 'turtlesim1')

       'use_provided_red':
           no description given
           (default: 'False')

       'new_background_r':
           no description given
           (default: '200')

现在可以将所需参数传递给启动文件：

.. tabs::

  .. group-tab:: YAML

    .. code-block:: console

       $ ros2 launch launch_tutorial example_substitutions.launch.yaml turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200

  .. group-tab:: XML

    .. code-block:: console

       $ ros2 launch launch_tutorial example_substitutions_launch.xml turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200

  .. group-tab:: Python

    .. code-block:: console

       $ ros2 launch launch_tutorial example_substitutions.launch.py turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200

文档
----

有关可用替换的详细信息，请参阅 `Launch 文档 <https://docs.ros.org/en/{DISTRO}/p/launch/doc/source/architecture.html>`_。

总结
----

本教程介绍了启动文件中的替换机制，以及如何利用替换的灵活性和功能创建可复用的启动文件。

接下来可以学习 :doc:`在启动文件中使用事件处理器 <./Using-Event-Handlers>`，了解如何定义一组复杂规则，并在启动过程中动态修改启动行为。
