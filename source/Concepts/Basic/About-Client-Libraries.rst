.. redirect-from::

   Concepts/About-Client-Interfaces
   Concepts/About-ROS-2-Client-Libraries

.. include:: ../../../global_substitutions.txt

客户端库
========

.. contents:: 目录
   :local:

概述
----

客户端库（Client Library）是用户编写 ROS 2 程序时使用的 API。通过客户端库，用户可以访问节点、话题、服务等 ROS 2 概念。

客户端库支持多种编程语言，用户可以根据应用需求选择最合适的语言编写 ROS 2 程序。例如，开发可视化工具时，使用 Python 可以加快原型迭代；而对于系统中注重运行效率的部分，则可能更适合使用 C++ 实现节点。

使用不同客户端库编写的节点可以相互交换消息，因为所有客户端库都实现了代码生成器，使用户能够使用相应语言与 ROS 2 接口文件交互。

除特定语言的通信工具外，客户端库还向用户提供构成 ROS 核心能力的基础功能。例如，客户端库通常可以访问以下功能：

* 名称和命名空间
* 时间（真实时间或仿真时间）
* 参数
* 控制台日志
* 线程模型
* 进程内通信

受支持的客户端库
----------------

C++ 客户端库（``rclcpp``）和 Python 客户端库（``rclpy``）都是客户端库，它们使用 ``rcl`` 中的通用功能。

``rclcpp`` 软件包
~~~~~~~~~~~~~~~~~~~

ROS C++ 客户端库（``rclcpp``）是面向用户、符合 C++ 编程习惯的接口，提供创建节点、发布者和订阅者等 ROS 客户端功能。

``rclcpp`` 构建于 ``rcl`` 和 ``rosidl`` |API| 之上，设计用于配合 ``rosidl_generator_cpp`` 生成的 C++ 消息类型使用。

``rclcpp`` 利用 C++ 及 C++17 的语言特性，让接口尽可能易于使用。由于它复用了 ``rcl`` 中的实现，因此能够与其他使用 ``rcl`` |API| 的客户端库保持一致的行为。

``rclcpp`` 仓库位于 GitHub：`ros2/rclcpp <https://github.com/ros2/rclcpp>`_，其中包含 ``rclcpp`` |package|。生成的 |API| 文档位于 {package_link(rclcpp)}。

``rclpy`` 软件包
~~~~~~~~~~~~~~~~~~~

ROS Python 客户端库（``rclpy``）是 C++ 客户端库对应的 Python 实现。与 C++ 客户端库类似，``rclpy`` 的实现也构建在 ``rcl`` C API 之上。

该接口提供符合 Python 使用习惯的编程体验，使用 Python 原生类型和列表、上下文对象等语言模式。由于底层使用 ``rcl`` |API|，它在功能和行为上能够与其他客户端库保持一致。

除围绕 ``rcl`` |API| 提供符合 Python 习惯的绑定，以及为每种消息提供 Python 类之外，Python 客户端库还负责执行模型，例如使用 ``threading.Thread`` 或类似机制运行 ``rcl`` |API| 中的函数。

与 C++ 类似，``rclpy`` 会为用户使用的每种 ROS 消息生成自定义 Python 代码。但与 C++ 不同的是，它最终会将原生 Python 消息对象转换为 C 版本的消息。所有操作最初都在 Python 消息对象上完成；只有当消息需要传递到 ``rcl`` 层时，才会将其转换为普通 C 消息，以便传入 ``rcl`` C |API|。如果发布者和订阅者位于同一进程内，则在可行的情况下会避免这类转换，以减少开销。

``rclpy`` 仓库位于 GitHub：`ros2/rclpy <https://github.com/ros2/rclpy>`_，其中包含 ``rclpy`` |package|。生成的 |API| 文档位于 {package_link(rclpy)}。

由社区维护的客户端库
~~~~~~~~~~~~~~~~~~~~

C++ 和 Python 客户端库由 ROS 2 核心团队维护，ROS 2 社区成员还维护了其他客户端库：

