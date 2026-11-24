.. redirect-from::

    Working-with-multiple-RMW-implementations
    Guides/Working-with-multiple-RMW-implementations
    Tutorials/Working-with-multiple-RMW-implementations

使用多个 ROS 2 中间件实现
=========================

.. contents:: 目录
   :depth: 2
   :local:

本页面介绍默认 RMW 实现，以及如何指定其他实现。

前置条件
--------

建议先阅读 :doc:`DDS 和 ROS 中间件实现 <../Concepts/Intermediate/About-Different-Middleware-Vendors>`。

指定 RMW 实现
-------------

要使用多个 RMW 实现，必须安装 ROS 2 二进制软件包以及特定 RMW 实现所需的额外依赖项；或者从源码构建 ROS 2，并在工作空间中包含多个 RMW 实现（如果满足编译时依赖项，构建过程默认会包含这些实现）。请参阅 :doc:`安装 RMW 实现 <../Installation/RMW-Implementations>`。

C++ 和 Python 节点都支持环境变量 ``RMW_IMPLEMENTATION``，用户可以通过它选择运行 ROS 2 应用程序时使用的 RMW 实现。

可以将该变量设置为特定实现标识符，例如 ``rmw_cyclonedds_cpp``、``rmw_fastrtps_cpp``、``rmw_connextdds`` 或 ``rmw_gurumdds_cpp``。

例如，使用 Connext RMW 实现运行 C++ talker 和 Python listener 演示：

.. tabs::

  .. group-tab:: Linux

    在一个终端中运行：

    .. code-block:: console

       $ RMW_IMPLEMENTATION=rmw_connextdds ros2 run demo_nodes_cpp talker

    在另一个终端中运行：

    .. code-block:: console

       $ RMW_IMPLEMENTATION=rmw_connextdds ros2 run demo_nodes_py listener

  .. group-tab:: macOS

    在一个终端中运行：

    .. code-block:: console

       $ RMW_IMPLEMENTATION=rmw_connextdds ros2 run demo_nodes_cpp talker

    在另一个终端中运行：

    .. code-block:: console

       $ RMW_IMPLEMENTATION=rmw_connextdds ros2 run demo_nodes_py listener

  .. group-tab:: Windows

    在一个终端中运行：

    .. code-block:: console

       $ set RMW_IMPLEMENTATION=rmw_connextdds
       $ ros2 run demo_nodes_cpp talker

    在另一个终端中运行：

    .. code-block:: console

       $ set RMW_IMPLEMENTATION=rmw_connextdds
       $ ros2 run demo_nodes_py listener

向工作空间添加 RMW 实现
------------------------

可以通过安装必要的依赖项并重新构建工作空间，将额外的 DDS 和 RMW 实现添加到工作空间。有关可用 DDS 选项的安装方法，请参阅 :doc:`RMW 实现 <../Installation/RMW-Implementations>`。

假设你构建 ROS 2 工作空间时只安装了 Fast DDS，因此只构建了 Fast DDS RMW 实现。上次构建工作空间时，其他 RMW 实现软件包（例如 ``rmw_connextdds``）可能无法找到相应 DDS 实现的安装目录。

如果之后又安装了额外的 DDS 实现（例如 Connext），则需要重新触发 Connext RMW 构建期间对 Connext 安装情况的检查。可以在下次构建工作空间时指定 ``--cmake-clean-cache`` 标志。这样，RMW 实现软件包就会针对新安装的 DDS 实现重新构建。

使用 ``--cmake-clean-cache`` 选项为工作空间添加额外 RMW 实现并重新构建时，可能会遇到默认 RMW 实现发生变化而导致构建报错的问题。

要解决此问题，可以通过 ``RMW_IMPLEMENTATION`` CMake 参数，将默认实现设置回之前的值；也可以删除报错软件包的 build 目录，然后使用 ``--packages-start <package name>`` 继续构建。

故障排查
--------

检查当前 RMW
^^^^^^^^^^^^

要检查当前使用的 RMW，只需查看 ``RMW_IMPLEMENTATION`` 环境变量。

在 Linux 系统上，``printenv`` 可以打印完整的环境变量列表。其他操作系统有各自查看环境变量的方法。

