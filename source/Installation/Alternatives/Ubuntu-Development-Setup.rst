.. _linux-latest:

.. redirect-from::

   Installation/Linux-Development-Setup
   Installation/Ubuntu-Development-Setup

Ubuntu（源码安装）
==================

.. contents:: 目录
   :depth: 2
   :local:

系统要求
--------

当前 `{DISTRO_TITLE_FULL}` 面向 Debian 系统的目标平台如下：

* Tier 1：Ubuntu Linux Jammy（22.04）64 位。
* Tier 3：Ubuntu Linux Focal（20.04）64 位。
* Tier 3：Debian Linux Bullseye（11）64 位。

其他 Linux 平台也有不同程度的支持：

* Arch Linux：参见`替代安装说明 <https://wiki.archlinux.org/index.php/ROS#ROS_2>`_。
* Fedora Linux：参见 :doc:`替代安装说明 <Fedora-Development-Setup>`。
* OpenEmbedded / webOS OSE：参见`替代安装说明 <https://github.com/ros/meta-ros/wiki/OpenEmbedded-Build-Instructions>`_。

以上平台支持情况由 `REP 2000 <https://reps.openrobotics.org/rep-2000/>`_ 定义。

系统配置
--------

设置区域语言
^^^^^^^^^^^^

.. include:: ../_Ubuntu-Set-Locale.rst

添加 ROS 2 apt 软件源
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_Apt-Repositories.rst

安装开发工具和 ROS 工具
^^^^^^^^^^^^^^^^^^^^^^^

安装通用软件包：

.. code-block:: console

   $ sudo apt update && sudo apt install -y \
     python3-flake8-docstrings \
     python3-pip \
     python3-pytest-cov \
     ros-dev-tools

根据 Ubuntu 版本安装其他软件包。

.. tabs::

   .. group-tab:: Ubuntu 22.04 LTS 及更高版本

      .. code-block:: console

         $ sudo apt install -y \
            python3-flake8-blind-except \
            python3-flake8-builtins \
            python3-flake8-class-newline \
            python3-flake8-comprehensions \
            python3-flake8-deprecated \
            python3-flake8-import-order \
            python3-flake8-quotes \
            python3-pytest-repeat \
            python3-pytest-rerunfailures

   .. group-tab:: Ubuntu 20.04 LTS

      .. code-block:: console

         $ python3 -m pip install -U \
            flake8-blind-except \
            flake8-builtins \
            flake8-class-newline \
            flake8-comprehensions \
            flake8-deprecated \
            flake8-import-order \
            flake8-quotes \
            "pytest>=5.3" \
            pytest-repeat \
            pytest-rerunfailures \
            empy==3.3.4

.. _linux-dev-get-ros2-code:

获取 ROS 2 源码
--------------

创建工作空间并克隆所有仓库：

.. code-block:: console

   $ mkdir -p ~/ros2_{DISTRO}/src
   $ cd ~/ros2_{DISTRO}
   $ vcs import --input https://raw.githubusercontent.com/ros2/ros2/{REPOS_FILE_BRANCH}/ros2.repos src

.. _linux-development-setup-install-dependencies-using-rosdep:

使用 rosdep 安装依赖项
----------------------

.. include:: ../_Apt-Upgrade-Admonition.rst

.. code-block:: console

   $ sudo rosdep init
   $ rosdep update
   $ rosdep install --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-6.0.1 urdfdom_headers"

.. include:: ../_rosdep_Linux_Mint.rst

安装其他 DDS 实现（可选）
------------------------

如果希望使用默认实现以外的 DDS 或 RTPS 供应商，请参阅 :doc:`相关说明 <../RMW-Implementations>`。

安装 colcon mixin
^^^^^^^^^^^^^^^^^

.. code-block:: console

   $ colcon mixin add default https://github.com/colcon/colcon-mixin-repository/raw/master/index.yaml
   $ colcon mixin update default

构建工作空间中的代码
--------------------

如果已经通过其他方式安装 ROS 2（例如 deb 软件包或二进制发行包），请确保在一个全新的环境中运行以下命令，不要 source 其他 ROS 2 安装环境。

