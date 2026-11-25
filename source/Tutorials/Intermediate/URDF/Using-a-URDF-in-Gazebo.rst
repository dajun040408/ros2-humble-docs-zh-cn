在 Gazebo 中使用 URDF
=====================

**目标：** 在 Gazebo 仿真器中仿真 URDF 模型。

**教程级别：** 中级

**预计时间：** 30 分钟

.. contents:: 目录
   :depth: 2
   :local:

本教程基于 `ROS 1 对应教程 <http://wiki.ros.org/urdf/Tutorials/Using%20a%20URDF%20in%20Gazebo>`_。

首先安装演示功能包及其依赖。

.. tabs::

   .. group-tab:: Ubuntu 软件包

      .. code-block:: console

         $ sudo apt install ros-{DISTRO}-urdf-sim-tutorial

   .. group-tab:: RHEL 软件包

      .. code-block:: console

         $ sudo dnf install ros-{DISTRO}-urdf-sim-tutorial

   .. group-tab:: 从源码构建

      .. code-block:: console

         $ git clone https://github.com/ros/urdf_sim_tutorial.git -b ros2

Gazebo 中无法交互的机器人模型
-----------------------------

可以使用 ``gazebo.launch.py`` 将此前创建的模型加载到 Gazebo：

.. code-block:: console

   $ ros2 launch urdf_sim_tutorial gazebo.launch.py

该启动文件会执行以下操作：

* 加载 :doc:`Xacro 教程 <Using-Xacro-to-Clean-Up-a-URDF-File>` 中的 URDF，并将其发布为 ``/robot_description`` 话题。
* 启动一个空的 Gazebo 世界。
* 运行脚本，从话题中读取 URDF 并在 Gazebo 中生成机器人模型。
* 默认情况下，还会显示 Gazebo GUI。

.. image:: https://raw.githubusercontent.com/ros/urdf_sim_tutorial/ros2/doc/NonFunctional.png
   :alt: Gazebo 中无法交互的机器人

不过，此时机器人还不能执行任何操作，因为它缺少 ROS 使用该机器人所需的关键信息。

在前面的 :doc:`URDF 可视化模型教程 <Building-a-Visual-Robot-Model-with-URDF-from-Scratch>` 和 :doc:`可运动机器人模型教程 <Building-a-Movable-Robot-Model-with-URDF>` 中，我们使用 ``joint_state_publisher`` 指定每个关节的位姿。

但在真实机器人或 Gazebo 仿真中，这些信息应该由机器人自身提供。如果没有指定相关信息，Gazebo 就不知道如何发布机器人状态。

为了让机器人能够与用户和 ROS 交互，需要配置两部分内容：插件（Plugins）和控制器（Controllers）。

补充说明：配置网格模型
^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/ros/urdf_sim_tutorial/ros2/doc/NoMesh.png
   :alt: 缺少网格模型的机器人

如果你使用自己的机器人模型，或者遇到其他异常，可能会发现 Gazebo GUI 中缺少部分网格模型，例如夹爪网格没有显示。

这也可能导致 Gazebo 在启动画面出现后需要等待数秒，因为它正在尝试通过互联网查找缺失的模型资源。

这是因为 URDF 所属功能包需要明确告诉 Gazebo 应该从哪里加载网格资源。可以通过修改存放 URDF 网格文件的功能包 ``package.xml``，添加一个新的 export 配置：

.. code-block:: xml

   <export>
     <build_type>ament_cmake</build_type>
     <gazebo_ros gazebo_model_path="DOLLAR{prefix}/.."/>
   </export>

``gazebo_model_path`` 属性采用该特定值的原因可参阅 `相关问题讨论 <https://github.com/ros-simulation/gazebo_ros_pkgs/issues/1500>`_。只要满足以下条件，该配置就可以正常工作：

* URDF 中的网格文件名使用 ``package://package_name/possible_folder/filename.ext`` 格式。
* 网格文件已经通过 CMake 安装到正确的 share 目录。

Gazebo 插件
-----------

为了让 ROS 2 与 Gazebo 交互，需要动态链接能够指示 Gazebo 如何工作的 ROS 库。从理论上讲，这种方式允许其他机器人操作系统以通用方式与 Gazebo 交互；实际使用中，这里连接的是 ROS。

具体来说，Gazebo 与 ROS 2 的交互通过链接 ROS 2 Control 库实现，并且需要在 URDF 中添加新的标签。

在 URDF 文件的 ``</robot>`` 结束标签之前添加：

