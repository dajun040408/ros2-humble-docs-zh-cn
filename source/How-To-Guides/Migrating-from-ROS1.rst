从 ROS 1 迁移到 ROS 2
======================

这些指南介绍如何将现有 ROS 1 功能包转换为 ROS 2。如果你刚开始接触 ROS 1 到 ROS 2 的移植工作，建议按照页面顺序阅读这些指南。

.. toctree::
   :maxdepth: 1

   功能包迁移 <Migrating-from-ROS1/Migrating-Packages>
   将 package.xml 迁移到格式 2 <Migrating-from-ROS1/Migrating-Package-XML>
   接口迁移 <Migrating-from-ROS1/Migrating-Interfaces>
   C++ 功能包迁移示例 <Migrating-from-ROS1/Migrating-CPP-Package-Example>
   C++ 功能包迁移参考 <Migrating-from-ROS1/Migrating-CPP-Packages>
   Python 功能包迁移示例 <Migrating-from-ROS1/Migrating-Python-Package-Example>
   Python 功能包迁移参考 <Migrating-from-ROS1/Migrating-Python-Packages>
   Launch 文件迁移 <Migrating-from-ROS1/Migrating-Launch-Files>
   参数迁移 <Migrating-from-ROS1/Migrating-Parameters>
   脚本迁移 <Migrating-from-ROS1/Migrating-Scripts>

自动化工具
----------

目前也存在一些自动转换工具，但它们并不能覆盖所有迁移场景：

* `Magical ROS 2 Conversion Tool <https://github.com/DLu/roscompile/tree/main/magical_ros2_conversion_tool>`__
* Launch 文件迁移工具：将 ROS 1 XML launch 文件转换为 ROS 2 Python launch 文件，参见 `ros2-launch-file-migrator <https://github.com/aws-robotics/ros2-launch-file-migrator>`__。
* Amazon 已公开其 ROS 1 到 ROS 2 移植工具，参见 `ros2-migration-tools/porting_tools <https://github.com/awslabs/ros2-migration-tools/tree/master/porting_tools>`__。
* `rospy2 <https://github.com/dheera/rospy2>`__：一个 Python 项目，用于自动将 rospy 调用转换为 rclpy 调用。
