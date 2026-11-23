# ROS 2 Humble 中文化进度

最后更新：2026-11-23

## 上游统计基线

- 上游仓库：ros2/ros2_documentation
- 上游分支：humble
- 官方 reStructuredText 文件：311 个
- 按当前排除规则剔除辅助/内部文件后，候选文档：297 个
- 统计口径：按候选文档源文件路径与当前仓库中的对应中文页面逐一比对。

## 当前进度

| 指标 | 数量 |
|---|---:|
| 候选文档总数 | 297 |
| 已有中文页面 | 165 |
| 待中文化 | 132 |
| 覆盖率 | 55.6% |

本轮新增 3 个此前缺失的候选页面：ROS 1 到 ROS 2 C++ 功能包迁移参考、C++ 功能包迁移示例、Ubuntu 源码安装指南。另更新/完善了构建农场、PR 提交和 Windows 开发技巧等贡献指南页面。

## 已完成的重点领域

- ROS 1 迁移：参数、接口、功能包、启动文件、package.xml，以及 C++ 功能包迁移参考和完整示例。
- 构建与开发：ament_cmake_python、功能包文档、回调组、同步/异步服务、GDB 调试、ROS 2 IDE、Windows 开发技巧。
- 中间件与通信：DDS 调优、Cyclone DDS、GurumDDS、RTI Connext DDS、Zenoh、多 RMW、rosbag2 QoS、零拷贝借用消息。
- 安装与部署：Ubuntu、RHEL、Windows、macOS、Raspberry Pi、Docker、软件源镜像、预发布软件包测试、apt 快照软件源；已补充 Ubuntu 源码安装指南。
- 发布与维护：软件包索引、Bloom 发布轨道、发布团队、首次发布、自定义 rosdistro、源码检出维护、发行版开发流程。
- 仿真、可视化与生态：MVSim、虚拟机器人、Foxglove Studio、Intel ROS、NVIDIA ROS 2 项目、URDF、TF2。
- ROS 项目与治理：发行计划、平台支持、社区指标、功能状态、功能构想、贡献指南、构建农场和 PR 流程。
- 历史发行说明：Alpha、Beta 及部分正式发行版页面。

## 构建与部署

- 已加入上游源码 overlay 构建脚本：`scripts/prepare_build.py`。
- 已加入 GitHub Actions 工作流：`.github/workflows/deploy-docs.yml`，用于构建 HTML、生成中文搜索索引并部署 GitHub Pages。
- 工作流会检出上游 Humble 源码，将本仓库中文页面覆盖到对应路径，再构建和部署。
- 之前的构建曾遇到 Python/Sphinx 版本兼容、Graphviz 缺失及 reStructuredText 标记等问题，相关工作流配置和部分页面已调整。
- 本轮提交触发的 GitHub Actions 仍在排队/运行；尚未得到成功的完整 Sphinx 构建和 GitHub Pages 部署结果。不能据此宣称网站构建已通过。

## 待完成工作

- [ ] 完成剩余 132 个候选文档中文化。
- [ ] 补齐所有导航目录、页面标题和层级。
- [ ] 检查页面内锚点、跨页引用、上一页/下一页和外部链接。
- [ ] 完成完整 Sphinx 构建并处理错误和警告。
- [ ] 验证 GitHub Pages 实际访问效果。
- [ ] 发布最终页面覆盖率和质量检查报告。

## 统计规则

- “已有中文页面”仅按对应候选源文件路径存在进行初步计数，不代表已经审核或通过构建。
- 代码、命令、API、类型名、参数名、话题名、路径及配置键应保持原样。
- 不把英文原文、空白页或占位页计为中文化完成。
- 最终覆盖率仍需结合逐页内容审查和 Sphinx 实际构建清单确认。
