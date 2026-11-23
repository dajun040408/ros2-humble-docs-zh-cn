# ROS 2 Humble 中文化进度

最后更新：2026-11-23

## 上游统计基线

- 上游仓库：ros2/ros2_documentation
- 上游分支：humble
- 候选文档总数：297
- 候选范围：剔除以下划线开头的辅助 .rst 文件及 source/_internal/ 内部文件。
- 统计方式：按上游候选 .rst 文件路径与当前仓库中的对应页面逐一比对。

## 当前覆盖情况

| 指标 | 数量 |
|---|---:|
| 官方候选文档 | 297 |
| 仓库中已有对应页面 | 297 |
| 缺失页面 | 0 |
| 路径覆盖率 | 100% |
| 已有中文正文的页面 | 297 |
| 需要完整翻译的发行版变更日志 | 6 |

**重要说明：** 六个 Complete Changelog 页面目前已创建中文标题、说明和上游导航入口，但逐包变更条目仍未完整翻译，页面中已明确标注这一点。因此，297/297 表示候选页面路径已全部覆盖，不等于 297 篇都已完成逐段翻译和质量验收。

## 本轮完成

本轮将剩余候选页面路径全部补齐，新增内容包括：

- ROS 1 Python 功能包迁移示例、VS Code 与 Docker 开发容器、ament_cmake 文档。
- ROS 2 质量指南、ROSCon 演讲索引。
- Fast DDS 扩展配置、RMW 实现开发、Discovery Server、ROS 2 tracing、ROS 2 安全密钥库、rqt_bag 插件、Webots macOS 安装。
- ROS 1 Bridge 与 rosbag、实时内核构建、IBM Cloud 部署、Eclipse Oxygen 与 rviz2。
- RViz Marker、RViz 自定义显示和面板、URDF、Xacro、Gazebo、robot_state_publisher 等教程。
- 六个发行版完整变更日志页面已补充中文导航入口，但逐条变更内容尚未翻译。

## 尚未完成的质量工作

- [ ] 将 Galactic、Humble、Iron、Jazzy、Kilted、Lyrical 六个 Complete Changelog 的逐包条目完整翻译。
- [ ] 全面审校所有页面的术语、代码示例、命令和配置说明。
- [ ] 核对所有 toctree 导航层级、页面标题和目录结构。
- [ ] 检查所有内部链接、锚点、图片引用、literalinclude 和跨页引用。
- [ ] 运行完整 Sphinx 构建，处理全部错误和重要警告。
- [ ] 验证 GitHub Pages 实际部署和页面跳转。
- [ ] 形成最终逐页质量验收报告。

## 构建与部署状态

- GitHub Actions 工作流：`.github/workflows/deploy-docs.yml`。
- 最新提交已触发 GitHub Actions，但最近多次提交触发的独立工作流出现 cancelled 状态；最新一次仍在运行。
- 目前没有证据证明完整 Sphinx 构建和 GitHub Pages 部署已成功。
- 不得将 GitHub 文件创建成功等同于网站构建成功。

## 统计规则

- “路径覆盖”只表示对应候选文件存在。
- “已有中文正文”表示页面有中文内容，不代表全文逐句翻译完成。
- 六个发行版变更日志的中文导航页不计为完整变更日志翻译完成。
- 代码、命令、API、类型名、参数名、话题名、路径及配置键应保持原样。
- 最终完成状态必须结合逐页内容审查和完整 Sphinx 构建结果确认。
