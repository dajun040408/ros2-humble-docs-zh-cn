从 bag 文件读取数据（C++）
============================

**目标：** 不使用命令行工具，直接从 bag 文件读取数据。

**教程级别：** 高级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

rosbag2 不仅提供 ros2 bag 命令行工具，还提供 C++ API，可以在自己的源代码中读取和写入 bag。这样就可以不必播放整个 bag，而直接读取其中的内容。

前置条件
--------

常规 ROS 2 安装中应已包含 rosbag2 软件包。如果需要安装 ROS 2，请参阅 :doc:§安装说明 <../../Installation>§。

请先完成 :doc:§ROS 2 bag 基础教程 <../Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data>§，本教程会使用其中创建的 subset bag。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

打开新终端并 :doc:§source ROS 2 安装环境 <../Beginner-CLI-Tools/Configuring-ROS2-Environment>§。

在新建或已有工作空间的 src 目录中创建功能包：

.. code-block:: console

  $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 bag_reading_cpp --dependencies rclcpp rosbag2_transport turtlesim

--dependencies 参数会自动将依赖项添加到 package.xml 和 CMakeLists.txt。本例使用 rosbag2_transport、rclcpp 和 turtlesim。

在 package.xml 中填写描述、维护者邮箱和姓名，以及许可证：

.. code-block:: xml

  <description>C++ bag reading tutorial</description>
  <maintainer email="you@email.com">Your Name</maintainer>
  <license>Apache-2.0</license>

2. 编写 C++ Reader
^^^^^^^^^^^^^^^^^^

在功能包 src 目录中创建 simple_bag_reader.cpp，并写入以下代码：

.. code-block:: cpp

    #include <chrono>
    #include <functional>
    #include <iostream>
    #include <memory>
    #include <string>

    #include "rclcpp/rclcpp.hpp"
    #include "rclcpp/serialization.hpp"
    #include "rosbag2_transport/reader_writer_factory.hpp"
    #include "turtlesim/msg/pose.hpp"

    using namespace std::chrono_literals;

    class PlaybackNode : public rclcpp::Node
    {
    public:
      PlaybackNode(const std::string & bag_filename)
      : Node("playback_node")
      {
        publisher_ = this->create_publisher<turtlesim::msg::Pose>("/turtle1/pose", 10);
        timer_ = this->create_wall_timer(
            100ms, std::bind(&PlaybackNode::timer_callback, this));

        rosbag2_storage::StorageOptions storage_options;
        storage_options.uri = bag_filename;
        reader_ = rosbag2_transport::ReaderWriterFactory::make_reader(storage_options);
        reader_->open(storage_options);
      }

    private:
      void timer_callback()
      {
        while (reader_->has_next()) {
          rosbag2_storage::SerializedBagMessageSharedPtr msg = reader_->read_next();

          if (msg->topic_name != "/turtle1/pose") {
            continue;
          }

          rclcpp::SerializedMessage serialized_msg(*msg->serialized_data);
          turtlesim::msg::Pose::SharedPtr ros_msg = std::make_shared<turtlesim::msg::Pose>();
          serialization_.deserialize_message(&serialized_msg, ros_msg.get());

          publisher_->publish(*ros_msg);
          std::cout << '(' << ros_msg->x << ", " << ros_msg->y << ")\n";
          break;
        }
      }

      rclcpp::TimerBase::SharedPtr timer_;
      rclcpp::Publisher<turtlesim::msg::Pose>::SharedPtr publisher_;
      rclcpp::Serialization<turtlesim::msg::Pose> serialization_;
      std::unique_ptr<rosbag2_cpp::Reader> reader_;
    };

    int main(int argc, char ** argv)
    {
      if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <bag>" << std::endl;
        return 1;
      }

      rclcpp::init(argc, argv);
      rclcpp::spin(std::make_shared<PlaybackNode>(argv[1]));
      rclcpp::shutdown();
      return 0;
    }

2.1 理解代码
~~~~~~~~~~~~

文件顶部的 include 语句对应功能包依赖项。注意这里包含 rosbag2_transport 中用于处理 bag 文件的头文件。

PlaybackNode 节点会创建一个 10 Hz 定时器，每次回调从 bag 中读取一条 /turtle1/pose 消息并发布。

构造函数接收 bag 文件路径，并通过 rosbag2_transport::ReaderWriterFactory 创建 reader。该工厂类可以根据存储选项创建压缩或未压缩的 reader/writer。

定时器回调会循环读取消息，直到找到目标话题。读取到的是序列化消息，其中包含话题名称和时间戳等元数据。

随后创建 rclcpp::SerializedMessage，并通过 rclcpp::Serialization::deserialize_message 将其反序列化为 turtlesim::msg::Pose。最后发布消息，并输出乌龟的 x、y 坐标。

2.2 添加可执行程序
~~~~~~~~~~~~~~~~~~

打开 CMakeLists.txt，在依赖项部分（包含 find_package(rosbag2_transport REQUIRED)）之后添加：

.. code-block:: cmake

    add_executable(simple_bag_reader src/simple_bag_reader.cpp)
    ament_target_dependencies(simple_bag_reader rclcpp rosbag2_transport turtlesim)

    install(TARGETS
      simple_bag_reader
      DESTINATION lib/\${PROJECT_NAME}
    )

3. 构建并运行
^^^^^^^^^^^^^

返回工作空间根目录并构建功能包：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ colcon build --packages-select bag_reading_cpp

  .. group-tab:: macOS

    .. code-block:: console

      $ colcon build --packages-select bag_reading_cpp

  .. group-tab:: Windows

    .. code-block:: console

      $ colcon build --merge-install --packages-select bag_reading_cpp

source 设置文件：

.. code-block:: console

   $ source install/setup.bash

Windows 使用：

.. code-block:: console

   $ call install/setup.bat

运行程序时，将 /path/to/subset 替换为 subset bag 的实际路径：

.. code-block:: console

    $ ros2 run bag_reading_cpp simple_bag_reader /path/to/subset

你应该能在终端中看到乌龟的 (x, y) 坐标。

总结
----

你创建了一个从 bag 文件读取数据的 C++ 可执行程序，并编译、运行该程序，将 bag 中的信息输出到终端。
