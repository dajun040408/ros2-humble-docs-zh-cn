* 贡献者：Chris Lalancette、Jacob Perron、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tf2_geometry_msgs <https://github.com/ros2/geometry2/tree/humble/tf2_geometry_msgs/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 确保找到正确的 Python 可执行文件（`#514 <https://github.com/ros2/geometry2/issues/514>`__）
* 依赖 orocos_kdl_vendor（`#473 <https://github.com/ros2/geometry2/issues/473>`__）
* 将头文件安装到 include/${PROJECT_NAME} 并使用现代 CMake（`#493 <https://github.com/ros2/geometry2/issues/493>`__）
* 移除 tf2_geometry_msgs 对 PyKDL 的依赖（`#509 <https://github.com/ros2/geometry2/issues/509>`__）
* 修复 cpplint 错误（`#497 <https://github.com/ros2/geometry2/issues/497>`__）
* 导出 tf2_geometry_msgs::tf2_geometry_msgs target（`#496 <https://github.com/ros2/geometry2/issues/496>`__）
* 功能：为 Wrench 消息添加 doTransform（`#476 <https://github.com/ros2/geometry2/issues/476>`__）
* 移除部分 ROS 1 wiki 引用
* 修复 tf2_geometry_msgs 中的代码风格问题（`#464 <https://github.com/ros2/geometry2/issues/464>`__）
* 修复问题 `#431 <https://github.com/ros2/geometry2/issues/431>`__：do_transform_pose_with_covariance_stamped 未对协方差进行变换（`#453 <https://github.com/ros2/geometry2/issues/453>`__）
* 为非 stamped 消息实现 doTransform（`#452 <https://github.com/ros2/geometry2/issues/452>`__）
* ``tf2_geometry_msgs``：修复 ``doTransform<PoseWithCovarianceStamped, TransformStamped>`` 中的协方差变换（`#430 <https://github.com/ros2/geometry2/issues/430>`__）
* 修正 Geometry 相关细节（`#426 <https://github.com/ros2/geometry2/issues/426>`__）
* 为 toMsg() 添加转换测试（`#423 <https://github.com/ros2/geometry2/issues/423>`__）
* 弃用 tf2_geometry_msgs.h（`#418 <https://github.com/ros2/geometry2/issues/418>`__）
* 贡献者：Abrar Rahman Protyasha、Bjar Ne、Chris Lalancette、Denis Štogl、Florian Vahl、Jacob Perron、Khasreto、Shane Loretz、vineet131


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tf2_kdl <https://github.com/ros2/geometry2/tree/humble/tf2_kdl/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 依赖 orocos_kdl_vendor（`#473 <https://github.com/ros2/geometry2/issues/473>`__）
* 将头文件安装到 include/${PROJECT_NAME} 并使用现代 CMake（`#493 <https://github.com/ros2/geometry2/issues/493>`__）
* KDL Python 格式调整和许可证更新（`#425 <https://github.com/ros2/geometry2/issues/425>`__）
* 弃用 tf2_kdl.h（`#414 <https://github.com/ros2/geometry2/issues/414>`__）
* 贡献者：Bjar Ne、Chris Lalancette、Jacob Perron、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tf2_msgs <https://github.com/ros2/geometry2/tree/humble/tf2_msgs/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 从 tf2_msgs 中移除无用文件（`#415 <https://github.com/ros2/geometry2/issues/415>`__）
* 贡献者：Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tf2_py <https://github.com/ros2/geometry2/tree/humble/tf2_py/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 确保正确完成 tf2_py BufferCore 的清理（`#505 <https://github.com/ros2/geometry2/issues/505>`__）
* 使 tf2_py 使用 FindPython3（`#494 <https://github.com/ros2/geometry2/issues/494>`__）
* 使 TF2Error 名称更具描述性（`#349 <https://github.com/ros2/geometry2/issues/349>`__）
* 移除 python_compat.h（`#417 <https://github.com/ros2/geometry2/issues/417>`__）
* 贡献者：Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tf2_ros <https://github.com/ros2/geometry2/tree/humble/tf2_ros/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME} 并使用现代 CMake（`#493 <https://github.com/ros2/geometry2/issues/493>`__）
* 使用专用 callback group 和 executor 隔离定时器（`#447 <https://github.com/ros2/geometry2/issues/447>`__）
* 为 tf2 buffer 添加 shared pointer 定义（`#508 <https://github.com/ros2/geometry2/issues/508>`__）
* 修复基础逻辑问题（`#510 <https://github.com/ros2/geometry2/issues/510>`__）
* 修复使用 rclcpp::Time::seconds() 导致的精度损失（`#511 <https://github.com/ros2/geometry2/issues/511>`__）
* MessageFilter 销毁时，清除 Buffer 的相对 callback（`#490 <https://github.com/ros2/geometry2/issues/490>`__）
* 在 tf2_echo 输出中提供更多信息（`#468 <https://github.com/ros2/geometry2/issues/468>`__）
* 修复 cpplint 错误（`#497 <https://github.com/ros2/geometry2/issues/497>`__）
* 修复与 uncrustify 0.72 的兼容问题（`#486 <https://github.com/ros2/geometry2/issues/486>`__）
* 改进静态变换发布器的命令行接口，使其更直观（`#392 <https://github.com/ros2/geometry2/issues/392>`__）
* 减少 transform listener 节点数量（`#442 <https://github.com/ros2/geometry2/issues/442>`__）
* ``tf2_ros``：修复已弃用订阅回调的警告（`#448 <https://github.com/ros2/geometry2/issues/448>`__）
* 修复 tf2_echo 无法与 ros-args 配合工作的问题（`#407 <https://github.com/ros2/geometry2/issues/407>`__）（`#408 <https://github.com/ros2/geometry2/issues/408>`__）
* 贡献者：Abrar Rahman Protyasha、Chen Lihui、Chris Lalancette、Hunter L. Allen、Jacob Perron、Kenji Brameld、PGotzmann、Shane Loretz、Steve Macenski、Zhenpeng Ge、gezp、simulacrus


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tf2_ros_py <https://github.com/ros2/geometry2/tree/humble/tf2_ros_py/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 tf2_geometry_msgs 对 PyKDL 的依赖（`#509 <https://github.com/ros2/geometry2/issues/509>`__）
* 补充一个测试中遗漏的 destroy 调用（`#504 <https://github.com/ros2/geometry2/issues/504>`__）
* 更谨慎地清理 tf2_ros_py 测试中的资源（`#499 <https://github.com/ros2/geometry2/issues/499>`__）
* 为 BufferClient.timeout_padding 使用正确的类型（`#498 <https://github.com/ros2/geometry2/issues/498>`__）：该值应为 duration，而不是 float。
* 将维护者更新为 Alejandro Hernandez Cordero 和 Chris Lalancette（`#481 <https://github.com/ros2/geometry2/issues/481>`__）
* 修复 buffer_client.py 使用默认 timeout_padding 的问题（`#437 <https://github.com/ros2/geometry2/issues/437>`__）
* 在 setup.cfg 中使用下划线，而不是连字符（`#403 <https://github.com/ros2/geometry2/issues/403>`__）
* 贡献者：Audrow Nash、Carlos Andrés Álvarez Restrepo、Chris Lalancette、Florian Vahl


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tf2_sensor_msgs <https://github.com/ros2/geometry2/tree/humble/tf2_sensor_msgs/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 在 aarch64 上禁用内存访问警告（`#506 <https://github.com/ros2/geometry2/issues/506>`__）
* 修复 cpplint 错误（`#497 <https://github.com/ros2/geometry2/issues/497>`__）
* 重新启用 sensor_msgs 测试（`#422 <https://github.com/ros2/geometry2/issues/422>`__）
* 弃用 tf2_sensor_msgs.h（`#416 <https://github.com/ros2/geometry2/issues/416>`__）
* 贡献者：Bjar Ne、Chris Lalancette、Jacob Perron


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tf2_tools <https://github.com/ros2/geometry2/tree/humble/tf2_tools/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Alejandro Hernandez Cordero 和 Chris Lalancette（`#481 <https://github.com/ros2/geometry2/issues/481>`__）
* 移除未使用的 import（`#465 <https://github.com/ros2/geometry2/issues/465>`__）
* 在 frames 文件名中添加日期时间（`#454 <https://github.com/ros2/geometry2/issues/454>`__）
* 在 setup.cfg 中使用下划线，而不是连字符（`#403 <https://github.com/ros2/geometry2/issues/403>`__）
* 贡献者：Audrow Nash、Hannu Henttinen、Nisala Kalupahana


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tlsf <https://github.com/ros2/tlsf/tree/humble/tlsf/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}（`#11 <https://github.com/ros2/tlsf/issues/11>`__）
* 导出现代 CMake target，替代旧式变量（`#10 <https://github.com/ros2/tlsf/issues/10>`__）
* 贡献者：Shane Loretz
