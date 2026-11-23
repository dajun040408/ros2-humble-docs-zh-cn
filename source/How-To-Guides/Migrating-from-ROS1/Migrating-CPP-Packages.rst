.. redirect-from::

   Migration-Guide
   Contributing/Migration-Guide
   The-ROS2-Project/Contributing/Migration-Guide

C++ 功能包迁移参考
================================

.. contents:: Table of Contents
   :depth: 2
   :local:

本页面介绍如何将 C++ 功能包的各个部分从 ROS 1 迁移到 ROS 2。如果这是你第一次迁移 C++ 功能包，请先阅读 :doc:`C++ 迁移示例 <Migrating-CPP-Package-Example>`。之后可在迁移自己的功能包时将本页作为参考。

构建工具
----------

ROS 2 不再使用 ``catkin_make``、``catkin_make_isolated`` 或 ``catkin build``，而是使用命令行工具 `colcon <https://design.ros2.org/articles/build_tool.html>`__ 来构建和安装一组功能包。请参阅 :doc:`入门教程 <../../Tutorials/Beginner-Client-Libraries/Colcon-Tutorial>`，了解如何开始使用 ``colcon``。

更新 ``CMakeLists.txt`` 以使用 *ament_cmake*
---------------------------------------------------

ROS 2 C++ 功能包使用 `CMake <https://cmake.org/>`__，并使用 `ament_cmake <https://index.ros.org/p/ament_cmake/>`__ 提供的便捷函数。请进行以下修改，以使用 ``ament_cmake`` 替代 ``catkin``。


要求使用较新版本的 CMake
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ROS 2 使用的 CMake 版本高于 ROS 1。请在 `REP 2000 <https://reps.openrobotics.org/rep-2000/>`__ 中查找目标 ROS 发行版要求的 CMake 最低版本，并在 ``CMakeLists.txt`` 顶部指定该版本。例如，`ROS Humble 推荐支持的最低版本为 3.14.4 <https://reps.openrobotics.org/rep-2000/#humble-hawksbill-may-2022-may-2027>`__。

.. code-block::

   cmake_minimum_required(VERSION 3.14.4)

将构建类型设置为 ament_cmake
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

从 ``package.xml`` 中移除对 ``catkin`` 的所有依赖

.. code-block::

   # Remove this!
   <buildtool_depend>catkin</buildtool_depend>

添加对 ``ament_cmake_ros`` 的新依赖 (`example <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/package.xml#L25>`__):

.. code-block:: xml

   <buildtool_depend>ament_cmake_ros</buildtool_depend>

如果 ``package.xml`` 中尚无 ``<export>`` 节，请添加该节，并将 ``<build_type>`` 设置为 ``ament_cmake``。 (`example <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/package.xml#L43-L45>`__)

.. code-block:: xml

   <export>
      <build_type>ament_cmake</build_type>
   </export>

添加 ``ament_package()`` 调用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 ``CMakeLists.txt`` 文件末尾插入 ``ament_package()`` 调用。 (`example <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L127>`__)

.. code-block:: cmake

   # Add this to the bottom of your CMakeLists.txt
   ament_package()

更新 ``find_package()`` 调用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

将 ``find_package(catkin COMPONENTS ...)`` 调用替换为独立的 ``find_package()`` 调用。 (`example <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L14-L18>`_):

For example, change this:

.. code-block::

   find_package(catkin REQUIRED COMPONENTS foo bar std_msgs)
   find_package(baz REQUIRED)

To this:

.. code-block:: cmake

   find_package(ament_cmake_ros REQUIRED)
   find_package(foo REQUIRED)
   find_package(bar REQUIRED)
   find_package(std_msgs REQUIRED)
   find_package(baz REQUIRED)


使用现代 CMake targets
^^^^^^^^^^^^^^^^^^^^^^^^

建议使用面向单个 target 的 CMake 函数，以便功能包能够导出现代 CMake targets。

如果 ``CMakeLists.txt`` 使用了 ``include_directories()``，请删除这些调用。

.. code-block::

   # Delete calls to include_directories like this one!
   include_directories(include ${catkin_INCLUDE_DIRS})

为功能包中的每个库添加 ``target_include_directories()`` 调用。 (`example <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L24-L26>`__).

.. code-block:: cmake

   target_include_directories(my_library PUBLIC
      "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
      "$<INSTALL_INTERFACE:include/${PROJECT_NAME}>")

