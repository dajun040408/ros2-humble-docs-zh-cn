.. redirect-from::

   Installation/Windows-Development-Setup

.. _windows-latest:

Windows（源码安装）
===================

.. contents:: 目录
   :depth: 2
   :local:

本指南介绍如何在 Windows 上配置 ROS 2 开发环境。

系统要求
--------

目前仅支持 Windows 10。

语言支持
^^^^^^^^

请确保系统区域语言支持 `UTF-8`。例如，对于中文 Windows 10 安装环境，可能需要安装`英文语言包 <https://support.microsoft.com/en-us/windows/language-packs-for-windows-a5094319-a92d-18de-5b53-1cfc697cfca8>`_。

.. include:: ../_Windows-Install-Prerequisites.rst

其他前置依赖
------------

从源码构建时，还需要安装一些额外依赖。

使用 Chocolatey 安装其他依赖
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   $ choco install -y cppcheck curl git winflexbison3

需要将 Git cmd 目录 `C:\Program Files\Git\cmd` 添加到 PATH。可以点击 Windows 图标，搜索“环境变量”，选择“编辑系统环境变量”；在弹出的窗口中点击“环境变量”，在下方窗格中选择“Path”，点击“编辑”，然后添加该路径。

安装 Python 前置依赖
^^^^^^^^^^^^^^^^^^^^

安装额外 Python 依赖：

.. code-block:: console

   $ pip install -U colcon-common-extensions coverage flake8 flake8-blind-except flake8-builtins flake8-class-newline flake8-comprehensions flake8-deprecated flake8-docstrings flake8-import-order flake8-quotes mock mypy==0.931 pep8 pydocstyle pytest pytest-mock vcstool

安装其他杂项依赖
^^^^^^^^^^^^^^^^

接下来安装 `xmllint`：

* 从 `libxml 项目网站 <https://www.zlatkovic.com/projects/libxml/>`_ 下载 `libxml2` 的 64 位二进制归档，以及其依赖 `iconv` 和 `zlib`。
* 将所有归档解压到某个目录，例如 `C:\xmllint`。
* 将 `C:\xmllint\bin` 添加到 `PATH`。

获取 ROS 2 源码
---------------

现在开发工具已经准备就绪，可以获取 ROS 2 源码。

首先创建开发目录，例如 `C:\{DISTRO}`：

.. note::

   由于 Windows 默认路径长度限制较短（260 个字符），所选路径必须尽量短。若要启用更长路径，请参阅`最大路径长度说明 <https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry>`_。

.. code-block:: console

   $ md \{DISTRO}\src
   $ cd \{DISTRO}

获取定义待克隆仓库的 `ros2.repos` 文件：

.. code-block:: console

   $ vcs import --input https://raw.githubusercontent.com/ros2/ros2/{REPOS_FILE_BRANCH}/ros2.repos src

安装其他 DDS 实现（可选）
^^^^^^^^^^^^^^^^^^^^^^^^^

Fast DDS 已包含在 ROS 2 源码中。除非在 `src\eProsima` 目录中创建 `COLCON_IGNORE` 文件，否则始终会构建 Fast DDS。

如果希望使用默认实现以外的 DDS 或 RTPS 供应商，请参阅 :doc:`相关说明 <../RMW-Implementations>`。

构建 ROS 2 代码
---------------

构建 ROS 2 时，需要以管理员身份运行 Visual Studio 命令提示符，例如“x64 Native Tools Command Prompt for VS 2019”。

构建 `\{DISTRO}` 目录树：

.. code-block:: console

   $ colcon build --merge-install

.. note::

   此处使用 `--merge-install`，是为了避免构建结束时 `PATH` 环境变量过长。如果只构建较小的工作空间，可以尝试默认的 isolated 安装模式，即将每个功能包安装到不同目录。

.. note::

   如果执行 Debug 构建，需要使用 `python_d path\to\colcon_executable` 调用 colcon。更多信息请参阅下文“Debug 模式附加内容”。

.. note::

   由于工作空间中包含大量功能包，源码安装可能需要较长时间。

环境配置
--------

打开命令行 Shell，并 source ROS 2 环境设置文件：

.. code-block:: console

   $ call C:\{DISTRO}\install\local_setup.bat

如果前面的命令没有其他错误，但恰好输出一次 `The system cannot find the path specified.`，这是正常现象。

测试与运行
----------

首次运行任何可执行程序时，Windows 防火墙可能会弹出窗口，要求允许其访问网络。

可以使用以下命令运行测试：

.. code-block:: console

   $ colcon test --merge-install

.. note::

   只有构建阶段也使用了 `--merge-install`，测试阶段才应使用该选项。

