.. redirect-from::

    Tutorials/Tf2/Tf2-Main

.. _Tf2Main:

tf2 教程
========

许多 tf2 教程同时提供 C++ 和 Python 版本。教程按语言分为两条学习路径，你可以选择完成 C++ 路径或 Python 路径。如果你希望同时学习 C++ 和 Python，建议先完整学习一遍 C++ 教程，再完整学习一遍 Python 教程。

.. contents:: 目录
   :depth: 2
   :local:

.. toctree::
   :hidden:

   Introduction-To-Tf2
   Writing-A-Tf2-Static-Broadcaster-Py
   Writing-A-Tf2-Static-Broadcaster-Cpp
   Writing-A-Tf2-Broadcaster-Py
   Writing-A-Tf2-Broadcaster-Cpp
   Writing-A-Tf2-Listener-Py
   Writing-A-Tf2-Listener-Cpp
   Adding-A-Frame-Py
   Adding-A-Frame-Cpp
   Learning-About-Tf2-And-Time-Cpp
   Time-Travel-With-Tf2-Cpp
   Debugging-Tf2-Problems
   Quaternion-Fundamentals
   Using-Stamped-Datatypes-With-Tf2-Ros-MessageFilter

工作空间配置
------------

如果你尚未创建用于完成教程的工作空间，请 :doc:`按照本教程创建工作空间 <../../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace>`。

学习 tf2
--------

#. :doc:`tf2 简介 <./Introduction-To-Tf2>`。

   本教程将帮助你了解 tf2 能够完成哪些工作。教程通过 turtlesim 多机器人示例展示 tf2 的部分功能，并介绍 `tf2_echo`、`view_frames` 和 `rviz` 的使用方法。

#. 编写静态广播器：:doc:`Python <./Writing-A-Tf2-Static-Broadcaster-Py>`、:doc:`C++ <./Writing-A-Tf2-Static-Broadcaster-Cpp>`。

   学习如何向 tf2 广播静态坐标系。

#. 编写广播器：:doc:`Python <./Writing-A-Tf2-Broadcaster-Py>`、:doc:`C++ <Writing-A-Tf2-Broadcaster-Cpp>`。

   学习如何向 tf2 广播机器人的状态。

#. 编写监听器：:doc:`Python <./Writing-A-Tf2-Listener-Py>`、:doc:`C++ <./Writing-A-Tf2-Listener-Cpp>`。

   学习如何使用 tf2 获取坐标系之间的变换。

#. 添加坐标系：:doc:`Python <./Adding-A-Frame-Py>`、:doc:`C++ <Adding-A-Frame-Cpp>`。

   学习如何向 tf2 添加额外的固定坐标系。

#. 使用时间：:doc:`C++ <Learning-About-Tf2-And-Time-Cpp>`。

   学习如何在 `lookup_transform` 函数中使用超时时间，等待 tf2 坐标树中出现所需变换。

#. 时间旅行：:doc:`C++ <./Time-Travel-With-Tf2-Cpp>`。

   学习 tf2 的高级时间旅行功能。

调试 tf2
--------

#. :doc:`四元数基础 <./Quaternion-Fundamentals>`。

   学习 ROS 2 中使用四元数的基础知识。

#. :doc:`调试 tf2 问题 <./Debugging-Tf2-Problems>`。

   学习系统化排查 tf2 相关问题的方法。

在 tf2 中使用传感器消息
-----------------------

#. :doc:`在 tf2_ros::MessageFilter 中使用带时间戳的数据类型 <./Using-Stamped-Datatypes-With-Tf2-Ros-MessageFilter>`。

   学习如何使用 `tf2_ros::MessageFilter` 处理带时间戳的数据类型。
