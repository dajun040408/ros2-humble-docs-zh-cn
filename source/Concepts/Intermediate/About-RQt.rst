.. redirect-from::

   RQt-Overview-Usage
   Tutorials/RQt-Overview-Usage
   Concepts/About-RQt

RQt 概述与使用方法
==================

.. contents:: 目录
   :local:

概述
----

RQt 是一个图形用户界面（GUI）框架，通过插件形式实现各种工具和界面。用户可以在 RQt 中将所有现有 GUI 工具作为可停靠窗口运行。

这些工具仍然可以按照传统方式独立运行，但 RQt 能够将各种窗口集中管理在同一个屏幕布局中，从而简化操作。

运行 RQt 工具或插件非常简单：

.. code-block:: console

   $ rqt

该图形界面允许你选择系统中可用的插件。你也可以在独立窗口中运行插件。例如，运行 RQt Python 控制台：

.. code-block:: console

   $ ros2 run rqt_py_console rqt_py_console

用户可以使用 ``Python`` 或 ``C++`` 为 RQt 创建自己的插件。

要查看系统中有哪些 RQt 插件，可以运行：

.. code-block:: console

   $ ros2 pkg list

然后查找以 ``rqt_`` 开头的功能包。

系统安装
--------

通过 deb 软件包安装
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   $ sudo apt install ros-{DISTRO}-rqt*

RQt 组件结构
------------

RQt 包含两个元功能包（metapackages）：

* ``rqt``：核心基础设施模块。
* ``rqt_common_plugins``：常用调试工具。

RQt 框架的优势
--------------

与从零开始自行构建 GUI 相比，RQt 具有以下优势：

* 提供标准化的 GUI 通用流程（启动/关闭钩子、恢复上次状态）。
* 多个控件可以停靠在同一个窗口中。
* 可以轻松地将现有 Qt 控件转换为 RQt 插件。
* 可以在 `Robotics Stack Exchange <https://robotics.stackexchange.com/>`__（ROS 社区问答网站）上获取支持。

从系统架构角度看：

* 支持多平台（基本上只要 Qt 和 ROS 能够运行的平台都可以），并支持多种语言（``Python``、``C++``）。
* 插件使用统一 API，生命周期易于管理，有助于维护和复用。

延伸阅读
--------

* ROS 2 移植公告：`RQt porting to ROS 2 <https://discourse.openrobotics.org/t/rqt-in-ros2/6428>`__。
* `ROS 1 的 RQt 文档 <https://wiki.ros.org/rqt>`__。
* `RQt 简介 <http://web.archive.org/web/20130518142837/http://www.willowgarage.com/blog/2012/10/21/ros-gui>`__。
