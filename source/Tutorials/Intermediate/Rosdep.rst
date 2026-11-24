.. redirect-from::

    Tutorials/Rosdep

.. _rosdep documentation:

使用 rosdep 管理依赖项
======================

**目标：** 使用 ``rosdep`` 管理外部依赖项。

**教程级别：** 中级

**预计时间：** 5 分钟

.. contents:: 目录
   :depth: 2
   :local:

本教程介绍如何使用 ``rosdep`` 管理外部依赖项。

.. warning::

   目前 rosdep 仅支持 Linux 和 macOS，不支持 Windows。长期计划是为 rosdep 添加 Windows 支持，参见 `rosdep GitHub 仓库 <https://github.com/ros-infrastructure/rosdep>`_。

什么是 rosdep？
---------------

``rosdep`` 是一种依赖管理工具，可用于处理功能包和外部库。它是一个命令行工具，用于识别并安装构建或安装某个功能包所需的依赖项。

``rosdep`` 本身并不是包管理器，而是一个元包管理器。它根据自身掌握的系统和依赖项信息，为特定平台查找合适的软件包。实际安装由系统包管理器完成，例如 Debian/Ubuntu 上的 ``apt``、Fedora/RHEL 上的 ``dnf`` 等。

它最常在构建工作空间之前调用，用于安装工作空间中各个功能包的依赖项。它既可以处理单个功能包，也可以处理包含多个功能包的目录，例如工作空间。

.. note::

   虽然名称中包含 ROS，但 ``rosdep`` 并非完全依赖 ROS。将其作为独立 Python 软件包安装后，也可以用于非 ROS 软件项目。

关于 package.xml 文件
---------------------

``package.xml`` 是 ``rosdep`` 查找依赖项集合的文件。确保其中的依赖列表完整且正确非常重要，因为所有工具都依靠它确定功能包的依赖关系。

缺失或错误的依赖项可能导致用户无法使用你的功能包、工作空间中的功能包构建顺序错误，或者功能包无法发布。

``package.xml`` 中的依赖项通常称为“rosdep keys”。功能包创建者需要手动填写这些依赖项，并完整列出功能包所需的所有非内置库和功能包。

这些依赖项通过以下标签表示，完整规范请参阅 `REP-149 <https://reps.openrobotics.org/rep-0149/>`_。

<depend>
^^^^^^^^

该标签声明功能包在构建时和运行时都需要的依赖项。对于 C++ 功能包，如果不确定应该使用哪种依赖标签，通常可以使用该标签。纯 Python 功能包一般没有构建阶段，因此通常不应使用它，而应使用 `<exec_depend>`。

<build_depend>
^^^^^^^^^^^^^^

如果某个依赖项只在构建功能包时使用，而运行时不需要，可以使用 `<build_depend>`。这种依赖关系意味着安装后的二进制功能包不需要安装该依赖项。

不过，如果功能包导出的头文件包含了该依赖项中的头文件，就会产生问题。此时还需要添加 `<build_export_depend>`。

<build_export_depend>
^^^^^^^^^^^^^^^^^^^^^

如果功能包导出的头文件包含某个依赖项中的头文件，那么依赖当前功能包的其他功能包在构建时也需要该依赖项。这种情况主要适用于头文件和 CMake 配置文件。被导出库引用的库通常应声明为 `<depend>`，因为它们在运行时也需要。

<exec_depend>
^^^^^^^^^^^^^

该标签声明运行功能包时需要的依赖项，例如共享库、可执行程序、Python 模块、启动脚本和其他运行所需文件。

<test_depend>
^^^^^^^^^^^^^

该标签声明仅测试时需要的依赖项。这里的依赖项不应与 `<build_depend>``、``<exec_depend>`` 或 ``<depend>` 中声明的 key 重复。

rosdep 如何工作？
-----------------

``rosdep`` 会检查指定路径中的 ``package.xml`` 文件，或者检查指定功能包，并找到其中保存的 rosdep keys。

随后，这些 key 会与中央索引交叉查询，以确定不同包管理器中对应的 ROS 软件包或软件库。找到软件包后，就可以安装使用。

``rosdep`` 会将中央索引下载到本地计算机，避免每次运行时都访问网络。在 Debian/Ubuntu 上，其配置通常保存在 ``/etc/ros/rosdep/sources.list.d/20-default.list``。

中央索引称为 ``rosdistro``，可以在`此处 <https://github.com/ros/rosdistro>`_ 查看。

如何确定 package.xml 中应填写哪些 key？
---------------------------------------

如果要依赖的软件包属于 ROS 生态系统，并且已经发布到 ROS 生态系统中 [1]_，例如 ``nav2_bt_navigator``，可以直接使用该软件包名称。

