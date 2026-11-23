安全部署指南
============

**目标：** 了解如何将安全制品部署到生产系统中的最佳实践。

**教程级别：** 高级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

典型部署场景通常涉及将容器化应用程序或软件包交付到远程系统。部署启用了安全机制的应用程序时，需要特别关注打包文件的敏感程度。

sros2 软件包遵循 DDS Security 标准，为 ROS 2 环境提供一组高度模块化、灵活的安全管理工具。

合理组织证书、密钥和目录，是避免系统安全受到破坏的关键。这包括识别敏感信息，并确定部署到远程生产系统所需的最小文件集合，以降低安全暴露面。

前置条件
--------

* 安装 Docker，并启用 Compose 插件。请参阅 Docker 安装说明：https://docs.docker.com/engine/install/ 和 Compose 插件：https://docs.docker.com/compose/install。
* （推荐）了解 ROS 2 安全设计：https://design.ros2.org/articles/ros2_dds_security.html。
* （推荐）完成此前的安全教程，特别是配置 ROS 2 安全机制、理解安全密钥库和设置访问控制。

通用指南
--------

ROS 2 使用 DDS Security 扩展保护同一个 enclave 内节点之间的消息通信。enclave 中的不同签名文件和证书由受信任实体 Certificate Authority（CA）的私钥和证书生成。

每个 enclave 可以分别选择两个不同的 CA，分别用于身份和权限验证。这些 CA 制品存储在密钥库（Keystore）的 private/ 和 public/ 子目录中，目录结构如下：

.. code-block:: text

  keystore
  ├── enclaves
  │   └── ...
  ├── private
  │   └── ...
  └── public
      └── ...

在典型生产系统部署中，创建和使用 CA 的推荐实践如下：

#. 在组织内部专用的系统中创建 CA。
#. 生成或修改所需的 enclaves，并注意：
   * 不应将生成的所有 enclaves 都部署到所有目标设备。
   * 一种合理的方式是每个应用程序使用一个 enclave，以实现职责分离。
#. 在远程生产设备初始化期间，将 public/ 目录及对应的 enclaves/ 一同部署到设备。
#. 在组织内部保存并保护 private/ 密钥和/或证书请求文件。

如果 private/ 文件丢失，就无法再修改访问权限，也无法添加或修改安全配置文件。

此外，还可以考虑以下实践：

* 为 enclaves/ 目录内容设置只读权限。
* 如果生成 enclave 私钥时提供了符合 PKCS#11 标准的 URI，可以使用硬件安全模块（HSM）保存私钥：https://en.wikipedia.org/wiki/Hardware_security_module。

.. list-table::
   :header-rows: 1

   * - 目录
     - 组织内部
     - 目标设备
     - 材料敏感程度
   * - public
     - ✓
     - ✓
     - 低
   * - private
     - ✓
     - ✕
     - 高
   * - enclaves
     - ✓
     - ✓
     - 中

构建部署场景
------------

为了展示一个简单的部署场景，本教程将在 ros:<DISTRO> 镜像基础上构建新的 Docker 镜像。随后创建三个容器，用于在本地主机的共享卷中初始化密钥库，并模拟两个通过安全方式相互通信的远程设备。

本例中，本地主机代表组织内部系统。首先创建工作目录：

.. code-block:: console

  $ mkdir ~/security_gd_tutorial
  $ cd ~/security_gd_tutorial

生成 Docker 镜像
^^^^^^^^^^^^^^^^

构建新 Docker 镜像需要 Dockerfile。运行以下命令下载本教程提供的 Dockerfile：

.. code-block:: console

  $ wget https://raw.githubusercontent.com/ros2/ros2_documentation/{DISTRO}/source/Tutorials/Advanced/Security/resources/deployment_gd/Dockerfile

然后构建 Docker 镜像：

.. code-block:: console

  $ docker build -t ros2_security/deployment_tutorial --build-arg ROS_DISTRO={DISTRO} .

理解 compose 文件
^^^^^^^^^^^^^^^^^

Compose 配置文件使用镜像创建容器服务。本教程在配置中定义了三个服务：

* **keystore-creator：** 在容器内部初始化新的密钥库目录树，创建 enclaves/、public/ 和 private/。密钥库目录会配置为容器间共享卷。
* **listener** 和 **talker：** 模拟远程设备。它们会加载所需的 Security 环境变量，以及共享卷中的必要密钥库文件。

通过以下命令下载 Compose YAML 配置文件：

.. code-block:: console

  $ wget https://raw.githubusercontent.com/ros2/ros2_documentation/{DISTRO}/source/Tutorials/Advanced/Security/resources/deployment_gd/compose.deployment.yaml

运行示例
--------

在同一工作目录 ~/security_gd_tutorial 中，运行：

.. code-block:: console

  $ docker compose -f compose.deployment.yaml up

预期输出包括 listener 找到对应的 security directory，以及 talker 和 listener 之间持续交换 Hello World 消息。

检查容器
^^^^^^^^

保持容器运行，打开两个不同终端并分别进入两个容器。

第一个终端：

.. code-block:: console

  $ docker exec -it tutorial-listener-1 bash
  $ cd keystore
  $ tree

第二个终端：

.. code-block:: console

  $ docker exec -it tutorial-talker-1 bash
  $ cd keystore
  $ tree

两个容器中都会包含各自应用所需的 enclave 文件和 public 证书。需要注意：

* private/ 目录没有被复制，仍然保留在本地主机（组织内部）。
* 每个部署设备只包含其应用程序所需的最小 enclave 集合。

.. note::

  为了简化示例，同一个 CA 同时用于该 enclave 的身份和权限验证。
