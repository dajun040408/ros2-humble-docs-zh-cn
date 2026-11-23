.. redirect-from::

   Migration-Guide
   Contributing/Migration-Guide
   The-ROS2-Project/Contributing/Migration-Guide

C++ 功能包迁移参考
==================

.. contents:: 目录
   :depth: 2
   :local:

本页面介绍如何将 C++ 功能包中的部分内容从 ROS 1 迁移到 ROS 2。如果这是你第一次迁移 C++ 功能包，请先阅读 :doc:`C++ 功能包迁移示例 <Migrating-CPP-Package-Example>`，然后在迁移自己的功能包时将本页作为参考。

构建工具
--------

ROS 2 使用命令行工具 `colcon` 构建和安装一组功能包，而不是使用 `catkin_make`、`catkin_make_isolated` 或 `catkin build`。入门请参阅 :doc:`colcon 初学者教程 <../../Tutorials/Beginner-Client-Libraries/Colcon-Tutorial>`。

更新 CMakeLists.txt，使用 ament_cmake
------------------------------------

ROS 2 C++ 功能包使用 `CMake`，并通过 `ament_cmake` 提供便捷函数。按照以下步骤，将 `catkin` 替换为 `ament_cmake`。

要求使用较新版本的 CMake
^^^^^^^^^^^^^^^^^^^^^^^^

ROS 2 依赖的 CMake 版本比 ROS 1 更新。请在 `REP 2000 <https://reps.openrobotics.org/rep-2000/>`_ 中查找目标 ROS 发行版要求的最低版本，并在 `CMakeLists.txt` 顶部设置。例如，ROS Humble 建议的最低版本为 3.14.4：

.. code-block:: cmake

   cmake_minimum_required(VERSION 3.14.4)

将构建类型设置为 ament_cmake
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

从 `package.xml` 中删除对 `catkin` 的依赖：

.. code-block:: xml

   <!-- 删除 -->
   <buildtool_depend>catkin</buildtool_depend>

添加 `ament_cmake_ros` 依赖，参见`示例 <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/package.xml#L25>`_：

.. code-block:: xml

   <buildtool_depend>ament_cmake_ros</buildtool_depend>

如果 `package.xml` 中还没有 `<export>` 部分，则添加该部分，并将 `<build_type>` 设置为 `ament_cmake`，参见`示例 <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/package.xml#L43-L45>`_：

.. code-block:: xml

   <export>
      <build_type>ament_cmake</build_type>
   </export>

添加 ament_package() 调用
^^^^^^^^^^^^^^^^^^^^^^^^^

在 `CMakeLists.txt` 文件末尾添加 `ament_package()`，参见`示例 <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L127>`_：

.. code-block:: cmake

   ament_package()

更新 find_package() 调用
^^^^^^^^^^^^^^^^^^^^^^^^

将 `find_package(catkin COMPONENTS ...)` 替换为针对每个依赖项单独调用 `find_package()`，参见`示例 <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L14-L18>`_。

例如，将：

.. code-block:: cmake

   find_package(catkin REQUIRED COMPONENTS foo bar std_msgs)
   find_package(baz REQUIRED)

改为：

.. code-block:: cmake

   find_package(ament_cmake_ros REQUIRED)
   find_package(foo REQUIRED)
   find_package(bar REQUIRED)
   find_package(std_msgs REQUIRED)
   find_package(baz REQUIRED)

使用现代 CMake target
^^^^^^^^^^^^^^^^^^^^^

优先使用针对单个 target 的 CMake 函数，以便功能包能够导出现代 CMake target。

如果 `CMakeLists.txt` 中使用了 `include_directories()`，请删除这些调用：

.. code-block:: cmake

   # 删除类似这样的调用
   include_directories(include ${catkin_INCLUDE_DIRS})

为功能包中的每个库添加 `target_include_directories()` 调用，参见`示例 <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L24-L26>`_：

.. code-block:: cmake

   target_include_directories(my_library PUBLIC
      "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
      "$<INSTALL_INTERFACE:include/${PROJECT_NAME}>")

