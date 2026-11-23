.. redirect-from::

    Tutorials/Run-2-nodes-in-a-single-docker-container
    Tutorials/Run-2-nodes-in-two-separate-docker-containers
    Guides/Run-2-nodes-in-two-separate-docker-containers

在 Docker 中运行 ROS 2 节点（社区贡献）
=======================================

在单个 Docker 容器中运行两个节点
--------------------------------

拉取标签为 `{DISTRO}-desktop` 的 ROS Docker 镜像：

.. code-block:: console

   $ docker pull osrf/ros:{DISTRO}-desktop

以交互模式在容器中运行镜像：

.. code-block:: console

   $ docker run -it osrf/ros:{DISTRO}-desktop

此时可以使用 `ros2` 命令行帮助查看可用命令：

.. code-block:: console

   $ ros2 --help

例如，列出所有已安装的功能包：

.. code-block:: console

   $ ros2 pkg list
   （此处将显示功能包列表）

例如，列出所有可执行程序：

.. code-block:: console

   $ ros2 pkg executables
   （此处将显示 <package> <executable> 列表）

在该容器中运行 `demo_nodes_cpp` 软件包中的两个 C++ 节点：一个话题订阅者 `listener` 和一个话题发布者 `talker`：

.. code-block:: console

   $ ros2 run demo_nodes_cpp listener &
   $ ros2 run demo_nodes_cpp talker

在两个独立的 Docker 容器中运行两个节点
--------------------------------------

打开一个终端。以交互模式运行镜像，并使用 `ros2 run` 启动话题发布者（`demo_nodes_cpp` 软件包中的 `talker` 可执行程序）：

.. code-block:: console

   $ docker run -it --rm osrf/ros:{DISTRO}-desktop ros2 run demo_nodes_cpp talker

再打开第二个终端。以交互模式运行镜像，并使用 `ros2 run` 启动话题订阅者（`demo_nodes_cpp` 软件包中的 `listener` 可执行程序）：

.. code-block:: console

   $ docker run -it --rm osrf/ros:{DISTRO}-desktop ros2 run demo_nodes_cpp listener

除了直接使用命令行，也可以创建 `docker-compose.yml` 文件（此处使用版本 2），内容如下：

.. code-block:: yaml

   version: '2'

   services:
     talker:
       image: osrf/ros:{DISTRO}-desktop
       command: ros2 run demo_nodes_cpp talker
     listener:
       image: osrf/ros:{DISTRO}-desktop
       command: ros2 run demo_nodes_cpp listener
       depends_on:
         - talker

在该文件所在目录中运行 `docker compose up` 启动容器。按 `Ctrl+C` 可以关闭容器。
