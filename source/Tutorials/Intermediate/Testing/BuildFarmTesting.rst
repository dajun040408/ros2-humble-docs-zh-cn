.. _BuildFarmTesting:

使用 ROS Build Farm 测试代码
============================

`ROS 2 Build Farm <https://build.ros2.org/>`_ 功能非常强大。除了生成二进制软件包外，它还会在 Pull Request 合并之前，编译并运行 ROS 功能包中的所有测试，从而对 Pull Request 进行测试。

使用该功能需要满足四个前置条件：

* GitHub 用户 `@ros-pull-request-builder <https://github.com/ros-pull-request-builder>`_ 必须拥有代码仓库访问权限。
* GitHub 代码仓库必须配置 Webhook。
* 你的功能包必须已在 rosdistro 中建立索引：:doc:`为功能包建立索引 <../../../How-To-Guides/Releasing/Index-Your-Packages>`。
* `test_pull_requests` 标志必须设置为 true。

GitHub 访问权限
---------------

你可以在 GitHub 组织级别授予 PR Builder 访问权限，也可以只对单个 GitHub 代码仓库授权。

GitHub 组织
^^^^^^^^^^^

#. 打开 `https://github.com/orgs/%YOUR_ORG%/people <https://github.com/orgs/%YOUR_ORG%/people>`_，并将 `%YOUR_ORG%` 替换为相应组织名称。
#. 点击 `Invite Member`，输入 `ros-pull-request-builder`。

GitHub 代码仓库
^^^^^^^^^^^^^^

#. 打开 `https://github.com/%YOUR_ORG%/%YOUR_REPO%/settings/access`，并将组织和仓库占位符替换为实际值。
#. 点击 `Add people`，输入 `ros-pull-request-builder`。
#. 为其选择 `Admin` 或 `Write` 角色（参见下一节）。

WebHook
-------

如果授予 `ros-pull-request-builder` 完整管理员权限，它会自动配置 WebHook。

也可以只授予**写入（Write）**权限，从而避免授予完整管理员权限，并手动配置 WebHook：

#. 打开 `https://github.com/%YOUR_ORG%/%YOUR_REPO%/settings/hooks/new`。
#. 将 `https://build.ros2.org/ghprbhook/` 设置为 Payload URL。
#. 勾选以下选项：
    * Let me select individual events.
    * Issue comments
    * Pull requests

test_pull_requests
------------------

对于希望启用 Pull Request 测试的每个 ROS 发行版，都必须在 `rosdistro` 仓库的相应配置部分启用 `test_pull_requests` 标志。

* **方式一**：运行 `bloom` 时，可以选择启用 Pull Request 测试，具体请参阅 :doc:`Bloom 发布功能包 <../../../How-To-Guides/Releasing/Releasing-a-Package>`。
* **方式二**：谨慎地手动编辑 rosdistro 仓库中的相应文件，并创建新的 Pull Request。

  `配置示例 <https://github.com/ros/rosdistro/blob/3c295f76b0755989e9ed526c0b5f28a5f6a94da3/rolling/distribution.yaml#L4708>`_。相关说明见 `REP 143 <http://docs.ros.org/en/independent/api/rep/html/rep-0143.html#distribution-file>`_。

请注意，Pull Request 合并后，通常要等到 Jenkins 夜间重新配置任务时，才会创建相应的测试任务。
