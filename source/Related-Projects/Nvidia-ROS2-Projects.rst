NVIDIA ROS 2 项目
=================

NVIDIA 提供用于开发机器人 AI 应用的多个软件包和项目。

ISAAC ROS 项目
--------------

* `预构建 ROS 2 Humble 支持 <https://nvidia-isaac-ros.github.io/getting_started/isaac_ros_buildfarm_cdn.html>`_：NVIDIA 构建农场提供的预构建 Debian 软件包，支持 Ubuntu 20.04 上的 ROS 2 Humble，可用于 Jetson 和其他 aarch64 平台。
* `CUDA 与 NITROS <https://nvidia-isaac-ros.github.io/concepts/nitros/cuda_with_nitros.html>`_：帮助用户开发支持 CUDA 的自定义节点，并与 Isaac ROS 的 NITROS 配合使用。NITROS 是一种类型适配和类型协商实现，可在 ROS 2 中实现加速计算。
* `Isaac ROS NITROS Bridge <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nitros_bridge>`_：用于将 Isaac ROS 软件包与现有 ROS 1 应用程序进行优化集成的 NITROS 桥接程序。可用于将 ROS 应用程序桥接到 ROS 2，实现加速计算；与传统 ROS bridge 相比，速度提升超过 2 倍。
* `Nova Carter <https://nvidia-isaac-ros.github.io/robots/nova_carter.html>`_：面向机器人开发和研究的参考 AMR 平台，由 Isaac ROS 和 Nav2 驱动，并通过 Open Navigation 调优，支持远程操作、建图和导航。
* `Isaac ROS Nova <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nova>`_：提供一组经过优化的软件包，用于连接 Isaac Nova Orin 传感器套件。
* `Isaac ROS Pose Estimation <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_pose_estimation>`_：包含用于预测物体位姿的 ROS 2 软件包。
* `ROS2_Benchmark <https://github.com/NVIDIA-ISAAC-ROS/ros2_benchmark>`_：提供工具，用于在不修改被测代码的情况下，测量复杂计算图的吞吐量、延迟和计算资源利用率。
* `Isaac ROS Benchmark <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_benchmark>`_：基于 ros2_benchmark 构建，为 Isaac ROS 计算图提供基准测试配置。
* `Isaac ROS Map Localization <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_map_localization>`_：包含用于激光雷达处理的 ROS 2 软件包，可估计相对于地图的位姿。占据栅格定位器处理平面激光扫描数据，在占据栅格地图中估计位姿；对于大多数地图，该过程可在 1 秒内完成。
* `Isaac ROS NITROS <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nitros>`_：面向硬件加速消息传输的 ROS 软件包。
* `Isaac ROS Compression <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_compression>`_：使用硬件加速 NITROS 软件包压缩摄像头数据采集和回放，以支持 AI 模型和感知功能开发。可压缩 4 路 1080p、30 fps 摄像头数据（总计超过 120 fps），并将数据占用量降低约 10 倍。
* `Isaac ROS DNN Stereo Depth <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_dnn_stereo_depth>`_：包含用于预测双目输入视差的 DNN Stereo Disparity 软件包。
* `Isaac ROS Depth Segmentation <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_depth_segmentation>`_：用于深度分割的硬件加速软件包。
* `Isaac ROS Nvblox <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox>`_：用于三维场景重建，并通过 nvblox 为 Nav2 提供局部代价地图。
* `Isaac ROS Object Detection <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_object_detection>`_：支持包括 DetectNet 在内的深度学习物体检测模型。
* `Isaac ROS DNN Inference <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_dnn_inference>`_：提供两个由 NVIDIA GPU 加速的 ROS 2 节点，使用自定义模型执行深度学习推理。其中一个节点使用 TensorRT SDK，另一个使用 Triton SDK。
* `Isaac ROS Visual SLAM <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam>`_：提供 ROS 2 软件包，使用 Isaac Elbrus GPU 加速库估计双目视觉惯性里程计。
* `Isaac ROS Mission Client <http://github.com/NVIDIA-ISAAC-ROS/isaac_ros_mission_client>`_：接收来自 ROS 的状态和错误更新，并将其转换为 VDA5050 JSON 消息，供 ROS 2 到 MQTT 节点发送给任务调度系统。
* `Isaac ROS Argus Camera <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_argus_camera>`_：提供单目和双目节点，使 ROS 开发者能够通过 CSI 接口使用连接到 Jetson 平台的摄像头。
* `Isaac ROS Image Pipeline <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_image_pipeline>`_：该元功能包提供与标准 CPU 版 image_pipeline 元功能包类似的功能，但利用 Jetson 平台专用计算机视觉硬件实现处理。
* `Isaac ROS Common <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common>`_：与 Isaac ROS 软件包套件配合使用的通用工具。
* `Isaac ROS AprilTag <https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_apriltag>`_：使用 NVIDIA GPU 加速的 AprilTags 库检测图像中的 AprilTag，并发布其位姿、ID 和其他元数据。

其他项目
--------

* `ROS 和 ROS 2 DockerFiles <https://github.com/dusty-nv/jetson-containers>`_：基于 L4T 的 ROS 2 Dockerfile，可用于构建自己的 Docker 镜像。
* `用于加速深度学习节点的 ROS/ROS 2 软件包 <https://github.com/dusty-nv/ros_deep_learning>`_：基于 `jetson-inference <https://github.com/dusty-nv/jetson-inference>`_ 库和 `NVIDIA Hello AI World 教程 <https://developer.nvidia.com/embedded/twodaysToDemo>`_，提供深度学习图像识别、物体检测、语义分割推理节点，以及摄像头/视频流节点。

仿真项目
--------

* `Isaac Sim Nav2 <https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/tutorial_ros2_navigation.html>`_：该 ROS 2 示例展示 Omniverse Isaac Sim 与 ROS 2 Nav2 项目的集成。
* `Isaac Sim 多机器人 ROS 2 导航 <https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/tutorial_ros2_multi_navigation.html>`_：该 ROS 2 示例展示 Omniverse Isaac Sim 与 ROS 2 Nav2 导航栈的集成，并实现多机器人同时导航。
