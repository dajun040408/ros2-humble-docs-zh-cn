.. _SnapshotRepository:

从快照软件源安装
================

ROS 主 apt 软件源只保留每个软件包的最新版本，因此一次同步可能会让系统升级到比上次测试版本更新的软件包。本文介绍如何从 ROS apt 软件源的快照安装 ROS，以便准确控制系统何时切换到新的同步版本。

.. note::

   Ubuntu 上只有长期支持（LTS）发行版提供快照。请参阅 :ref:`ROS 发行版列表 <list_of_distributions>`。

.. contents:: 目录
   :depth: 2
   :local:

概述
----

每个活跃发行版都会定期将软件包从 ``ros-testing`` :doc:`apt 软件源 </Installation/Testing>` 同步到 ROS 主 apt 软件源。

同步发生时，主软件源中已更新软件包的旧版本会被删除，因此不再能够安装。此外，尽管维护者和 ROS Boss 会尽力避免回归问题，但同步时构建失败的软件包也会被移除。

如果你的构建或部署依赖于一组特定版本的软件包，这种变化可能会造成干扰。

为了提高整体可复现性，并让用户更好地控制软件包更新，`snapshots.ros.org <http://snapshots.ros.org/>`_ 快照软件源会保存每次同步完成后 ROS 主 apt 软件源的副本。

从快照安装可以获得一组固定的软件包版本，只有在你主动选择其他快照时才会发生变化。

大多数用户应按照 :doc:`安装说明 </Installation/Ubuntu-Install-Debs>` 从主软件源安装。快照软件源适用于将 ROS 软件包打包到容器镜像等制品中，或者希望主动决定何时切换到新同步版本，而不是在下次运行 ``apt upgrade`` 时自动更新的场景。

快照针对 ROS 发行版的 Ubuntu 目标平台和体系结构生成。请参阅 :ref:`二进制软件包构建平台列表 <binary-package-platforms>`。

.. warning::

   快照不会接收缺陷修复或安全更新。请持续关注 ROS 发行版，并定期升级。

使用方法
--------

1. 添加快照软件源密钥
^^^^^^^^^^^^^^^^^^^^^

快照软件源使用独立的签名密钥，该密钥与 ``ros2-apt-source`` 软件包为主软件源安装的密钥不同。

请将密钥下载到单独的 keyring：

.. code-block:: console

   $ sudo mkdir -p /etc/apt/keyrings
   $ curl -fsSL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x4B63CF8FDE49746E98FA01DDAD19BAB3CBF125EA" | sudo gpg --dearmor -o /etc/apt/keyrings/ros-snapshots-archive-keyring.gpg

使用之前，请检查下载的密钥是否正确：

.. code-block:: console

   $ gpg --show-keys --with-fingerprint /etc/apt/keyrings/ros-snapshots-archive-keyring.gpg

确认输出的指纹为：

``4B63 CF8F DE49 746E 98FA 01DD AD19 BAB3 CBF1 25EA`` 。

2. 选择快照
^^^^^^^^^^^

浏览 `snapshots.ros.org <http://snapshots.ros.org/>`_，先选择发行版，再选择希望安装的快照。

快照名称采用其对应同步日期，例如 ``2026-08-07`` 。当某个发行版结束生命周期时，会生成一个名为 ``final`` 的最后快照，可以像使用其他快照一样使用它。

在后续步骤所使用的 Shell 中记录所选发行版和快照，例如 ``humble`` 和 ``2026-08-07`` ：

.. code-block:: console

   $ export ROS_DISTRO=humble
   $ export SNAPSHOT=2026-08-07

3. 将快照软件源添加到 apt
^^^^^^^^^^^^^^^^^^^^^^^^^

创建 apt 软件源文件，指向所选快照：

.. code-block:: bash

   sudo tee /etc/apt/sources.list.d/ros2-snapshots.sources > /dev/null <<EOF
   Types: deb
   URIs: http://snapshots.ros.org/${ROS_DISTRO}/${SNAPSHOT}/ubuntu
   Suites: $(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})
   Components: main
   Signed-By: /etc/apt/keyrings/ros-snapshots-archive-keyring.gpg
   EOF

如果之前已经安装 ROS，请移除 ``ros2-apt-source`` 软件包：

.. code-block:: console

   $ sudo apt remove ros2-apt-source

如果正在切换到较旧的快照，需要将快照软件源的 pin 优先级设置为高于 1000，使 apt 优先使用快照；否则 apt 不会将软件包降级到快照中的旧版本：

