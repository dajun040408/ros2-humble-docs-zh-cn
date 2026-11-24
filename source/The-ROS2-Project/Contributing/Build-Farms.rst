.. redirect-from::

  Contributing/Build-Farms

.. _BuildFarms:

ROS 构建农场
============

.. contents:: 目录
   :depth: 1
   :local:

ROS 构建农场是支持 ROS 生态系统的重要基础设施，由 `Open Robotics`_ 提供并维护。它为 ROS 1 和 ROS 2 软件包提供源码和二进制软件包构建、持续集成、测试及分析服务。

目前有两个面向开源软件包的托管实例：

#. ``https://build.ros.org/``：用于 ROS 1 软件包。
#. ``https://build.ros2.org/``：用于 ROS 2 软件包。

如果你计划使用这些基础设施，建议注册 `构建农场讨论论坛 <https://discourse.openrobotics.org/c/infrastructure-project/infra-buildfarm/20>`_，以便接收通知，例如即将发生的变更。

任务与部署
----------

ROS 构建农场执行多种不同类型的任务：

* `release jobs`_：生成二进制软件包，例如 deb 软件包。
* `devel jobs`_：按轮询机制，在单个仓库中构建和测试 ROS 软件包。
* `pull_request jobs`_：由 Webhook 触发，在单个仓库中构建和测试 ROS 软件包。
* `CI jobs`_：跨多个仓库构建和测试 ROS 软件包，并可使用其他 CI 任务的构建产物加快构建速度。
* `doc jobs`_：生成软件包 API 文档，并从清单文件中提取信息。
* `miscellaneous jobs`_：执行维护任务，并生成信息数据，以可视化构建农场及其生成产物的状态。

创建与部署
^^^^^^^^^^

当软件包通过 Bloom 发布（即发布到 ROS 1 或 ROS 2）时，会创建并部署上述任务。

Bloom 成功完成，并且软件包通过向 `rosdistro`_ 提交 Pull Request 被纳入某个 ROS 发行版后，相应任务就会自动生成。

任务名称编码了任务类型和用途：[1]_

* 发布任务：

  * ``{distro}src_{platf}__{package}__{platform}__source``：构建发行版的源码软件包。
  * ``{distro}bin_{platf}__{package}__{platform}__binary``：构建发行版的二进制软件包。

  例如，ROS 2 Iron 中 ``rclcpp`` 在 Ubuntu Jammy amd64 上的二进制打包任务名为 ``Ibin_uJ64__rclcpp__ubuntu_jammy_amd64__binary``。

* 开发任务：

  * ``{distro}dev__{package}__{platform}``：针对发布分支执行 CI 构建。

* Pull Request 任务：

  * ``{distro}pr__{package}__{platform}``：针对 Pull Request 执行 CI 构建。

  例如，ROS 2 Iron 中 ``rclcpp`` 在 Ubuntu Jammy amd64 上的 PR 任务名为 ``Ipr__rclcpp__ubuntu_jammy_amd64``。

执行方式
^^^^^^^^

任务的执行方式取决于任务类型：

* ``devel jobs``：根据配置的轮询频率，每当相应分支出现新提交时触发。
* ``pull_request jobs``：由上游仓库 [2]_ 对应 Pull Request 的 Webhook 触发。
* ``release jobs``：每当软件包发布新版本时触发，也就是该软件包对应的 rosdistro Pull Request 被接受时触发。源码任务由 rosdistro distribution 文件中的版本变化触发，二进制任务则由对应源码任务触发。

常见问题与故障排查
------------------

#. **收到构建农场任务失败的 Jenkins 邮件，应该怎么办？**

   打开触发问题的任务。Jenkins 邮件顶部会提供任务链接。进入构建任务页面后，点击左侧的 *Console Output*，再点击 *Full Log*，即可查看完整控制台输出。

   尝试查找最靠前的错误，因为它通常最重要，后续错误可能只是由它引起的连锁问题。

   邮件底部可能包含类似以下内容：

   ``'apt-src build [...]' failed. This is usually because of an error building the package.``

   这通常意味着构建软件包时发生错误，可能缺少依赖项，参见问题 2。

#. **似乎缺少依赖项，如何找出缺少哪个依赖？**

   基本有两种方法。方法 A 更简单，但可能需要多次尝试；方法 B 更全面，也支持本地调试。

   A）检查触发问题的发布任务，定位 CMake 依赖问题。对于 Ubuntu/Debian 构建任务，可以通过左侧菜单进入 *build binarydeb* 部分，再查看 CMake 部分。``CMake Error`` 通常会提示 CMake 配置需要某个依赖，而该依赖未在`软件包清单`_中声明。

   在清单中修复依赖后，重新发布软件包，并等待构建农场反馈。

   B）为了获得更完整的信息并加快本地调试，可以`在本地运行发布任务`_。这样可以在本地反复调整软件包清单，直到所有依赖问题都解决。

#. **为什么发布任务失败，但开发任务、GitHub Actions 或本地构建成功？**

   可能有多种原因。

   首先，发布任务使用最小化 ROS 安装环境进行构建，以检查所有依赖项是否正确声明在`软件包清单`_中。而开发任务、GitHub Actions 或本地构建环境中可能已经安装了这些依赖项，因此无法发现依赖声明问题。

   其次，它们构建的源码版本可能不同。开发任务、GitHub Actions 和本地构建通常构建`上游``_[2]_ 仓库中的最新代码，而``发布任务`_构建的是最新发布版本的源码，也就是``发布`` 仓库 [3]_ 中对应的上游分支代码。

延伸阅读
--------

* `ros_buildfarm 通用文档 <https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/index.rst>`_
* `回归测试 <http://wiki.ros.org/regression_tests#Setting_up_Your_Computer_for_Prerelease>`__
* `ROS 1 构建农场 Wiki <http://wiki.ros.org/buildfarm>`_ （部分内容已过时）
* `cookbook-ros-buildfarm <https://github.com/ros-infrastructure/cookbook-ros-buildfarm>`_

.. [1] ``{distro}`` 是 ROS 发行版名称的首字母；``{platform}``（``{platf}``）表示软件包构建目标平台及其缩写；``{package}`` 表示正在构建的 ROS 软件包名称。
.. [2] ``上游`` 仓库是存放对应 ROS 1/ROS 2 软件包原始源码的仓库。
.. [3] ``发布`` 仓库是 ROS 2 基础设施用于发布软件包的仓库，参见 ``https://github.com/ros2-gbp/``。

.. _release jobs:
   https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/release_jobs.rst
.. _devel jobs:
   https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/devel_jobs.rst
.. _pull_request jobs:
   https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/devel_jobs.rst
.. _CI jobs:
   https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/ci_jobs.rst
.. _doc jobs:
   https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/doc_jobs.rst
.. _miscellaneous jobs:
   https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/miscellaneous_jobs.rst
.. _bloomed:
   http://wiki.ros.org/bloom
.. _rosdistro:
   https://github.com/ros/rosdistro
.. _run the release jobs locally:
   https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/release_jobs.rst#run-the-release-job-locally
.. _Open Robotics:
   https://www.openrobotics.org/
.. _job descriptions above:
   #jobs-and-deployment
.. _package manifest:
   http://wiki.ros.org/Manifest
