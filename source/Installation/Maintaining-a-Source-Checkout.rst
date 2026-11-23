.. _MaintainingSource:

维护源码检出
============

.. ifconfig:: smv_current_version != '' and smv_current_version != 'rolling'

  .. note::

     有关维护 ROS 2 **最新开发版本**源码检出的说明，请参阅
     §维护 ROS 2 Rolling 源码检出 <../../rolling/Installation/Maintaining-a-Source-Checkout.html>§_。

.. contents::
   :depth: 2
   :local:

如果你从源码安装了 ROS 2，那么自检出代码以来，源代码可能已经发生变化。

要使源码检出保持最新，需要定期更新 §ros2.repos§ 文件、下载最新源码，并重新构建工作空间。

更新仓库列表
------------

每个 ROS 2 发行版都包含一个 §ros2.repos§ 文件，其中列出了该发行版使用的代码仓库及其版本。

ROS 2 {DISTRO_TITLE} 分支的最新代码
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果希望检出 ROS 2 {DISTRO_TITLE} 的最新代码，可以运行以下命令获取对应的仓库列表：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ cd ~/ros2_{DISTRO}
       $ mv -i ros2.repos ros2.repos.old
       $ wget https://raw.githubusercontent.com/ros2/ros2/{REPOS_FILE_BRANCH}/ros2.repos

  .. group-tab:: macOS

    .. code-block:: console

       $ cd ~/ros2_{DISTRO}
       $ mv -i ros2.repos ros2.repos.old
       $ wget https://raw.githubusercontent.com/ros2/ros2/{REPOS_FILE_BRANCH}/ros2.repos

  .. group-tab:: Windows

    使用 Windows 命令行：

    .. code-block:: console

       $ cd \dev\ros2_{DISTRO}
       $ curl -sk https://raw.githubusercontent.com/ros2/ros2/{REPOS_FILE_BRANCH}/ros2.repos -o ros2.repos

    或使用 PowerShell：

    .. code-block:: console

       $ cd \dev\ros2_{DISTRO}
       $ curl https://raw.githubusercontent.com/ros2/ros2/{REPOS_FILE_BRANCH}/ros2.repos -o ros2.repos

更新本地仓库
------------

在 §ros2.repos§ 文件中，每个仓库都有一个 §version§，指向特定提交哈希、标签或分支名称。

这些版本可能指向新的标签/分支，而本地已经检出的仓库可能尚未识别这些引用，因为本地仓库较旧。因此，应使用以下命令更新已经检出的仓库：

.. code-block:: console

   $ vcs custom --args remote update

下载新源代码
------------

现在可以根据新的仓库列表下载源码：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ vcs import src < ros2.repos
       $ vcs pull src

  .. group-tab:: macOS

    .. code-block:: console

       $ vcs import src < ros2.repos
       $ vcs pull src

  .. group-tab:: Windows

   在 Windows 命令行中：

   .. code-block:: console

       $ vcs import --input ros2.repos src
       $ vcs pull src

   或在 PowerShell 中：

   .. code-block:: console

       $ vcs import --input ros2.repos src
       $ vcs pull src

重新构建工作空间
----------------

工作空间更新为最新源码后，删除之前的 install 目录，并重新构建工作空间，例如：

.. code-block:: console

   $ colcon build --symlink-install

检查源码检出状态
----------------

在开发过程中，你可能已经修改了工作空间，使其不再与最初导入仓库列表时的状态一致。

如果希望了解工作空间中各个仓库的版本，可以使用以下命令导出相关信息：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ cd ~/ros2_{DISTRO}
       $ vcs export src > my_ros2.repos

  .. group-tab:: macOS

    .. code-block:: console

       $ cd ~/ros2_{DISTRO}
       $ vcs export src > my_ros2.repos

  .. group-tab:: Windows

    .. code-block:: console

       $ cd \dev\ros2_{DISTRO}
       $ vcs export src > my_ros2.repos

随后可以将 §my_ros2.repos§ 文件分享给其他人，使他们能够复现你当前工作空间中各个仓库的状态。
