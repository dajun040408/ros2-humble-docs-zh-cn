使用 Foxglove Studio 可视化 ROS 2 数据
=========================================

`Foxglove Studio <https://foxglove.dev/studio>`_ 是一款开源工具，用于可视化和调试机器人数据。

它提供多种使用方式，方便开发工作：可以作为独立桌面应用运行，也可以通过浏览器访问，甚至可以托管在自己的域名下。

可以在 `GitHub <https://www.github.com/foxglove/studio>`_ 查看源代码。

安装
----

要使用 Web 应用，只需打开 Google Chrome 并访问 `studio.foxglove.dev <https://studio.foxglove.dev>`_。

要在 Linux、macOS 或 Windows 上使用桌面应用，请直接从 `Foxglove Studio 网站 <https://foxglove.dev/download>`_ 下载。

连接数据源
----------

打开 Foxglove Studio 后，会看到一个对话框，其中列出了`所有可用数据源 <https://foxglove.dev/docs/studio/connection/data-sources>`_。

要连接 ROS 2 系统，点击“Open connection”，选择“Rosbridge (ROS 1 & 2)”选项卡，并配置“WebSocket URL”。

也可以将本地 ROS 2 `.db3` 文件直接拖放到应用程序中，以加载并回放数据。

.. note::

  如果需要`加载 ROS 2 文件中的自定义消息定义 <https://github.com/ros2/rosbag2/issues/782>`_，可以尝试将其转换为 `MCAP 文件格式 <https://mcap.dev>`_。

更详细的操作说明请参阅 `Foxglove Studio 文档 <https://foxglove.dev/docs/studio/connection/native>`_。

使用面板构建布局
----------------

`面板 <https://foxglove.dev/docs/studio/panels/introduction>`_ 是模块化可视化界面，可以进行配置和排列，组成 Studio `布局 <https://foxglove.dev/docs/studio/layouts>`_。你也可以保存布局，以便个人日后参考，或与机器人团队共享。

可以在侧边栏的“Add panel”选项卡中查看所有可用面板。

下面介绍一些特别有用的面板：

1. 3D：在三维场景中显示可视化标记
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

发布标记消息，可以在 3D 面板场景中添加基本形状（箭头、球体等）以及更复杂的可视化对象（占据栅格、点云等）。

通过左侧的话题选择器选择要显示的话题，并在“Edit topic settings”菜单中配置每个话题的可视化设置。

.. image:: foxglove-studio/3d.png
  :width: 500 px
  :alt: Foxglove Studio 的 3D 面板

完整支持消息类型列表和常用交互方式请参阅 `3D 面板文档 <https://foxglove.dev/docs/studio/panels/3d>`_、`支持的消息 <https://foxglove.dev/docs/studio/panels/3d#supported-messages>`_ 和 `用户交互 <https://foxglove.dev/docs/studio/panels/3d#user-interactions>`_。

2. Diagnostics：筛选和排序诊断消息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

从正在运行的数据流中，显示数据类型为 `diagnostic_msgs/msg/DiagnosticArray` 的话题所报告节点的状态（例如 stale、error、warn 或 OK），并显示指定 `diagnostic_name/hardware_id` 的诊断数据。

.. image:: foxglove-studio/diagnostics.png
  :width: 500 px
  :alt: Foxglove Studio 的 Diagnostics 面板

更多详情请参阅 `Diagnostics 文档 <https://foxglove.dev/docs/studio/panels/diagnostics>`_。

3. Image：查看摄像头图像
^^^^^^^^^^^^^^^^^^^^^^^^

选择 `sensor_msgs/msg/Image` 或 `sensor_msgs/msg/CompressedImage` 类型的话题即可显示图像。

.. image:: foxglove-studio/image.png
  :width: 500 px
  :alt: Foxglove Studio 的 Image 面板

更多详情请参阅 `Image 文档 <https://foxglove.dev/docs/studio/panels/image>`_。

4. Log：查看日志消息
^^^^^^^^^^^^^^^^^^^^^

要实时查看 `rcl_interfaces/msg/Log` 消息，请使用桌面应用`连接 <https://foxglove.dev/docs/studio/connection/native>`_ 到正在运行的 ROS 系统。

要查看预先录制的数据文件中的 `rcl_interfaces/msg/Log` 消息，可以将文件拖放到 Web 应用或桌面应用中。

