补充自定义 rosdep key
=====================

.. contents:: 目录
   :depth: 2
   :local:

概述与动机
----------

如 :doc:§rosdep 教程 <../Intermediate/Rosdep>§ 所述，rosdep 会在 package.xml 文件中查找 rosdep key，并将其映射到当前 ROS 发行版和操作系统需要安装的软件包。

任何人都可以通过§向 rosdistro 贡献规则 <https://github.com/ros/rosdistro/blob/master/CONTRIBUTING.md#rosdep-rules-contributions>§_，请求添加新的 rosdep key。如果依赖项是希望通过 rosdep 安装的 apt 或 pip 软件包，这是首选方式。

但在许多情况下，直接贡献 key 可能比较困难。例如，依赖项不在目标发行版默认的 APT 或 pip 软件源中、属于专有库、只对特定组织有用，或者是自行构建和打包但不希望公开的 ROS 软件包。

也可以 :doc:§fork 整个 rosdistro <../../How-To-Guides/Using-Custom-Rosdistro>§，但如果只是希望在官方 ROS 发行版基础上额外定义几个 rosdep key，这种方式可能过于复杂。本教程介绍如何实现这一目标。

.. warning::

   不要不加区分地使用自定义 rosdep key。它可能导致难以调试的问题，例如二进制不兼容、静默失败、无法解释的崩溃或数据损坏。如果在启用自定义 key 的系统上寻求帮助，请明确说明添加或覆盖了哪些内容。

rosdep 如何获取 rosdep key
--------------------------

rosdep 与 apt 等工具类似，使用 sources list 维护本地索引。源配置保存在 /etc/ros/rosdep/sources.list.d。

首次运行 rosdep init 时，默认只会创建一个源文件：/etc/ros/rosdep/sources.list.d/20-default.list。

查看文件内容：

.. code-block:: console

   $ cat /etc/ros/rosdep/sources.list.d/20-default.list
   ...
   yaml https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/base.yaml
   yaml https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/python.yaml
   ...

这些条目决定 rosdep update 时从哪里获取 rosdep key 及其映射规则。执行更新时，rosdep 会将所有源文件中声明的内容合并到本地缓存索引。安装或查询 rosdep key 时，就会使用该本地索引。

例如，base.yaml 中定义了 libopencv-dev key，因此 rosdep 可以解析它：

.. code-block:: console

   $ rosdep where-defined libopencv-dev
   https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/base.yaml
   $ rosdep resolve libopencv-dev
   #apt
   libopencv-dev

这表示在 Ubuntu 或 Debian 系统上，该 key 会映射到同名 apt 软件包。

在 RHEL 上，该 key 会映射到 DNF 软件包 opencv-devel：

.. code-block:: console

   $ rosdep resolve libopencv-dev --os=rhel:9
   #dnf
   opencv-devel

使用自定义源文件扩展 rosdep
--------------------------

要让 rosdep 识别新的 key，只需添加一个自定义源文件。

下面创建一个简单示例，让 rosdep 从本地 YAML 文件读取规则。使用具有 root 权限的编辑器，将以下内容写入 /etc/ros/rosdep/sources.list.d/30-custom.list：

.. code-block:: yaml

  yaml file:///etc/ros/rosdep/custom_rules.yaml

然后在 /etc/ros/rosdep/custom_rules.yaml 中写入：

.. code-block:: yaml

  awesome_library:
    ubuntu: [awesome_library]
  that_other_library:
    ubuntu:
      pip:
        packages: [another_library]

这定义了两个新的 rosdep 规则：

1. awesome_library：仅对 Ubuntu 定义，映射到同名 apt 软件包。
2. that_other_library：仅对 Ubuntu 定义，映射到名为 another_library 的 pip 软件包。

运行 rosdep update 后，rosdep 会检测新的 30-custom.list，并扫描 custom_rules.yaml。之后即可解析这些 key：

.. code-block:: console

   $ rosdep resolve awesome_library
   #apt
   awesome_library
   $ rosdep resolve that_other_library
   #pip
   another_library

现在只需在 ROS 功能包的 package.xml 中添加：

.. code-block:: xml

   <depend>awesome_library</depend>

rosdep 就会知道如何安装该依赖。

补充说明
--------

* 如果依赖项是托管在第三方 PPA 中的 APT 软件包，可以先添加 PPA。rosdep 会将 key 转换为 apt install 命令，APT 就能够安装该软件包。
* 如果依赖项是托管在第三方索引中的 pip 软件包，可以将索引添加到 pip.conf。
* 源文件不必指向本地文件，也支持 file:// 和 https://。Linux 绝对路径以 / 开头，因此 file URL 通常使用三个斜杠，例如 file:///etc/rosdep/my.file。
* 源文件按字母顺序加载。如果在 30 前缀文件中添加冲突规则，该规则不会生效；如果使用 10 前缀，则会覆盖默认列表（20 前缀）中的规则。使用二进制软件包时，强烈建议不要覆盖依赖声明，否则可能导致难以调试的二进制不兼容。
* 不支持合并 key。例如，不能只为已有 rosdep key 添加 fedora 安装规则。根据加载顺序，该规则可能被忽略，也可能完全覆盖原有 key，从而删除其他所有安装规则。

延伸阅读
--------

* https://docs.ros.org/en/independent/api/rosdep/html/rosdep_yaml_format.html
* https://docs.ros.org/en/independent/api/rosdep/html/contributing_rules.html
