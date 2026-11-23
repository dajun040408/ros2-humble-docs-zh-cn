.. redirect-from::

    Source-Control-Best-Practices
    Contributing/Source-Control-Best-Practices

版本控制最佳实践
================

.. contents:: 目录
   :depth: 2
   :local:

简介
----

本页面介绍参与 ROS 2 项目时常见的源代码版本控制注意事项。它不能替代 Git 官方文档，而是侧重 ROS 项目的具体建议，并提供适当的外部参考资料。

避免提交生成文件和临时文件
--------------------------

ROS 2 工作空间会生成构建产物，通常不应提交到版本控制系统。

生成文件、临时文件和备份文件的来源
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

colcon 工作空间产物
~~~~~~~~~~~~~~~~~~~

常见工作空间产物包括：

.. code-block:: text

   build/
   install/
   log/

build/、install/ 和 log/ 目录由 colcon build 在 ROS 2 工作空间中生成，通常位于工作空间根目录，而不是单个 Git 仓库内部。

如果这些目录出现在仓库内部（例如不小心在错误目录运行了 colcon build），不应将它们提交到版本控制系统。

Python 生成文件
~~~~~~~~~~~~~~~

Python 运行程序时会生成临时文件，包括 __pycache__/ 目录，以及 *.pyc、*.pyo 和 *.pyd 文件。这些文件都不应提交到仓库。

IDE 配置文件
~~~~~~~~~~~~

编辑器和 IDE 经常生成项目级或用户级配置文件，例如：

.. code-block:: text

   .vscode/
   .idea/

许多 ROS 2 仓库会忽略这些编辑器配置文件。除非仓库明确要求，否则贡献者应避免提交个人编辑器配置。

编辑器临时文件和备份文件
~~~~~~~~~~~~~~~~~~~~~~~~

某些编辑器（例如 Vim）会创建以 ~ 结尾的备份文件（如 test.py~），以及以 *.swp、*.swo 等结尾的临时文件。这些文件不应提交到仓库。

操作系统文件
~~~~~~~~~~~~

操作系统可能生成元数据文件，例如 macOS 的 .DS_Store 和 Windows 的 Thumbs.db。这些文件不应提交到仓库。

提交前应检查提交中包含的文件，确保没有意外添加生成文件或临时文件。

.gitignore 的放置位置
---------------------

仓库级 .gitignore
^^^^^^^^^^^^^^^^^

判断文件应该放入仓库专用的 .gitignore，还是个人全局 .gitignore，可以参考以下原则：

* 如果该文件会出现在每个开发者的计算机上，应将其添加到仓库的 .gitignore。
* 如果该文件只与个人开发环境有关，应优先放入全局 .gitignore。
* 如果文件是构建工具生成的通用产物，应检查 ROS 2 仓库是否已有适用的忽略规则。

全局 .gitignore
^^^^^^^^^^^^^^^

可以通过 Git 配置全局忽略文件：

.. code-block:: console

   $ git config --global core.excludesfile ~/.gitignore_global

然后将个人 IDE 配置、操作系统元数据和其他本地临时文件添加到该文件中。

提交前检查
----------

在创建提交之前，使用 git status 和 git diff 检查修改：

.. code-block:: console

   $ git status
   $ git diff --stat
   $ git diff

如果发现生成文件或临时文件，应在提交前将其从暂存区移除，并在适当的 .gitignore 中添加规则。