.. code-block:: xml

   <ros2_control name="GazeboSystem" type="system">
     <hardware>
       <plugin>gazebo_ros2_control/GazeboSystem</plugin>
     </hardware>
     <joint name="head_swivel" />
   </ros2_control>

   <gazebo>
     <plugin filename="libgazebo_ros2_control.so" name="gazebo_ros2_control">
       <parameters>$(find urdf_sim_tutorial)/config/09a-minimal.yaml</parameters>
     </plugin>
   </gazebo>

.. note::

   * ``<gazebo>`` 和 ``<plugin>`` 标签的用法与 ROS 1 相同。
   * 最小示例至少需要指定一个关节才能正常工作，后续还会添加更多关节。

最小配置文件如下：

.. code-block:: yaml

   controller_manager:
     ros__parameters:
       update_rate: 100

可以在 `09a-minimal.urdf.xacro <https://github.com/ros/urdf_sim_tutorial/blob/ros2/urdf/09a-minimal.urdf.xacro>`_ 中查看完整配置，并运行：

.. code-block:: console

   $ ros2 launch urdf_sim_tutorial 09a-minimal.launch.py

该命令会启动 ``/controller_manager`` 节点，并提供 ``load_controller`` 服务，但还不能让机器人执行有用的交互操作。要实现这一点，需要在控制器 YAML 文件中指定更多信息。

生成控制器（Spawning Controllers）
----------------------------------

现在 ROS 与 Gazebo 已经连接，接下来需要指定希望在 Gazebo 中运行的 ROS 代码，这些代码统称为控制器（controllers）。

下面使用 `joints.yaml 配置文件 <https://github.com/ros/urdf_sim_tutorial/blob/ros2/config/joints.yaml>`_，创建第一个控制器：

.. code-block:: yaml

   controller_manager:
     ros__parameters:
       update_rate: 100
       use_sim_time: true

       joint_state_broadcaster:
         type: joint_state_broadcaster/JointStateBroadcaster

该控制器来自 ``joint_state_broadcaster`` 功能包，会直接从 Gazebo 获取机器人关节状态，并将其发布到 ROS。

在 `09-joints.launch.py <https://github.com/ros/urdf_sim_tutorial/blob/ros2/launch/09-joints.launch.py>`_ 中，还会通过 ``ExecuteProcess`` 添加一条 ``ros2 control`` 命令，用于启动该控制器。

可以尝试启动：

.. code-block:: console

   $ ros2 launch urdf_sim_tutorial 09-joints.launch.py

该命令会运行控制器，实际上也会向 ``/joint_states`` 话题发布消息，但消息内容为空：

.. code-block:: yaml

   header:
     stamp:
       sec: 13
       nanosec: 331000000
     frame_id: ''
   name: []
   position: []
   velocity: []
   effort: []

Gazebo 还需要更多关于关节的信息。

ROS 2 Control 关节定义
----------------------

对于每个非固定关节，都需要在 ``ros2_control`` 标签中添加关节信息，告诉 ROS 2 Control 该关节支持哪些接口。

先从头部关节开始。将 URDF 中的关节定义修改为：

.. code-block:: xml

   <joint name="head_swivel">
     <command_interface name="position" />
     <command_interface name="velocity" />
     <state_interface name="position"/>
     <state_interface name="velocity"/>
   </joint>

该修改可参阅 `URDF 对应片段 <https://github.com/ros/urdf_sim_tutorial/blob/ros2/urdf/10-firsttransmission.urdf.xacro#L241>`_。

需要注意：

* 这里的关节名称必须与标准 URDF ``<joint>`` 标签中的关节名称一致。
* 目前重点关注 ``state_interface``，它指定需要发布该关节的位置和速度。

可以使用前面的启动配置运行该 URDF：

.. code-block:: console

   $ ros2 launch urdf_sim_tutorial 09-joints.launch.py urdf_package_path:=urdf/10-firsttransmission.urdf.xacro

现在，头部应该能够在 RViz 中正确显示，因为 ``head_swivel`` 关节已经包含在 ``joint_states`` 消息中。

消息内容类似：

.. code-block:: yaml

   header:
     stamp:
       sec: 4
       nanosec: 707000000
     frame_id: ''
   name:
   - head_swivel
   position:
   - -2.9051283156888985e-08
   velocity:
   - 7.575990694887896e-06
   effort:
   - .nan

可以继续为所有非固定关节添加定义，使所有关节都能正确发布状态。

不过，机器人不仅需要被观察，还需要能够被控制。因此，接下来再添加一个控制器。

关节控制
--------

下面是即将添加的 `头部控制器配置 <https://github.com/ros/urdf_sim_tutorial/blob/ros2/config/head.yaml>`_：

.. code-block:: yaml

   controller_manager:
     ros__parameters:
       # ... 此处省略其他配置 ...

       head_controller:
         type: position_controllers/JointGroupPositionController

   head_controller:
     ros__parameters:
       joints:
         - head_swivel
       interface_name: position

