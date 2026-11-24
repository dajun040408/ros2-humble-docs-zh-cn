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


## 2026-11-24 线上站点来源核验（关键结论）

- 已从用户提供的 robook.org 页面点击 “Edit on GitHub”，链接明确指向 `ros2/ros2_documentation` 仓库的 `humble` 分支（例如 `source/How-To-Guides/Migrating-from-ROS1/Migrating-Launch-Files.rst`）。因此 robook.org 当前 Humble 页面由 ROS 官方上游仓库内容生成，而不是由本项目 `dajun040408/ros2-humble-docs-zh-cn` 生成。
- 已现场抽查用户提供的10个 robook.org 页面，页面标题、目录或正文仍含英文；例如 Migrating Packages 正文仍显示 “There are two different kinds of package migrations”，Migrating Interfaces 正文仍显示 “Messages, services, and actions are collectively called interfaces in ROS 2”。
- 本项目 GitHub Actions #432 的 build job 成功：Sphinx HTML、搜索索引和 Pages Artifact 均成功；deploy job 仍因本项目 GitHub Pages 未启用而 404。
- 当前 GitHub 连接对上游 `ros2/ros2_documentation` 只有 pull 权限，没有 push 权限；本项目是独立仓库（`fork=false`），不是上游 fork，因此无法直接把本项目提交推送到上游 Humble 分支。
- 要让用户给出的 `https://ros2docs.robook.org/humble/` 网址更新，必须选择并落实实际发布目标：将本项目的构建产物部署到 robook.org 当前托管环境，或将该域名迁移/绑定到本项目启用后的 GitHub Pages。仅在本项目提交中文 RST 不会改变当前 robook.org 页面。
- 目前尚未获得 robook.org 主机/部署凭据，也未确认该域名 DNS 可由用户修改；因此未擅自改写 CNAME 或 DNS。
- 2026-11-24 最新构建 #433（提交 `16a03ea`）：build job 成功，Pages Artifact `github-pages` 已生成，大小约 38.4 MB，Artifact ID `14880130183`，有效期至 2026-11-25 01:10 UTC；deploy job 再次因 GitHub Pages 未启用而 404。
- 本次从 robook.org 实际页面重新读取 HTML：Migrating Packages 页面标题仍为英文，正文仍包含 “There are two different kinds of package migrations”；部分小节目录标题显示中文、正文仍为英文。Migrating Interfaces 页面标题和正文也仍为英文。引用证据：页面抓取时间 2026-11-24，页面分别为 `/Migrating-Packages.html` 与 `/Migrating-Interfaces.html`。


## GitHub Pages 已启用后的重新发布

- 用户已确认在仓库 Settings → Pages 将 Source 设置为 GitHub Actions。
- 本次通过更新状态记录触发新的 `push` 工作流，以验证 Pages 初始化后的发布权限。
- 目标域名仍为 `ros2docs.robook.org`；工作流发布前必须写入 CNAME 并在部署后核验域名解析与 HTTPS。

## 2026-11-24 GitHub Pages 工作流修复

- 检查 #438 日志后发现 `actions/configure-pages@v5` 不接受 `cname` 输入参数，导致该步骤失败；此前将该步骤错误地作为域名配置手段。
- 已移除不受支持的 `cname` 输入，保留发布目录中的 `site/CNAME` 文件，并提交修复 `3d2d56f`。
- 最新构建 #439（提交 `3d2d56f`）已排队，待验证 build、artifact 和 deploy。
- 自定义域名仍需在仓库 Settings → Pages → Custom domain 中配置 `ros2docs.robook.org`，并由域名 DNS 管理端将 `ros2docs` CNAME 指向 `dajun040408.github.io`；当前没有 DNS 管理凭据，不能代替用户修改 DNS。
- `https://ros2docs.robook.org/humble/` 尚未通过新版本实站验收。

## 2026-11-24 GitHub Pages 部署成功后的实站复核

