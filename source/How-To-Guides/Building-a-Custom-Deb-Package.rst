.. redirect-from::

  Guides/Building-a-Custom-Debian-Package
  How-To-Guides/Building-a-Custom-Debian-Package

构建自定义 deb 软件包
=====================

许多 Ubuntu 用户通过安装 :doc:`deb 软件包 <../Installation/Ubuntu-Install-Debs>` 在系统中安装 ROS 2。本指南简要介绍如何在本地构建自定义 deb 软件包。

.. contents:: 目录
   :local:

前置条件
--------

要成功构建自定义软件包，待构建软件包的所有依赖项都必须能够在本地找到，或能够通过 rosdep 获取。此外，软件包的所有依赖项都应在其 `package.xml` 文件中正确声明。

安装依赖项
----------

运行以下命令安装构建所需的工具：

.. code-block:: console

  $ sudo apt install python3-bloom python3-rosdep fakeroot debhelper dh-python

初始化 rosdep
-------------

运行以下命令初始化 rosdep 数据库：

.. code-block:: console

  $ sudo rosdep init
  $ rosdep update

注意，如果此前已经初始化过 rosdep，``rosdep init`` 命令可能会失败；这种情况可以安全忽略。

从功能包构建 deb
----------------

运行以下命令构建 deb 软件包：

.. code-block:: console

  $ cd /path/to/pkg_source  # 此目录应包含 package.xml
  $ bloom-generate rosdebian
  $ fakeroot debian/rules binary

如果所有必需依赖项都已具备，并且编译成功，新生成的软件包将位于当前目录的父目录中。
