Ament Lint 命令行工具
=====================

**目标：** 学习如何使用 ``ament_lint`` 及相关工具识别并修复代码质量问题。

**教程级别：** 高级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

``ament`` 工具系列是一组用于 ROS 2 软件开发的 Python 工具。Ament 工具可以与任何构建系统配合使用，其中 ``ament_cmake`` 工具专门用于简化基于 CMake 的开发。

Ament 提供了一组命令行程序，帮助开发者编写符合 ROS 2 代码规范的代码。使用这些工具可以提高开发效率，并帮助 ROS 应用和核心代码符合 :doc:`ROS 项目代码规范 <../../The-ROS2-Project/Contributing/Code-Style-Language-Versions>`。建议 ROS 开发者熟悉这些工具，并在提交 Pull Request 之前运行检查。

前置条件
--------

常规 ROS 2 安装环境中应已包含 ``ament`` 软件包。若需安装 ROS 2，请参阅 :doc:`安装说明 <../../Installation>`。

Ament Lint 命令行工具
---------------------

所有 ament lint 工具采用类似的命令行模式：接收一个或多个目录或文件，分析输入内容并生成报告。

**对于某个 ament 工具，最准确、最新的文档通常可以通过其内置的** ``--help`` **选项查看。**

* ``-h, --help``：显示帮助信息并退出。
* ``--exclude [filename ...]``：排除指定文件名，支持通配符。
* ``--xunit-file XUNIT_FILE``：生成符合 xUnit 格式的 XML 文件，常用于 IDE 和 CI 自动收集测试结果。

1. ament_copyright
^^^^^^^^^^^^^^^^^^

``ament_copyright`` 命令行工具用于检查和更新 ROS 源代码中的版权声明，也可以检查是否包含适当的软件许可证、版权年份和版权持有人信息。

该工具以当前目录为起点，递归检查子目录中的源文件。可以在功能包、工作空间、普通目录或单个源文件范围内运行。它还可以自动为缺少声明的源文件添加版权和许可证信息。

1.1 参数
~~~~~~~~

默认情况下，``ament_copyright`` 会递归扫描当前目录，并报告缺少版权声明的文件。

程序还可以接收一个可选参数，即需要扫描的目录列表。例如，只检查源文件和头文件：

.. code-block:: console

   $ ament_copyright ./src ./include

1.2 选项
~~~~~~~~

``ament_copyright`` 支持以下选项：

* ``--add-missing COPYRIGHT_NAME LICENSE``：为缺少版权声明的文件添加版权和许可证信息。``LICENSE`` 是要使用的许可证名称。可用许可证列表可以通过 ``ament_copyright --list-licenses`` 查看。
* ``--add-copyright-year``：为现有版权声明添加当前年份。
* ``--list-copyright-names``：列出已知版权持有人。
* ``--list-licenses``：列出已知许可证。
* ``--verbose``：显示所有文件，而不只是存在错误或修改的文件。

1.3 示例
~~~~~~~~

如果希望检查 ROS 功能包是否包含适当的版权和许可证声明，可以直接运行 ``ament_copyright``。使用 ``--verbose`` 可以列出所有检查过的文件：

.. code-block:: console

   $ ament_copyright --verbose
   my_package/src/new_file.cpp: could not find copyright notice
   my_package/src/old_file.cpp: copyright=Open Source Robotics Foundation, Inc. (2023), license=apache2
   my_package/include/new_file.h: could not find copyright notice
   my_package/include/old_file.h: copyright=Open Source Robotics Foundation, Inc. (2023), license=apache2

2. ament_cppcheck
^^^^^^^^^^^^^^^^^

``ament_cppcheck`` 命令行工具用于对 C++ 源代码文件执行静态分析。

`静态分析 <https://en.wikipedia.org/wiki/Static_program_analysis>`_ 是自动检查源代码中可能在编译后引发问题的代码模式的过程。

``ament_cppcheck`` 底层使用 `cppcheck <https://github.com/danmar/cppcheck>`_。某些版本的 cppcheck 运行速度可能比较慢，因此部分系统会默认禁用 ``ament_cppcheck``。如需启用，可以设置环境变量 ``AMENT_CPPCHECK_ALLOW_SLOW_VERSIONS``。

2.1 参数
~~~~~~~~

默认情况下，``ament_cppcheck`` 会递归扫描当前目录，并报告源代码文件中可能存在的问题。

程序可以接收一个可选参数，即需要扫描的目录列表。例如，只检查最近修改的一个文件：

.. code-block:: console

   $ ament_cppcheck ./src/my_cpp_file.cpp

2.2 选项
~~~~~~~~

``ament_cppcheck`` 支持以下选项：

