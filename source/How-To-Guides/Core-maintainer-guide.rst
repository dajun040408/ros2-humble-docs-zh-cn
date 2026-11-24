.. redirect-from::

  Guides/Package-maintainer-guide
  How-To-Guides/Package-maintainer-guide

ROS 2 核心软件包维护者指南
==========================

ROS 2 核心中的每个软件包都有一个或多个维护者，负责维护软件包的整体健康状态。本指南介绍 ROS 2 核心软件包维护者的职责。

.. contents:: 目录
   :local:

持续集成
--------

所有提交到 ROS 2 核心代码仓库的代码都必须经过持续集成（CI）。ROS 2 目前有两套独立的 CI 系统，Pull Request 必须通过两套系统的检查后才能合并。

PR 构建（https://build.ros2.org/view/Rpr）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

每当创建 Pull Request 时，ROS 2 PR 构建都会自动运行。这些构建只会构建并测试当前代码仓库，不会构建其依赖项，也不会构建依赖于当前仓库中软件包的其他仓库。

PR 构建适合快速反馈，例如检查代码是否通过 lint、单元测试等。它有两个主要限制：

* 无法跨多个代码仓库构建，因此不适合添加或修改 API 等涉及多个仓库的变更。
* 测试只在 Linux 上运行，不会在 macOS 或 Windows 上运行。

为解决这些问题，还需要使用 CI 构建。

CI 构建（https://ci.ros2.org）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

创建 Pull Request 时不会自动运行 CI 构建。仓库维护者必须访问 ``https://ci.ros2.org/job/ci_launcher/``，手动请求执行 CI 构建。

默认情况下，运行该任务会在所有平台（Linux、macOS 和 Windows）上构建并测试全部软件包（目前超过 300 个）。完整构建可能需要数小时，并占用 CI 机器，因此建议限制每次构建和测试的软件包数量。

可以使用 colcon 参数 ``--packages-up-to``、``--packages-select``、``--packages-above-and-dependencies``、``--packages-above`` 等实现限制。更多示例请参阅 `colcon 文档 <https://colcon.readthedocs.io/en/released/user/how-to.html#build-only-a-single-package-or-selected-packages>`_。CI 工具的详细使用说明见 ``CI_BUILDERS.md <https://github.com/ros2/ci/blob/master/CI_BUILDERS.md>`_。

合并 Pull Request
-----------------

满足以下所有条件后，Pull Request 才可以合并：

* DCO bot 检查通过。
* PR 构建检查通过。
* CI 构建在所有平台上均通过。
* 至少一名维护者完成审查并批准该 PR。

有关 PR 审查流程的更多信息，请参阅 :doc:`审查 Pull Request <../The-ROS2-Project/Contributing/Contributing-to-code/Reviewing-a-PR>`。

PR 合并后，会自动在下一轮 `nightly 构建 <https://ci.ros2.org/view/nightly>`_ 中构建。强烈建议在合并后检查 nightly 构建，以确保没有引入回归问题。

保持 CI 通过
------------

nightly 任务运行的测试通常比单个 Pull Request 的检查更加全面。因此，nightly 构建中可能出现 PR CI 未发现的回归问题。

维护者有责任在以下位置检查自己软件包的回归问题：

* https://ci.ros2.org/view/nightly
* https://ci.ros2.org/view/packaging
* https://build.ros2.org/view/Rci
* https://build.ros2.org/view/Rdev

发现问题后，应在相关代码仓库中创建新的 issue 和/或 Pull Request。

发布新版本
----------

为了让最终用户获得新功能和缺陷修复，维护者必须定期发布代码仓库的新版本（其他维护者也可以按需请求发布）。

如 :ref:`开发者指南 <semver>` 所述，ROS 2 软件包的版本号遵循语义化版本（semver）。

ROS 中的发布包含两个独立步骤：源码发布和二进制发布。

源码发布
^^^^^^^^

源码发布会在相关代码仓库中生成变更日志并创建标签。

首先，使用以下命令生成或更新 ``CHANGELOG.rst`` 文件：

.. code-block:: console

  $ catkin_generate_changelog

如果仓库中一个或多个软件包尚无 ``CHANGELOG.rst``，可以添加 ``--all`` 选项，将每个软件包此前的所有提交记录填入变更日志。``catkin_generate_changelog`` 只是将仓库提交日志写入文件。由于提交日志并不总适合作为变更日志，建议编辑 ``CHANGELOG.rst``，使其更易阅读。编辑完成后，应将更新后的文件提交到仓库。

接下来，使用以下命令更新 ``package.xml`` 和变更日志中的版本号：

.. code-block:: console

  $ catkin_prepare_release

该命令会查找仓库中的所有软件包，检查变更日志是否存在、是否有未提交的本地修改，递增 ``package.xml`` 中的版本号，并使用兼容 Bloom 的标签提交这些变更。

默认情况下，``catkin_prepare_release`` 会提升软件包的补丁版本，例如 ``0.1.1 -> 0.1.2``。也可以提升次版本号或主版本号，或者指定精确版本。更多信息请查看该命令的帮助输出。

上述步骤成功完成后，即完成源码发布。

二进制发布
^^^^^^^^^^

下一步使用 ``bloom-release`` 命令创建二进制发行版。Bloom 的完整使用说明请参阅 ``http://wiki.ros.org/bloom``。

发布代码仓库的二进制版本，请运行：

.. code-block:: console

  $ bloom-release --track <rosdistro> --rosdistro <rosdistro> <repository_name>

例如，将 ``rclcpp`` 仓库发布到 {DISTRO_TITLE} 发行版：

.. code-block:: console

  $ bloom-release --track {DISTRO} --rosdistro {DISTRO} rclcpp

该命令会获取发行仓库、进行发布所需的修改、推送修改到发行仓库，最后在 ``https://github.com/ros/rosdistro`` 创建 Pull Request。

向已发布发行版回移植
--------------------

所有新变更都应首先合并到开发分支。变更合并到开发分支后，才可以考虑回移植到已发布的发行版。

不过，回移植的代码不得破坏已发布发行版的 API 或 ABI。如果某项变更能够在不破坏 API 或 ABI 的情况下回移植，则应针对相应分支创建新的 Pull Request，并将该 PR 添加到对应发行版的项目看板：``https://github.com/orgs/ros2/projects``。

新的 Pull Request 仍需执行前面介绍的所有步骤，并确保 CI 等检查针对相应发行版运行。

响应 Issue
----------

软件包维护者还应关注仓库中收到的 Issue，并对用户遇到的问题进行分类处理。

如果 Issue 看起来只是一个问题咨询，应关闭该 Issue，并引导用户前往 `Robotics Stack Exchange <https://robotics.stackexchange.com/>`_。

如果 Issue 描述的问题确实存在，但与当前代码仓库无关，应使用 GitHub 的“Transfer issue”按钮将其转移到合适的仓库。

如果报告者提供的信息不足以确定问题原因，应向报告者请求更多信息。

如果是新功能请求，应为 Issue 添加 ``help-wanted`` 标签。

其余问题都应尝试复现，并判断是否确实属于缺陷。如果确认是缺陷，欢迎提交修复。

获取帮助
--------

在维护软件包的过程中，可能会遇到有关通用流程或具体问题的疑问。

对于一般性问题，请遵循 :doc:`贡献指南 <../The-ROS2-Project/Contributing>`。

对于具体 Issue 的问题，请标记 ROS 2 GitHub 团队（``@ros/team``），团队成员会进行查看。
