使用自定义 rosdistro 版本
==========================

.. contents:: 目录
    :depth: 2
    :local:

概述
----

§rosdistro <https://github.com/ros/rosdistro>§_ 包含所有 ROS 发行版的软件包中央索引，以及用于安装二进制依赖项的 §rosdep§ key。

执行 §rosdep install ...§ 时，rosdep 会检查本地缓存的 rosdistro 索引（该缓存由 §rosdep update§ 填充），并根据 §package.xml§ 中的 key 确定要安装的 ROS 软件包、Python 模块或二进制软件包。因此，该索引是 ROS 生态系统中的重要组成部分。

不过，有时用户希望进一步控制该索引，例如添加自己的专有 key，或使用 rosdistro 之前某个时间点的状态。本指南介绍如何在系统中指定要使用的 rosdistro 版本。

本指南使用的示例场景是：由于开发计算机或持续集成环境出现问题，希望使用 Rolling 的某个历史版本。在操作系统迁移期间，旧操作系统上的 Rolling 可能因支持转向新操作系统而无法使用（例如从 Ubuntu 22.04 迁移到 24.04）。因此，我们希望指定一个与当前操作系统上可正常工作的 Rolling 发行版相匹配的历史 rosdistro 版本，在升级操作系统之前保持系统正常运行。

如果要通过二进制软件包实现这一点，请参阅 :doc:§快照软件源 < /Installation/Snapshot-Repository>§。

重要准备事项
------------

默认情况下，rosdep 从 §/etc/ros/rosdep/sources.list.d/20-default.list§ 中设置的位置填充缓存。

使用 §rosdep init§ 初始化 rosdep 时，会在 §20-default.list§ 中写入主要 rosdistro URL（来自 §此文件 <https://github.com/ros/rosdistro/blob/master/rosdep/sources.list.d/20-default.list>§_）。

§rosdep update§ 生成的缓存位于 §~/.ros/rosdep/sources.cache§，不应手动修改。

如果运行 §rosdep update§ 时没有设置 §ROSDISTRO_INDEX_URL§ 环境变量，则会使用主公共 rosdistro 索引。如果设置了该变量，则可以使用自定义 rosdistro 索引。该索引既可以是公共索引的快照，也可以是包含专有软件包的完全独立索引。

如果希望了解更多信息，请查看 §ros_buildfarm 软件包中的文档 <https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/custom_rosdistro.rst>§_。

如何使用自定义 rosdistro 版本
-----------------------------

要在 CI、Docker 构建、本地环境、机器人或其他应用中使用自定义版本，首先需要确定要使用的 rosdistro 版本。

在本指南的示例中，我们希望使用新操作系统上 Rolling 首次同步之前的最后一个索引状态。本例中，该操作系统上的最后一次同步发生在 2024 年 2 月 28 日。

方便的是，同步版本带有标签，因此可以通过 §rolling/2024-02-28§ 标签分支获取该信息。

因此，我们需要将 §20-default.list§ 更新为使用该标签分支，而不是主仓库当前状态。可以使用以下脚本完成。如果在本地主机上运行，可能需要添加 §sudo§。该命令会将列表配置从 master 分支切换为指定标签分支。

.. code-block:: console

    $ sed -i "s|ros\/rosdistro\/master|ros\/rosdistro\/rolling\/2024-02-28|" /etc/ros/rosdep/sources.list.d/20-default.list

然后，需要更新环境变量 §ROSDISTRO_INDEX_URL§，使其指向新的 rosdistro 索引：

.. code-block:: console

    $ export ROSDISTRO_INDEX_URL=https://raw.githubusercontent.com/ros/rosdistro/rolling/2024-02-28/index-v4.yaml

如果计划在本地主机上长期使用该配置，建议将其添加到 §~/.bashrc§，这样所有新终端都会自动使用该配置。

索引 URL 中的 §v4§ 表示使用新版索引格式。出于历史兼容和旧系统需要，仍然存在不带 §v4§ 的旧索引，但不应再使用它。

完成后，运行 §rosdep update§，即可根据 2024 年 2 月 28 日 Rolling 发行版的状态更新索引，也就是相关问题开始出现之前的状态。

可以参考 §Nav2 的 CircleCI <https://github.com/ros-planning/navigation2/commit/80bb5bff1488c0677efcc4254b7a89908c853ba0>§_ 和 §ros_gz 的 GitHub Actions <https://github.com/gazebosim/ros_gz/pull/522/files>§_，了解如何在 CI 系统中绕过临时 Rolling 服务中断。

.. note:: 如果使用自定义 rosdistro 版本，可以将默认列表和索引 URL 中的最终地址替换为自己的 fork 或索引地址。
