^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tlsf_cpp <https://github.com/ros2/realtime_support/tree/humble/tlsf_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}（`#114 <https://github.com/ros2/realtime_support/issues/114>`__）
* 导出现代 CMake targets（`#110 <https://github.com/ros2/realtime_support/issues/110>`__）
* 在 tlsf_cpp 测试中移除 malloc hooks 的使用（`#109 <https://github.com/ros2/realtime_support/issues/109>`__）
* 贡献者：Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`topic_monitor <https://github.com/ros2/demos/tree/humble/topic_monitor/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Audrow Nash 和 Michael Jeronimo（`#543 <https://github.com/ros2/demos/issues/543>`__）
* 对 topic monitor 进行小幅清理（`#517 <https://github.com/ros2/demos/issues/517>`__）
* 修复高发布频率下的 topic_monitor（`#461 <https://github.com/ros2/demos/issues/461>`__）
* 使用 is_alive 检查线程状态（`#510 <https://github.com/ros2/demos/issues/510>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Elias De Coninck


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`topic_statistics_demo <https://github.com/ros2/demos/tree/humble/topic_statistics_demo/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}（`#548 <https://github.com/ros2/demos/issues/548>`__）
* 修复 demos 文档中的其他问题（`#538 <https://github.com/ros2/demos/issues/538>`__）
* 修复已弃用订阅回调的警告（`#532 <https://github.com/ros2/demos/issues/532>`__）
* 贡献者：Abrar Rahman Protyasha、Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tracetools <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/tracetools/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}
* 合并分支 'update-mentions-of-tracetools-test'：将适用位置对 tracetools_test 的引用更新为 test_tracetools。参见合并请求 `ros-tracing/ros2_tracing!259 <https://gitlab.com/ros-tracing/ros2_tracing/-/merge_requests/259>`__
* 将适用位置对 tracetools_test 的引用更新为 test_tracetools
* 合并分支 'version-3-1-0'：发布版本 3.1.0。参见合并请求 `ros-tracing/ros2_tracing!256 <https://gitlab.com/ros-tracing/ros2_tracing/-/merge_requests/256>`__
* 正确处理不带 tracepoint 参数的 TRACEPOINT() 宏调用
* 将 publisher handle tracepoint 参数从 rclcpp_publish 移至 rcl_publish
* 添加对 rmw 初始化/发布、take 和 executor 插桩的支持
* 在 Windows 上导出 target，并在 TRACETOOLS_DISABLED 时导出 interface
* 移除已弃用的工具函数
* 贡献者：Christophe Bedard、Ivan Santiago Paunovic、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tracetools_launch <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/tracetools_launch/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 默认禁用内核跟踪
* 不再要求必须安装内核跟踪器，并在未安装时进行检测
* 添加预加载 pthread 和 dl 插桩共享库的支持
* 移除 profile_fast 选项，并考虑同时通过 LD_PRELOAD 预加载这两个库
* 改进共享库预加载的事件匹配
* 改进 LdPreload action 的库查找函数，并添加适当的测试
* 修复多个 LdPreload actions 无法正常工作的问题，并添加测试
* 弃用 'context_names' 参数，改用 'context_fields'
* 支持 Trace action 的按 domain 配置 context fields
* 改进 LdPreload.get_shared_lib_path()，以处理可能存在静态库的情况
* 将部分测试从 tracetools_launch 移至 test_tracetools_launch
* 将 Trace action 暴露为前端 action，并支持 substitutions
* 贡献者：Christophe Bedard、Ingo Lütkebohle


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tracetools_test <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/tracetools_test/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 允许为 TraceTestCase 提供额外的 actions
* 移除 TraceTestCase 的 'package' 关键字参数默认值
* 将实际测试从 tracetools_test 移至新建的 test_tracetools 功能包
* 为 rmw 初始化/发布、take 和 executor 插桩添加测试
* 为 TraceTestCase 添加字段类型断言工具
* 修复已弃用订阅回调的警告
* 贡献者：Abrar Rahman Protyasha、Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tracetools_trace <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/tracetools_trace/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 默认禁用内核跟踪
* 不再要求必须安装内核跟踪器，并在未安装时进行检测
* 为 tracepoint 名称引入常量
* 优化默认 tracing session channel 配置值
* 弃用 'context_names' 参数，改用 'context_fields'
* 支持 Trace action 的按 domain 配置 context fields
* 添加对 rmw 初始化/发布、take 和 executor tracepoints 的支持
* 贡献者：Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`trajectory_msgs <https://github.com/ros2/common_interfaces/tree/humble/trajectory_msgs/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 接口功能包应完整声明对其所依赖接口功能包的 <depend> 依赖（`#173 <https://github.com/ros2/common_interfaces/issues/173>`__）
* 将维护者更新为 Geoffrey Biggs 和 Tully Foote（`#163 <https://github.com/ros2/common_interfaces/issues/163>`__）
* 贡献者：Audrow Nash、Grey


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`turtlesim <https://github.com/ros/ros_tutorials/tree/humble-devel/turtlesim/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 处理 qreal orient\_ 时使用 ``double``（`#114 <https://github.com/ros/ros_tutorials/issues/114>`__）
* 添加 Rolling 图标（`#133 <https://github.com/ros/ros_tutorials/issues/133>`__）
* 将维护者更新为 Audrow Nash 和 Michael Jeronimo（`#137 <https://github.com/ros/ros_tutorials/issues/137>`__）
* 修复已弃用订阅回调的警告（`#134 <https://github.com/ros/ros_tutorials/issues/134>`__）
* 使用 rosidl_get_typesupport_target()（`#132 <https://github.com/ros/ros_tutorials/issues/132>`__）
* 启动时输出正确的节点名称（`#122 <https://github.com/ros/ros_tutorials/issues/122>`__）
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Chris Lalancette、Katherine Scott、Seulbae Kim、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`urdf <https://github.com/ros2/urdf/tree/humble/urdf/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}（`#31 <https://github.com/ros2/urdf/issues/31>`__）
