在 Ubuntu 22.04 上使用上游 ROS 与 ros1_bridge
===============================================

.. contents:: 目录
   :depth: 1
   :local:

ROS 2 Humble（以及 Rolling）在 Ubuntu 22.04 Jammy Jellyfish 上发布，标志着 ROS 2 首次在一个没有官方 ROS 1 发行版的平台上发布。

ROS 1 Noetic 在其`长期支持周期 <https://reps.openrobotics.org/rep-0003/#noetic-ninjemys-may-2020---may-2025>`_ 内仍会继续受到支持，但只面向 Ubuntu 20.04。

另一种选择是使用 Debian 和 Ubuntu 中的`上游 ROS 1 软件包变体 <https://packages.ubuntu.com/jammy/ros-desktop>`_，但这些软件包并未由 ROS 维护者作为官方发行版进行维护。

本指南介绍在 Ubuntu 22.04 Jammy Jellyfish 上，将 ROS 2 发行版与这些上游软件包桥接的当前方法。这为仍依赖 ROS 1、但希望迁移到更新版本 ROS 2 和 Ubuntu 的用户提供了一条迁移路径。

通过 deb 软件包安装 ROS 2
-------------------------

目前，在 Ubuntu Jammy 上通过 :doc:`deb 软件包安装 ROS 2 <../Installation/Ubuntu-Install-Debs>` 无法正常工作。

Ubuntu 软件源中的 ``catkin-pkg-modules`` 版本与 ROS 2 软件包仓库中的版本冲突。

如果 ROS 2 apt 软件源位于可用 apt 软件源列表（``/etc/apt/sources.list.d``）中，就无法安装 ROS 1 软件包。错误如下：

.. code-block:: console

  $ apt install ros-core-dev
  Reading package lists... Done
  Building dependency tree... Done
  Reading state information... Done
  Some packages could not be installed. This may mean that you have
  requested an impossible situation or if you are using the unstable
  distribution that some required packages have not yet been created
  or been moved out of Incoming.
  The following information may help to resolve the situation:

  The following packages have unmet dependencies:
   ros-core-dev : Depends: catkin but it is not installable
  E: Unable to correct problems, you have held broken packages.

要解决此问题，请从软件源列表中移除 ``packages.ros.org``。如果你之前按照 ROS 2 安装指南配置过系统，只需删除 ``/etc/apt/sources.list.d/ros2.list`` 即可。

目前，要支持 ``ros1_bridge``，请按照下面的说明从源码构建 ROS 2。

从源码构建 ROS 2
----------------

在 Ubuntu Jammy 上，只有从源码安装这一种 ROS 2 配置能够正常工作。

下面汇总了源码构建所需的步骤。主要区别在于：由于软件包冲突，我们跳过 ROS 2 apt 软件源，不使用其中的软件包。

安装开发工具和 ROS 工具
^^^^^^^^^^^^^^^^^^^^^^^

由于不使用 ROS 2 apt 软件源，必须通过 ``pip`` 安装 ``colcon``。

.. code-block:: console

   $ sudo apt update && sudo apt install -y \
     build-essential \
     cmake \
     git \
     python3-flake8 \
     python3-flake8-blind-except \
     python3-flake8-builtins \
     python3-flake8-class-newline \
     python3-flake8-comprehensions \
     python3-flake8-deprecated \
     python3-flake8-docstrings \
     python3-flake8-import-order \
     python3-flake8-quotes \
     python3-pip \
     python3-pytest \
     python3-pytest-cov \
     python3-pytest-repeat \
     python3-pytest-rerunfailures \
     python3-rosdep \
     python3-setuptools \
     wget

   # 从 PyPI 安装 colcon，而不是使用 apt 软件包
   python3 -m pip install -U colcon-common-extensions vcstool

从这里开始，继续按照 :doc:`源码安装指南 <../Installation/Alternatives/Ubuntu-Development-Setup>` 构建 ROS 2。

从 Ubuntu 软件包安装 ROS 1
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   $ sudo apt update && sudo apt install -y ros-core-dev

构建 ros1_bridge
^^^^^^^^^^^^^^^^

.. code-block:: console

    $ mkdir -p ~/ros1_bridge/src # 为 ros1_bridge 创建工作空间
    $ cd ~/ros1_bridge/src
    $ git clone https://github.com/ros2/ros1_bridge
    $ cd ~/ros1_bridge
    $ . ~/ros2_humble/install/local_setup.bash # source ROS 2 工作空间
    $ colcon build # 构建

完成 ``ros1_bridge`` 的构建后，`ros1_bridge 示例 <https://github.com/ros2/ros1_bridge#example-1-run-the-bridge-and-the-example-talker-and-listener>`_ 中的其余示例应该可以在新安装环境中正常运行。
