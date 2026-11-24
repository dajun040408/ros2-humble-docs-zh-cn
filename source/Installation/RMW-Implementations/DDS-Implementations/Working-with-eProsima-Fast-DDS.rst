eProsima Fast DDS
=================

eProsima Fast DDS 是一款完整的开源 DDS 实现，面向实时嵌入式架构和操作系统。更多信息请参阅：`eProsima Fast DDS 官网 <https://www.eprosima.com/index.php/products-all/eprosima-fast-dds>`_。

前置条件
--------

请先安装 :doc:`rosdep <../../../Tutorials/Intermediate/Rosdep>`。

安装软件包
----------

最简单的方式是从 ROS 2 apt 软件源安装：

.. code-block:: console

   $ sudo apt install ros-{DISTRO}-rmw-fastrtps-cpp

从源码构建
----------

也可以通过源码构建进行安装。

首先，在 ROS 2 工作空间的源码目录中克隆 Fast DDS 和 rmw_fastrtps：

.. code-block:: console

   $ cd ros2_ws/src
   $ git clone https://github.com/ros2/rmw_fastrtps ros2/rmw_fastrtps -b {REPOS_FILE_BRANCH}
   $ git clone https://github.com/eProsima/Fast-DDS eProsima/fastrtps

然后，为 Fast DDS 安装必要的软件包：

.. code-block:: console

   $ cd ..
   $ rosdep install --from src -i

最后，运行 colcon build：

.. code-block:: console

   $ colcon build --symlink-install

切换到 rmw_fastrtps
-------------------

通过设置环境变量，可以选择 eProsima Fast DDS RMW 实现：

.. code-block:: console

   $ export RMW_IMPLEMENTATION=rmw_fastrtps_cpp

另请参阅：:doc:`使用多个 RMW 实现 <../../../How-To-Guides/Working-with-multiple-RMW-implementations>`。

运行 talker 和 listener
-----------------------

现在运行 ``talker`` 和 ``listener``，测试 Fast DDS：

.. code-block:: console

   $ source /opt/ros/{DISTRO}/setup.bash
   $ ros2 run demo_nodes_cpp talker

在另一个终端中运行：

.. code-block:: console

   $ source /opt/ros/{DISTRO}/setup.bash
   $ ros2 run demo_nodes_cpp listener
