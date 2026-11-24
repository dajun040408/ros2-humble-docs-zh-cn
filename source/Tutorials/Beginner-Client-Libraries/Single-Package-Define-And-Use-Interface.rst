.. _SinglePkgInterface:

.. redirect-from::

    Rosidl-Tutorial
    Tutorials/Single-Package-Define-And-Use-Interface

在单个功能包中定义和使用自定义接口
==================================

**目标：** 学习在 ROS 2 中实现自定义接口的其他方式。

**教程级别：** 初级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

在 :doc:`此前的教程 <./Custom-ROS2-Interfaces>` 中，你已经学习了如何创建自定义 msg 和 srv 接口。

最佳实践是将接口定义放在独立接口功能包中，但有时也可以在同一个功能包中声明、创建和使用接口。

目前接口只能在 CMake 功能包中定义。不过，CMake 功能包也可以通过 ``ament_cmake_python`` 包含 Python 库和节点。因此，可以在一个功能包中同时定义接口和 Python 节点。本教程为简化说明，使用 CMake 功能包和 C++ 节点。

本教程重点介绍 msg 接口，但相同步骤也适用于其他接口类型。

前置条件
--------

建议先阅读 :doc:`自定义 ROS 2 接口基础教程 <./Custom-ROS2-Interfaces>`。还需要安装 ROS 2、创建工作空间，并了解如何创建功能包。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

在工作空间的 ``src`` 目录中创建 ``more_interfaces`` 功能包，并创建消息目录：

.. code-block:: console

   $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 more_interfaces
   $ mkdir more_interfaces/msg

2. 创建 msg 文件
^^^^^^^^^^^^^^^^

在 ``more_interfaces/msg`` 中创建 ``AddressBook.msg``：

.. code-block:: text

   uint8 PHONE_TYPE_HOME=0
   uint8 PHONE_TYPE_WORK=1
   uint8 PHONE_TYPE_MOBILE=2

   string first_name
   string last_name
   string phone_number
   uint8 phone_type

该消息包含以下字段：

* ``first_name``：string 类型。
* ``last_name``：string 类型。
* ``phone_number``：string 类型。
* ``phone_type``：uint8 类型，并定义了多个命名常量。

消息定义中的字段也可以设置默认值。更多接口定制方式请参阅 :doc:`接口概念 <../../Concepts/Basic/About-Interfaces>`。

2.1 构建 msg 文件
~~~~~~~~~~~~~~~~~

现在需要确保 msg 文件能够转换为 C++、Python 等语言可用的源代码。

打开 ``package.xml``，添加以下依赖：

.. code-block:: xml

   <buildtool_depend>rosidl_default_generators</buildtool_depend>
   <exec_depend>rosidl_default_runtime</exec_depend>
   <member_of_group>rosidl_interface_packages</member_of_group>

构建阶段需要 ``rosidl_default_generators``，运行阶段需要 ``rosidl_default_runtime``。

打开 ``CMakeLists.txt``，查找负责从 msg/srv 文件生成消息代码的功能包：

.. code-block:: cmake

   find_package(rosidl_default_generators REQUIRED)

声明需要生成的消息文件列表：

.. code-block:: cmake

   set(msg_files
     "msg/AddressBook.msg"
   )

手动列出 .msg 文件，可以确保添加其他 .msg 文件时，CMake 能够检测到变化并重新配置项目。

接下来生成消息：

.. code-block:: cmake

   rosidl_generate_interfaces(${PROJECT_NAME}
     ${msg_files}
   )

还需要导出消息运行时依赖：

.. code-block:: cmake

   ament_export_dependencies(rosidl_default_runtime)

现在已经可以根据消息定义生成源文件。本教程会在后面的步骤中统一完成编译，因此这里暂时跳过编译步骤。

3. 在同一功能包中使用接口
^^^^^^^^^^^^^^^^^^^^^^^^^^

现在可以开始编写使用该消息的代码。

在 ``more_interfaces/src`` 目录中创建 ``publish_address_book.cpp``，并写入以下代码：

