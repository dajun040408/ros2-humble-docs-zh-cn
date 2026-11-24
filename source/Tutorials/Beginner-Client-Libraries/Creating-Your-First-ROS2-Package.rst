.. redirect-from::

    Tutorials/Creating-Your-First-ROS2-Package

.. _CreatePkg:

创建功能包
==========

**目标：** 使用 CMake 或 Python 创建新功能包，并运行其中的可执行程序。

**教程级别：** 初级

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

1. 什么是 ROS 2 功能包？
^^^^^^^^^^^^^^^^^^^^^^^^

功能包是组织 ROS 2 代码的基本单元。如果希望安装代码或与他人分享，就需要将代码组织到功能包中。通过功能包，可以发布 ROS 2 开发成果，让其他人轻松构建和使用。

ROS 2 功能包使用 ament 作为构建系统，使用 colcon 作为构建工具。可以使用 CMake 或 Python 创建功能包，这两种构建类型均受官方支持，此外还存在其他构建类型。

2. ROS 2 功能包包含哪些内容？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ROS 2 Python 和 CMake 功能包各自具有最低内容要求：

.. tabs::

   .. group-tab:: CMake

      * CMakeLists.txt：描述如何构建功能包中的代码。
      * include/<package_name>：包含功能包的公共头文件。
      * package.xml：包含功能包元信息。
      * src：包含功能包源代码。

   .. group-tab:: Python

      * package.xml：包含功能包元信息。
      * resource/<package_name>：功能包标记文件。
      * setup.cfg：当功能包包含可执行程序时必须提供，以便 ros2 run 能够找到它们。
      * setup.py：包含安装功能包的说明。
      * <package_name>：与功能包同名的目录，包含 __init__.py，供 ROS 2 工具查找功能包。

最简单的功能包目录结构如下：

.. tabs::

   .. group-tab:: CMake

      .. code-block:: text

        my_package/
             CMakeLists.txt
             include/my_package/
             package.xml
             src/

   .. group-tab:: Python

      .. code-block:: text

        my_package/
              package.xml
              resource/my_package
              setup.cfg
              setup.py
              my_package/

3. 工作空间中的功能包
^^^^^^^^^^^^^^^^^^^^^

一个工作空间可以包含任意数量的功能包，每个功能包都位于自己的目录中。一个工作空间也可以包含不同构建类型的功能包，例如 CMake、Python 等，但不能嵌套功能包。

最佳实践是在工作空间中创建 src 目录，并将功能包放在其中，使工作空间顶层目录保持整洁。

一个简单的工作空间可能具有如下结构：

.. code-block:: text

   workspace_folder/
       src/
         cpp_package_1/
             CMakeLists.txt
             include/cpp_package_1/
             package.xml
             src/
         py_package_1/
             package.xml
             resource/py_package_1
             setup.cfg
             setup.py
             py_package_1/
         ...
         cpp_package_n/
             CMakeLists.txt
             include/cpp_package_n/
             package.xml
             src/


前置条件
--------

按照 :doc:`上一篇教程 <./Creating-A-Workspace/Creating-A-Workspace>` 的说明，准备好 ROS 2 工作空间。本教程将在该工作空间中创建功能包。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

首先 :doc:`source ROS 2 安装环境 <../Beginner-CLI-Tools/Configuring-ROS2-Environment>`。

本教程使用上一篇教程创建的 ros2_ws 工作空间。运行创建命令前，确保当前目录为 src。

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        $ cd ~/ros2_ws/src

   .. group-tab:: macOS

      .. code-block:: console

        $ cd ~/ros2_ws/src

   .. group-tab:: Windows

      .. code-block:: console

        $ cd \ros2_ws\src

ROS 2 中创建功能包的命令格式如下：

.. tabs::

   .. group-tab:: CMake

      .. code-block:: console

        $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 <package_name>

   .. group-tab:: Python

      .. code-block:: console

        $ ros2 pkg create --build-type ament_python --license Apache-2.0 <package_name>

本教程使用可选参数 --node-name，在功能包中创建一个简单的 Hello World 可执行程序。

在终端中输入：

.. tabs::

   .. group-tab:: CMake

      .. code-block:: console

        $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 --node-name my_node my_package

   .. group-tab:: Python

      .. code-block:: console

        $ ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name my_node my_package

