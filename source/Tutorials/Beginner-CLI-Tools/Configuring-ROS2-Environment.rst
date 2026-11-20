.. redirect-from::

    Tutorials/Configuring-ROS2-Environment

配置环境
========

**目标：** 本教程将介绍如何准备 ROS 2 环境。

**教程级别：** 初学者

**预计时间：** 5 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景知识
--------

ROS 2 依赖 Shell 环境来组合多个工作空间。工作空间（Workspace）是 ROS 中的一个术语，指你在系统中进行 ROS 2 开发的位置。

在典型的 ROS 2 环境中，ROS 2 核心安装目录称为底层工作空间（underlay）。在该安装环境之后加载的本地工作空间称为覆盖工作空间（overlay），因为它叠加在底层工作空间之上。同一个工作空间也可以作为另一个稍后加载的工作空间的底层工作空间。在 ROS 2 开发过程中，通常会同时启用多个工作空间。

组合工作空间可以更方便地针对不同 ROS 2 版本或不同功能包集合进行开发，也允许在同一台计算机上安装多个 ROS 2 发行版（例如 Dashing 和 Eloquent），并在它们之间切换。

实现方式是在每次打开新 Shell 时加载相应的环境设置文件，或者只需一次将 source 命令添加到 Shell 启动脚本中。如果不加载环境设置文件，就无法访问 ROS 2 命令，也无法查找或使用 ROS 2 功能包。换句话说，你将无法使用 ROS 2。

前置条件
--------

开始本系列教程之前，请按照 ROS 2 :doc:`安装页面 <../../Installation>` 中的说明安装 ROS 2。

本教程中的命令假设你按照操作系统对应的二进制软件包安装指南完成了安装（Linux 使用 deb 软件包）。如果你从源码构建 ROS 2，仍然可以跟随本教程操作，但环境设置文件的路径可能不同。此外，如果采用源码安装方式，也无法使用初学者教程中经常出现的 ``sudo apt install ros-<distro>-<package>`` 命令。

如果你使用 Linux 或 macOS，但还不熟悉 Shell，可以参考 `Bash 命令行入门教程 <https://www.linux.com/training-tutorials/bash-101-working-cli/>`__。

任务
----

1 加载环境设置文件
^^^^^^^^^^^^^^^^^^

每次打开新的 Shell，都需要运行以下命令，才能使用 ROS 2 命令：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        $ source /opt/ros/{DISTRO}/setup.bash

      如果使用的不是 bash，请将 ``.bash`` 替换为对应 Shell 的后缀。可选文件包括：``setup.bash``、``setup.sh`` 和 ``setup.zsh``。

   .. group-tab:: macOS

      .. code-block:: console

        $ . ~/ros2_install/ros2-osx/setup.bash

   .. group-tab:: Windows

      .. code-block:: console

        $ call C:\dev\ros2\local_setup.bat

.. note::

   具体命令取决于 ROS 2 的安装位置。如果遇到问题，请确认文件路径确实指向你的 ROS 2 安装目录。

2 将环境加载命令添加到 Shell 启动脚本
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果不希望每次打开新 Shell 都手动加载环境设置文件（即跳过任务 1），可以将 source 命令添加到 Shell 启动脚本中：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        $ echo "source /opt/ros/{DISTRO}/setup.bash" >> ~/.bashrc

      如果需要撤销此设置，请找到系统的 Shell 启动脚本，并删除追加的 source 命令。

   .. group-tab:: macOS

      .. code-block:: console

        $ echo "source ~/ros2_install/ros2-osx/setup.bash" >> ~/.bash_profile

      如果需要撤销此设置，请找到系统的 Shell 启动脚本，并删除追加的 source 命令。

   .. group-tab:: Windows

      仅适用于 PowerShell 用户：在“我的文档”目录中创建一个名为 ``WindowsPowerShell`` 的文件夹。

      在 ``WindowsPowerShell`` 文件夹中创建文件 ``Microsoft.PowerShell_profile.ps1``，并在文件中粘贴以下内容：

      .. code-block:: console

        $ C:\dev\ros2_{DISTRO}\local_setup.ps1

      每次打开新的 Shell 时，PowerShell 都会请求运行该脚本的权限。要避免这一问题，可以运行：

      .. code-block:: console

        $ Unblock-File C:\dev\ros2_{DISTRO}\local_setup.ps1

      如果需要撤销此设置，请删除新建的 ``Microsoft.PowerShell_profile.ps1`` 文件。