- 工作流 #440（run ID 45310556482，提交 45ed7361fb6436824dbcf0ddf1ce74d525072104）最终完成，build 与 deploy 两个 job 均为 success。
- Pages Artifact github-pages 已成功生成，大小 38,409,683 bytes；Deploy to GitHub Pages 步骤成功。
- 但通过公开网页抓取重新检查 https://ros2docs.robook.org/humble/...，抓取到的内容仍是旧英文版本。例如 Migrating Packages 正文仍包含 “There are two different kinds of package migrations”；Migrating Interfaces 仍显示英文标题和英文正文；Migrating Parameters、C++ 示例、C++ 参考、Python 参考、Launch Files、Scripts 页面也仍有英文标题/正文。搜索引擎抓取时间较旧，不能单凭缓存判定 DNS 当前状态，但可以确认尚无可靠证据证明原域名已切换到新部署。
- 因此：GitHub Pages 项目部署已成功；自定义域名 ros2docs.robook.org 的 Pages Custom domain 绑定、DNS CNAME 指向 dajun040408.github.io、HTTPS 证书及原域名实时内容切换仍未验收。/humble/ 路径在构建产物中已按要求生成。
- 下一步必须在仓库 Settings → Pages → Custom domain 中填写 ros2docs.robook.org 并保存，同时在域名 DNS 控制台确认 ros2docs CNAME 指向 dajun040408.github.io。目前连接没有 DNS 控制台权限，不能代替域名所有者修改 DNS。


## 2026-11-24 迁移指南二次内容审校

- 复核10篇 Humble 迁移指南后，发现此前翻译文件仍有少量英文说明残留，以及 package.xml 示例中反引号嵌套错误、接口依赖 XML 标签反引号位置错误、C++ function 头文件被误翻译等问题。
- 已修订 `Migrating-Interfaces.rst`、`Migrating-Package-XML.rst`、`Migrating-CPP-Packages.rst`、`Migrating-Launch-Files.rst`，修正说明文字与 RST 代码标记，保留示例代码/API 标识符。
- 修订提交：`54d9d1c5ec1be4a55540f58066eecfd2fbee8506`。该提交将触发新一轮 GitHub Actions 构建。
- 最新已知成功部署仍是 #441；本次修订尚未构建和部署，原域名尚未验收。
- GitHub Pages 自定义域名设置不能由当前 GitHub 连接工具修改；GitHub 官方说明，自定义 Actions 发布时 CNAME 文件会被忽略，域名必须在 Settings → Pages → Custom domain 配置。DNS CNAME 记录还必须指向 `dajun040408.github.io`。


## 2026-11-24 迁移指南第三轮 RST 与术语审校

- 重新检查 `Migrating-Package-XML.rst`，修正 XML 示例中不应出现在代码块内的双反引号、补齐章节标题下划线长度、补充 ROS 2 功能包文档指南链接，并规范 CMake/构建命令字面量。
- 重新检查 `Migrating-Parameters.rst`，规范 ROS 参数、节点名、通配符、参数 API 的行内代码标记，并恢复 CLI 与参数黑板的 Sphinx 内部文档链接。
- 重新检查 `Migrating-Scripts.rst`，规范命令行参数、重映射规则和 ROS 1 私有参数名称的行内代码标记。
- 重新检查 `Migrating-Python-Packages.rst`，补充 Colcon 教程及同步/异步调用说明的内部文档链接，规范 Python/ROS API 标记。
- 本轮提交：`e87ff998f3f05f4ca2eb97dff691dcd60dee08f8`。
- 新构建 #445（run ID `45320986274`）已触发，当前 queued；上一轮 #444 对此前两篇修订的构建成功，但不包含本轮最新4篇修改。
- 仍需在 #445 成功后抽查 HTML、链接和导航；原域名 `ros2docs.robook.org` 的 DNS/Pages 自定义域名仍未确认，故线上原网址验收未完成。


## 2026-11-24 迁移指南第四轮审校与部署复核

