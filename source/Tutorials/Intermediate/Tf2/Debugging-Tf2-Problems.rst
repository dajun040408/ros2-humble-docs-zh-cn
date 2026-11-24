.. redirect-from::

    Tutorials/Tf2/Debugging-Tf2-Problems

.. _DebuggingTf2Problems:

调试 tf2 问题
=============

**目标：** 学习使用系统化方法调试 tf2 相关问题。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程将逐步介绍如何调试典型 tf2 问题，并使用多种 tf2 调试工具，例如 ``tf2_echo``、``tf2_monitor`` 和 ``view_frames``。

本教程假设你已经完成 :doc:`学习 tf2 系列教程 <./Tf2-Main>`。

调试示例
--------

1. 设置并启动示例
^^^^^^^^^^^^^^^^^^

本教程将配置一个包含多个问题的演示应用，目标是使用系统化方法查找并解决这些问题。

进入此前创建的 ``learning_tf2_cpp`` 功能包。在 ``src`` 目录中复制源文件 ``turtle_tf2_listener.cpp``，并将其重命名为 ``turtle_tf2_listener_debug.cpp``。

打开文件，将第 67 行：

.. code-block:: c++

   std::string toFrameRel = "turtle2";

修改为：

.. code-block:: c++

   std::string toFrameRel = "turtle3";

然后将第 75 至 79 行的 ``lookupTransform()`` 调用从：

