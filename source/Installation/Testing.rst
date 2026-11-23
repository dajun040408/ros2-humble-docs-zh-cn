.. redirect-from::

   Installation/Prerelease-Testing

使用预发布二进制软件包进行测试
==============================

许多 ROS 软件包都以预构建二进制文件的形式提供。通常，按照 :doc:§安装说明 <../Installation>§ 操作时，会获得已经正式发布的二进制版本。

此外，还提供一些预发布版本的二进制软件包，可用于正式发布前进行测试。本文介绍尝试使用 ROS 二进制预发布版本的几种方法。

软件包通过 Bloom 发布到 ROS 发行版时，构建农场会将其构建为 deb 软件包，并暂时存储在名为 **building** 的 apt 软件源中。

随着依赖软件包不断重新构建，自动流程会定期将 **building** 中的软件包同步到名为 **ros-testing** 的辅助软件源。

**ros-testing** 是一个测试缓冲区，开发者和希望尝试最新功能的用户可以在软件包被手动同步到公共 ROS 软件源之前进行额外测试。用户通常从公共 ROS 软件源安装软件包。

大约每两周，rosdistro 的发行版管理员会手动将 **ros-testing** 中的内容同步到 ROS **main** 软件源。

deb 测试软件源
--------------

对于基于 Debian 的操作系统，可以从 **ros-testing** 软件源安装二进制软件包。

1. 确保已经通过 deb 软件包安装了可正常工作的 ROS 2（参见 :doc:§安装说明 <../Installation>§）。

2. 安装 §ros2-testing-apt-source§ 软件包。由于同一时间只能启用一个软件源，该操作会自动卸载 §ros2-apt-source§ 软件包。

   .. code-block:: console

      $ sudo apt install -y ros2-testing-apt-source

3. 更新 apt 索引：

   .. code-block:: console

      $ sudo apt update

4. 现在可以从测试软件源安装单个软件包，例如：

   .. code-block:: console

      $ sudo apt install ros-{DISTRO}-my-just-released-package

5. 也可以将整个 ROS 2 安装切换到测试软件源：

   .. code-block:: console

      $ sudo apt dist-upgrade

6. 测试完成后，可以重新安装 §ros2-apt-source§ 软件包，切换回常规软件源：

   .. code-block:: console

      $ sudo apt install -y ros2-apt-source

   然后执行更新和升级：

   .. code-block:: console

      $ sudo apt update
      $ sudo apt dist-upgrade

RHEL 测试软件源
---------------

对于 RHEL，可以通过修改软件源配置启用测试软件源，从 **ros-testing** 安装二进制软件包。

1. 确保已经通过 RPM 软件包安装了可正常工作的 ROS 2（参见 :doc:§RHEL 安装说明 <RHEL-Install-RPMs>§）。

2. 启用测试软件源并禁用主软件源：

   .. code-block:: console

      $ sudo dnf config-manager --set-enabled ros2-testing
      $ sudo dnf config-manager --set-disabled ros2

3. 更新 dnf 索引：

   .. code-block:: console

      $ sudo dnf update

4. 现在可以从测试软件源安装单个软件包，例如：

   .. code-block:: console

      $ sudo dnf install ros-{DISTRO}-my-just-released-package

5. 测试完成后，重新启用主软件源，切换回常规软件源：

   .. code-block:: console

      $ sudo dnf config-manager --set-disabled ros2-testing
      $ sudo dnf config-manager --set-enabled ros2

   然后执行更新和升级：

   .. code-block:: console

      $ sudo dnf update
      $ sudo dnf system-upgrade

二进制归档包
------------

对于核心软件包，我们会针对 Ubuntu Linux、RHEL 和 Windows 运行 nightly 打包任务。这些任务会生成预构建二进制归档包，可以下载并解压到文件系统中。

1. 根据平台的 :doc:§最新开发环境配置 <Alternatives/Latest-Development-Setup>§，确保已经安装所有依赖项。

2. 访问 §https://ci.ros2.org/view/packaging/§，并从列表中选择与你的平台对应的打包任务。

3. 在“Last Successful Artifacts”标题下，可以找到下载链接（例如 Windows 对应 §ros2-package-windows-AMD64.zip§）。

4. 下载归档包，并将其解压到文件系统中。

5. 要使用二进制归档安装，请 source 归档根目录中的 §setup.*§ 文件。

   .. tabs::

     .. group-tab:: Ubuntu Linux 和 RHEL

       .. code-block:: console

          $ source path/to/extracted/archive/setup.bash

     .. group-tab:: Windows

       .. code-block:: console

          $ call path\to\extracted\archive\setup.bat

Docker
------

对于 Ubuntu Linux，还提供基于 nightly 二进制归档包构建的 nightly Docker 镜像。

1. 拉取 Docker 镜像：

   .. code-block:: console

      $ docker pull osrf/ros2:nightly

2. 启动交互式容器：

   .. code-block:: console

      $ docker run -it osrf/ros2:nightly

有关在 Docker 中运行 GUI 应用程序的支持，请参阅 §Docker 用户 GUI 教程 <https://wiki.ros.org/docker/Tutorials/GUI>§_ 或 §rocker 工具 <https://github.com/osrf/rocker>§_。
