.. _Colcon:

.. redirect-from::

    Colcon-Tutorial
    Tutorials/Colcon-Tutorial

使用 colcon 构建功能包
======================

.. contents:: 目录
   :depth: 2
   :local:

**目标：** 使用 colcon 构建 ROS 2 工作空间。

**教程级别：** 初级

**预计时间：** 20 分钟

本教程简要介绍如何使用 colcon 创建并构建 ROS 2 工作空间。这是一篇实践教程，不能替代核心文档。

背景
----

colcon 是对 ROS 构建工具 catkin_make、catkin_make_isolated、catkin_tools 和 ament_tools 的迭代改进。有关 colcon 的设计，请参阅`构建工具设计文档 <https://design.ros2.org/articles/build_tool.html>`_。

源码位于`colcon GitHub 组织 <https://github.com/colcon>`_。

前置条件
--------

安装 colcon
^^^^^^^^^^^

.. tabs::

  .. group-tab:: Ubuntu

    .. code-block:: console

        $ sudo apt install python3-colcon-common-extensions

  .. group-tab:: RHEL

    .. code-block:: console

        $ sudo dnf install python3-colcon-common-extensions

  .. group-tab:: macOS

    .. code-block:: console

        $ python3 -m pip install colcon-common-extensions

  .. group-tab:: Windows

    .. code-block:: console

        $ pip install -U colcon-common-extensions

安装 ROS 2
^^^^^^^^^^

构建示例需要安装 ROS 2，请按照 :doc:`安装说明 <../../Installation>` 操作。

.. attention::

   如果通过 deb 软件包安装，本教程要求安装 :ref:`桌面版 <linux-install-debs-install-ros-2-packages>`。

基础知识
--------

ROS 工作空间是具有特定目录结构的目录。通常包含一个 src 子目录，ROS 功能包的源代码就放在该目录中。除此之外，工作空间目录通常为空。

colcon 使用源码目录之外的构建方式。默认情况下，它会在 src 目录旁创建以下目录：

* build：保存中间文件。每个功能包都会创建一个子目录，例如 CMake 在其中执行配置和构建。
* install：保存安装后的功能包。默认情况下，每个功能包会安装到独立的子目录。
* log：保存每次 colcon 调用的日志信息。

.. note::

   与 catkin 不同，colcon 没有 devel 目录。

创建工作空间
^^^^^^^^^^^^

首先创建目录 ros2_ws，用于存放工作空间：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ mkdir -p ~/ros2_ws/src
       $ cd ~/ros2_ws

  .. group-tab:: macOS

    .. code-block:: console

       $ mkdir -p ~/ros2_ws/src
       $ cd ~/ros2_ws

  .. group-tab:: Windows

    .. code-block:: console

       $ md \dev\ros2_ws\src
       $ cd \dev\ros2_ws

此时工作空间中只有一个空的 src 目录：

.. code-block:: bash

    .
    └── src

    1 directory, 0 files

添加源码
^^^^^^^^

将 examples 仓库克隆到工作空间的 src 目录：

.. code-block:: console

    $ git clone https://github.com/ros2/examples src/examples -b {REPOS_FILE_BRANCH}

现在工作空间中应该包含 ROS 2 示例源码：

.. code-block:: bash

    .
    └── src
        └── examples
            ├── CONTRIBUTING.md
            ├── LICENSE
            ├── rclcpp
            ├── rclpy
            └── README.md

    4 directories, 3 files

source underlay
^^^^^^^^^^^^^^^

需要先 source 一个已有 ROS 2 安装环境，为工作空间提供示例功能包所需的构建依赖。可以 source 二进制安装或源码安装提供的设置脚本，也可以 source 另一个 colcon 工作空间。

这个环境称为 **underlay（底层工作空间）**。

我们的 ros2_ws 工作空间将作为已有 ROS 2 安装之上的 **overlay（覆盖工作空间）**。通常，如果只打算迭代少量功能包，建议使用 overlay，而不是将所有功能包放在同一个工作空间中。

构建工作空间
^^^^^^^^^^^^

.. attention::

   在 Windows 上构建功能包时，需要处于 Visual Studio 环境中。更多详情请参阅 :ref:`构建 ROS 2 代码 <windows-dev-build-ros2>`。

在工作空间根目录运行 colcon build。由于 ament_cmake 等构建类型不支持 devel space，并要求安装功能包，colcon 提供了 --symlink-install 选项。使用该选项后，可以通过修改 source 目录中的文件（例如 Python 文件或其他非编译资源）来更新安装文件，从而加快迭代速度。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ colcon build --symlink-install

  .. group-tab:: macOS

    .. code-block:: console

      $ colcon build --symlink-install

  .. group-tab:: Windows

    .. code-block:: console

      $ colcon build --merge-install

    Windows 不允许过长路径，因此 merge-install 会将所有路径合并到 install 目录中。Windows 创建符号链接需要特殊权限，所以默认不使用 --symlink-install。若要启用，需要以管理员身份运行命令，或在系统设置中启用开发者模式。

