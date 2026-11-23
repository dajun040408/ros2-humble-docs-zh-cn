.. redirect-from::

  Guides/Using-Python-Packages
  Tutorials/Using-Python-Packages

.. _PythonPackages:

在 ROS 2 中使用 Python 软件包
=============================

**目标：** 说明如何在 ROS 2 生态系统中与其他 Python 软件包进行互操作。

.. contents:: 目录
    :depth: 2
    :local:

.. note::

    注意：如果你打算使用预先打包的二进制发行版（无论是 `deb` 文件还是二进制归档包），Python 解释器必须与构建这些二进制文件时使用的解释器一致。

    如果使用 `virtualenv` 或 `pipenv`，请确保使用系统解释器。如果使用 `conda`，其解释器很可能与系统解释器不一致，因此可能与 ROS 2 二进制软件包不兼容。

通过 rosdep 安装
----------------

引入第三方 Python 软件包最快的方式，是使用其对应的 rosdep key（如果存在）。

可以通过以下文件检查 rosdep key：

* `rosdep/base.yaml <https://github.com/ros/rosdistro/blob/master/rosdep/base.yaml>`_
* `rosdep/python.yaml <https://github.com/ros/rosdistro/blob/master/rosdep/python.yaml>`_

可以将这些 rosdep key 添加到 `package.xml`，以声明当前功能包及其依赖功能包对这些软件包的依赖。

在新的工作空间中，也可以通过以下命令快速安装所有 rosdep key：

.. code-block:: console

    $ rosdep install -yr --from-paths ./path/to/your/workspace

如果目标软件包目前还没有对应的 rosdep key，可以按照 :ref:`rosdep key 贡献指南 <rosdep key contribution guide>` 添加。

要了解 rosdep 工具及其工作原理，请参阅 :ref:`rosdep 文档 <rosdep documentation>`。

通过系统软件包管理器安装
------------------------

如果不希望创建 rosdep key，但该软件包已存在于系统软件包管理器中（例如 `apt`），可以直接安装并使用：

.. code-block:: console

    $ sudo apt install python3-serial

如果软件包位于 `PyPI <https://pypi.org/>`_，并且希望全局安装到系统中：

.. code-block:: console

    $ python3 -m pip install -U pyserial

如果希望将 PyPI 软件包仅安装到当前用户目录：

.. code-block:: console

    $ python3 -m pip install -U --user pyserial

通过虚拟环境安装
----------------

首先，创建一个 Colcon 工作空间：

.. code-block:: console

    $ mkdir -p ~/colcon_venv/src
    $ cd ~/colcon_venv/

然后创建并配置虚拟环境：

.. code-block:: console

    $ virtualenv -p python3 ./venv # 创建并激活虚拟环境
    $ source ./venv/bin/activate
    $ touch ./venv/COLCON_IGNORE # 确保 colcon 不会尝试构建虚拟环境

接下来，在虚拟环境中安装所需的 Python 软件包：

.. code-block:: console

    $ python3 -m pip install gtsam pyserial… etc

现在可以构建工作空间，并运行依赖于虚拟环境中软件包的 Python 节点：

.. code-block:: console

    $ source /opt/ros/{DISTRO}/setup.bash # source {DISTRO_TITLE} 并进行构建
    $ colcon build

.. note::

    如果希望使用 Bloom 发布你的功能包，应将所需软件包添加到 rosdep。具体请参阅 :ref:`rosdep key 贡献指南 <rosdep key contribution guide>`。

.. _rosdep key contribution guide: http://docs.ros.org/en/independent/api/rosdep/html/contributing_rules.html

.. _rosdep documentation: http://docs.ros.org/en/independent/api/rosdep/html/
