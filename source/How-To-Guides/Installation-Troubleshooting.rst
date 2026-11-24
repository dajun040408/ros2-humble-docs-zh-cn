.. redirect-from::

  Guides/Installation-Troubleshooting
  Troubleshooting/Installation-Troubleshooting

安装故障排查
============

安装故障排查方法按照适用平台分类。

.. contents:: 平台
   :depth: 2
   :local:

通用问题
--------

以下方法适用于所有平台。

启用组播
^^^^^^^^

要通过 DDS 成功通信，所使用的网络接口必须启用组播。根据以往经验，在 Ubuntu 或 macOS 上使用回环网络适配器时，组播功能不一定默认启用。

相关讨论请参阅 `原始 Issue <https://github.com/ros2/ros2/issues/552>`_ 或 `ros-answers 讨论 <https://answers.ros.org/question/300370/ros2-talker-cannot-communicate-with-listener/>`_。

可以使用 ROS 2 工具验证当前配置是否允许组播。

终端 1：

.. code-block:: console

   $ ros2 multicast receive

终端 2：

.. code-block:: console

   $ ros2 multicast send

如果第一个命令没有返回类似以下内容：

.. code-block:: bash

   Received from xx.xxx.xxx.xx:43751: 'Hello World!'

可以使用 `ifconfig` 检查网络接口是否启用了组播标志。在 flags 部分查找 `MULTICAST`：

.. code-block:: bash

   eno1: flags=4163<...,MULTICAST>
      ...

系统中存在库文件，但导入仍然失败
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

有时，由于找不到预期的 C 扩展库，`rclpy` 会导入失败。

此时，可以将目录中实际存在的库文件与错误信息中提到的文件进行比较。如果存在名称相似的文件（例如具有相同的 `_rclpy.` 前缀和 `.so` 后缀，但 Python 版本或体系结构不同），说明当前使用的 Python 解释器与构建 C 扩展时使用的解释器不同。

请确保使用构建二进制扩展时所使用的同一个 Python 解释器。操作系统更新后可能出现这种不匹配，重新构建工作空间或许可以解决问题。

.. _linux-troubleshooting:

Linux
-----

编译器内部错误
^^^^^^^^^^^^^^

如果在 Raspberry Pi 等内存受限的平台上编译时遇到 ICE（Internal Compiler Error），可以尝试单线程构建：

.. code-block:: console

   $ MAKEFLAGS=-j1 colcon build

内存不足
^^^^^^^^

当前版本的 `ros1_bridge` 编译需要 4 GB 可用内存。如果没有这么多内存，建议在该目录中创建 `COLCON_IGNORE` 文件，跳过它的编译。

多个主机相互干扰
^^^^^^^^^^^^^^^^

如果同一网络中运行多个 ROS 2 实例，可能会产生相互干扰。可以将环境变量 `ROS_DOMAIN_ID` 设置为不同整数，以避免这种情况。默认值为 0，该变量用于定义系统的 DDS Domain ID。

source setup.bash 时出现异常
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. only relevant to Eloquent and Foxy

如果从源码构建后，source 环境时出现异常，可以尝试升级 colcon 相关软件包：

.. code-block:: console

   $ colcon version-check
   $ sudo apt install python3-colcon* --only-upgrade

混用 conda 和 apt 导致 Python 冲突
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 ROS 2 环境中，混合使用通过 `apt` 安装的软件包和通过 `conda` 安装的软件包可能无法正常工作。

如果使用 ROS 2 官方 apt 二进制包，请确保 `PATH` 环境变量中没有 conda 路径。可能需要检查 `.bashrc` 并注释掉相关配置。

Windows 上的 ROS 2 官方安装流程通过 pixi 包管理器使用 conda 软件包，这种方式可以正常工作，因为没有混用不同包管理器。

社区维护的 `RoboStack <https://robostack.github.io/>`_ 项目等可能会构建 ROS 2 conda 软件包，但 ROS 2 官方不提供 conda 软件包。

防火墙阻止组播
^^^^^^^^^^^^^^

如果组播测试失败，可能需要更新防火墙配置，允许组播通信。可以使用 `ufw <https://help.ubuntu.com/community/UFW>`_：

.. code-block:: console

   $ sudo ufw allow in proto udp to 224.0.0.0/4
   $ sudo ufw allow in proto udp from 224.0.0.0/4

.. _macOS-troubleshooting:

macOS
-----

使用 pyenv 时发生段错误
^^^^^^^^^^^^^^^^^^^^^^^^

`pyenv` 似乎默认使用 `.a` 文件构建 Python，这可能导致 `rclpy` 出现问题。因此，在 macOS 上使用 pyenv 时，建议启用 Frameworks 支持来构建 Python：

`pyenv：如何构建支持 Framework 的 CPython <https://github.com/pyenv/pyenv/wiki#how-to-build-cpython-with-framework-support-on-os-x>`_。

Library not loaded；找不到 image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果运行测试或节点时出现运行时库加载问题，例如：

.. code-block:: bash

   ImportError: dlopen(.../rclpy/_rclpy.cpython-37m-darwin.so, 2): Library not loaded: @rpath/librcl_interfaces__rosidl_typesupport_c.dylib
     Reason: image not found

那么系统可能启用了 System Integrity Protection（SIP）。请按照 `Apple 官方说明 <https://developer.apple.com/library/content/documentation/Security/Conceptual/System_Integrity_Protection_Guide/ConfiguringSystemIntegrityProtection/ConfiguringSystemIntegrityProtection.html>`_ 操作，禁用 SIP。

