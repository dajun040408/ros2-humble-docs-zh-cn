.. redirect-from::

  Guides/Launch-file-different-formats

使用 XML、YAML 和 Python 编写 ROS 2 启动文件
============================================

.. contents:: 目录
   :depth: 2
   :local:

ROS 2 启动文件可以使用 XML、YAML 和 Python 编写。本指南展示如何使用不同格式完成相同任务，并讨论每种格式适合的使用场景。

启动文件示例
------------

下面分别展示使用 XML、YAML 和 Python 实现的启动文件。每个启动文件都会执行以下操作：

* 设置带默认值的命令行参数。
* 包含另一个启动文件。
* 在另一个命名空间中包含启动文件。
* 启动一个节点并设置其命名空间。
* 启动一个节点，设置其命名空间，并为该节点设置参数（使用传入的参数）。
* 创建一个节点，将消息从一个话题重映射到另一个话题。

.. tabs::

   .. group-tab:: XML

      .. literalinclude:: launch/different_formats_launch.xml
        :language: xml

   .. group-tab:: YAML

      .. literalinclude:: launch/different_formats_launch.yaml
        :language: yaml

   .. group-tab:: Python

      .. literalinclude:: launch/different_formats_launch.py
        :language: python

通过命令行使用启动文件
----------------------

启动
^^^^

上述任意启动文件都可以使用 ``ros2 launch`` 运行。要在本地尝试，可以先创建一个新功能包，然后运行：

.. code-block:: console

  $ ros2 launch <package_name> <launch_file_name>

也可以直接指定启动文件路径来运行：

.. code-block:: console

  $ ros2 launch <path_to_launch_file>

设置参数
^^^^^^^^

要向启动文件传递参数，应使用 ``key:=value`` 语法。例如，可以通过以下方式设置 ``background_r`` 的值：

.. code-block:: console

  $ ros2 launch <package_name> <launch_file_name> background_r:=255

或者：

.. code-block:: console

  $ ros2 launch <path_to_launch_file> background_r:=255

控制海龟
^^^^^^^^

要测试重映射是否生效，可以在另一个终端中运行以下命令控制海龟：

.. code-block:: console

  $ ros2 run turtlesim turtle_teleop_key --ros-args --remap __ns:=/turtlesim1

.. _launch-file-different-formats-which:

XML、YAML 还是 Python：应该使用哪一种？
---------------------------------------

.. note::

  ROS 1 的启动文件使用 XML 编写，因此对于从 ROS 1 迁移过来的用户，XML 可能最熟悉。有关变化内容，请参阅 :doc:`从 ROS 1 迁移启动文件 <Migrating-from-ROS1/Migrating-Launch-Files>`。

对于大多数应用，选择哪种 ROS 2 启动文件格式主要取决于开发者偏好。不过，如果启动文件需要 XML 或 YAML 无法实现的灵活性，则可以使用 Python 编写。

Python 启动文件更加灵活，主要有两个原因：

* Python 是一种脚本语言，因此可以在启动文件中使用该语言及其库。
* `ros2/launch <https://github.com/ros2/launch>`__ （通用启动功能）和 `ros2/launch_ros <https://github.com/ros2/launch_ros>`__ （ROS 2 专用启动功能）都是使用 Python 编写的，因此你可以更直接地访问 XML 和 YAML 未暴露的底层启动功能。

不过，与 XML 或 YAML 相比，使用 Python 编写的启动文件可能更加复杂，代码也更加冗长。
