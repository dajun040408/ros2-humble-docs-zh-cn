.. redirect-from::

    Tutorials/Getting-Started-With-Ros2doctor

.. _Ros2Doctor:

使用 ros2doctor 识别问题
========================

**目标：** 使用 ros2doctor 工具识别 ROS 2 环境中的问题。

**教程级别：** 初级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

当 ROS 2 环境未按预期运行时，可以使用 ros2doctor 工具检查配置。

ros2doctor 会检查 ROS 2 的各个方面，包括平台、版本、网络、环境和正在运行的系统等，并针对可能存在的错误和问题原因发出警告。

前置条件
--------

ros2doctor 属于 ros2cli 软件包。只要安装了 ros2cli（常规安装通常都会包含），就可以使用 ros2doctor。

本教程使用 :doc:§turtlesim <../Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim>§ 展示部分示例。

任务
----

1. 检查环境配置
^^^^^^^^^^^^^^^

首先使用 ros2doctor 检查整体 ROS 2 环境。在新终端中 source ROS 2，然后输入：

.. code-block:: console

    $ ros2 doctor
    All <n> checks passed

该命令会检查所有环境模块，并返回警告和错误。如果 ROS 2 环境状态良好，就会看到类似上面的消息。

不过，出现少量警告并不罕见。UserWarning 并不意味着环境无法使用，更可能表示某些配置方式并不理想。

警告通常类似：

.. code-block:: console

    <path>: <line>: UserWarning: <message>

例如，如果使用尚不稳定的 ROS 2 发行版，ros2doctor 可能会发出以下警告：

.. code-block:: console

    UserWarning: Distribution <distro> is not fully supported or tested. To get more consistent features, download a stable version at https://index.ros.org/doc/ros2/Installation/

如果 ros2doctor 只发现警告，仍然会显示 All <n> checks passed。

大多数检查结果都被归类为警告，而不是错误。用户需要根据实际情况判断反馈的重要性。如果发现少见的错误，通常会显示 UserWarning: ERROR:，此时该项检查会被判定为失败。

问题反馈可能类似：

.. code-block:: console

  1/3 checks failed

  Failed modules: network

错误表示系统缺少 ROS 2 正常运行所需的重要设置或功能，应当及时处理。

2. 检查正在运行的系统
^^^^^^^^^^^^^^^^^^^^^

也可以检查正在运行的 ROS 2 系统，以识别可能的问题原因。这里使用 turtlesim，它包含正在相互通信的节点。

在新终端中 source ROS 2 并启动 turtlesim：

.. code-block:: console

    $ ros2 run turtlesim turtlesim_node

打开另一个终端，source ROS 2 并启动键盘控制节点：

.. code-block:: console

    $ ros2 run turtlesim turtle_teleop_key

现在在另一个终端中再次运行 ros2doctor。除了上次检查环境时发现的警告和错误，还可能看到与系统本身有关的新警告：

.. code-block:: console

    $ ros2 doctor
    UserWarning: Publisher without subscriber detected on /turtle1/color_sensor.
    UserWarning: Publisher without subscriber detected on /turtle1/pose.

这说明 /turtlesim 节点在两个没有订阅者的话题上发布数据，ros2doctor 认为这可能导致问题。

如果运行命令订阅 /color_sensor 和 /pose 话题，这些警告就会消失，因为发布者已经有了订阅者。

在 turtlesim 仍运行时，打开两个新终端，分别 source ROS 2 并运行：

.. code-block:: console

    $ ros2 topic echo /turtle1/color_sensor

.. code-block:: console

    $ ros2 topic echo /turtle1/pose

然后再次运行 ros2doctor，publisher without subscriber 警告就会消失。完成后，在运行 echo 的终端中按 Ctrl+C。

现在尝试关闭 turtlesim 窗口或退出 teleop，再次运行 ros2doctor。由于系统中有一个节点不可用，会看到更多关于不同话题 publisher without subscriber 或 subscriber without publisher 的警告。

在包含许多节点的复杂系统中，ros2doctor 对定位通信问题的可能原因非常有帮助。

3. 获取完整报告
^^^^^^^^^^^^^^^

ros2doctor 可以报告网络、系统等方面的警告。使用 --report 参数可以获得更多详细信息，帮助分析问题。

如果网络配置出现警告，并希望准确了解配置中的哪一部分导致警告，或者需要提交 ROS 2 支持请求，都可以使用 --report。你可以将报告中的相关内容复制到支持请求中，帮助他人了解你的环境。

运行以下命令获取完整报告：

.. code-block:: console

    $ ros2 doctor --report

报告包含五个类别：

.. code-block:: console

  NETWORK CONFIGURATION
  ...

  PLATFORM INFORMATION
  ...

  RMW MIDDLEWARE
  ...

  ROS 2 INFORMATION
  ...

  TOPIC LIST
  ...

可以将报告中的信息与 ros2 doctor 输出的警告进行对照。例如，如果 ros2doctor 警告发行版“尚未得到全面支持或测试”，可以查看报告中的 ROS 2 INFORMATION 部分：

.. code-block:: console

  distribution name      : <distro>
  distribution type      : ros2
  distribution status    : prerelease
  release platforms      : {'<platform>': ['<version>']}

这里可以看到 distribution status 为 prerelease，这解释了该发行版为何尚未得到全面支持。

总结
----

ros2doctor 可以报告 ROS 2 环境和正在运行的系统中的问题。使用 --report 参数可以深入查看警告背后的环境信息。

请注意，ros2doctor 不是调试工具，不能帮助定位代码或系统实现层面的错误。

相关内容
--------

§ros2doctor README <https://github.com/ros2/ros2cli/tree/{REPOS_FILE_BRANCH}/ros2doctor>§_ 介绍了更多参数。也可以浏览 ros2doctor 仓库，该仓库对初学者较友好，也是参与贡献的好起点。

下一步
------

你已经完成初级教程！
