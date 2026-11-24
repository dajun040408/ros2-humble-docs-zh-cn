在 Gazebo 中使用 URDF
=====================

**目标：** 在 Gazebo 仿真器中仿真 URDF 模型。

**教程级别：** 中级 | **预计时间：** 30 分钟

.. contents:: 目录
   :depth: 2
   :local:

安装演示功能包
--------------

.. tabs::

   .. group-tab:: Ubuntu 软件包

      .. code-block:: console

         sudo apt install ros-{DISTRO}-urdf-sim-tutorial

   .. group-tab:: RHEL 软件包

      .. code-block:: console

         sudo dnf install ros-{DISTRO}-urdf-sim-tutorial

   .. group-tab:: 源码安装

      .. code-block:: console

         git clone https://github.com/ros/urdf_sim_tutorial.git -b ros2

加载模型
--------

使用 ``gazebo.launch.py`` 将此前创建的模型加载到 Gazebo：

.. code-block:: console

  ros2 launch urdf_sim_tutorial gazebo.launch.py

该启动文件会加载 :doc:`Xacro 教程 <Using-Xacro-to-Clean-Up-a-URDF-File>` 中的 URDF，并将其发布为 ``/robot_description`` 话题；启动空 Gazebo 世界；运行脚本从话题读取 URDF 并生成模型；默认显示 Gazebo GUI。

.. image:: https://raw.githubusercontent.com/ros/urdf_sim_tutorial/ros2/doc/NonFunctional.png
  :alt: Gazebo 中无法交互的机器人

此时机器人无法执行任何操作，因为缺少 ROS 使用机器人所需的关键信息。此前教程使用 ``joint_state_publisher`` 指定关节位姿，但在真实机器人或 Gazebo 中，这些信息应由机器人本身提供。

要让机器人能够与用户和 ROS 交互，需要配置插件和控制器。

配置网格模型
------------

如果 Gazebo GUI 中缺少网格模型，可能是 URDF 功能包没有明确告诉 Gazebo 从哪里加载网格。可以在存放 URDF 网格的功能包 ``package.xml`` 中添加 export：

.. code-block:: xml

   <export>
     <build_type>ament_cmake</build_type>
     <gazebo_ros gazebo_model_path="${prefix}/.."/>
   </export>

该配置假设 URDF 中的网格文件名使用 ``package://package_name/possible_folder/filename.ext`` 格式，并且网格已通过 CMake 安装到正确的 share 目录。

Gazebo 插件
-----------

ROS 2 与 Gazebo 的交互通过 ROS 2 Control 库实现，并在 URDF 中添加相应标签。在 ``</robot>`` 结束标签之前添加：

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
   * 最小示例至少需要指定一个关节，后续可以添加更多关节和控制器配置。

总结
----

本教程介绍了如何将 URDF 模型加载到 Gazebo，以及为什么仅有视觉模型不足以进行仿真。要实现交互，需要配置网格资源路径、Gazebo 插件、ROS 2 Control 硬件接口和控制器。
