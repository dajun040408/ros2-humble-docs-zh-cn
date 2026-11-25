RViz 用户指南
=============

**目标：** 了解 RViz 的基本使用方法。

**教程级别：** 中级

**预计时间：** 25 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

RViz 是 Robot Operating System（ROS，机器人操作系统）框架中的三维可视化工具。

安装或构建 RViz
---------------

按照操作系统对应的 :doc:`安装说明 <../../../../Installation>` 安装 RViz。

启动
----

启动 RViz 前不要忘记 source ROS 2 环境：

.. code-block:: console

   $ source /opt/ros/{DISTRO}/setup.bash

然后启动可视化程序：

.. code-block:: console

   $ ros2 run rviz2 rviz2

首次启动 RViz 时，会显示以下窗口：

.. image:: images/initial_startup.png

中间的大型黑色窗口是三维视图，因为当前没有数据，所以为空。

左侧是 Displays 列表，显示已经加载的显示插件。初始状态下通常包含 Global Options 和 Grid，后面会介绍这两项内容。

右侧是其他面板，下面也会逐一说明。

Displays
--------

Display 是用于在三维场景中绘制数据的插件，通常会在 Displays 列表中提供相应属性。例如，点云、机器人状态等都可以通过 Display 显示。

添加 Display
^^^^^^^^^^^^

点击底部的 Add 按钮：

.. image:: images/add-button.png

随后会弹出新增 Display 对话框：

.. image:: images/add-display-dialog.png

顶部列表用于选择 Display 类型。类型决定该插件可以可视化哪种数据。中间文本框显示所选类型的描述。最后，需要为 Display 指定一个唯一名称。

例如，如果机器人上有两个激光雷达，可以创建两个 ``Laser Scan`` 显示，并分别命名为 ``Laser Base`` 和 ``Laser Head``。

Display 属性
^^^^^^^^^^^^

每个 Display 都有自己的属性列表。例如：

.. image:: images/display-properties.png

Display 状态
^^^^^^^^^^^^

每个 Display 都有自己的状态信息，用于提示显示是否正常。状态包括 ``OK``、``Warning``、``Error`` 和 ``Disabled``。

状态会通过 Display 标题的背景颜色显示，也会显示在展开 Display 后的 Status 分类中：

.. image:: images/display-status.png

展开 ``Status`` 分类后，还可以查看具体的状态信息。不同 Display 提供的状态信息可能不同，相关消息通常会直接说明问题。

内置 Display 类型
^^^^^^^^^^^^^^^^^

下表列出了 RViz 内置的常见 Display 类型、用途以及对应使用的消息类型。

