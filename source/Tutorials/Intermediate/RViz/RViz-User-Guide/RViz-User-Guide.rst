RViz 用户指南
=============

**目标：** 了解 RViz 的基本使用方法。

**教程级别：** 中级 | **预计时间：** 25 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

RViz 是 ROS 框架中的三维可视化工具。

安装或构建 RViz
---------------

按照操作系统对应的 :doc:§安装说明 <../../../../Installation>§ 安装 RViz。

启动
----

启动 RViz 前不要忘记 source ROS 2 环境：

.. code-block:: console

   $ source /opt/ros/{DISTRO}/setup.bash

启动可视化程序：

.. code-block:: console

   $ ros2 run rviz2 rviz2

首次启动 RViz 时，会显示初始窗口：

.. image:: images/initial_startup.png

中间的大型黑色窗口是三维视图，因为当前没有数据，所以为空。左侧是 Displays 列表，显示已加载的显示插件。初始状态下通常包含 Global Options 和 Grid。右侧是其他面板。

Displays
--------

Display 是在三维场景中绘制数据的插件，并通常在 Displays 列表中提供相应属性。例如点云、机器人状态等。

添加 Display
^^^^^^^^^^^^

点击底部的 Add 按钮：

.. image:: images/add-button.png

随后会弹出新增 Display 对话框：

.. image:: images/add-display-dialog.png

顶部列表用于选择 Display 类型，类型决定该插件可以可视化哪种数据。中间文本框显示所选类型的描述。最后，需要为 Display 指定唯一名称。

例如，机器人上有两个激光雷达时，可以添加两个 §Laser Scan§ 显示，并分别命名为 §Laser Base§ 和 §Laser Head§。

Display 属性
^^^^^^^^^^^^

每个 Display 都有自己的属性列表，可用于配置数据源、坐标变换、显示样式和其他行为。

.. image:: images/display-properties.png

Display 状态
^^^^^^^^^^^^

每个 Display 都有状态信息，用于提示运行是否正常。状态包括：

* §OK§：正常。
* §Warning§：警告。
* §Error§：错误。
* §Disabled§：已禁用。

状态会显示在 Display 标题的背景颜色中，也会显示在 Status 属性分类下。

全局选项
--------

Global Options 用于配置整个 RViz 场景的公共属性，例如 Fixed Frame、背景颜色和帧率。§Fixed Frame§ 是 RViz 用于显示数据的参考坐标系，必须选择 TF 树中实际存在的坐标系。

视角控制
--------

RViz 提供多种视角控制方式，可以使用鼠标旋转、平移和缩放三维视图。也可以选择不同视角类型，以便从机器人不同方向观察场景。

总结
----

本指南介绍了 RViz 的基本界面、Display 管理、Display 属性和状态，以及全局选项和三维视角控制。
