.. redirect-from::

   Installation/Linux-Install-Debians
   Installation/Ubuntu-Install-Debians

Ubuntu（deb 软件包）
====================

.. contents:: 目录
   :depth: 2
   :local:

ROS 2 {DISTRO_TITLE_FULL} 的 deb 软件包目前可用于 Ubuntu Jammy（22.04）。目标平台由 `REP 2000 <https://reps.openrobotics.org/rep-2000/>`__ 定义。

资源
------

* 状态页面：

  * ROS 2 {DISTRO_TITLE}（Ubuntu Jammy）：`amd64 <http://repo.ros2.org/status_page/ros_{DISTRO}_default.html>`__、`arm64 <http://repo.ros2.org/status_page/ros_{DISTRO}_ujv8.html>`__
* `Jenkins 实例 <http://build.ros2.org/>`__
* `软件仓库 <http://repo.ros2.org>`__

设置区域语言
--------------

.. include:: _Ubuntu-Set-Locale.rst

.. _linux-install-debians-setup-sources:

配置软件源
------------

.. include:: _Apt-Repositories.rst

.. _linux-install-debs-install-ros-2-packages:

安装 ROS 2 软件包
-------------------

配置软件仓库后，更新 apt 软件包索引：

.. code-block:: console

   $ sudo apt update

.. include:: _Apt-Upgrade-Admonition.rst

.. warning::

   由于 Ubuntu 22.04 早期更新中的相关问题，在安装 ROS 2 之前，务必先更新与 ``systemd`` 和 ``udev`` 相关的软件包。如果在全新安装的系统上未先执行系统升级就安装 ROS 2 依赖项，可能会触发**关键系统软件包被移除**的问题。

   更多信息请参阅 `ros2/ros2#1272 <https://github.com/ros2/ros2/issues/1272>`__ 和 `Launchpad #1974196 <https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1974196>`__。

桌面版安装（推荐）：包含 ROS、RViz、演示程序和教程。

.. code-block:: console

   $ sudo apt install ros-{DISTRO}-desktop

ROS 基础版安装（最小安装）：包含通信库、消息功能包和命令行工具，不包含 GUI 工具。

.. code-block:: console

   $ sudo apt install ros-{DISTRO}-ros-base

开发工具：用于构建 ROS 功能包的编译器和其他工具。

.. code-block:: console

   $ sudo apt install ros-dev-tools

配置环境
----------

加载 setup 脚本
^^^^^^^^^^^^^^^^^

通过加载以下文件配置环境：

.. code-block:: console

   $ source /opt/ros/{DISTRO}/setup.bash

.. note::

   如果使用的不是 bash，请将 ``.bash`` 替换为对应 Shell 的后缀。可选文件包括：``setup.bash``、``setup.sh`` 和 ``setup.zsh``。

运行示例
----------

Talker-Listener 示例
^^^^^^^^^^^^^^^^^^^^^^

如果你已经安装了上文介绍的 ``ros-{DISTRO}-desktop``，可以尝试运行以下示例。

在一个终端中，加载环境设置文件，然后运行 C++ ``talker`` 节点：

.. code-block:: console

   $ source /opt/ros/{DISTRO}/setup.bash
   $ ros2 run demo_nodes_cpp talker

在另一个终端中，加载环境设置文件，然后运行 Python ``listener`` 节点：

.. code-block:: console

   $ source /opt/ros/{DISTRO}/setup.bash
   $ ros2 run demo_nodes_py listener

你应该能看到 ``talker`` 持续输出 ``Publishing`` 消息，而 ``listener`` 输出 ``I heard`` 并显示收到的消息。这说明 C++ 和 Python API 都能够正常工作。

如果希望使用其他 RMW 实现，请参阅 :doc:`相关指南 <./RMW-Implementations>`。

安装后的后续步骤
------------------

继续学习 :doc:`教程和演示 <../../Tutorials>`，配置开发环境、创建自己的工作空间和功能包，并学习 ROS 2 核心概念。

使用 ROS 1 bridge
-------------------

ROS 1 bridge 可以连接 ROS 1 与 ROS 2 之间的话题，实现双向通信。有关如何构建和使用 ROS 1 bridge，请参阅其专门的 `文档 <https://github.com/ros2/ros1_bridge/blob/master/README.md>`__。

其他 RMW 实现（可选）
---------------------

ROS 2 默认使用的中间件是 ``Fast DDS``，但可以在运行时替换中间件（RMW）。有关如何使用多个 RMW 实现，请参阅 :doc:`相关指南 <../How-To-Guides/Working-with-multiple-RMW-implementations>`。

故障排查
----------

故障排查方法请参阅 :doc:`此处 <../How-To-Guides/Installation-Troubleshooting>`。

卸载
------

如果需要卸载 ROS 2，或者在通过二进制软件包安装后切换为源码安装，可以运行以下命令：

.. code-block:: console

   $ sudo apt remove '~nros-{DISTRO}-*' && sudo apt autoremove

你也可以移除软件仓库：

.. code-block:: console

   $ sudo apt remove ros2-apt-source
   $ sudo apt update
   $ sudo apt autoremove
   $ sudo apt upgrade # Consider upgrading for packages previously shadowed.

如何安装某个发行版的旧版本？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

请使用 :doc:`快照软件仓库 <Snapshot-Repository>`。