.. code-block:: c++

   #include <chrono>
   #include <memory>

   #include "rclcpp/rclcpp.hpp"
   #include "more_interfaces/msg/address_book.hpp"

   using namespace std::chrono_literals;

   class AddressBookPublisher : public rclcpp::Node
   {
   public:
     AddressBookPublisher()
     : Node("address_book_publisher")
     {
       address_book_publisher_ =
         this->create_publisher<more_interfaces::msg::AddressBook>("address_book", 10);

       auto publish_msg = [this]() -> void {
           auto message = more_interfaces::msg::AddressBook();

           message.first_name = "John";
           message.last_name = "Doe";
           message.phone_number = "1234567890";
           message.phone_type = message.PHONE_TYPE_MOBILE;

           std::cout << "Publishing Contact\\nFirst:" << message.first_name <<
             "  Last:" << message.last_name << std::endl;

           this->address_book_publisher_->publish(message);
         };
       timer_ = this->create_wall_timer(1s, publish_msg);
     }

   private:
     rclcpp::Publisher<more_interfaces::msg::AddressBook>::SharedPtr address_book_publisher_;
     rclcpp::TimerBase::SharedPtr timer_;
   };


   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);
     rclcpp::spin(std::make_shared<AddressBookPublisher>());
     rclcpp::shutdown();

     return 0;
   }

3.1 代码解析
~~~~~~~~~~~~~

首先，包含刚刚创建的 ``AddressBook.msg`` 对应的头文件：

.. code-block:: c++

   #include "more_interfaces/msg/address_book.hpp"

创建节点和 ``AddressBook`` 发布者：

