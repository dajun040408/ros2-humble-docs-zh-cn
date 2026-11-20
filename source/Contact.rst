.. _Help:

联系社区
========

.. _Using Robotics Stack Exchange:

技术支持
--------

不同类型的问题和讨论应选择不同的沟通渠道。请阅读以下说明，选择合适的方式。

需要排查系统问题？

首先，请在 `Robotics Stack Exchange <https://robotics.stackexchange.com/>`__ 上搜索，看看其他人是否遇到过类似问题，以及他们提供的解决方案是否适用于你的情况。

如果没有找到答案，可以在 `Robotics Stack Exchange <https://robotics.stackexchange.com/>`__ 上提出新问题。请务必添加标签，至少包含 ``ros2`` 标签以及你正在使用的 ROS 发行版版本，例如 ``{DISTRO}``。如果问题与本站文档有关，请添加 ``docs`` 标签，或更具体地添加 ``tutorials`` 标签。

请不要直接联系开发者或维护者。社区无法看到没有公开提出或回答的问题。开源开发依赖整个社区共同参与讨论并帮助解答问题。建议将所有技术问题发布到 `Robotics Stack Exchange <https://robotics.stackexchange.com/>`__，并将缺陷报告提交到相应的问题跟踪系统。

参与技术支持
^^^^^^^^^^^^

ROS 2 用户具有不同的技术背景，使用各种操作系统，也不一定有 ROS（ROS 1 或 ROS 2）使用经验。因此，无论经验多少，用户都可以为社区提供支持。

如果你在 `Robotics Stack Exchange <https://robotics.stackexchange.com/>`__ 上看到与自己曾遇到的问题相似的提问，请考虑分享当时对你有帮助的排查方法。即使不确定回答是否完全正确，也不必担心；只需说明自己的不确定之处，其他社区成员会在必要时补充。

问题报告
--------

如果你发现缺陷、有改进建议，或有针对某个功能包的问题，可以在 GitHub 上提交 Issue。

例如，如果你正在学习 :doc:`本站教程 <Tutorials>`，发现某条操作说明在你的系统上无法正常工作，可以在 `ros2_documentation <https://github.com/ros2/ros2_documentation>`__ 仓库中提交 Issue。

你可以在 `ROS 2 的 GitHub 组织 <https://github.com/ros2>`__ 中搜索各个 ROS 2 代码仓库。

提交 Issue 之前，请先在 ros2 和 ament 两个 GitHub 组织中搜索，确认是否已有用户报告类似问题：`示例搜索 <https://github.com/search?q=user%3Aros2+user%3Aament+turtlesim&type=Issues>`__。

然后，请在 `Robotics Stack Exchange <https://robotics.stackexchange.com/>`__ 上搜索，确认是否有人提出过相同问题或报告过相同故障。

如果问题尚未被报告，可以在相应代码仓库的问题跟踪系统中提交 Issue。如果不确定应该向哪个仓库提交，请将问题提交到 `ros2/ros2 仓库 <https://github.com/ros2/ros2/issues>`__，社区会协助查看。

提交 Issue 时，请注意以下事项：

* 提供足够的信息，使其他人能够理解问题。

  准确描述你当时正在执行或希望执行的操作，以及具体发生了什么错误。如果问题发生在跟随教程或在线说明操作时，请提供对应说明页面的链接。

* 使用能够准确描述问题的标题。

  不好的示例：“rviz 无法运行”。

  好的示例：“最近一次 apt 更新后，Rviz 因缺少 ``.so`` 文件而崩溃”。

* 提供与问题相关的平台、软件、版本和环境信息。

  包括软件的安装方式（使用二进制包还是从源码构建），以及你使用的 ROS 中间件/DDS 实现（如果知道）。

* 提供所有警告和错误信息。

  请直接从输出这些信息的终端复制粘贴，不要手动重新输入，也不要只提供截图。

