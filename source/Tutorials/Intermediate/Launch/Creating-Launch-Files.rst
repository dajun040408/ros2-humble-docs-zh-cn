创建启动文件
============

**目标：** 学习如何创建并运行 ROS 2 启动文件。

**教程级别：** 中级

.. contents:: 目录
   :depth: 2
   :local:

背景
----

启动文件可以一次启动多个节点，并为每个节点设置参数、命名空间和重映射规则。ROS 2 支持 Python、XML 和 YAML 三种启动文件格式。

前置条件
--------

需要安装 ROS 2，并熟悉 :doc:§创建功能包 <../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>§ 和 :doc:§运行节点 <../../Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes>§。

创建启动文件
------------

启动文件可以直接放在目录中运行，也可以安装到 ROS 2 功能包中。常见做法是在功能包中创建 §launch§ 目录，并将启动文件放入其中。

Python 启动文件
^^^^^^^^^^^^^^^

Python 启动文件需要定义 §generate_launch_description()§，返回 §LaunchDescription§：

.. code-block:: python

   from launch import LaunchDescription
   from launch_ros.actions import Node

   def generate_launch_description():
       return LaunchDescription([
           Node(
               package='turtlesim',
               executable='turtlesim_node',
               name='sim'
           )
       ])

XML 启动文件
^^^^^^^^^^^^

XML 启动文件使用 §<launch>§ 作为根元素，并通过 §<node>§ 描述节点：

.. code-block:: xml

   <launch>
     <node pkg="turtlesim" exec="turtlesim_node" name="sim"/>
   </launch>

YAML 启动文件
^^^^^^^^^^^^^

YAML 启动文件通过 §launch:§ 根键描述动作：

.. code-block:: yaml

   launch:
     - node:
         pkg: turtlesim
         exec: turtlesim_node
         name: sim

运行启动文件
------------

进入启动文件所在目录，使用 §ros2 launch§ 运行：

.. code-block:: console

   $ ros2 launch turtlesim_mimic_launch.py

如果启动文件属于功能包，命令格式为：

.. code-block:: console

   $ ros2 launch <package_name> <launch_file_name>

将启动文件安装到功能包
----------------------

Python 功能包应在 §setup.py§ 的 §data_files§ 中安装启动文件：

.. code-block:: python

   import os
   from glob import glob

   data_files=[
       (os.path.join('share', package_name, 'launch'), glob('launch/*')),
   ]

C++ 功能包应在 §ament_package()§ 之前添加：

.. code-block:: cmake

   install(DIRECTORY launch
     DESTINATION share/${PROJECT_NAME}/)

并在 §package.xml§ 中声明 §ros2launch§ 运行依赖：

.. code-block:: xml

   <exec_depend>ros2launch</exec_depend>

总结
----

启动文件可以用 Python、XML 或 YAML 描述多个节点及其启动配置，并通过 §ros2 launch§ 命令统一运行。