将所有 `target_link_libraries()` 调用改为使用现代 CMake target。

例如，ROS 1 功能包可能使用旧式标准 CMake 变量：

.. code-block:: cmake

   target_link_libraries(my_library ${catkin_LIBRARIES} ${baz_LIBRARIES})

应改为使用具体的现代 CMake target。对于 `std_msgs` 这样的消息功能包，请使用 `${package_name_TARGETS}`：

.. code-block:: cmake

   target_link_libraries(my_library PUBLIC foo::foo bar::bar ${std_msgs_TARGETS} baz::baz)

根据依赖项的使用方式选择 `PUBLIC` 或 `PRIVATE`：

* 如果下游使用者需要该依赖项，例如库的公共 API 使用了它，则使用 `PUBLIC`。
* 如果该依赖项只在库内部使用，则使用 `PRIVATE`。

使用多个 ament_cmake 调用替换 catkin_package()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

假设 `CMakeLists.txt` 中有如下 `catkin_package` 调用：

.. code-block:: cmake

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

替换 catkin_package(INCLUDE_DIRS ...)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

如果已经使用现代 CMake target 和 `target_include_directories()`，则无需进一步操作。下游使用者依赖这些现代 CMake target 时，就会获得相应的 include 目录。

替换 catkin_package(LIBRARIES ...)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

使用 `ament_export_targets()` 和 `install(TARGETS ... EXPORT ...)` 替换 `LIBRARIES` 参数。

安装 `my_library` target 时使用 `EXPORT` 关键字，参见`示例 <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L37-L41>`_：

.. code-block:: cmake

   install(TARGETS my_library EXPORT export_my_package
      ARCHIVE DESTINATION lib
      LIBRARY DESTINATION lib
      RUNTIME DESTINATION bin
   )

对于库 target，这是一个合适的默认配置。如果功能包使用了不同的 `CATKIN_*_DESTINATION` 变量，请按以下方式转换：

.. list-table::
   :header-rows: 1

   * - catkin
     - ament_cmake
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

添加 `ament_export_targets()` 调用，并使用与 `EXPORT` 关键字相同的名称，参见`示例 <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/CMakeLists.txt#L124-L125>`_：

.. code-block:: cmake

   ament_export_targets(export_my_package)

替换 catkin_package(CATKIN_DEPENDS ... DEPENDS ...)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能包的使用者必须对功能包公共 API 使用的依赖项调用 `find_package()`。ROS 1 中通过 `CATKIN_DEPENDS` 和 `DEPENDS` 参数为下游使用者完成此操作。ROS 2 中使用 `ament_export_dependencies`，参见`实现 <https://github.com/ament/ament_cmake/blob/{REPOS_FILE_BRANCH}/ament_cmake_export_dependencies/cmake/ament_export_dependencies.cmake>`_：

.. code-block:: cmake

   ament_export_dependencies(
      foo
      bar
      std_msgs
      baz
   )

生成消息
^^^^^^^^

如果功能包同时包含 C++ 代码和 ROS 消息、服务或动作定义，可以考虑拆分为两个功能包：

* 只包含 ROS 消息、服务和/或动作定义的功能包。
* 包含 C++ 代码的功能包。

在包含 ROS 消息的功能包 `package.xml` 中添加以下依赖项：

1. 添加对 `rosidl_default_generators` 的 `<buildtool_depend>`，参见`示例 <https://github.com/ros2/common_interfaces/blob/d685509e9cb9f80bd320a347f2db954a73397ae7/std_msgs/package.xml#L19>`_：

   .. code-block:: xml

      <buildtool_depend>rosidl_default_generators</buildtool_depend>

2. 添加对 `rosidl_default_runtime` 的 `<exec_depend>`，参见`示例 <https://github.com/ros2/common_interfaces/blob/d685509e9cb9f80bd320a347f2db954a73397ae7/std_msgs/package.xml#L22>`_：

   .. code-block:: xml

      <exec_depend>rosidl_default_runtime</exec_depend>

