获取 ROS 2 中的调用堆栈
########################

.. contents:: 目录
   :local:

**目标：** 介绍在 ROS 2 中获取调用堆栈的多种方法。

**教程级别：** 中级

**预计时间：** 15 分钟

以下步骤介绍 ROS 2 用户在遇到问题时，如何获取调用堆栈。

概述
----

**什么是调用堆栈（Backtrace）？**

- 可以把程序想象成一叠煎饼，每一层煎饼代表程序当前正在执行的一个函数。调用堆栈就像程序崩溃后这叠煎饼倒下时的一张照片，展示它们原本的顺序，从而揭示程序是如何发生故障的。
- 调用堆栈会列出函数调用的先后关系，显示程序在发生故障之前依次调用了哪些函数。

**为什么调用堆栈有用？**

- **定位问题：** 不必猜测代码中的错误位置，调用堆栈可以显示导致崩溃的具体代码行。
- **揭示上下文：** 可以看到最终触发故障的函数调用链，从而理解问题发生的位置和原因。

**形象理解：一叠煎饼**

1. 每一层煎饼代表一个函数。最底层是程序的 ``main()`` 函数，程序从这里开始执行。
2. 每当一个函数调用另一个函数，就相当于在煎饼堆顶部增加一层。
3. 程序崩溃就像底部盘子滑落，导致当前执行的函数发生故障。
4. 调用堆栈就像这叠倒下的煎饼的照片，展示函数顺序，帮助定位崩溃位置。

**代码示例：**

.. code-block:: cpp

  void functionC() {
    // 此处发生错误，导致程序崩溃
  }

  void functionB() {
      functionC();
  }

  void functionA() {
      functionB();
  }

  int main() {
      functionA();
      return 0;
  }

**崩溃时的调用堆栈：**

.. code-block:: bash

  #0  functionC() at file.cpp:3 // 崩溃发生在这里
  #1  functionB() at file.cpp:8
  #2  functionA() at file.cpp:13
  #3  main() at file.cpp:18

**调用堆栈的作用：**

- **崩溃起点：** 显示触发崩溃的 ``functionC()`` 中的确切代码行。
- **调用顺序：** 揭示 ``main()`` 调用了 ``functionA()``，``functionA()`` 调用了 ``functionB()``，最终导致 ``functionC()`` 中发生错误。

以上示例说明了调用堆栈是什么，以及它的用途。接下来介绍 ROS 2 用户遇到问题时，如何获取特定节点的调用堆栈。本教程适用于仿真机器人和实体机器人。

本教程涵盖三种场景：使用 ``ros2 run`` 获取特定节点的调用堆栈；使用 ``ros2 launch`` 获取单节点启动文件中的调用堆栈；以及在更复杂的节点编排场景中获取调用堆栈。

完成本教程后，你应该能够在发现 ROS 2 节点崩溃时获取调用堆栈。

前置准备
--------

GDB 是 Unix 系统中最常用的 C/C++ 调试器。它可用于确定程序崩溃的原因、跟踪线程，也可以在代码中设置断点，以检查程序运行到特定位置时的内存值。

对于所有从事 C/C++ 开发的软件工程师而言，掌握 GDB 都是一项重要技能。虽然许多 IDE 内置了调试器或性能分析器，但理解如何使用底层工具非常重要，不能完全依赖 IDE。否则，当你更换开发环境，或通过 SSH 远程调试设备时，可能无法继续使用熟悉的 IDE 工具。

掌握基础知识后，GDB 的使用并不复杂。下面介绍如何让 ROS 2 代码具备调试条件：

- **使用 `--cmake-args`：** 最简单的方法是在 ``colcon build`` 命令中添加 ``--cmake-args -DCMAKE_BUILD_TYPE=Debug``，以包含调试符号：

.. code-block:: console

  $ colcon build --packages-up-to <package_name> --cmake-args -DCMAKE_BUILD_TYPE=Debug

- **编辑 `CMakeLists.txt`：** 也可以为希望分析或调试的 ROS 软件包，在编译器标志中添加 ``-g``。该标志会生成 GDB 可以读取的调试符号，使其能够显示项目中具体哪一行代码发生故障，以及故障原因。如果未设置该标志，仍然可以获取调用堆栈，但不会显示故障对应的源代码行号。

现在就可以开始调试代码了。

对于非 ROS 项目，可以直接启动 GDB 并让程序立即运行。程序崩溃后，会返回 ``(gdb)`` 提示符，可以在其中查看所需信息。不过，ROS 项目涉及大量节点配置和其他运行环境，因此对于初学者或不熟悉命令行及文件系统的用户，这种方式并不方便。

.. code-block:: console

  $ gdb -ex run --args /path/to/exe/program

