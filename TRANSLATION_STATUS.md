# ROS 2 Humble 中文化进度与自检记录

最后更新：2026-11-23（持续更新）

## 上游统计基线

- 上游仓库：ros2/ros2_documentation
- 上游分支：humble
- 官方候选文档：297 篇
- 候选范围：剔除以下划线开头的辅助 .rst 文件及 source/_internal/ 内部文件。
- 统计方式：逐项比较上游 humble 分支与本仓库 main 分支中的 source/**/*.rst 路径。

## 路径覆盖自检

| 指标 | 结果 |
|---|---:|
| 上游候选文档 | 297 |
| 本仓库对应页面 | 297 |
| 缺失页面 | 0 |
| 路径覆盖率 | 100% |
| 本仓库 source/ 下全部 .rst 文件 | 300 |

**注意：路径覆盖率 100% 只说明 297 个上游候选路径均有对应文件，不代表 297 篇都已完成全文翻译。** 本轮已直接检查六个 Complete Changelog 页面，确认它们是中文说明/导航页，逐包变更记录仍为英文上游链接，并非完整中文译本。

## 已确认未完成的翻译

以下六个页面均未完成逐条变更记录翻译：

- Galactic：`source/Releases/Galactic-Geochelone-Complete-Changelog.rst`
- Humble：`source/Releases/Humble-Hawksbill-Complete-Changelog.rst`
- Iron：`source/Releases/Iron-Irwini-Complete-Changelog.rst`
- Jazzy：`source/Releases/Jazzy-Jalisco-Complete-Changelog.rst`
- Kilted：`source/Releases/Kilted-Kaiju-Complete-Changelog.rst`
- Lyrical：`source/Releases/Lyrical-Luth-Complete-Changelog.rst`

其中 Humble 变更日志是本项目发行版对应的重点未完成项。六个上游文件体量约为 272 KB 至 445 KB，不能以简短中文导航说明替代逐条翻译。

## 本轮翻译进度

- Humble 完整变更日志已逐条翻译至上游文件约第 2640 行，分为 22 个 RST 子文件并通过 include 汇入原页面。
- 本轮新增翻译 ros2run、ros2service、ros2test、ros2topic、ros2trace、rosbag2 及其多个子功能包、rosgraph_msgs、rosidl_adapter、rosidl_cli、rosidl_generator_c/cpp/dds_idl/py、rosidl_parser、rosidl_runtime_c/cpp/py，以及多种 rosidl_typesupport 的变更记录。
- Humble 后续条目仍待翻译；Galactic、Iron、Jazzy、Kilted、Lyrical 五份完整变更日志尚未完成。

## Sphinx 构建自检

- GitHub Actions 工作流：`.github/workflows/deploy-docs.yml`
- 最近一次完整日志：#386（失败，12 条 RST 错误）；#388 因后续提交而取消。
- 已修复 #386 暴露的匿名链接和变更日志行内标记错误，并继续提交翻译批次。
- 最近运行 #395（提交 `6bafcc8`）正在执行 HTML 构建；最新翻译提交已触发 #396，当前处于待运行状态。
- 本记录更新时尚无成功构建及部署证据。
- 在 Sphinx 构建成功前，搜索索引和 Pages artifact/部署不能视为通过。

已定位的错误文件包括：

- `source/Concepts/Basic/About-Client-Libraries.rst`
- `source/How-To-Guides/Using-Python-Packages.rst`
- `source/Tutorials/Intermediate/URDF/Exporting-an-URDF-File.rst`
- `source/index.rst`
- `source/Tutorials/Intermediate/Rosdep.rst`
- `source/Installation/ROS-2-Mirrors.rst`
- `source/Package-Docs.rst`
- `source/Related-Projects/Intel-ROS2-Projects.rst`
- `source/The-ROS2-Project/Contributing/Code-Style-Language-Versions.rst`
- `source/The-ROS2-Project/Contributing/Contributing-to-code/Making-a-PR.rst`

此外，构建中大量出现中文标题下划线长度不足、RST 行内标记不匹配、重复显式目标等警告。必须逐类修复，不能简单关闭 warnings-as-errors 来掩盖问题。

## 尚未通过的验收项目

- [ ] 六个 Complete Changelog 逐包条目完整翻译。
- [ ] 297 篇候选文档逐页检查翻译完整性、遗漏英文段落及术语一致性。
- [ ] 根据最新 Actions 日志继续修复 Sphinx/docutils ERROR。
- [ ] 分类处理构建警告，并重新运行完整构建。
- [ ] 检查全部 toctree 导航层级、页面标题和左侧目录。
- [ ] 检查内部链接、锚点、图片引用、literalinclude 和跨页引用。
- [ ] 确认搜索索引正常生成。
- [ ] 确认 GitHub Pages 部署成功并抽查实际页面跳转。
- [ ] 形成最终逐页质量验收报告。

## 统计与验收规则

- “路径覆盖”只表示对应文件存在。
- 页面含有中文标题或说明，不代表全文翻译完成。
- 代码、命令、API、类型名、参数名、话题名、路径及配置键应保持原样。
- 只有逐页内容审查、导航与链接检查、完整 Sphinx 构建和部署验证全部通过，才能标记项目完成。
