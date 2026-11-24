* 仅当 default_logger_level 已设置时，才更改默认日志记录器级别（`#943 <https://github.com/ros2/rcl/issues/943>`__）
* 为 wait_for_entity_helpers 添加独立库，以避免重复编译（`#942 <https://github.com/ros2/rcl/issues/942>`__）
* 将 Windows 超时时间从 15 毫秒增加到 25 毫秒（`#940 <https://github.com/ros2/rcl/issues/940>`__）
* 测试应检查指定数量的实体（`#935 <https://github.com/ros2/rcl/issues/935>`__）
* 修复使用 rosdoc2 时 rcl 的文档构建问题（`#932 <https://github.com/ros2/rcl/issues/932>`__）
* 包含 rmw_event_t，而不是仅进行前向声明（`#933 <https://github.com/ros2/rcl/issues/933>`__）
* 增加对 rcl_publisher_wait_for_all_acked 的支持（`#913 <https://github.com/ros2/rcl/issues/913>`__）
* 为 rcl_take 添加 tracing 插桩（`#930 <https://github.com/ros2/rcl/issues/930>`__）
* 修复 rcl_subscription_init 文档块中 C++ typesupport 示例的 #include（`#927 <https://github.com/ros2/rcl/issues/927>`__）
* 在 rcutils/get_env.h 弃用后更新头文件包含（`#917 <https://github.com/ros2/rcl/issues/917>`__）
* 使用正确的 rcl_logging 返回值类型，并与常量进行比较（`#916 <https://github.com/ros2/rcl/issues/916>`__）
* 贡献者：Barry Xu、Chen Lihui、Chris Lalancette、Christophe Bedard、Haowei Wen、Ivan Santiago Paunovic、Jafar Abdi、Michel Hidalgo、Miguel Company、NoyZuberi、Scott K Logan、Shane Loretz、Tomoya Fujita、William Woodall、iRobot ROS、mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rcl_action <https://github.com/ros2/rcl/tree/humble/rcl_action/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 新增 Events Executor（`#839 <https://github.com/ros2/rcl/issues/839>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#959 <https://github.com/ros2/rcl/issues/959>`__）
* 修复使用 rosdoc2 时 rcl_action 的文档构建问题（`#937 <https://github.com/ros2/rcl/issues/937>`__）
* 修复 action server 已过期目标的容量问题（`#931 <https://github.com/ros2/rcl/issues/931>`__）
* 在 rcl_action 通信测试中等待 action server（`#919 <https://github.com/ros2/rcl/issues/919>`__）
* 贡献者：Michel Hidalgo、Shane Loretz、iRobot ROS、spiralray


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rcl_interfaces <https://github.com/ros2/rcl_interfaces/tree/humble/rcl_interfaces/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Chris Lalancette（`#130 <https://github.com/ros2/rcl_interfaces/issues/130>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rcl_lifecycle <https://github.com/ros2/rcl/tree/humble/rcl_lifecycle/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}（`#959 <https://github.com/ros2/rcl/issues/959>`__）
* [rcl_lifecycle] 不在不同节点之间共享 transition event 消息（`#956 <https://github.com/ros2/rcl/issues/956>`__）
* 将维护者更新为 Ivan Paunovic 和 William Woodall（`#952 <https://github.com/ros2/rcl/issues/952>`__）
* 修复使用 rosdoc2 时 rcl_lifecycle 的文档构建问题（`#938 <https://github.com/ros2/rcl/issues/938>`__）
* 重命名变量，以修复名称遮蔽警告（`#929 <https://github.com/ros2/rcl/issues/929>`__）
* 贡献者：Alberto Soragna、Audrow Nash、Ivan Santiago Paunovic、Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rcl_logging_interface <https://github.com/ros2/rcl_logging/tree/humble/rcl_logging_interface/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}（`#85 <https://github.com/ros2/rcl_logging/issues/85>`__）
* 修复 cpplint 的头文件包含顺序（`#84 <https://github.com/ros2/rcl_logging/issues/84>`__），相关问题参见 ament_lint PR #324。
* 将维护者更新为 Chris Lalancette（`#83 <https://github.com/ros2/rcl_logging/issues/83>`__）
* 修复重命名后的 ``rcpputils`` 头文件（`#81 <https://github.com/ros2/rcl_logging/issues/81>`__）
* 为 rcl_logging_interface 功能包添加 Doxyfile（`#80 <https://github.com/ros2/rcl_logging/issues/80>`__）
* 在 rcutils/get_env.h 弃用后更新头文件包含（`#75 <https://github.com/ros2/rcl_logging/issues/75>`__）
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Christophe Bedard、Jacob Perron、Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rcl_logging_noop <https://github.com/ros2/rcl_logging/tree/humble/rcl_logging_noop/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Chris Lalancette（`#83 <https://github.com/ros2/rcl_logging/issues/83>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rcl_logging_spdlog <https://github.com/ros2/rcl_logging/tree/humble/rcl_logging_spdlog/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 cpplint 的头文件包含顺序（`#84 <https://github.com/ros2/rcl_logging/issues/84>`__），相关问题参见 ament_lint PR #324。
* 将维护者更新为 Chris Lalancette（`#83 <https://github.com/ros2/rcl_logging/issues/83>`__）
* 修复重命名后的 ``rcpputils`` 头文件（`#81 <https://github.com/ros2/rcl_logging/issues/81>`__）
* 在 rcutils/get_env.h 弃用后更新头文件包含（`#75 <https://github.com/ros2/rcl_logging/issues/75>`__）
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Christophe Bedard、Jacob Perron


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rcl_yaml_param_parser <https://github.com/ros2/rcl/tree/humble/rcl_yaml_param_parser/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}（`#959 <https://github.com/ros2/rcl/issues/959>`__）
* 将维护者更新为 Ivan Paunovic 和 William Woodall（`#952 <https://github.com/ros2/rcl/issues/952>`__）
* 调整 rcl_yaml_param_parser 文档（`#939 <https://github.com/ros2/rcl/issues/939>`__）
* 贡献者：Audrow Nash、Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rclcpp <https://github.com/ros2/rclcpp/tree/humble/rclcpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 DEFINE_CONTENT_FILTER CMake 选项（`#1914 <https://github.com/ros2/rclcpp/issues/1914>`__）
* 移除 Galactic 发行版期间已弃用的内容（`#1913 <https://github.com/ros2/rclcpp/issues/1913>`__）
* 为 waitable 新增 take_data_by_entity_id API（`#1892 <https://github.com/ros2/rclcpp/issues/1892>`__）
* 新增内容过滤话题接口（`#1561 <https://github.com/ros2/rclcpp/issues/1561>`__）
* [NodeParameters] 在参数信息预检查阶段设置名称（`#1908 <https://github.com/ros2/rclcpp/issues/1908>`__）
* 添加 ament_cmake_google_benchmark 测试依赖（`#1904 <https://github.com/ros2/rclcpp/issues/1904>`__）
* 在 GenericPublisher 中增加 loaned message 发布方式（`#1856 <https://github.com/ros2/rclcpp/issues/1856>`__）
* 添加缺失的 rcl_interfaces ament 依赖（`#1903 <https://github.com/ros2/rclcpp/issues/1903>`__）
* 更新数据回调测试，以覆盖所有已发布样本（`#1900 <https://github.com/ros2/rclcpp/issues/1900>`__）
* 增加确认超时时间，以适应较慢的 Connext 设置（`#1901 <https://github.com/ros2/rclcpp/issues/1901>`__）
* clang-tidy：使用显式构造函数（`#1782 <https://github.com/ros2/rclcpp/issues/1782>`__）
* 新增客户端/服务 QoS 获取接口（`#1784 <https://github.com/ros2/rclcpp/issues/1784>`__）
* 修复 rclcpp 中的多项 rosdoc2 问题（`#1897 <https://github.com/ros2/rclcpp/issues/1897>`__）
* 定时器取消后，time_until_trigger 返回最大时间值（`#1893 <https://github.com/ros2/rclcpp/issues/1893>`__）
* 对 rclcpp 进行微优化（`#1896 <https://github.com/ros2/rclcpp/issues/1896>`__）
* 支持零超时的 spin_all（`#1878 <https://github.com/ros2/rclcpp/issues/1878>`__）
* 新增 RMW listener API（`#1579 <https://github.com/ros2/rclcpp/issues/1579>`__）
* 移除测试中的 fastrtps 定制（`#1887 <https://github.com/ros2/rclcpp/issues/1887>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#1888 <https://github.com/ros2/rclcpp/issues/1888>`__）
* 使用 ament_generate_version_header（`#1886 <https://github.com/ros2/rclcpp/issues/1886>`__）
* 使用通用引用以支持右值（`#1883 <https://github.com/ros2/rclcpp/issues/1883>`__）
* 修复一个订阅无法两次调用 wait_for_message 的问题（`#1870 <https://github.com/ros2/rclcpp/issues/1870>`__）
* 为 get_parameter_or 添加返回值版本（`#1813 <https://github.com/ros2/rclcpp/issues/1813>`__）
* 清理时间源对象的生命周期管理（`#1867 <https://github.com/ros2/rclcpp/issues/1867>`__）
* 在 executor 基类中新增 is_spinning() 方法
* 清理 TypeAdapt 测试（`#1858 <https://github.com/ros2/rclcpp/issues/1858>`__）
* 清理头文件包含（`#1857 <https://github.com/ros2/rclcpp/issues/1857>`__）
* 修复 cpplint 的头文件包含顺序和相对路径问题（`#1859 <https://github.com/ros2/rclcpp/issues/1859>`__）
