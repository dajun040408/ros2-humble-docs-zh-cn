ROS 软件包索引
==============

你是否准备将一个新的 ROS 软件包发布到 ROS 发行版中？可以先为软件包建立索引，从而加快整个流程。

将 ROS 软件包放入公共代码仓库
-----------------------------

如果尚未完成，请将 ROS 软件包源代码放入公共 Git 仓库。所有发布到 ROS 的软件包都必须是开源的。代码可以托管在任何地方，但推荐使用 GitHub，因为它支持启用 Pull Request 构建任务。可选平台包括：

* `GitHub <https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository>`__（**推荐**）
* `GitLab <https://docs.gitlab.com/ee/user/project/repository/>`__
* `Bitbucket <https://support.atlassian.com/bitbucket-cloud/docs/create-a-git-repository/>`__

为软件包指定 OSI 认可的许可证
-----------------------------

选择一个 `OSI 认可的许可证 <https://opensource.org/licenses>`_，并将其用于 ROS 软件包。如果难以决定，可以考虑使用大多数 ROS 2 核心软件包采用的 `Apache-2.0 许可证 <https://opensource.org/license/apache-2-0>`_。

对于仓库中的每个 `package.xml`，都应在 `<license>` 标签中填写许可证的 SPDX 简短标识符。

如果仓库中所有 ROS 软件包使用相同许可证，或者仓库中只有一个 ROS 软件包，请在仓库根目录创建名为 `LICENSE` 的文件，并写入所选许可证的文本。如果不同 ROS 软件包使用不同许可证，则应在每个 `package.xml` 文件旁边分别创建 `LICENSE` 文件。

确保软件包名称符合 REP 144
---------------------------

发布到 ROS 发行版的软件包名称必须符合 `REP 144 <https://reps.openrobotics.org/rep-0144/>`_。请阅读完整 REP 了解命名规则。如果某个 ROS 软件包名称不符合要求，应先修改名称再继续。

决定要发布到哪个 ROS 发行版
----------------------------

决定要将软件包发布到哪个 ROS 发行版。至少应将软件包发布到 `ROS Rolling <https://docs.ros.org/en/rolling>`_，这样软件包就会自动包含在下一个 ROS 发行版中。

你也可以选择发布到当前仍处于活动支持期的其他 ROS 发行版，具体由你决定。

创建 GitHub 账户
----------------

如果尚未拥有 GitHub 账户，请 `创建 GitHub 账户 <https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github>`_。

你不一定要将 ROS 软件包源代码托管在 GitHub 上，但建立索引和发布软件包时需要 GitHub 账户。

Fork 并克隆 ros/rosdistro
-------------------------

`Fork <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo>`_ `ros/rosdistro <https://github.com/ros/rosdistro/>`_ 仓库。每个 GitHub 账户只需执行一次此步骤。之后每次发布时都会使用这个 fork。

修改你的 fork
-------------

还记得你决定发布到哪些 ROS 发行版了吗？`ros/rosdistro` 仓库中每个 ROS 发行版都有一个对应目录。例如，ROS Rolling 的目录名为 `rolling`。

对于每个希望发布软件包的 ROS 发行版：

1. 填写以下模板。
2. 将填写完成的模板放入对应 ROS 发行版目录中的 `distribution.yaml` 文件。
3. 确保 `MY-REPO-NAME` 在 YAML 文件中的字母顺序位置正确。

.. code-block:: yaml

  YOUR-REPO-NAME:
    source:
      type: git
      url: https://YOUR-GIT-REPO-URL.git
      version: YOUR-BRANCH-NAME
    status: YOUR-STATUS

各字段填写方式如下：

* `YOUR-REPO-NAME`：自定义的、人类可读的仓库名称。对于托管在 GitHub 上的仓库，使用仓库的小写名称，不包含组织名称。例如，`https://github.com/ros2/rosidl` 对应的仓库名称为 `rosidl`。
* `YOUR-GIT-REPO-URL`：可以用于 `git clone` 该仓库的 HTTPS URL。例如，`https://github.com/ros2/rosidl` 对应的 Git 仓库 URL 为 `https://github.com/ros2/rosidl.git`。URL 必须以 `.git` 结尾，否则无法通过 lint 检查。
* `YOUR-BRANCH-NAME`：用于向该 ROS 发行版发布软件包的 Git 分支。通常为 `main`、`master` 或 ROS 发行版名称。例如，`rosidl` 仓库使用 `rolling` 分支保存将发布到 ROS Rolling 的变更。
* `YOUR-STATUS`：从 `REP 141 <https://reps.openrobotics.org/rep-0141/#distribution-file>`_ 的状态列表中选择。通常使用 `maintained` 或 `developed`。

向 ros/rosdistro 提交 Pull Request
----------------------------------

针对你修改的分支，向 `ros/rosdistro <https://github.com/ros/rosdistro/>`_ 提交 `Pull Request <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_。等待几天，直到有人完成审查。

接下来会发生什么
----------------

现在，你已经完成了 ROS 软件包建立索引所需的全部工作。审查人员会检查你的 Pull Request，并判断其是否 `符合审查指南 <https://github.com/ros/rosdistro/blob/master/REVIEW_GUIDELINES.md>`_。

审查人员可能直接批准你的修改，也可能给出可执行的反馈。Pull Request 符合审查指南后就会被合并，你的软件包随后会出现在 `ROS Index <https://index.ros.org/>`_ 中。

你已经完成了软件包发布过程中的一个重要步骤。接下来请继续阅读 :doc:`首次发布指南 <First-Time-Release>`。
