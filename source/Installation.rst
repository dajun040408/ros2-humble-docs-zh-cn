.. _InstallationGuide:
.. _RollingInstall:

安装指南
========

ROS 2 {DISTRO_TITLE_FULL} 提供以下安装方式：

.. toctree::
   :hidden:
   :glob:

   Installation/Ubuntu-Install-Debs
   Installation/Windows-Install-Binary
   Installation/RHEL-Install-RPMs
   Installation/Alternatives
   Installation/Maintaining-a-Source-Checkout
   Installation/Testing
   Installation/RMW-Implementations
   Installation/ROS-2-Mirrors
   Installation/Snapshot-Repository

.. _binary-package-platforms:

二进制软件包
------------

二进制软件包仅针对 `REP-2000 <https://reps.openrobotics.org/rep-2000/#rolling-ridley-june-2020---ongoing>`__ 中列出的 Tier 1 操作系统构建。如果你使用的不是以下操作系统，可能需要从源码构建 ROS 2，或者使用 :doc:`容器方案 <How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers>` 在当前平台运行 ROS 2。

我们为以下平台提供 ROS 2 二进制软件包：

* Ubuntu Linux（amd64 / aarch64）—— Jammy Jellyfish（22.04）

  * :doc:`deb 软件包 <Installation/Ubuntu-Install-Debs>`（推荐）
  * :doc:`二进制归档包 <Installation/Alternatives/Ubuntu-Install-Binary>`

* Red Hat Enterprise Linux 8（amd64）

  * :doc:`RPM 软件包 <Installation/RHEL-Install-RPMs>`（推荐）
  * :doc:`二进制归档包 <Installation/Alternatives/RHEL-Install-Binary>`

* Windows 10（amd64）

  * :doc:`Windows 二进制包（VS 2019）<Installation/Windows-Install-Binary>`

.. _building-from-source:

从源码构建
----------

我们支持在以下平台上从源码构建 ROS 2：

* :doc:`Ubuntu Linux 22.04 <Installation/Alternatives/Ubuntu-Development-Setup>`
* :doc:`Windows 10 <Installation/Alternatives/Windows-Development-Setup>`
* :doc:`RHEL 8 <Installation/Alternatives/RHEL-Development-Setup>`
* :doc:`macOS <Installation/Alternatives/macOS-Development-Setup>`

应该选择哪种安装方式？
----------------------

无论通过二进制软件包安装，还是从源码构建，最终都可以得到功能完整、可正常使用的 ROS 2 环境。两种方式的区别主要取决于你计划如何使用 ROS 2。

**二进制软件包**面向一般用户，提供已经构建好的 ROS 2 安装内容。对于希望立即开始使用 ROS 2、暂时不需要修改底层实现的用户，这是很合适的选择。

Linux 用户有两种二进制安装方式：

- 软件包（根据平台使用 deb 或 RPM）
- 二进制归档包

推荐使用系统软件包安装，因为它会自动安装必要依赖，并随常规系统更新进行更新。不过，安装 deb 或 RPM 软件包通常需要 root 权限。如果没有 root 权限，二进制归档包是较好的替代选择。

Windows 用户使用二进制方式安装时，只能选择二进制归档包（deb 软件包仅适用于 Ubuntu/Debian）。

**从源码构建**面向希望修改 ROS 2 基础组件，或明确排除部分组件的开发者。对于不提供二进制软件包的平台，也建议采用源码构建。此外，从源码构建还可以选择安装 ROS 2 的最新版本。

直接参与 ROS 2 核心开发？
^^^^^^^^^^^^^^^^^^^^^^^^^^

如果你计划直接为 ROS 2 核心功能包贡献代码，可以从源码安装 :doc:`最新开发版本 <Installation/Alternatives/Latest-Development-Setup>`。该安装方式与 :ref:`Rolling 发行版 <rolling_distribution>` 共用安装说明。
