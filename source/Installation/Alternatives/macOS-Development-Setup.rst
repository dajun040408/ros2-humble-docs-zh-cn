.. _macOS-latest:

macOS（源码安装）
=================

.. contents:: 目录
   :depth: 2
   :local:

系统要求
--------

目前支持 macOS Mojave（10.14）。

安装前置依赖
------------

构建 ROS 2 需要安装以下工具。

1. **Xcode**

   * 如果尚未安装，请安装 `Xcode <https://apps.apple.com/app/xcode/id497799835>`_。
   * 注意：macOS Mojave 无法安装高于 11.3.1 的 Xcode 版本，因此需要手动安装较旧版本。参见 `相关说明 <https://stackoverflow.com/a/61046761>`_。
   * 如果尚未安装命令行工具，也需要安装：

     .. code-block:: console

        $ xcode-select --install
        $ sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer

   .. note::

      如果手动安装了 Xcode.app，需要接受 Xcode.app 许可证。可以打开 Xcode.app，或运行：

      .. code-block:: console

         $ sudo xcodebuild -license

2. ``brew`` （用于安装其他依赖项；通常已经安装）

   * 按照 `Homebrew 安装说明 <http://brew.sh/>`_ 操作。
   * 可选：运行以下命令，检查 brew 的系统配置是否正常：

     .. code-block:: console

        $ brew doctor

     根据提示修复发现的问题。

3. 使用 `brew` 安装其他依赖项：

   .. code-block:: console

      $ brew install asio assimp bison bullet cmake console_bridge cppcheck \
         cunit eigen freetype graphviz opencv openssl orocos-kdl pcre poco \
         pyqt@5 python qt@5 sip spdlog osrf/simulation/tinyxml1 tinyxml2

4. 配置部分环境变量：

   .. code-block:: console

      # 添加 DDS-Security 所需的 openssl 目录
      # 如果使用 BASH，请将 .zshrc 替换为 .bashrc
      $ echo "export OPENSSL_ROOT_DIR=$(brew --prefix openssl)" >> ~/.zshrc

      # 将 Qt 目录添加到 PATH 和 CMAKE_PREFIX_PATH
      $ export CMAKE_PREFIX_PATH=$CMAKE_PREFIX_PATH:$(brew --prefix qt@5)
      $ export PATH=$PATH:$(brew --prefix qt@5)/bin

5. 使用 `python3 -m pip` 安装其他依赖项。直接使用 `pip` 可能安装 Python 3 或 Python 2，因此建议显式使用 Python 3：

   .. code-block:: console

      $ python3 -m pip install --upgrade pip

      $ python3 -m pip install -U \
        --config-settings="--global-option=build_ext" \
        --config-settings="--global-option=-I$(brew --prefix graphviz)/include/" \
        --config-settings="--global-option=-L$(brew --prefix graphviz)/lib/" \
        argcomplete catkin_pkg colcon-common-extensions coverage \
        cryptography empy flake8 flake8-blind-except==0.1.1 flake8-builtins \
        flake8-class-newline flake8-comprehensions flake8-deprecated \
        flake8-docstrings flake8-import-order flake8-quotes \
        importlib-metadata lark==1.1.1 lxml matplotlib mock mypy==0.931 netifaces \
        nose pep8 psutil pydocstyle pydot pygraphviz pyparsing==2.4.7 \
        pytest-mock rosdep rosdistro setuptools==59.6.0 vcstool

   请确保 `PATH` 环境变量包含二进制文件的安装位置（`$(brew --prefix)/bin`）。

6. **可选：** 如果希望构建 ROS 1 与 ROS 2 桥接程序，还必须安装 ROS 1。

   * 首先按照 `ROS 1 常规安装说明 <http://wiki.ros.org/kinetic/Installation/OSX/Homebrew/Source>`_ 操作。
   * 执行 `rosinstall_generator` 获取源码时，可以使用以下命令，仅获取构建可用桥接程序所需的最少依赖项：

     .. code-block:: console

        $ rosinstall_generator catkin common_msgs roscpp rosmsg --rosdistro kinetic --deps --wet-only --tar > kinetic-ros2-bridge-deps.rosinstall
        $ wstool init -j8 src kinetic-ros2-bridge-deps.rosinstall

   否则，按照常规说明完成安装，然后在继续构建 ROS 2 之前，source 生成的 `install_isolated/setup.bash`。

