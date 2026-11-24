.. redirect-from::

    Tutorials/Ros2bag/Recording-And-Playing-Back-Data

.. _ROS2Bag:

录制和回放数据
==============

**目标：** 录制话题上发布的数据，以便随时回放和检查。

**教程级别：** 初级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

ros2 bag 是一个命令行工具，用于录制系统中话题发布的数据。它会累积一个或多个话题上的数据，并将其保存到数据库中。之后可以回放数据，重现测试和实验结果。录制话题也是分享工作、帮助其他人复现实验的好方法。

前置条件
--------

ros2 bag 通常已经包含在 ROS 2 安装环境中。

如果需要安装 ROS 2，请参阅 :doc:`安装说明 <../../../Installation>`。

本教程会使用前面教程介绍过的节点和话题概念，也会使用 turtlesim 软件包。每次打开新终端时，都不要忘记 source ROS 2 环境。

任务
----

1. 准备工作
^^^^^^^^^^^

本教程将录制 turtlesim 系统中的键盘输入，以便之后保存和回放。因此，先启动 /turtlesim 和 /teleop_turtle 节点。

打开一个新终端并运行：

.. code-block:: console

    $ ros2 run turtlesim turtlesim_node

打开另一个终端并运行：

.. code-block:: console

    $ ros2 run turtlesim turtle_teleop_key

再创建一个目录保存录制文件：

.. tabs::

    .. group-tab:: Linux

        .. code-block:: console

            $ mkdir bag_files
            $ cd bag_files

    .. group-tab:: macOS

        .. code-block:: console

            $ mkdir bag_files
            $ cd bag_files

    .. group-tab:: Windows

        .. code-block:: console

            $ md bag_files
            $ cd bag_files

2. 选择话题
^^^^^^^^^^^

ros2 bag 只能录制话题中发布的消息。打开一个新终端，运行以下命令查看系统中的话题：

.. code-block:: console

  $ ros2 topic list
  /parameter_events
  /rosout
  /turtle1/cmd_vel
  /turtle1/color_sensor
  /turtle1/pose

在话题教程中，你已经了解到 /turtle_teleop 节点会在 /turtle1/cmd_vel 话题上发布命令，从而控制 turtlesim 中的乌龟移动。

要查看 /turtle1/cmd_vel 发布的数据，运行：

.. code-block:: console

    $ ros2 topic echo /turtle1/cmd_vel

最初不会显示任何内容，因为 teleop 尚未发布数据。回到运行 teleop 的终端并将其设为活动窗口，使用方向键移动乌龟。此时运行 ros2 topic echo 的终端就会显示发布的数据。

.. code-block:: console

  linear:
    x: 2.0
    y: 0.0
    z: 0.0
  angular:
    x: 0.0
    y: 0.0
    z: 0.0
    ---

3. ros2 bag record
^^^^^^^^^^^^^^^^^^

3.1 录制单个话题
~~~~~~~~~~~~~~~~

使用以下命令语法录制话题数据：

.. code-block:: console

    $ ros2 bag record <topic_name>

运行命令之前，先在新终端中进入之前创建的 bag_files 目录，因为 rosbag 文件会保存在运行命令时所在的目录。

运行：

.. code-block:: console

    $ ros2 bag record /turtle1/cmd_vel
    [INFO] [rosbag2_storage]: Opened database 'rosbag2_2019_10_11-05_18_45'.
    [INFO] [rosbag2_transport]: Listening for topics...
    [INFO] [rosbag2_transport]: Subscribed to topic '/turtle1/cmd_vel'
    [INFO] [rosbag2_transport]: All requested topics are subscribed. Stopping discovery...

现在 ros2 bag 正在录制 /turtle1/cmd_vel 话题发布的数据。回到 teleop 终端，再次移动乌龟。移动轨迹没有特定要求，但建议画出容易识别的图案，以便之后回放时观察。

.. image:: images/record.png

按 Ctrl+C 停止录制。