现在，工作空间 ``src`` 目录中会出现名为 ``my_package`` 的新目录。终端会输出新功能包的名称、目标目录、package format、版本、描述、维护者、许可证、构建类型和生成的文件列表。

例如，CMake 功能包的输出类似：

.. code-block:: console

   going to create a new package
   package name: my_package
   destination directory: /home/user/ros2_ws/src
   package format: 3
   version: 0.0.0
   description: TODO: Package description
   maintainer: ['<name> <email>']
   licenses: ['TODO: License declaration']
   build type: ament_cmake
   dependencies: []
   node_name: my_node
   creating folder ./my_package
   creating ./my_package/package.xml
   creating source and include folder
   creating folder ./my_package/src
   creating folder ./my_package/include/my_package
   creating ./my_package/CMakeLists.txt
   creating ./my_package/src/my_node.cpp

Python 功能包的输出类似：

.. code-block:: console

   going to create a new package
   package name: my_package
   destination directory: /home/user/ros2_ws/src
   package format: 3
   version: 0.0.0
   description: TODO: Package description
   maintainer: ['<name> <email>']
   licenses: ['TODO: License declaration']
   build type: ament_python
   dependencies: []
   node_name: my_node
   creating folder ./my_package
   creating ./my_package/package.xml
   creating source folder
   creating folder ./my_package/my_package
   creating ./my_package/setup.py
   creating ./my_package/setup.cfg
   creating folder ./my_package/resource
   creating folder ./my_package/my_package
   creating ./my_package/my_package/__init__.py
   creating folder ./my_package/test
   creating ./my_package/test/test_copyright.py
   creating ./my_package/test/test_flake8.py
   creating ./my_package/test/test_pep257.py
   creating ./my_package/my_package/my_node.py

可以看到，ROS 2 已经自动生成了新功能包所需的文件。

2. 构建功能包
^^^^^^^^^^^^^

将功能包放入工作空间的好处是，可以在工作空间根目录运行 colcon build，一次构建多个功能包，而不必逐个构建。

返回工作空间根目录：

.. code-block:: console

   $ cd ~/ros2_ws

然后构建功能包：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ colcon build

  .. group-tab:: macOS

    .. code-block:: console

      $ colcon build

  .. group-tab:: Windows

    .. code-block:: console

      $ colcon build --merge-install

Windows 不允许过长路径，因此 merge-install 会将所有路径合并到 install 目录中。

回顾上一教程，ros2_ws 中还包含 ros_tutorials 功能包。运行 colcon build 时，turtlesim 也会被构建。工作空间功能包较少时没有问题，但功能包很多时，完整构建可能耗时较长。

下次如果只想构建 my_package，可以运行：

.. code-block:: console

    $ colcon build --packages-select my_package

3. source 设置文件
^^^^^^^^^^^^^^^^^^

要使用新功能包及其可执行程序，先打开新终端并 source 主 ROS 2 安装环境。

然后在 ros2_ws 目录中运行以下命令 source 工作空间：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ source install/local_setup.bash

  .. group-tab:: macOS

    .. code-block:: console

      $ . install/local_setup.bash

  .. group-tab:: Windows

    .. code-block:: console

      $ call install/local_setup.bat

现在工作空间已经添加到路径中，可以使用新功能包的可执行程序。

4. 使用功能包
^^^^^^^^^^^^^

要运行创建功能包时通过 --node-name 参数生成的可执行程序，输入：

.. code-block:: console

  $ ros2 run my_package my_node

终端会返回以下消息：

.. tabs::

   .. group-tab:: CMake

      .. code-block:: console

        hello world my_package package

   .. group-tab:: Python

      .. code-block:: console

        Hi from my_package.

5. 检查功能包内容
^^^^^^^^^^^^^^^^^

在 ros2_ws/src/my_package 中，可以看到 ros2 pkg create 自动生成的文件和目录：

.. tabs::

   .. group-tab:: CMake

      .. code-block:: text

        CMakeLists.txt  include  package.xml  src

      my_node.cpp 位于 src 目录中。以后自定义的 C++ 节点也会放在这里。

   .. group-tab:: Python

      .. code-block:: text

        my_package  package.xml  resource  setup.cfg  setup.py  test

      my_node.py 位于 my_package 目录中。以后自定义的 Python 节点也会放在这里。