.. list-table::
   :header-rows: 1
   :widths: 15 45 40

   * - 名称
     - 描述
     - 使用的消息
   * - Axes（坐标轴）
     - 显示一组坐标轴。
     -
   * - Effort（关节力矩）
     - 显示机器人每个旋转关节所承受的力或力矩。
     - `sensor_msgs/msg/JointState <https://github.com/ros2/common_interfaces/blob/{DISTRO}/sensor_msgs/msg/JointState.msg>`_
   * - Camera（相机）
     - 根据相机视角创建新的渲染窗口，并在其上叠加图像。
     - `sensor_msgs/msg/Image <https://github.com/ros2/common_interfaces/blob/{DISTRO}/sensor_msgs/msg/Image.msg>`_、`sensor_msgs/msg/CameraInfo <https://github.com/ros2/common_interfaces/blob/{DISTRO}/sensor_msgs/msg/CameraInfo.msg>`_
   * - Grid（网格）
     - 沿某个平面显示二维或三维网格。
     -
   * - Grid Cells（网格单元）
     - 绘制网格中的单元格，通常用于显示 Navigation2 导航栈代价地图中的障碍物。
     - `nav_msgs/msg/GridCells <https://github.com/ros2/common_interfaces/blob/{DISTRO}/nav_msgs/msg/GridCells.msg>`_
   * - Image（图像）
     - 创建一个显示图像的新渲染窗口。与 Camera 显示不同，该显示不使用 CameraInfo。
     - `sensor_msgs/msg/Image <https://github.com/ros2/common_interfaces/blob/{DISTRO}/sensor_msgs/msg/Image.msg>`_
   * - InteractiveMarker（交互式标记）
     - 显示一个或多个 Interactive Marker 服务端发布的三维对象，并允许用户通过鼠标与其交互。
     - `visualization_msgs/msg/InteractiveMarker <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/InteractiveMarker.msg>`_
   * - Laser Scan（激光扫描）
     - 显示激光扫描数据，并提供不同渲染模式、数据累积等选项。
     - `sensor_msgs/msg/LaserScan <https://github.com/ros2/common_interfaces/blob/{DISTRO}/sensor_msgs/msg/LaserScan.msg>`_
   * - Map（地图）
     - 在地面平面上显示地图。
     - `nav_msgs/msg/OccupancyGrid <https://github.com/ros2/common_interfaces/blob/{DISTRO}/nav_msgs/msg/OccupancyGrid.msg>`_
   * - Markers（标记）
     - 允许程序通过话题显示任意基本几何形状。
     - `visualization_msgs/msg/Marker <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/Marker.msg>`_、`visualization_msgs/msg/MarkerArray <https://github.com/ros2/common_interfaces/blob/{DISTRO}/visualization_msgs/msg/MarkerArray.msg>`_
   * - Path（路径）
     - 显示 Navigation2 导航栈发布的路径。
     - `nav_msgs/msg/Path <https://github.com/ros2/common_interfaces/blob/{DISTRO}/nav_msgs/msg/Path.msg>`_
   * - Point（点）
     - 将一个点绘制为小球体。
     - `geometry_msgs/msg/PointStamped <https://github.com/ros2/common_interfaces/blob/{DISTRO}/geometry_msgs/msg/PointStamped.msg>`_
   * - Pose（位姿）
     - 将一个位姿绘制为箭头或坐标轴。
     - `geometry_msgs/msg/PoseStamped <https://github.com/ros2/common_interfaces/blob/{DISTRO}/geometry_msgs/msg/PoseStamped.msg>`_
   * - Pose Array（位姿数组）
     - 将位姿数组中的每个位姿绘制为箭头，从而形成箭头集合。
     - `geometry_msgs/msg/PoseArray <https://github.com/ros2/common_interfaces/blob/{DISTRO}/geometry_msgs/msg/PoseArray.msg>`_
   * - Point Cloud（点云）
     - 显示点云数据，并提供不同渲染模式、数据累积等选项。
     - `sensor_msgs/msg/PointCloud <https://github.com/ros2/common_interfaces/blob/{DISTRO}/sensor_msgs/msg/PointCloud.msg>`_、`sensor_msgs/msg/PointCloud2 <https://github.com/ros2/common_interfaces/blob/{DISTRO}/sensor_msgs/msg/PointCloud2.msg>`_
   * - Polygon（多边形）
     - 使用线条绘制多边形轮廓。
     - `geometry_msgs/msg/Polygon <https://github.com/ros2/common_interfaces/blob/{DISTRO}/geometry_msgs/msg/Polygon.msg>`_
   * - Odometry（里程计）
     - 累积并显示一段时间内的里程计位姿。
     - `nav_msgs/msg/Odometry <https://github.com/ros2/common_interfaces/blob/{DISTRO}/nav_msgs/msg/Odometry.msg>`_
   * - Range（距离）
     - 显示声呐或红外距离传感器测量值对应的圆锥体。
     - `sensor_msgs/msg/Range <https://github.com/ros2/common_interfaces/blob/{DISTRO}/sensor_msgs/msg/Range.msg>`_
   * - RobotModel（机器人模型）
     - 根据当前 TF 变换定义的位姿显示机器人的可视化模型。
     -
   * - TF
     - 显示 tf2 坐标变换层级结构。
     -
   * - Wrench（力/力矩）
     - 使用箭头表示力，使用箭头和圆形表示力矩。
     - `geometry_msgs/msg/WrenchStamped <https://github.com/ros2/common_interfaces/blob/{DISTRO}/geometry_msgs/msg/WrenchStamped.msg>`_
   * - Twist（速度）
     - 使用箭头表示线速度，使用箭头和圆形表示角速度。
     - `geometry_msgs/msg/TwistStamped <https://github.com/ros2/common_interfaces/blob/{DISTRO}/geometry_msgs/msg/TwistStamped.msg>`_

配置（Configurations）
----------------------