接下来，将 `Log` 面板添加到布局中。如果已正确连接 ROS 系统，就可以看到日志消息列表，并按节点名称或严重级别筛选。

更多详情请参阅 `Log 面板文档 <https://foxglove.dev/docs/studio/panels/log>`_。

5. Plot：绘制任意数值随时间变化的曲线
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

可以在回放时间轴上绘制话题消息路径中的任意数值。

指定要绘制在 Y 轴上的话题值。X 轴可以选择 Y 轴值的时间戳、元素索引，或其他自定义话题消息路径。

.. image:: foxglove-studio/plot.png
  :width: 500 px
  :alt: Foxglove Studio 的 Plot 面板

更多详情请参阅 `Plot 面板文档 <https://foxglove.dev/docs/studio/panels/plot>`_。

6. Raw Messages：查看接收到的话题消息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

以易于阅读、可折叠的 JSON 树结构显示接收到的话题数据。

.. image:: foxglove-studio/raw-messages.png
  :width: 500 px
  :alt: Foxglove Studio 的 Raw Messages 面板

更多详情请参阅 `Raw Messages 面板文档 <https://foxglove.dev/docs/studio/panels/raw-messages>`_。

7. Teleop：远程控制机器人
^^^^^^^^^^^^^^^^^^^^^^^^^

通过在指定话题上发布 `geometry_msgs/msg/Twist` 消息，可以远程控制正在运行的物理机器人。

.. image:: foxglove-studio/teleop.png
  :width: 300 px
  :alt: Foxglove Studio 的 Teleop 面板

更多详情请参阅 `Teleop 面板文档 <https://foxglove.dev/docs/studio/panels/teleop>`_。

8. URDF Viewer：查看和操作 URDF 模型
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

要在 Foxglove Studio 中可视化和控制机器人模型，请打开 Web 或桌面应用，并将 `URDF Viewer <https://foxglove.dev/docs/studio/panels/urdf-viewer>`_ 面板添加到布局中。然后将 URDF 文件拖放到该面板中，即可查看机器人模型。

.. image:: foxglove-studio/urdf.png
  :width: 300 px
  :alt: Foxglove Studio 的 URDF Viewer 面板

选择一个发布 `JointState` 消息的话题，即可根据发布的关节状态更新可视化结果（默认话题为 `/joint_states`）。

切换到“Manual joint control”，即可通过提供的控件设置关节位置。

.. image:: foxglove-studio/urdf-joints.png
  :width: 500 px
  :alt: Foxglove Studio 的 URDF Viewer 面板及可编辑关节位置

更多详情请参阅 `URDF Viewer 文档 <https://foxglove.dev/docs/studio/panels/urdf-viewer>`_。

其他基本操作
------------

1. 查看 ROS 计算图
^^^^^^^^^^^^^^^^^^

使用`桌面应用 <https://foxglove.dev/download>`_ `连接 <https://foxglove.dev/docs/studio/connection/native>`_到正在运行的 ROS 系统。然后将 `Topic Graph` 面板添加到布局中。如果已正确连接，就可以在该面板中看到 ROS 节点、话题和服务组成的计算图。使用面板右侧的控件选择要显示的话题，或切换服务显示状态。

2. 查看和编辑 ROS 参数
^^^^^^^^^^^^^^^^^^^^^^

使用`桌面应用 <https://foxglove.dev/download>`_ `连接 <https://foxglove.dev/docs/studio/connection/native>`_到正在运行的 ROS 系统。然后将 `Parameters` 面板添加到布局中。如果已正确连接，就可以实时查看当前 ROS 参数。可以编辑参数值，并将参数更新发布回 ROS 系统。

3. 向正在运行的 ROS 系统发布消息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用`桌面应用 <https://foxglove.dev/download>`_ `连接 <https://foxglove.dev/docs/studio/connection/native>`_到正在运行的 ROS 系统。然后将 `Publish` 面板添加到布局中。

指定要发布的话题，面板会推断其数据类型，并在文本框中填入 JSON 消息模板。

也可以在常见 ROS 数据类型下拉列表中选择数据类型，文本框同样会自动填入 JSON 消息模板。

编辑模板以自定义消息，然后点击“Publish”发布。

.. image:: foxglove-studio/publish.png
  :width: 300 px
  :alt: Foxglove Studio 的 Publish 面板