这段配置表示创建一个名为 ``head_controller`` 的 ``JointGroupPositionController``，然后在新的参数命名空间中指定该控制器包含哪些关节，以及使用哪种接口发布数据。

之所以能够使用位置控制，是因为前面已经在关节定义中指定了 ``<command_interface name="position" />``。

现在可以使用新增的配置文件和另一条 ``ros2 control`` 命令启动：

.. code-block:: console

   $ ros2 launch urdf_sim_tutorial 10-head.launch.py

此时 Gazebo 会订阅一个新的话题。向该话题发布数值，就可以控制头部位置：

.. code-block:: console

   $ ros2 topic pub /head_controller/commands std_msgs/msg/Float64MultiArray "data: [-0.707]"

发布该命令后，头部位置会立即改变为指定值。

控制多个关节和关节模仿
----------------------

可以用类似的方法修改夹爪关节的 URDF 定义，但这次会将多个关节关联到同一个控制器。

更新后的 ROS 参数配置可参阅 `gripper.yaml <https://github.com/ros/urdf_sim_tutorial/blob/ros2/config/gripper.yaml>`_。还需要更新 `URDF 文件 <https://github.com/ros/urdf_sim_tutorial/blob/ros2/urdf/12-gripper.urdf.xacro>`_，为三个额外关节添加接口定义。

启动：

.. code-block:: console

   $ ros2 launch urdf_sim_tutorial 12-gripper.launch.py

现在可以通过包含三个浮点数的数组控制夹爪。

打开并伸出：

.. code-block:: console

   $ ros2 topic pub /gripper_controller/commands std_msgs/msg/Float64MultiArray "data: [0.0, 0.5, 0.5]"

闭合并收回：

.. code-block:: console

   $ ros2 topic pub /gripper_controller/commands std_msgs/msg/Float64MultiArray "data: [-0.4, 0.0, 0.0]"

该夹爪的设计要求左夹爪关节始终与右夹爪关节保持相同的值。可以通过以下步骤在 URDF 和控制器中实现这一点：

* 在 URDF 中 ``right_gripper_joint`` 的定义中插入 ``<mimic joint="left_gripper_joint"/>``。具体修改可参阅 `对应 Xacro 文件 <https://github.com/ros/urdf_sim_tutorial/blob/ros2/urdf/12a-mimic-gripper.urdf.xacro>`_。
* 在 ``right_gripper_joint`` 的 ``ros2_control`` 关节接口中插入 ``<param name="mimic">left_gripper_joint</param>``。
* 在新的 `控制参数配置 <https://github.com/ros/urdf_sim_tutorial/blob/ros2/config/mimic-gripper.urdf>`_ 中，夹爪控制器只列出两个关节，不再单独列出 ``right_gripper_joint``。

使用以下命令启动：

.. code-block:: console

   $ ros2 launch urdf_sim_tutorial 12-gripper.launch.py urdf_package_path:=urdf/12a-mimic-gripper.urdf.xacro

现在只需要两个数值就可以控制夹爪，例如：

.. code-block:: console

   $ ros2 topic pub /gripper_controller/commands std_msgs/msg/Float64MultiArray "data: [0.0, 0.5]"

机器人车轮转起来
----------------

要驱动机器人移动，首先需要为 URDF 中的四个车轮分别在 ``ros2_control`` 标签中指定更多接口。不过，这次只需要速度命令接口。

可以为每个车轮单独指定控制器，但更方便的方式是同时控制所有车轮。

为此，需要使用更多 ROS 参数配置 `DiffDriveController <https://github.com/ros/urdf_sim_tutorial/blob/ros2/config/diffdrive.yaml>`_。该控制器订阅标准的 Twist ``cmd_vel`` 消息，并根据消息内容驱动机器人。

四个车轮的 URDF 接口定义可参阅 `差速驱动 URDF <https://github.com/ros/urdf_sim_tutorial/blob/ros2/urdf/13-diffdrive.urdf.xacro>`_。

启动：

.. code-block:: console

   $ ros2 launch urdf_sim_tutorial 13-diffdrive.launch.py

除了加载上述配置，该启动文件还会打开 ``RobotSteering`` 面板。通过该面板可以驾驶 R2D2 机器人，同时观察它在 Gazebo 中的实际运动，以及在 RViz 中的可视化结果：

.. image:: https://raw.githubusercontent.com/ros/urdf_sim_tutorial/ros2/doc/DrivingInterface.png
   :alt: Gazebo 驾驶控制界面

恭喜！现在已经可以使用 URDF 在 Gazebo 中仿真机器人了。