将所有 ``target_link_libraries()`` 调用修改为使用现代 CMake targets。
例如，如果 ROS 1 功能包使用如下旧式标准 CMake 变量：

.. code-block::

   target_link_libraries(my_library ${catkin_LIBRARIES} ${baz_LIBRARIES})

则应改为使用具体的现代 CMake targets。如果依赖的是 ``std_msgs`` 这样的消息功能包，请使用 ``${package_name_TARGETS}``。

.. code-block:: cmake

   target_link_libraries(my_library PUBLIC foo::foo bar::bar ${std_msgs_TARGETS} baz::baz)

根据库对依赖项的使用方式选择 ``PUBLIC`` 或 ``PRIVATE``。 (`example <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L27-L31>`__).

* 如果下游用户也需要该依赖项，例如你的库的公共 API 使用了它，则使用 ``PUBLIC``。
* 如果该依赖项仅在库内部使用，则使用 ``PRIVATE``。

使用多个 ament_cmake 调用替换 ``catkin_package()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

假设你的 ``CMakeLists.txt`` 中有如下 ``catkin_package`` 调用：

.. code-block::

   catkin_package(
       INCLUDE_DIRS include
       LIBRARIES my_library
       CATKIN_DEPENDS foo bar std_msgs
       DEPENDS baz
   )

   install(TARGETS my_library
      ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
      LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
      RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
   )


替换 ``catkin_package(INCLUDE_DIRS ...)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

如果已经使用现代 CMake targets 和 ``target_include_directories()``，则无需进一步操作。下游用户依赖你的现代 CMake targets 时，会自动获得相应的头文件目录。

替换 ``catkin_package(LIBRARIES ...)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

使用 ``ament_export_targets()`` 和 ``install(TARGETS ... EXPORT ...)`` 替换 ``LIBRARIES`` 参数。

安装 ``my_library`` target 时使用 ``EXPORT`` 关键字。 (`example <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L37-L41>`__).

.. code-block:: cmake

   install(TARGETS my_library EXPORT export_my_package
      ARCHIVE DESTINATION lib
      LIBRARY DESTINATION lib
      RUNTIME DESTINATION bin
   )

以上是库 targets 的推荐默认配置。如果功能包使用了其他 ``CATKIN_*_DESTINATION`` 变量，请按下表转换：

.. list-table::
   :header-rows: 1

   * - **catkin**
     - **ament_cmake**
   * - CATKIN_GLOBAL_BIN_DESTINATION
     - bin
   * - CATKIN_GLOBAL_INCLUDE_DESTINATION
     - include
   * - CATKIN_GLOBAL_LIB_DESTINATION
     - lib
   * - CATKIN_GLOBAL_LIBEXEC_DESTINATION
     - lib
   * - CATKIN_GLOBAL_SHARE_DESTINATION
     - share
   * - CATKIN_PACKAGE_BIN_DESTINATION
     - lib/${PROJECT_NAME}
   * - CATKIN_PACKAGE_INCLUDE_DESTINATION
     - include/${PROJECT_NAME}
   * - CATKIN_PACKAGE_LIB_DESTINATION
     - lib
   * - CATKIN_PACKAGE_SHARE_DESTINATION
     - share/${PROJECT_NAME}

添加 ``ament_export_targets()`` 调用，其参数名称应与 ``EXPORT`` 关键字指定的名称相同。 (`example <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L124-L125>`__).

.. code-block:: cmake

   ament_export_targets(export_my_package)


替换 ``catkin_package(CATKIN_DEPENDS .. DEPENDS ..)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

使用你的功能包公共 API 的依赖项，必须由功能包的使用者通过 ``find_package()`` 查找。在 ROS 1 中，这通过 ``CATKIN_DEPENDS`` 和 ``DEPENDS`` 参数为下游用户完成。在 ROS 2 中，请使用 `ament_export_dependencies <https://github.com/ament/ament_cmake/blob/{REPOS_FILE_BRANCH}/ament_cmake_export_dependencies/cmake/ament_export_dependencies.cmake>`__ 实现。

.. code-block:: cmake

   ament_export_dependencies(
      foo
      bar
      std_msgs
      baz
   )

生成消息
^^^^^^^^^^^^^^^^^

如果功能包同时包含 C++ 代码和 ROS 消息、服务或动作定义，请考虑将其拆分为两个功能包：

* 一个只包含 ROS 消息、服务和/或动作定义的功能包。
* 一个包含 C++ 代码的功能包。

在包含 ROS 消息的功能包的 ``package.xml`` 中添加以下依赖项：

