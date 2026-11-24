.. _TestingCLI:

在 ROS 2 中通过命令行运行测试
=============================

前置条件
--------

你需要准备一个工作空间，其中包含带有测试的功能包。

.. _colcon-run-the-tests:

构建并运行测试
--------------

要编译并运行测试，只需在工作空间根目录使用 `colcon` 的 `test` 动词：

.. code-block:: console

  $ colcon test --ctest-args tests [package_selection_args]

其中 `package_selection_args` 是可选的功能包选择参数，可用于限制 `colcon` 构建和运行哪些功能包。更多信息请参阅 `colcon 关于功能包选择参数的文档 <https://colcon.readthedocs.io/en/released/reference/package-selection-arguments.html>`_。

测试之前通常不需要 :ref:`source 工作空间 <colcon-tutorial-source-the-environment>`。`colcon test` 会确保测试在正确的环境中运行，并能够访问所需依赖项。

查看测试结果
------------

要查看测试结果，请运行 `colcon` 的 `test-result` 动词：

.. code-block:: console

  $ colcon test-result --all

如果要查看具体哪些测试用例失败，可以添加 `--verbose` 标志：

.. code-block:: console

  $ colcon test-result --all --verbose

使用 GDB 调试测试
-----------------

有关使用 GDB 调试测试的详细说明，请参阅 :doc:`GDB 教程 <../../../How-To-Guides/Getting-Backtraces-in-ROS-2>`。
