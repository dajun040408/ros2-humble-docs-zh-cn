首次发布
========

本指南介绍如何发布此前从未发布过的 ROS 2 软件包。

由于 ROS 软件包发布时有许多可选项，本指南重点介绍最常见的场景，不会涵盖所有特殊情况。

.. contents:: 目录
   :depth: 1
   :local:

加入发布团队
------------

你必须属于一个 :ref:`发布团队 <what-is-a-release-team>`。

如果尚未加入发布团队，请选择以下方式之一：

* :ref:`加入发布团队 <join-a-release-team>`。
* :ref:`创建新的发布团队 <start-a-new-release-team>`。

创建新的发布仓库
----------------

发布软件包需要一个 :ref:`发布仓库 <what-is-a-release-repository>``。请按照 :ref:``创建新的发布仓库 <create-a-new-release-repository>` 操作。

安装依赖项
----------

.. include:: _Install-Dependencies.rst

设置 Personal Access Token
--------------------------

.. include:: _Personal-Access-Token.rst

确保仓库为最新状态
------------------

.. include:: _Ensure-Repositories-Are-Up-To-Date.rst

生成变更日志
------------

使用以下命令，为仓库中的每个软件包生成 ``CHANGELOG.rst`` 文件：

.. code-block:: console

   $ catkin_generate_changelog --all

.. include:: _Clean-Up-Changelog.rst

提升软件包版本号
----------------

.. include:: _Bump-Package-Version.rst

使用 Bloom 发布
---------------

运行以下命令，将 ``my_repo`` 替换为你的仓库名称：

.. code-block:: console

  $ bloom-release --new-track --rosdistro {DISTRO} --track {DISTRO} my_repo

.. tip::

   * ``--new-track`` 表示让 Bloom 创建并配置新的 :ref:`发布轨道 <what-is-a-track>`。
   * ``--rosdistro {DISTRO}`` 表示本次发布面向 ``{DISTRO}`` 发行版。
   * ``--track {DISTRO}`` 表示将轨道名称设置为 ``{DISTRO}``。

随后，系统会提示你输入信息以配置新的发布轨道。

以下是一个常见场景：

* 你的软件包位于名为 ``my_repo`` 的仓库中。
* 你要发布的分支名为 ``main``。
* 源码仓库托管在 GitHub：``https://github.com/my_organization/my_repo.git``。
* 发布仓库位于：``https://github.com/ros2-gbp/my_repo-release.git``。

对于提示信息，应按以下方式填写：

.. list-table::
   :header-rows: 1
   :widths: 1 2

   * - 配置项
     - 值
   * - :ref:`发布仓库 URL <release-repository-url>`
     - ``https://github.com/ros2-gbp/my_repo-release.git``
   * - :ref:`仓库名称 <repository-name>`
     - ``my_repo``
   * - :ref:`上游仓库 URI <upstream-repository-uri>`
     - ``https://github.com/my_organization/my_repo.git``
   * - :ref:`上游 VCS 类型 <upstream-vcs-type>`
     -
   * - :ref:`版本 <version>`
     -
   * - :ref:`发布标签 <release-tag>`
     -
   * - :ref:`上游开发分支 <upstream-devel-branch>`
     - ``main``
   * - :ref:`ROS 发行版 <ros-distro>`
     -
   * - :ref:`补丁目录 <patches-directory>`
     -
   * - :ref:`发布仓库推送 URL <release-repository-push-url>`
     -

.. note::

  表格中的空单元格表示使用默认值。只需在 Bloom 提示时直接按 Enter 即可。

Bloom 会自动针对 `rosdistro <https://github.com/ros/rosdistro>`_ 仓库创建 Pull Request。

.. note::

  默认情况下，Bloom 会发布源码仓库中的所有软件包。如果希望针对某个 ``{DISTRO}`` 发行版选择性地阻止部分软件包发布，可以在发布仓库的 ``master`` 分支中添加 ``{DISTRO}.ignored`` 文件。

  每个文件中每行列出一个需要阻止发布的软件包名称。

  `rosidl-release <https://github.com/ros2-gbp/rosidl-release>`_ 仓库可以作为该配置的参考。

后续步骤
--------

.. include:: _Next-Steps.rst