禁用 System Integrity Protection（SIP）
---------------------------------------

macOS/OS X 10.11 及更高版本默认启用了 System Integrity Protection。

为了避免 SIP 阻止进程继承动态链接器环境变量（例如 `DYLD_LIBRARY_PATH`），需要按照 `Apple 官方说明 <https://developer.apple.com/library/content/documentation/Security/Conceptual/System_Integrity_Protection_Guide/ConfiguringSystemIntegrityProtection/ConfiguringSystemIntegrityProtection.html>`_ 禁用 SIP。

获取 ROS 2 源码
---------------

创建工作空间并克隆所有仓库：

.. code-block:: console

   $ mkdir -p ~/ros2_{DISTRO}/src
   $ cd ~/ros2_{DISTRO}
   $ vcs import --input https://raw.githubusercontent.com/ros2/ros2/{REPOS_FILE_BRANCH}/ros2.repos src

安装其他 DDS 供应商实现（可选）
-------------------------------

如果希望使用默认实现之外的 DDS 或 RTPS 供应商，请参阅 :doc:`此处的说明 <../RMW-Implementations>`。

构建 ROS 2 源码
---------------

运行 `colcon` 构建所有内容。有关 `colcon` 的更多信息，请参阅 :doc:`相关教程 <../../Tutorials/Beginner-Client-Libraries/Colcon-Tutorial>`。

.. code-block:: console

   $ cd ~/ros2_{DISTRO}/
   $ colcon build --symlink-install --packages-skip-by-dep python_qt_binding

注意：由于 SIP、Qt@5 和 PyQt5 存在尚未解决的问题，需要跳过 `python_qt_binding`，才能成功完成构建。问题解决后即可移除这一限制，参见 `相关 Issue <https://github.com/ros-visualization/python_qt_binding/issues/103>`_。

环境配置
--------

source ROS 2 环境设置文件：

.. code-block:: console

   $ . ~/ros2_{DISTRO}/install/setup.zsh

该操作会自动配置构建时支持的 DDS 供应商环境。

尝试示例
--------

在一个终端中，按照前面的说明配置 ROS 2 环境，然后运行 C++ `talker`：

.. code-block:: console

   $ ros2 run demo_nodes_cpp talker

在另一个终端中 source 环境设置文件，然后运行 Python `listener`：

.. code-block:: console

   $ ros2 run demo_nodes_py listener

你应该能看到 `talker` 输出正在 `Publishing` 消息，而 `listener` 输出 `I heard` 并显示收到的消息。这说明 C++ 和 Python API 均能正常工作。

安装后的后续步骤
----------------

继续阅读 :doc:`教程和演示 <../../Tutorials>`，配置环境、创建自己的工作空间和功能包，并学习 ROS 2 核心概念。

使用 ROS 1 桥接
---------------

ROS 1 bridge 可以连接 ROS 1 到 ROS 2 的话题，反之亦然。有关如何构建和使用 ROS 1 bridge，请参阅`专门的文档 <https://github.com/ros2/ros1_bridge/blob/master/README.md>`_。

其他 RMW 实现（可选）
---------------------

ROS 2 默认使用的中间件是 `Fast DDS`，但可以在运行时替换中间件（RMW）。有关如何使用多个 RMW 的说明，请参阅 :doc:`多 RMW 使用指南 <../../How-To-Guides/Working-with-multiple-RMW-implementations>`。

保持源码为最新状态
------------------

请参阅 :doc:`维护源码检出 <../Maintaining-a-Source-Checkout>`，了解如何定期更新源码安装。

故障排查
--------

故障排查方法请参阅 :ref:`此处 <macOS-troubleshooting>`。

卸载
----

1. 如果按照上文说明使用 colcon 安装工作空间，“卸载”可能只需要打开一个新终端，不再 source 工作空间的 `setup` 文件。这样，环境就会表现得如同系统中没有安装 {DISTRO_TITLE} 一样。

2. 如果还希望释放磁盘空间，可以删除整个工作空间目录：

   .. code-block:: console

      $ rm -rf ~/ros2_{DISTRO}
