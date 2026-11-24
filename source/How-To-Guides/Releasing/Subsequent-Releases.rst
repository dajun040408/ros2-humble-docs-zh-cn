后续版本发布
============

本指南介绍如何发布已经发布过的 ROS 功能包的新版本。

.. contents:: 目录
   :depth: 1
   :local:

加入发行团队
------------

如果你不属于拥有发行仓库写入权限的发行团队，请按照 :ref:`加入发行团队 <join-a-release-team>` 的说明操作。

安装依赖项
----------

.. include:: _Install-Dependencies.rst

配置 Personal Access Token
--------------------------

.. include:: _Personal-Access-Token.rst

确保代码仓库为最新状态
----------------------

.. include:: _Ensure-Repositories-Are-Up-To-Date.rst

更新变更日志
------------

为了方便用户和开发者，请保持变更日志简洁且及时更新。

.. code-block:: console

   $ catkin_generate_changelog

.. include:: _Clean-Up-Changelog.rst

提升功能包版本号
----------------

.. include:: _Bump-Package-Version.rst

使用 Bloom 发布
---------------

运行以下命令，将 ``my_repo`` 替换为包含相关功能包的代码仓库名称：

.. code-block:: console

   $ bloom-release --rosdistro {DISTRO} my_repo

Bloom 会自动针对 `rosdistro <https://github.com/ros/rosdistro>`_ 仓库为你创建 Pull Request。

.. note::

  默认情况下，Bloom 会发布源码仓库中的所有功能包。如果希望在某个 ``{DISTRO}`` 发行版中选择性地阻止部分功能包发布，可以在发行仓库的 ``master`` 分支中添加 ``{DISTRO}.ignored`` 文件。每个文件中每行列出一个需要阻止发布的功能包名称。

  `rosidl-release <https://github.com/ros2-gbp/rosidl-release>`_ 仓库可以作为该配置的参考。

后续步骤
--------

.. include:: _Next-Steps.rst
