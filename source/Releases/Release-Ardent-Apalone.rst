.. redirect-from::

  Release-Ardent-Apalone

Ardent Apalone（ardent）
========================

.. contents:: 目录
   :depth: 2
   :local:

欢迎使用 ROS 2 第一个非 Beta 正式发行版：Ardent Apalone！

支持平台
--------

该 ROS 2 版本支持以下三个平台：

* Ubuntu 16.04（Xenial）
* macOS 10.12（Sierra）
* Windows 10

三个平台均提供二进制软件包和源码编译说明，参见 :doc:`安装说明 <../../Installation>` 以及`Ardent 文档 <https://docs.ros2.org/ardent/>`_。

目标平台
--------

.. list-table::
   :header-rows: 1

   * - 架构
     - Ubuntu Xenial（16.04）
     - macOS Sierra（10.12）
     - Windows 10（VS2015）
   * - amd64
     - 支持
     - 支持
     - 支持
   * - arm64
     - 支持
     -
     -

最低语言要求
------------

* C11
* C++14
* Python 3.5

依赖项要求
----------

以下为首次发布时的最低依赖版本。带星号的版本表示不是操作系统官方软件源中的上游版本，而是由 OSRF 或社区在自定义软件源中构建和分发的版本。

.. list-table::
   :header-rows: 1

   * - 软件包
     - Ubuntu Xenial
     - macOS
     - Windows 10
   * - CMake
     - 3.5.1
     - 3.11.0
     - 3.10.2
   * - EmPY
     - 3.3.2
     - 3.6.5
     - 3.3.2
   * - Ogre
     - 1.10*
     - 1.10*
     - 1.10*
   * - OpenCV
     - 2.4.9
     - 3.4.1
     - 2.4.13.2*
   * - Poco
     - 1.7.7*
     - 1.7.7*
     - 1.7.7*
   * - Python
     - 3.5.1
     - 3.6.5
     - 3.6.4
   * - Qt
     - 5.5.1
     - 5.10.0
     - 5.10.0

Linux 专用依赖（用于 TurtleBot 演示）：PCL 1.7.2。

依赖项包管理器
--------------

* Ubuntu Xenial：apt
* macOS：Homebrew、pip
* Windows：Chocolatey、pip

构建系统支持
------------

* ament_cmake
* cmake
* setuptools

中间件实现支持
--------------

* eProsima Fast-RTPS
* RTI Connext
* ADLINK OpenSplice

功能特性
--------

本次 ROS 2 发行版新增功能：

* 基于 DDS 的分布式发现、发布/订阅和请求/响应通信。
  * 通过 C API 提供。
  * 支持多种供应商实现，包括 eProsima Fast RTPS、ADLINK OpenSplice 和 RTI Connext。
  * 提供多种 QoS 设置，以应对非理想网络。
  * 支持 DDS Security（Connext 和 Fast RTPS）。
* C++ 和 Python 3 客户端库。
  * 使用 C 语言共享通用代码，统一实现。
  * 执行模型与节点分离，支持可组合节点。
  * 节点级参数（当时仅支持 C++）。
  * 生命周期管理（当时仅支持 C++）。
  * 可选进程内通信（当时仅支持 C++）。
* 消息定义支持有界数组、有界字符串和默认值。
* 命令行工具，例如 ros2 run。
* RViz，支持部分显示类型。
* 基于文件系统的资源索引。
* 发布/订阅路径中的实时安全代码（仅适用于兼容 DDS 实现）。
* ROS 1 与 ROS 2 桥接。
* HSR 和 TurtleBot 演示。

更多详情请参阅 :doc:`功能特性 <../../The-ROS2-Project/Features>`。

自 Beta 3 以来的变更
--------------------

* 改进 RViz。
* 改进 C++ 消息数据结构初始化选项。
* 改进日志 API，并在演示程序中使用。
* C++ 支持不同的时钟类型。
* Python 客户端库支持等待服务。
* 初步实现 REP 149，定义 package manifest 格式 3。

已知问题
--------

* Fast RTPS 在处理较大的图像等数据时性能可能不足。
* 使用 Connext 时，基础名称相同但命名空间不同的话题，不能使用不同的数据类型。
* 某些 RMW 实现之间无法列出节点名称。
* Windows 上使用 Ctrl+C 终止 Python 启动文件时可能挂起。
