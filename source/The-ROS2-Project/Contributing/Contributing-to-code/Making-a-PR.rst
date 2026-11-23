创建 Pull Request（PR）指南
=============================

Pull Request 用于向 ROS 项目贡献代码和文档变更。本文介绍如何从 ROS 仓库的 fork 准备并创建 Pull Request。

**领域：** 贡献、社区 | **内容类型：** 操作指南 | **适用经验：** 初级、中级、专家

.. contents:: 目录
   :depth: 2
   :local:

概述
----

`Pull Request（PR）<https://docs.github.com/en/pull-requests>`_ 是将变更合并到 ROS 仓库的提案。通过创建 PR，你可以与其他 ROS 贡献者协作，在 ROS 维护者合并代码之前讨论并审查代码变更。

欢迎向任何`ROS 仓库 <https://github.com/ros2>`_ 提交 Pull Request。有关贡献行为规范，请参阅 :doc:`参与贡献 </The-ROS2-Project/Contributing>`。

前置条件
--------

#. 为目标 ROS 仓库`创建 fork <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo>`_。
#. 在 fork 中基于 **rolling** 分支创建开发分支，并在该分支上完成代码修改。
#. 确保修改符合 ROS 指南。

   * 如果 Pull Request 涉及代码变更：

     * 遵循 :doc:`开发者指南 </The-ROS2-Project/Contributing/Developer-Guide>`。
     * 检查代码是否符合 :doc:`代码风格指南 </The-ROS2-Project/Contributing/Code-Style-Language-Versions>`。
     * 确保已经 :ref:`运行测试 <colcon-run-the-tests>`，并针对代码变更运行适当的 linter。

   * 如果 Pull Request 涉及文档变更：

     * 遵循 :doc:`ROS 2 文档贡献指南 </The-ROS2-Project/Contributing/Contributing-To-ROS-2-Documentation>`。

步骤
----

1. 准备 Pull Request
^^^^^^^^^^^^^^^^^^^^

* **范围与重点**

  * 每个 Pull Request 只包含一个定义明确的变更。
  * 无关变更应拆分为独立的 Pull Request。
  * 保持补丁规模较小，避免不必要或附带的修改。

* **提交历史与压缩提交**

  * 将变更压缩为数量尽可能少、语义清晰的提交，以保持项目历史易于阅读。
  * Pull Request 处于审查期间时，不要压缩提交，否则审查者可能无法注意到新变更。
  * PR 审查期间可以继续创建新的提交。

* **草稿 Pull Request**

  * 使用 Draft Pull Request 在开发过程中提前征求反馈。
  * 在将草稿标记为 Ready 之前，不应期待它得到正式审查或合并。
  * 如果希望特定人员提前审查草稿 PR，可以在 PR 描述或评论中通过 `@` 提及对方。

* **提及与引用**

  * 如果变更基于设计文档（例如 REP），请在 PR 描述中提及参与设计的其他人员，例如审查过该 REP 的人员。
  * 如果 PR 依赖另一个 PR，请在描述中明确说明依赖关系，并使用 `#` 格式注明 PR 编号。
  * 如果计划将变更纳入某个特定 ROS 版本，请在 PR 描述中注明该 ROS 版本。

* **记录代码变更**

  * 如果 PR 涉及代码变更，应尽量在同一个 PR 中更新相关文档，包括 API 文档、功能文档和发行说明。

2. 提交 Pull Request
^^^^^^^^^^^^^^^^^^^^

#. 从包含变更的 fork 分支向目标 ROS 仓库的 **rolling** 分支创建 Pull Request。可以使用 GitHub CLI、GitHub Desktop 或 GitHub Web 界面创建 PR。

   有关从 fork 创建 PR 的说明，请参阅`GitHub 文档 <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork>`_。有关其他创建方式，请参阅`GitHub 文档 <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_。

#. 按照描述模板填写 PR 内容，包括：

   * **Description：** 总结代码变更，通过编号链接相关 GitHub Issue 和 PR，并突出关键点或需要关注的问题。
   * **Issue：** 使用 `Fixes #(issue)` 格式填写本次修改修复的 GitHub Issue 编号。PR 合并后，该 Issue 会自动关闭。
   * **Generative AI：** 如果该 PR 使用生成式 AI 创建，请注明模型及版本，例如 GitHub Copilot v3.2。
   * **Additional information：** 提供有助于理解本次变更的其他背景信息。

#. 勾选 `Allow edits by maintainers <https://github.blog/news-insights/product-news/improving-collaboration-with-forks/>`_，方便 ROS 维护者在必要时直接进行小幅修改。

提交 PR 后，ROS 社区中的其他开发者和贡献者会审查你的变更，并检查其是否符合相关指南。

3. 响应审查意见
^^^^^^^^^^^^^^

当其他开发者或贡献者向 PR 添加审查意见或建议时，你会收到 GitHub 通知。

可以直接在 GitHub 中查看并讨论审查意见，参阅`查看 PR 审查的 GitHub 文档 <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/viewing-a-pull-request-review>`_。

必要时，可以向分支添加新提交来处理审查意见。也可以直接接受 PR 中的建议修改，GitHub 会自动向分支添加一个新提交，参阅`接受建议修改的说明 <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/incorporating-feedback-in-your-pull-request>`_。

根据反馈讨论并迭代修改，在需要时更新开发分支。建议在一周内回复审查意见，避免自己和审查者丢失上下文。

4. 合并 Pull Request
^^^^^^^^^^^^^^^^^^^^

处理完所有反馈后，PR 必须由目标 ROS 仓库的 :doc:`Committer </The-ROS2-Project/Governance>` 批准，才能合并。

Committer 批准 PR 后，会将其合并到目标分支（通常为 **rolling**），你也会收到 GitHub 通知。

你的变更也可能被回移植到较旧的 ROS 发行版。

相关内容
--------

* :ref:`ROS 开发通用原则 <general-principles>`
* :doc:`Reviewing-a-PR <Reviewing-a-PR>`
