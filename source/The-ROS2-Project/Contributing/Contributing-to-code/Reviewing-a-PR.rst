审查 Pull Request（PR）指南
=============================

所有提交到 ROS 项目的代码和文档都必须通过 Pull Request 进行审查。本文介绍如何准备并审查贡献者提交的 Pull Request。阅读本文后，你将能够确保 PR 变更符合要求的标准。

**领域：** 贡献、社区 | **内容类型：** 操作指南 | **适用经验：** 初级、中级、专家

.. contents:: 目录
   :depth: 2
   :local:

概述
----

审查贡献者提交的 Pull Request（PR），可以检查其变更是否符合相应指南和标准。任何人都可以审查并批准 PR。PR 获得批准后即可准备合并。

只有目标仓库的 :doc:`Committer </The-ROS2-Project/Governance>` 才能将 PR 合并到该仓库，而且在获得批准之前不会合并。

前置条件
--------

代码或文档贡献者已经向某个 `ROS 仓库 <https://github.com/ros2>`__ 提交了 :doc:`Pull Request </The-ROS2-Project/Contributing/Contributing-to-code/Making-a-PR>`。

步骤
----

1. 准备审查
^^^^^^^^^^^

* 欢迎任何人审查 Pull Request。一个 PR 通常需要两次审查才能合并。
* 应将 PR 审查视为提交者与其他开发者之间的协作活动，而不是被动或单向的过程。
* 作为审查者：

  * 可以直接对代码或文档进行小幅改进，例如修复拼写错误或轻微的风格问题。
  * 应尽最大努力在 PR 提交后一周内发表评论。

* 开始审查 PR 时，应先发表评论，让其他人知道你正在进行审查。

2. 审查 Pull Request
^^^^^^^^^^^^^^^^^^^^

#. 按照以下指南检查 PR：

   * 确认代码或文档变更适合目标仓库。
   * 确认代码正确、完整，并且修改范围仅包含一个定义明确的变更。
   * 检查 PR 是否以默认分支（通常为 ``rolling`` ）为目标分支。
   * 如果变更基于设计文档（例如 REP），请确认变更与设计内容一致。
   * 对于代码变更，确保其：

     * 遵循 :doc:`开发者指南 <../Developer-Guide>`。
     * 遵循 :doc:`代码风格指南 <../Code-Style-Language-Versions>`。
     * 为新功能或缺陷修复添加测试。

   * 对于文档变更，确保其遵循 :doc:`文档贡献指南 </The-ROS2-Project/Contributing/Contributing-To-ROS-2-Documentation>`。
   * 确认该 PR 的持续集成（CI）运行成功，没有失败。

#. 提供审查意见。

   可以直接在 PR 中添加审查评论，也可以直接建议修改，参阅`GitHub 评论指南 <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request>`_。

#. 遵循以下建议，确保审查意见有用且可执行：

   * 先提出较高层次的意见（例如重构或设计变更），再讨论具体细节。
   * 可以考虑提供以下类型的评论：

     * **正面反馈**，例如：

       ``很好地处理了边界情况，提前返回让代码更容易理解。``

     * **问题**，例如：

       ``为确保我没有遗漏需求，使用自定义排序函数而不是 localeCompare 的原因是什么？``

     * **建议**，例如：

       ``可以使用 Array.map 简化这个循环，让代码更简洁：``

       .. code-block:: javascript

         const names = users.map(user => user.name)

     * **问题缺陷**，例如：

       ``该函数没有处理 response 为 null 的情况，可能导致运行时错误。建议增加保护条件：``

       .. code-block:: javascript

         if (!response) {
           return [...];
         }

     * **整理建议**，例如与 PR 主要目的无关，但有助于保持仓库健康的修改：

       ``既然已经修改了这个文件，是否也可以删除顶部未使用的 formatDate 导入？``

     * **细节建议**，例如改善代码风格或可读性的细微建议：

       ``命名方面的小建议：user_list 可以改为 users，更准确地表示这是一个集合。``

   * 明确说明希望提交者如何响应每条意见，包括该意见是否阻止 PR 合并，以及你的要求是可选还是必须。
   * 记得提供正面反馈并感谢提交者的工作，始终保持建设性。

3. 批准并合并 Pull Request
^^^^^^^^^^^^^^^^^^^^^^^^^^

完成审查并提供反馈后，提交者可能会继续讨论，或通过向 PR 添加新提交来迭代修改。

当你对变更满意并认为可以合并时，请批准 PR，参阅`GitHub 必需审查批准说明 <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews>`_。

* 欢迎任何人审查 PR，即使该 PR 已经有其他审查意见。
* PR 至少需要一名开发者（作者本人除外）批准；大多数情况下，需要两名开发者批准后才能合并到目标分支。
* 只有目标仓库的 Committer 才能合并已批准的 PR。

  * 请参阅 :doc:`当前 ROS Committer 列表 </The-ROS2-Project/Governance>`，查看拥有目标仓库合并权限的人员。

* 如果 PR 存在依赖关系，请确保按照正确顺序合并依赖 PR。

相关内容
--------

* :ref:`ROS 开发通用原则 <general-principles>`
* :doc:`Making-a-PR <Making-a-PR>`
* `关于 Pull Request 审查 <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews>`_
