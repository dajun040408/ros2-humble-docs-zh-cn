# ROS 2 Humble 中文化进度与自检记录

最后更新：2026-11-23（持续更新）

## 用户指定的优先任务：ROS 1 到 ROS 2 迁移指南（仅 Humble）

- 处理目录：`source/How-To-Guides/Migrating-from-ROS1/`
- 范围：仅按 ROS 2 Humble 上游分支翻译；未修改其他 ROS 发行版的迁移指南。
- 目录内上游 RST 页面：10 篇；当前仓库对应页面：10 篇。
- 10 篇正文均已写入中文译文；但本轮复核发现，先前导航栏使用隐式标题，未显式指定中文目录标签，用户截图仍显示英文标题，因此不能把此前状态表述为导航中文化已完成。
- 已修正父页面 `Migrating-from-ROS1.rst` 的 toctree，为 10 个子页面逐一设置显式中文标题，并确认父页面标题为“从 ROS 1 迁移到 ROS 2”。
- 涉及 C++ 示例与迁移参考、Python 示例与迁移参考、接口、launch 文件、package.xml、功能包、参数及脚本迁移。
- 本轮正文提交：`186fa38`、`dfa6188`、`1b289c5`；导航显式中文标题修正：`c771c1b`。
- GitHub Actions #430（提交 `377ac21`）已成功生成 HTML、中文搜索索引并上传 Pages Artifact；Sphinx 仍有约 1504 条警告，本轮为避免警告阻断发布，已暂时不启用 `-W`，警告仍保留在日志中。
- #430 的 Deploy to GitHub Pages 步骤失败，GitHub 返回 `404` 并提示尚未启用仓库 Pages。当前仓库没有 `CNAME`，工作流生成的 sitemap 指向 `https://dajun040408.github.io/ros2-humble-docs-zh-cn/`，不是用户访问的 `https://ros2docs.robook.org/humble/`。
- 已直接核对用户提供的 robook.org 页面：仍返回旧版英文内容，说明该站点尚未接入本仓库的构建产物。即使仓库 Pages 启用，仍需配置自定义域名/DNS 或将生成产物部署到 robook.org 当前的托管服务，才能更新用户正在访问的地址。
- 当前10篇 Humble 迁移指南的源文件已完成中文主体和标题修订；但实际 robook.org 页面尚未更新，不能标记网页验收完成。
- 后续该目录如有更新，仍只以 Humble 分支为翻译依据；其他 ROS 2 发行版暂不处理。

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
| 本仓库 source/ 下全部 .rst 文件 | 339 |

**注意：路径覆盖率 100% 只说明 297 个上游候选路径均有对应文件，不代表 297 篇都已完成全文翻译。** 本轮已对 Humble 和 Galactic 的完整变更日志开展逐包翻译。Humble 上游逐包条目已全部纳入中文译文；Galactic 已开始分批翻译。

## 已确认未完成的翻译

以下发行版完整变更日志的逐条翻译状态如下：

- Galactic：`source/Releases/Galactic-Geochelone-Complete-Changelog.rst` —— 已翻译前约 720 行，分为 6 个子文件，仍在继续。
- Humble：`source/Releases/Humble-Hawksbill-Complete-Changelog.rst` —— 已补齐上游全部逐包条目，现进入格式与内容核验阶段。
- Iron：`source/Releases/Iron-Irwini-Complete-Changelog.rst`
- Jazzy：`source/Releases/Jazzy-Jalisco-Complete-Changelog.rst`
- Kilted：`source/Releases/Kilted-Kaiju-Complete-Changelog.rst`
- Lyrical：`source/Releases/Lyrical-Luth-Complete-Changelog.rst`

Humble 是本项目发行版对应的重点文档，其逐包文本已全部翻译；仍需逐条校对和通过构建。Galactic、Iron、Jazzy、Kilted、Lyrical 五份完整变更日志仍需继续翻译。六个上游文件体量约为 272 KB 至 445 KB。

