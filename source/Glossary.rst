术语表
======

.. include:: ../global_substitutions.txt

本文档中使用的术语：

.. glossary::

   API
       API（Application Programming Interface，应用程序编程接口）是应用程序对外提供的接口。在本文档语境中，应用程序通常是共享库或其他适合特定编程语言的共享资源。API 由一组文件组成，这些文件定义了使用接口的软件与提供接口的软件之间的契约。在 C 和 C++ 中，这些文件通常表现为头文件；在 Python 中则通常表现为 Python 文件。API 应当在文档中进行分组和说明，并明确标记为公共接口或私有接口。公共接口受到变更规则约束，对公共接口的修改通常需要提升所提供软件的版本号。

   client_library
       客户端库（Client Library）是一种 :term:`API`，通过话题（Topic）、服务（Service）和动作（Action）等基础中间件概念访问 ROS 计算图。

   package
       功能包（Package）是一个独立的软件单元，包含源代码、构建系统文件、文档、测试及其他相关资源。

   REP
       机器人技术增强提案（Robotics Enhancement Proposal）。该文档用于描述 ROS 社区的功能增强、标准化方案或约定。相关 REP 审批流程允许社区持续讨论提案，直至形成一定共识；提案获批并实施后，相关内容会成为正式文档。所有 REP 均可在 `REP 索引 <https://reps.openrobotics.org/>`_ 中查看。

   VCS
       版本控制系统（Version Control System），例如 CVS、SVN、git、Mercurial 等。

   rclcpp
       ROS 的 C++ 客户端库（:term:`Client Library <client_library>`）。它包含中间件相关 API，以及根据消息、服务和动作等接口定义生成 C++ 数据结构的相关功能。

   repository
       通常使用 :term:`VCS`（如 git 或 Mercurial）管理，并托管在 GitHub 或 BitBucket 等网站上的功能包集合。在本文档语境中，代码仓库通常包含一个或多个某种类型的 |packages|。
