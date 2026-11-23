.. redirect-from::

  Intel-ROS2-Projects

Intel ROS 2 项目
================

Intel® Robotics Open Source Project（Intel® ROS Project）利用 Intel 的多种技术和平台，支持物体检测、定位与跟踪、人员检测、车辆检测，以及工业机械臂抓取点分析。这些技术和平台包括 CPU、GPU、针对深度学习后端优化的 `Intel® Movidius™ NCS <https://www.intel.com/content/www/us/en/developer/tools/neural-compute-stick/overview.html>`_、FPGA、`Intel® RealSense™ 摄像头 <https://www.intel.com/content/www/us/en/architecture-and-technology/realsense-overview.html>`_ 等。

重点项目
--------

我们正在开展以下 ROS 2 项目，并逐步通过 `Intel GitHub 组织 <https://github.com/intel/>`_ 或 ROS 2 GitHub 仓库发布源代码。

* `ROS2 OpenVINO <https://github.com/intel/ros2_openvino_toolkit>`_：Intel® Visual Inference and Neural Network Optimization Toolkit 的 ROS 2 软件包，用于开发跨平台计算机视觉解决方案。
* `ROS2 RealSense Camera <https://github.com/IntelRealSense/realsense-ros>`_：适用于 Intel® RealSense™ D400 系列摄像头的 ROS 2 软件包。
* `ROS2 Movidius NCS <https://github.com/intel/ros2_intel_movidius_ncs>`_：使用 Intel® Movidius™ Neural Computing Stick（NCS）进行物体检测的 ROS 2 软件包。
* `ROS2 Object Messages <https://github.com/intel/ros2_object_msgs>`_：用于描述物体的 ROS 2 消息。
* `ROS2 Object Analytics <https://github.com/intel/ros2_object_analytics>`_：用于物体检测、跟踪以及二维/三维定位的 ROS 2 软件包。
* `ROS2 Message Filters <https://github.com/ros2/message_filters>`_：用于基于时间戳进行消息同步的 ROS 2 软件包。
* `ROS2 CV Bridge <https://github.com/ros-perception/vision_opencv/tree/ros2/cv_bridge>`_：用于与 OpenCV 桥接的 ROS 2 软件包。
* `ROS2 Object Map <https://github.com/intel/ros2_object_map>`_：基于 ROS 2 Object Analytics 提供的信息，在 SLAM 地图上标记物体标签的 ROS 2 软件包。
* `ROS2 Moving Object <https://github.com/intel/ros2_moving_object>`_：基于 ROS 2 Object Analytics 提供的信息，输出物体运动信息（例如物体在 x、y、z 轴上的速度）的 ROS 2 软件包。
* `ROS2 Grasp Library <https://github.com/intel/ros2_grasp_library>`_：用于抓取位置分析的 ROS 2 软件包，并兼容 `MoveIt <https://github.com/ros-planning/moveit2.git>`_ 抓取接口。
* `ROS2 Navigation <https://github.com/ros-planning/navigation2>`_：用于机器人导航的 ROS 2 软件包，已集成到 ROS 2 Crystal 发行版中。
* `Intel Robot DevKit（SDK）<https://github.com/intel/robot_devkit>`_：一个开源项目，使开发者能够轻松、高效地为基于 ROS 2 框架的自主移动机器人（AMR）平台创建、定制、优化和部署机器人软件栈。

参考资料
--------

`ROS 组件 <https://wiki.ros.org/IntelROSProject>`_ 页面展示了这些软件包之间的关系，该关系同样适用于 ROS 2。