Qt 构建错误：unknown type name 'Q_ENUM'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果遇到 Qt 相关构建错误，例如 `unknown type name 'Q_ENUM'`，可能是使用了 Qt 4，而不是 Qt 5。请参阅 `相关 Issue <https://github.com/ros2/ros2/issues/441>`_。

通过 Homebrew 安装 OpenCV 后出现缺失符号
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果安装了 OpenCV，可能会出现 `__cg_jpeg_resync_to_restart` 符号缺失的错误。此时，构建前需要执行：

.. code-block:: console

   $ brew unlink libpng libtiff libjpeg

但这会导致 OpenCV 无法正常工作，因此还需要使用 `install_name_tool` 更新相关动态库路径。原始命令及库路径请以本节上游文档为准。

Xcode-select 错误
^^^^^^^^^^^^^^^^^

.. only relevant to Eloquent and Foxy

如果最近安装了 Xcode，可能遇到 `xcodebuild requires Xcode` 错误。解决方法：

1. 安装命令行工具：

.. code-block:: console

   $ xcode-select --install

2. 接受 Xcode 许可协议：

.. code-block:: console

   $ sudo xcodebuild -license accept

3. 确保 Xcode 应用位于 `/Applications` 目录中。
4. 将 `xcode-select` 指向 Xcode Developer 目录：

.. code-block:: console

   $ sudo xcode-select -s /Applications/Xcode.app/Contents/Developer

rosdep 无法确认 qt5 安装成功
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

按照创建工作空间教程操作时，可能遇到 `homebrew: Failed to detect successful installation of [qt5]` 错误。

该错误可能源于`链接问题 <https://github.com/ros-infrastructure/rosdep/issues/490#issuecomment-334959426>`_。可以尝试：

.. code-block:: console

   $ cd /usr/local/Cellar
   $ sudo ln -s qt qt5

然后重新运行 rosdep 安装命令。

.. _windows-troubleshooting:

Windows
-------

系统中存在库文件，但导入仍然失败
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

有时，`rclpy` 会因为系统中缺少 DLL 而导入失败。请确保安装了 :ref:`Windows 安装前置依赖 <windows-install-binary-installing-prerequisites>` 中列出的所有依赖项。

如果通过二进制包安装，依赖项版本必须与构建二进制包时使用的版本相同。

如果问题仍然存在，可以使用 `Dependencies <https://github.com/lucasg/Dependencies>`_ 工具检查 `.pyd` 文件，确定系统中缺少哪些 DLL。执行工具前，请确保已经 source 当前工作空间，否则可能会出现 ROS DLL 文件无法解析的情况。

CMake 设置文件修改时间失败
^^^^^^^^^^^^^^^^^^^^^^^^^^

如果安装文件时遇到 `file INSTALL cannot set modification time` 错误，通常是杀毒软件或 Windows Defender 干扰了构建。可以将工作空间目录添加到排除列表。

260 字符路径长度限制
^^^^^^^^^^^^^^^^^^^^

构建时可能出现路径长度限制错误。要允许更长路径：

运行 `regedit.exe`，导航到：

`Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`

将 `LongPathsEnabled` 设置为 `0x00000001 (1)`。

然后打开“Edit Group Policy”，导航到“Local Computer Policy > Computer Configuration > Administrative Templates > System > Filesystem”，编辑“Enable Win32 long paths”，选择 Enabled。

关闭并重新打开终端，再尝试构建。

CMake 无法找到 asio、tinyxml2、tinyxml 或 eigen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

有时，Chocolatey 安装的 `asio`、`tinyxml2` 等软件包不会添加重要的注册表项，导致 CMake 无法找到它们。可以尝试卸载这些 Chocolatey 软件包，然后重新安装。

patch.exe 打开新命令窗口并要求管理员权限
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

这可能导致需要使用 patch 的软件包构建失败。可以运行：

.. code-block:: console

   $ choco uninstall patch
   $ colcon build --cmake-clean-cache

这是 `GNU Patch for Windows <https://chocolatey.org/packages/patch>`_ 软件包的一个缺陷。不安装该软件包时，构建过程会改用 Git 自带的 Patch 版本。

Fast RTPS 共享库加载失败
^^^^^^^^^^^^^^^^^^^^^^^^

.. does not apply to Crystal

Fast RTPS 需要 `msvcr20.dll`，该文件属于 Visual C++ Redistributable Packages for Visual Studio 2013。部分 Windows 系统可能没有安装，可以从 `Microsoft 下载页面 <https://www.microsoft.com/en-us/download/details.aspx?id=40784>`_ 获取。

创建进程失败
^^^^^^^^^^^^

如果运行 ROS 二进制程序时出现 ``failed to create process`` 错误，可能是找不到 Python 解释器。请确保 Python 位于预期路径下，默认路径为 ``C:\Python38\``。

二进制安装特有问题
^^^^^^^^^^^^^^^^^^

* 如果示例因为缺少 DLL 无法启动，请确认 OpenCV 等外部依赖库都位于 `PATH` 环境变量包含的目录中。
* 如果忘记在终端中调用 `local_setup.bat`，演示程序可能会立即崩溃。

在 WSL2 中运行 RViz
^^^^^^^^^^^^^^^^^^^

如果使用 `WSL2 <https://learn.microsoft.com/en-us/windows/wsl/install>`_ 运行 ROS 2，启动 RViz 时可能发生段错误。一种可能的解决方法是强制 RViz 使用软件渲染：

.. code-block:: console

   $ export LIBGL_ALWAYS_SOFTWARE=true
   $ rviz2
