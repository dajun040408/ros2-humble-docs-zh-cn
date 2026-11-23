# ROS 2 Humble 中文化进度

最后更新：2026-11-23

## 上游基线

- 上游仓库：ros2/ros2_documentation
- 上游分支：humble
- 已上传并核对源码归档：ros2_documentation_humble.tar.gz
- 上游 Git tree：790 个条目，其中 684 个文件。
- .rst 文件总数：311。
- 根据上游 Sphinx exclude_patterns 初步排除 14 个辅助/内部文件，得到 297 个构建候选文档源文件。最终 HTML 页面数以 Sphinx 构建输出为准。

## 当前已提交翻译页面

| 模块 | 已翻译初稿 |
|---|---|
| 首页与项目入口 | index、About ROS、Installation、Ubuntu deb 安装、Releases、Contact、The ROS 2 Project、Package Docs、Related Projects、Citations |
| 后续批次新增（15 个候选文档） | rosbag2 QoS 覆盖、ROS 软件包索引、发布团队与发布仓库、Bloom 发布轨道、自定义 rosdistro、Ubuntu Jammy ros1_bridge、Foxglove Studio、NVIDIA ROS 2 项目、ROS 2 软件源镜像、预发布软件包测试、源码检出维护、RHEL RPM 安装、Windows 二进制安装、RHEL 二进制安装、Ubuntu 二进制安装 | ament_cmake_python、核心维护者指南、DDS 调优、功能包文档、同步/异步服务客户端、Python 软件包使用、ROS 2 IDE、零拷贝借用消息、多个 RMW 实现、回调组、ROS 1 启动文件迁移、package.xml 格式迁移 |
| 本轮新增（60 个候选文档） | 代码贡献导航、开发中发行版、Gazebo/Webots/MVSim 仿真导航、Phantom Bridge、交叉编译、RViz、EOL 发行版、Makoa 发行信息、RMW/DDS/Zenoh、Fedora 源码环境、软件包发布、Rolling、Launch、测试、Docker、自定义 deb、ROS 市场、平台支持等级、Lyrical 路线图与发行时间表、ROS 1 脚本/接口/功能包迁移、树莓派、生命周期节点、Build Farm、跟踪插桩、Intel ROS、跨机器安全、tf2、URDF、Eclipse、虚拟机器人、启动格式、软件包变体等 |\n| 入门与教程 | First Steps、Tutorials 导航、Beginner CLI Tools 导航、Beginner Client Libraries 导航、节点教程、话题教程入口、服务教程正文、动作教程正文、参数教程正文、环境配置教程、Intermediate、Advanced、Demos、Miscellaneous |
| 核心概念 | Concepts、Basic、Nodes、Topics、Services、Actions、Parameters、Discovery、Launch、Interfaces、Command Line Tools、Client Libraries |
| 进阶概念 | Intermediate、Composition、Executors、Logging、QoS、TF2、Domain ID、RQt、话题统计、交叉编译、不同中间件供应商、安全机制 |
| 高级概念 | Advanced、构建系统、内部接口、中间件实现 |\n| 应用指南 | How-To Guides、ROS 1 迁移入口、ros2 param、功能包开发、节点命令行参数 |\n| 其他 | Glossary、Ubuntu 区域语言和 apt 软件源配置片段 |

当前仓库已跟踪 **145 个 .rst 中文化源文件**，其中 **145 个属于 297 个正式候选文档**，候选文档覆盖率约为 **48.8%**。本轮继续新增完成 15 个候选文档中文化，尚余 **152 个候选文档**。所有页面仍需 Sphinx 构建、引用和技术术语复核。

## 构建与部署

- 已加入上游源码 overlay 构建脚本：scripts/prepare_build.py。
- 已加入 GitHub Actions 工作流：.github/workflows/deploy-docs.yml，包含构建 HTML、生成中文搜索索引和部署 GitHub Pages 的步骤。
- 工作流会在构建时检出上游 Humble 源码，将本仓库的中文页面覆盖到对应路径，再构建并部署 GitHub Pages。
- 首次构建曾因 Python 3.10 与上游锁定的 Sphinx 8.2.3 版本不兼容而失败；工作流已改用 Python 3.12。
- 构建日志发现本地缺少 Graphviz，工作流已增加 graphviz 系统依赖安装步骤。
- 首轮 Sphinx 检查还发现若干 reStructuredText 行内标记问题，已修正相关页面。
- 已完成本地构建准备脚本的配置注入测试，以及搜索索引脚本的独立测试。\n- 最近一次已完成构建仍失败，曾发现外部链接、行内标记及教程代码引用问题。最新翻译提交已触发 GitHub Actions；截至本次检查，工作流仍在排队/运行，尚未获得成功的完整 Sphinx HTML 构建和 GitHub Pages 部署结果。

## 待完成工作

- [ ] 翻译其余所有页面源文件（包括安装细节、教程正文、应用指南正文、迁移、开发者指南、发行版专题等）。
- [ ] 补齐所有二级、三级导航标题的中文化。
- [x] 已实现中文搜索页面、侧边栏搜索跳转和 HTML 搜索索引生成脚本；[ ] 仍需通过完整构建验证中文关键词与英文术语检索效果。
- [ ] 完成页面内锚点、跨页引用、上一页/下一页和外部链接检查。
- [ ] 完成 Sphinx 构建并处理全部警告。
- [ ] 验证 GitHub Pages 实际访问效果。
- [ ] 发布最终页面覆盖率和质量检查报告。

## 统计规则

- “已翻译初稿”不等于“已审核”或“已验证”。
- 代码、命令、API、类型名、参数名、话题名、路径及配置键保持原样。
- 不把英文原文仍然存在的页面标记为已翻译。
- 不以文件数量代替页面覆盖率；最终统计以 Sphinx 实际构建文档清单为准。
