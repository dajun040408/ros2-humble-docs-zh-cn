迁移 package.xml 到格式 2
===========================

.. contents:: 目录
   :depth: 2
   :local:

ROS 2 要求 `package.xml` 至少使用 `格式 2 <https://reps.openrobotics.org/rep-0140/>`_。本指南介绍如何将 `package.xml` 从格式 1 迁移到格式 2。

如果 `package.xml` 开头的 `<package>` 标签如下所示，则说明使用的是格式 1，必须进行迁移：

.. code-block:: xml

    <package>

.. code-block:: xml

    <package format="1">

前置条件
--------

你应当有一个可正常工作的 ROS 1 安装环境。这样就可以通过构建和测试功能包，检查转换后的 `package.xml` 是否有效，因为 ROS 1 支持所有 `package.xml` 格式版本。

从格式 1 迁移到格式 2
---------------------

格式 1 和格式 2 在依赖项声明方式上有所不同。差异概述请参阅 `REP-0140 兼容性章节 <https://reps.openrobotics.org/rep-0140/#compatibility>`_。

为 <package> 添加 format 属性
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

添加或设置 `format` 属性为 `2`，表示 `package.xml` 使用格式 2：

.. code-block:: xml

  <package format="2">

替换 <run_depend>
~~~~~~~~~~~~~~~~~

`<run_depend>` 标签不再允许使用。如果依赖项声明如下：

.. code-block:: xml

  <run_depend>foo</run_depend>

则将其替换为以下一个或两个标签：

.. code-block:: xml

  <build_export_depend>foo</build_export_depend>
  <exec_depend>foo</exec_depend>

如果依赖项在执行功能包中的内容时需要使用，则使用 `<exec_depend>`。如果依赖于当前功能包的其他功能包在构建时需要该依赖项，则使用 `<build_export_depend>`。如果不确定，可以同时使用这两个标签。

将部分 <build_depend> 转换为 <test_depend>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在格式 1 中，`<test_depend>` 用于声明运行功能包测试时所需的依赖项。在格式 2 中，它仍然具有这一作用，同时还声明构建功能包测试所需的依赖项。

由于格式 1 中该标签存在限制，你的功能包可能会将仅用于测试的依赖项声明为 `<build_depend>`，例如：

.. code-block:: xml

  <build_depend>testfoo</build_depend>

此时应将其改为 `<test_depend>`：

.. code-block:: xml

  <test_depend>testfoo</test_depend>

.. note::

    如果使用 CMake，请确保测试依赖项只在 `if(BUILD_TESTING)` 块中引用：

    .. code-block:: cmake

        if (BUILD_TESTING)
            find_package(testfoo REQUIRED)
        endif()

开始使用 <doc_depend>
~~~~~~~~~~~~~~~~~~~~~~

使用新增的 `<doc_depend>` 标签声明构建功能包文档所需的依赖项。

例如，C++ 功能包可能需要：

.. code-block:: xml

  <doc_depend>doxygen</doc_depend>

Python 功能包可能需要：

.. code-block:: xml

  <doc_depend>python3-sphinx</doc_depend>

更多信息请参阅 :doc:`编写 ROS 2 功能包文档指南 <../Documenting-a-ROS-2-Package>`。

使用 <depend> 简化依赖项
~~~~~~~~~~~~~~~~~~~~~~~~~

`<depend>` 是一个新增标签，可以让 `package.xml` 更简洁。

如果 `package.xml` 对同一个依赖项包含以下三个标签：

.. code-block:: xml

  <build_depend>foo</build_depend>
  <build_export_depend>foo</build_export_depend>
  <exec_depend>foo</exec_depend>

则可以用一个 `<depend>` 替换：

.. code-block:: xml

  <depend>foo</depend>

测试新的 package.xml
--------------------

按照平时的方式，使用 `catkin_make`、`catkin_make_isolated` 或 `catkin` 构建工具构建并测试功能包。若所有测试都通过，则说明 `package.xml` 已正确转换。
