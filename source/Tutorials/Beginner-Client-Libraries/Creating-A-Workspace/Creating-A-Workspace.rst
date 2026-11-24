.. redirect-from::

    Tutorials/Workspace/Creating-A-Workspace

.. _ROS2Workspace:

创建工作空间
============

**目标：** 创建工作空间，并学习如何设置用于开发和测试的 overlay。

**教程级别：** 初级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

工作空间是一个包含 ROS 2 功能包的目录。使用 ROS 2 之前，需要在准备工作的终端中 source ROS 2 安装工作空间，这样该终端就可以使用 ROS 2 的功能包。

你还可以 source 一个 overlay（覆盖工作空间），它是一个次级工作空间，可以在不影响现有 ROS 2 工作空间（underlay，底层工作空间）的情况下添加新功能包。underlay 必须包含 overlay 中所有功能包的依赖项。overlay 中的功能包会覆盖 underlay 中的同名功能包。

也可以创建多层 underlay 和 overlay，每一层 overlay 都可以使用其父级 underlay 中的功能包。

前置条件
--------

* :doc:`ROS 2 安装 <../../../Installation>`
* :doc:`colcon 安装 <../Colcon-Tutorial>`
* `git 安装 <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_
* :doc:`turtlesim 安装 <../../Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim>`
* :doc:`安装 rosdep <../../Intermediate/Rosdep>`
* 了解基本终端命令。
* 选择一个文本编辑器。

任务
----

1. source ROS 2 环境
^^^^^^^^^^^^^^^^^^^^

本教程中，主要 ROS 2 安装将作为 underlay。注意，underlay 不一定必须是主要 ROS 2 安装。

根据 ROS 2 的安装方式和所使用的平台，source 命令会有所不同：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        $ source /opt/ros/{DISTRO}/setup.bash

   .. group-tab:: macOS

      .. code-block:: console

        $ . ~/ros2_install/ros2-osx/setup.bash

   .. group-tab:: Windows

      运行以下命令时，请使用 x64 Native Tools Command Prompt for VS 2019，因为后续需要构建工作空间。

      .. code-block:: console

        $ call C:\dev\ros2\local_setup.bat

如果命令无法运行，请参考你所使用的 :doc:`安装指南 <../../../Installation>`。

.. _new-directory:

2. 创建新目录
^^^^^^^^^^^^^

最佳实践是为每个新工作空间创建一个新目录。目录名称可以自定义，但最好能体现工作空间用途。本教程使用 ros2_ws，表示开发工作空间：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        $ mkdir -p ~/ros2_ws/src
        $ cd ~/ros2_ws/src

   .. group-tab:: macOS

      .. code-block:: console

        $ mkdir -p ~/ros2_ws/src
        $ cd ~/ros2_ws/src

   .. group-tab:: Windows

      .. code-block:: console

        $ md \ros2_ws\src
        $ cd \ros2_ws\src

另一个最佳实践是将工作空间中的所有功能包放在 src 目录中。上面的命令会在 ros2_ws 中创建 src 目录并进入该目录。

3. 克隆示例仓库
^^^^^^^^^^^^^^^

克隆之前，请确保当前目录仍然是 ros2_ws/src。

在后续初级开发者教程中，你将创建自己的功能包。现在先练习使用已有功能包搭建工作空间。

如果已经完成“初级：CLI 工具”教程，就会熟悉 ros_tutorials 仓库中的 turtlesim 功能包。

仓库可能包含多个分支，需要检出与你安装的 ROS 2 发行版对应的分支。克隆时使用 -b 参数指定分支：

.. code-block:: console

  $ git clone https://github.com/ros/ros_tutorials.git -b {DISTRO}

现在 ros_tutorials 已经克隆到工作空间中。该仓库包含 turtlesim 功能包，后续教程会使用它。仓库中的其他功能包包含 COLCON_IGNORE 文件，因此不会被构建。

目前工作空间中已有示例功能包，但还不是完整可用的工作空间。需要先解决依赖项，然后构建工作空间。

4. 解决依赖项
^^^^^^^^^^^^^

构建工作空间之前，需要解决功能包依赖。即使可能已经安装了所有依赖项，最佳实践仍然是在每次克隆后检查依赖，以免构建耗时很久后才发现缺少依赖。

在工作空间根目录 ros2_ws 中运行：

.. tabs::

   .. group-tab:: Linux

      如果当前仍在 src 目录，请先运行 cd .. 返回工作空间根目录。

      .. code-block:: console

        $ cd ..
        $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

   .. group-tab:: macOS

      rosdep 仅在 Linux 上运行，可以跳到“使用 colcon 构建工作空间”一节。

   .. group-tab:: Windows

      rosdep 仅在 Linux 上运行，可以跳到“使用 colcon 构建工作空间”一节。

如果在 Linux 上通过源码或二进制归档包安装 ROS 2，需要使用相应安装指南中的 rosdep 命令。

如果已经具备全部依赖项，终端会返回：

.. code-block:: text

  #All required rosdeps installed successfully

功能包会在 package.xml 文件中声明依赖项。该命令会遍历这些声明，并安装缺少的依赖项。

5. 使用 colcon 构建工作空间
^^^^^^^^^^^^^^^^^^^^^^^^^^^

现在可以在工作空间根目录 ros2_ws 中运行以下命令构建功能包：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ colcon build

  .. group-tab:: macOS

    .. code-block:: console

      $ colcon build

  .. group-tab:: Windows

    .. code-block:: console

      $ colcon build --merge-install

    Windows 不允许过长路径，因此 merge-install 会将所有路径合并到 install 目录中。

.. note::

  colcon build 的其他常用参数：

  * --packages-up-to：构建指定功能包及其所有依赖项，而不是整个工作空间。
  * --symlink-install：修改 Python 脚本后，无需每次都重新构建。
  * --event-handlers console_direct+：构建时直接显示控制台输出。
  * --executor sequential：逐个处理功能包，而不是并行构建。

构建完成后，工作空间根目录中会出现以下目录：

.. code-block:: console

  $ ls
  build  install  log  src

install 目录中包含工作空间的环境设置文件，可用于 source overlay。

6. source overlay
^^^^^^^^^^^^^^^^^

source overlay 之前，非常重要的一点是：请打开一个新终端，不要在构建工作空间的同一个终端中 source overlay。在同一终端中 source overlay 后再构建，或在已 source overlay 的终端中构建，都可能产生复杂问题。

在新终端中，先 source 主 ROS 2 环境作为 underlay：

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        $ source /opt/ros/{DISTRO}/setup.bash

   .. group-tab:: macOS

      .. code-block:: console

        $ . ~/ros2_install/ros2-osx/setup.bash

   .. group-tab:: Windows

      .. code-block:: console

        $ call C:\dev\ros2\local_setup.bat

进入工作空间根目录：

.. code-block:: console

   $ cd ~/ros2_ws

然后 source overlay：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ source install/local_setup.bash

  .. group-tab:: macOS

    .. code-block:: console

      $ . install/local_setup.bash

  .. group-tab:: Windows

    .. code-block:: console

      $ call install\setup.bat

.. note::

  source overlay 的 local_setup 只会将 overlay 中的功能包添加到环境中。setup 则会同时 source overlay 及其创建时所依赖的 underlay。

  因此，先 source 主 ROS 2 安装的 setup，再 source ros2_ws overlay 的 local_setup，与直接 source ros2_ws 的 setup 效果相同。

现在可以从 overlay 运行 turtlesim：

.. code-block:: console

  $ ros2 run turtlesim turtlesim_node

如何确认运行的是 overlay 中的 turtlesim，而不是主安装中的版本？

7. 修改 overlay
^^^^^^^^^^^^^^^

可以通过修改 turtlesim 窗口标题栏来验证 overlay。找到文件 ~/ros2_ws/src/ros_tutorials/turtlesim/src/turtle_frame.cpp，并使用文本编辑器打开。

找到 setWindowTitle("TurtleSim");，将 "TurtleSim" 改为 "MyTurtleSim"，然后保存。

回到之前运行 colcon build 的第一个终端，再次执行构建。

然后回到 source 了 overlay 的第二个终端，再次运行 turtlesim：

.. code-block:: console

  $ ros2 run turtlesim turtlesim_node

此时 turtlesim 窗口标题栏会显示 MyTurtleSim。

.. image:: images/overlay.png

尽管此前已经 source 了主 ROS 2 环境，但 ros2_ws overlay 的优先级高于 underlay。

为了确认 underlay 仍然完好，可以打开一个全新终端，只 source ROS 2 主安装，然后再次运行 turtlesim：

.. code-block:: console

  $ ros2 run turtlesim turtlesim_node

.. image:: images/underlay.png

可以看到，overlay 中的修改并没有影响 underlay。

总结
----

本教程中，你将主 ROS 2 发行版安装作为 underlay，并通过在新工作空间中克隆和构建功能包创建 overlay。overlay 会被添加到路径前面，因此优先级高于 underlay。

如果只处理少量功能包，建议使用 overlay，这样无需将所有功能包放在同一个工作空间中，也不必每次迭代都重新构建庞大的工作空间。

下一步
------

现在已经了解如何创建、构建和 source 自己的工作空间，接下来可以学习 :doc:`创建自己的功能包 <../Creating-Your-First-ROS2-Package>`。