3. 添加 `<member_of_group>` 标签，组名为 `rosidl_interface_packages`，参见`示例 <https://github.com/ros2/common_interfaces/blob/d685509e9cb9f80bd320a347f2db954a73397ae7/std_msgs/package.xml#L26>`_：

   .. code-block:: xml

      <member_of_group>rosidl_interface_packages</member_of_group>

在 `CMakeLists.txt` 中，将 `add_message_files`、`add_service_files` 和 `generate_messages` 替换为 `rosidl_generate_interfaces`。第一个参数必须是 `${PROJECT_NAME}`，原因参见`相关问题 <https://github.com/ros2/rosidl_typesupport/issues/120>`_。

例如，ROS 1 功能包可能如下：

.. code-block:: cmake

   add_message_files(DIRECTORY msg FILES FooBar.msg Baz.msg)
   add_service_files(DIRECTORY srv FILES Ping.srv)
   add_action_files(DIRECTORY action FILES DoPong.action)
   generate_messages(
      DEPENDENCIES actionlib_msgs std_msgs geometry_msgs
   )

改为：

.. code-block:: cmake

   rosidl_generate_interfaces(${PROJECT_NAME}
     "msg/FooBar.msg"
     "msg/Baz.msg"
     "srv/Ping.srv"
     "action/DoPong.action"
     DEPENDENCIES actionlib_msgs std_msgs geometry_msgs
   )

删除对 devel space 的引用
^^^^^^^^^^^^^^^^^^^^^^^^^^

删除所有对 *devel space* 的引用，例如 `CATKIN_DEVEL_PREFIX`。ROS 2 中没有与 *devel space* 对应的概念。

单元测试
^^^^^^^^

如果功能包使用 `gtest`，则：

* 将 `CATKIN_ENABLE_TESTING` 替换为 `BUILD_TESTING`。
* 将 `catkin_add_gtest` 替换为 `ament_add_gtest`。
* 使用 `ament_cmake_gtest` 的 `find_package()`，而不是 `GTest`。

例如，ROS 1 功能包可能这样添加测试：

.. code-block:: cmake

   if (CATKIN_ENABLE_TESTING)
     find_package(GTest REQUIRED)
     include_directories(${GTEST_INCLUDE_DIRS})
     catkin_add_gtest(my_test src/test/some_test.cpp)
     target_link_libraries(my_test ${GTEST_LIBRARIES})
   endif()

改为：

.. code-block:: cmake

   if (BUILD_TESTING)
     find_package(ament_cmake_gtest REQUIRED)
     ament_add_gtest(my_test src/test/test_something.cpp)
     target_link_libraries(my_test
       # ...
     )
   endif()

在 `package.xml` 中添加 `<test_depend>ament_cmake_gtest</test_depend>`，参见`示例 <https://github.com/ros2/geometry2/blob/d85102217f692746abea8546c8e41f0abc95c8b8/tf2/package.xml#L35>`_：

.. code-block:: xml

   <test_depend>ament_cmake_gtest</test_depend>

代码检查工具
^^^^^^^^^^^^

ROS 2 的代码 :doc:`风格指南 <../../The-ROS2-Project/Contributing/Developer-Guide>` 与 ROS 1 不同。

如果选择遵循 ROS 2 风格指南，可以在 `if(BUILD_TESTING)` 块中添加以下内容，启用自动 linter 测试：

.. code-block:: cmake

   if(BUILD_TESTING)
      find_package(ament_lint_auto REQUIRED)
      ament_lint_auto_find_test_dependencies()
      # ...
   endif()

在 `package.xml` 中添加以下依赖项：

.. code-block:: xml

   <test_depend>ament_lint_auto</test_depend>
   <test_depend>ament_lint_common</test_depend>

更新源代码
----------

消息、服务和动作
^^^^^^^^^^^^^^^^

ROS 2 消息、服务和动作的命名空间会在功能包名称后增加子命名空间，分别为 `msg`、`srv` 或 `action`。

因此，头文件包含方式如下：

