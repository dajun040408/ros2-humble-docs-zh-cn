.. redirect-from::

  Release-Crystal-Clemmys

Crystal Clemmys（crystal）
==========================

.. contents:: 目录
   :depth: 2
   :local:

Crystal Clemmys 是 ROS 2 的第三个发行版。

支持平台
--------

Crystal Clemmys 根据:doc:`平台支持等级 <../The-ROS2-Project/Platform-Support-Tiers>` 支持以下平台。

Tier 1 平台：

* Ubuntu 18.04（Bionic）
* macOS 10.12（Sierra）
* Windows 10

Tier 2 平台：

* Ubuntu 16.04（Xenial）

目标平台
--------

.. list-table::
   :header-rows: 1

   * - 架构
     - Ubuntu Bionic（18.04）
     - macOS Sierra（10.12）
     - Windows 10（VS2017）
     - Ubuntu Xenial（16.04）
     - Debian Stretch（9）
   * - amd64
     - Tier 1
     - Tier 1
     - Tier 1
     - Tier 2
     - Tier 3
   * - arm64
     - Tier 1
     -
     -
     - Tier 2
     - Tier 3

平台交付方式：

* Debian 软件包：向 rosdistro 提交的软件包会在对应平台提供 Debian 包。
* 二进制归档包：每个平台提供一个归档包，包含 Crystal ROS 2 repos 文件中的所有软件包。
* 源码编译：可从源码构建。

中间件实现支持
--------------

.. list-table::
   :header-rows: 1

   * - 中间件库
     - 供应商
     - 支持等级
     - 平台
     - 架构
   * - rmw_fastrtps_cpp（默认）
     - eProsima Fast-RTPS
     - Tier 1
     - 所有平台
     - 所有架构
   * - rmw_connext_cpp
     - RTI Connext
     - Tier 1
     - 除 Debian 外的平台
     - 除 arm64 外的架构
   * - rmw_opensplice_cpp
     - ADLINK OpenSplice
     - Tier 2
     - 除 Debian 外的平台
     - 所有架构

中间件实现的支持等级取决于平台支持等级。例如，某中间件实现本身为 Tier 1，但运行在 Tier 2 平台上时，只能获得 Tier 2 支持。

最低语言要求
------------

* C11
* C++14
* Python 3.5

依赖项要求
----------

依赖项版本表记录的是首次发布时的最低版本。后续依赖版本可能变化，因此这些版本仅作为最低版本参考。

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
     - 3.13.3
     - 3.13.3
     - 3.5.1
     - 3.7.2
   * - EmPY
     - 3.3.2
     - 3.3.2
     - 3.3.2
     - 3.3.2
     - 3.3.2
   * - Gazebo
     - 9.0.0
     - 9.9.0
     - 不适用
     - 9.9.0*
     - 9.8.0*
   * - OpenCV
     - 3.2.0
     - 4.0.1
     - 3.4.1*
     - 2.4.9
     - 3.2*
   * - OpenSSL
     - 1.1.0g
     - 1.0.2q
     - 1.0.2q
     - 1.0.2g
     - 1.1.0j
   * - Python
     - 3.6.5
     - 3.7.2
     - 3.7.2
     - 3.5.1
     - 3.5.3
   * - Qt
     - 5.9.5
     - 5.12.0
     - 5.10.0
     - 5.5.1
     - 5.7.1

Linux 专用依赖包括 PCL。RMW DDS 中间件供应商包括 Connext DDS 和 Fast-RTPS。
