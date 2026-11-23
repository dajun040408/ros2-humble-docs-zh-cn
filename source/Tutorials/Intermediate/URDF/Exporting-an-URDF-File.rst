生成 URDF 文件
===============

**目标：** 学习如何导出 URDF 文件。

**教程级别：** 中级

**预计时间：** 5 分钟

.. contents:: 目录
   :depth: 2
   :local:

大多数机器人开发者都在团队中工作，而团队中通常会有机械工程师负责开发机器人的 CAD 模型。与手工编写 URDF 不同，许多 CAD 和建模软件都支持直接导出 URDF 模型。

这些导出工具通常由熟悉相应 CAD 软件的个人开发者维护。下面列出了适用于多种 CAD 和三维建模软件的 URDF 导出工具。

*ROS 核心维护团队不负责维护这些软件包，因此我们不对其性能或易用性作出保证。* 但我们认为，整理一份可用 URDF 导出工具列表会对用户有所帮助。

**CAD 导出工具**

* `Blender URDF Exporter <https://github.com/dfki-ric/phobos>`_
* `CREO Parametric URDF Exporter <https://github.com/icub-tech-iit/creo2urdf>`_
* `FreeCAD ROS Workbench <https://github.com/galou/freecad.cross>`_
* `RobotCAD（FreeCAD OVERCROSS）<https://github.com/drfenixion/freecad.overcross>`_
* `FreeCAD to Gazebo Exporter <https://github.com/Dave-Elec/freecad_to_gazebo>`_
* `Fusion 360 URDF Exporter <https://github.com/dheena2k2/fusion2urdf-ros2>`_
* `fusion2URDF（Fusion 360、ros2_control、闭环）<https://github.com/Adriaeik/fusion2URDF>`_
* `FusionSDF：Fusion 360 到 SDF 导出工具 <https://github.com/andreasBihlmaier/FusionSDF>`_
* `OnShape URDF Exporter <https://github.com/Rhoban/onshape-to-robot>`_
* `SolidWorks URDF Exporter <https://github.com/ros/solidworks_urdf_exporter>`_
* `sw2robot（基于 SolidWorks mate 的导出工具和跨平台 URDF 编辑器）<https://github.com/jsk-ros-pkg/solidworks_urdf_exporter2>`_
* `ExportURDF Library（Fusion360、OnShape、Solidworks）<https://github.com/daviddorf2023/ExportURDF>`_

**其他 URDF 导出和转换工具**

* `Gazebo SDFormat to URDF Parser <https://github.com/ros/sdformat_urdf>`_
* `Python SDF to URDF Converter <https://github.com/andreasBihlmaier/pysdf>`_
* `URDF to Webots Simulator Format <https://github.com/cyberbotics/urdf2webots>`_
* `Blender Robotics Tools <https://github.com/robotology/blender-robotics-utils/>`_ 仓库包含多种实用工具，其中包括 `从 Blender 导出 URDF 文件 <https://github.com/robotology/blender-robotics-utils/tree/master?tab=readme-ov-file#urdftoblender>`_。
* `CoppeliaSim URDF Exporter <https://manual.coppeliarobotics.com/en/importExport.htm#urdf>`_
* `Isaac Sim URDF Exporter <https://docs.omniverse.nvidia.com/isaacsim/latest/advanced_tutorials/tutorial_advanced_export_urdf.html>`_
* `ProtoJoint（基于浏览器的 CAD，可导出 URDF、MJCF 和 ROS 2 软件包）<https://protojoint.ai/cad-to-urdf/>`_

**URDF 和 SDF 文件查看工具**

* `常见 URDF 启动文件示例 <https://github.com/ros/urdf_launch>`_
* URDF 文件 Web 查看器：`GitHub 仓库 <https://github.com/gkjohnson/urdf-loaders/>`_ 和 `在线网站 <https://gkjohnson.github.io/urdf-loaders/javascript/example/bundle/index.html>`_。
* `在 RViz 中查看 SDF 模型 <https://github.com/Yadunund/view_sdf_rviz>`_
* `Jupyterlab URDF Viewer <https://github.com/IsabelParedes/jupyterlab-urdf>`_

如果你有喜欢的 URDF 工具，也欢迎将其添加到上面的列表中！
