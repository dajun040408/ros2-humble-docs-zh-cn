Windows（二进制安装）
=====================

.. contents:: 目录
   :depth: 2
   :local:

本页面介绍如何在 Windows 上通过预构建二进制软件包安装 ROS 2。

.. note::

    预构建二进制包不包含所有 ROS 2 软件包。它包含 `ROS base 变体 <https://reps.openrobotics.org/rep-2001/#ros-base>`_ 中的全部软件包，以及 ``ROS desktop 变体 <https://reps.openrobotics.org/rep-2001/#desktop-variants>`_ 中的一部分软件包。具体软件包列表由 ``此 ros2.repos 文件 <https://github.com/ros2/ros2/blob/{REPOS_FILE_BRANCH}/ros2.repos>`_ 中列出的仓库决定。

系统要求
--------

目前仅支持 Windows 10。

.. _windows-install-binary-installing-prerequisites:

.. include:: _Windows-Install-Prerequisites.rst

下载 ROS 2
----------

* 访问 `发行页面 <https://github.com/ros2/ros2/releases>`_。
* 下载最新的 Windows 软件包，例如 ``ros2-{DISTRO}-*-windows-release-amd64.zip``。

.. note::

    可能存在多个二进制下载选项，因此实际文件名可能不同。

.. note::

    如果需要安装 ROS 2 调试库，请参阅下文的“调试相关附加内容”，然后继续下载 ``ros2-package-windows-debug-AMD64.zip``。

* 将 ZIP 文件解压到某个目录（以下假设路径为 ``C:\dev\ros2_{DISTRO}``）。

.. note::

   这些二进制文件使用 Release 构建配置编译。在 Windows（MSVC）上，这意味着下游二进制文件（例如你自己的节点）也必须使用 Release 或 RelWithDebInfo 配置构建，以保证 ABI 兼容性。

   如果希望使用其他构建配置构建下游软件包，请 :doc:`从源码构建 ROS 2 <Alternatives/Windows-Development-Setup>`。例如，使用 Debug 配置：

   .. code-block:: console

      $ colcon build --cmake-args -DCMAKE_BUILD_TYPE=Debug

安装其他 DDS 实现（可选）
-------------------------

如果希望使用默认 Fast DDS 以外的 DDS 或 RTPS 供应商实现，请参阅 :doc:`此处的说明 <RMW-Implementations>`。

环境配置
--------

打开命令行 Shell，并 source ROS 2 环境设置文件，以配置工作空间：

.. code-block:: console

   $ call C:\dev\ros2_{DISTRO}\local_setup.bat

如果之前的命令没有其他错误，但恰好输出一次 ``The system cannot find the path specified.``，这是正常现象。

尝试示例
--------

在命令行 Shell 中，按照上文说明配置 ROS 2 环境，然后运行 C++ ``talker``：

.. code-block:: console

   $ ros2 run demo_nodes_cpp talker

再打开另一个命令行 Shell，运行 Python ``listener``：

.. code-block:: console

   $ ros2 run demo_nodes_py listener

你应该能看到 ``talker`` 输出正在 ``Publishing`` 消息，而 ``listener`` 输出 ``I heard`` 并显示收到的消息。这验证了 C++ 和 Python API 均能正常工作。

安装后的后续步骤
----------------

继续阅读 :doc:`教程和演示 <../../Tutorials>`，配置环境、创建自己的工作空间和功能包，并学习 ROS 2 核心概念。

其他 RMW 实现（可选）
---------------------

ROS 2 默认使用的中间件是 ``Fast DDS``，但可以在运行时替换中间件（RMW）。有关如何使用多个 RMW 的说明，请参阅 :doc:`多 RMW 使用指南 <../How-To-Guides/Working-with-multiple-RMW-implementations>`。

故障排查
--------

故障排查方法请参阅 :ref:`此处 <windows-troubleshooting>`。

卸载
----

1. 如果按照上文说明使用 colcon 安装工作空间，“卸载”可能只需要打开一个新终端，不再 source 工作空间的 ``setup`` 文件。这样，环境就会表现得如同系统中没有安装 {DISTRO_TITLE} 一样。
2. 如果还希望释放磁盘空间，可以删除整个工作空间目录：

   .. code-block:: console

     $ rmdir /s /q \ros2_{DISTRO}

调试相关附加内容
----------------

要下载 ROS 2 调试库，需要下载 ``ros2-{DISTRO}-*-windows-debug-AMD64.zip``。请注意，调试库还需要进行一些额外配置，才能正常使用。

可能需要修改 Python 安装，以启用调试符号和调试二进制文件：

* 在 Windows **搜索栏**中搜索并打开 **Apps and Features**。
* 找到已安装的 Python 版本。
* 点击 Modify。

  .. image:: images/python_installation_modify.png
     :width: 500 px

* 点击 Next，进入 **Advanced Options**。

  .. image:: images/python_installation_next.png
     :width: 500 px

* 确保勾选 **Download debugging symbols** 和 **Download debug binaries**。

  .. image:: images/python_installation_enable_debug.png
     :width: 500 px

* 点击 Install。
