.. _TestingPython:

使用 Python 编写基础测试
========================

本教程假设你已经创建了一个基础的 :ref:`ament_python 功能包 <CreatePkg>`，现在希望为它添加一些测试。

如果你使用的是 ament_cmake_python，请参阅 :doc:`ament_cmake_python 文档 <../../../How-To-Guides/Ament-CMake-Python-Documentation>``，了解如何让测试能够被发现。测试内容以及通过 ``colcon` 调用测试的方式保持不变。

功能包配置
----------

setup.py
^^^^^^^^

在 ``setup.py`` 中，``setup(...)`` 调用必须声明对 ``pytest`` 的测试依赖：

.. code-block:: python

    tests_require=['pytest'],

测试文件和目录
^^^^^^^^^^^^^^

测试代码需要放在功能包根目录下名为 ``tests`` 的文件夹中。

所有希望运行的测试文件都必须采用 ``test_FOO.py`` 的命名形式，其中 ``FOO`` 可以替换为任意名称。

示例功能包目录结构：

.. code-block::

  awesome_ros_package/
    awesome_ros_package/
        __init__.py
        fozzie.py
    package.xml
    setup.cfg
    setup.py
    tests/
        test_init.py
        test_copyright.py
        test_fozzie.py

测试内容
--------

现在，你可以根据需要编写测试。`pytest <https://docs.pytest.org>`_ 提供了大量资源。简单来说，你可以编写以 ``test_` 为前缀的函数，并在其中加入所需的 assert 断言。

.. code-block:: python

  def test_math():
      assert 2 + 2 == 5   # 对大多数数学系统而言，该断言应该失败

运行测试
--------

有关如何运行测试以及检查测试结果的更多信息，请参阅 :doc:`通过命令行运行测试的教程 <CLI>`。

特殊命令
--------

除了 :doc:`标准 colcon 测试命令 <CLI>`` 外，你还可以使用 ``--pytest-args`` 标志，从命令行向 ``pytest` 框架传递参数。

例如，可以指定要运行的测试函数名称：

.. tabs::

  .. group-tab:: Linux/macOS

      .. code-block:: console

         $ colcon test --packages-select <name-of-pkg> --pytest-args -k name_of_the_test_function

  .. group-tab:: Windows

      .. code-block:: console

         $ colcon test --merge-install --packages-select <name-of-pkg> --pytest-args -k name_of_the_test_function

如果希望在运行测试时查看 pytest 输出，可以使用以下标志：

.. code-block:: console

  $ colcon test --event-handlers console_cohesion+