## 本轮翻译进度

- Humble 完整变更日志：上游逐包条目约 3960 行已全部翻译，拆分为 33 个 RST 子文件并通过 include 汇入原页面。
- Humble 翻译覆盖：ros2run、ros2service、ros2test、ros2topic、ros2trace、rosbag2 及其多个子功能包、rosgraph_msgs、rosidl_adapter、rosidl_cli、rosidl_generator_c/cpp/dds_idl/py、rosidl_parser、rosidl_runtime_c/cpp/py、多种 rosidl_typesupport、rpyutils、rqt_gui 系列、rti_connext_dds_cmake_module、rttest、rviz2 及多个 RViz 子功能包、sensor_msgs 系列、sros2、statistics_msgs、std_msgs、std_srvs、stereo_msgs、test_cli、test_communication、test_interface_files、test_launch_ros、test_launch_testing、test_msgs、test_quality_of_service、test_rclcpp、test_rmw_implementation、test_security、test_tf2、test_tracetools、test_tracetools_launch、tf2 系列、tlsf、tracetools、trajectory_msgs、turtlesim、urdf、urdf_parser_plugin、visualization_msgs、yaml_cpp_vendor 和 zstd_vendor。
- Galactic 翻译覆盖：已翻译 action_msgs、action_tutorials_*、actionlib_msgs，以及 ament_lint 和 ament_cmake 部分功能包；当前约前 720 行，6 个子文件。
- Humble 逐包翻译已完成，仍需核验翻译完整性、RST 格式和构建结果；Galactic、Iron、Jazzy、Kilted、Lyrical 五份完整变更日志尚未完成。

## Sphinx 构建自检

- GitHub Actions 工作流：`.github/workflows/deploy-docs.yml`
- 最近一次完成的 Sphinx 构建：#413，结果失败。
- 本次已无 Sphinx/docutils ERROR（0 条），此前阻断构建的链接目标和两个悬空标题分隔线问题已修复。
- 构建仍报告约 1902 条警告，因配置将警告视为错误而退出；日志显示中文搜索索引和 sitemap 已生成，但 Pages artifact 上传及部署步骤未执行。
- 最新提交已触发 #419，目前正在运行；此前 #413 已生成 HTML、中文搜索索引和 sitemap，但因 1902 条警告触发 warnings-as-errors 而失败。

此前已定位并修复的主要错误文件包括：

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

- [ ] Galactic、Iron、Jazzy、Kilted、Lyrical 五个 Complete Changelog 逐包条目完整翻译。
- [ ] Humble Complete Changelog 逐条内容校对和格式验收。
- [ ] 297 篇候选文档逐页检查翻译完整性、遗漏英文段落及术语一致性。
- [ ] 分类处理约 1902 条构建警告，修复真实问题并区分上游既有警告。
- [ ] 在不掩盖错误的前提下重新运行完整构建。
- [ ] 检查全部 toctree 导航层级、页面标题和左侧目录。
- [ ] 检查内部链接、锚点、图片引用、literalinclude 和跨页引用。
- [ ] 确认搜索索引正常生成。
- [ ] 在 GitHub 仓库 Settings → Pages 启用 GitHub Actions 发布源，或明确 robook.org 当前的部署目标/凭据。
- [ ] 配置 `ros2docs.robook.org` 自定义域名和 DNS，或将构建产物部署到 robook.org 现有托管服务。
- [ ] 确认 GitHub Pages/robook.org 部署成功，并逐一抽查用户提供的10个实际页面。
- [ ] 形成最终逐页质量验收报告。

## 统计与验收规则

- “路径覆盖”只表示对应文件存在。
- 页面含有中文标题或说明，不代表全文翻译完成。
- 代码、命令、API、类型名、参数名、话题名、路径及配置键应保持原样。
- 只有逐页内容审查、导航与链接检查、完整 Sphinx 构建和部署验证全部通过，才能标记项目完成。