* ``--libraries [LIBRARIES ...]``：除标准 C 和 C++ 库外，还要加载的库配置。每个库都会作为 ``--library=<library_name>`` 传递给 cppcheck。
* ``--include_dirs [INCLUDE_DIRS ...]``：C/C++ 文件的头文件搜索目录。每个目录都会以 ``-I <include_dir>`` 的形式传递给 cppcheck。
* ``--cppcheck-version``：获取并输出 cppcheck 版本，然后退出。

2.3 示例
~~~~~~~~

创建一个名为 ``example.cpp`` 的简单 C++ 程序：

.. code-block:: cpp

   int main()
   {
       char a[10];
       a[10] = 0;
       return 0;
   }

该程序访问了数组已分配内存范围之外的位置。

在包含该文件的目录中运行 ``ament_cppcheck``，会得到类似以下结果：

.. code-block:: console

   $ ament_cppcheck
   [example.cpp:4]: (error: arrayIndexOutOfBounds) Array 'a[10]' accessed at index 10, which is out of bounds.

3. ament_cpplint
^^^^^^^^^^^^^^^^

``ament_cpplint`` 可以使用 `cpplint <https://github.com/cpplint/cpplint?tab=readme-ov-file>`_ 检查 C++ 代码是否符合 `Google C++ 代码风格 <https://google.github.io/styleguide/cppguide.html>`_。

``ament_cpplint`` 会扫描当前目录及其子目录中的 C++ 头文件和源文件，并对这些文件执行 CppLint 检查，最后返回检查结果。

目前，``ament_cpplint`` 无法自动修复发现的问题。如果希望自动修复格式问题，请使用 ``ament_uncrustify``。

3.1 参数
~~~~~~~~

程序可以接收一个可选参数，即需要扫描的目录列表。例如，只检查源文件和头文件：

.. code-block:: console

   $ ament_cpplint ./src ./include

3.2 选项
~~~~~~~~

``ament_cpplint`` 支持以下选项：

* ``--filters FILTER,FILTER,...``：以逗号分隔的类别过滤器列表。
* ``--linelength N``：最大行长度，默认值为 100。
* ``--root ROOT``：传递给 cpplint 的 ``--root`` 选项。

3.3 示例
~~~~~~~~

创建一个名为 ``example.cpp`` 的简单 C++ 程序，其中包含几处违反代码规范的内容：

.. code-block:: cpp

   int main()
   {
     int a = 10;
     int b = 10;
     int c = 0;/*<trailing whitespace>*/
     if( a == b)  {/*<tab>*/      c=a;}/*<trailing whitespace>*/
     return 0;
   }

对该文件运行 ``ament_cpplint``，会得到以下错误：

.. code-block:: console

   example.cpp:0:  No copyright message found.  You should have a line: "Copyright [year] <Copyright Owner>"  [legal/copyright] [5]
   example.cpp:6:  Line ends in whitespace.  Consider deleting these extra spaces.  [whitespace/end_of_line] [4]
   example.cpp:6:  Tab found; better to use spaces  [whitespace/tab] [1]
   example.cpp:6:  Line ends in whitespace.  Consider deleting these extra spaces.  [whitespace/end_of_line] [4]
   example.cpp:6:  Missing spaces around =  [whitespace/operators] [4]

4. ament_flake8
^^^^^^^^^^^^^^^

`Flake8 <https://pypi.org/project/flake8/>`_ 是用于 Python 代码检查和风格约束的工具。

``ament_flake8`` 命令行工具使用 Flake8 检查 Python 源代码，可以帮助定位 ROS Python 程序中的小错误和风格问题，例如行尾空格、代码行过长、函数参数间距不规范等。

需要注意，``flake8`` 和 ``ament_flake8`` 都不能自动重新格式化代码来修复这些问题。

4.1 参数
~~~~~~~~

程序可以接收一个可选参数，即需要扫描的目录列表。例如，如果只希望检查工作空间中的一个功能包，可以直接在该功能包目录中运行 ``ament_flake8``，也可以将目录路径作为参数传入。

4.2 选项
~~~~~~~~

* ``--config path``：指定配置文件。默认配置文件位于当前 Python 安装环境的 site-packages 目录中。不建议修改默认配置。
* ``--linelength N``：手动设置最大行长度。

4.3 示例
~~~~~~~~

创建一个名为 ``example.py`` 的简单 Python 程序：

.. code-block:: python

   def uglyPythonFunction(a,b,  c):
       if a != b:
           print("A does not match b")
       thisIsAVariableNameThatIsWayTooLongLongLong = 2
       extra_long =(thisIsAVariableNameThatIsWayTooLongLongLong*thisIsAVariableNameThatIsWayTooLongLongLong )
       return(c)

对该文件运行 ``ament_flake8``，会得到以下错误：

