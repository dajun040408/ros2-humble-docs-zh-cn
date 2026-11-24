定义 MVSim 世界、机器人和传感器
===============================

**目标：** 学习 MVSim 世界文件的基本结构、如何添加车辆和传感器，以及主要可用功能。

**教程级别：** 高级

**预计时间：** 30 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

MVSim 世界通过 XML 文件（.world.xml）定义。世界文件描述环境（地面、墙壁、障碍物）、车辆（动力学模型、形状、传感器）以及仿真参数（物理时间步长、GUI 选项）。

MVSim 提供预定义车辆和传感器定义库，可以通过 XML include 在世界文件中复用。也可以从头定义所有内容，以获得完整控制。

前置条件
--------

请先完成 :doc:`MVSim 入门教程 <Getting-Started-MVSim>` 并安装 MVSim。

任务
----

1. 最小世界文件
^^^^^^^^^^^^^^^

下面是一个最小世界文件，它创建一个空环境并放置一台机器人：

.. code-block:: xml

    <mvsim_world version="1.0">
      <!-- 仿真设置 -->
      <simul_timestep>5e-3</simul_timestep>

      <!-- GUI 选项 -->
      <gui>
          <cam_distance>15</cam_distance>
      </gui>

      <!-- 地面 -->
      <element class="ground_grid">
      </element>

      <!-- 差速驱动机器人 -->
      <vehicle name="robot1">
        <init_pose>0 0 0</init_pose>  <!-- x y yaw(deg) -->

        <!-- 动力学模型 -->
        <dynamics class="differential">
            <l_wheel pos="0.0  0.5" mass="4.0" width="0.20" diameter="0.40" />
            <r_wheel pos="0.0 -0.5" mass="4.0" width="0.20" diameter="0.40" />
            <chassis mass="15.0" zmin="0.05" zmax="0.6">
            </chassis>
            <controller class="twist_pid">
                <KP>4.1543</KP>
                <KI>1.9118</KI>
                <KD>0.0000</KD>
                <max_torque>14.44</max_torque>
                <V>0.0</V><W>0</W>
            </controller>
        </dynamics>
      </vehicle>
    </mvsim_world>

将其保存为 my_world.world.xml 并启动：

.. code-block:: console

    $ mvsim launch my_world.world.xml

2. 使用预定义车辆和传感器
^^^^^^^^^^^^^^^^^^^^^^^^^

不必从头定义车辆，也可以使用 MVSim 自带的预定义定义文件。这些 XML 文件位于 MVSim 软件包的 definitions/ 目录中。

**可用车辆：**

* turtlebot3_burger.vehicle.xml：TurtleBot3 Burger（差速驱动）。
* jackal.vehicle.xml：Clearpath Jackal UGV（四轮差速）。
* ackermann.vehicle.xml：通用 Ackermann 汽车式车辆。
* pickup.vehicle.xml：皮卡车（Ackermann）。
* agricobiot2.vehicle.xml：农业机器人（Ackermann 传动系统）。

**可用传感器：**

* lidar2d.sensor.xml：通用 2D 激光扫描仪。
* rplidar-a2.sensor.xml：RPLidar A2。
* velodyne-vlp16.sensor.xml：Velodyne VLP-16 3D LiDAR。
* ouster-os1.sensor.xml：Ouster OS1 3D LiDAR。
* helios-32-FOV-70.sensor.xml：Helios 32 线 3D LiDAR。
* camera.sensor.xml：RGB 摄像头。
* rgbd_camera.sensor.xml：深度摄像头（RGBD）。
* imu.sensor.xml：惯性测量单元。
* gnss.sensor.xml：GPS/GNSS 接收机。

要使用带传感器的预定义车辆，可以通过 XML include 引入定义：

.. code-block:: xml

    <mvsim_world version="1.0">
      <simul_timestep>5e-3</simul_timestep>
      <gui>
          <cam_distance>15</cam_distance>
      </gui>
      <element class="ground_grid">
      </element>

      <!-- 引入 Jackal 车辆定义 -->
      <include file="$(ros2 pkg prefix mvsim)/share/mvsim/definitions/jackal.vehicle.xml"
        default_sensors="true"
        />

      <vehicle name="r1" class="jackal">
        <init_pose>0 0 170</init_pose>
        <init_vel>0 0 0</init_vel>
      </vehicle>
    </mvsim_world>

也可以通过单独的 include 为车辆添加传感器，或直接在 vehicle 块中定义传感器。
