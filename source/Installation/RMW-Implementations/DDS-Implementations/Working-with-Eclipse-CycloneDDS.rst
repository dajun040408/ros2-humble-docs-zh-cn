.. redirect-from::

    Working-with-Eclipse-CycloneDDS

Eclipse Cyclone DDS
===================

Eclipse Cyclone DDS 是一款性能出色且稳健的开源 DDS 实现。Cyclone DDS 作为 Eclipse IoT 项目完全采用开放方式开发。更多信息请参阅：`Eclipse Cyclone DDS 项目 <https://projects.eclipse.org/projects/iot.cyclonedds>`_。

前置条件
--------

请先安装 :doc:`rosdep <../../../Tutorials/Intermediate/Rosdep>`。

安装软件包
----------

最简单的方式是从 ROS 2 apt 软件源安装：

.. code-block:: console

   $ sudo apt install ros-{DISTRO}-rmw-cyclonedds-cpp

从源码构建
----------

也可以通过源码构建进行安装。

首先，在 ROS 2 工作空间的源码目录中克隆 Cyclone DDS 和 rmw_cyclonedds。要确定正确的检出分支，需要查看 `ROS 发行版的 ros2.repos 文件 <https://raw.githubusercontent.com/ros2/ros2/refs/heads/{DISTRO}/ros2.repos>`_ 中指定的版本。

也可以运行以下命令，自动获取 Cyclone DDS 所需的分支或标签：

.. code-block:: console

   $ CYCLONEDDS_BRANCH=$(curl -s https://raw.githubusercontent.com/ros2/ros2/refs/heads/{DISTRO}/ros2.repos | grep -A 3 "eclipse-cyclonedds/cyclonedds:" | grep "version:" | awk '{print $2}')

然后克隆并检出源码：

.. code-block:: console

   $ cd ros2_ws/src
   $ git clone https://github.com/ros2/rmw_cyclonedds ros2/rmw_cyclonedds -b {DISTRO}
   $ git clone https://github.com/eclipse-cyclonedds/cyclonedds eclipse-cyclonedds/cyclonedds -b ``CYCLONEDDS_BRANCH``

接下来，为 Cyclone DDS 安装必要的软件包：

.. code-block:: console

   $ cd ..
   $ rosdep install --from src -i

最后运行 colcon build：

.. code-block:: console

   $ colcon build --symlink-install

切换到 rmw_cyclonedds
---------------------

通过指定环境变量，可以从其他 RMW 实现切换到 rmw_cyclonedds：

.. code-block:: console

   $ export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

另请参阅：:doc:`使用多个 RMW 实现 <../../../How-To-Guides/Working-with-multiple-RMW-implementations>`。

运行 talker 和 listener
-----------------------

现在运行 ``talker`` 和 ``listener``，测试 Cyclone DDS：

.. code-block:: console

   $ source /opt/ros/{DISTRO}/setup.bash
   $ ros2 run demo_nodes_cpp talker

在另一个终端中运行：

.. code-block:: console

   $ source /opt/ros/{DISTRO}/setup.bash
   $ ros2 run demo_nodes_cpp listener