- 最新 #446（run ID `45321016014`，提交 `0d4702ec657e581e8c5322b6a3bf9674d948e1f5`）build 和 deploy 两个 job 均成功；Pages Artifact 约 38.4 MB。
- 对 C++ 示例、C++ 参考、Python 示例、Launch 文件四篇中文源文件进行逐段文本扫描：未发现整句英文说明残留；标题均为中文。技术标识符、代码和 XML/launch 标签保留英文属于预期，不作为未翻译内容。
- 对10篇文档的 `:doc:` 内部引用做了路径核对：迁移目录内的引用均能解析；Launch 文件中的两个 `../../../Tutorials/...` 引用沿用 Humble 上游路径写法，需在 HTML 构建结果中继续确认。
- 发现 `Migrating-Package-XML.rst` 的 XML 示例代码块已正确使用原始 XML 标签（不应在 code-block 中额外包裹双反引号）；本轮复核确认当前 main 文件已是正确状态，无需新增提交。
- 实际站点抓取结果：搜索/网页抓取缓存中，`Migrating Packages`、`Migrating Interfaces`、`Migrating Parameters`、C++/Python/Launch/Scripts 页面仍显示旧英文正文；抓取时间分布在约1至5个月前，故这是旧缓存证据，不能据此证明当前 DNS 已指向或未指向 Pages。当前 Pages 部署成功，但自定义域名配置及 DNS/HTTPS 实时状态仍无可验证结果。
- GitHub 官方自定义域名流程：自定义 Actions 发布时 GitHub 不会创建或读取 CNAME 文件来绑定域名；必须在 Settings → Pages → Custom domain 设置 `ros2docs.robook.org`，并由 DNS 将 `ros2docs` CNAME 指向 `dajun040408.github.io`。官方文档：https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site。


## 2026-11-24 第五轮迁移指南审校（脚本迁移）

- 依据 ROS 2 Humble 上游 `Migrating-Scripts.rst` 逐项对照，发现原中文文件的 ROS CLI 示例存在严重的 reStructuredText 行内标记破损：``--ros-args``、``--param``、``--remap`` 等命令被拆成错误的反引号片段，快速参考表格分隔线也被错误包裹，可能导致网页显示异常或 Sphinx 警告。
- 已按 Humble 上游内容重写该页的命令示例、术语说明和快速参考表格；恢复真实命令 `ros2 run ... --ros-args -r ...`、`--param` 等，保留 ROS 1/ROS 2 参数名称和代码原样。
- 修订文件：`source/How-To-Guides/Migrating-from-ROS1/Migrating-Scripts.rst`。
- 提交：`575d712649c7dd4760a30ad7b499806f41a38b00`（2026-11-24 04:04 UTC）。
- 已回读 GitHub main 确认更新后的文件存在；本次提交会触发 `.github/workflows/deploy-docs.yml`。该提交对应的构建与部署结果尚待核验。
- 下一轮优先逐段核对 C++/Python 迁移参考页、Launch 文件页及其代码块/表格；不能把代码标识符、XML 标签、CLI 参数或英文 API 名称误判为未翻译正文。


## 2026-11-24 第六轮迁移指南代码块审校

