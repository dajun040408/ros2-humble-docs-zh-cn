.. redirect-from::

    Tutorials/Tf2/Writing-A-Tf2-Broadcaster-Py

编写广播器（Python）
====================

**目标：** 学习如何向 tf2 广播机器人的状态。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

接下来的两个教程将编写代码，重现 :doc:`tf2 入门 <./Introduction-To-Tf2>` 中的演示。之后的教程会扩展更多高级功能，包括变换查询超时和时间旅行。

前置条件
--------

需要具备 ROS 2 基础知识，并完成 :doc:`tf2 入门教程 <./Introduction-To-Tf2>` 和 :doc:`Python 静态广播器教程 <./Writing-A-Tf2-Static-Broadcaster-Py>`。本教程会继续使用 ``learning_tf2_py`` 功能包。

任务
----

1. 编写广播器节点
^^^^^^^^^^^^^^^^^

在 ``src/learning_tf2_py/learning_tf2_py`` 目录下载示例代码：

.. code-block:: console

   $ wget https://raw.githubusercontent.com/ros/geometry_tutorials/{DISTRO}/turtle_tf2_py/turtle_tf2_py/turtle_tf2_broadcaster.py

Windows 可以使用 ``curl`` 下载。节点订阅海龟的位姿话题，并将海龟位姿广播到 tf2。主要实现如下：

.. code-block:: python

   class FramePublisher(Node):
       def __init__(self):
           super().__init__('turtle_tf2_frame_publisher')
           self.turtlename = self.declare_parameter(
               'turtlename', 'turtle').get_parameter_value().string_value
           self.tf_broadcaster = TransformBroadcaster(self)
           self.subscription = self.create_subscription(
               Pose,
               f'/{self.turtlename}/pose',
               self.handle_turtle_pose,
               1)

       def handle_turtle_pose(self, msg):
           t = TransformStamped()
           t.header.stamp = self.get_clock().now().to_msg()
           t.header.frame_id = 'world'
           t.child_frame_id = self.turtlename
           t.transform.translation.x = msg.x
           t.transform.translation.y = msg.y
           t.transform.translation.z = 0.0
           q = quaternion_from_euler(0, 0, msg.theta)
           t.transform.rotation.x = q[0]
           t.transform.rotation.y = q[1]
           t.transform.rotation.z = q[2]
           t.transform.rotation.w = q[3]
           self.tf_broadcaster.sendTransform(t)

1.1 理解代码
~~~~~~~~~~~~

首先声明并获取 ``turtlename`` 参数，用于指定海龟名称，例如 ``turtle1`` 或 ``turtle2``。节点订阅 ``/{turtlename}/pose`` 话题，每收到一条消息就执行 ``handle_turtle_pose``。

回调函数创建 ``TransformStamped``，设置当前时间戳、父坐标系 ``world`` 和子坐标系海龟名称。海龟只有二维运动，因此 x、y 来自位姿消息，z 设置为 0；旋转只绕 z 轴发生，因此使用 ``msg.theta`` 计算四元数。最后调用 ``sendTransform()`` 发布变换。

1.2 添加入口点
~~~~~~~~~~~~~~

在 ``src/learning_tf2_py/setup.py`` 的 ``console_scripts`` 中添加：

.. code-block:: python

   'turtle_tf2_broadcaster = learning_tf2_py.turtle_tf2_broadcaster:main',

2. 编写启动文件
^^^^^^^^^^^^^^^

在 ``src/learning_tf2_py`` 中创建 ``launch`` 目录，并创建 ``turtle_tf2_demo_launch.py``、``.xml`` 或 ``.yaml`` 启动文件。

.. tabs::

  .. group-tab:: XML

    .. literalinclude:: launch/py_turtle_tf2_demo_launch.xml
        :language: xml

  .. group-tab:: YAML

    .. literalinclude:: launch/py_turtle_tf2_demo_launch.yaml
        :language: yaml

  .. group-tab:: Python

    .. literalinclude:: launch/py_turtle_tf2_demo_launch.py
        :language: python

启动文件会启动 turtlesim 仿真节点，并启动 ``turtle_tf2_broadcaster`` 将 ``turtle1`` 的状态广播到 tf2。

2.1 添加依赖
~~~~~~~~~~~~

在 ``package.xml`` 中添加启动依赖：

.. code-block:: xml

   <exec_depend>launch</exec_depend>
   <exec_depend>launch_ros</exec_depend>

在 ``setup.py`` 的 ``data_files`` 中安装启动文件：

.. code-block:: python

   import os
   from glob import glob

   data_files=[
       ...
       (os.path.join('share', package_name, 'launch'), glob('launch/*')),
   ],

3. 构建
^^^^^^^

在工作空间根目录检查依赖：

.. code-block:: console

   $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

macOS 和 Windows 上 rosdep 不可用，需要自行安装 ``geometry_msgs`` 和 ``turtlesim`` 依赖。

构建功能包：

.. code-block:: console

   $ colcon build --packages-select learning_tf2_py

Windows 使用 ``--merge-install``。打开新终端并 source 工作空间环境。

4. 运行
^^^^^^^

运行启动文件：

.. tabs::

  .. group-tab:: XML

    .. code-block:: console

        $ ros2 launch learning_tf2_py turtle_tf2_demo_launch.xml

  .. group-tab:: YAML

    .. code-block:: console

        $ ros2 launch learning_tf2_py turtle_tf2_demo_launch.yaml

  .. group-tab:: Python

    .. code-block:: console

        $ ros2 launch learning_tf2_py turtle_tf2_demo_launch.py

在第二个终端运行键盘控制节点：

.. code-block:: console

   $ ros2 run turtlesim turtle_teleop_key

现在可以控制第一只海龟。

.. image:: images/turtlesim_broadcast.png

使用 ``tf2_echo`` 检查海龟位姿是否已广播到 tf2：

.. code-block:: console

   $ ros2 run tf2_ros tf2_echo world turtle1

该命令会持续显示第一只海龟的位姿。使用方向键移动海龟，终端会输出时间戳、平移、四元数旋转、RPY 旋转和变换矩阵。

如果查询 ``world`` 到 ``turtle2`` 的变换，此时不会看到结果，因为第二只海龟尚未创建。后续教程创建第二只海龟后，其位姿也会被广播到 tf2。

总结
----

本教程介绍了如何将机器人的位姿（海龟的位置和方向）广播到 tf2，以及如何使用 ``tf2_echo`` 工具检查变换。若要使用广播到 tf2 的变换，请继续学习 :doc:`创建 tf2 监听器 <./Writing-A-Tf2-Listener-Py>`。
