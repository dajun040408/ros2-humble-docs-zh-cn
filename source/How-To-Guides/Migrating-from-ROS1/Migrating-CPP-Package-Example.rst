C++ 功能包迁移示例
===============================

.. contents:: 目录
   :depth: 2
   :local:

本示例演示如何将一个示例 C++ 功能包从 ROS 1 迁移到 ROS 2。

前置条件
-------------

你需要一个可正常工作的 ROS 2 安装环境，例如 :doc:`ROS {DISTRO} <../../Installation>`。

ROS 1 代码
--------------

假设你有一个名为 ``talker`` 的 ROS 1 功能包，其中包含一个使用 ``roscpp`` 的节点，该节点也名为 ``talker``。
该功能包位于 ``~/ros1_talker`` 目录下的 catkin 工作空间中。

ROS 1 工作空间的目录结构如下：

.. code-block:: console

   $ cd ~/ros1_talker
   $ find .
   .
   ./src
   ./src/talker
   ./src/talker/package.xml
   ./src/talker/CMakeLists.txt
   ./src/talker/talker.cpp

这些文件的内容如下：

``src/talker/package.xml``:

.. code-block:: xml

   <?xml version="1.0"?>
   <?xml-model href="http://download.ros.org/schema/package_format2.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
   <package format="2">
     <name>talker</name>
     <version>0.0.0</version>
     <description>talker</description>
     <maintainer email="gerkey@example.com">Brian Gerkey</maintainer>
     <license>Apache-2.0</license>
     <buildtool_depend>catkin</buildtool_depend>
     <depend>roscpp</depend>
     <depend>std_msgs</depend>
   </package>

``src/talker/CMakeLists.txt``:

