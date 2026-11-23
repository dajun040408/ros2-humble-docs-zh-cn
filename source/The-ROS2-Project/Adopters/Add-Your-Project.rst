将你的项目添加到 ROS 2 使用者列表
====================================

使用本页面中的表单，可以为你的组织或项目生成 YAML 条目。生成后，将 YAML 片段复制到 ROS 2 文档仓库 rolling 分支中的 adopters.yaml 文件，并提交 Pull Request：

§https://github.com/ros2/ros2_documentation/blob/rolling/source/The-ROS2-Project/Adopters/adopters.yaml§

政策
----

该列表由项目或组织自行报告并自行确认。除非收到投诉，否则通常只进行最低限度的审查。

由于贡献通过 Pull Request 提交，因此后续可以方便地审计和清理条目。

贡献步骤
--------

1. 填写页面中的表单。
2. 点击 Generate YAML，生成 YAML 片段。
3. 点击 Open PR on GitHub，在 GitHub 网页编辑器中打开目标文件（YAML 会自动复制到剪贴板）。
4. 将生成的 YAML 粘贴到文件 adopters: 列表的末尾。
5. 提交变更并创建 Pull Request。

.. note::

   所有提交到 ROS 2 文档仓库的 Pull Request 都必须包含 Developer Certificate of Origin（DCO）签署。

   如果使用 GitHub 网页编辑器，DCO bot 会在缺少签署时向 PR 添加评论，并说明如何补充。

   如果通过命令行签署，请使用：

   .. code-block:: console

      $ git commit --signoff

表单字段说明
------------

* Organization：组织或机构名称，必填。
* Organization URL：组织网站地址，可选。
* Project：使用 ROS 的具体项目名称，必填。
* Project URL：项目网址，可选。
* Domain：项目所属领域，可多选，例如农业、航空/无人机、汽车、机器人组件等。
* Description：项目说明。
* ROS 2 Distributions：项目使用的 ROS 2 发行版。
* Country/Region：组织或项目所在地区。

生成 YAML 后，请检查组织名称、项目名称、链接和分类是否正确，再提交 Pull Request。
