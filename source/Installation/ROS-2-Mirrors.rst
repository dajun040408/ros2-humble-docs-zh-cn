ROS 2 软件源镜像
=================

.. contents:: 目录
   :depth: 3

文档镜像
--------

ROS 文档镜像可在`主站 <http://docs.ros.org>`_ 无法访问时作为备用站点，也可能为地理位置更接近镜像站点的用户提供更快的访问速度。

Debian/Ubuntu（APT）软件源镜像
------------------------------

要使用这些镜像，请在 APT 配置中用下表列出的地址替换官方 ROS 软件源 URL。

亚洲
^^^^

.. list-table::
   :widths: 30 20 50

   * - 清华大学（TUNA）
     - 中国
     - `镜像地址 <https://mirrors.tuna.tsinghua.edu.cn/ros2/ubuntu/>`__
   * - 中国科学技术大学（USTC）
     - 中国
     - `镜像地址 <https://mirrors.ustc.edu.cn/ros2/ubuntu/>`__
   * - 阿里云（Aliyun）
     - 中国
     - `镜像地址 <https://mirrors.aliyun.com/ros2/ubuntu/>`__
   * - 齐鲁工业大学（QLU）
     - 中国
     - `镜像地址 <https://mirrors.qlu.edu.cn/ros2/ubuntu/>`__
   * - 重庆大学（CQU）
     - 中国
     - `镜像地址 <https://mirrors.cqu.edu.cn/ros2/ubuntu/>`__

欧洲
^^^^

.. list-table::
   :widths: 30 20 50

   * - 代尔夫特理工大学
     - 荷兰
     - `镜像地址 <http://ftp.tudelft.nl/ros2/ubuntu/>`__

北美洲
^^^^^^

.. list-table::
   :widths: 30 20 50

   * - 马里兰大学（UMD）
     - 美国
     - `镜像地址 <http://mirror.umd.edu/packages.ros.org/ros2/ubuntu/>`__
   * - nulled LLC
     - 美国
     - `镜像地址 <http://mirror.nulled.llc/ros2/ubuntu/>`__

大洋洲
^^^^^^

.. list-table::
   :widths: 30 20 50

   * - AARNet
     - 澳大利亚
     - `镜像地址 <https://mirror.aarnet.edu.au/pub/ros2-packages/ubuntu/>`__

南美洲和非洲
^^^^^^^^^^^^

目前，这些地区尚无经过官方验证的 ROS 2 镜像。如果你在南美洲或非洲托管镜像，并希望将其列入此列表，请参阅下文“托管镜像”部分。

创建镜像
--------

如果你正在维护镜像，请加入 discourse.openrobotics.org 上的 Mirrors 分类：`镜像地址 <https://discourse.openrobotics.org/c/infrastructure-project/infra-mirrors/>`__，以便获取反馈和及时更新。

使用镜像
^^^^^^^^

要使用镜像，请在 `ros2-latest.list` 文件中将 `packages.ros.org` 替换为镜像 URL：

.. code-block:: bash

   # TUNA 镜像示例
   sudo sed -i 's|http://packages.ros.org/ros2/ubuntu|https://mirrors.tuna.tsinghua.edu.cn/ros2/ubuntu|g' /etc/apt/sources.list.d/ros2-latest.list
   sudo apt update

设置镜像
--------

ROS 基础设施使用 `rsync` 分发软件包。要创建 ROS 2 软件源的本地镜像：

1. **存储空间要求：** 确保至少有 500 GB 可用磁盘空间。
2. **同步命令：** 使用 `rsync` 从官方 OSUOSL 端点拉取数据：

.. code-block:: bash

   # 同步 ROS 2 主软件源
   rsync -azv rsync.osuosl.org::ros2-main /your/local/path --delete

3. **维护：** 设置 `cron` 任务，每 6–12 小时同步一次。

将镜像添加到此列表
^^^^^^^^^^^^^^^^^^

要正式列入此列表，你的镜像必须满足以下要求：

* 支持 **HTTPS**。
* 至少每 24 小时同步一次。
* 提供用于基础设施告警的联系邮箱。

验证通过后，请针对本页面提交 Pull Request，或在 `Mirrors Discourse <https://discourse.openrobotics.org/c/infrastructure-project/infra-mirrors/>`_ 中发帖。

镜像 docs.ros.org
-----------------

镜像文档网站需要进行特定配置，以避免搜索引擎索引分散。如果你有兴趣托管区域性文档镜像，请在开始之前通过 Discourse **联系基础设施团队**。
