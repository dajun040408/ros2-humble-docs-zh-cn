编写可组合节点（C++）
======================

.. contents:: 目录
   :depth: 2
   :local:

起点
----

假设你有一个常规的 `rclcpp::Node` 可执行程序，希望让它与其他节点运行在同一个进程中，以实现更高效的通信。

首先，类直接继承自 `Node`，并定义了 `main` 方法：

.. code-block:: cpp

    namespace palomino
    {
        class VincentDriver : public rclcpp::Node
        {
            // ...
        };
    }

    int main(int argc, char * argv[])
    {
        rclcpp::init(argc, argv);
        rclcpp::spin(std::make_shared<palomino::VincentDriver>());
        rclcpp::shutdown();
        return 0;
    }

通常会在 CMake 中将其编译为可执行程序：

.. code-block:: cmake

    add_executable(vincent_driver src/vincent_driver.cpp)
    install(TARGETS vincent_driver
        DESTINATION lib/${PROJECT_NAME}
    )

代码更新
--------

添加功能包依赖
^^^^^^^^^^^^^^

`package.xml` 应依赖 `rclcpp_components`，参见`示例 <https://github.com/ros2/demos/tree/{REPOS_FILE_BRANCH}/composition/package.xml>`_：

.. code-block:: xml

    <depend>rclcpp_components</depend>

也可以分别添加 `build_depend` 和 `exec_depend`。

类定义
^^^^^^

类定义唯一可能需要的修改，是确保`类构造函数 <https://github.com/ros2/demos/tree/{REPOS_FILE_BRANCH}/composition/src/talker_component.cpp>`_ 接受一个 `NodeOptions` 参数：

.. code-block:: cpp

    VincentDriver(const rclcpp::NodeOptions & options) : Node("vincent_driver", options)
    {
      // ...
    }

不再需要 main 方法
^^^^^^^^^^^^^^^^^^

将 `main` 方法替换为类似 `pluginlib` 的宏调用：

.. code-block:: cpp

    #include <rclcpp_components/register_node_macro.hpp>
    RCLCPP_COMPONENTS_REGISTER_NODE(palomino::VincentDriver)

.. caution::

    如果被替换的 main 方法中包含 `MultiThreadedExecutor`，请记录这一点，并确保组件容器节点也使用多线程执行器。详情见下文。

CMake 修改
^^^^^^^^^^

首先，在 `CMakeLists.txt` 中添加 `rclcpp_components` 依赖：

.. code-block:: cmake

    find_package(rclcpp_components REQUIRED)

其次，将 `add_executable` 替换为 `add_library`，并使用新的 target 名称：

.. code-block:: cmake

    add_library(vincent_driver_component SHARED src/vincent_driver.cpp)

第三，将其他使用旧 target 的构建命令改为针对新 target 执行。不要忘记在 `ament_target_dependencies` 中添加 `rclcpp_components`。例如，将 `ament_target_dependencies(vincent_driver ...)` 改为 `ament_target_dependencies(vincent_driver_component "rclcpp_components" ...)`。

第四，添加新的命令声明组件：

.. code-block:: cmake

    rclcpp_components_register_node(
        vincent_driver_component
        PLUGIN "palomino::VincentDriver"
        EXECUTABLE vincent_driver
    )

第五，将 CMake 中所有针对旧 target 的安装命令改为安装库版本。不要将库 target 安装到 `lib/${PROJECT_NAME}`，而应按以下方式安装：

.. code-block:: cmake

    ament_export_targets(export_vincent_driver_component)
    install(TARGETS vincent_driver_component
            EXPORT export_vincent_driver_component
            ARCHIVE DESTINATION lib
            LIBRARY DESTINATION lib
            RUNTIME DESTINATION bin
    )

运行节点
--------

有关节点组合的详细介绍，请参阅 :doc:`Composition 教程 <Composition>`。

简单来说，如果 Python 启动文件中原本包含：

.. code-block:: python

    from launch_ros.actions import Node

    ld.add_action(Node(
        package='palomino',
        executable='vincent_driver',
    ))

可以将其替换为：

.. code-block:: python

    from launch_ros.actions import ComposableNodeContainer
    from launch_ros.descriptions import ComposableNode

    ld.add_action(ComposableNodeContainer(
        name='a_buncha_nodes',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='palomino',
                plugin='palomino::VincentDriver',
                name='vincent_driver',
                extra_arguments=[{'use_intra_process_comms': True}],
            ),
        ]
    ))

.. caution::

    如果需要多线程，不要将可执行程序设置为 `component_container`，而应使用 `component_container_mt`。
