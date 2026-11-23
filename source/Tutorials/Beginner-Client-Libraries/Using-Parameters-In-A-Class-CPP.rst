.. redirect-from::

    Tutorials/Using-Parameters-In-A-Class-CPP

.. _CppParamNode:

在类中使用参数（C++）
=====================

**目标：** 使用 C++ 创建并运行包含 ROS 参数的类。

**教程级别：** 初级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

创建自己的 :doc:§节点 <../Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes>§ 时，有时需要添加可以从启动文件设置的参数。本教程介绍如何在 C++ 类中创建参数，以及如何在启动文件中设置参数。

前置条件
--------

此前的教程已经介绍了如何 :doc:§创建工作空间 <./Creating-A-Workspace/Creating-A-Workspace>§、:doc:§创建功能包 <./Creating-Your-First-ROS2-Package>§，以及 :doc:§参数 <../Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters>§ 的作用。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

source ROS 2 环境，并在 ros2_ws/src 目录中创建新功能包：

.. code-block:: console

  $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_parameters --dependencies rclcpp

在 package.xml 中填写描述、维护者信息和许可证：

.. code-block:: xml

  <description>C++ parameter tutorial</description>
  <maintainer email="you@email.com">Your Name</maintainer>
  <license>Apache License 2.0</license>

2. 编写 C++ 节点
^^^^^^^^^^^^^^^^

在 ros2_ws/src/cpp_parameters/src 目录中创建 cpp_parameters_node.cpp：

.. code-block:: cpp

    #include <chrono>
    #include <functional>
    #include <string>
    #include <vector>
    #include <rclcpp/rclcpp.hpp>

    using namespace std::chrono_literals;

    class MinimalParam : public rclcpp::Node
    {
    public:
      MinimalParam()
      : Node("minimal_param_node")
      {
        this->declare_parameter("my_parameter", "world");
        timer_ = this->create_wall_timer(
          1000ms, std::bind(&MinimalParam::timer_callback, this));
      }

      void timer_callback()
      {
        std::string my_param = this->get_parameter("my_parameter").as_string();
        RCLCPP_INFO(this->get_logger(), "Hello %s!", my_param.c_str());

        std::vector<rclcpp::Parameter> all_new_parameters{
          rclcpp::Parameter("my_parameter", "world")};
        this->set_parameters(all_new_parameters);
      }

    private:
      rclcpp::TimerBase::SharedPtr timer_;
    };

    int main(int argc, char ** argv)
    {
      rclcpp::init(argc, argv);
      rclcpp::spin(std::make_shared<MinimalParam>());
      rclcpp::shutdown();
      return 0;
    }

2.1 理解代码
~~~~~~~~~~~

构造函数中的 declare_parameter() 创建名为 my_parameter、默认值为 world 的参数。参数类型会根据默认值推断，因此这里是字符串类型。

定时器周期为 1000ms，也就是每秒执行一次 timer_callback()。

回调函数首先通过 get_parameter() 读取参数并输出日志，然后通过 set_parameters() 将参数重新设置为默认字符串 world。如果用户从外部修改了参数，该回调会将它恢复为原始值。

2.1.1（可选）添加 ParameterDescriptor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

可以为参数设置描述符，提供文本说明和约束，例如只读属性或取值范围：

.. code-block:: cpp

    auto param_desc = rcl_interfaces::msg::ParameterDescriptor{};
    param_desc.description = "This parameter is mine!";
    this->declare_parameter("my_parameter", "world", param_desc);

使用后，可以运行以下命令查看参数类型和描述：

.. code-block:: console

    $ ros2 param describe /minimal_param_node my_parameter

2.2 添加可执行程序
~~~~~~~~~~~~~~~~~~

在 CMakeLists.txt 中查找 rclcpp 的位置添加：

.. code-block:: cmake

    add_executable(minimal_param_node src/cpp_parameters_node.cpp)
    ament_target_dependencies(minimal_param_node rclcpp)

    install(TARGETS minimal_param_node DESTINATION lib/cpp_parameters)

3. 构建并运行
^^^^^^^^^^^^^

建议在工作空间根目录运行 rosdep，检查缺少的依赖项：

.. code-block:: console

    $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

然后构建：

.. code-block:: console

    $ colcon build --packages-select cpp_parameters

source 工作空间并运行：

.. code-block:: console

    $ source install/setup.bash
    $ ros2 run cpp_parameters minimal_param_node

终端应该每秒输出一次 Hello world!。

3.1 通过命令行修改参数
~~~~~~~~~~~~~~~~~~~~~~

节点运行时，在另一个终端 source 工作空间并查看参数：

.. code-block:: console

    $ ros2 param list

修改参数：

.. code-block:: console

    $ ros2 param set /minimal_param_node my_parameter earth

如果看到 Set parameter successful，就说明修改成功。另一个终端会输出 Hello earth!。由于节点随后会将参数恢复为 world，因此之后又会输出 Hello world!。

3.2 通过启动文件修改参数
~~~~~~~~~~~~~~~~~~~~~~~~

在 ros2_ws/src/cpp_parameters/ 中创建 launch 目录，并在其中创建 cpp_parameters_launch.py。启动文件可以在启动 minimal_param_node 时将 my_parameter 设置为 earth。

在 CMakeLists.txt 中添加安装 launch 目录的规则：

.. code-block:: cmake

    install(
      DIRECTORY launch
      DESTINATION share/cpp_parameters
    )

重新构建并 source 工作空间后运行：

.. code-block:: console

    $ ros2 launch cpp_parameters cpp_parameters_launch.py

第一次输出应为 Hello earth!，之后由于节点将参数恢复为默认值，会继续输出 Hello world!。

总结
----

你创建了一个包含自定义参数的节点，并学习了如何通过启动文件或命令行设置参数。
