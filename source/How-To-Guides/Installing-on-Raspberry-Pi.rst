在 Raspberry Pi 上运行 ROS 2
==============================

ROS 2 同时支持 32 位（arm32）和 64 位（arm64）ARM 处理器。不过，参见 `REP-2000 <https://reps.openrobotics.org/rep-2000/>`_ 可知，arm64 获得 Tier 1 支持，而 arm32 属于 Tier 3。Tier 1 表示提供特定发行版的软件包和二进制归档；Tier 3 则要求用户从源码编译 ROS 2。

使用 ROS 2 最快、最简单的方式是选择 Tier 1 支持的配置。这意味着可以在 Raspberry Pi 上安装 64 位 Ubuntu，或者使用 64 位 Raspberry Pi OS 并在 Docker 中运行 ROS 2。

在 Raspberry Pi 上使用 Ubuntu Linux 安装 ROS 2 二进制包
-------------------------------------------------------

可以从 `Ubuntu for Raspberry Pi <https://ubuntu.com/download/raspberry-pi>`_ 下载 Ubuntu。请按照 `REP-2000 <https://reps.openrobotics.org/rep-2000/>`_ 中的说明，确认选择了正确的版本。

之后即可按照 Ubuntu Linux 的常规二进制安装说明安装 ROS 2。

在 Raspberry Pi OS 上通过 Docker 运行 ROS 2
-------------------------------------------

64 位 Raspberry Pi OS 可从 `此处 <https://www.raspberrypi.com/software/operating-systems/>`_ 获取。

Raspberry Pi OS 基于 Debian，属于 Tier 3 支持平台，但它可以运行 Ubuntu Docker 容器，从而使用 Tier 1 支持环境。

刷写操作系统后，请 `安装 Docker <https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script>`_。

官方 ROS 2 Docker 镜像可在 `Docker Hub <https://hub.docker.com/_/ros/tags>`_ 找到。你可以选择 ros-core、ros-base 或 perception 变体。有关这些变体的更多信息，请参阅 `REP-2001 <https://reps.openrobotics.org/rep-2001/>`_。

拉取并运行镜像：

.. code-block:: console

    $ docker pull ros:{DISTRO}-ros-core
    $ docker run -it --rm ros:{DISTRO}-ros-core

你也可以自行构建镜像：

将 ``docker_images`` Git 仓库（``https://github.com/osrf/docker_images``）克隆到 Raspberry Pi 上，进入相应目录，再进入你所选择的变体目录。

在该目录中，运行以下命令构建容器：

.. code-block:: console

    $ docker build -t ros_docker .

在受支持的系统上，构建 Docker 容器只需一两分钟，因为源码已经预先构建为二进制文件。
