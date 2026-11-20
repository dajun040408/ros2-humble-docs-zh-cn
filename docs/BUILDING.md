# 上游源码导入与本地构建

## 1. 上游版本

本项目以 ros2/ros2_documentation 的 humble 分支为基线：

```bash
git clone --branch humble --single-branch https://github.com/ros2/ros2_documentation.git upstream
```

导入时保留上游文件结构、图片、扩展、配置、许可证及版权声明。建议先在独立工作目录中完成上游源码与本项目中文化目录的整合，避免误覆盖翻译成果。

## 2. Python 环境

建议使用 Ubuntu 22.04 / Python 3 环境。具体依赖以导入后的上游 requirements.txt 和 constraints.txt 为准。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt -c constraints.txt
```

系统还需安装 make、graphviz 等上游构建依赖。

## 3. 构建 HTML

在导入完整 Sphinx 源码后执行：

```bash
make html
```

生成目录通常为 build/html/。

## 4. 本地预览

```bash
python3 -m http.server 8000 --directory build/html
```

浏览器访问 http://localhost:8000。

## 5. 实时预览

如果上游 Makefile 提供 serve 目标且已安装 sphinx-autobuild：

```bash
make serve
```

## 6. 检查

构建时应重点检查 Sphinx warnings、缺失文件、未解析引用、toctree 项目和图片路径。发布前还需对生成的 HTML 执行内部链接与锚点检查。

> 当前仓库尚未导入上游完整源码，因此上述构建命令需在源码导入后执行。
