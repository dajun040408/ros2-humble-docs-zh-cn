使用 VS Code 和 Docker 配置 ROS 2
=================================

.. contents:: 目录
   :depth: 2
   :local:

本教程介绍如何使用 Visual Studio Code 和 Docker 容器运行 ROS 2。这样可以在不更换主机操作系统、也不使用虚拟机的情况下，配置 ROS 2 开发环境。

安装 Docker
-----------

在 Ubuntu 上安装 Docker 和相关工具：

.. code-block:: console

   $ sudo apt install docker.io git python3-pip
   $ pip3 install vcstool
   $ echo export PATH=$HOME/.local/bin:$PATH >> ~/.bashrc
   $ source ~/.bashrc
   $ sudo groupadd docker
   $ sudo usermod -aG docker $USER
   $ newgrp docker

运行以下命令验证安装：

.. code-block:: console

   $ docker run hello-world

如果无法运行，可能需要先启动 Docker Daemon：

.. code-block:: console

   $ sudo systemctl start docker

安装 VS Code
------------

安装 VS Code 所需依赖并添加软件源：

.. code-block:: console

   $ sudo apt update
   $ sudo apt install software-properties-common apt-transport-https wget -y
   $ wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
   $ sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
   $ sudo apt install code

在终端输入 ``code`` 即可启动 VS Code。

安装 Remote Development 扩展
----------------------------

在 VS Code 中打开 Extensions（``Ctrl+Shift+X``），搜索并安装 ``Remote Development`` 扩展。

配置 Docker 和 VS Code 工作空间
-------------------------------

创建 ROS 2 工作空间：

.. code-block:: console

   $ cd ~/
   $ mkdir -p ws/src

在工作空间根目录创建 ``.devcontainer`` 文件夹，并在其中创建 ``devcontainer.json`` 和 ``Dockerfile``。目录结构如下：

.. code-block:: text

   ws
   ├── .devcontainer
   │   ├── devcontainer.json
   │   └── Dockerfile
   └── src
       ├── package1
       └── package2

使用 VS Code 的 File → Open Folder 打开 ``ws`` 工作空间。

配置 devcontainer.json
----------------------

Dev Container 应使用正确的主机用户名和权限。配置示例：

.. code-block:: json

   {
     "name": "ROS 2 Development Container",
     "privileged": true,
     "remoteUser": "YOUR_USERNAME",
     "build": {
       "dockerfile": "Dockerfile",
       "args": {
         "USERNAME": "YOUR_USERNAME"
       }
     },
     "workspaceFolder": "/home/ws",
     "workspaceMount": "source=${localWorkspaceFolder},target=/home/ws,type=bind",
     "containerEnv": {
       "DISPLAY": "unix:0",
       "ROS_LOCALHOST_ONLY": "1",
       "ROS_DOMAIN_ID": "42"
     },
     "runArgs": [
       "--net=host",
       "--pid=host",
       "--ipc=host",
       "-e", "DISPLAY=${env:DISPLAY}"
     ]
   }

将 ``YOUR_USERNAME`` 替换为 Linux 用户名。可以在终端运行 ``echo $USER`` 查看当前用户名。

配置 Dockerfile
---------------

Dockerfile 用于选择 ROS 2 基础镜像并创建与主机用户匹配的容器用户。示例开头：

.. code-block:: dockerfile

   FROM ros:ROS_DISTRO
   ARG USERNAME=USERNAME
   ARG USER_UID=1000
   ARG USER_GID=$USER_UID

将 ``ROS_DISTRO`` 替换为所需 ROS 2 发行版名称，并按照开发环境要求创建用户、安装工具和依赖。

启动开发容器
------------

在 VS Code 中打开命令面板，选择 ``Dev Containers: Reopen in Container``。VS Code 会根据 ``devcontainer.json`` 和 Dockerfile 构建容器，并将工作空间挂载到容器中。

容器创建后，可以在 VS Code 集成终端中 source ROS 2 环境、使用 colcon 构建功能包，并使用 ROS 扩展进行代码开发和调试。

总结
----

通过 Docker Dev Container，可以为 ROS 2 项目创建可复现的开发环境，并在 VS Code 中完成构建、编辑和调试。
