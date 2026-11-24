.. redirect-from::

    Tutorials/Ros2bag/Recording-A-Bag-From-Your-Own-Node-Cpp

.. _ROS2BagOwnNode:

从节点录制 bag（C++）
=====================

**目标：** 将自己的 C++ 节点数据录制到 bag。

**教程级别：** 高级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

rosbag2 不仅提供 ros2 bag 命令行工具，还提供 C++ API，可以在自己的源代码中读取和写入 bag。这样可以订阅话题，并在执行其他数据处理的同时，将收到的数据保存到 bag。

前置条件
--------

常规 ROS 2 安装中应已包含 rosbag2。如果通过 Linux deb 软件包安装，通常默认已安装；如果没有，可以运行：

.. code-block:: console

  $ sudo apt install ros-{DISTRO}-rosbag2

请先完成 :doc:§ROS 2 bag 基础教程 <../Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data>§。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

打开新终端并 :doc:§source ROS 2 安装环境 <../Beginner-CLI-Tools/Configuring-ROS2-Environment>§。

进入此前创建的 ros2_ws/src 目录，创建新功能包：

.. code-block:: console

  $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 bag_recorder_nodes --dependencies example_interfaces rclcpp rosbag2_cpp std_msgs

--dependencies 参数会自动将依赖项添加到 package.xml 和 CMakeLists.txt。本例使用 rosbag2_cpp 和 rclcpp，后续部分还需要 example_interfaces。

在 package.xml 中填写描述、维护者信息和许可证：

.. code-block:: xml

  <description>C++ bag writing tutorial</description>
  <maintainer email="you@email.com">Your Name</maintainer>
  <license>Apache License 2.0</license>

2. 编写 C++ 节点
^^^^^^^^^^^^^^^^

在 ros2_ws/src/bag_recorder_nodes/src 目录中创建 simple_bag_recorder.cpp：

.. code-block:: cpp

    #include <rclcpp/rclcpp.hpp>
    #include <std_msgs/msg/string.hpp>
    #include <rosbag2_cpp/writer.hpp>

    using std::placeholders::_1;

    class SimpleBagRecorder : public rclcpp::Node
    {
    public:
      SimpleBagRecorder()
      : Node("simple_bag_recorder")
      {
        writer_ = std::make_unique<rosbag2_cpp::Writer>();
        writer_->open("my_bag");

        subscription_ = create_subscription<std_msgs::msg::String>(
          "chatter", 10, std::bind(&SimpleBagRecorder::topic_callback, this, _1));
      }

    private:
      void topic_callback(std::shared_ptr<rclcpp::SerializedMessage> msg) const
      {
        rclcpp::Time time_stamp = this->now();
        writer_->write(msg, "chatter", "std_msgs/msg/String", time_stamp);
      }

      rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
      std::unique_ptr<rosbag2_cpp::Writer> writer_;
    };

    int main(int argc, char * argv[])
    {
      rclcpp::init(argc, argv);
      rclcpp::spin(std::make_shared<SimpleBagRecorder>());
      rclcpp::shutdown();
      return 0;
    }

.. include:: ../../_internal/Rclcpp-Convenience-Header-Note.rst

2.1 理解代码
~~~~~~~~~~~~

文件顶部的 include 语句对应功能包依赖项。这里包含 rosbag2_cpp 中用于处理 bag 文件的头文件。

在类构造函数中，首先创建 Writer 对象：

.. code-block:: cpp

    writer_ = std::make_unique<rosbag2_cpp::Writer>();

然后打开 bag。这里只指定 URI，其他选项使用默认值。默认存储格式为 sqlite3，默认转换选项不会进行转换，而是按照收到消息时的序列化格式保存：

.. code-block:: cpp

    writer_->open("my_bag");

随后创建订阅者，并指定回调函数。回调中会将消息写入 bag：

.. code-block:: cpp

    subscription_ = create_subscription<std_msgs::msg::String>(
      "chatter", 10, std::bind(&SimpleBagRecorder::topic_callback, this, _1));

该回调接收的是 rclcpp::SerializedMessage，而不是话题数据类型的实例。这样做有两个原因：

1. rosbag2 写入 bag 前需要序列化消息。直接接收序列化数据可以避免先反序列化、再重新序列化。
2. Writer API 可以直接接收序列化消息。

回调首先确定消息时间戳。时间戳可以根据数据类型选择，例如数据产生时间或数据接收时间。本例使用接收时间：

.. code-block:: cpp

    rclcpp::Time time_stamp = this->now();

随后将消息写入 bag。由于尚未向 bag 注册话题，因此需要同时指定话题名称和类型：

.. code-block:: cpp

    writer_->write(msg, "chatter", "std_msgs/msg/String", time_stamp);

