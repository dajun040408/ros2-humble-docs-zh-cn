# ROS 2 Humble 中文文档项目

本项目旨在基于 ROS 2 官方 Humble 文档源码，制作完整、可维护的简体中文文档站点。

> 本项目是社区翻译与本地化项目，不是 ROS 官方发布或背书的中文版本。导入上游源码时必须保留许可证、版权声明和第三方资源许可。

## 上游来源

- 上游仓库：[ros2/ros2_documentation](https://github.com/ros2/ros2_documentation)
- 上游分支：[humble](https://github.com/ros2/ros2_documentation/tree/humble)
- 官方文档：[ROS 2 Humble](https://docs.ros.org/en/humble/)
- 参考中文站点：[Robook](https://ros2docs.robook.org/humble/index.html)

## 项目目标

- 完整覆盖 ROS 2 Humble 文档页面。
- 翻译正文、标题、导航及说明文字。
- 保留 Sphinx / reStructuredText 结构、代码、命令、API 名称和交叉引用。
- 构建包含左侧目录、页面内目录、搜索和页面跳转的 HTML 网站。
- 记录真实翻译进度、构建结果和链接检查结果。

## 当前状态

项目刚完成初始化。上游 Humble 文档树初步盘点得到 311 个 .rst 文件，最终参与构建的页面数以完整源码导入后的 Sphinx 结果为准。当前仓库尚未导入完整上游源码，不能视为已完成翻译。

- [翻译进度](TRANSLATION_STATUS.md)
- [术语表](TERMINOLOGY.md)
- [源码导入与构建说明](docs/BUILDING.md)

## 许可证与归属

导入上游文件时，保留上游 LICENSE、版权声明、文件头及第三方资产许可信息。翻译内容明确标注为非官方社区翻译。对再分发条件不明确的资源，先核实再纳入。

## 翻译原则

1. 以 Humble 上游文档为技术基线，不混入 Jazzy、Rolling 等发行版内容。
2. 不翻译代码标识符、命令、文件路径、话题名、消息类型、API 名称和配置键。
3. 不随意删减、总结或改变原文技术结论。
4. 修改标题或导航时，验证交叉引用和锚点。
5. 每批翻译更新进度，并执行 Sphinx 构建和链接检查。
