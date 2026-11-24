集成开发环境与调试（社区贡献）
================================

ROS 2 并不依赖某个特定开发环境，其主要开发流程仍以命令行构建和运行作为重点。不过，也可以使用集成开发环境（IDE）开发、运行和/或调试 ROS 2 节点。

下面列出一些 IDE，以及如何将它们与 ROS 2 配合使用的说明。

.. contents:: 目录
    :depth: 2
    :local:

通用说明
--------

.. _installedpythoncode:

已安装的 Python 代码
^^^^^^^^^^^^^^^^^^^^

默认情况下，使用以下命令构建工作空间时：

.. code-block:: console

   $ colcon build

Python 代码会被复制到 `build`/`install` 目录中。因此，如果从 IDE 内部调试 `ros2 run` 命令，实际运行的代码（来自 `build`/`install`）与 IDE 项目中打开的源文件并不是同一份文件。

有两种处理方式：

* 打开 `build`/`install` 目录中的源文件，并在这些文件中设置断点。
* 使用 colcon 的 `--symlink-install` 标志构建工作空间，使 `build`/`install` 目录中的文件通过符号链接指向源文件。更多信息请参阅 `colcon 文档 <https://colcon.readthedocs.io/en/released/reference/verb/build.html#command-line-arguments>`__。

Visual Studio Code
------------------

`VSCode <https://code.visualstudio.com/>`_ 是一款功能丰富且免费的开发环境。

VSCode 与 ROS 2 配合使用相对简单。只需在命令行中激活 ROS 2 环境，并从同一个终端启动 VSCode，然后正常使用即可：

#. 按照平时的方式创建 ROS 工作空间。
#. 在终端中 source ROS 2 环境；如果工作空间已经构建，也要 source 其 install 环境。
#. 从同一个命令行启动 VSCode。VSCode 关闭前，启动它的终端会一直被占用。

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        $ source /opt/ros/{DISTRO}/setup.bash
        $ cd ~/dev_ws
        $ source ./install/setup.bash
        $ /usr/bin/code ./src/my_node/

   .. group-tab:: macOS

      .. code-block:: console

        $ . ~/ros2_install/ros2-osx/setup.bash
        $ cd ~/dev_ws
        $ . ./install/setup.bash
        $ /Applications/Visual Studio Code.app/Contents/Resources/app/bin/code ./src/my_node/

   .. group-tab:: Windows

      在 Windows 命令行中：

      .. code-block:: console

        $ call C:\dev\ros2\local_setup.bat
        $ cd C:\dev_ws
        $ call .\install\local_setup.bat
        $ "C:\Program Files\Microsoft VS Code\Code.exe" .\src\my_node\

      或在 PowerShell 中：

      .. code-block:: console

        $ C:\dev\ros2\local_setup.ps1
        $ cd C:\dev_ws
        $ .\install\local_setup.ps1
        $ & "C:\Program Files\Microsoft VS Code\Code.exe" .\src\my_node\

VSCode 以及在 VSCode 内部创建的任何终端都会正确继承父进程环境，因此应该能够访问 ROS 和已安装的软件包。

.. note::

   添加软件包或进行重大修改后，可能需要重新 source install 环境。最简单的方法是关闭 VSCode，然后按照上述方式重新启动。

Python
^^^^^^

在工作空间中，确认使用了正确的 Python 解释器。source 环境后，命令行中的 `python` 通常就是正确的解释器，但 VSCode 倾向于使用 Python 的绝对路径。

点击右下角的“Selected Python Interpreter”可以更改解释器。

如果 ROS 2 的 Python 版本来自虚拟环境，VSCode 会尝试在每次运行命令时重新激活该环境。但由于 VSCode 已经从 source 过的环境中启动，因此这一步并不必要。

可以在当前工作空间中打开“Settings” > “Extensions” > “Python” > “Activate Environment”，并取消启用该选项。

现在可以直接运行文件，或在 `launch.json` 中创建配置。调试节点时，创建类似 `python ...` 的配置通常比使用 `ros2 run/launch ...` 更简单。`launch.json` 示例：

.. code-block:: json

   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Python: File",
               "type": "python",
               "request": "launch",
               "program": "my_node.py"
           },
       ]
   }

也可以创建“Attach using Process Id”配置，附加到正在运行的进程。

有关 VSCode 与 Docker 配合使用的完整说明，请参阅 :doc:`使用 VSCode 和 Docker 配置 ROS 2 <Setup-ROS-2-with-VSCode-and-Docker-Container>`。

PyCharm
-------

`PyCharm <https://www.jetbrains.com/pycharm/>`_ 是一款专门面向 Python 的 IDE，因此只适合用于 Python 节点。

