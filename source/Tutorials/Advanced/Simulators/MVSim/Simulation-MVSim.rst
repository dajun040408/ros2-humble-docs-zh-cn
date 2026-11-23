MVSim 仿真
==========

本组教程将介绍如何配置 `MVSim <https://mvsimulator.readthedocs.io/>`_ 仿真器，使其与 ROS 2 配合使用。

MVSim 是一款轻量级开源多车辆仿真器，专注于移动机器人的 2D/3D 可视化。它使用 Box2D 实现二维刚体物理，并提供真实的车辆动力学模型（差速驱动、阿克曼转向）、传感器仿真（二维/三维激光雷达、摄像头、IMU、GPS）以及原生 ROS 2 集成。MVSim 尤其适合用于导航、SLAM 和多机器人协同场景测试，同时具有计算开销低、迭代速度快等特点。

.. contents:: 目录
   :depth: 2
   :local:

.. toctree::
   :maxdepth: 1

   Installation-Ubuntu
   Getting-Started-MVSim
   Defining-Worlds-MVSim
