RHEL（二进制安装）
===================

.. contents:: 目录
   :depth: 2
   :local:

本页面介绍如何在 RHEL 上通过预构建二进制软件包安装 ROS 2。

.. note::

    预构建二进制包不包含所有 ROS 2 软件包。它包含 `ROS base 变体 <https://reps.openrobotics.org/rep-2001/#ros-base>`_ 中的全部软件包，以及 `ROS desktop 变体 <https://reps.openrobotics.org/rep-2001/#desktop-variants>`_ 中的一部分软件包。具体软件包列表由 `此 ros2.repos 文件 <https://github.com/ros2/ros2/blob/{REPOS_FILE_BRANCH}/ros2.repos>`_ 中列出的仓库决定。

此外，还提供 :doc:`RPM 软件包 <../RHEL-Install-RPMs>`。

系统要求
--------

目前支持 64 位 RHEL 8。

启用所需软件源
--------------

rosdep 数据库包含来自 EPEL 和 PowerTools 软件源的软件包，而这些软件源默认未启用。可以运行以下命令启用：

.. code-block:: console

   $ sudo dnf install 'dnf-command(config-manager)' epel-release -y
   $ sudo dnf config-manager --set-enabled powertools

.. note:: 根据所使用的发行版，此步骤可能略有不同。
          `请查看 EPEL 文档 <https://docs.fedoraproject.org/en-US/epel/#_quickstart>`_

安装前置依赖
------------

需要安装一些软件包，以便下载并解压二进制发行包：

.. code-block:: console

   $ sudo dnf install tar bzip2 wget -y

下载 ROS 2
----------

* 访问 `发行页面 <https://github.com/ros2/ros2/releases>`_。
* 下载最新的 RHEL 软件包。以下假设下载文件位于 ``~/Downloads/ros2-package-linux-x86_64.tar.bz2``。

  * 注意：可能存在多个二进制下载选项，因此实际文件名可能不同。

* 解压：

  .. code-block:: console

       $ mkdir -p ~/ros2_{DISTRO}
       $ cd ~/ros2_{DISTRO}
       $ tar xf ~/Downloads/ros2-package-linux-x86_64.tar.bz2

安装并初始化 rosdep
-------------------

.. code-block:: console

       $ sudo dnf install -y python3-rosdep
       $ sudo rosdep init
       $ rosdep update

.. _rhel-install-binary-install-missing-dependencies:

安装缺失的依赖项
----------------

.. include:: ../_Dnf-Update-Admonition.rst

根据下载的发行版设置 rosdistro。

.. code-block:: bash

       rosdep install --from-paths ~/ros2_{DISTRO}/ros2-linux/share --ignore-src -y --skip-keys "asio cyclonedds fastcdr fastrtps ignition-cmake2 ignition-math6 python3-babeltrace python3-mypy rti-connext-dds-6.0.1 urdfdom_headers"

安装其他 DDS 实现（可选）
^^^^^^^^^^^^^^^^^^^^^^^^^

如果希望使用默认 DDS 以外的 DDS 或 RTPS 供应商实现，请参阅 :doc:`此处的说明 <../RMW-Implementations>`。

环境配置
--------

source 环境设置脚本
^^^^^^^^^^^^^^^^^^^

通过 source 以下文件配置环境：

.. code-block:: console

   $ . ~/ros2_{DISTRO}/ros2-linux/setup.bash

.. note::

   如果使用的不是 bash，请将 ``.bash`` 替换为对应 Shell。可选值包括：``setup.bash``、``setup.sh``、``setup.zsh``。

尝试示例
--------

在一个终端中 source 环境设置文件，然后运行 C++ ``talker``：

.. code-block:: console

   $ . ~/ros2_{DISTRO}/ros2-linux/setup.bash
   $ ros2 run demo_nodes_cpp talker

在另一个终端中 source 环境设置文件，然后运行 Python ``listener``：

.. code-block:: console

   $ . ~/ros2_{DISTRO}/ros2-linux/setup.bash
   $ ros2 run demo_nodes_py listener

你应该能看到 ``talker`` 输出正在 ``Publishing`` 消息，而 ``listener`` 输出 ``I heard`` 并显示收到的消息。这验证了 C++ 和 Python API 均能正常工作。

安装后的后续步骤
----------------

继续阅读 :doc:`教程和演示 <../../Tutorials>`，配置环境、创建自己的工作空间和功能包，并学习 ROS 2 核心概念。

其他 RMW 实现（可选）
---------------------

ROS 2 默认使用的中间件是 ``Fast DDS``，但可以在运行时替换中间件（RMW）。有关如何使用多个 RMW 的说明，请参阅 :doc:`多 RMW 使用指南 <../../How-To-Guides/Working-with-multiple-RMW-implementations>`。

故障排查
--------

故障排查方法请参阅 :doc:`此处 <../../How-To-Guides/Installation-Troubleshooting>`。

卸载
----

1. 如果按照上文说明使用 colcon 安装工作空间，“卸载”可能只需要打开一个新终端，不再 source 工作空间的 ``setup`` 文件。这样，环境就会表现得如同系统中没有安装 {DISTRO_TITLE} 一样。
2. 如果还希望释放磁盘空间，可以删除整个工作空间目录：

   .. code-block:: console

      $ rm -rf ~/ros2_{DISTRO}