1. Add a ``<buildtool_depend>`` on ``rosidl_default_generators`` (`example <https://github.com/ros2/common_interfaces/blob/d685509e9cb9f80bd320a347f2db954a73397ae7/std_msgs/package.xml#L19>`__)

   .. code-block:: xml

      <buildtool_depend>rosidl_default_generators</buildtool_depend>

2. Add an ``<exec_depend>`` on ``rosidl_default_runtime`` (`example <https://github.com/ros2/common_interfaces/blob/d685509e9cb9f80bd320a347f2db954a73397ae7/std_msgs/package.xml#L22>`__)

   .. code-block:: xml

      <exec_depend>rosidl_default_runtime</exec_depend>

3. Add a ``<member_of_group>`` tag with the group name ``rosidl_interface_packages`` (`example <https://github.com/ros2/common_interfaces/blob/d685509e9cb9f80bd320a347f2db954a73397ae7/std_msgs/package.xml#L26>`__)

   .. code-block:: xml

      <member_of_group>rosidl_interface_packages</member_of_group>

在 ``CMakeLists.txt`` 中，将 ``add_message_files``、``add_service_files`` 和 ``generate_messages`` 调用替换为 `rosidl_generate_interfaces <https://github.com/ros2/rosidl/blob/{REPOS_FILE_BRANCH}/rosidl_cmake/cmake/rosidl_generate_interfaces.cmake>`__。由于 `该问题 <https://github.com/ros2/rosidl_typesupport/issues/120>`__，第一个参数必须是 ``${PROJECT_NAME}``。

例如，ROS 1 功能包中的代码如下：

.. code-block::

   add_message_files(DIRECTORY msg FILES FooBar.msg Baz.msg)
   add_service_files(DIRECTORY srv FILES Ping.srv)

   add_action_files(DIRECTORY action FILES DoPong.action)
   generate_messages(
      DEPENDENCIES actionlib_msgs std_msgs geometry_msgs
   )

则修改为： (`example <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2_msgs/CMakeLists.txt#L18-L25>`__)

.. code-block:: cmake

       rosidl_generate_interfaces(${PROJECT_NAME}
         "msg/FooBar.msg"
         "msg/Baz.msg"
         "srv/Ping.srv"
         "action/DoPong.action"
         DEPENDENCIES actionlib_msgs std_msgs geometry_msgs
       )

移除对 devel space 的引用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

删除所有对 *devel space* 的引用，例如 ``CATKIN_DEVEL_PREFIX``。ROS 2 中没有与 *devel space* 对应的概念。


单元测试
^^^^^^^^^^

如果功能包使用 `gtest <https://github.com/google/googletest>`__，则：

* 将 ``CATKIN_ENABLE_TESTING`` 替换为 ``BUILD_TESTING``。
* 将 ``catkin_add_gtest`` 替换为 ``ament_add_gtest``。
* 添加 ``ament_cmake_gtest`` 的 ``find_package()`` 调用，替代 ``GTest``。

例如，ROS 1 功能包通过以下方式添加测试：

.. code-block::

      if (CATKIN_ENABLE_TESTING)
        find_package(GTest REQUIRED)
        include_directories(${GTEST_INCLUDE_DIRS})
        catkin_add_gtest(my_test src/test/some_test.cpp)
        target_link_libraries(my_test
          # ...
          ${GTEST_LIBRARIES})
      endif()

则修改为：:

.. code-block:: CMake

      if (BUILD_TESTING)
        find_package(ament_cmake_gtest REQUIRED)
        ament_add_gtest(my_test src/test/test_something.cpp)
        target_link_libraries(my_test
          #...
         )
      endif()

Add ``<test_depend>ament_cmake_gtest</test_depend>`` to your ``package.xml`` (`example <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/package.xml#L35>`__).

.. code-block:: xml

   <test_depend>ament_cmake_gtest</test_depend>

Linters
^^^^^^^

The ROS 2 code :doc:`style guide <../../The-ROS2-Project/Contributing/Developer-Guide>` differs from ROS 1.

If you choose to follow the ROS 2 style guide, then turn on automatic linter tests by adding these lines in a ``if(BUILD_TESTING)`` block:

.. code-block:: cmake

   if(BUILD_TESTING)
      find_package(ament_lint_auto REQUIRED)
      ament_lint_auto_find_test_dependencies()
      # ...
   endif()

Add the following dependencies to your ``package.xml``:

