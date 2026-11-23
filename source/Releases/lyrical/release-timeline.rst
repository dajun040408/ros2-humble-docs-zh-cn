Lyrical Luth 发行时间表
=======================

有关 Lyrical Luth 的开发进度，请查看 `项目看板 <https://github.com/orgs/ros2/projects/70>`_。有关 Lyrical Luth 整体发布流程，请参阅 :doc:`流程说明页面 <../Release-Process>`。

**尽快** - 将 ROS Rolling 迁移到 ROS Lyrical 的目标平台
    * RHEL 10 和 Ubuntu 26.04：核心软件包在两个平台上均成功构建后立即迁移。
    * Windows 11：构建通过后立即迁移。

**2026 年 4 月 13 日，星期一** - Alpha 阶段及 RMW 冻结（延期；原计划为 4 月 6 日）
    * 对 ROS Base 软件包进行初步测试。
    * 冻结 RMW 供应商软件包的 API 和功能。

**2026 年 4 月 20 日，星期一** - 冻结阶段（延期；原计划为 4 月 13 日）
    * 冻结 Rolling Ridley 中 ROS Base 软件包的 API 和功能。
    * 此后只应发布缺陷修复版本。
    * 允许发布新软件包。

**2026 年 4 月 21 日，星期二** - 分支阶段（延期；原计划为 4 月 20 日）
    * 从 Rolling Ridley 创建分支。
    * 重新开放 `rosdistro`，接受针对 ROS Base 软件包的 Rolling Pull Request。
    * Lyrical 开发从 `ros-rolling-*` 软件包转向 `ros-lyrical-*` 软件包。

**2026 年 4 月 27 日，星期一** - Beta 阶段
    * 提供更新后的 ROS Desktop 软件包。
    * 启动公开测试征集。

**2026 年 4 月 30 日，星期四** - 启动教程测试活动
    * 开放教程，供社区测试。

**2026 年 5 月 11 日，星期一** - Release Candidate 阶段
    * 构建直至 ROS Desktop 级别的候选发行版软件包。

**2026 年 5 月 18 日，星期一** - 发行版冻结
    * 冻结所有 ROS Desktop 软件包中的 Lyrical 分支。
    * 不再合并任何针对 Lyrical 分支，或针对 `rosdistro` 仓库中 `lyrical/distribution.yaml` 的 Pull Request。

**2026 年 5 月 22 日，星期五** - 正式发布
    * 发布公告。
    * 解除 ROS Desktop 软件包源码冻结，并重新开放 `rosdistro`，接受 Lyrical Pull Request。

**2031 年 5 月** - 生命周期结束
    * ROS Lyrical 将停止接收更新，包括安全更新。