.. code-block:: console

   example.py:1:25: E231 missing whitespace after ','
   def uglyPythonFunction(a,b,  c):

   example.py:5:5: F841 local variable 'extra_long' is assigned to but never used
       extra_long =(thisIsAVariableNameThatIsWayTooLongLongLong*thisIsAVariableNameThatIsWayTooLongLongLong )
       ^

   example.py:5:17: E225 missing whitespace around operator
       extra_long =(thisIsAVariableNameThatIsWayTooLongLongLong*thisIsAVariableNameThatIsWayTooLongLongLong )
                   ^

   example.py:5:100: E501 line too long (106 > 99 characters)
       extra_long =(thisIsAVariableNameThatIsWayTooLongLongLong*thisIsAVariableNameThatIsWayTooLongLongLong )
                                                                                                      ^

   example.py:5:105: E202 whitespace before ')'
       extra_long =(thisIsAVariableNameThatIsWayTooLongLongLong*thisIsAVariableNameThatIsWayTooLongLongLong )
                                                                                                           ^

   1     E202 whitespace before ')'
   1     E225 missing whitespace around operator
   1     E231 missing whitespace after ','
   1     E501 line too long (106 > 99 characters)
   1     F841 local variable 'extra_long' is assigned to but never used

   1 files checked
   5 errors

   'E'-type errors: 4
   'F'-type errors: 1

   Checked files:

   * example.py

5. ament_uncrustify
^^^^^^^^^^^^^^^^^^^

`Uncrustify <https://github.com/uncrustify/uncrustify>`_ 是一种 C++ 代码检查工具，与 ``ament_cpplint`` 类似，但它的优势在于能够**自动修复**发现的格式问题。

该工具可以帮助定位和修复 ROS C++ 程序中的小错误和风格问题，例如行尾空格、代码行过长、函数参数间距不规范等。

5.1 参数
~~~~~~~~

程序可以接收一个可选参数，即需要扫描的目录列表。例如，如果只希望检查工作空间中的一个功能包，可以直接在该功能包目录中运行 ``ament_uncrustify``，也可以将目录路径作为参数传入。

5.2 选项
~~~~~~~~

* ``-c CFG``：指定 Uncrustify 使用的配置文件。如果不需要自定义设置，建议使用默认配置。
* ``--linelength N``：最大行长度。
* ``--language``：指定语言类型，可选值为 ``C``、``C++`` 或 ``CPP``。该选项会以 ``-l <language>`` 的形式传递给 Uncrustify，而不是根据文件扩展名自动选择语言。
* ``--reformat``：直接在原文件中重新格式化，即修复检查发现的格式问题。

**建议运行** ``ament_uncrustify`` **时使用** ``--reformat`` **选项，这样可以节省大量时间。**

5.3 示例
~~~~~~~~

回到之前的 ``example.cpp`` 文件：

.. code-block:: cpp

   int main()
   {
        int a = 10;
        int b = 10;
        int c = 0;<trailing whitespace>
        if( a == b)<trailing whitespace>{
   <tab>      c=a;}<trailing whitespace>
        return 0;
    }

运行 ``ament_uncrustify example.cpp``，会得到如下格式差异：

.. code-block:: diff

   --- example.cpp
   +++ example.cpp.uncrustify
   @@ -1,9 +1,10 @@
   -  int main()
   -  {
   -       int a = 10;
   -       int b = 10;
   -       int c = 0;<trailing whitespace>
   -       if( a == b)<trailing whitespace>{
   - <tab>       c=a;}<trailing whitespace>
   -       return 0;
   -   }
   +int main()
   +{
   +  int a = 10;
   +  int b = 10;
   +  int c = 0;
   +  if (a == b) {
   +    c = a;
   +  }
   +  return 0;
   +}
   1 files with code style divergence

如果希望将这些修改应用到文件中，可以使用 ``--reformat`` 标志再次运行 ``ament_uncrustify``。

**指定该选项后，Uncrustify 会直接在原文件中应用必要修改。对于较大的代码库，这可以节省大量时间。**

6. 其他值得了解的 Ament 工具
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ROS Desktop Full 还包含一些值得了解的 Ament 开发工具：

* ``ament_lint_cmake``：检查 CMake 文件是否符合代码风格规范。
* ``ament_xmllint``：使用 xmllint 检查 XML 标记，例如 XML 启动文件。
* ``ament_pep257``：检查 Python 文档字符串是否符合 `PEP 257 <https://peps.python.org/pep-0257/>`_ 规范。

Ament 具有很强的可扩展性，鼓励 ROS 用户开发和使用能够提高开发效率的 Ament 工具。

可以使用 ``apt search`` 搜索社区贡献的其他 Ament lint 工具，也可以在 `ROS Index 中搜索 Ament <https://index.ros.org/?pkgs=ament&search_packages=true>`_。
