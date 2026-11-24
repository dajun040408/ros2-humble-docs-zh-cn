.. redirect-from::

    Deploying-ROS2-on-IBM-Cloud
    Tutorials/Deploying-ROS-2-on-IBM-Cloud

在 IBM Cloud Kubernetes 上部署 ROS 2（社区贡献）
================================================

.. contents:: 目录
   :depth: 3
   :local:

概述
----

本文介绍如何使用 Docker 镜像在 IBM Cloud 上运行 ROS 2。首先介绍 Docker 镜像及其本地运行方式，然后说明 IBM Cloud 容器部署流程，并介绍如何将 GitHub 上的自定义 ROS 2 功能包加入镜像。最后创建 Kubernetes 集群，并将 Docker 镜像部署到集群中。

原始项目和文章：

* `ros2_ibmcloud 示例仓库 <https://github.com/mm-nasr/ros2_ibmcloud>`_
* `IBM Cloud 上运行 ROS 2 的文章 <https://medium.com/@mahmoud-nasr/running-ros2-on-ibm-cloud-1b1284cbd487>`_

ROS 2 与 IBM Cloud
------------------

本教程展示如何在 IBM Cloud 上集成和运行 ROS 2，以及如何部署自定义功能包。

ROS 2 是新一代机器人操作系统，为多机器人编队提供了更灵活的控制能力。随着云计算发展，云机器人应用日益重要。通过 Docker 文件，可以构建包含 ROS 2 和自定义功能包的镜像，并将其部署到云端。

本教程原始命令基于 Linux，并在 Ubuntu 18.04 上测试。

1. 准备系统
^^^^^^^^^^^

开始部署之前，需要安装 Docker 和 IBM Cloud 相关工具。Docker 容器能够将不同项目隔离运行，避免项目依赖影响主机系统。容器镜像包含运行应用所需的依赖，便于在不同环境间传递和部署。

2. 构建 ROS 2 Docker 镜像
^^^^^^^^^^^^^^^^^^^^^^^^^

创建 Dockerfile，选择合适的 ROS 2 基础镜像，并在镜像中安装项目依赖。若项目包含自定义功能包，可以通过 Git 克隆仓库，将功能包加入工作空间，然后使用 colcon 构建。

构建镜像：

.. code-block:: console

   $ docker build -t ros2-application .

在本地运行容器，确认 ROS 2 节点和自定义功能包正常工作后，再推送镜像到容器镜像仓库。

3. 配置 IBM Cloud
^^^^^^^^^^^^^^^^^

登录 IBM Cloud，创建 Kubernetes 集群，并配置本地 kubectl 工具，使其能够访问集群。将构建好的 Docker 镜像推送到 IBM Cloud Container Registry。

4. 部署到 Kubernetes
^^^^^^^^^^^^^^^^^^^^

创建 Kubernetes Deployment，指定镜像地址、容器启动命令和所需环境变量。对于需要 ROS 2 节点互相发现的应用，应根据网络拓扑配置 DDS 发现方式、端口和 ROS_DOMAIN_ID。

通过 kubectl 将 Deployment 应用到集群，并使用日志和 Pod 状态检查部署结果。

总结
----

本教程展示了使用 Docker 构建 ROS 2 应用镜像，并通过 IBM Cloud Kubernetes 部署容器的基本流程。实际生产部署还需要根据 ROS 2 通信方式配置网络、发现机制、存储和安全策略。