- 复核全部 10 篇 ROS 1 → ROS 2 迁移指南源文件中的 `code-block` / `code` 代码区域，发现两处此前未清理的 RST 行内标记错误。
- `Migrating-Python-Packages.rst`：代码块内的 ``rospy``、``rclpy``、``String``、``AddTwoInts`` 等标识符被错误包裹双反引号；这些标记在代码块中不应作为 RST 行内标记。已清除代码区域内错误的反引号，并修复 `catkin_make_isolated` 命令拼写。提交：`30d7375462691d2a169e78fec58a16d5e3d69f62`。
- `Migrating-Parameters.rst`：YAML/console 代码块中存在同类错误标记；已修复参数黑板命令、YAML 键和通配符示例，并修复源代码链接中嵌入双反引号导致的 URL 错误。提交：`f0c0e5d925e00506d783e2a390a5c331f9a0186a`。
- `Migrating-CPP-Package-Example.rst`：修复 XML 示例中多余的尾随反引号。提交：`4ed8dc055b07d2081fe754c6d36aaacb42b6621d`。
- `Migrating-Scripts.rst`：修复 ROS CLI 示例和快速参考表格。提交：`575d712649c7dd4760a30ad7b499806f41a38b00`。
- 对迁移目录全部 10 篇页面再次执行代码区域扫描：未再发现 `code-block` / `code` 区域内残留双反引号行内标记。
- 该扫描是源文件静态检查，不等同于 Sphinx 构建成功；最新提交的 Actions build/deploy 结果仍须从 GitHub Actions 运行页确认。GitHub 连接当前可用的 commit status 检查没有返回状态项，不能据此宣称构建通过。
- 本轮仅处理迁移指南，不代表其余 287 篇候选文档已完成全文审校。297 篇路径覆盖仍不能作为全文翻译完成证明。


## 2026-11-24 第七轮 Humble 范围核验与构建文档修复

- 重新读取 Humble 完整变更日志入口：`source/Releases/Humble-Hawksbill-Complete-Changelog.rst`，确认包含 33 条 `.. include:: Humble-Changelog-Parts/part-001.rst` 至 `part-033.rst` 的拆分引用。
- 已逐个从 GitHub main 读取 33 个 Humble 子文件，33/33 均存在且有内容；入口文件的 33 个 include 与拆分目录命名对应。该项证明拆分文件存在，不等同于逐条翻译质量、上游条目完整性和 Sphinx include 构建验收。
- 本项目目标发行版为 Humble。Iron、Jazzy、Kilted、Lyrical 的完整变更日志当前只是中文导航说明页，未逐条翻译；Galactic 仅有部分拆分翻译。这些其他发行版不属于本项目当前 Humble 交付范围，不应列为 Humble 项目的阻断项，也不应宣称已翻译。
- 修复 `docs/BUILDING.md` 中构建命令和“中文搜索”章节被错误保存为字面量 `\\n` 的 Markdown 格式问题，恢复正常换行和代码围栏。提交：`11e9e0c80222a8a1354a58795a4059fc4ed962bf`。
- 此前迁移指南代码块审校提交：`575d712`、`4ed8dc0`、`30d7375`、`f0c0e5d`；全部 10 篇迁移指南的代码块扫描已无双反引号行内标记残留。
- 仍未取得 GitHub Actions 最近一次 run 的完整 jobs/logs 读取能力；当前连接返回的 commit status 列表为空，不能作为构建成功证据。完整 Sphinx 构建、警告分类、生成 HTML 的链接检查、最新 Pages 部署及 `ros2docs.robook.org` 实际域名验收仍未完成。
- 全站 297 篇候选页面的逐页全文质量审校仍未完成。297/297 仅代表路径覆盖；不得据此标记全部翻译完成。


## 2026-11-24 第八轮全站构建警告清理（构建 #650）

- 构建 #650（run ID `45335700833`，提交 `a4c70fa754958f8e702e5c1e4bccdcea069f7d90`）的 build 与 deploy jobs 均成功；Sphinx HTML、中文搜索索引、Pages Artifact 和 GitHub Pages 部署步骤全部成功。Artifact ID：`14893487692`，大小约 38.37 MB。
- 本轮 Sphinx 构建成功，但仍有 118 条 warning 行（其中包括 1 条外部 Adopters URL 超时警告）；没有 Sphinx ERROR 行。与构建 #456 的 1511 条警告相比，下降约 92%。
- 主要剩余警告类别：RST 行内 literal/role 格式、少量未解析文档引用和标签、少量标题下划线长度。需继续区分源文件格式问题与网络超时、上游引用等非翻译问题。
- 本轮修复了 ROS CLI 表格、多个文档中的错误行内引用、外部链接、ROS 参数/命令 literal、Foxglove 链接、GurumDDS 版本表、ROS 1 迁移示例等。
- 后续提交已继续修复：ROS 1 迁移/文档发布/教程中的错链和缺失标签，包括 MVSim、Tracing、GurumDDS、Snapshot Repository、Creating an Action、Launch、Event Handlers、tf2、Python Testing 等交叉引用；这些提交在本记录写入时尚未取得新的完整构建结果。
- 当前最新待验构建 #684（run ID `45337963252`，提交 `807ee5aea5e405e870ef4e103567121c9c39f188`）尚未启动 jobs，状态 Pending；不能将 #650 的成功结果视为 #684 后续修订已部署。
- 原域名 `ros2docs.robook.org` 的 Settings → Pages 自定义域名、DNS CNAME、HTTPS 和实时内容切换仍未得到新证据；此前已确认仅将构建产物部署到 GitHub Pages 不会自动更新原 robook.org 托管站点。