`#include <my_interfaces/msg/my_message.hpp>`

对应的 C++ 类型为 `my_interfaces::msg::MyMessage`。

消息结构体中提供了共享指针类型别名，例如 `my_interfaces::msg::MyMessage::SharedPtr` 和 `my_interfaces::msg::MyMessage::ConstSharedPtr`。

更多详情请参阅`生成的 C++ 接口设计文章 <https://design.ros2.org/articles/generated_interfaces_cpp.html>`_。

迁移时，头文件需要：

* 在功能包名称和消息类型之间插入 `msg` 子目录。
* 将包含文件名从 CamelCase 改为下划线分隔。
* 将 `*.h` 改为 `*.hpp`。

.. code-block:: cpp

   // ROS 1
   // #include <geometry_msgs/PointStamped.h>
   // ROS 2
   #include <geometry_msgs/msg/point_stamped.hpp>

   // geometry_msgs::PointStamped point_stamped;
   geometry_msgs::msg::PointStamped point_stamped;

所有使用消息类型的代码都需要插入 `msg` 命名空间。

使用服务对象
^^^^^^^^^^^^

ROS 2 服务回调没有布尔返回值。发生失败时，不再返回 `false`，而是建议抛出异常。

.. code-block:: cpp

   // ROS 1
   // #include "nav_msgs/GetMap.h"
   // bool service_callback(
   //   nav_msgs::GetMap::Request & request,
   //   nav_msgs::GetMap::Response & response)

   // ROS 2
   #include "nav_msgs/srv/get_map.hpp"

   void service_callback(
     const std::shared_ptr<nav_msgs::srv::GetMap::Request> request,
     std::shared_ptr<nav_msgs::srv::GetMap::Response> response)
   {
     // ...
   }

使用 ros::Time
^^^^^^^^^^^^^^

对于 `ros::Time`：

* 将所有 `ros::Time` 替换为 `rclcpp::Time`。
* 如果消息或代码使用 `std_msgs::Time`：
  * 将所有 `std_msgs::Time` 替换为 `builtin_interfaces::msg::Time`。
  * 将 `#include "std_msgs/time.h"` 替换为 `#include "builtin_interfaces/msg/time.hpp"`。
  * 将 `std_msgs::Time` 字段 `nsec` 替换为 `builtin_interfaces::msg::Time` 字段 `nanosec`。

使用 ros::Rate
^^^^^^^^^^^^^^

ROS 2 提供了等效的 `rclcpp::Rate` 对象，基本可以直接替换 `ros::Rate`。

Boost
^^^^^

Boost 之前提供的许多功能已经集成到 C++ 标准库中。因此，建议利用新的标准库功能，并尽可能避免依赖 Boost。

共享指针
~~~~~~~~

将共享指针从 Boost 切换到标准 C++，需要替换：

* `#include <boost/shared_ptr.hpp>` → `#include <memory>`
* `boost::shared_ptr` → `std::shared_ptr`

也可能存在 `weak_ptr` 等变体，也需要相应转换。

此外，建议使用 `using` 而不是 `typedef`。`using` 在模板逻辑中具有更好的适用性。详情请参阅`相关讨论 <https://stackoverflow.com/questions/10747810/what-is-the-difference-between-typedef-and-using-in-c11>`_。

线程与互斥锁
~~~~~~~~~~~~

ROS 代码中另一个常见的 Boost 用法是 `boost::thread` 中的互斥锁。

* 将 `boost::mutex::scoped_lock` 替换为 `std::unique_lock<std::mutex>`。
* 将 `boost::mutex` 替换为 `std::mutex`。
* 将 `#include <boost/thread/mutex.hpp>` 替换为 `#include <mutex>`。

无序映射
~~~~~~~~

替换：

* `#include <boost/unordered_map.hpp>` → `#include <unordered_map>`
* `boost::unordered_map` → `std::unordered_map`

function
~~~~~~~~

替换：

* `#include <boost/function.hpp>` → `#include <functional>`
* `boost::function` → `std::function`
