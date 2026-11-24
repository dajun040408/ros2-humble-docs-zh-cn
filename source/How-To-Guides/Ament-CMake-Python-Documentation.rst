.. redirect-from::

  Guides/Ament-CMake-Python-Documentation

ament_cmake_python 用户文档
===========================

``ament_cmake_python`` 是一个软件包，为包含 Python 代码、且使用 ``ament_cmake`` 构建类型的功能包提供 CMake 函数。更多信息请参阅 :doc:`ament_cmake 用户文档 <Ament-CMake-Documentation>`。

.. note::

   大多数情况下，纯 Python 功能包应使用 ``ament_python`` 构建类型。创建 ``ament_python`` 功能包，请参阅 :doc:`创建你的第一个 ROS 2 功能包 <../Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>`。只有在无法使用该方式时才应使用 ``ament_cmake_python``，例如需要混合编译 C/C++ 和 Python 代码的情况。

.. contents:: 目录
   :depth: 2
   :local:

基础知识
--------

基本项目结构
^^^^^^^^^^^^

一个名为 ``my_project``、使用 ``ament_cmake`` 构建类型和 ``ament_cmake_python`` 的功能包，其基本结构如下：

.. code-block::

   .
   └── my_project
       ├── CMakeLists.txt
       ├── package.xml
       └── my_project
           ├── __init__.py
           └── my_script.py

``__init__.py`` 文件可以为空，但必须存在，以便 Python 将包含该文件的目录识别为一个包。相关说明请参阅 `Python 包文档 <https://docs.python.org/3/tutorial/modules.html#packages>`_。``CMakeLists.txt`` 同级目录中也可以包含 ``src`` 或 ``include`` 目录，用于存放 C/C++ 代码。

使用 ament_cmake_python
^^^^^^^^^^^^^^^^^^^^^^^^

功能包必须在 `package.xml` 中声明对 ``ament_cmake_python`` 的构建依赖：

.. code-block:: xml

   <buildtool_depend>ament_cmake_python</buildtool_depend>

``CMakeLists.txt`` 中应包含：

.. code-block:: cmake

   find_package(ament_cmake_python REQUIRED)
   # ...
   ament_python_install_package(${PROJECT_NAME})

``ament_python_install_package()`` 的参数是与 ``CMakeLists.txt`` 同级、包含 Python 文件的目录名称。本例中为 ``my_project``，也就是 ``${PROJECT_NAME}``。

.. warning::

   在同一个 CMake 项目中同时调用 ``rosidl_generate_interfaces`` 和 ``ament_python_install_package`` 无法正常工作。更多信息请参阅 `GitHub issue <https://github.com/ros2/rosidl_python/issues/141>`_。最佳实践是将消息生成部分拆分到单独的功能包中。

随后，正确依赖 ``my_project`` 的另一个 Python 功能包，就可以像使用普通 Python 模块一样使用它：

.. code-block:: python

   from my_project.my_script import my_function

假设 ``my_script.py`` 中定义了 ``my_function()`` 函数。

使用 ament_cmake_pytest
^^^^^^^^^^^^^^^^^^^^^^^

``ament_cmake_pytest`` 软件包用于让 CMake 能够发现测试。功能包必须在 `package.xml` 中声明对 ``ament_cmake_pytest`` 的测试依赖：

.. code-block:: xml

   <test_depend>ament_cmake_pytest</test_depend>

假设功能包结构如下，测试文件位于 ``tests`` 目录中：

.. code-block::

   .
   ├── CMakeLists.txt
   ├── my_project
   │   └── my_script.py
   ├── package.xml
   └── tests
       ├── test_a.py
       └── test_b.py

``CMakeLists.txt`` 中应包含：

.. code-block:: cmake

   if(BUILD_TESTING)
     find_package(ament_cmake_pytest REQUIRED)
     set(_pytest_tests
       tests/test_a.py
       tests/test_b.py
       # 在此添加其他测试文件
     )
     foreach(_test_path ${_pytest_tests})
       get_filename_component(_test_name ${_test_path} NAME_WE)
       ament_add_pytest_test(${_test_name} ${_test_path}
         APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
         TIMEOUT 60
         WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
       )
     endforeach()
   endif()

与支持自动发现测试的 ``ament_python`` 用法相比，``ament_cmake_pytest`` 必须为每个测试文件显式提供路径。可以根据需要缩短超时时间。

现在，你可以使用 :doc:`标准 colcon 测试命令 <../Tutorials/Intermediate/Testing/CLI>` 调用测试。