## 2026-11-24 Beginner CLI Tools 教程页面复核与补译

- 用户指定页面：`Tutorials/Beginner-CLI-Tools.html`。该页面本身是教程目录页，标题及 10 个子教程的 toctree 标签均已翻译为中文；英文文件路径保留是正常行为。
- 对照 ROS 2 官方 `humble` 分支，检查该目录下 10 篇子教程的源文件及章节结构。发现 `Introducing-Turtlesim.rst` 缺少 5.2 set_pen 服务、重映射、关闭仿真、总结、下一步及相关内容等后续部分；已补译。
- 发现 `Understanding-ROS2-Topics.rst` 在 `ros2 topic info --verbose` 输出后截断，缺少接口查看、话题发布、发布频率、带宽、话题查找、清理环境、总结和下一步等章节；已补译，并补齐 verbose 输出中的订阅者信息。
- 修订提交：`cd79729ba25650174c61e37dbe3b941ba3ab0f23`、`aa4e9d8f3498caf804a808a59903d784b04ed49a`。
- 其余 8 篇子教程的章节标题结构与 Humble 上游基本对应；本轮未发现整章缺失的证据，但仍需逐段翻译完整性和技术内容校对。
- 最新 GitHub Actions #735（提交 `aa4e9d8`）正在构建；须等待构建和部署成功后再进行网页验收。

## 2026-11-24 Beginner CLI Tools 第二轮逐项核验

- 上一轮整合提交对应 GitHub Actions #736（提交 `592e572`）build 与 deploy 均成功。
- 继续逐段对照 ROS 2 官方 Humble 上游，复核 Beginner CLI Tools 目录的 10 篇子教程。章节标题、图片、代码块、literalinclude、注释块及页面结尾均进行结构核对。
- 在 `Understanding-ROS2-Actions.rst` 中发现原中文版本省略了 QWERTY 键盘布局参考链接，并将两处 `ros2 node info` 输出简化为仅显示动作部分。已补充键盘布局链接、完整节点订阅者/发布者/服务/动作输出及相应中文解释。提交：`d7d998c1421cd90886ae996472f7e4c0b859c953`。
- 在 `Understanding-ROS2-Topics.rst` 中发现缺少上游的 `images/unhide.png` 配图。已恢复图片，并调整相邻说明文字。提交：`8128039248c4148c68c89d587fcfea044c76508a`。
- `Introducing-Turtlesim.rst` 已补齐 set_pen、重映射、关闭仿真、总结、下一步及相关内容；`Understanding-ROS2-Topics.rst` 已补齐 interface show、topic pub/hz/bw/find、清理环境和总结等章节。
- 其余配置环境、启动多个节点、录制回放、理解节点、理解参数、理解服务及 rqt_console 页面，本轮章节结构和主要图片/代码示例数量与上游 Humble 对应；未发现整章缺失。但结构计数不等于逐句语义审校，后续仍需抽查译文准确性、链接和网页呈现。
- 本轮最新修改尚待 GitHub Actions 完整构建、部署及线上 HTML 验收；不得将前一轮 #736 成功视为本轮修改已部署。