随后可以运行以下命令查看测试摘要：

.. code-block:: console

   $ colcon test-result

要运行示例，请打开一个干净的新 `cmd.exe`，source `local_setup.bat`，然后运行 C++ `talker`：

.. code-block:: console

   $ call install\local_setup.bat
   $ ros2 run demo_nodes_cpp talker

在另一个 Shell 中执行相同的环境配置，然后运行 Python `listener`：

.. code-block:: console

   $ call install\local_setup.bat
   $ ros2 run demo_nodes_py listener

你应该能看到 `talker` 输出正在 `Publishing` 消息，而 `listener` 输出 `I heard` 并显示收到的消息。这说明 C++ 和 Python API 均能正常工作。

.. note::

   不建议在已经 source `local_setup.bat` 的同一个 cmd 提示符中执行构建。

安装后的后续步骤
----------------

继续阅读 :doc:`教程和演示 <../../Tutorials>`，配置环境、创建自己的工作空间和功能包，并学习 ROS 2 核心概念。

其他 RMW 实现（可选）
---------------------

ROS 2 默认使用的中间件是 `Fast DDS`，但可以在运行时替换中间件（RMW）。有关如何使用多个 RMW 的说明，请参阅 :doc:`多 RMW 使用指南 <../../How-To-Guides/Working-with-multiple-RMW-implementations>`。

Debug 模式附加内容
------------------

如果希望在 Debug 模式下运行所有测试，还需要安装一些额外内容。

* 为了能够解压 Python 源码 tarball，可以使用 PeaZip：

  .. code-block:: console

     $ choco install -y peazip

* 还需要 SVN，因为部分 Python 源码构建依赖通过 SVN 检出：

  .. code-block:: console

     $ choco install -y svn hg

* 安装以上工具后，需要退出并重新启动命令提示符。
* 获取并解压 Python 3.8.3 源码：

  * `Python-3.8.3 <https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz>`_
  * 为简化说明，将其解压到 `C:\dev\Python-3.8.3`。

* 在 Visual Studio 命令提示符中以 Debug 模式构建 Python 源码：

  .. code-block:: console

     cd C:\dev\Python-3.8.3\PCbuild
     get_externals.bat
     build.bat -p x64 -d

* 将构建产物复制到 Python38 安装目录，与 Release 模式的 Python 可执行程序和 DLL 放在一起：

  .. code-block:: console

     cd C:\dev\Python-3.8.3\PCbuild\amd64
     copy python_d.exe C:\Python38 /Y
     copy python38_d.dll C:\Python38 /Y
     copy python3_d.dll C:\Python38 /Y
     copy python38_d.lib C:\Python38\libs /Y
     copy python3_d.lib C:\Python38\libs /Y
     copy sqlite3_d.dll C:\Python38\DLLs /Y
     for %I in (*_d.pyd) do copy %I C:\Python38\DLLs /Y

* 在新的命令提示符中，确认 `python_d` 可以正常运行：

  .. code-block:: console

     python_d -c "import _ctypes ; import coverage"

* 确认 `python_d` 正常后，需要使用启用 Debug 的库重新安装部分依赖：

  .. code-block:: console

     python_d -m pip install --force-reinstall https://github.com/ros2/ros2/releases/download/numpy-archives/numpy-1.18.4-cp38-cp38d-win_amd64.whl
     python_d -m pip install --force-reinstall https://github.com/ros2/ros2/releases/download/lxml-archives/lxml-4.5.1-cp38-cp38d-win_amd64.whl

* 验证这些依赖是否安装成功：

  .. code-block:: console

     python_d -c "from lxml import etree ; import numpy"

* 如果要恢复构建 Release 二进制文件，需要卸载 Debug 版本并重新安装 Release 版本：

  .. code-block:: console

     python -m pip uninstall numpy lxml
     python -m pip install numpy lxml

* 要将 Python 脚本创建为可执行程序（`.exe`），需要使用 `python_d` 调用 colcon：

  .. code-block:: console

     python_d path\to\colcon_executable build

保持源码为最新状态
------------------

请参阅 :doc:`维护源码检出 <../Maintaining-a-Source-Checkout>`，了解如何定期更新源码安装。

故障排查
--------

故障排查方法请参阅 :ref:`此处 <windows-troubleshooting>`。

卸载
----

1. 如果按照上文说明使用 colcon 安装工作空间，“卸载”可能只需要打开新终端，不再 source 工作空间的 `setup` 文件。这样，环境就会表现得如同系统中没有安装 {DISTRO_TITLE} 一样。
2. 如果还希望释放磁盘空间，可以删除整个工作空间目录：

   .. code-block:: console

      $ rmdir /s /q \ros2_{DISTRO}
