.. redirect-from::

    Tutorials/Tf2/Adding-A-Frame-Py

tf2 添加坐标系（Python）
========================

**目标：** 学习如何向 tf2 添加额外坐标系。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 3
   :local:

背景
----

此前教程通过 :doc:`tf2 广播器 <./Writing-A-Tf2-Broadcaster-Py>` 和 :doc:`tf2 监听器 <Writing-A-Tf2-Listener-Py>` 重现了海龟演示。本教程介绍如何向变换树添加固定坐标系和动态坐标系。

对于许多坐标变换任务，使用局部坐标系思考更容易。例如，在激光雷达中心建立坐标系，可以更直观地理解激光扫描测量值。tf2 允许为系统中的传感器、连杆或关节定义局部坐标系，并自动处理坐标系之间的中间变换。

tf2 变换树
----------

tf2 使用树结构组织坐标系，不允许出现闭环。每个坐标系只能有一个父坐标系，但可以有多个子坐标系。当前树包含 ``world``、``turtle1`` 和 ``turtle2``，两只海龟都是 ``world`` 的子坐标系。

.. image:: images/turtlesim_frames.png

任务
----

1. 编写固定坐标系广播器
^^^^^^^^^^^^^^^^^^^^^^^

在海龟示例中添加名为 ``carrot1`` 的新坐标系，使其成为 ``turtle1`` 的子坐标系，并作为第二只海龟的目标。

进入此前创建的 ``learning_tf2_py`` 功能包，在 ``src/learning_tf2_py/learning_tf2_py`` 目录下载固定坐标系广播器：

.. code-block:: console

   $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/fixed_frame_tf2_broadcaster.py

Windows 可使用 ``curl`` 下载对应文件。

核心实现通过 ``StaticTransformBroadcaster`` 创建固定变换：

.. code-block:: python

   t = TransformStamped()
   t.header.stamp = self.get_clock().now().to_msg()
   t.header.frame_id = 'turtle1'
   t.child_frame_id = 'carrot1'
   t.transform.translation.x = 0.0
   t.transform.translation.y = 2.0
   t.transform.translation.z = 0.0
   t.transform.rotation.w = 1.0
   self.tf_static_broadcaster.sendTransform(t)

该变换表示 ``carrot1`` 相对于 ``turtle1`` 在 y 轴方向偏移 2 米。对于相对于父坐标系不会变化的坐标系，应使用静态广播器；对于随时间变化的坐标系，应使用 ``TransformBroadcaster`` 定期发布。

1.1 检查代码
~~~~~~~~~~~~

``TransformStamped`` 消息包含时间戳、父坐标系和子坐标系名称，以及平移和旋转信息。当前时间通过 ``self.get_clock().now().to_msg()`` 获取，父坐标系为 ``turtle1``，子坐标系为 ``carrot1``。

1.2 更新功能包配置
~~~~~~~~~~~~~~~~~~

在 ``setup.py`` 中为节点添加入口点，并确保 ``package.xml`` 声明 ``geometry_msgs``、``rclpy``、``tf2_ros_py`` 和 ``turtlesim`` 等运行依赖。

2. 编写动态坐标系广播器
^^^^^^^^^^^^^^^^^^^^^^^

动态坐标系会随时间改变相对于父坐标系的位姿。下载动态广播器示例：

.. code-block:: console

   $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/dynamic_frame_tf2_broadcaster.py

动态广播器定期计算 carrot 的位置，并通过 ``TransformBroadcaster`` 发布变换。示意计算如下：

.. code-block:: python

   x = now.seconds() * PI
   t.transform.translation.x = 10 * math.sin(x)
   t.transform.translation.y = 10 * math.cos(x)
   self.tf_broadcaster.sendTransform(t)

3. 构建与运行
^^^^^^^^^^^^^

在工作空间根目录检查依赖并构建：

.. code-block:: console

   $ rosdep install -i --from-path src --rosdistro {DISTRO} -y
   $ colcon build --packages-select learning_tf2_py

Windows 使用 ``--merge-install``。source 工作空间后，运行对应启动文件：

.. code-block:: console

   $ ros2 launch learning_tf2_py turtle_tf2_fixed_frame_demo_launch.py

要让第二只海龟跟随 carrot，可以在启动参数中将 ``target_frame`` 设置为 ``carrot1``。动态版本则运行 ``turtle_tf2_dynamic_frame_demo_launch.py``，观察第二只海龟跟随不断移动的 carrot。

总结
----

本教程介绍了 tf2 变换树的结构，以及如何在 Python 中添加固定和动态坐标系。
