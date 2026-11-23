* 贡献者：Aditya Pande、Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`test_communication <https://github.com/ros2/system_tests/tree/humble/test_communication/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将 test_subscriber 拆分为多个编译单元（`#500 <https://github.com/ros2/system_tests/issues/500>`__）
* 添加 test_msgs 依赖（`#497 <https://github.com/ros2/system_tests/issues/497>`__）
* 更新 Python 节点对 SIGINT 的处理（`#490 <https://github.com/ros2/system_tests/issues/490>`__）
* 更新维护者信息（`#489 <https://github.com/ros2/system_tests/issues/489>`__）
* 修复已弃用订阅回调的警告（`#483 <https://github.com/ros2/system_tests/issues/483>`__）
* 为 BoundedPlainSequences 添加测试（`#481 <https://github.com/ros2/system_tests/issues/481>`__）
* 使用 rosidl_get_typesupport_target()（`#480 <https://github.com/ros2/system_tests/issues/480>`__）
* 使用 rcpputils/scope_exit.hpp 替代 rclcpp/scope_exit.hpp（`#479 <https://github.com/ros2/system_tests/issues/479>`__）
* 新增变更日志（`#473 <https://github.com/ros2/system_tests/issues/473>`__）
* 贡献者：Abrar Rahman Protyasha、Aditya Pande、Chris Lalancette、Christophe Bedard、Ivan Santiago Paunovic、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`test_interface_files <https://github.com/ros2/test_interface_files/tree/humble/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 撤销“更新 package.xml”的修改（`#18 <https://github.com/ros2/test_interface_files/issues/18>`__），对应撤销提交为（`#19 <https://github.com/ros2/test_interface_files/issues/19>`__）
* 更新 package.xml（`#18 <https://github.com/ros2/test_interface_files/issues/18>`__）
* 将维护者更新为 Audrow Nash（`#17 <https://github.com/ros2/test_interface_files/issues/17>`__）
* 添加 BoundedPlainSequences 消息（`#14 <https://github.com/ros2/test_interface_files/issues/14>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Miguel Company、Nikolai Morin


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`test_launch_ros <https://github.com/ros2/launch_ros/tree/humble/test_launch_ros/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 放宽测试时间容差（`#305 <https://github.com/ros2/launch_ros/issues/305>`__）
* 为可组合节点评估参数文件时使用正确的命名空间（`#303 <https://github.com/ros2/launch_ros/issues/303>`__）
* 处理参数评估过程中的空字符串（`#300 <https://github.com/ros2/launch_ros/issues/300>`__）
* 添加参数替换功能（`#297 <https://github.com/ros2/launch_ros/issues/297>`__）
* 提供更有帮助的错误消息（`#275 <https://github.com/ros2/launch_ros/issues/275>`__）
* 更新 setup.py 中的维护者信息（`#287 <https://github.com/ros2/launch_ros/issues/287>`__）
* 为可组合节点从文件设置参数（`#281 <https://github.com/ros2/launch_ros/issues/281>`__）
* 更新功能包维护者（`#284 <https://github.com/ros2/launch_ros/issues/284>`__）
* 更新节点名称匹配器（`#282 <https://github.com/ros2/launch_ros/issues/282>`__）
* 支持可组合节点的两种参数文件配置方式（`#259 <https://github.com/ros2/launch_ros/issues/259>`__）
* 在测试后关闭 context（`#267 <https://github.com/ros2/launch_ros/issues/267>`__）
* 处理 RosTimer 中的 substitutions（`#264 <https://github.com/ros2/launch_ros/issues/264>`__）
* 添加 SetParametersFromFile action（`#260 <https://github.com/ros2/launch_ros/issues/260>`__）
* 通过 launch 前端正确支持 ros_args 属性（`#253 <https://github.com/ros2/launch_ros/issues/253>`__）
* 为 'push-ros-namespace' 添加 'push_ros_namespace' 别名（`#250 <https://github.com/ros2/launch_ros/issues/250>`__）
* 为 Node action 添加 ros_arguments 选项（`#249 <https://github.com/ros2/launch_ros/issues/249>`__）
* ROS Timer Action（`#244 <https://github.com/ros2/launch_ros/issues/244>`__）
* 在前端支持 container（`#235 <https://github.com/ros2/launch_ros/issues/235>`__）
* 添加 normalize_remap_rule 及相关类型（launch `#173 <https://github.com/ros2/launch/issues/173>`__）
* 修复 setup.py 中的版本信息（launch `#155 <https://github.com/ros2/launch/issues/155>`__）
* 修复 bug，确保正确处理 shutdown 事件（launch `#154 <https://github.com/ros2/launch/issues/154>`__）
* 修复并为传递给 Node actions 的 remappings 添加测试（launch `#137 <https://github.com/ros2/launch/issues/137>`__）
* 贡献者：Aditya Pande、Audrow Nash、Christophe Bedard、David V. Lu!!、Jacob Perron、Jorge Perez、Kenji Miyake、Michel Hidalgo、Rebecca Butler


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`test_launch_testing <https://github.com/ros2/launch/tree/humble/test_launch_testing/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Aditya Pande 和 Michel Hidalgo（`#559 <https://github.com/ros2/launch/issues/559>`__）
* 更新维护者信息（`#555 <https://github.com/ros2/launch/issues/555>`__）
* 贡献者：Aditya Pande、Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`test_msgs <https://github.com/ros2/rcl_interfaces/tree/humble/test_msgs/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}，并直接依赖 rosidl_typesupport_* targets（`#133 <https://github.com/ros2/rcl_interfaces/issues/133>`__）
* 将维护者更新为 Chris Lalancette（`#130 <https://github.com/ros2/rcl_interfaces/issues/130>`__）
* 为 BoundedPlainSequences 添加测试夹具（`#125 <https://github.com/ros2/rcl_interfaces/issues/125>`__）
* 将 BoundedPlainSequences 添加到 test_msgs（`#123 <https://github.com/ros2/rcl_interfaces/issues/123>`__）
* 贡献者：Audrow Nash、Miguel Company、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`test_quality_of_service <https://github.com/ros2/system_tests/tree/humble/test_quality_of_service/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Aditya Pande 和 Shane Loretz（`#491 <https://github.com/ros2/system_tests/issues/491>`__）
* 更新维护者信息（`#489 <https://github.com/ros2/system_tests/issues/489>`__）
* 修复已弃用订阅回调的警告（`#483 <https://github.com/ros2/system_tests/issues/483>`__）
* 新增变更日志（`#473 <https://github.com/ros2/system_tests/issues/473>`__）
* 贡献者：Abrar Rahman Protyasha、Aditya Pande、Audrow Nash、Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`test_rclcpp <https://github.com/ros2/system_tests/tree/humble/test_rclcpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 cpplint 的头文件包含顺序（`#493 <https://github.com/ros2/system_tests/issues/493>`__）
* 修复测试（`#488 <https://github.com/ros2/system_tests/issues/488>`__）
* 更新维护者信息（`#489 <https://github.com/ros2/system_tests/issues/489>`__）
* 为 rclcpp 的 SIGTERM 处理器添加测试（`#485 <https://github.com/ros2/system_tests/issues/485>`__）
* 修复已弃用订阅回调的警告（`#483 <https://github.com/ros2/system_tests/issues/483>`__）
* 修复客户端 API 更新后的弃用警告和失败问题（`#482 <https://github.com/ros2/system_tests/issues/482>`__）
* 使用 rosidl_get_typesupport_target()（`#480 <https://github.com/ros2/system_tests/issues/480>`__）
* 使用 rcpputils/scope_exit.hpp 替代 rclcpp/scope_exit.hpp（`#479 <https://github.com/ros2/system_tests/issues/479>`__）
* 为延迟服务回调签名添加测试（`#478 <https://github.com/ros2/system_tests/issues/478>`__）
* 新增变更日志（`#473 <https://github.com/ros2/system_tests/issues/473>`__）
* 合并来自 ros2/ros2_658_leftovers 的 Pull Request（`#357 <https://github.com/ros2/system_tests/issues/357>`__）
* 贡献者：Abrar Rahman Protyasha、Aditya Pande、Christophe Bedard、Ivan Santiago Paunovic、Jacob Perron、Mauro Passerino、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`test_rmw_implementation <https://github.com/ros2/rmw_implementation/tree/humble/test_rmw_implementation/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 添加内容过滤话题接口（`#181 <https://github.com/ros2/rmw_implementation/issues/181>`__）
* 修复代码检查问题（`#200 <https://github.com/ros2/rmw_implementation/issues/200>`__）
* 添加客户端/服务 QoS 获取接口（`#196 <https://github.com/ros2/rmw_implementation/issues/196>`__）
* 添加有界序列序列化测试（`#193 <https://github.com/ros2/rmw_implementation/issues/193>`__）
* 添加 RMW_DURATION_INFINITE 基本符合性测试（`#194 <https://github.com/ros2/rmw_implementation/issues/194>`__）
* 测试 SubscriptionOptions::ignore_local_publications（`#192 <https://github.com/ros2/rmw_implementation/issues/192>`__）
* 添加 rmw_publisher_wait_for_all_acked（`#188 <https://github.com/ros2/rmw_implementation/issues/188>`__）
* 在 test_rmw_implementation 的 service 测试中等待 server 启动（`#191 <https://github.com/ros2/rmw_implementation/issues/191>`__）
