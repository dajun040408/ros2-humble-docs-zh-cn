.. redirect-from::

    Contributing/Contributing-To-ROS-2-Documentation

参与 ROS 2 文档贡献
===================

.. contents:: 目录
   :depth: 2
   :local:

欢迎为 ROS 2 文档网站贡献内容。本页面介绍如何参与 ROS 2 文档开发。提交贡献前，请仔细阅读以下说明。

文档网站使用`Sphinx <https://www.sphinx-doc.org/en/master/>`_ 构建，并使用`Sphinx multiversion <https://sphinx-contrib.github.io/multiversion/main/index.html>`_ 管理多个发行版。

分支结构
--------

文档源代码位于`ROS 2 Documentation GitHub 仓库 <https://github.com/ros2/ros2_documentation>`_。仓库为每个 ROS 2 发行版维护一个分支，以处理不同发行版之间的差异。

如果变更适用于所有 ROS 2 发行版，应提交到 rolling 分支，之后会根据需要回移植到其他分支。如果变更只适用于某个特定发行版，则应提交到对应发行版分支。

源代码结构
----------

网站源文件位于 source 子目录中。各种 Sphinx 插件的模板位于 source/_templates。仓库根目录包含配置文件以及用于本地构建网站进行测试的文件。

在本地构建网站
--------------

首先创建 Python 虚拟环境：

.. code-block:: console

   $ python3 -m venv ros2doc
   $ source ros2doc/bin/activate

安装 requirements.txt 中列出的依赖项：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ pip install -r requirements.txt -c constraints.txt

  .. group-tab:: macOS

    .. code-block:: console

       $ pip install -r requirements.txt -c constraints.txt

  .. group-tab:: Windows

    .. code-block:: console

      $ python -m pip install -r requirements.txt -c constraints.txt

为了让 Sphinx 能够生成图表，系统中必须可以使用 dot 命令。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ sudo apt update
       $ sudo apt install graphviz

  .. group-tab:: macOS

    .. code-block:: console

      $ brew install graphviz

  .. group-tab:: Windows

    从`Graphviz 下载页面 <https://graphviz.gitlab.io/_pages/Download/Download_windows.html>`_ 下载并安装程序。安装时确保允许安装器将其添加到 Windows PATH，否则 Sphinx 将无法找到它。

构建单个分支的网站
^^^^^^^^^^^^^^^^^^

如果只构建当前分支的网站，在仓库顶层运行：

.. code-block:: console

   $ make html

这是测试本地文档变更的推荐方式。构建过程可能需要一些时间。完成后，生成的 HTML 页面位于 build/html 目录中。

构建所有分支
^^^^^^^^^^^^

如果希望使用 Sphinx multiversion 构建多个发行版，可以使用仓库提供的构建目标。构建所有分支通常比单分支构建耗时更长。

提交文档变更
------------

文档变更应遵循以下原则：

* 保持内容清晰、准确，并使用一致的术语。
* 新增页面时，更新相应的 toctree，确保页面能够通过导航访问。
* 添加或修改内部链接时，确保引用的文档路径和锚点正确。
* 代码示例应尽可能完整，并确保与对应 ROS 发行版兼容。
* 图片应放在合适的资源目录中，并添加有意义的替代文本。
* 尽量在本地运行 Sphinx 构建，确认没有格式错误和链接错误。

提交 Pull Request
-----------------

将修改提交到自己的 fork，并向 ros2/ros2_documentation 对应分支创建 Pull Request。描述中应说明修改目的、影响范围，以及是否涉及特定发行版。

ROS 2 文档仓库的 Pull Request 需要 Developer Certificate of Origin（DCO）签署。使用 Git 提交时，可以通过以下命令签署：

.. code-block:: console

   $ git commit --signoff

更多信息请参阅`DCO <https://developercertificate.org/>`_。