6. 自定义 package.xml
^^^^^^^^^^^^^^^^^^^^^

创建功能包时，终端返回信息中的 description 和 license 字段包含 TODO 提示。这是因为功能包描述和许可证声明不会自动设置，但如果以后要发布功能包，就必须填写。maintainer 字段也可能需要补充。

使用文本编辑器打开 ros2_ws/src/my_package/package.xml。请填写维护者姓名和邮箱，将 description 修改为功能包用途，并填写许可证。

例如，CMake 和 Python 功能包的 ``package.xml`` 都包含包名、版本、描述、维护者、许可证和构建类型等元信息。CMake 功能包还会声明 ``ament_cmake`` 构建工具依赖，Python 功能包则会声明相应的测试依赖。

CMake 功能包中的相关配置示例：

.. code-block:: xml

   <package format="3">
     <name>my_package</name>
     <version>0.0.0</version>
     <description>Beginner client libraries tutorials practice package</description>
     <maintainer email="you@email.com">Your Name</maintainer>
     <license>Apache License 2.0</license>

     <buildtool_depend>ament_cmake</buildtool_depend>

     <test_depend>ament_lint_auto</test_depend>
     <test_depend>ament_lint_common</test_depend>

     <export>
       <build_type>ament_cmake</build_type>
     </export>
   </package>

Python 功能包中的相关配置示例：

.. code-block:: xml

   <package format="3">
     <name>my_package</name>
     <version>0.0.0</version>
     <description>Beginner client libraries tutorials practice package</description>
     <maintainer email="you@email.com">Your Name</maintainer>
     <license>Apache License 2.0</license>

     <test_depend>ament_copyright</test_depend>
     <test_depend>ament_flake8</test_depend>
     <test_depend>ament_pep257</test_depend>
     <test_depend>python3-pytest</test_depend>

     <export>
       <build_type>ament_python</build_type>
     </export>
   </package>

开源许可证列表请参阅 `OSI 许可证列表 <https://opensource.org/licenses/alphabetical>`_。本教程仅用于练习，可以选择任意许可证，这里使用 ``Apache License 2.0``。

license 标签下方以 ``_depend`` 结尾的标签用于声明功能包依赖，供 colcon 查找。``my_package`` 很简单，没有依赖项，但后续教程会使用这些标签。

开源许可证列表请参阅`OSI 许可证列表 <https://opensource.org/licenses/alphabetical>`_。本教程仅用于练习，可以选择任意许可证，这里使用 Apache License 2.0。

license 标签下方以 _depend 结尾的标签用于声明功能包依赖，供 colcon 查找。my_package 很简单，没有依赖项，但后续教程会使用这些标签。

.. tabs::

   .. group-tab:: CMake

      到这里，CMake 功能包的配置就完成了。

   .. group-tab:: Python

      setup.py 文件也包含与 package.xml 相同的 description、maintainer 和 license 字段，因此也需要同步填写。两个文件中的这些字段必须完全一致，version 和 name（package_name）也必须一致。

      打开 ``setup.py``，修改 ``maintainer``、``maintainer_email`` 和 ``description``，使其与 ``package.xml`` 相同，并填写许可证。

      .. code-block:: python

         from setuptools import setup

         package_name = 'my_package'

         setup(
           name=package_name,
           version='0.0.0',
           packages=[package_name],
           data_files=[
             ('share/ament_index/resource_index/packages',
               ['resource/' + package_name]),
             ('share/' + package_name, ['package.xml']),
           ],
           install_requires=['setuptools'],
           zip_safe=True,
           maintainer='Your Name',
           maintainer_email='you@email.com',
           description='Beginner client libraries tutorials practice package',
           license='Apache License 2.0',
           tests_require=['pytest'],
           entry_points={
             'console_scripts': [
               'my_node = my_package.my_node:main'
             ],
           },
         )

      保存文件。

总结
----

你已经创建了一个功能包，用于组织代码并方便其他人使用。

功能包自动生成了必要文件，然后通过 colcon 构建，使其可执行程序能够在本地环境中使用。

下一步
------

接下来为功能包添加实际功能。可以选择使用 :doc:`C++ <./Writing-A-Simple-Cpp-Publisher-And-Subscriber>` 或 :doc:`Python <./Writing-A-Simple-Py-Publisher-And-Subscriber>` 编写简单的发布者/订阅者系统。
