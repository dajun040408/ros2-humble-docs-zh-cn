.. redirect-from::

   Concepts/About-Tf2

TF2 坐标变换库
================

.. contents:: 目录
   :local:

概述
------

tf2 是一个坐标变换库，允许用户跟踪多个坐标系随时间发生的变化。tf2 以带时间缓存的树形结构维护各坐标系之间的关系，并允许用户在指定时间点，将点、向量等数据从任意一个坐标系转换到另一个坐标系。

.. image:: ../images/ros2_tf2_frames.png

TF2 的特性
------------

机器人系统通常包含许多随时间变化的三维坐标系，例如世界坐标系、底盘坐标系、夹爪坐标系、头部坐标系等。tf2 会持续跟踪这些坐标系，并允许用户查询以下问题：

* 5 秒前，头部坐标系相对于世界坐标系位于什么位置？
* 夹爪中物体相对于底盘坐标系的位姿是什么？
* 当前底盘坐标系在地图坐标系中的位姿是什么？

tf2 可以在分布式系统中运行。这意味着机器人各坐标系的全部信息都可以被系统中任意计算机上的 ROS 2 组件访问。tf2 可以让分布式系统中的每个组件分别构建自己的坐标变换信息数据库，也可以使用一个中心节点收集并存储所有坐标变换信息。

.. mermaid::

   flowchart LR
      E((Earth))
      E --> A[[Car A]]
      E --> B[[Car B]]
      E --> C{{Satellite C}}
      E --> D((Moon D))

发布坐标变换
^^^^^^^^^^^^^^

发布坐标变换时，我们通常会将其理解为从一个坐标系到另一个坐标系的变换。这里需要区分两种语义：变换以某个坐标系表示的数据，或变换坐标系本身。这两种表示的数值互为逆变换。

通过 ``geometry_msgs/msg/Transform`` 消息发布的变换采用坐标系本身的表示方式。调试已发布的变换时，请记住：根据你沿坐标变换树查询的方向，发布的变换与查找到的变换可能互为逆变换。

.. math::

   _{B}T^{data}_{A} = (_{B}T^{frame}_{A})^{-1}

TF 库会根据你沿坐标变换树遍历的方向，自动为这些元素执行求逆操作。在本文档后续部分，我们统一使用 :math:`T^{data}`` 表示变换，并省略上标中的 ``data``。

位置
^^^^^^

假设汽车 :math:`A` 上的驾驶员观测到某个物体，地面上的人员希望知道该物体相对于自身的位置。此时，需要将观测结果从源坐标系转换到目标坐标系。

.. math::

   _{E}T_{A} * P_{A}^{Obs} = P_{E}^{Obs}

如果汽车 B 上的人员也想知道该物体的位置，则可以计算组合变换：

.. math::

   _{B}T_{E} * _{E}T_{A} * P_{A}^{Obs} = _{B}T_{A} * P_{A}^{Obs} = P_{B}^{Obs}

这正是 ``lookupTransform`` 提供的功能，其中 ``A`` 是*源坐标系* ``frame_id``，``B`` 是*目标坐标系* ``frame_id``。

如果条件允许，建议优先使用 `transform<T>(target_frame, ...)`` 方法，因为该方法会从数据类型中读取*源坐标系* ``frame_id``，并将*目标坐标系* ``frame_id`` 写入转换后的数据类型，具体数学运算由内部自动完成。

如果 ``P`` 是一个 ``Stamped`` 数据类型，那么 ``A`` 表示它的 ``frame_id``。

例如，如果根坐标系 A 位于坐标系 B 下方一米，那么从 A 到 B 的变换值为正。

但如果要将数据从坐标系 B 转换到坐标系 A，则必须使用该值的逆变换。可以这样理解：切换到较低的参考坐标系时，高度值会增加。相反，如果将数据从坐标系 A 转换到坐标系 B，由于新的参考坐标系更高，高度值会减小。

.. math::

   _{B}T_{A} = (_{B}{Tf}_{A})^{-1}

速度
^^^^^^

表示 ``Velocity`` 时，需要三个部分的信息：

:math:`V^{moving\_frame - reference\_frame}_{observing\_frame}`

该速度表示运动坐标系相对于参考坐标系的速度，并且使用观测坐标系表示。

