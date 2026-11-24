将 package.xml 迁移到格式 2
=============================

.. contents:: 目录
   :depth: 2
   :local:

ROS 2 要求 package.xml 文件至少使用格式 2。格式 2 规范请参阅 REP-0140：https://reps.openrobotics.org/rep-0140/。
本指南介绍如何将 package.xml 从格式 1 迁移到格式 2。

如果 package.xml 开头的 ``<package>`` 标签看起来像下面任意一种形式，则表示它使用的是格式 1，必须进行迁移。

.. code-block:: xml

    <package>

.. code-block:: xml

    <package format="1">

前置条件
--------

你应当拥有一个可正常工作的 ROS 1 安装环境。
这样就可以通过构建和测试功能包来检查转换后的 package.xml 是否有效，因为 ROS 1 支持所有 package.xml 格式版本。

从格式 1 迁移到格式 2
----------------------

格式 1 和格式 2 在依赖项的声明方式上有所不同。
有关差异摘要，请阅读 REP-0140 中的兼容性章节：https://reps.openrobotics.org/rep-0140/#compatibility。

为 ``<package>`` 添加 format 属性
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

添加或设置 format 属性为 2，以表明 package.xml 使用格式 2。

.. code:: xml

  <package format="2">

替换 ``<run_depend>``
~~~~~~~~~~~~~~~~~

``<run_depend>`` 标签已不再允许使用。
如果你的依赖项采用如下声明方式：

.. code:: xml

  <run_depend>foo</run_depend>

则应将其替换为以下一个或两个标签：

.. code:: xml

  <build_export_depend>foo</build_export_depend>
  <exec_depend>foo</exec_depend>

如果依赖项在执行功能包中的某些内容时需要使用，则使用 ``<exec_depend>`` 标签。
如果依赖你的功能包的其他功能包在构建时需要该依赖项，则使用 ``<build_export_depend>`` 标签。
如果不确定，可以同时使用这两个标签。

将部分 ``<build_depend>`` 转换为 ``<test_depend>``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在格式 1 中，``<test_depend>`` 用于声明运行功能包测试时所需的依赖项。
在格式 2 中，它仍然用于此目的，同时还声明构建功能包测试时所需的依赖项。

由于格式 1 中该标签存在限制，你的功能包可能会将仅用于测试的依赖项声明为 ``<build_depend>``，例如：

.. code:: xml

  <build_depend>testfoo</build_depend>

如果是这种情况，请将其改为 ``<test_depend>``：

.. code:: xml

  <test_depend>testfoo</test_depend>

.. note::

    如果使用 CMake，请确保仅在 ``if(BUILD_TESTING)`` 代码块中引用测试依赖项：

    .. code:: cmake

        if (BUILD_TESTING)
            find_package(testfoo REQUIRED)
        endif()

开始使用 ``<doc_depend>``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

使用新的 ``<doc_depend>`` 标签声明构建功能包文档所需的依赖项。
例如，C++ 功能包可能需要声明：

.. code:: xml

  <doc_depend>doxygen</doc_depend>

而 Python 功能包可能需要声明：

.. code:: xml

  <doc_depend>python3-sphinx</doc_depend>

更多信息请参阅 :doc:`ROS 2 功能包文档编写指南 <../Documenting-a-ROS-2-Package>`。

使用 ``<depend>`` 简化依赖项
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``<depend>`` 是一个新标签，可以让 package.xml 文件更加简洁。
如果你的 ``package.xml`` 中针对同一个依赖项使用了以下三个标签：

.. code::

  <build_depend>foo</build_depend>
  <build_export_depend>foo</build_export_depend>
  <exec_depend>foo</exec_depend>

则可以将它们替换为一个 ``<depend>`` 标签：

.. code:: xml

  <depend>foo</depend>

测试新的 ``package.xml``
-----------------------------

像平常一样，使用 ``catkin_make``、``catkin_make_isolated`` 或 ``catkin`` 构建工具构建并测试功能包。
如果所有操作均成功，则说明 package.xml 有效。
