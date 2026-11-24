.. redirect-from::

    Quality-of-Service
    Tutorials/Quality-of-Service

在有损网络中使用 QoS 设置
=========================

.. contents:: 目录
   :depth: 2
   :local:

背景
----

有关 ROS 2 可用 QoS 支持的背景信息，请参阅 :doc:`QoS 设置概念页面 <../../Concepts/Intermediate/About-Quality-of-Service-Settings>`。

本演示将启动一个发布摄像头图像的节点，以及一个订阅图像并显示在屏幕上的节点。随后模拟两者之间的有损网络连接，展示不同 QoS 设置如何处理网络质量下降的问题。

前置条件
--------

本教程假设你已经安装 ROS 2 和 OpenCV。还需要 image_tools 软件包。

.. tabs::

   .. group-tab:: Linux 二进制软件包

      .. code-block:: console

        $ sudo apt-get install ros-{DISTRO}-image-tools

   .. group-tab:: 从源码安装

      克隆并构建与当前安装版本匹配分支的 demos 仓库：

      .. code-block:: console

        $ git clone https://github.com/ros2/demos.git -b {REPOS_FILE_BRANCH}

运行演示
--------

确保计算机连接了可用摄像头。

source ROS 2 设置文件：

.. code-block:: console

   $ . <ROS 2 安装目录>/setup.bash

然后运行：

.. code-block:: console

   $ ros2 run image_tools showimage

此时不会发生任何事情。showimage 是一个订阅者节点，正在等待 image 话题上的发布者。

注意：之后需要在终端中按 Ctrl+C 关闭 showimage 进程，不能只关闭窗口。

在另一个终端中 source 设置文件并运行发布者：

.. code-block:: console

   $ ros2 run image_tools cam2image
   Publishing image #1
   Publishing image #2
   Publishing image #3

该节点会发布摄像头图像。如果计算机没有连接摄像头，也可以使用命令行选项发布预定义图像。

此时会弹出标题为 view 的窗口，显示摄像头画面。第一个窗口中的订阅者终端会输出收到图像的相关信息。

模拟有损网络
------------

为了模拟网络质量下降，可以使用 Linux 的 tc 工具在网络接口上添加延迟、丢包和抖动。网络条件发生变化后，可以观察图像订阅者是否出现延迟、丢帧或数据中断。

QoS 策略对比
------------

ROS 2 QoS 配置文件会影响消息传递行为：

* Reliable：尽可能确保消息送达，但在网络质量较差时可能增加延迟。
* Best Effort：不保证每条消息送达，但可以减少重传造成的延迟。
* Keep Last：只保留最近指定深度的消息。
* Keep All：保留所有消息，直到资源限制生效。

对于实时摄像头流，Best Effort 通常更适合避免接收过期图像；对于不能丢失的数据，则可能更适合 Reliable。

总结
----

本演示展示了如何在有损网络环境中比较不同 QoS 配置。应根据数据类型、实时性要求和可靠性需求选择合适的 QoS 策略。