下面介绍 ROS 2 系统中可能遇到的三种主要情况。请阅读与你要解决的问题相对应的部分。

使用 GDB 调试特定节点
---------------------

要在启动 ROS 2 节点之前轻松建立 GDB 调试会话，可以使用 `--prefix` 选项。

.. note::

  请注意，一个 ROS 2 可执行程序可能包含多个节点。使用 `--prefix` 可以确保调试的是目标进程中的相应节点。

**为什么直接使用 GDB 比较麻烦？**

`--prefix` 会在 ROS 2 命令执行之前运行一些代码，从而允许我们插入额外的调试命令。

如果尝试使用 `gdb -ex run --args ros2 run <pkg> <node>`，可能会发现 GDB 无法找到 ``ros2`` 命令。在 GDB 中尝试 source 工作空间也可能失败。

这是因为以这种方式启动 GDB 时，它没有获得通常用于查找 ``ros2`` 命令的环境配置。

**使用 --prefix 简化流程**

不必查找可执行程序的安装路径并手动输入完整路径，可以使用 `--prefix`。这样就能继续使用熟悉的 ``ros2 run`` 语法，而不必处理 GDB 的这些细节。

.. code-block:: console

  $ ros2 run --prefix 'gdb -ex run --args' <pkg> <node> --all-other-launch arguments

**GDB 调试过程**

与前面的方式一样，该前缀会启动 GDB 会话，并运行指定节点，同时保留其他命令行参数。

此时节点应该已经运行，并输出正常的调试日志。

读取调用堆栈
------------

使用 GDB 获取调用堆栈后，可以按照以下方式解读：

- **从底部开始：** 调用堆栈按时间倒序列出函数调用，底部的函数是调用链的起点。
- **沿堆栈向上追踪：** 上方每一行表示调用下方函数的函数。一直向上追踪，直到找到自己项目中的代码行，通常就能发现问题的起点。
- **寻找调试线索：** 函数名称和参数可以提供有价值的信息，帮助判断问题原因。

**节点崩溃后如何调试**

节点崩溃后，你会看到如下提示符：

.. code-block:: bash

  (gdb)

在该会话中输入 ``backtrace``，GDB 就会输出调用堆栈。复制输出内容以便后续分析。

**调用堆栈示例**

.. code-block:: bash

  (gdb) backtrace
  #0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
  #1  0x00007ffff79cc859 in __GI_abort () at abort.c:79
  #2  0x00007ffff7c52951 in ?? () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
  #3  0x00007ffff7c5e47c in ?? () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
  #4  0x00007ffff7c5e4e7 in std::terminate() () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
  #5  0x00007ffff7c5e799 in __cxa_throw () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
  #6  0x00007ffff7c553eb in ?? () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
  #7  0x000055555555936c in std::vector<int, std::allocator<int> >::_M_range_check (
      this=0x5555555cfdb0, __n=100) at /usr/include/c++/9/bits/stl_vector.h:1070
  #8  0x0000555555558e1d in std::vector<int, std::allocator<int> >::at (this=0x5555555cfdb0,
      __n=100) at /usr/include/c++/9/bits/stl_vector.h:1091
  #9  0x000055555555828b in GDBTester::VectorCrash (this=0x5555555cfb40)
      at /home/steve/Documents/nav2_ws/src/gdb_test_pkg/src/gdb_test_node.cpp:44
  #10 0x0000555555559cfc in main (argc=1, argv=0x7fffffffc108)
      at /home/steve/Documents/nav2_ws/src/gdb_test_pkg/src/main.cpp:25

在这个示例中，应从底部开始阅读：

- 在 ``main`` 函数第 25 行调用了 ``VectorCrash`` 函数。
- 在 ``VectorCrash`` 函数第 44 行，调用 STL vector 的 ``at()`` 方法时传入了 ``100``。
- ``at()`` 在 STL vector 第 1091 行抛出了范围检查异常，最终导致程序崩溃。

阅读这类堆栈需要一些练习。通常，从底部开始向上查看，找到发生崩溃的代码行，然后分析崩溃原因即可。

完成 GDB 调试后，输入 `quit` 退出会话，并结束仍在运行的进程。如果 GDB 询问是否结束某些线程，请选择 yes。

从启动文件调试
--------------

与非 ROS 示例一样，需要在运行 ROS 2 启动文件之前建立 GDB 会话。可以通过命令行完成，也可以使用与 ``ros2 run`` 节点示例相同的方式，在启动文件中配置调试前缀。

在启动文件中找到需要调试的节点。本节假设启动文件只包含一个节点（也可以包含其他配置信息）。

``launch_ros`` 软件包中的 ``Node`` 函数提供 ``prefix`` 字段，接受一个前缀参数列表。我们将在这里插入 GDB 命令。