数据会累积到一个新 bag 目录中，目录名称格式为 rosbag2_年_月_日-时_分_秒。该目录包含 metadata.yaml 文件，以及采用录制格式保存的 bag 文件。

3.2 录制多个话题
~~~~~~~~~~~~~~~~

也可以同时录制多个话题，并修改 ros2 bag 保存的文件名称。

运行以下命令：

.. code-block:: console

  $ ros2 bag record -o subset /turtle1/cmd_vel /turtle1/pose
  [INFO] [rosbag2_storage]: Opened database 'subset'.
  [INFO] [rosbag2_transport]: Listening for topics...
  [INFO] [rosbag2_transport]: Subscribed to topic '/turtle1/cmd_vel'
  [INFO] [rosbag2_transport]: Subscribed to topic '/turtle1/pose'
  [INFO] [rosbag2_transport]: All requested topics are subscribed. Stopping discovery...

-o 选项允许为 bag 文件指定唯一名称，本例中名称为 subset。

要同时录制多个话题，只需用空格分隔列出每个话题。上面的输出确认两个话题都已开始录制。

移动乌龟，并在完成后按 Ctrl+C。

.. note::

    还可以使用 -a 选项录制系统中的所有话题。

4. ros2 bag info
^^^^^^^^^^^^^^^^

运行以下命令查看录制文件的详细信息：

.. code-block:: console

    $ ros2 bag info <bag_file_name>

对 subset 文件运行该命令，会返回文件信息：

.. code-block:: console

    $ ros2 bag info subset
    Files:             subset.db3
    Bag size:          228.5 KiB
    Storage id:        sqlite3
    Duration:          48.47s
    Start:             Oct 11 2019 06:09:09.12 (1570799349.12)
    End                Oct 11 2019 06:09:57.60 (1570799397.60)
    Messages:          3013
    Topic information: Topic: /turtle1/cmd_vel | Type: geometry_msgs/msg/Twist | Count: 9 | Serialization Format: cdr
                       Topic: /turtle1/pose | Type: turtlesim/msg/Pose | Count: 3004 | Serialization Format: cdr

5. ros2 bag play
^^^^^^^^^^^^^^^^

回放 bag 文件之前，在运行 teleop 的终端中按 Ctrl+C 停止键盘控制。然后确保 turtlesim 窗口可见，以便观察回放过程。

输入：

.. code-block:: console

    $ ros2 bag play subset
    [INFO] [rosbag2_storage]: Opened database 'subset'.

乌龟会沿着录制时输入的路径移动（但不一定完全一致，因为 turtlesim 对系统时序中的微小变化比较敏感）。

.. image:: images/playback.png

由于 subset 文件录制了 /turtle1/pose 话题，只要 turtlesim 仍在运行，ros2 bag play 就不会退出，即使你没有移动乌龟也是如此。

这是因为只要 /turtlesim 节点处于活动状态，它就会定期在 /turtle1/pose 话题上发布数据。前面的 ros2 bag info 输出中，/turtle1/cmd_vel 的 Count 只有 9，表示录制时按下方向键发布命令的次数为 9。

而 /turtle1/pose 的 Count 超过 3000，说明录制期间该话题发布了 3000 多条数据。

要了解位置数据的发布频率，可以运行：

.. code-block:: console

    $ ros2 topic hz /turtle1/pose

总结
----

可以使用 ros2 bag 命令录制 ROS 2 系统中通过话题传递的数据。无论是与他人分享工作，还是检查自己的实验结果，这都是一个非常实用的工具。

下一步
------

你已经完成“初级：CLI 工具”系列教程！下一步可以学习“初级：客户端库”系列教程，从 :doc:`创建工作空间 <../../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace>` 开始。

相关内容
--------

有关 ros2 bag 的更完整说明，请参阅`rosbag2 README <https://github.com/ros2/rosbag2>`_。有关 QoS 兼容性和 ros2 bag 的更多信息，请参阅 :doc:`录制和回放时覆盖 QoS 策略 <../../../How-To-Guides/Overriding-QoS-Policies-For-Recording-And-Playback>`。
