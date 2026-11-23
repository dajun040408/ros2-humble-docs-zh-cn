Zenoh
=====

Zenoh 是一种开源通信协议和中间件，旨在促进异构系统之间高效的数据分发。它为高性能发布/订阅和分布式查询提供与位置无关的抽象。更多信息请参阅 `Zenoh 入门文档 <https://zenoh.io/docs/getting-started/first-app/>`_。

前置条件
--------

请先安装 :doc:`rosdep <../../../Tutorials/Intermediate/Rosdep>`。

安装软件包
----------

推荐通过二进制软件包安装 Zenoh RMW 实现，以便进行稳定开发。

受支持的 ROS 2 发行版（参见对应发行版分支）会在各自的 Tier 1 平台上提供二进制软件包。首先，请按照相关说明配置系统，以便安装 ROS 2 二进制软件包。

然后运行以下命令安装 rmw_zenoh 二进制包：

.. code-block:: bash

   sudo apt install ros-{DISTRO}-rmw-zenoh-cpp

从源码构建
----------

只有在需要最新功能时，才建议从源码构建。

默认情况下，项目会将 `zenoh-cpp` 作为 vendored 依赖，并仅启用 Zenoh 的部分功能进行编译。如果有需要，可以通过 CMake 参数 `ZENOHC_CARGO_FLAGS` 覆盖默认设置，以包含其他功能。更多细节请参阅 `zenoh_cpp_vendor/CMakeLists.txt <https://github.com/ros2/rmw_zenoh/blob/{DISTRO}/zenoh_cpp_vendor/CMakeLists.txt>`_。

1. 克隆代码仓库：

.. code-block:: bash

    mkdir ~/ws_rmw_zenoh/src -p && cd ~/ws_rmw_zenoh/src
    git clone https://github.com/ros2/rmw_zenoh.git -b {DISTRO}

2. 安装依赖项：

.. code-block:: bash

    cd ~/ws_rmw_zenoh
    rosdep install --from-paths src --ignore-src --rosdistro {DISTRO} -y

3. 使用 Colcon 构建工作空间：

.. code-block:: bash

    source /opt/ros/{DISTRO}/setup.bash
    colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release

切换到 rmw_zenoh_cpp
--------------------

通过指定环境变量，可以从其他 RMW 实现切换到 rmw_zenoh_cpp：

.. code-block:: bash

   export RMW_IMPLEMENTATION=rmw_zenoh_cpp

运行 talker 和 listener
-----------------------

现在运行 `talker` 和 `listener`，测试 Zenoh。

首先启动 Zenoh 路由器：

.. code-block:: bash

   # terminal 1
   source /opt/ros/{DISTRO}/setup.bash
   ros2 run rmw_zenoh_cpp rmw_zenohd

.. note:: 默认情况下，节点会话配置中禁用了多播发现。如果没有 Zenoh 路由器，节点将无法发现彼此。相反，节点会通过 Zenoh 路由器的 gossip 机制接收其他节点的发现信息。

在第二个终端中运行发布者：

.. code-block:: bash

   # terminal 2
   export RMW_IMPLEMENTATION=rmw_zenoh_cpp
   source /opt/ros/{DISTRO}/setup.bash
   ros2 run demo_nodes_cpp talker

在第三个终端中运行订阅者：

.. code-block:: bash

   # terminal 3
   export RMW_IMPLEMENTATION=rmw_zenoh_cpp
   source /opt/ros/{DISTRO}/setup.bash
   ros2 run demo_nodes_cpp listener

.. note:: 运行这些命令之前，请记得 source ROS 2 环境设置脚本。
