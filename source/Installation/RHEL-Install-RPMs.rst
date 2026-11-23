RHEL（RPM 软件包）
==================

.. contents:: 目录
   :depth: 2
   :local:

目前，ROS 2 {DISTRO_TITLE_FULL} 的 RPM 软件包可用于 RHEL 8。目标平台定义在 `REP 2000 <https://reps.openrobotics.org/rep-2000/>`_ 中。

相关资源
--------

* 状态页面：
  * ROS 2 {DISTRO_TITLE}（RHEL 8）：`amd64 <http://repo.ros2.org/status_page/ros_{DISTRO}_rhel.html>`_
* `Jenkins 实例 <http://build.ros2.org/>`_
* `软件仓库 <http://repo.ros2.org>`_

设置区域语言
------------

.. include:: _RHEL-Set-Locale.rst

.. _rhel-install-rpms-setup-sources:

配置软件源
----------

需要启用 EPEL 软件源和 PowerTools 软件源：

.. code-block:: console

   $ sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-$(rpm -E %rhel).noarch.rpm
   $ sudo env FORCE_DNF=1 crb enable

.. note:: 根据所使用的发行版，此步骤可能略有不同。
          `请查看 EPEL 文档 <https://docs.fedoraproject.org/en-US/epel/getting-started/>`_

接下来，下载 `ros2-release` 软件包并安装：

.. code-block:: console

   $ sudo dnf install curl
   $ export ROS_APT_SOURCE_VERSION=$(curl -fsSL -o /dev/null -w '%{url_effective}' https://github.com/ros-infrastructure/ros-apt-source/releases/latest | awk -F/ '{print $NF}')
   $ sudo dnf install "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-release-${ROS_APT_SOURCE_VERSION}-1.noarch.rpm"

`ros2-release <https://github.com/ros-infrastructure/ros-apt-source/>`_ 软件包提供各种 ROS 软件源所需的密钥和仓库配置。当 ROS 软件源发布新版本时，仓库配置也会自动更新。

.. _rhel-install-rpms-install-ros-2-packages:

安装 ROS 2 软件包
-----------------

.. include:: _Dnf-Update-Admonition.rst

桌面版安装（推荐）：包含 ROS、RViz、演示程序和教程。

.. code-block:: console

   $ sudo dnf install ros-{DISTRO}-desktop

ROS-Base 安装（最精简）：包含通信库、消息软件包和命令行工具，不包含 GUI 工具。

.. code-block:: console

   $ sudo dnf install ros-{DISTRO}-ros-base

环境配置
--------

source 环境设置脚本
^^^^^^^^^^^^^^^^^^^

通过 source 以下文件配置环境：

.. code-block:: console

   $ source /opt/ros/{DISTRO}/setup.bash

.. note::

   如果使用的不是 bash，请将 `.bash` 替换为对应 Shell。可选值包括：`setup.bash`、`setup.sh`、`setup.zsh`。

尝试示例
--------

如果已经安装上面的 `ros-{DISTRO}-desktop`，可以尝试运行以下示例。

在一个终端中 source 环境设置文件，然后运行 C++ `talker`：

.. code-block:: console

   $ source /opt/ros/{DISTRO}/setup.bash
   $ ros2 run demo_nodes_cpp talker

在另一个终端中 source 环境设置文件，然后运行 Python `listener`：

.. code-block:: console

   $ source /opt/ros/{DISTRO}/setup.bash
   $ ros2 run demo_nodes_py listener

你应该能看到 `talker` 输出正在 `Publishing` 消息，而 `listener` 输出 `I heard` 并显示收到的消息。这验证了 C++ 和 Python API 均能正常工作。

如果希望使用其他 RMW 实现，请参阅 :doc:`相关指南 <./RMW-Implementations>`。

安装后的后续步骤
----------------

继续阅读 :doc:`教程和演示 <../../Tutorials>`，配置环境、创建自己的工作空间和功能包，并学习 ROS 2 核心概念。

其他 RMW 实现（可选）
--------------------

ROS 2 默认使用的中间件是 `Fast DDS`，但可以在运行时替换中间件（RMW）。有关如何使用多个 RMW 的说明，请参阅 :doc:`多 RMW 使用指南 <../How-To-Guides/Working-with-multiple-RMW-implementations>`。

故障排查
--------

故障排查方法请参阅 :doc:`此处 <../How-To-Guides/Installation-Troubleshooting>`。

卸载
----

如果需要卸载 ROS 2，或者在已经通过二进制软件包安装后切换到源码安装，请运行：

.. code-block:: console

   $ sudo dnf remove ros-{DISTRO}-*

要移除软件源配置，请运行：

.. code-block:: console

   $ sudo dnf remove ros2-release