.. code-block:: c++

   using namespace std::chrono_literals;

   class AddressBookPublisher : public rclcpp::Node
   {
   public:
     AddressBookPublisher()
     : Node("address_book_publisher")
     {
       address_book_publisher_ =
         this->create_publisher<more_interfaces::msg::AddressBook>("address_book", 10);

创建一个回调函数，用于周期性发布消息：

.. code-block:: c++

   auto publish_msg = [this]() -> void {

创建 ``AddressBook`` 消息实例，稍后将发布该消息：

.. code-block:: c++

   auto message = more_interfaces::msg::AddressBook();

为 ``AddressBook`` 的各个字段赋值：

.. code-block:: c++

   message.first_name = "John";
   message.last_name = "Doe";
   message.phone_number = "1234567890";
   message.phone_type = message.PHONE_TYPE_MOBILE;

最后，发布消息：

.. code-block:: c++

   std::cout << "Publishing Contact\\nFirst:" << message.first_name <<
     "  Last:" << message.last_name << std::endl;

   this->address_book_publisher_->publish(message);

创建一个 1 秒定时器，每秒调用一次 ``publish_msg`` 函数：

.. code-block:: c++

   timer_ = this->create_wall_timer(1s, publish_msg);

3.2 构建发布者
~~~~~~~~~~~~~~~~~~~~

需要在 ``CMakeLists.txt`` 中为该节点创建新的构建目标：

.. code-block:: cmake

   find_package(rclcpp REQUIRED)

   add_executable(publish_address_book src/publish_address_book.cpp)
   ament_target_dependencies(publish_address_book rclcpp)

   install(TARGETS
     publish_address_book
     DESTINATION lib/${PROJECT_NAME})

3.3 链接接口
~~~~~~~~~~~~

为了在同一个功能包中使用生成的消息，需要添加以下 CMake 代码：

.. code-block:: cmake

   rosidl_get_typesupport_target(cpp_typesupport_target
     ${PROJECT_NAME} rosidl_typesupport_cpp)

   target_link_libraries(publish_address_book "${cpp_typesupport_target}")

这段代码会找到由 ``AddressBook.msg`` 生成的相关 C++ 代码，并使发布者目标能够链接该代码。

如果使用的是另一个独立构建的功能包中的接口，就不需要这一步。只有在同一个功能包中定义并使用接口时，才需要添加这段 CMake 配置。

4. 运行验证
^^^^^^^^^^^

返回工作空间根目录，构建功能包：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ cd ~/ros2_ws
       $ colcon build --packages-up-to more_interfaces

  .. group-tab:: macOS

    .. code-block:: console

       $ cd ~/ros2_ws
       $ colcon build --packages-up-to more_interfaces

  .. group-tab:: Windows

    .. code-block:: console

       $ cd /ros2_ws
       $ colcon build --merge-install --packages-up-to more_interfaces

随后加载工作空间环境并运行发布者：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ source install/local_setup.bash
       $ ros2 run more_interfaces publish_address_book

  .. group-tab:: macOS

    .. code-block:: console

       $ . install/local_setup.bash
       $ ros2 run more_interfaces publish_address_book

  .. group-tab:: Windows

    .. code-block:: console

       $ call install/local_setup.bat
       $ ros2 run more_interfaces publish_address_book

    也可以使用 PowerShell：

    .. code-block:: console

       $ install/local_setup.ps1
       $ ros2 run more_interfaces publish_address_book

此时应该可以看到发布者正在发送你定义的消息，其中包含在 ``publish_address_book.cpp`` 中设置的字段值。

为了确认消息确实通过 ``address_book`` 话题发布，打开另一个终端，加载工作空间环境，然后运行 ``ros2 topic echo``：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ source install/setup.bash
       $ ros2 topic echo /address_book

  .. group-tab:: macOS

    .. code-block:: console

       $ . install/setup.bash
       $ ros2 topic echo /address_book

  .. group-tab:: Windows

    .. code-block:: console

       $ call install/setup.bat
       $ ros2 topic echo /address_book

    也可以使用 PowerShell：

    .. code-block:: console

       $ install/setup.ps1
       $ ros2 topic echo /address_book

本教程不再创建订阅者节点。你可以尝试自己编写一个订阅者作为练习，并参考 :doc:`C++ 发布者和订阅者教程 <./Writing-A-Simple-Cpp-Publisher-And-Subscriber>`。

5. （扩展）使用已有接口定义
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   也可以在新的接口定义中使用已有的接口定义。

   例如，假设 ROS 2 中已有一个名为 ``Contact.msg`` 的消息，它属于 ``rosidl_tutorials_msgs`` 功能包，并且其定义与前面创建的 ``AddressBook.msg`` 相同。

   此时，可以将当前功能包中的 ``AddressBook.msg`` 定义为另一个功能包中 ``Contact`` 类型的字段。甚至可以将 ``AddressBook.msg`` 定义为 ``Contact`` 类型的数组，例如：

   .. code-block:: text

      rosidl_tutorials_msgs/Contact[] address_book

   为了生成该消息，需要在 ``package.xml`` 中声明对 ``Contact.msg`` 所属功能包 ``rosidl_tutorials_msgs`` 的依赖：

   .. code-block:: xml

      <build_depend>rosidl_tutorials_msgs</build_depend>
      <exec_depend>rosidl_tutorials_msgs</exec_depend>

   并在 ``CMakeLists.txt`` 中添加：

   .. code-block:: cmake

      find_package(rosidl_tutorials_msgs REQUIRED)

      rosidl_generate_interfaces(${PROJECT_NAME}
        ${msg_files}
        DEPENDENCIES rosidl_tutorials_msgs
      )

   还需要在发布者节点中包含 ``Contact.msg`` 对应的头文件，才能向 ``address_book`` 添加 ``contacts``：

   .. code-block:: c++

      #include "rosidl_tutorials_msgs/msg/contact.hpp"

   随后可以将回调函数修改为类似下面的形式：

   .. code-block:: c++

      auto publish_msg = [this]() -> void {
        auto msg = std::make_shared<more_interfaces::msg::AddressBook>();
        {
          rosidl_tutorials_msgs::msg::Contact contact;
          contact.first_name = "John";
          contact.last_name = "Doe";
          contact.phone_number = "1234567890";
          contact.phone_type = contact.PHONE_TYPE_MOBILE;
          msg->address_book.push_back(contact);
        }
        {
          rosidl_tutorials_msgs::msg::Contact contact;
          contact.first_name = "Jane";
          contact.last_name = "Doe";
          contact.phone_number = "4254242424";
          contact.phone_type = contact.PHONE_TYPE_HOME;
          msg->address_book.push_back(contact);
        }

        std::cout << "Publishing address book:" << std::endl;
        for (auto contact : msg->address_book) {
          std::cout << "First:" << contact.first_name << "  Last:" << contact.last_name <<
            std::endl;
        }

        address_book_publisher_->publish(*msg);
      };

   构建并运行这些修改后，就可以看到按预期定义的消息，以及上面定义的消息数组。

总结
----

本教程介绍了如何尝试使用不同字段类型定义接口，并在实际使用接口的同一个功能包中构建接口。

你还学习了如何将另一个接口用作字段类型，以及为实现这一功能所需的 ``package.xml``、``CMakeLists.txt`` 和 ``#include`` 配置。

下一步
------

接下来，你将创建一个带有自定义参数的简单 ROS 2 功能包，并学习如何通过启动文件设置该参数。你可以选择使用 :doc:`C++ <./Using-Parameters-In-A-Class-CPP>` 或 :doc:`Python <./Using-Parameters-In-A-Class-Python>` 编写。

相关内容
--------

ROS 2 接口和 IDL（接口定义语言）还有 `多篇设计文章 <https://design.ros2.org/#interfaces>`_ 可供参考。