例如，汽车 A 的驾驶员可以报告汽车正在向前行驶（在 A 坐标系中观测），速度为 1 m/s（相对于地球）。此时可表示为：:math:`V_{A}^{A - E} = (1,0,0)`。

同一个速度也可以从地球坐标系的视角进行观测（假设汽车向东行驶，地球坐标系采用 NED，即北-东-地坐标约定），此时表示为：:math:`V_{E}^{A - E} = (0, 1, 0)`。

坐标变换可以说明这两种表示实际上描述的是同一个速度：

.. math::

   _{E}T_{A} * V_{A}^{A - E} = V_{E}^{A - E}

如果多个速度都使用同一个观测坐标系（此处为 ``Obs``）表示，则可以进行相加或相减：

.. math::

   V_{Obs}^{A - C} = V_{Obs}^{A - B} + V_{Obs}^{D - C}

通过取反可以“反转”速度：

.. math::

   V_{Obs}^{A - C} = -(V_{Obs}^{C - A})

如果要比较两个速度，必须先将它们转换到相同的观测坐标系中。

教程
------

我们提供了一组 :doc:`tf2 教程 <../../Tutorials/Intermediate/Tf2/Tf2-Main>``，通过循序渐进的方式介绍 tf2 的使用方法。你可以从 :doc:`tf2 简介 <../../Tutorials/Intermediate/Tf2/Introduction-To-Tf2>`` 开始学习。完整的 tf2 及相关教程列表请参阅 :doc:`教程页面 <../../Tutorials/Intermediate/Tf2/Tf2-Main>`。

用户使用 tf2 主要有两项任务：监听坐标变换和广播坐标变换。

如果希望使用 tf2 在坐标系之间进行变换，节点需要监听坐标变换。节点会接收并缓存系统中广播的所有坐标系信息，然后查询指定坐标系之间的变换。有关详细信息，请参阅“编写监听器”教程：:doc:`（Python） <../../Tutorials/Intermediate/Tf2/Writing-A-Tf2-Listener-Py>`` :doc:`（C++） <../../Tutorials/Intermediate/Tf2/Writing-A-Tf2-Listener-Cpp>`。

如果希望扩展机器人的能力，就需要开始广播坐标变换。广播坐标变换意味着向系统中的其他部分发送坐标系之间的相对位姿。一个系统可以包含多个广播器，每个广播器负责提供机器人不同部分的信息。有关详细信息，请参阅“编写广播器”教程：:doc:`（Python） <../../Tutorials/Intermediate/Tf2/Writing-A-Tf2-Broadcaster-Py>`` :doc:`（C++） <../../Tutorials/Intermediate/Tf2/Writing-A-Tf2-Broadcaster-Cpp>`。

此外，tf2 还可以广播不会随时间变化的静态坐标变换。这主要用于节省存储空间和查询时间，同时也能减少发布开销。请注意，静态变换只发布一次，并假设之后不会发生变化，因此不会保存历史记录。如果要在 tf2 坐标树中定义静态变换，请参阅“编写静态广播器”教程：:doc:`（Python） <../../Tutorials/Intermediate/Tf2/Writing-A-Tf2-Static-Broadcaster-Py>`` :doc:`（C++） <../../Tutorials/Intermediate/Tf2/Writing-A-Tf2-Static-Broadcaster-Cpp>`。

你还可以通过“添加坐标系”教程，学习如何向 tf2 坐标树中添加固定坐标系和动态坐标系：:doc:`（Python） <../../Tutorials/Intermediate/Tf2/Adding-A-Frame-Py>`` :doc:`（C++） <../../Tutorials/Intermediate/Tf2/Adding-A-Frame-Cpp>`。

完成基础教程后，可以继续学习 tf2 与时间的关系。:doc:`tf2 与时间教程（C++） <../../Tutorials/Intermediate/Tf2/Learning-About-Tf2-And-Time-Cpp>`` 介绍 tf2 和时间的基本原理；:doc:`tf2 时间旅行进阶教程（C++） <../../Tutorials/Intermediate/Tf2/Time-Travel-With-Tf2-Cpp>` 则介绍如何使用 tf2 进行时间回溯。

论文
------

2013 年 TePRA 会议发表过一篇关于 tf2 的论文：

`tf: The transform library <https://ieeexplore.ieee.org/abstract/document/6556373>`_。
