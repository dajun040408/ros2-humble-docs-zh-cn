.. redirect-from::

    Tutorials/Tf2/Debugging-Tf2-Problems

.. _DebuggingTf2Problems:

tf2 问题调试
============

**目标：** 学习使用系统化方法调试 tf2 相关问题。

**教程级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

本教程将逐步介绍如何调试典型 tf2 问题，并使用 tf2_echo、tf2_monitor 和 view_frames 等调试工具。

本教程假设你已经完成 :doc:§学习 tf2 系列教程 <./Tf2-Main>§。

调试示例
--------

1. 设置并启动示例
^^^^^^^^^^^^^^^^^^

本教程将配置一个包含多个问题的演示应用。目标是使用系统化方法查找并解决这些问题。

进入此前创建的 learning_tf2_cpp 功能包。在 src 目录中复制 turtle_tf2_listener.cpp，并将其重命名为 turtle_tf2_listener_debug.cpp。

打开文件，将第 67 行：

.. code-block:: cpp

   std::string toFrameRel = "turtle2";

改为：

.. code-block:: cpp

   std::string toFrameRel = "turtle3";

再将第 75 至 79 行的 lookupTransform() 调用：

.. code-block:: cpp

   try {
      t = tf_buffer_->lookupTransform(
        toFrameRel,
        fromFrameRel,
        tf2::TimePointZero);
   } catch (tf2::TransformException & ex) {

改为：

.. code-block:: cpp

   try {
      t = tf_buffer_->lookupTransform(
        toFrameRel,
        fromFrameRel,
        this->now());
   } catch (tf2::TransformException & ex) {

保存修改。

为了运行该演示，需要在 learning_tf2_cpp 功能包的 launch 子目录中创建名为 start_tf2_debug_demo_launch 的启动文件，扩展名可以为 .py、.xml 或 .yaml。

不要忘记在 CMakeLists.txt 中添加 turtle_tf2_listener_debug 可执行程序，并重新构建功能包。

运行启动文件后，会看到 turtlesim 窗口。再打开一个终端运行 turtle_teleop_key，就可以使用方向键控制 turtle1。

.. code-block:: console

   $ ros2 run turtlesim turtle_teleop_key

此时会看到类似以下错误：

.. code-block:: text

   Could not transform turtle3 to turtle1: "turtle3" passed to lookupTransform argument target_frame does not exist

你还会看到左下角有第二只乌龟。如果演示正常，这只乌龟应该跟随你通过方向键控制的乌龟，但目前它并没有跟随，因为还需要先解决一些问题。

2. 找出 tf2 请求
^^^^^^^^^^^^^^^^

首先，需要弄清楚代码具体要求 tf2 执行什么操作。

打开 src/turtle_tf2_listener_debug.cpp，查看设置目标坐标系的代码：

.. code-block:: cpp

   std::string toFrameRel = "turtle3";

以及 lookupTransform() 调用：

.. code-block:: cpp

   try {
      t = tf_buffer_->lookupTransform(
        toFrameRel,
        fromFrameRel,
        this->now());
   } catch (tf2::TransformException & ex) {

这里就是向 tf2 发出请求的位置。请求包含目标坐标系、源坐标系和时间参数。

3. 检查坐标系是否存在
^^^^^^^^^^^^^^^^^^^^^

错误信息表明 turtle3 坐标系不存在。可以使用 view_frames 生成当前 tf2 坐标系树，检查实际广播的坐标系名称：

.. code-block:: console

   $ ros2 run tf2_tools view_frames

打开生成的 frames.pdf，检查坐标系树中是否存在请求的坐标系。

4. 检查变换时间
^^^^^^^^^^^^^^^

如果坐标系存在，但仍然无法获得变换，可以检查时间参数是否有效，以及所请求的时间是否位于缓冲区保存的变换时间范围内。

使用 tf2_monitor 可以检查变换发布频率、延迟和广播者等信息：

.. code-block:: console

   $ ros2 run tf2_ros tf2_monitor

总结
----

调试 tf2 问题时，应先明确 lookupTransform() 的源坐标系、目标坐标系和时间参数，再检查坐标系树、变换发布状态以及时间范围。tf2_echo、tf2_monitor 和 view_frames 都是定位问题的实用工具。