* 如果是软件缺陷，建议提供一个简短、自包含、正确且可编译的示例（`SSCCE <https://sscce.org/>`__）。

* 如果讨论编译、链接或安装问题，请同时提供编译器版本。

根据问题情况，还可以提供：

* ROS 环境变量（``env | grep ROS``）
* 回溯信息（Backtrace）
* 相关配置文件
* 显卡型号和驱动版本
* 如果可能，提供 rviz 的 Ogre.log（使用 ``rviz -l`` 运行）
* 能够复现问题的 Bag 文件和代码示例
* 用于演示问题的 GIF 或视频

.. _Using ROS Discourse:

社区讨论
--------

如果你希望与其他 ROS 2 社区成员展开讨论，请访问官方 `Open Robotics Discourse <https://discourse.openrobotics.org/>`__。

Discourse 适合开展较高层次的讨论，不适合用于解决具体代码问题；但你可以在这里讨论最佳实践或标准改进建议。

有关 ROS 2 开发和未来计划的讨论正在 `Open Robotics Discourse 的 ROS 分类 <https://discourse.openrobotics.org/c/ros/111>`__ 中进行。参与这些讨论，是影响 ROS 2 不同功能设计和实现方式的重要途径。

ROS 生态系统背后的多元化社区是其最重要的优势之一。我们鼓励所有 ROS 社区成员参与这些设计讨论，以充分利用社区成员的经验，并在设计时考虑不同的使用场景。

社区交流礼仪
------------

秉持“善意推定（assume good faith）”原则。互联网上的评论很容易被误解其含义或语气。善意推定意味着在存在疑问时，优先相信对方是出于善意，避免误伤善意的社区成员或破坏讨论氛围。即使对方最初并非出于善意，以善意方式回应通常也更有效。

请不要重复发布同一个问题：这通常意味着问题已经被看到。如果没有收到回复，很可能是因为暂时没有人有时间回答，也可能是社区成员暂时不知道答案。无论哪种情况，重复发送都不合适，也容易引起其他成员反感。这同样适用于跨论坛重复发帖。请尽量选择最合适的论坛提问；如果有人建议你转到另一个论坛，请提供原讨论的链接。

在 `Robotics Stack Exchange <https://robotics.stackexchange.com/>`__ 上，你可以编辑自己的问题并补充更多细节。问题描述越详细，其他人就越容易帮助你找到解决方案，你获得回复的可能性也越高。

列出个人截止日期通常被认为是不恰当的。回答问题的社区成员也有自己的工作安排。

不要乞求他人帮助。如果有人愿意且能够解决你的问题，通常会主动回复。催促他人尽快回答，大多只会产生负面效果。

不要在帖子中添加无关内容。帖子应围绕主题展开，不要加入无关信息。与主题无关的内容、链接和图片都可能被视为垃圾信息。

对于商业相关帖子，也请参阅 `相关讨论 <https://discourse.openrobotics.org/t/sponsorship-notation-in-posts-on-ros-org/2078>`_。

尽量减少对付费墙后内容的引用。`Open Robotics Discourse <https://discourse.openrobotics.org/>`__ 和 `Robotics Stack Exchange <https://robotics.stackexchange.com/>`__ 上发布的内容原则上应当免费并向所有人开放。私人期刊论文、教科书和付费新闻网站等付费内容的链接，虽然可能有帮助且与主题相关，但并非所有用户都能访问。尽可能优先引用免费、开放的第一手资料，让付费内容仅起辅助作用。

应避免只包含单个链接的帖子。通常来说，只提供一个链接的回答帮助有限，也容易被误认为垃圾信息。此外，链接可能随时间失效或被替换。相比只贴链接，结合上下文和来源说明，对链接内容进行概述通常更有帮助。

私人联系
--------

如果你希望私下联系我们（例如，你的问题包含组织或项目的敏感信息，或者涉及安全问题），可以直接发送电子邮件至 ``ros@osrfoundation.org``。
