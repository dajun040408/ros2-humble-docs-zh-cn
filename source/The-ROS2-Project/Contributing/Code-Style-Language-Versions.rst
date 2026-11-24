.. redirect-from::

  Contributing/Code-Style-Language-Versions

.. _CodeStyle:

代码风格与语言版本
==================

.. contents:: 目录
   :depth: 2
   :local:

为了确保产品风格一致，ROS 2 开发者应尽可能遵循各编程语言已有的外部风格指南。对于功能包布局、文档布局等没有统一外部标准的内容，则需要结合当前流行实践制定自己的规范。

建议开发者在编辑器中集成工具，自动检查是否遵循这些规范。例如，每个人都应在编辑器中启用 PEP8 检查器，以减少代码审查中与风格相关的反复修改。

在条件允许的情况下，功能包也应在单元测试中检查代码风格，以便自动发现问题。参见`ament_lint_auto <https://github.com/ament/ament_lint/blob/{REPOS_FILE_BRANCH}/ament_lint_auto/doc/index.rst>`_。

C
-

标准
^^^^

目标标准为 C99。

风格
^^^^

采用 `Python PEP7 <https://www.python.org/dev/peps/pep-0007/>`_ 作为 C 语言风格指南，并做如下调整：

* 目标为 C99，不需要像 PEP7 建议的那样兼容 C89。
  * 这样可以同时使用 // 和 /* */ 注释。
  * C99 目前已得到广泛支持。
* 允许使用 C++ 风格的 // 注释。
* （可选）比较运算时始终将字面量放在左侧，例如 0 == ret，而不是 ret == 0。
  * 这样可以降低意外将 == 写成 = 的风险。
  * 此项为可选，因为现代编译器在启用 -Wall 等警告后通常会提示此类问题。

以下修改仅适用于非 Python 模块：

* 不要将 ``Py_`` 作为所有符号的统一前缀，应使用功能包名称的 CamelCase 形式或其他合适前缀。
* 文档字符串相关要求不适用。

可以使用`pep7 <https://github.com/mike-perdide/pep7>`_ Python 模块检查风格。

C++
---

标准
^^^^

{DISTRO_TITLE} 的目标标准为 C++17。

风格
^^^^

采用`Google C++ Style Guide <https://google.github.io/styleguide/cppguide.html>`_，并做以下调整。

行长度
~~~~~~

最大行长度为 100 个字符。

文件扩展名
~~~~~~~~~~

* 头文件使用 .hpp 扩展名，以便工具区分 C++ 和 C 文件。
* 实现文件使用 .cpp 扩展名。

变量命名
~~~~~~~~

* 全局变量使用小写加下划线，并以 ``g_`` 为前缀。
* 局部变量和成员变量遵循 Google C++ 风格指南。
* 命名应清楚表达变量用途，避免使用容易产生歧义的缩写。

Python
------

标准
^^^^

Python 代码使用当前 ROS 发行版支持的 Python 3 版本。版本要求请参阅`REP 2000 <https://reps.openrobotics.org/rep-2000/>`_。

风格
^^^^

采用`PEP 8 <https://peps.python.org/pep-0008/>`_ 作为 Python 代码风格指南，并使用 PEP 257 文档字符串规范。

建议在编辑器中集成 flake8 或其他兼容工具，并在测试阶段运行 ament_python_lint 或 ament_lint_auto。

XML
---

XML 文件应保持一致的缩进和清晰的层级结构。package.xml、启动文件和其他配置文件应避免不必要的空白、重复标签和难以理解的嵌套。

版本和兼容性
------------

ROS 2 核心软件包应使用目标发行版规定的语言标准和工具链版本。具体版本请参阅`REP 2000 <https://reps.openrobotics.org/rep-2000/>`_。

如果修改涉及 API 或 ABI 兼容性，应在代码审查中明确说明，并遵循 ROS 发行版的兼容性策略。
