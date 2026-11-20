# ROS 2 Humble 中文化进度

最后更新：2026-11-20

## 上游基线

- 上游仓库：ros2/ros2_documentation
- 上游分支：humble
- 已上传并核对源码归档：ros2_documentation_humble.tar.gz
- 上游 Git tree：790 个条目，其中 684 个文件。
- .rst 文件总数：311。
- 根据上游 Sphinx exclude_patterns 初步排除 13 个辅助文件，得到 298 个构建候选文档源文件。最终 HTML 页面数以 Sphinx 构建输出为准。

## 当前已提交翻译页面

| 模块 | 已翻译初稿 |
|---|---|
| 首页与项目入口 | index、About ROS、Installation、Releases、Contact、The ROS 2 Project、Package Docs、Related Projects、Citations |
| 入门与教程导航 | First Steps、Tutorials、Beginner CLI Tools、Beginner Client Libraries、Intermediate、Advanced、Demos、Miscellaneous |
| 核心概念 | Concepts、Basic、Nodes、Topics、Services、Actions、Parameters、Discovery、Launch、Interfaces、Command Line Tools、Client Libraries |
| 进阶概念 | Intermediate、Composition、Executors、Logging、QoS、TF2 |
| 其他 | How-To Guides、Glossary |

当前已提交 **37 个 .rst 翻译初稿**，约占 298 个构建候选源文件的 **12.4%**。这不是全站完成率；这些页面仍需 Sphinx 构建、引用和技术术语复核。

## 构建与部署

- 已加入上游源码 overlay 构建脚本：scripts/prepare_build.py。
- 已加入 GitHub Actions 工作流：.github/workflows/deploy-docs.yml，包含构建 HTML、生成中文搜索索引和部署 GitHub Pages 的步骤。
- 工作流会在构建时检出上游 Humble 源码，将本仓库的中文页面覆盖到对应路径，再构建并部署 GitHub Pages。
- 首次构建曾因 Python 3.10 与上游锁定的 Sphinx 8.2.3 版本不兼容而失败；工作流已改用 Python 3.12。
- 构建日志发现本地缺少 Graphviz，工作流已增加 graphviz 系统依赖安装步骤。
- 首轮 Sphinx 检查还发现若干 reStructuredText 行内标记问题，已修正相关页面。
- 已完成本地构建准备脚本的配置注入测试，以及搜索索引脚本的独立测试。\n- 目前尚未获得修正后的完整 Sphinx HTML 构建和 GitHub Pages 部署结果。

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
