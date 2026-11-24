Ament Lint 命令行工具
=====================

**目标：** 学习如何使用 ``ament_lint`` 及相关工具发现并修复代码质量问题。

**教程级别：** 高级 | **预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

``ament`` 工具系列是用于 ROS 2 软件开发的 Python 工具。Ament 工具可以与任何构建系统配合使用，其中 ``ament_cmake`` 工具专门用于简化基于 CMake 的开发。

Ament 提供了一组命令行程序，帮助开发者编写符合 ROS 2 代码规范的代码。使用这些工具可以提高开发效率，并帮助 ROS 应用和核心代码符合:doc:`ROS 项目代码规范 <../../The-ROS2-Project/Contributing/Code-Style-Language-Versions>`。建议 ROS 开发者熟悉这些工具，并在提交 Pull Request 之前运行检查。

前置条件
--------

常规 ROS 2 安装环境中应已包含 ``ament`` 软件包。若需安装 ROS 2，请参阅 :doc:`安装说明 <../../Installation>`。

Ament Lint 命令行工具
---------------------

所有 ament lint 工具采用类似的命令行模式：接收一个或多个目录或文件，分析输入内容并生成报告。常见选项包括：

* ``-h, --help``：显示帮助信息。工具内置帮助通常是最准确、最新的说明。
* ``--exclude [filename ...]``：排除指定文件名，支持通配符。
* ``--xunit-file XUNIT_FILE``：生成符合 xUnit 格式的 XML 文件，常用于 IDE 和 CI 自动收集测试结果。

1. ament_copyright
^^^^^^^^^^^^^^^^^^

``ament_copyright`` 用于检查和更新 ROS 源代码中的版权声明，也可以检查是否包含适当的软件许可证、版权年份和版权持有人信息。

该工具以当前目录为起点，递归检查子目录中的源文件。可以在功能包、工作空间、普通目录或单个源文件范围内运行。

例如，只检查 ``src`` 和 ``include`` 目录：

.. code-block:: console

   $ ament_copyright ./src ./include

默认情况下，工具会递归扫描当前目录，并报告缺少版权声明的文件。它也可以自动为缺少声明的源文件添加版权和许可证信息。

2. 其他 Lint 工具
^^^^^^^^^^^^^^^^^

Ament lint 还提供多种代码质量检查工具，例如：

* ``ament_flake8``：检查 Python 代码风格。
* ``ament_pep257``：检查 Python 文档字符串规范。
* ``ament_cpplint``：检查 C++ 代码风格。
* ``ament_uncrustify``：根据配置格式化和检查 C/C++ 代码。
* ``ament_lint_cmake``：检查 CMake 文件规范。
* ``ament_xmllint``：检查 XML 文件格式。

运行具体工具时，建议先使用其 ``--help`` 选项确认参数和行为。

在功能包中集成
--------------

基于 CMake 的 ROS 2 功能包可以在测试阶段使用 ``ament_lint_auto`` 自动发现并运行 lint 依赖：

.. code-block:: cmake

   if(BUILD_TESTING)
     find_package(ament_lint_auto REQUIRED)
     ament_lint_auto_find_test_dependencies()
   endif()

在 ``package.xml`` 中声明测试依赖：

.. code-block:: xml

   <test_depend>ament_lint_auto</test_depend>
   <test_depend>ament_lint_common</test_depend>

总结
----

Ament lint 工具可以自动检查版权、代码风格、文档字符串、CMake 和 XML 等问题。建议在提交代码前运行相应工具，并将 lint 测试集成到功能包的 CI 流程中。