如果环境中没有 ``RMW_IMPLEMENTATION``，则可以认为正在使用当前 ROS 发行版的默认实现；否则，当前使用的 RMW 就是该变量列出的值。

各 ROS 发行版的默认 RMW 可在 `REP-2000 <https://reps.openrobotics.org/rep-2000/#platforms-by-distribution>`_ 中查看。

确保使用指定的 RMW 实现
^^^^^^^^^^^^^^^^^^^^^^^^

如果 ``RMW_IMPLEMENTATION`` 环境变量设置为一个尚未安装支持的 RMW 实现，并且系统只安装了一种实现，则可能看到类似以下错误：

.. code-block:: bash

   Expected RMW implementation identifier of 'rmw_connextdds' but instead found 'rmw_fastrtps_cpp', exiting with 102.

如果系统安装了多个 RMW 实现，但请求使用的实现并未安装，则可能看到类似以下错误：

.. code-block:: bash

   Error getting RMW implementation identifier / RMW implementation not installed (expected identifier of 'rmw_connextdds'), exiting with 1.

如果发生这种情况，请确认 ROS 2 安装中确实包含 ``RMW_IMPLEMENTATION`` 环境变量指定的 RMW 实现。

如果希望在不同 RMW 实现之间切换，请确认 ROS 2 daemon 进程没有继续使用之前的 RMW 实现运行，以免节点与 ``ros2 node`` 等命令行工具之间发生问题。

例如，运行：

.. code-block:: bash

   RMW_IMPLEMENTATION=rmw_connextdds ros2 run demo_nodes_cpp talker

然后运行：

.. code-block:: console

   $ ros2 node list

此时可能会启动一个使用 Fast DDS 实现的 daemon：

.. code-block:: bash

   21318 22.0  0.6 535896 55044 pts/8    Sl   16:14   0:00 /usr/bin/python3 /opt/ros/{DISTRO}/bin/_ros2_daemon --rmw-implementation rmw_fastrtps_cpp --ros-domain-id 0

即使随后使用正确的 RMW 实现再次运行命令行工具，daemon 使用的 RMW 实现也不会自动改变，ROS 2 命令行工具仍会失败。

解决方法是停止 daemon 进程：

.. code-block:: console

   $ ros2 daemon stop

然后使用正确的 RMW 实现重新运行 ROS 2 命令行工具。

RTI Connext 在 macOS 上运行失败：共享内存内核设置不足
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果在 macOS 上运行 RTI Connext 时收到类似以下错误：

.. code-block:: console

   [D0062|ENABLE]DDS_DomainParticipantPresentation_reserve_participant_index_entryports:!enable reserve participant index
   [D0062|ENABLE]DDS_DomainParticipant_reserve_participant_index_entryports:Unusable shared memory transport. For a more in-   depth explanation of the possible problem and solution, please visit https://community.rti.com/kb/osx510.

该错误由操作系统允许的共享内存段数量或大小不足导致。因此，``DomainParticipant`` 无法分配足够资源并计算其 participant index，从而引发错误。

可以临时或永久增加计算机的共享内存资源。

要临时增加设置，可以使用 root 用户运行以下命令：

.. code-block:: console

   $ /usr/sbin/sysctl -w kern.sysv.shmmax=419430400
   $ /usr/sbin/sysctl -w kern.sysv.shmmin=1
   $ /usr/sbin/sysctl -w kern.sysv.shmmni=128
   $ /usr/sbin/sysctl -w kern.sysv.shmseg=1024
   $ /usr/sbin/sysctl -w kern.sysv.shmall=262144

要永久增加设置，需要编辑或创建 ``/etc/sysctl.conf`` 文件。创建或编辑该文件需要 root 权限。可以将以下内容添加到现有 ``etc/sysctl.conf`` 文件中，或直接创建 ``/etc/sysctl.conf``：

.. code-block:: bash

   kern.sysv.shmmax=419430400
   kern.sysv.shmmin=1
   kern.sysv.shmmni=128
   kern.sysv.shmseg=1024
   kern.sysv.shmall=262144

修改该文件后，需要重新启动计算机，设置才会生效。

该解决方案根据 RTI Connext 社区论坛内容整理。更详细的说明请参阅 `原始帖子 <https://community.rti.com/kb/osx510>`_。