.. code-block:: c++

   try {
      t = tf_buffer_->lookupTransform(
        toFrameRel,
        fromFrameRel,
        tf2::TimePointZero);
   } catch (tf2::TransformException & ex) {

修改为：

.. code-block:: c++

   try {
      t = tf_buffer_->lookupTransform(
        toFrameRel,
        fromFrameRel,
        this->now());
   } catch (tf2::TransformException & ex) {

保存文件。

为了运行该演示，需要在 ``learning_tf2_cpp`` 功能包的 ``launch`` 子目录中创建名为 ``start_tf2_debug_demo_launch`` 的启动文件，扩展名可以为 ``.py``、``.xml`` 或 ``.yaml``：

.. tabs::

  .. group-tab:: Python

    .. literalinclude:: launch/start_tf2_debug_demo_launch.py
       :language: python

  .. group-tab:: XML

    .. literalinclude:: launch/start_tf2_debug_demo_launch.xml
       :language: xml

  .. group-tab:: YAML

    .. literalinclude:: launch/start_tf2_debug_demo_launch.yaml
       :language: yaml

不要忘记在 ``CMakeLists.txt`` 中添加 ``turtle_tf2_listener_debug`` 可执行程序，并重新构建功能包。

现在运行启动文件：

.. tabs::

  .. group-tab:: XML

    .. code-block:: console

       $ ros2 launch learning_tf2_cpp start_tf2_debug_demo_launch.xml

  .. group-tab:: YAML

    .. code-block:: console

       $ ros2 launch learning_tf2_cpp start_tf2_debug_demo_launch.yaml

  .. group-tab:: Python

    .. code-block:: console

       $ ros2 launch learning_tf2_cpp start_tf2_debug_demo_launch.py

此时会启动 turtlesim。再打开另一个终端，运行 ``turtle_teleop_key``，就可以使用方向键控制 ``turtle1``：

.. code-block:: console

   $ ros2 run turtlesim turtle_teleop_key

你会看到类似以下错误：

.. code-block:: console

   [turtle_tf2_listener_debug-4] [INFO] [listener_debug]: Could not transform turtle3 to turtle1:
   "turtle3" passed to lookupTransform argument target_frame does not exist

你还会看到左下角有第二只乌龟。如果演示正常，这只乌龟应该跟随你通过方向键控制的乌龟，但目前它并没有跟随，因为还需要先解决一些问题。

2. 找出 tf2 请求
^^^^^^^^^^^^^^^^

首先，需要弄清楚代码具体要求 tf2 执行什么操作。打开 ``src/turtle_tf2_listener_debug.cpp``，查看设置目标坐标系的代码：

.. code-block:: c++

   std::string toFrameRel = "turtle3";

以及 ``lookupTransform()`` 调用：

.. code-block:: c++

   try {
      t = tf_buffer_->lookupTransform(
        toFrameRel,
        fromFrameRel,
        this->now());
   } catch (tf2::TransformException & ex) {

这里就是向 tf2 发出请求的位置。三个参数分别表示：从 ``turtle3`` 坐标系变换到 ``turtle1`` 坐标系，并且查询当前时间 ``now`` 对应的变换。

接下来检查为什么该请求失败。

3. 检查坐标系
^^^^^^^^^^^^^

首先，使用 ``tf2_echo`` 工具检查 tf2 是否知道 ``turtle3`` 和 ``turtle1`` 之间的变换：

.. code-block:: console

   $ ros2 run tf2_ros tf2_echo turtle3 turtle1
   [INFO] [tf2_echo]: Waiting for transform turtle3 -> turtle1:
   Invalid frame ID "turtle3" passed to canTransform argument target_frame - frame does not exist

输出表明 ``turtle3`` 坐标系不存在。

那么当前有哪些坐标系？可以使用 ``view_frames`` 工具生成图形化表示：

.. code-block:: console

   $ ros2 run tf2_tools view_frames

打开生成的 ``frames.pdf`` 文件：

.. image:: images/turtlesim_frames.png

显然，问题在于代码请求了从不存在的 ``turtle3`` 坐标系到 ``turtle1`` 坐标系的变换。

要修复该问题，只需将第 67 行中的 ``turtle3`` 替换为 ``turtle2``。

停止当前演示，重新构建并运行：

.. tabs::

  .. group-tab:: XML

    .. code-block:: console

       $ ros2 launch learning_tf2_cpp start_tf2_debug_demo_launch.xml

  .. group-tab:: YAML

    .. code-block:: console

       $ ros2 launch learning_tf2_cpp start_tf2_debug_demo_launch.yaml

  .. group-tab:: Python

    .. code-block:: console

       $ ros2 launch learning_tf2_cpp start_tf2_debug_demo_launch.py

此时又会出现下一个问题：

.. code-block:: console

   Could not transform turtle2 to turtle1: Lookup would require extrapolation into the future.
   Requested time ... but the latest data is at time ..., when looking up transform
   from frame [turtle1] to frame [turtle2]

4. 检查时间戳
^^^^^^^^^^^^^

现在已经解决了坐标系名称问题，接下来需要检查时间戳。

回顾一下，代码尝试获取 ``turtle2`` 和 ``turtle1`` 之间当前时间（``now``）的变换。可以使用 ``tf2_monitor`` 并指定对应坐标系，获取时间统计信息：

.. code-block:: console

   $ ros2 run tf2_ros tf2_monitor turtle2 turtle1
   RESULTS: for turtle2 to turtle1
   Chain is: turtle1
   Net delay     avg = 0.00287347: max = 0.0167241

   Frames:
   Frame: turtle1, published by <no authority available>, Average Delay: 0.000295833, Max Delay: 0.000755072

   All Broadcasters:
   Node: <no authority available> 125.246 Hz, Average Delay: 0.000290237 Max Delay: 0.000786781

这里的关键是 ``turtle2`` 到 ``turtle1`` 变换链的延迟。输出显示平均延迟约为 3 毫秒。这意味着 tf2 需要等待大约 3 毫秒，才能获得两只乌龟之间的变换。

因此，如果请求的是 3 毫秒之前的变换，而不是当前时间 ``now``，tf2 就有可能成功返回结果。

可以通过修改第 75 至 79 行快速验证。将时间参数改为当前时间减去 0.1 秒：

.. code-block:: c++

   try {
      t = tf_buffer_->lookupTransform(
        toFrameRel,
        fromFrameRel,
        this->now() - rclcpp::Duration::from_seconds(0.1));
   } catch (tf2::TransformException & ex) {

新代码请求的是 100 毫秒之前的变换。实际应用中通常会使用适当的时间间隔，确保所需变换已经到达。

停止演示，重新构建并运行：

.. tabs::

  .. group-tab:: XML

    .. code-block:: console

       $ ros2 launch learning_tf2_cpp start_tf2_debug_demo_launch.xml

  .. group-tab:: YAML

    .. code-block:: console

       $ ros2 launch learning_tf2_cpp start_tf2_debug_demo_launch.yaml

  .. group-tab:: Python

    .. code-block:: console

       $ ros2 launch learning_tf2_cpp start_tf2_debug_demo_launch.py

现在应该能看到第二只海龟开始移动：

.. image:: images/turtlesim_follow1.png

需要注意，刚才的修改只是为了验证问题确实来自时间延迟，并不是最理想的最终解决方法。

更合适的做法是将时间参数改为 ``tf2::TimePointZero``：

.. code-block:: c++

   try {
      t = tf_buffer_->lookupTransform(
        toFrameRel,
        fromFrameRel,
        tf2::TimePointZero);
   } catch (tf2::TransformException & ex) {

也可以使用：

.. code-block:: c++

   try {
      t = tf_buffer_->lookupTransform(
        toFrameRel,
        fromFrameRel,
        tf2::TimePoint());
   } catch (tf2::TransformException & ex) {

``TimePointZero`` 表示请求缓冲区中最新可用的变换，而不是要求获取当前时刻尚未到达的变换。

如果需要了解更多关于时间和超时的内容，请参阅 :doc:`使用时间 <./Learning-About-Tf2-And-Time-Cpp>` 教程。也可以在 ``lookupTransform()`` 中使用超时参数：

.. code-block:: c++

   try {
      t = tf_buffer_->lookupTransform(
        toFrameRel,
        fromFrameRel,
        this->now(),
        rclcpp::Duration::from_seconds(0.05));
   } catch (tf2::TransformException & ex) {

总结
----

本教程介绍了使用系统化方法调试 tf2 问题的过程。

还学习了如何使用 ``tf2_echo``、``tf2_monitor`` 和 ``view_frames`` 等工具，检查坐标系是否存在、变换时间戳是否有效，以及定位 tf2 变换失败的原因。
