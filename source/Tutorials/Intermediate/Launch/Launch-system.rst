.. redirect-from::

  Tutorials/Launch-system
  Tutorials/Launch-Files/Launch-system
  Tutorials/Launch/Launch-system

将启动文件集成到 ROS 2 功能包
==============================

**目标：** 向 ROS 2 功能包添加启动文件。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

前置条件
--------

你应当已经完成 :doc:`创建 ROS 2 功能包 <../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>` 教程。每次打开新终端时，都不要忘记 source ROS 2 环境，参见 :doc:`配置 ROS 2 环境 <../../Beginner-CLI-Tools/Configuring-ROS2-Environment>`。

背景
----

在 :doc:`上一个教程 <Creating-Launch-Files>` 中，我们学习了如何编写独立启动文件。本教程将介绍如何将启动文件添加到现有功能包，以及通常采用的目录约定。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

创建用于存放功能包的工作空间：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ mkdir -p launch_ws/src
      $ cd launch_ws/src

  .. group-tab:: macOS

    .. code-block:: console

      $ mkdir -p launch_ws/src
      $ cd launch_ws/src

  .. group-tab:: Windows

    .. code-block:: console

      $ md launch_ws\src
      $ cd launch_ws\src

.. tabs::

  .. group-tab:: Python 功能包

    .. code-block:: console

      $ ros2 pkg create --build-type ament_python --license Apache-2.0 py_launch_example

  .. group-tab:: C++ 功能包

    .. code-block:: console

      $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_launch_example

2. 创建存放启动文件的目录结构
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

按照约定，功能包的所有启动文件都存放在该功能包内部的 `launch` 目录中。请在刚才创建的功能包顶层目录下创建 `launch` 目录。

.. tabs::

  .. group-tab:: Python 功能包

    Python 功能包的目录结构应如下所示：

    .. code-block:: text

      src/
        py_launch_example/
          launch/
          package.xml
          py_launch_example/
          resource/
          setup.cfg
          setup.py
          test/

    为了让 colcon 能够找到并使用启动文件，需要在 Python setup 工具中声明这些文件。打开 `setup.py`，在顶部添加必要的 import 语句，并将启动文件加入 `setup()` 的 `data_files` 参数：

    .. code-block:: python

      import os
      from glob import glob

      package_name = 'py_launch_example'

      setup(
          data_files=[
              (os.path.join('share', package_name, 'launch'), glob('launch/*'))
          ]
      )

  .. group-tab:: C++ 功能包

    对于 C++ 功能包，只需修改 `CMakeLists.txt`，添加以下内容：

    .. code-block:: cmake

      install(DIRECTORY
        launch
        DESTINATION share/${PROJECT_NAME}/
      )

    将其放在文件末尾，但必须位于 `ament_package()` 之前。

3. 编写启动文件
^^^^^^^^^^^^^^^

.. tabs::

  .. group-tab:: XML 启动文件

    在 `launch` 目录中创建名为 `my_script_launch.xml` 的启动文件。建议但不强制使用 `_launch.xml` 作为 XML 启动文件的后缀。

    .. literalinclude:: launch/my_script_launch.xml
      :language: xml

  .. group-tab:: YAML 启动文件

    在 `launch` 目录中创建名为 `my_script_launch.yaml` 的启动文件。建议但不强制使用 `_launch.yaml` 作为 YAML 启动文件的后缀。

    .. literalinclude:: launch/my_script_launch.yaml
      :language: yaml

  .. group-tab:: Python 启动文件

    在 `launch` 目录中创建名为 `my_script_launch.py` 的启动文件。建议但不强制使用 `_launch.py` 作为 Python 启动文件的后缀。不过，为了让 `ros2 launch` 识别并自动补全该文件名，启动文件名称必须以 `launch.py` 结尾。

    启动文件应定义 `generate_launch_description()` 函数，并返回供 `ros2 launch` 命令使用的 `launch.LaunchDescription()`。

    .. literalinclude:: launch/my_script_launch.py
      :language: python

4. 构建并运行启动文件
^^^^^^^^^^^^^^^^^^^^^

进入工作空间顶层目录并构建：

.. code-block:: console

  $ colcon build

`colcon build` 成功且已 source 工作空间后，就可以运行启动文件。

.. tabs::

  .. group-tab:: Python 功能包

    .. tabs::

      .. group-tab:: XML 启动文件

        .. code-block:: console

          $ ros2 launch py_launch_example my_script_launch.xml

      .. group-tab:: YAML 启动文件

        .. code-block:: console

          $ ros2 launch py_launch_example my_script_launch.yaml

      .. group-tab:: Python 启动文件

        .. code-block:: console

          $ ros2 launch py_launch_example my_script_launch.py

  .. group-tab:: C++ 功能包

    .. tabs::

      .. group-tab:: XML 启动文件

        .. code-block:: console

          $ ros2 launch cpp_launch_example my_script_launch.xml

      .. group-tab:: YAML 启动文件

        .. code-block:: console

          $ ros2 launch cpp_launch_example my_script_launch.yaml

      .. group-tab:: Python 启动文件

        .. code-block:: console

          $ ros2 launch cpp_launch_example my_script_launch.py

文档
----

`Launch 文档 <https://github.com/ros2/launch/blob/{REPOS_FILE_BRANCH}/launch/doc/source/architecture.rst>`_ 提供了更多细节，介绍 `launch_ros` 中使用的相关概念。

后续还会提供更多关于 Launch 功能的文档和示例。在此之前，可以参考源代码：`https://github.com/ros2/launch` 和 `https://github.com/ros2/launch_ros`。
