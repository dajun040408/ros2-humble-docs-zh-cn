.. redirect-from::

    Tutorials/Security/Introducing-ros2-security

.. _sros2:
.. _ROS-2-Security-Tutorials:

配置安全机制
============

**目标：** 使用 sros2 配置 ROS 2 安全机制。

**教程级别：** 高级

**预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

sros2 软件包提供了在 DDS-Security 基础上使用 ROS 2 的工具和说明。安全功能已经在 Linux、macOS、Windows 等平台以及 C++、Python 等语言环境中进行测试。SROS2 的设计目标是支持任何安全中间件，但并非所有中间件都是开源的，实际支持情况也取决于所使用的 ROS 发行版。

安装
----

通常，按照 :doc:`ROS 2 安装指南 <../../../Installation>` 和 :doc:`环境配置指南 <../../Beginner-CLI-Tools/Configuring-ROS2-Environment>` 完成安装后，即可使用安全功能。如果计划从源码安装，需要安装 OpenSSL 1.0.2g 或更高版本。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ sudo apt update
      $ sudo apt install libssl-dev

  .. group-tab:: macOS

    .. code-block:: console

      $ brew install openssl
      $ export DYLD_LIBRARY_PATH=$(brew --prefix openssl)/lib:$DYLD_LIBRARY_PATH
      $ export OPENSSL_ROOT_DIR=$(brew --prefix openssl)

  .. group-tab:: Windows

    请按照 :ref:`Windows 安装前置依赖 <windows-install-binary-installing-prerequisites>` 安装 OpenSSL。

Fast DDS 需要额外的 CMake 标志来构建安全插件：

.. code-block:: console

  $ colcon build --symlink-install --cmake-args -DSECURITY=ON --packages-select fastrtps rmw_fastrtps_cpp rmw_fastrtps_dynamic_cpp rmw_fastrtps_shared_cpp

选择其他中间件
^^^^^^^^^^^^^^

如果不使用默认中间件实现，请先 :doc:`切换 RMW 实现 <../../../Installation/RMW-Implementations/>`。ROS 2 允许在运行时切换 RMW 实现。有关不同中间件实现的使用方法，请参阅 `多个 RMW 实现使用指南 <../../../How-To-Guides/Working-with-multiple-RMW-implementations>`__。不同供应商之间不支持安全通信。

运行演示
--------

创建用于保存安全文件的目录：

.. code-block:: console

  $ mkdir ~/sros2_demo
  $ cd ~/sros2_demo
  $ ros2 security create_keystore demo_keystore

为 talker 和 listener 节点创建密钥和证书：

.. code-block:: console

  $ ros2 security create_enclave demo_keystore /talker_listener/talker
  $ ros2 security create_enclave demo_keystore /talker_listener/listener

如果 Windows 上出现 unable to write 'random state'，请设置环境变量：

.. code-block:: console

  $ set RANDFILE=C:\dev\ros2\sros2_demo\.rnd

配置环境变量，使中间件能够定位加密材料并启用安全机制。有关变量说明，请参阅 `ROS 2 DDS-Security 集成设计文档 <https://design.ros2.org/articles/ros2_dds_security.html>`__。

.. code-block:: console

  $ export ROS_SECURITY_KEYSTORE=~/sros2_demo/demo_keystore
  $ export ROS_SECURITY_ENABLE=true
  $ export ROS_SECURITY_STRATEGY=Enforce

Windows 环境请使用 set 命令设置相同变量，并将密钥库路径改为 Windows 路径。每个用于演示的终端都必须设置这些变量。

启动 talker 节点：

.. code-block:: console

  $ ros2 run demo_nodes_cpp talker --ros-args --enclave /talker_listener/talker

在另一个终端中启动 listener 节点：

.. code-block:: console

  $ ros2 run demo_nodes_py listener --ros-args --enclave /talker_listener/listener

现在，两个节点将通过身份验证和加密进行通信。可以使用 tcpdump 或 Wireshark 检查网络数据包，验证消息是否已加密。可以任意切换使用 C++（demo_nodes_cpp）或 Python（demo_nodes_py）软件包。
