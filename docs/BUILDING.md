# 上游源码导入与本地构建

## 1. 上游版本

本项目以 ros2/ros2_documentation 的 humble 分支为技术基线。

~~~bash
git clone --branch humble --single-branch https://github.com/ros2/ros2_documentation.git upstream
~~~

本仓库采用翻译覆盖层方式管理。将本仓库 source/ 中已翻译的 .rst 文件覆盖到上游同名路径即可，不需要把上游图片、模板和扩展复制进翻译仓库。

## 2. Python 环境

建议使用 Ubuntu 22.04/24.04 和 Python 3.12。上游依赖版本以 requirements.txt 和 constraints.txt 为准。

~~~bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r upstream/requirements.txt -c upstream/constraints.txt
~~~

系统还需安装 make、graphviz 等上游构建依赖。

## 3. 准备中文构建目录

在本仓库根目录执行：

~~~bash
python scripts/prepare_build.py --upstream upstream
~~~

脚本会把本仓库 source/ 中的翻译文件覆盖到上游目录，并修改 Sphinx 配置：文档语言设置为 zh_CN，默认发行版固定为 Humble，GitHub 编辑链接指向本翻译仓库。

## 4. 构建 HTML

~~~bash
make -C upstream html JOBS=2
python scripts/build_search_index.py --html-dir upstream/build/html
~~~

生成目录为 upstream/build/html/。

## 5. 中文搜索

构建完成后，运行搜索索引脚本：

~~~bash
python scripts/build_search_index.py --html-dir upstream/build/html
~~~

该脚本从构建后的 HTML 页面生成 `search-index.json`。中文搜索页面为 `search-zh.html`，侧边栏搜索表单会跳转到该页面。

## 6. 本地预览

~~~bash
python3 -m http.server 8000 --directory upstream/build/html
~~~

浏览器访问 http://localhost:8000。

## 7. GitHub Pages 自动部署

仓库中的 .github/workflows/deploy-docs.yml 会在 main 分支有提交时自动执行：

- 检出翻译仓库和上游 Humble 源码。
- 安装上游文档构建依赖。
- 应用中文翻译覆盖层。
- 构建 Sphinx HTML。
- 部署到 GitHub Pages。

首次使用时，需要在 GitHub 仓库 Settings -> Pages 中将 Build and deployment 来源设置为 GitHub Actions。

## 8. 检查

构建时应重点检查 Sphinx warnings、缺失文件、未解析引用、toctree 项目和图片路径。发布前还需对生成的 HTML 执行内部链接与锚点检查。
