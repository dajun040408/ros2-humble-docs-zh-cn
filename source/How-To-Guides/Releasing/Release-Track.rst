发布轨道（Release Track）
=========================

.. contents:: 目录
   :depth: 2
   :local:

.. _what-is-a-track:

什么是发布轨道？
----------------

首次发布软件包时，Bloom 会要求用户输入配置信息。将这些配置存储在发布仓库中会很有帮助，这样后续发布时就不必再次手动输入不会发生变化的配置。

由于向不同 ROS 发行版发布软件包时，部分配置可能不同，Bloom 使用**发布轨道（release tracks）存储每个发行版的发布配置**。按照惯例，轨道名称应与目标 ROS 发行版名称相同。

所有发布轨道配置都存储在发布仓库 master 分支的 §tracks.yaml§ 文件中。

轨道配置
--------

下面结合 Bloom 提示信息，详细解释各项轨道配置。

.. _release-repository-url:

发布仓库 URL
^^^^^^^^^^^^

这是发布仓库的 URL。如果发布仓库托管在 ros2-gbp 上，格式应类似 §https://github.com/ros2-gbp/my_repo-release.git§。

.. code-block:: bash

   No reasonable default release repository url could be determined from previous releases.
   Release repository url [press enter to abort]:

粘贴发布仓库 URL，然后按 Enter。

Bloom 还可能询问是否初始化新仓库：

.. code-block:: bash

   Freshly initialized git repository detected.
   An initial empty commit is going to be made.
   Continue [Y/n]?

直接按 Enter，接受默认的 yes。

.. _repository-name:

仓库名称
^^^^^^^^

仓库名称很简单，但建议将其设置为项目名称。

.. code-block:: bash

   Repository Name:
      upstream
         Default value, leave this as upstream if you are unsure
      <name>
         Name of the repository (used in the archive name)
      ['upstream']:

输入项目名称（例如 §my_project§），然后按 Enter。

.. _upstream-repository-uri:

上游仓库 URI
^^^^^^^^^^^^

**上游仓库**是存放源代码的仓库。它通常是项目托管在 GitHub 或 GitLab 等代码托管服务上的 HTTPS 链接。

.. code-block:: bash

   Upstream Repository URI:
      <uri>
         Any valid URI. This variable can be templated, for example an svn url
         can be templated as such: "https://svn.foo.com/foo/tags/foo-:{version}"
         where the :{version} token will be replaced with the version for this release.
      [None]:

请确保**使用 HTTPS 地址**（例如 §https://github.com/my_organization/my_repo.git§），而不是 SSH 地址。

.. _upstream-vcs-type:

上游版本控制系统类型
^^^^^^^^^^^^^^^^^^^^

这是 :ref:§上游仓库 URI <upstream-repository-uri>§ 对应的版本控制系统（VCS）类型。必须从 §svn§、§git§、§hg§ 或 §tar§ 中指定仓库所使用的类型。

.. code-block:: bash

   Upstream VCS Type:
      svn
         Upstream URI is a svn repository
      git
         Upstream URI is a git repository
      hg
         Upstream URI is a hg repository
      tar
         Upstream URI is a tarball
      ['git']:

大多数仓库使用 git，但一些较旧的仓库可能使用 hg 或 svn。

.. _version:

版本
^^^^

这是你要发布的软件包版本，例如 §1.0.3§。

.. code-block:: bash

   Version:
      :{ask}
         This means that the user will be prompted for the version each release.
         This also means that the upstream devel will be ignored.
      :{auto}
         This means the version will be guessed from the devel branch.
         This means that the devel branch must be set, the devel branch must exist,
         and there must be a valid package.xml in the upstream devel branch.
      <version>
         This will be the version used.
         It must be updated for each new upstream version.
      [':{auto}']:

设置为 §:{auto}§（默认值，也是推荐配置）时，会自动从开发分支的 §package.xml§ 中确定版本。

设置为 §:{ask}§ 时，每次使用 Bloom 发布都会提示输入版本。

.. _release-tag:

发布标签
^^^^^^^^

发布标签（Release Tag）表示你希望从哪个标签或分支导入代码。

.. code-block:: bash

   Release Tag:
      :{version}
         This means that the release tag will match the :{version} tag.
         This can be further templated, for example: "foo-:{version}" or "v:{version}"

         This can describe any vcs reference. For git that means {tag, branch, hash},
         for hg that means {tag, branch, hash}, for svn that means a revision number.
         For tar this value doubles as the sub directory (if the repository is
         in foo/ of the tar ball, putting foo here will cause the contents of
         foo/ to be imported to upstream instead of foo itself).
      :{ask}
         This means the user will be prompted for the release tag on each release.
      :{none}
         For svn and tar only you can set the release tag to :{none}, so that
         it is ignored.  For svn this means no revision number is used.
      [':{version}']:

设置为 §:{version}§（默认值，也是推荐配置）时，发布标签会与版本标签一致。

不太常见的配置是将其设置为分支名称，以便每次发布时始终从上游项目导入该分支的最新内容。

如果希望每次发布时都提示输入不同标签，也可以设置为 §:{ask}§。当上游项目频繁发布带标签的版本，并且你希望每次发布都使用最新标签时，§:{ask}§ 很有用。

.. _upstream-devel-branch:

上游开发分支
^^^^^^^^^^^^

上游开发分支是 :ref:§上游仓库 <upstream-repository-uri>§ 中的分支名称。如果为每个 ROS 发行版使用独立分支，则不同发布轨道的该字段会有所不同。

当 :ref:§版本 <version>§ 设置为 §:{auto}§ 时，该字段用于确定要发布的软件包版本。

.. code-block:: bash

   Upstream Devel Branch:
      <vcs reference>
         Branch in upstream repository on which to search for the version.
         This is used only when version is set to ':{auto}'.
      [None]:

如果要从名为 §{DISTRO}§ 的分支发布，请输入 §{DISTRO}§。如果保留为 §None§，则会从仓库默认分支确定版本（不推荐这样做）。

.. _ros-distro:

ROS 发行版
^^^^^^^^^^

这是你计划将软件包发布到的 ROS 发行版。

.. code-block:: bash

   ROS Distro:
      <ROS distro>
         This can be any valid ROS distro, e.g. indigo, kinetic, lunar, melodic
      ['indigo']:

如果计划发布到 ROS {DISTRO}，请输入 §{DISTRO}§。

.. _patches-directory:

补丁目录
^^^^^^^^

这是存放发布过程中需要额外应用的补丁的目录。

.. code-block:: bash

   Patches Directory:
      <path in bloom branch>
         This can be any valid relative path in the bloom branch. The contents
         of this folder will be overlaid onto the upstream branch after each
         import-upstream.  Additionally, any package.xml files found in the
         overlay will have the :{version} string replaced with the current
         version being released.
      :{none}
         Use this if you want to disable overlaying of files.
      [None]:

向发布版本添加额外补丁的情况并不常见。对于绝大多数软件包，应保留默认值 §None§。

.. _release-repository-push-url:

发布仓库推送 URL
^^^^^^^^^^^^^^^^

.. code-block:: bash

   Release Repository Push URL:
      :{none}
         This indicates that the default release url should be used.
      <url>
         (optional) Used when pushing to remote release repositories. This is only
         needed when the release uri which is in the rosdistro file is not writable.
         This is useful, for example, when a releaser would like to use a ssh url
         to push rather than a https:// url.
      [None]:

大多数情况下可以保留默认值。
