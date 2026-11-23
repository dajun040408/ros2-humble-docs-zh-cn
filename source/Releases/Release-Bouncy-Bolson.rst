.. redirect-from::

  Release-Bouncy-Bolson

Bouncy Bolson（bouncy）
======================

.. contents:: 目录
   :depth: 2
   :local:

Bouncy Bolson 是 ROS 2 的第二个发行版。

支持平台
--------

该 ROS 2 版本支持四个平台。完整信息请参阅§REP 2000 <https://reps.openrobotics.org/rep-2000/#bouncy-bolson-june-2018-june-2019>§_。

* Ubuntu 18.04（Bionic）
  * 提供 amd64 和 arm64 Debian 软件包。
* Ubuntu 16.04（Xenial）
  * 不提供 Debian 软件包，但支持源码构建。
* macOS 10.12（Sierra）
* Windows 10（Visual Studio 2017）

各平台均提供二进制软件包和源码编译说明，参见 :doc:§安装说明 <../../Installation>§ 以及§Bouncy 文档 <https://docs.ros2.org/bouncy/>§_。

最低语言要求
------------

* C11
* C++14
* Python 3.5

依赖项要求
----------

以下版本记录的是首次发布时的依赖最低版本。带星号的版本表示由 OSRF 或社区在自定义软件源中构建和分发，而非操作系统官方软件源中的上游版本。

.. list-table::
   :header-rows: 1

   * - 软件包
     - Ubuntu Bionic
     - macOS
     - Windows 10
     - Ubuntu Xenial
     - Debian Stretch
   * - CMake
     - 3.10.2
     - 3.11.0
     - 3.10.2
     - 3.5.1
     - 3.7.2
   * - EmPY
     - 3.3.2
     - 3.6.5
     - 3.3.2
     - 3.3.2
     - 3.3.2
   * - Ogre
     - 1.10*
     - 1.10*
     - 1.10*
     - 1.10*
     - 1.10*
   * - OpenCV
     - 3.2.0
     - 3.4.1
     - 3.4.1*
     - 2.4.9
     - 3.2*
   * - Poco
     - 1.8.0
     - 1.9.0
     - 1.8.0*
     - 1.8.0*
     - 1.8.0*
   * - Python
     - 3.6.5
     - 3.6.5
     - 3.6.5
     - 3.5.1
     - 3.5.3
   * - Qt
     - 5.9.5
     - 5.10.0
     - 5.10.0
     - 5.5.1
     - 5.7.1

Linux 专用依赖（用于 TurtleBot 演示）：PCL。

功能特性
--------

本次 ROS 2 发行版新增功能：

* 全新的 Launch 系统，提供更强大、更灵活的 Python API。
* 可以通过命令行参数向 C++ 可执行程序传递参数。
* 支持通过命令行参数进行静态重映射。
* 改进 Python 客户端库。
* 支持发布和订阅序列化数据，为原生 rosbag 实现奠定基础。
* 增加更多命令行工具，例如参数和生命周期状态工具。
* 二进制软件包和 fat archive 默认支持三种 RMW 实现，无需源码构建：
  * eProsima Fast RTPS（默认）
  * RTI Connext
  * ADLINK OpenSplice

完整功能列表请参阅 :doc:§功能特性 <../../The-ROS2-Project/Features>§。

自 Ardent 以来的变更
--------------------

* Python launch 软件包经过重新设计。旧 Python API 移动到了 launch.legacy 子模块。若暂时不希望迁移到新 API，可以修改现有启动文件继续使用旧 API。
* ROS 话题名称中的命名空间会映射到包含对应命名空间的 DDS 话题。
* 改进 Python 客户端库和命令行工具。
* 增加序列化消息发布/订阅支持。
