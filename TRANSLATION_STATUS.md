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

| 文件 | 状态 |
|---|---|
| source/index.rst | 已翻译初稿 |
| source/About-ROS.rst | 已翻译初稿 |
| source/Installation.rst | 已翻译初稿 |
| source/Tutorials.rst | 已翻译初稿 |
| source/First-Steps.rst | 已翻译初稿 |
| source/How-To-Guides.rst | 已翻译初稿 |
| source/Concepts.rst | 已翻译初稿 |
| source/Concepts/Basic.rst | 已翻译初稿 |
| source/Concepts/Basic/About-Nodes.rst | 已翻译初稿 |
| source/Concepts/Basic/About-Topics.rst | 已翻译初稿 |
| source/Concepts/Basic/About-Services.rst | 已翻译初稿 |
| source/Concepts/Basic/About-Actions.rst | 已翻译初稿 |
| source/Concepts/Basic/About-Parameters.rst | 已翻译初稿 |
| source/Concepts/Basic/About-Discovery.rst | 已翻译初稿 |
| source/Concepts/Basic/About-Launch.rst | 已翻译初稿 |
| source/Concepts/Basic/About-Client-Libraries.rst | 已翻译初稿 |
| source/Concepts/Intermediate.rst | 已翻译初稿 |
| source/Glossary.rst | 已翻译初稿 |

当前已提交 18 个翻译初稿，约占 298 个构建候选源文件的 6.0%。这不是全站完成率；这些页面仍需 Sphinx 构建、引用和技术术语复核。

## 构建与部署

- 已加入上游源码 overlay 构建脚本：scripts/prepare_build.py。
- 已加入 GitHub Actions 工作流：.github/workflows/deploy-docs.yml。
- 工作流会在构建时检出上游 Humble 源码，将本仓库的中文页面覆盖到对应路径，再构建并部署 GitHub Pages。
- 首次构建曾因 Python 3.10 与上游锁定的 Sphinx 8.2.3 版本不兼容而失败；工作流已改用 Python 3.12，后续运行结果待核验。
- 当前尚未获得成功的 Sphinx HTML 构建和 GitHub Pages 部署结果。

## 待完成工作

- [ ] 翻译其余所有页面源文件（包括安装细节、教程、应用指南、概念、迁移、开发者指南、发行版等）。
- [ ] 补齐所有一级/二级导航标题的中文化。
- [ ] 完成中文搜索分词与英文术语检索。
- [ ] 完成页面内锚点、跨页引用、上一页/下一页和外部链接检查。
- [ ] 完成 Sphinx 构建并处理全部警告。
- [ ] 验证 GitHub Pages 实际访问效果。
- [ ] 发布最终页面覆盖率和质量检查报告。

## 统计规则

- “已翻译初稿”不等于“已审核”或“已验证”。
- 代码、命令、API、类型名、参数名、话题名、路径及配置键保持原样。
- 不把英文原文仍然存在的页面标记为已翻译。
- 不以文件数量代替页面覆盖率；最终统计以 Sphinx 实际构建文档清单为准。