3 检查环境变量
^^^^^^^^^^^^^^

加载 ROS 2 环境设置文件时，会设置运行 ROS 2 所需的多个环境变量。如果你在查找或使用 ROS 2 功能包时遇到问题，请使用以下命令检查环境配置是否正确：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        $ printenv | grep -i ROS

   .. group-tab:: macOS

      .. code-block:: console

        $ printenv | grep -i ROS

   .. group-tab:: Windows

      .. code-block:: console

        $ set | findstr -i ROS

检查 ``ROS_DISTRO`` 和 ``ROS_VERSION`` 等变量是否已经设置。

::

  ROS_VERSION=2
  ROS_PYTHON_VERSION=3
  ROS_DISTRO={DISTRO}

如果环境变量设置不正确，请返回你所使用的安装指南中的 ROS 2 软件包安装部分。如果需要更具体的帮助（因为环境设置文件可能来自不同位置），可以在社区 `获取解答 <https://robotics.stackexchange.com/>`__。

3.1 ``ROS_DOMAIN_ID`` 变量
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

有关 ROS 域 ID 的详细信息，请参阅 `域 ID 说明 <../../Concepts/Intermediate/About-Domain-ID>`。

为 ROS 2 节点组确定一个唯一整数后，可以使用以下命令设置环境变量：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        $ export ROS_DOMAIN_ID=<your_domain_id>

      如果希望在不同 Shell 会话之间保留该设置，可以将命令添加到 Shell 启动脚本中：

      .. code-block:: console

        $ echo "export ROS_DOMAIN_ID=<your_domain_id>" >> ~/.bashrc

   .. group-tab:: macOS

      .. code-block:: console

        $ export ROS_DOMAIN_ID=<your_domain_id>

      如果希望在不同 Shell 会话之间保留该设置，可以将命令添加到 Shell 启动脚本中：

      .. code-block:: console

        $ echo "export ROS_DOMAIN_ID=<your_domain_id>" >> ~/.bash_profile

   .. group-tab:: Windows

      .. code-block:: console

        $ set ROS_DOMAIN_ID=<your_domain_id>

      如果希望该设置在不同 Shell 会话之间永久生效，还需要运行：

      .. code-block:: console

        $ setx ROS_DOMAIN_ID <your_domain_id>

3.2 ``ROS_LOCALHOST_ONLY`` 变量
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

默认情况下，ROS 2 通信并不局限于 localhost。

``ROS_LOCALHOST_ONLY`` 环境变量允许你将 ROS 2 通信限制在本机范围内。这意味着其他局域网计算机将无法看到你的 ROS 2 系统及其话题、服务和动作。

在某些场景中，使用 ``ROS_LOCALHOST_ONLY`` 很有帮助，例如在教室中，多台机器人可能会向同一个话题发布消息，从而引发异常行为。可以使用以下命令设置该环境变量：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        export ROS_LOCALHOST_ONLY=1

      如果希望在不同 Shell 会话之间保留该设置，可以将命令添加到 Shell 启动脚本中：

      .. code-block:: console

        echo "export ROS_LOCALHOST_ONLY=1" >> ~/.bashrc

   .. group-tab:: macOS

      .. code-block:: console

        export ROS_LOCALHOST_ONLY=1

      如果希望在不同 Shell 会话之间保留该设置，可以将命令添加到 Shell 启动脚本中：

      .. code-block:: console

        echo "export ROS_LOCALHOST_ONLY=1" >> ~/.bash_profile

   .. group-tab:: Windows

      .. code-block:: console

        set ROS_LOCALHOST_ONLY=1

      如果希望在不同 Shell 会话之间永久保留该设置，还需要运行：

      .. code-block:: console

        setx ROS_LOCALHOST_ONLY 1

总结
----

使用 ROS 2 之前，必须正确配置 ROS 2 开发环境。可以通过两种方式完成：每次打开新 Shell 时加载环境设置文件，或者将 source 命令添加到 Shell 启动脚本中。

如果使用 ROS 2 时遇到无法定位或使用功能包的问题，首先应检查环境变量，确保它们指向预期的 ROS 版本和发行版。

下一步
------

现在你已经拥有可正常工作的 ROS 2 安装环境，并且了解如何加载环境设置文件，可以开始使用 :doc:`turtlesim 工具 <./Introducing-Turtlesim/Introducing-Turtlesim>` 学习 ROS 2 的各项功能。