可以在 `rosdistro GitHub 仓库 <https://github.com/ros/rosdistro>`` 对应 ROS 发行版的 ``<distro>/distribution.yaml`` 文件中查看所有已发布 ROS 软件包，例如 Humble 对应 ``humble/distribution.yaml`。

如果要依赖非 ROS 软件包，也就是通常所说的“系统依赖项”，则需要查找特定库对应的 key。通常需要关注两个文件：

* `rosdep/base.yaml <https://github.com/ros/rosdistro/blob/master/rosdep/base.yaml>`_：包含 apt 系统依赖项。
* `rosdep/python.yaml <https://github.com/ros/rosdistro/blob/master/rosdep/python.yaml>`_：包含 Python 依赖项。

在这些文件中搜索所需库，找到对应名称。该名称就是应写入 ``package.xml`` 的 key。

例如，假设某个功能包依赖 ``doxygen``。在 ``rosdep/base.yaml`` 中搜索 ``doxygen``，可以找到如下配置：

.. code-block:: yaml

  doxygen:
    arch: [doxygen]
    debian: [doxygen]
    fedora: [doxygen]
    freebsd: [doxygen]
    gentoo: [app-doc/doxygen]
    macports: [doxygen]
    nixos: [doxygen]
    openembedded: [doxygen@meta-oe]
    opensuse: [doxygen]
    rhel: [doxygen]
    ubuntu: [doxygen]

这意味着 rosdep key 为 ``doxygen``，在不同操作系统上会解析为对应包管理器中的软件包名称。

如果库不在 rosdistro 中怎么办？
-------------------------------

如果库尚未包含在 ``rosdistro`` 中，可以自行添加。``rosdistro`` 的 Pull Request 通常会在一周内合并。

如何贡献新的 rosdep key，请参阅`详细说明 <https://github.com/ros/rosdistro/blob/master/CONTRIBUTING.md#rosdep-rules-contributions>`_。

如果由于某些原因不能公开贡献，还可以选择：

1. Fork rosdistro 并维护包含额外 key 的替代索引，参见 :doc:`使用自定义 rosdistro <../../How-To-Guides/Using-Custom-Rosdistro>`。
2. 创建包含自定义 key 的新文件，并在填充本地索引时要求 ``rosdep`` 检查该文件，参见 :doc:`补充自定义 rosdep keys <../Advanced/Supplementing-Custom-Rosdep-Keys>`。

如何使用 rosdep 工具？
----------------------

安装 rosdep
^^^^^^^^^^^

如果在 ROS 环境中使用 ``rosdep``，它通常随 ROS 发行版一起提供。这是推荐的安装方式。

.. tabs::

  .. group-tab:: Ubuntu

    .. code-block:: console

        $ sudo apt install python3-rosdep

  .. group-tab:: RHEL

    .. code-block:: console

        $ sudo dnf install python3-rosdep

.. note::

    Debian 和 Ubuntu 中还有一个名称相似的软件包 ``python3-rosdep2``。如果已安装该软件包，请先将其卸载，再安装 ``python3-rosdep``。

如果在 ROS 之外使用 ``rosdep``，系统包管理器可能没有提供相应软件包。这种情况下，可以直接从 PyPI 安装：

.. code-block:: console

    $ pip install rosdep

运行 rosdep
^^^^^^^^^^^

首次使用 ``rosdep`` 时，必须先初始化：

.. code-block:: console

    $ sudo rosdep init
    $ rosdep update

这会初始化 rosdep，并通过 ``update`` 更新本地缓存的 rosdistro 索引。建议定期运行 ``rosdep update``，以获取最新索引。

最后，运行 ``rosdep install`` 安装依赖项。通常会在包含多个功能包的工作空间中一次性运行该命令。如果当前位于工作空间根目录，且源代码位于 ``src`` 目录中，可以执行：

.. code-block:: console

    $ rosdep install --from-paths src -y --ignore-src

参数说明：

* ``--from-paths src``：指定需要检查 ``package.xml`` 文件并解析依赖 key 的路径。
* ``-y``：对包管理器的所有安装提示默认回答 yes，无需交互。
* ``--ignore-src``：如果某个 rosdep key 对应的功能包已经存在于当前工作空间中，则忽略该依赖，不再安装。

还有其他参数和选项。运行 ``rosdep -h`` 查看帮助，或阅读更完整的 `rosdep 文档 <http://docs.ros.org/en/independent/api/rosdep/html/>`_。

.. [1] “发布到 ROS 生态系统”是指该软件包列在 ``rosdistro`` 数据库中的一个或多个 `<distro>/distribution.yaml`` 文件中，参见 ``rosdistro 数据库 <https://github.com/ros/rosdistro>`_。
