.. redirect-from::

  Contributing

.. _Contributing:

参与贡献
========

.. contents:: 目录
   :depth: 1
   :local:

开始为 ROS 2 项目做贡献之前，请记住以下几点。

基本原则
--------

* **尊重已有成果**

  ROS 已经发展十多年，并被世界各地的开发者和团队广泛使用。参与贡献时，应保持谦逊和开放的心态。

* **尽早与 Open Robotics 沟通**

  * Open Robotics 在 ROS 社区中承担把关和倡导职责。在设计阶段就应充分利用其专业知识和技术判断。
  * 尽早与 Open Robotics 及社区展开讨论。长期参与 ROS 的贡献者可能对整体方向有更清晰的认识。
  * 如果没有事先与社区讨论，就直接实现功能并提交 Pull Request，可能面临被拒绝或被要求大幅重新设计的风险。
  * 通常建议在开始实现之前，先创建 Issue 或通过 Discourse 讨论想法。

* **尽可能采用社区最佳实践，而不是临时自定义流程**

  开发和贡献时，应考虑最终用户的使用体验。避免使用并非所有人都容易获得的非标准工具或库。

* **从整个社区的角度思考**

  需要考虑更大的整体情况。不同开发者正在构建具有不同约束条件的机器人，ROS 必须满足整个社区的需求。

参与 ROS 2 项目有多种方式。

讨论与支持
----------

参与社区讨论和提供支持，是为 ROS 2 做贡献最简单的方式之一。有关如何参与的更多信息，请参阅 :doc:`联系方式 <../../Contact>` 页面。

贡献代码
--------

配置开发环境
^^^^^^^^^^^^

开始贡献代码，首先需要从源码安装 ROS 2。请按照对应平台的 :ref:`源码安装说明 <building-from-source>` 操作。

开发指南
^^^^^^^^

.. toctree::
   :titlesonly:
   :maxdepth: 1

   Contributing/Developer-Guide
   Contributing/Source-Control-Best-Practices
   Contributing/Code-Style-Language-Versions
   Contributing/Quality-Guide
   Contributing/Build-Farms
   Contributing/Windows-Tips-and-Tricks
   Contributing/Contributing-to-code
   Contributing/Contributing-To-ROS-2-Documentation

可以参与哪些工作
^^^^^^^^^^^^^^^^

我们整理了一些适合社区成员参与的任务。你可以`搜索 ROS 2 仓库中标记为 help wanted 的 Issue <https://github.com/search?q=user%3Aament+user%3Aros2+is%3Aopen+label%3A%22help+wanted%22&type=Issues>`_。

如果发现自己感兴趣的任务，请在对应条目下留言，告知其他人你正在关注该任务。

我们还使用 `good first issue` 标签标记适合首次参与贡献者的任务。你可以`搜索这些 Issue <https://github.com/search?q=user%3Aament+user%3Aros2+is%3Aopen+label%3A%22good+first+issue%22&type=Issues>`_。

如果你有兴趣参与 ROS 2 项目，建议先查看这些任务。也欢迎你参与任何开放 Issue，或提出新的任务，特别是已经设置里程碑、计划纳入下一 ROS 2 发行版的任务。

如果你有修复缺陷或改进文档的代码，请向对应仓库提交 Pull Request。

对于较大的变更，建议在开始开发之前，先`在 ROS 2 论坛讨论提案 <https://discourse.openrobotics.org/c/ros/111>`_，以便确认是否已经有人在开展类似工作。如果提案涉及 API 变更，则尤其建议提前讨论实现方案。

成为核心维护者
^^^^^^^^^^^^^^

ROS 2 维护者负责确保项目持续取得进展。维护者的职责包括：

* 审查提交的代码贡献，检查代码风格、质量，以及其是否符合仓库和 ROS 2 的总体目标。
* 确保持续集成（CI）始终保持通过状态。
* 合并符合质量和 CI 标准的 Pull Request。
* 处理用户提交的 Issue。

`ros2` 和 `ament` 两个 GitHub 组织中的每个仓库都有各自的维护者团队。

成为其中一个或多个仓库的维护者需要获得邀请，通常需要满足以下条件：

* 在过去一年中，向目标仓库提交了大量代码贡献。
* 在过去一年中，对目标仓库收到的 Pull Request 进行了大量审查。

ROS 2 团队大约每三个月会检查所有仓库的贡献情况，并向新的维护者发送邀请。接受邀请后，新维护者需要参加一个简短的培训，了解 ROS 2 仓库的工作机制和政策。完成培训后，即可获得相应仓库的写入权限。