对于不同的可视化用途，通常需要使用不同的 Display 配置。

例如，适用于完整 PR2 机器人的配置不一定适用于测试小车。因此，RViz 支持加载和保存不同的配置。

一个配置包含：

* Displays 及其属性。
* 工具属性。
* 三维可视化视角及其相关设置。

视角面板（Views Panel）
-----------------------

RViz 提供多种相机类型：

.. image:: images/camera-types.png

相机类型既包括不同的相机控制方式，也包括不同的投影方式（正交投影或透视投影）。

轨道相机（默认）
^^^^^^^^^^^^^^^^

轨道相机会围绕一个焦点旋转，并始终朝向该焦点。

移动相机时，焦点会显示为一个小圆盘：

.. image:: images/focal-point.png

控制方式：

* **鼠标左键：** 按住并拖动，使相机围绕焦点旋转。
* **鼠标中键：** 按住并拖动，在由相机向上方向和向右方向构成的平面内移动焦点。

  移动距离取决于焦点位置。如果某个对象正好位于焦点上，并且你在该对象上按下鼠标中键拖动，该对象会保持在鼠标指针下方。

* **鼠标右键：** 按住并拖动，以焦点为中心缩放。向上拖动表示放大，向下拖动表示缩小。
* **滚轮：** 以焦点为中心放大或缩小。

第一人称相机（FPS）
^^^^^^^^^^^^^^^^^^^

FPS 相机采用第一人称视角，旋转方式类似于人转动头部观察周围环境。

控制方式：

* **鼠标左键：** 按住并拖动以旋转相机。按住 Ctrl 并单击，可以选中鼠标下方的对象并直接观察该对象。
* **鼠标中键：** 按住并拖动，在由相机向上方向和向右方向构成的平面内移动。
* **鼠标右键：** 按住并拖动，沿相机前向方向移动。向上拖动表示向前移动，向下拖动表示向后移动。
* **滚轮：** 向前或向后移动。

俯视正交相机
^^^^^^^^^^^^

俯视正交相机始终沿机器人坐标系的 Z 轴向下观察，并使用正交投影。这意味着对象不会因为距离相机更远而显得更小。

控制方式：

* **鼠标左键：** 按住并拖动，围绕 Z 轴旋转。
* **鼠标中键：** 按住并拖动，沿 XY 平面移动相机。
* **鼠标右键：** 按住并拖动，缩放图像。
* **滚轮：** 缩放图像。

XY 轨道相机
^^^^^^^^^^^

该相机与轨道相机相同，但焦点被限制在 XY 平面内移动。

控制方式：参阅轨道相机的控制方式。

第三人称跟随相机
^^^^^^^^^^^^^^^^

相机会保持相对于目标坐标系的固定观察角度。

与 XY 轨道相机不同，当目标坐标系发生偏航旋转时，相机也会随之转动。例如，在具有拐角的走廊中进行三维建图时，这种视角可能很有用。

控制方式：参阅轨道相机的控制方式。

自定义视角
^^^^^^^^^^

Views 面板还允许创建多个具名视角。保存后，可以在不同视角之间切换。

一个视角由目标坐标系、相机类型和相机位姿组成。点击 Views 面板中的 Save 按钮即可保存视角：

.. image:: images/views.png

视角包含：

* 视角控制器类型。
* 视角配置（位置、方向等，具体内容可能因视角控制器类型而异）。
* 目标坐标系（Target Frame）。

视角按用户保存，而不是保存在 RViz 配置文件中。

坐标系（Coordinate Frames）
---------------------------

RViz 使用 tf 变换系统，将数据从其原始坐标系转换到全局参考坐标系。

在 RViz 中，有两个重要的坐标系需要了解：目标坐标系（Target Frame）和固定坐标系（Fixed Frame）。

固定坐标系（The Fixed Frame）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

两个坐标系中更重要的是固定坐标系。

固定坐标系是用于表示 ``world`` 坐标系的参考坐标系。它通常是 ``map``、``world`` 或类似坐标系，也可以是里程计坐标系。

如果错误地将固定坐标系设置为机器人底座坐标系，那么机器人曾经看到的所有对象都会出现在机器人前方，并且位置始终是相对于机器人检测到它们时的位置。

