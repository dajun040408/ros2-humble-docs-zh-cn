# ROS 2 Humble 中文文档项目

本项目基于 **ROS 2 官方 Humble 文档源码**制作简体中文翻译与本地化网站。

> 本项目是社区翻译项目，不是 ROS 官方发布或背书的中文版本。上游版权、许可证和第三方资源声明均应保留。

## 上游来源

- 上游仓库：[ros2/ros2_documentation](https://github.com/ros2/ros2_documentation)
- 上游分支：[humble](https://github.com/ros2/ros2_documentation/tree/humble)
- 官方文档：[ROS 2 Humble](https://docs.ros.org/en/humble/)
- 参考中文站点：[Robook ROS 2 文档](https://ros2docs.robook.org/humble/index.html)

## 构建架构

本仓库采用“中文翻译覆盖层”方式管理，不复制上游全部二进制图片和构建资源：

1. GitHub Actions 检出本仓库的 main 分支。
2. 同时检出 ros2/ros2_documentation 的 humble 分支。
3. 将本仓库 source/ 下的中文 .rst 文件覆盖到上游对应路径。
4. 将 Sphinx 配置切换为简体中文，并固定 Humble 发行版参数。
5. 构建完整 HTML 网站并部署到 GitHub Pages。

这样既保留了上游全部图片、模板、扩展和导航资源，也避免复制 50 MB 以上的重复资源。上游源码只在构建环境中检出，不会被修改。

## 本地构建

请参阅 [源码导入与本地构建说明](docs/BUILDING.md)。

## 翻译进度

请查看 [TRANSLATION_STATUS.md](TRANSLATION_STATUS.md)。当前页面仍处于分批翻译阶段，未完成页面不会被标记为已翻译。

## 术语规范

统一术语见 [TERMINOLOGY.md](TERMINOLOGY.md)。

## 许可证与归属

上游文档源码及资源的许可证、版权声明应随构建保留。翻译文本应标注为非官方社区翻译。对再分发条件不明确的第三方资源，应先核实再纳入。