* `Go <https://github.com/merlindrones/rclgo>`__：``rclgo``，ROS 2 的 Go 语言绑定。
* `Ada <https://github.com/ada-ros/ada4ros2>`__：一组支持 ROS 2 Ada 应用开发的软件包，包括 ``rcl`` 绑定、消息生成器、``tf2`` 绑定、示例和教程。
* `C <https://github.com/ros2/rclc>`__：``rclc`` 不在 ``rcl`` 之上增加额外抽象层，而是对 ``rcl`` 进行补充，使 ``rcl+rclc`` 成为功能完整的 C 客户端库。教程请参阅 `micro.ros.org <https://micro.ros.org/>`__。
* `JVM 和 Android <https://github.com/ros2-java>`__：ROS 2 的 Java 和 Android 绑定。
* `.NET Core、UWP 和 C# <https://github.com/esteve/ros2_dotnet>`__：用于编写 ROS 2 应用的一组项目，包括绑定、代码生成器和示例等。
* `Node.js <https://www.npmjs.com/package/rclnodejs>`__：``rclnodejs`` 是 ROS 2 的 Node.js 客户端，提供简单易用的 JavaScript API。
* `Rust <https://github.com/ros2-rust/ros2_rust>`__：一组支持使用 Rust 开发 ROS 2 应用的项目，包括 ``rclrs`` 客户端库、代码生成器和示例等。
* `Flutter 和 Dart <https://github.com/rcldart>`__：ROS 2 的 Flutter 和 Dart 绑定。

以下客户端库较旧且已停止维护：

* `C# <https://github.com/firesurfer/rclcs>`__
* `Objective C 和 iOS <https://github.com/esteve/ros2_objc>`__
* `Zig <https://github.com/jacobperron/rclzig>`__

通用功能：``rcl``
-------------------

客户端库中的大部分功能并不依赖具体编程语言。例如，参数行为和命名空间逻辑原则上应当在所有编程语言中保持一致。

因此，客户端库不会从头实现这些通用功能，而是使用统一的 ROS 客户端库（ROS Client Library，RCL）接口。RCL 实现了与编程语言无关的 ROS 概念逻辑和行为。客户端库只需通过外部函数接口（FFI）封装 RCL 中的通用功能，从而让客户端库更加轻量，也更容易开发。通用 RCL 功能通过 C 接口暴露，是因为 C 通常最容易被其他客户端库封装。

通用核心不仅能让客户端库保持轻量，还能提高不同语言之间行为的一致性。如果修改了 RCL 核心中的逻辑或行为（例如命名空间处理），所有使用 RCL 的客户端库都会体现这些变化。此外，使用共同核心也能减少维护多个客户端库时修复缺陷所需的工作量。

``rcl`` 的 API 文档可在 `此处 <{package_link(rcl)}>`__ 查看。

特定语言的功能
--------------

需要依赖特定编程语言特性或属性的客户端库概念，不会在 RCL 中实现，而是由各客户端库分别实现。例如，``spin`` 函数所使用的线程模型，就会根据客户端库所使用的语言采用不同实现。

演示
----

如果希望了解使用 ``rclpy`` 的发布者与使用 ``rclcpp`` 的订阅者之间如何交换消息，建议观看 `这场 ROSCon 演讲 <https://vimeo.com/187696091>`__，从 17:25 开始；也可以 `查看演讲幻灯片 <https://roscon.ros.org/2016/presentations/ROSCon%202016%20-%20ROS%202%20Update.pdf>`_。

与 ROS 1 的比较
---------------

在 ROS 1 中，所有客户端库都是从头开始独立开发的。例如，ROS 1 的 Python 客户端库可以完全使用 Python 实现，因此不需要编译代码。

但这种方式也存在不足：不同客户端库的命名约定和行为不一定一致；修复缺陷时需要在多个位置重复修改；某些功能也只在某一个客户端库中实现过（例如 UDPROS）。

总结
----

通过使用共同的 ROS 客户端库核心，可以更容易地开发多种编程语言的客户端库，并使它们具有更加一致的行为。