为了得到正确结果，固定坐标系不应相对于世界发生移动。

如果更改固定坐标系，当前正在显示的所有数据都会被清除，而不是重新进行坐标变换。

目标坐标系（The Target Frame）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

目标坐标系是相机视角所使用的参考坐标系。

例如，如果目标坐标系设置为地图坐标系，就会看到机器人在地图中移动。

如果目标坐标系设置为机器人底座坐标系，机器人将保持在视图中的同一位置，而其他对象会相对于机器人移动。

工具（Tools）
------------

RViz 在工具栏中提供多种工具。下面简要介绍这些工具。

.. image:: images/tool.png

交互（Interact）
^^^^^^^^^^^^^^^^

该工具允许用户与可视化场景中的对象交互。

可以单击对象，并根据对象属性选择对象、移动对象或执行其他操作。

键盘快捷键：``i``。

移动相机（Move Camera）
^^^^^^^^^^^^^^^^^^^^^^^

移动相机是默认工具。

选择该工具后，在三维视图中单击，相机会根据 Views 面板中选择的选项和相机类型改变视角。更多信息请参阅前面的“视角面板”部分。

键盘快捷键：``m``。

选择（Select）
^^^^^^^^^^^^^

选择工具允许选中三维视图中显示的对象。

它支持单点选择，也支持通过单击并拖动鼠标进行框选。

* 按住 Shift 键可以向当前选择中添加对象。
* 按住 Ctrl 键可以从当前选择中移除对象。
* 如果希望在选择对象时移动相机，而不切换回 Move Camera 工具，可以按住 Alt 键。
* 按 ``f`` 键可以让相机聚焦于当前选中的对象。

.. image:: images/selection_highlight.png

.. image:: images/selection_selected.png

键盘快捷键：``s``。

聚焦相机（Focus Camera）
^^^^^^^^^^^^^^^^^^^^^^^^

聚焦相机工具允许在可视化场景中选择一个位置。

相机会通过改变自身方向来聚焦该点，但不会改变相机位置。

键盘快捷键：``c``。

测量（Measure）
^^^^^^^^^^^^^^

测量工具可以测量可视化场景中两个点之间的距离。

激活工具后，第一次单击设置测量起点，第二次单击设置终点。测量结果会显示在 RViz 窗口底部。

需要注意，测量工具只能用于场景中实际渲染出来的对象，不能在空白区域中使用。

.. image:: images/measure.png

键盘快捷键：``n``。

2D 位姿估计（2D Pose Estimate）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

该工具用于设置初始位姿，为定位系统提供初始估计值。消息会发布到 ``initialpose`` ROS 话题。

在地面平面上单击一个位置，然后拖动鼠标选择方向。输出话题可以在 Tool Properties 面板中修改。

.. image:: images/set_pose.png

该工具与 `Navigation2 <https://github.com/ros-planning/navigation2>`_ 导航栈配合使用。

键盘快捷键：``p``。

2D 导航目标（2D Nav Goal）
^^^^^^^^^^^^^^^^^^^^^^^^^

该工具用于设置导航目标，并将目标发布到 ``goal_pose`` ROS 话题。

在地面平面上单击一个位置，然后拖动鼠标选择目标方向。输出话题可以在 Tool Properties 面板中修改。

该工具与 `Navigation2 <https://github.com/ros-planning/navigation2>`_ 导航栈配合使用。

键盘快捷键：``g``。

发布点（Publish Point）
^^^^^^^^^^^^^^^^^^^^^^^

发布点工具允许在可视化场景中选择一个对象，并根据其所在坐标系发布该点的坐标。

结果会像测量工具一样显示在 RViz 窗口底部，同时也会发布到 ``clicked_point`` 话题。

键盘快捷键：``u``。

时间（Time）
-----------

Time 面板在仿真环境中尤其有用，因为它可以显示 ROS Time 已经经过的时间，以及 ``Wall Clock``（即真实时间）已经经过的时间。

Time 面板还允许重置 RViz 内部时间状态。重置后，所有 Display 以及 tf 内部的数据缓存都会被重置。

.. image:: images/time.png

如果没有运行仿真，Time 面板通常没有太大用处。大多数情况下可以将其关闭，除了为其他 RViz 内容腾出更多屏幕空间外，不会对使用造成明显影响。