2.2 添加可执行程序
~~~~~~~~~~~~~~~~~~

打开 CMakeLists.txt，将 C++ 标准设置为 C++17：

.. code-block:: cmake

    if(NOT CMAKE_CXX_STANDARD)
      set(CMAKE_CXX_STANDARD 17)
    endif()

在依赖项部分（包含 find_package(rosbag2_cpp REQUIRED)）之后添加：

.. code-block:: cmake

    add_executable(simple_bag_recorder src/simple_bag_recorder.cpp)
    ament_target_dependencies(simple_bag_recorder rclcpp rosbag2_cpp std_msgs)

    install(TARGETS
      simple_bag_recorder
      DESTINATION lib/\${PROJECT_NAME}
    )

3. 构建并运行
^^^^^^^^^^^^^

返回 ros2_ws 工作空间根目录并构建：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ colcon build --packages-select bag_recorder_nodes

  .. group-tab:: macOS

    .. code-block:: console

      $ colcon build --packages-select bag_recorder_nodes

  .. group-tab:: Windows

    .. code-block:: console

      $ colcon build --merge-install --packages-select bag_recorder_nodes

打开新终端，进入 ros2_ws 并 source 设置文件：

.. code-block:: console

   $ source install/setup.bash

Windows 使用：

.. code-block:: console

   $ call install/setup.bat

运行节点：

.. code-block:: console

    $ ros2 run bag_recorder_nodes simple_bag_recorder

打开第二个终端，运行 talker 示例节点：

.. code-block:: console

    $ ros2 run demo_nodes_cpp talker

该节点会在 chatter 话题上发布数据。bag 录制节点接收到数据后，会将其写入 my_bag。

停止两个节点后，在一个终端中启动 listener：

.. code-block:: console

    $ ros2 run demo_nodes_cpp listener

在另一个终端中回放刚才录制的 bag：

.. code-block:: console

    $ ros2 bag play my_bag

listener 节点应该能够接收到 bag 中的消息。如果希望再次运行 bag 录制节点，需要先删除 my_bag 目录。

4. 从节点录制合成数据
^^^^^^^^^^^^^^^^^^^^^

bag 不仅可以记录话题数据，也可以记录任意数据。常见场景是生成并保存合成数据。本节介绍两种方式：第一种使用带定时器的节点，适用于从硬件读取数据等场景；第二种不使用节点，适用于不需要 ROS 基础设施功能的情况。

4.1 编写 C++ 节点
~~~~~~~~~~~~~~~~~

在 ros2_ws/src/bag_recorder_nodes/src 中创建 data_generator_node.cpp。节点使用定时器每秒生成一个 example_interfaces/msg/Int32 消息，并写入 timed_synthetic_bag。

.. code-block:: cpp

    #include <chrono>
    #include <example_interfaces/msg/int32.hpp>
    #include <rclcpp/rclcpp.hpp>
    #include <rosbag2_cpp/writer.hpp>

    using namespace std::chrono_literals;

    class DataGenerator : public rclcpp::Node
    {
    public:
      DataGenerator()
      : Node("data_generator")
      {
        data_.data = 0;
        writer_ = std::make_unique<rosbag2_cpp::Writer>();
        writer_->open("timed_synthetic_bag");
        writer_->create_topic(
          {"synthetic", "example_interfaces/msg/Int32",
           rmw_get_serialization_format(), ""});
        timer_ = create_wall_timer(1s, std::bind(&DataGenerator::timer_callback, this));
      }

    private:
      void timer_callback()
      {
        writer_->write(data_, "synthetic", now());
        ++data_.data;
      }

      rclcpp::TimerBase::SharedPtr timer_;
      std::unique_ptr<rosbag2_cpp::Writer> writer_;
      example_interfaces::msg::Int32 data_;
    };

    int main(int argc, char * argv[])
    {
      rclcpp::init(argc, argv);
      rclcpp::spin(std::make_shared<DataGenerator>());
      rclcpp::shutdown();
      return 0;
    }

在 CMakeLists.txt 中添加 data_generator_node 可执行程序，并将 rclcpp、rosbag2_cpp 和 example_interfaces 作为依赖。

构建后运行：

.. code-block:: console

    $ ros2 run bag_recorder_nodes data_generator_node

等待约 30 秒，然后按 Ctrl+C 终止节点。回放生成的 bag：

.. code-block:: console

    $ ros2 bag play timed_synthetic_bag

在另一个终端中查看 /synthetic 话题：

.. code-block:: console

    $ ros2 topic echo /synthetic

你会看到生成并保存的数据以每秒一条的速率输出。

总结
----

你创建了一个订阅话题并将收到的数据写入 bag 的节点，还验证了录制数据可以通过回放重新发布。随后又创建了生成合成数据并写入 bag 的节点和可执行程序。