.. code-block:: cmake

   cmake_minimum_required(VERSION 2.8.3)
   project(talker)
   find_package(catkin REQUIRED COMPONENTS roscpp std_msgs)
   catkin_package()
   include_directories(${catkin_INCLUDE_DIRS})
   add_executable(talker talker.cpp)
   target_link_libraries(talker ${catkin_LIBRARIES})
   install(TARGETS talker
     RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

``src/talker/talker.cpp``:

.. code-block:: cpp

   #include <sstream>
   #include "ros/ros.h"
   #include "std_msgs/String.h"
   int main(int argc, char **argv)
   {
     ros::init(argc, argv, "talker");
     ros::NodeHandle n;
     ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
     ros::Rate loop_rate(10);
     int count = 0;
     std_msgs::String msg;
     while (ros::ok())
     {
       std::stringstream ss;
       ss << "hello world " << count++;
       msg.data = ss.str();
       ROS_INFO("%s", msg.data.c_str());
       chatter_pub.publish(msg);
       ros::spinOnce();
       loop_rate.sleep();
     }
     return 0;
   }

迁移到 ROS 2
------------------

首先，创建一个新的工作空间：

.. code-block:: console

   $ mkdir ~/ros2_talker
   $ cd ~/ros2_talker

将 ROS 1 功能包的源代码目录复制到新工作空间中，以便进行修改：

.. code-block:: console

   $ mkdir src
   $ cp -a ~/ros1_talker/src/talker src

现在修改节点中的 C++ 代码。
ROS 2 的 C++ 库名为 ``rclcpp``，它提供的 API 与 ``roscpp`` 不同。
这两个库的概念非常相似，因此迁移时所需的修改相对直接。

包含头文件
~~~~~~~~~~~~~~~~

原先通过 ``ros/ros.h`` 访问 ``roscpp`` 库 API；现在需要包含 ``rclcpp/rclcpp.hpp``，以访问 ``rclcpp`` 库 API：

.. code-block:: cpp

   //#include "ros/ros.h"
   #include "rclcpp/rclcpp.hpp"

要使用 ``std_msgs/String`` 消息定义，原先包含 ``std_msgs/String.h``；现在需要包含 ``std_msgs/msg/string.hpp``：

.. code-block:: cpp

   //#include "std_msgs/String.h"
   #include "std_msgs/msg/string.hpp"

修改 C++ 库调用
~~~~~~~~~~~~~~~~~~~~~~~~~~

ROS 2 不再将节点名称传递给库初始化函数，而是先完成初始化，再在创建节点对象时传入节点名称：

.. code-block:: cpp

   //  ros::init(argc, argv, "talker");
   //  ros::NodeHandle n;
       rclcpp::init(argc, argv);
       auto node = rclcpp::Node::make_shared("talker");

发布者和频率对象的创建方式非常相似，只是命名空间和方法名称有所变化。

.. code-block:: cpp

   //  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
   //  ros::Rate loop_rate(10);
     auto chatter_pub = node->create_publisher<std_msgs::msg::String>("chatter",
       1000);
     rclcpp::Rate loop_rate(10);

为了进一步控制消息传递方式，可以传入服务质量（``QoS``）配置文件。默认配置文件为 ``rmw_qos_profile_default``。更多详情请参阅 `设计文档 <https://design.ros2.org/articles/qos.html>`__ 和 :doc:`概念概述 <../../Concepts/Intermediate/About-Quality-of-Service-Settings>`。

创建待发布消息时，消息类型的命名空间也有所不同：

.. code-block:: cpp

   //  std_msgs::String msg;
     std_msgs::msg::String msg;

原先调用 ``ros::ok()`` 的位置，现在改为调用 ``rclcpp::ok()``：

.. code-block:: cpp

   //  while (ros::ok())
     while (rclcpp::ok())

在发布循环中，仍然像以前一样访问 ``data`` 字段：

.. code-block:: cpp

       msg.data = ss.str();

输出控制台日志时，不再使用 ``ROS_INFO()``，而是使用 ``RCLCPP_INFO()`` 及其相关宏。关键区别在于，``RCLCPP_INFO()`` 的第一个参数是 Logger 对象。

.. code-block:: cpp

   //    ROS_INFO("%s", msg.data.c_str());
       RCLCPP_INFO(node->get_logger(), "%s\n", msg.data.c_str());

将发布调用中的 ``.`` 运算符改为 ``->`` 运算符。

.. code-block:: cpp

   //    chatter_pub.publish(msg);
       chatter_pub->publish(msg);

Spin 操作（即让通信系统处理所有待处理的收发消息，直到没有更多工作）也有所不同：现在调用时需要传入节点和超时时间作为参数：

.. code-block:: cpp

   //    ros::spinOnce();
       rclcpp::spin_all(node, 0s);

使用 rate 对象休眠的方式保持不变。

综合以上修改，新的 ``talker.cpp`` 如下所示：

.. code-block:: cpp

   #include <chrono>
   #include <sstream>
   // #include "ros/ros.h"
   #include "rclcpp/rclcpp.hpp"
   // #include "std_msgs/String.h"
   #include "std_msgs/msg/string.hpp"

   using namespace std::chrono_literals;

   int main(int argc, char **argv)
   {
   //  ros::init(argc, argv, "talker");
   //  ros::NodeHandle n;
     rclcpp::init(argc, argv);
     auto node = rclcpp::Node::make_shared("talker");
   //  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
   //  ros::Rate loop_rate(10);
     auto chatter_pub = node->create_publisher<std_msgs::msg::String>("chatter", 1000);
     rclcpp::Rate loop_rate(10);
     int count = 0;
   //  std_msgs::String msg;
     std_msgs::msg::String msg;
   //  while (ros::ok())
     while (rclcpp::ok())
     {
       std::stringstream ss;
       ss << "hello world " << count++;
       msg.data = ss.str();
   //    ROS_INFO("%s", msg.data.c_str());
       RCLCPP_INFO(node->get_logger(), "%s\n", msg.data.c_str());
   //    chatter_pub.publish(msg);
       chatter_pub->publish(msg);
   //    ros::spinOnce();
       rclcpp::spin_all(node, 0s);
       loop_rate.sleep();
     }
     return 0;
   }

修改 ``package.xml``
~~~~~~~~~~~~~~~~~~~~~~~~~~

ROS 2 功能包使用 ``ament_cmake_ros`` 提供的 CMake 函数和宏，而不是 ``catkin``。删除对 ``catkin`` 的依赖：

.. code-block::

   <!-- delete this -->
   <buildtool_depend>catkin</buildtool_depend>`

添加对 ``ament_cmake_ros`` 的新依赖：

.. code-block:: xml

     <buildtool_depend>ament_cmake_ros</buildtool_depend>

ROS 2 C++ 库使用 `rclcpp <https://index.ros.org/p/rclcpp/#{DISTRO}>`__，而不是 `roscpp <https://index.ros.org/p/roscpp/#noetic>`__。

删除对 ``roscpp`` 的依赖：

.. code-block::

   <!-- delete this -->
   <depend>roscpp</depend>

添加对 ``rclcpp`` 的依赖：

.. code-block:: xml

     <depend>rclcpp</depend>


添加 ``<export>`` 节，告知 colcon 该功能包是 ``ament_cmake`` 类型，而不是 ``catkin`` 类型。

.. code-block:: xml

     <export>
       <build_type>ament_cmake</build_type>
     </export>

修改后的 ``package.xml`` 如下所示：

.. code-block:: xml

   <?xml version="1.0"?>
   <?xml-model href="http://download.ros.org/schema/package_format2.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
   <package format="2">
     <name>talker</name>
     <version>0.0.0</version>
     <description>talker</description>
     <maintainer email="gerkey@example.com">Brian Gerkey</maintainer>
     <license>Apache-2.0</license>
     <buildtool_depend>ament_cmake</buildtool_depend>
     <depend>rclcpp</depend>
     <depend>std_msgs</depend>
     <export>
       <build_type>ament_cmake</build_type>
     </export>
   </package>


修改 CMake 代码
~~~~~~~~~~~~~~~~~~~~~~~

要求使用较新版本的 CMake，以确保 ``ament_cmake`` 函数正常工作。

.. code-block:: cmake

   cmake_minimum_required(VERSION 3.14.4)

使用与你目标 ROS 发行版匹配的较新 C++ 标准，具体版本可参阅 `REP 2000 <https://reps.openrobotics.org/rep-2000/>`__。如果使用 C++17，请在 ``project(talker)`` 调用之后添加以下代码设置标准。同时建议增加编译器检查。

.. code-block:: cmake

   if(NOT CMAKE_CXX_STANDARD)
     set(CMAKE_CXX_STANDARD 17)
   endif()
   if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
     add_compile_options(-Wall -Wextra -Wpedantic)
   endif()

将 ``find_package(catkin ...)`` 调用替换为针对每个依赖项的独立调用。

.. code-block:: cmake

   find_package(ament_cmake REQUIRED)
   find_package(rclcpp REQUIRED)
   find_package(std_msgs REQUIRED)

删除 ``catkin_package()`` 调用，并在 ``CMakeLists.txt`` 文件末尾添加 ``ament_package()`` 调用。

.. code-block:: cmake

   ament_package()

让 ``target_link_libraries`` 使用 ``rclcpp`` 和 ``std_msgs`` 提供的现代 CMake targets。

.. code-block:: cmake

   target_link_libraries(talker PUBLIC
     rclcpp::rclcpp
     ${std_msgs_TARGETS})

删除 ``include_directories()`` 调用，并在 ``add_executable(talker talker.cpp)`` 之后添加 ``target_include_directories()`` 调用。不要将 ``rclcpp_INCLUDE_DIRS`` 之类的变量传入 ``target_include_directories()``；使用现代 CMake targets 调用 ``target_link_libraries()`` 时，头文件目录已经得到处理。

.. code-block:: cmake

   target_include_directories(talker PUBLIC
      "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
      "$<INSTALL_INTERFACE:include/${PROJECT_NAME}>")

修改 ``install()`` 调用，将 ``talker`` 可执行文件安装到项目专属目录中。

.. code-block:: cmake

   install(TARGETS talker
     DESTINATION lib/${PROJECT_NAME})

新的 ``CMakeLists.txt`` 如下所示：

.. code-block:: cmake

   cmake_minimum_required(VERSION 3.14.4)
   project(talker)
   if(NOT CMAKE_CXX_STANDARD)
     set(CMAKE_CXX_STANDARD 17)
   endif()
   if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
     add_compile_options(-Wall -Wextra -Wpedantic)
   endif()
   find_package(ament_cmake REQUIRED)
   find_package(rclcpp REQUIRED)
   find_package(std_msgs REQUIRED)
   add_executable(talker talker.cpp)
   target_include_directories(talker PUBLIC
      "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
      "$<INSTALL_INTERFACE:include/${PROJECT_NAME}>")
   target_link_libraries(talker PUBLIC
     rclcpp::rclcpp
     ${std_msgs_TARGETS})
   install(TARGETS talker
     DESTINATION lib/${PROJECT_NAME})
   ament_package()

构建 ROS 2 代码
~~~~~~~~~~~~~~~~~~~~~~~

首先 source 环境配置文件（这里使用按照 ROS 2 安装教程生成的配置文件，该教程在 ``~/ros2_ws`` 中构建），然后使用 ``colcon build`` 构建功能包：

.. code-block:: console

   $ . ~/ros2_ws/install/setup.bash
   $ cd ~/ros2_talker
   $ colcon build

运行 ROS 2 节点
~~~~~~~~~~~~~~~~~~~~~~

由于 ``talker`` 可执行文件已安装到正确目录，source 环境配置文件后，就可以从安装空间通过以下命令运行它：

.. code-block:: console

   $ . ~/ros2_ws/install/setup.bash
   $ ros2 run talker talker

总结
----------

现在，你已经了解如何将一个示例 C++ ROS 1 功能包迁移到 ROS 2。迁移自己的 C++ 功能包时，请参考 :doc:`C++ 功能包迁移参考 <./Migrating-CPP-Packages>`。
