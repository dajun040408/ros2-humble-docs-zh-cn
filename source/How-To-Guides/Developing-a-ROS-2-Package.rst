.. redirect-from::

    Developing-a-ROS-2-Package
    Guides/Developing-a-ROS-2-Package
    Tutorials/Developing-a-ROS-2-Package

开发 ROS 2 功能包
##################

.. contents:: 目录
   :depth: 2
   :local:

本教程将指导你创建第一个 ROS 2 应用程序。它面向希望学习如何在 ROS 2 中创建自定义功能包的开发者，而不是只希望使用 ROS 2 现有功能包的用户。

前置条件
--------

* :doc:`安装 ROS <../../Installation>`。
* `安装 colcon <https://colcon.readthedocs.io/en/released/user/installation.html>`__。
* 通过加载 ROS 2 安装环境脚本配置工作空间环境。

创建功能包
----------

在工作空间中运行以下命令，即可创建 ROS 2 功能包：

.. code-block:: console

   $ ros2 pkg create --license Apache-2.0 <pkg-name> --dependencies [deps]

通常在工作空间的 ``<workspace-name>/src`` 目录中执行，例如 ``nav2_ws/src`` 或 ``my_robot_ws/src``。

如果要为特定客户端库创建功能包，可以指定对应的构建类型：

.. tabs::

  .. group-tab:: C++

    .. code-block:: console

       $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 <pkg-name> --dependencies [deps]

  .. group-tab:: Python

    .. code-block:: console

       $ ros2 pkg create --build-type ament_python --license Apache-2.0 <pkg-name> --dependencies [deps]

之后，你可以更新 ``package.xml``，填写功能包信息，例如依赖项、描述和作者信息。

C++ 功能包
^^^^^^^^^^

通常使用 ``add_executable()`` CMake 宏创建可执行节点，并通过以下函数声明依赖关系：

.. code-block:: cmake

   ament_target_dependencies(<executable-name> [dependencies])

要安装 launch 文件和节点，可以在文件末尾、``ament_package()`` 宏之前使用 ``install()`` 宏。

launch 文件和节点的安装示例：

.. code-block:: cmake

   # Install launch files
   install(
     DIRECTORY launch
     DESTINATION share/${PROJECT_NAME}
   )

   # Install nodes
   install(
     TARGETS [node-names]
     DESTINATION lib/${PROJECT_NAME}
   )

Python 功能包
^^^^^^^^^^^^^

ROS 2 遵循 Python 标准模块分发流程，使用 ``setuptools``。对于 Python 功能包，``setup.py`` 文件承担的作用类似于 C++ 功能包中的 ``CMakeLists.txt``。

有关 Python 模块分发的更多细节，请参阅 `Python 官方文档 <https://docs.python.org/3/distributing/index.html#distributing-index>`__。

ROS 2 Python 功能包中应包含一个 ``setup.cfg`` 文件，内容如下：

.. code-block:: ini

   [develop]
   script_dir=$base/lib/<package-name>
   [install]
   install_scripts=$base/lib/<package-name>

同时还需要一个 ``setup.py`` 文件，例如：

.. code-block:: python

   import os
   from glob import glob
   from setuptools import setup

   package_name = 'my_package'

   setup(
       name=package_name,
       version='0.0.0',
       # Packages to export
       packages=[package_name],
       # Files we want to install, specifically launch files
       data_files=[
           # Install marker file in the package index
           ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
           # Include our package.xml file
           (os.path.join('share', package_name), ['package.xml']),
           # Include all launch files.
           (os.path.join('share', package_name, 'launch'), glob('launch/*')),
       ],
       # This is important as well
       install_requires=['setuptools'],
       zip_safe=True,
       author='ROS 2 Developer',
       author_email='ros2@ros.com',
       maintainer='ROS 2 Developer',
       maintainer_email='ros2@ros.com',
       keywords=['foo', 'bar'],
       classifiers=[
           'Intended Audience :: Developers',
           'License :: TODO',
           'Programming Language :: Python',
           'Topic :: Software Development',
       ],
       description='My awesome package.',
       license='TODO',
       # Like the CMakeLists add_executable macro, you can add your python
       # scripts here.
       entry_points={
           'console_scripts': [
               'my_script = my_package.my_script:main'
           ],
       },
   )

C++ 与 Python 混合功能包
^^^^^^^^^^^^^^^^^^^^^^^^

如果功能包同时包含 C++ 和 Python 代码，则不使用 ``setup.py`` 和 ``setup.cfg`` 文件，而应使用 :doc:`ament_cmake_python <./Ament-CMake-Python-Documentation>`。