.. tip::

   在 CPU、内存和 I/O 资源受限的系统（例如 Raspberry Pi）上运行 colcon build 可能导致屏幕和鼠标卡顿。可以使用 --executor sequential 参数逐个构建功能包，而不是并行构建。更多参数请参阅`colcon 执行器文档 <https://colcon.readthedocs.io/en/released/reference/executor-arguments.html>`_。

构建完成后，应该看到 build、install 和 log 目录：

.. code-block:: bash

    .
    ├── build
    ├── install
    ├── log
    └── src

    4 directories, 0 files

运行测试
^^^^^^^^

要运行刚才构建的功能包的测试，请执行：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ colcon test

  .. group-tab:: macOS

    .. code-block:: console

      $ colcon test

  .. group-tab:: Windows

    请使用 x64 Native Tools Command Prompt for VS 2019 执行命令：

    .. code-block:: console

      $ colcon test --merge-install

    这里同样需要指定 --merge-install，因为上面构建时使用了该选项。

source 环境
^^^^^^^^^^^

colcon 成功完成构建后，输出文件位于 install 目录中。在使用安装的可执行程序或库之前，需要将它们添加到 PATH 和库搜索路径中。

colcon 会在 install 目录中生成 bash/bat 文件，以帮助配置环境。这些文件会将所需内容添加到 PATH 和库搜索路径，并提供功能包导出的 Shell 命令。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ source install/setup.bash

  .. group-tab:: macOS

    .. code-block:: console

       $ . install/setup.bash

  .. group-tab:: Windows

    在 Windows 命令行中：

    .. code-block:: console

       $ call install\setup.bat

    或在 PowerShell 中：

    .. code-block:: console

       $ install\setup.ps1

尝试运行演示
^^^^^^^^^^^^

source 环境后，就可以运行 colcon 构建的可执行程序。先运行 examples 中的订阅者节点：

.. code-block:: console

    $ ros2 run examples_rclcpp_minimal_subscriber subscriber_member_function

在另一个终端中运行发布者节点（不要忘记 source 设置脚本）：

.. code-block:: console

    $ ros2 run examples_rclcpp_minimal_publisher publisher_member_function

应该能看到发布者和订阅者输出不断递增的数字消息。

创建自己的功能包
----------------

colcon 使用 REP 149 定义的 package.xml 规范（也支持格式 2）。

colcon 支持多种构建类型。推荐的构建类型是 ament_cmake 和 ament_python，也支持纯 CMake 功能包。

ament_python 构建示例可参考`ament_index_python <https://github.com/ament/ament_index/tree/{REPOS_FILE_BRANCH}/ament_index_python>`_，其中 setup.py 是构建入口。

demo_nodes_cpp 等功能包使用 ament_cmake 构建类型，并使用 CMake 作为构建工具。

可以使用 ros2 pkg create 工具，根据模板创建新功能包。有关创建功能包和使用 ros2 pkg create 的完整说明，请参阅 :doc:`创建功能包 <./Creating-Your-First-ROS2-Package>`。

.. note::

   对于 catkin 用户，这相当于 catkin_create_package。

配置 colcon_cd
--------------

colcon_cd 命令可以快速将 Shell 当前工作目录切换到某个功能包目录。例如，执行 colcon_cd some_ros_package，就可以快速进入 ~/ros2_ws/src/some_ros_package。

在 Linux 中，可以运行以下命令修改 Shell 启动脚本：

.. code-block:: console

    $ echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
    $ echo "export _colcon_cd_root=/opt/ros/{DISTRO}/" >> ~/.bashrc

macOS 的路径可能不同，Windows 暂不可用。具体请参阅`colcon_cd 文档 <https://colcon.readthedocs.io/en/released/user/installation.html#quick-directory-changes>`_。

配置 colcon 命令补全
--------------------

colcon 命令支持 bash 及类似 Shell 的命令补全。需要安装 colcon-argcomplete 软件包，并可能需要执行`额外配置 <https://colcon.readthedocs.io/en/released/user/installation.html#enable-completion>`_。

技巧
----

* 如果不希望构建某个功能包，可以在其目录中创建一个名为 COLCON_IGNORE 的空文件，这样 colcon 就不会索引它。
* 如果希望避免配置和构建 CMake 功能包中的测试，可以传入 --cmake-args -DBUILD_TESTING=0。
* 如果只想运行某个功能包中的单个测试：

  .. code-block:: console

     $ colcon test --packages-select YOUR_PKG_NAME --ctest-args -R YOUR_TEST_IN_PKG

配置 colcon mixin
-----------------

一些命令行选项较长，或者不容易记忆。例如，将 CMake 构建类型设置为 debug，通常需要：

.. code-block:: console

    $ colcon build --cmake-args -DCMAKE_BUILD_TYPE=Debug

colcon mixin 仓库提供了常用命令行选项的快捷方式。

安装默认 mixin：

.. code-block:: console

    $ colcon mixin add default https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml
    $ colcon mixin update default

然后尝试使用 debug mixin：

.. code-block:: console

    $ colcon build --mixin debug

更多详情请参阅`colcon mixin 仓库 <https://github.com/colcon/colcon-mixin-repository>`_。