**根据使用环境选择以下方式：**

- **本地 GUI 调试：** 如果本地有图形界面，可以使用：

.. code-block:: python

  prefix=['xterm -e gdb -ex run --args']

这样会在单独窗口中提供交互式调试体验。以下示例在 ``start_sync_slam_toolbox_node`` 中使用该方式：

.. code-block:: python

  start_sync_slam_toolbox_node = Node(
    parameters=[
        get_package_share_directory("slam_toolbox") + '/config/mapper_params_online_sync.yaml',
        {'use_sim_time': use_sim_time}
    ],
    package='slam_toolbox',
    executable='sync_slam_toolbox_node',
    name='slam_toolbox',
    prefix=['xterm -e gdb -ex run --args'],
    output='screen')

- **远程调试（无 GUI）：** 如果没有图形界面，请省略 ``xterm -e``：

.. code-block:: python

  prefix=['gdb -ex run --args']

GDB 的输出和交互会发生在启动 ROS 2 应用程序的终端会话中。对应示例：

.. code-block:: python

  start_sync_slam_toolbox_node = Node(
    parameters=[
        get_package_share_directory("slam_toolbox") + '/config/mapper_params_online_sync.yaml',
        {'use_sim_time': use_sim_time}
    ],
    package='slam_toolbox',
    executable='sync_slam_toolbox_node',
    name='slam_toolbox',
    prefix=['gdb -ex run --args'],
    output='screen')

与之前一样，该前缀会启动 GDB 会话，并运行指定启动文件中的节点，同时保留其他启动参数。

节点崩溃后，可以在 xterm 窗口或当前终端中看到 GDB 提示符，并按照前面“读取调用堆栈”一节的方法获取和分析堆栈。

在大型项目中调试
----------------

包含多个节点的启动文件调试方式略有不同。为了避免其他节点的日志干扰 GDB 会话，建议将需要调试的节点单独提取出来运行。

如果目标节点由嵌套启动文件（例如被包含的启动文件）启动，可以按以下方式操作：

- 在父启动文件中注释掉对应启动文件的 include。
- 使用 ``-g`` 调试符号标志重新编译目标软件包。
- 在一个终端中启动父启动文件。
- 在另一个终端中，按照前面“从启动文件调试”一节的说明启动目标节点的启动文件。

如果目标节点直接在这些启动文件中启动（例如 ``Node``、``LifecycleNode`` 或 `ComponentContainer`），则需要将其与其他节点分离：

- 在父启动文件中注释掉目标节点。
- 使用 ``-g`` 调试符号标志重新编译目标软件包。
- 在一个终端中启动父启动文件。
- 在另一个终端中，按照前面“使用 GDB 调试特定节点”一节的说明启动目标节点。

.. note::

  此时可能需要为该节点重新映射话题或提供参数文件，因为此前这些配置可能由启动文件提供。可以使用 ``--ros-args`` 指定新的参数文件、重映射规则或节点名称。所需命令行参数请参阅 :doc:`本教程 <../../How-To-Guides/Node-arguments>`。

  我们理解这一过程可能比较麻烦，因此建议尽可能将每个节点放在独立的可包含启动文件中，以便调试。例如，可以使用以下参数模板：

  ``--ros-args -r __node:=<node_name> --params-file /absolute/path/to/params.yaml``。

节点崩溃后，可以在目标节点对应的终端中看到 GDB 提示符，并按照“读取调用堆栈”一节获取和分析堆栈。

使用 GDB 调试测试
-----------------

如果 C++ 测试失败，可以直接对 build 目录中的测试可执行程序使用 GDB。

确保代码使用 Debug 模式构建。由于之前的构建类型可能被 CMake 缓存，需要清理缓存并重新构建：

.. code-block:: console

  $ colcon build --cmake-clean-cache --mixin debug

为了让 GDB 能够加载所调用共享库的调试符号，请确保已经 source 环境。这会配置 ``LD_LIBRARY_PATH`` 的值：

.. code-block:: console

  $ source install/setup.bash

最后，直接通过 GDB 运行测试。例如：

.. code-block:: console

  $ gdb -ex run ./build/rcl/test/test_logging

如果代码抛出了未处理的异常，可以在 gtest 处理异常之前使用 GDB 捕获它：

.. code-block:: console

  $ gdb ./build/rcl/test/test_logging
  $ catch throw
  $ run

崩溃时自动生成调用堆栈
----------------------

``backward-cpp`` 库可以生成清晰易读的调用堆栈，而 ``backward_ros`` 封装库则简化了它在 ROS 中的集成。

只需将其添加为依赖项，并在 ``CMakeLists.txt`` 中调用 ``find_package``，backward 库就会被注入所有可执行程序和库中。
