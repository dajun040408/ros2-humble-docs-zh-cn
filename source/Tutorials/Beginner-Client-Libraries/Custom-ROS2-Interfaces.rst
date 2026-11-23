.. redirect-from::

    Tutorials/Custom-ROS2-Interfaces

.. _CustomInterfaces:

创建自定义 msg 和 srv 文件
==========================

**目标：** 定义自定义接口文件（.msg 和 .srv），并在 Python 和 C++ 节点中使用。

**教程级别：** 初级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

此前的教程已经使用消息和服务接口学习 :doc:§话题 <../Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics>§、:doc:§服务 <../Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services>§，以及简单的发布者/订阅者和服务端/客户端节点。

虽然优先使用预定义接口是很好的实践，但有时仍需要定义自己的消息和服务。本教程介绍创建自定义接口定义的基本方法。

前置条件
--------

需要一个 :doc:§ROS 2 工作空间 <./Creating-A-Workspace/Creating-A-Workspace>§。本教程还会使用此前创建的 C++ 和 Python 发布者/订阅者、服务端/客户端功能包测试新接口。

任务
----

1. 创建新功能包
^^^^^^^^^^^^^^^

本教程将在独立功能包中创建自定义 .msg 和 .srv 文件，然后在另一个功能包中使用它们。两个功能包应位于同一个工作空间中。

进入 ros2_ws/src 并创建新功能包：

.. code-block:: console

  $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 tutorial_interfaces

tutorial_interfaces 是新功能包的名称。自定义接口功能包必须使用 ament_cmake，但这不限制其他类型功能包使用其中的消息和服务。你可以在 ament_cmake 功能包中定义接口，然后在 C++ 或 Python 节点中使用。

.msg 和 .srv 文件必须分别放在名为 msg 和 srv 的目录中：

.. code-block:: console

  $ mkdir msg srv

2. 创建自定义定义
^^^^^^^^^^^^^^^^^

2.1 msg 定义
~~~~~~~~~~~~

在 tutorial_interfaces/msg 中创建 Num.msg，内容为：

.. code-block:: text

    int64 num

该自定义消息传递一个名为 num 的 64 位整数。

再创建 Sphere.msg：

.. code-block:: text

    geometry_msgs/Point center
    float64 radius

该消息使用了其他消息功能包中的类型，这里使用 geometry_msgs/Point。

2.2 srv 定义
~~~~~~~~~~~~

在 tutorial_interfaces/srv 中创建 AddThreeInts.srv：

.. code-block:: text

    int64 a
    int64 b
    int64 c
    ---
    int64 sum

该服务请求三个整数 a、b、c，并返回一个名为 sum 的整数。

3. 配置 CMakeLists.txt
^^^^^^^^^^^^^^^^^^^^^^

为了将接口转换为 C++、Python 等语言可用的代码，在 CMakeLists.txt 中添加：

.. code-block:: cmake

  find_package(geometry_msgs REQUIRED)
  find_package(rosidl_default_generators REQUIRED)

  rosidl_generate_interfaces(${PROJECT_NAME}
    "msg/Num.msg"
    "msg/Sphere.msg"
    "srv/AddThreeInts.srv"
    DEPENDENCIES geometry_msgs
  )

注意：rosidl_generate_interfaces 的第一个参数（库名称）必须以功能包名称开头，例如 ${PROJECT_NAME} 或 ${PROJECT_NAME}_suffix。详情参阅§相关问题 <https://github.com/ros2/rosidl/issues/441#issuecomment-591025515>§_。

4. 配置 package.xml
^^^^^^^^^^^^^^^^^^^

接口生成依赖 rosidl_default_generators，因此需要声明构建工具依赖。rosidl_default_runtime 是运行阶段依赖。rosidl_interface_packages 是该功能包所属的接口依赖组，需要通过 member_of_group 标签声明。

在 package.xml 的 package 元素中添加：

.. code-block:: xml

  <depend>geometry_msgs</depend>
  <buildtool_depend>rosidl_default_generators</buildtool_depend>
  <exec_depend>rosidl_default_runtime</exec_depend>
  <member_of_group>rosidl_interface_packages</member_of_group>

5. 构建 tutorial_interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^

在工作空间根目录运行：

.. code-block:: console

  $ colcon build --packages-select tutorial_interfaces

Windows 使用：

.. code-block:: console

  $ colcon build --merge-install --packages-select tutorial_interfaces

构建后，其他 ROS 2 功能包就可以发现这些接口。

6. 确认 msg 和 srv 已创建
^^^^^^^^^^^^^^^^^^^^^^^^^

打开新终端，在工作空间中 source 设置文件：

.. code-block:: console

  $ source install/setup.bash

Windows 使用：

.. code-block:: console

  $ call install/setup.bat

使用 ros2 interface show 检查接口：

.. code-block:: console

  $ ros2 interface show tutorial_interfaces/msg/Num
  int64 num

.. code-block:: console

  $ ros2 interface show tutorial_interfaces/msg/Sphere
  geometry_msgs/Point center
          float64 x
          float64 y
          float64 z
  float64 radius

.. code-block:: console

  $ ros2 interface show tutorial_interfaces/srv/AddThreeInts
  int64 a
  int64 b
  int64 c
  ---
  int64 sum

7. 测试新接口
^^^^^^^^^^^^^

可以修改此前教程创建的发布者/订阅者和服务端/客户端功能包，使其使用新的接口。

例如，测试 Num.msg 时，将标准字符串消息替换为 tutorial_interfaces/msg/Num，并将发布者赋值改为 message.num = count。订阅者则读取 msg.num。

测试 AddThreeInts.srv 时，将原来的 AddTwoInts 替换为 tutorial_interfaces/srv/AddThreeInts，并在请求中增加 c 字段，服务端计算 a + b + c。

在使用自定义接口的功能包中，还需要添加 tutorial_interfaces 依赖：

.. tabs::

  .. group-tab:: C++

    .. code-block:: xml

      <depend>tutorial_interfaces</depend>

  .. group-tab:: Python

    .. code-block:: xml

      <exec_depend>tutorial_interfaces</exec_depend>

完成修改后，先构建 tutorial_interfaces，再构建使用它的功能包。随后运行对应发布者/订阅者或服务端/客户端，即可验证自定义接口。

总结
----

本教程介绍了如何在独立功能包中创建自定义接口，并在其他功能包中使用这些接口。

更多信息请参阅 :doc:§ROS 2 接口概念 <../../Concepts/Basic/About-Interfaces>§。

下一步
------

下一篇教程 :doc:§单功能包中定义和使用接口 <./Single-Package-Define-And-Use-Interface>§ 将介绍 ROS 2 中使用接口的其他方式。