同时，确保 `.bashrc` 中没有 `source /opt/ros/${ROS_DISTRO}/setup.bash`。可以运行 `printenv | grep -i ROS` 检查 ROS 2 是否已 source。如果没有 source，命令应无输出。

有关 ROS 工作空间的更多信息，请参阅 :doc:`相关教程 <../../Tutorials/Beginner-Client-Libraries/Colcon-Tutorial>`。

.. code-block:: console

   $ cd ~/ros2_{DISTRO}/
   $ colcon build --symlink-install --mixin release

注意：如果无法成功编译所有示例，且这阻碍了整个工作空间构建，可以使用 `COLCON_IGNORE`，其作用类似于 `CATKIN_IGNORE`，忽略某个子目录；也可以直接从工作空间中移除该目录。

例如，如果希望避免安装体积较大的 OpenCV 库，可以在 `cam2image` 演示目录中运行 `touch COLCON_IGNORE`，将其排除在构建之外。

环境配置
--------

source 环境设置脚本
^^^^^^^^^^^^^^^^^^^

通过 source 以下文件配置环境：

.. code-block:: console

   $ . ~/ros2_{DISTRO}/install/local_setup.bash

.. note::

   如果使用的不是 bash，请将 `.bash` 替换为对应 Shell。可选值包括：`setup.bash`、`setup.sh`、`setup.zsh`。

.. _talker-listener:

尝试示例
--------

在一个终端中 source 设置文件，然后运行 C++ `talker`：

.. code-block:: console

   $ . ~/ros2_{DISTRO}/install/local_setup.bash
   $ ros2 run demo_nodes_cpp talker

在另一个终端中 source 设置文件，然后运行 Python `listener`：

.. code-block:: console

   $ . ~/ros2_{DISTRO}/install/local_setup.bash
   $ ros2 run demo_nodes_py listener

你应该能看到 `talker` 输出正在 `Publishing` 消息，而 `listener` 输出 `I heard` 并显示收到的消息。这说明 C++ 和 Python API 均能正常工作。

安装后的后续步骤
----------------

继续阅读 :doc:`教程和演示 <../../Tutorials>`，配置环境、创建自己的工作空间和功能包，并学习 ROS 2 核心概念。

使用 ROS 1 桥接
---------------

ROS 1 bridge 可以连接 ROS 1 到 ROS 2 的话题，反之亦然。有关如何构建和使用 ROS 1 bridge，请参阅`专门的文档 <https://github.com/ros2/ros1_bridge/blob/master/README.md>`_。

其他 RMW 实现（可选）
--------------------

ROS 2 默认使用的中间件是 `Fast DDS`，但可以在运行时替换中间件（RMW）。有关如何使用多个 RMW 的说明，请参阅 :doc:`多 RMW 使用指南 <../../How-To-Guides/Working-with-multiple-RMW-implementations>`。

其他编译器
----------

除了 GCC，也可以轻松使用其他编译器编译 ROS 2。

将环境变量 `CC` 和 `CXX` 分别设置为可用的 C 和 C++ 编译器可执行程序，然后重新触发 CMake 配置（使用 `--cmake-force-configure`，或删除需要重新配置的软件包），CMake 就会重新配置并使用新的编译器。

Clang
^^^^^

要配置 CMake 检测并使用 Clang：

.. code-block:: console

   $ sudo apt install clang
   $ export CC=clang
   $ export CXX=clang++
   $ colcon build --cmake-force-configure

保持源码为最新状态
------------------

请参阅 :doc:`维护源码检出 <../Maintaining-a-Source-Checkout>`，了解如何定期更新源码安装。

故障排查
--------

故障排查方法请参阅 :ref:`此处 <linux-troubleshooting>`。

卸载
----

1. 如果按照上文说明使用 colcon 安装工作空间，“卸载”可能只需要打开一个新终端，不再 source 工作空间的 `setup` 文件。这样，环境就会表现得如同系统中没有安装 {DISTRO_TITLE} 一样。

2. 如果还希望释放磁盘空间，可以删除整个工作空间目录：

   .. code-block:: console

      $ rm -rf ~/ros2_{DISTRO}
