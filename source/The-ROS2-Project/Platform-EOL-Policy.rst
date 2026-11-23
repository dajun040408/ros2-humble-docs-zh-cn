.. _PlatformEOLPolicy:

平台生命周期结束（EOL）政策
===========================

.. contents:: 目录
   :depth: 1
   :local:

即使某个 ROS 发行版仍处于支持期，:doc:`ROS 发行版 <../Releases>` 也不会支持已经结束生命周期（EOL）的平台。本页面说明 EOL 平台的用户应当了解哪些情况，以及 ROS 负责人应当采取哪些措施。

政策
----

每个 ROS 发行版都支持特定的**平台**，例如 Windows 11 或 Ubuntu 24.04。这些平台的**供应商**（例如 Microsoft 或 Canonical）决定其支持期限。

当供应商宣布某个平台结束生命周期时，通常会停止发布重要缺陷修复和安全更新。为了避免受到未修补安全漏洞的影响，我们会主动从 ROS 构建农场中移除所有针对 EOL 平台的构建任务。

如果你使用的平台已不再受到供应商支持，应当预期将无法继续收到更新后的 ROS 软件包。现有 ROS 软件包仍然可以使用，但不会再更新。不过，在特殊情况下，ROS 负责人可以选择更新 EOL 平台上的软件包。

面向 ROS 负责人
----------------

目标平台到达 EOL 之前：

* 确保 ROS 发行版文档包含那些早于 ROS 发行版本身结束生命周期的平台的 EOL 日期。
* 至少提前两次同步周期（约 60–90 天）发布平台即将结束生命周期的公告，以便软件包维护者有时间更新软件包。
* 在 `ros_buildfarm_config <https://github.com/ros2/ros_buildfarm_config>`_ 中提交禁用该平台构建任务的 Pull Request，并邀请 `Infrastructure PMC <https://osralliance.org/wp-content/uploads/2024/03/infrastructure_project_charter.pdf>`_ 审查。
* 对该平台再执行最后一次同步。

目标平台到达 EOL 之后：

* 更新 ROS 发行版文档，明确说明该平台将不再收到 ROS 软件包更新。
* 在 Discourse 上公告 ROS 发行版已停止支持该平台。
* 在以下条件均满足时，可以考虑再向该平台发布最后一个版本：
    * EOL 之前尚未完成最后一次发布；
    * 更新内容看起来不太可能引入回归问题；
    * ROS Buildfarm 仍有该平台的运行节点。
* 合并禁用该平台构建任务的 Pull Request。