.. code-block:: bash

   sudo tee /etc/apt/preferences.d/ros2-snapshots > /dev/null <<EOF
   Package: *
   Pin: origin snapshots.ros.org
   Pin-Priority: 1001
   EOF

然后更新 apt 缓存：

.. code-block:: console

   $ sudo apt update

4. 使用匹配的 rosdistro 索引
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

rosdistro 索引与 apt 软件源分别进行版本管理，因此 ``rosdep`` 可能会根据比当前快照更新的 ``rosdistro`` 状态解析依赖项 key。

rosdistro 中的同步版本使用与快照相同的 ``<distribution>/<date>`` 命名方式打标签。因此，可以按照 :doc:`自定义 rosdistro 索引 </How-To-Guides/Using-Custom-Rosdistro>` 的说明，将索引固定到与快照匹配的标签。

.. code-block:: console

   $ sed -i "s|ros\/rosdistro\/master|ros\/rosdistro\/${ROS_DISTRO}\/${SNAPSHOT}|" /etc/ros/rosdep/sources.list.d/20-default.list
   $ mkdir -p ~/.config/rosdistro
   $ echo "index_url: https://raw.githubusercontent.com/ros/rosdistro/${ROS_DISTRO}/${SNAPSHOT}/index-v4.yaml" > ~/.config/rosdistro/config.yaml
   $ rosdep update

.. note::

   本指南使用 ``~/.config/rosdistro/config.yaml`` 作为更持久的 rosdistro 索引固定配置。不过，环境变量 ``ROSDISTRO_INDEX_URL`` 的优先级高于该配置文件。如果设置了该环境变量，请先取消设置，否则索引不会固定到当前快照。

   可以通过以下命令检查当前使用的索引：

   .. code-block:: console

      $ python3 -c "from rosdistro import get_index_url; print(get_index_url())"

5. 安装 ROS
^^^^^^^^^^^

按照常规方式安装软件包。安装到的版本，就是快照时主软件源中存在的版本：

.. code-block:: console

   $ sudo apt install ros-{DISTRO}-desktop

如果之前已经从主软件源安装 ROS，可以将现有安装切换到快照：

.. code-block:: console

   $ sudo apt dist-upgrade

注意：由于快照可能比主软件源旧，这一操作可能会降级软件包。

返回主软件源
------------

要返回主软件源，请删除快照软件源和 pin 配置：

.. code-block:: console

   $ sudo rm /etc/apt/sources.list.d/ros2-snapshots.sources
   $ sudo rm -f /etc/apt/preferences.d/ros2-snapshots

.. include:: _Apt-Repositories.rst

然后更新 apt 索引并升级：

.. code-block:: console

   $ sudo apt update
   $ sudo apt dist-upgrade

重置 rosdistro 索引：

.. code-block:: console

   $ rm ~/.config/rosdistro/config.yaml
   $ rm /etc/ros/rosdep/sources.list.d/20-default.list
   $ sudo rosdep init
   $ rosdep update

如果要切换到其他快照，请从第 2 步重新开始。

常见问题
--------

**快照多久发布一次？**

通常在每次同步后生成快照，但快照之间的时间间隔并不固定。请浏览 `snapshots.ros.org <http://snapshots.ros.org/>`_，查看某个发行版当前可用的快照。

**快照会保留多久？**

已发布发行版的快照至少会从其同步日期或生命周期结束日期起保留六个月。

**Rolling 是否有快照软件源？**

没有。快照只针对已经正式发布的发行版提供。

**快照软件源与 ros-testing 软件源有什么区别？**

两者的方向正好相反。

``ros-testing`` 软件源保存的是尚未同步到主软件源的软件包，用户可以在发布前进行测试。

快照则保存过去某次同步完成时的软件包状态，以便继续安装已经测试过的版本。请参阅 :doc:`使用预发布二进制软件包进行测试 </Installation/Testing>`。

**可以在生产机器人上使用快照吗？**

快照不会接收缺陷修复或安全更新。如果使用快照，应将切换到更新快照或更新发行版纳入定期维护计划。

请注意，不同快照之间的 ABI 兼容性未经测试，也不作保证。因此，将系统切换到新快照时，建议更新所有 ROS 软件包。

**如何获取 Ubuntu 中 Debian 软件包的快照，例如 ROS 依赖项？**

`Ubuntu 提供自己的快照服务 <https://snapshot.ubuntu.com/>`_。
