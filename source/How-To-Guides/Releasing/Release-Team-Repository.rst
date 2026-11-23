发布团队与发布仓库
====================

.. contents:: 目录
   :depth: 2
   :local:

本页面介绍在 `ros2-gbp <https://github.com/ros2-gbp>`_ 上托管发布仓库的推荐方法。

什么是 ROS 2 GBP？
-----------------

`ros2-gbp <https://github.com/ros2-gbp>`_ 是一个 GitHub 组织，用于托管 ROS 软件包的发布仓库。它还维护发布团队列表、各团队成员列表，以及由这些团队维护的发布仓库列表。相关信息保存在 `ros2-gbp-github-org <https://github.com/ros2-gbp/ros2-gbp-github-org>`_ 中。

与 `ros2-gbp-github-org` 的交互通过创建 GitHub Issue 完成。建议尽早申请加入发布团队并设置发布仓库，因为 ros2-gbp 维护者回复请求可能需要一些时间。

.. _what-is-a-release-team:

什么是发布团队？
----------------

发布团队是一个 `GitHub Team <https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams>`_，由一组负责一个或多个代码仓库发布流程的人员组成。

发布团队通常由一个组织、工作组甚至个人组成，并以其所代表的团队或组织命名。发布团队及其对应发布仓库的列表由 `ros2-gbp-github-org <https://github.com/ros2-gbp/ros2-gbp-github-org>`_ 维护。

**你必须属于计划发布项目的发布团队。**

如果计划通过现有团队发布，请按照 :ref:`加入发布团队 <join-a-release-team>` 操作。如果计划创建新团队，请按照 :ref:`创建新的发布团队 <start-a-new-release-team>` 操作。

.. _join-a-release-team:

加入发布团队
^^^^^^^^^^^^

如果项目已经有发布团队，但你尚未加入，请填写 `更新发布团队成员资格 Issue <https://github.com/ros2-gbp/ros2-gbp-github-org/issues/new?assignees=&labels=&template=update_release_team_membership.md&title=Update+release+team+membership>`_ 模板。

.. _start-a-new-release-team:

创建新的发布团队
^^^^^^^^^^^^^^^^

如果项目尚无发布团队，请填写 `新建发布团队 Issue <https://github.com/ros2-gbp/ros2-gbp-github-org/issues/new?assignees=&labels=&template=new_release_team.md&title=Add+release+team>`_ 模板，请求创建团队。

.. _what-is-a-release-repository:

什么是发布仓库？
----------------

发布仓库是一个代码仓库，用于：

* 存储发布流程生成的文件，供 ROS 构建农场使用。
* 缓存发布流程中的配置，以简化该仓库未来的后续发布。

在 ROS 2 中，发布仓库必须与源代码仓库分开。

.. _create-a-new-release-repository:

创建新的发布仓库
^^^^^^^^^^^^^^^^

如果你的仓库刚刚加入 ROS 社区，应首先向 `ros/rosdistro <https://github.com/ros/rosdistro>`_ 提交 Pull Request，为该仓库添加 `source` 条目（例如 `https://github.com/ros/rosdistro/pull/39513`）。

rosdistro 数据库的审查流程会确保你的仓库和软件包符合 `REP 144 软件包命名规范 <https://reps.openrobotics.org/rep-0144/>`_ 及其他要求。

软件包名称获得批准并合并后，如果项目尚无发布仓库，请填写 `添加新的发布仓库 Issue <https://github.com/ros2-gbp/ros2-gbp-github-org/issues/new?assignees=&labels=&template=new_release_repository.md&title=Add+new+release+repositories>`_ 模板。

如果现有发布仓库不在 ros2-gbp 组织中怎么办？
--------------------------------------------

ros2-gbp 成立之前发布的软件包，其发布仓库可能托管在其他位置。现在强烈建议将发布仓库放在这个专用 GitHub 组织中。

如果你正在将 ROS 1 软件包移植到 ROS 2，并计划首次向 ROS 2 发布软件包，请按照标准流程申请新的 ROS 2 发布仓库。

如果你此前已经为 ROS 2 发布过软件包，在创建 `添加新的发布仓库 Issue` 时，**请注明当前发布仓库的 URL**，其余步骤仍按照标准流程执行。

.. note::

   **向 Rolling 发行版发布软件包时，必须使用托管在 ros2-gbp 组织中的发布仓库。**

   如果不计划将仓库发布到 Rolling，那么对于稳定发行版，仍支持托管在其他位置的发布仓库。

   由于从 Rolling 创建的稳定发行版将使用 ros2-gbp 组织中的发布仓库，因此建议所有 ROS 2 发行版都使用 ros2-gbp 发布仓库，以避免发布信息分散。

   未来 ros2-gbp 发布仓库可能成为所有发行版的强制要求。所有 ROS 2 发行版使用单一发布仓库，也有助于简化 Rolling 发行版维护者和软件包维护者的发布维护工作。