.. code-block:: xml

   <test_depend>ament_lint_auto</test_depend>
   <test_depend>ament_lint_common</test_depend>

Update source code
------------------

Messages, services, and actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The namespace of ROS 2 messages, services, and actions use a subnamespace (``msg``, ``srv``, or ``action``, respectively) after the package name.
Therefore an include looks like: ``#include <my_interfaces/msg/my_message.hpp>``.
The C++ type is then named: ``my_interfaces::msg::MyMessage``.

Shared pointer types are provided as typedefs within the message structs: ``my_interfaces::msg::MyMessage::SharedPtr`` as well as ``my_interfaces::msg::MyMessage::ConstSharedPtr``.

For more details please see the article about the `generated C++ interfaces <https://design.ros2.org/articles/generated_interfaces_cpp.html>`__.

The migration requires includes to change by:


* inserting the subfolder ``msg`` between the package name and message datatype
* changing the included filename from CamelCase to underscore separation
* changing from ``*.h`` to ``*.hpp``

.. code-block:: cpp

   // ROS 1 style is in comments, ROS 2 follows, uncommented.
   // # include <geometry_msgs/PointStamped.h>
   #include <geometry_msgs/msg/point_stamped.hpp>

   // geometry_msgs::PointStamped point_stamped;
   geometry_msgs::msg::PointStamped point_stamped;

The migration requires code to insert the ``msg`` namespace into all instances.

Use of service objects
^^^^^^^^^^^^^^^^^^^^^^

Service callbacks in ROS 2 do not have boolean return values.
Instead of returning false on failures, throwing exceptions is recommended.

.. code-block:: cpp

   // ROS 1 style is in comments, ROS 2 follows, uncommented.
   // #include "nav_msgs/GetMap.h"
   #include "nav_msgs/srv/get_map.hpp"

   // bool service_callback(
   //   nav_msgs::GetMap::Request & request,
   //   nav_msgs::GetMap::Response & response)
   void service_callback(
     const std::shared_ptr<nav_msgs::srv::GetMap::Request> request,
     std::shared_ptr<nav_msgs::srv::GetMap::Response> response)
   {
     // ...
     // return true;  // or false for failure
   }

Usages of ros::Time
^^^^^^^^^^^^^^^^^^^

For usages of ``ros::Time``:

* Replace all instances of ``ros::Time`` with ``rclcpp::Time``

* If your messages or code makes use of std_msgs::Time:

  * Convert all instances of std_msgs::Time to builtin_interfaces::msg::Time

  * Convert all ``#include "std_msgs/time.h`` to ``#include "builtin_interfaces/msg/time.hpp"``

  * Convert all instances using the std_msgs::Time field ``nsec`` to the builtin_interfaces::msg::Time field ``nanosec``

Usages of ros::Rate
^^^^^^^^^^^^^^^^^^^

There is an equivalent type ``rclcpp::Rate`` object which is basically a drop in replacement for ``ros::Rate``.


Boost
^^^^^

Much of the functionality previously provided by Boost has been integrated into the C++ standard library.
As such we would like to take advantage of the new core features and avoid the dependency on boost where possible.

Shared Pointers
~~~~~~~~~~~~~~~

To switch shared pointers from boost to standard C++ replace instances of:


* ``#include <boost/shared_ptr.hpp>`` with ``#include <memory>``
* ``boost::shared_ptr`` with ``std::shared_ptr``

There may also be variants such as ``weak_ptr`` which you want to convert as well.

Also it is recommended practice to use ``using`` instead of ``typedef``.
``using`` has the ability to work better in templated logic.
For details `see here <https://stackoverflow.com/questions/10747810/what-is-the-difference-between-typedef-and-using-in-c11>`__

Thread/Mutexes
~~~~~~~~~~~~~~

Another common part of boost used in ROS codebases are mutexes in ``boost::thread``.


* Replace ``boost::mutex::scoped_lock`` with ``std::unique_lock<std::mutex>``
* Replace ``boost::mutex`` with ``std::mutex``
* Replace ``#include <boost/thread/mutex.hpp>`` with ``#include <mutex>``

Unordered Map
~~~~~~~~~~~~~

Replace:


* ``#include <boost/unordered_map.hpp>`` with ``#include <unordered_map>``
* ``boost::unordered_map`` with ``std::unordered_map``

function
~~~~~~~~

Replace:


* ``#include <boost/function.hpp>``  with ``#include <functional>``
* ``boost::function`` with ``std::function``