使用 PyCharm 时，可以附加到已有进程（例如通过 `ros2 run ...` 或 `ros2 launch ...` 启动的进程），也可以直接从 Python 运行节点（相当于 `python [file.py]`）。

集成代码检查
^^^^^^^^^^^^

可以配置 PyCharm 项目，使其完整识别 ROS 2 代码，从而支持代码补全和提示。

Linux
"""""

打开终端，source ROS 2 环境，然后启动 PyCharm：

.. code-block:: console

   $ source /opt/ros/humble/setup.bash
   $ cd path/to/dev_ws
   $ /opt/pycharm/bin/pycharm.sh

选择正确的解释器后，应该就可以正常使用。

.. note::

    此方法未经测试。

Windows
"""""""

在 Windows 上，先 source ROS 再从命令行启动 PyCharm 似乎不起作用，因此需要调整一些设置。

#. 按照平时的方式创建 ROS 工作空间。
#. 正常启动 PyCharm。
#. 打开一个项目。项目根目录应为正在开发的 ROS 节点目录，例如 `C:\dev_ws\src\my_node`。
#. 点击“Add new interpreter” > “Add local interpreter...”。选择系统解释器（或正在使用的虚拟环境），并选择 ROS Python 版本对应的可执行文件（通常为 `C:\Python38\python.exe`）。

   * 此时打开代码文件，可能会看到缺少导入模块的警告。尝试运行文件也会确认这些问题。

#. 在“Python Interpreters”窗口中找到并选择 ROS 解释器，为其设置一个容易识别的名称。然后点击“Show Interpreter Paths”。
#. 在新窗口中可以看到该解释器已有的路径。点击“+”添加两个路径（根据你的 ROS 安装位置调整）：

   * `C:\dev\ros2_humble\bin`
   * `C:\dev\ros2_humble\Lib\site-packages`

PyCharm 会重新建立索引。完成后，它应该能够正确识别项目中的 ROS 2 系统软件包，并支持代码导航、补全和文档提示。

如果还有与当前功能包一起构建的依赖项，它们可能尚未被识别，从而导致 IDE 警告或运行时错误。

可以通过以下方式解决：

* 确保运行/调试配置中的 `PATH` 覆盖值同时包含 ROS 2 安装目录和工作空间，例如：

  .. code-block:: console

     $ C:\dev\ros2_humble\local_setup.ps1
     $ C:\dev_ws\install\local_setup.ps1
     $ echo $ENV:Path

* 将 `install/` 目录中相关文件夹添加到项目源目录。

  打开“Settings...” > “Project: ” > “Project Structure”，点击“Add content root”，添加 `install/Lib/*` 下所有相关 `site-packages` 文件夹。

  最后，确保运行/调试配置启用了“include content roots in PYTHONPATH”选项。

.. tip::

   使用 colcon build 的 `--merge-install` 选项可以减少依赖目录的数量，从而更容易配置 PyCharm。更多信息请参阅 `colcon 文档 <https://colcon.readthedocs.io/en/released/user/isolated-vs-merged-workspaces.html>`__。

附加到进程
^^^^^^^^^^

即使没有对 PyCharm 进行任何配置，也可以直接附加到正在运行的 Python 节点。

打开项目源代码，然后按正常方式运行节点：

.. code-block:: console

   $ ros2 run my_node main

接着在 PyCharm 中选择“Run” > “Attach to Process...”。稍等片刻，会弹出一个小窗口，列出当前运行的 Python 实例，其中包括你的节点。

由于可能存在多个 Python 进程，可能需要尝试几次才能找到正确的进程。

选择实例后，就可以使用常规调试工具，例如暂停进程、在代码中创建断点以及单步执行。

.. note::

   项目中的代码可能并不是实际执行的文件，请参阅 :ref:`已安装的 Python 代码 <InstalledPythonCode>`。

运行/调试
^^^^^^^^^

首先按照前面的步骤完成集成。

从 PyCharm 运行 Python 文件时，可能会出现导入错误。这是因为 PyCharm 会扩展 `PYTHONPATH` 环境变量，但不会修改 `PATH`，导致无法找到 `ros/bin` 中的必要库文件。

编辑该文件的运行/调试配置，在“Environment Variables”中添加一个新变量。当前不支持扩展已有 `PATH`，因此需要覆盖它。

在已经 source ROS 环境的终端中运行 `echo $Env:PATH`，导出 `PATH` 的内容并复制结果。

回到 PyCharm，将复制的内容粘贴为 `PATH`，应用修改后运行或调试节点。此后应当能够像普通 Python 项目一样工作，并方便地添加断点或使用其他调试方法。

.. note::

   在 Windows 上，“Environment Variables”中的 `PATH` 变量似乎必须全部使用小写形式 `path` 才能正常工作。