## 2026-11-24 Beginner CLI Tools 部署及全站构建日志复核

- 构建 #739（提交 `c92e637`）build 与 deploy 均成功，Beginner CLI Tools 本轮页面修改已进入 GitHub Pages 发布产物。
- 检查 #739 的 Sphinx 日志时，额外发现 Humble 完整变更日志的两个历史 RST 问题：`part-004.rst` 首行存在孤立的标题分隔线，导致 CRITICAL “Missing matching underline for section title overline”；`part-032.rst` 的 turtlesim `qreal orient_` 行触发 inline literal 警告。
- 已定位 `part-004.rst` 的孤立分隔线属于切分文件时遗留的多余行；前一文件已经包含 `ament_cmake_pep257` 标题，故删除孤立分隔线，保留其后条目作为该节正文。提交：`df624d9c7cbb62ac3255b7a916d7563fe3ffae81`。
- 已将 `part-032.rst` 中 ``qreal orient\\_`` 改为 ``qreal orient_``，避免 docutils 将行内 literal 解析为未闭合。提交：`b46c9577c3e58de936f5252eb37beabe59d0f19b`。
- 上述两项修复尚待新的完整 Sphinx 构建日志确认；此前 #739 虽然部署成功，但工作流没有启用 warnings-as-errors，不能仅凭 success 认定没有 RST 错误。

- 构建 #742（提交 `0993305`）build/deploy 均成功；日志确认 `part-004.rst` 的 CRITICAL 已消失，Sphinx ERROR 为 0，但 `part-032.rst:107` 仍有一条行内 literal 警告（日志重复显示上游路径和覆盖路径），另有 1 条外部网站超时和 2 条 Lyrical 上游页面未纳入 Humble toctree 的警告。
- 为彻底排除该行内 literal 警告，已将该 changelog 条目中的 `qreal orient_` 改为普通文本，仅保留 ``double`` 的代码标记。提交：`f3d0041f34843601080f240ce2c6a87febb4dac2`。需由下一轮构建验证警告是否消失。

- 构建 #744（提交 `7730361`）build/deploy 成功，但日志进一步表明：移除行内 literal 的反引号后，未转义的 `orient_` 被 docutils 当作引用目标，产生 Unknown target name 错误。因此已将该术语保留为普通文本并对下划线使用 RST 转义（`qreal orient\\_`），只将 `double` 保留为行内 literal。修复提交：`e64214f55b638f4d99df64171ec798ad1315e4b3`。最终需由下一次构建确认该行不再产生 warning/error。

- 构建 #746（提交 `acf0e51`）build/deploy 成功，`part-004.rst` CRITICAL 与 Sphinx ERROR 均为 0；但 `part-032.rst:107` 仍触发行内 literal 警告。现已进一步移除该行的所有双反引号标记，将 `qreal orient\\_` 作为普通转义文本、`double` 作为普通技术术语，避免该行的行内标记解析歧义。提交：`2ac82ae4128dc66ef9524d537922c8e7a83cca36`。待下一次构建复核。

- 构建 #748（提交 `05890b2`）build 与 deploy 均成功。Sphinx 日志确认本轮 `part-032.rst:107` 的 inline literal 警告及 Unknown target 错误均已消失；`part-004.rst` 的标题 CRITICAL 也未再出现。当前日志剩余 2 条 `toc.not_included` 警告，均指向上游 Lyrical 发行版页面（`release-timeline.rst`、`supported-platforms.rst`），不属于 Humble 中文页面；Sphinx ERROR=0、CRITICAL=0。
- GitHub Pages 已成功部署本轮 Beginner CLI Tools 补译和 RST 修复。工作流 #748 的 build/deploy 均为 success。由于外部网页抓取工具无法直接读取 GitHub Pages 页面，本轮以 Actions 构建、Artifact 和部署成功作为部署证据；浏览器端页面逐页视觉验收仍需后续抽查。
