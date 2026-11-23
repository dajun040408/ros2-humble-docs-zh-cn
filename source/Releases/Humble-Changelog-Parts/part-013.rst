* 将维护者更新为 Geoffrey Biggs（`#23 <https://github.com/ros2/mimick_vendor/issues/23>`__）
* 更新至最新提交，以支持 Apple M1（`#20 <https://github.com/ros2/mimick_vendor/issues/20>`__）
* 贡献者：Audrow Nash、Brett Downing、Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`nav_msgs <https://github.com/ros2/common_interfaces/tree/humble/nav_msgs/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 接口功能包应对其依赖的接口功能包完整声明 ``<depend>`` 依赖（`#173 <https://github.com/ros2/common_interfaces/issues/173>`__）
* 将维护者更新为 Geoffrey Biggs 和 Tully Foote（`#163 <https://github.com/ros2/common_interfaces/issues/163>`__）
* 贡献者：Audrow Nash、Grey


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`pendulum_control <https://github.com/ros2/demos/tree/humble/pendulum_control/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 cpplint 的头文件包含顺序和相对路径问题（`#551 <https://github.com/ros2/demos/issues/551>`__）
* 从 pendulum_demo 中移除 malloc_hook（`#544 <https://github.com/ros2/demos/issues/544>`__）
* 将维护者更新为 Audrow Nash 和 Michael Jeronimo（`#543 <https://github.com/ros2/demos/issues/543>`__）
* 修复 demos 文档中的其他问题（`#538 <https://github.com/ros2/demos/issues/538>`__）
* 修复 pendulum_control 文档（`#537 <https://github.com/ros2/demos/issues/537>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Jacob Perron


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`pendulum_msgs <https://github.com/ros2/demos/tree/humble/pendulum_msgs/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Audrow Nash 和 Michael Jeronimo（`#543 <https://github.com/ros2/demos/issues/543>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`pluginlib <https://github.com/ros/pluginlib/tree/humble/pluginlib/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}，并移除 ament_target_dependencies 调用（`#226 <https://github.com/ros/pluginlib/issues/226>`__）
* 要求包含 <memory>（`#225 <https://github.com/ros/pluginlib/issues/225>`__）
* 将 LibraryLoadExceptions 下移一级，以提供更准确的错误消息（`#221 <https://github.com/ros/pluginlib/issues/221>`__）
* 将维护者更新为 Chris Lalancette（`#223 <https://github.com/ros/pluginlib/issues/223>`__）
* 扩展终止条件，避免找不到 package.xml 时出现无限循环（`#220 <https://github.com/ros/pluginlib/issues/220>`__）
* 移除已弃用的头文件（`#217 <https://github.com/ros/pluginlib/issues/217>`__）
* 贡献者：Alberto Soragna、Audrow Nash、Chris Lalancette、David V. Lu!!、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`pybind11_vendor <https://github.com/ros2/pybind11_vendor/tree/humble/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 使用 sha256 哈希替代标签（`#12 <https://github.com/ros2/pybind11_vendor/issues/12>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#11 <https://github.com/ros2/pybind11_vendor/issues/11>`__）
* 将 pybind11 更新至 2.7.1（`#10 <https://github.com/ros2/pybind11_vendor/issues/10>`__），该版本随 Ubuntu 22.04 一同提供。
* 贡献者：Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`python_cmake_module <https://github.com/ros2/python_cmake_module/tree/humble/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 要求 Python 3.6，因为多个位置使用了格式化字符串（`#10 <https://github.com/ros2/python_cmake_module/issues/10>`__）
* 记录该模块设置的所有变量（`#5 <https://github.com/ros2/python_cmake_module/issues/5>`__）
* 新增变更日志（`#4 <https://github.com/ros2/python_cmake_module/issues/4>`__）
* 贡献者：Ivan Santiago Paunovic、Shane Loretz、William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`qt_gui_cpp <https://github.com/ros-visualization/qt_gui_core/tree/humble-devel/qt_gui_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include${PROJECT_NAME}（`#259 <https://github.com/ros-visualization/qt_gui_core/issues/259>`__）
* 导出 targets，替代旧式 CMake 变量（`#257 <https://github.com/ros-visualization/qt_gui_core/issues/257>`__）
* 显式使用 FindPython3，替代隐式使用 FindPythonInterp（`#254 <https://github.com/ros-visualization/qt_gui_core/issues/254>`__）
* 贡献者：Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`quality_of_service_demo_cpp <https://github.com/ros2/demos/tree/humble/quality_of_service_demo/rclcpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}（`#548 <https://github.com/ros2/demos/issues/548>`__）
* 修复 cpplint 的头文件包含顺序和相对路径问题（`#551 <https://github.com/ros2/demos/issues/551>`__）
* 修复与 uncrustify 0.72 的兼容问题（`#545 <https://github.com/ros2/demos/issues/545>`__）
* 将维护者更新为 Audrow Nash 和 Michael Jeronimo（`#543 <https://github.com/ros2/demos/issues/543>`__）
* 修复 demos 文档中的其他问题（`#538 <https://github.com/ros2/demos/issues/538>`__）
* 修复已弃用的订阅者回调警告（`#532 <https://github.com/ros2/demos/issues/532>`__）
* 正确初始化消息（`#522 <https://github.com/ros2/demos/issues/522>`__）
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Chris Lalancette、Ivan Santiago Paunovic、Jacob Perron、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`quality_of_service_demo_py <https://github.com/ros2/demos/tree/humble/quality_of_service_demo/rclpy/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Audrow Nash 和 Michael Jeronimo（`#543 <https://github.com/ros2/demos/issues/543>`__）
* 更新 Python 节点对 SIGINT 的处理方式（`#539 <https://github.com/ros2/demos/issues/539>`__）
* 贡献者：Audrow Nash、Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rcl <https://github.com/ros2/rcl/tree/humble/rcl/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 新增内容过滤话题接口（`#894 <https://github.com/ros2/rcl/issues/894>`__）
* 为定时器参数增加额外的空值检查（`#973 <https://github.com/ros2/rcl/issues/973>`__）
* 在参数解析的规则中允许使用正斜杠（`#860 <https://github.com/ros2/rcl/issues/860>`__）
* 抑制 clang-tidy 误报（`#951 <https://github.com/ros2/rcl/issues/951>`__）
* 修复 rcl_context_impl_t.argv 中缺失终止符 \\0 的问题（`#969 <https://github.com/ros2/rcl/issues/969>`__）
* test_publisher_wait_all_ack 增加对 rcpputils 的依赖（`#968 <https://github.com/ros2/rcl/issues/968>`__）
* 对 rcl 进行微优化（`#965 <https://github.com/ros2/rcl/issues/965>`__）
* 如果定时器已取消，rcl_timer_get_time_until_next_call 返回 TIMER_CANCELED（`#963 <https://github.com/ros2/rcl/issues/963>`__）
* 新增 Events Executor（`#839 <https://github.com/ros2/rcl/issues/839>`__）
* 移除 test_events 中的 fastrtps 定制（`#960 <https://github.com/ros2/rcl/issues/960>`__）
* 新增客户端/服务 QoS 获取接口（`#941 <https://github.com/ros2/rcl/issues/941>`__）
* 引入 ROS_DISABLE_LOAN_MSG，以禁用 can_loan_messages（`#949 <https://github.com/ros2/rcl/issues/949>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#959 <https://github.com/ros2/rcl/issues/959>`__）
* 将 rcl_difference_times 的参数声明为 const（`#955 <https://github.com/ros2/rcl/issues/955>`__）
* 更新 inject_on_return 测试的跳过逻辑（`#953 <https://github.com/ros2/rcl/issues/953>`__）
* 修复使用零时间跳变阈值时仍调用跳变回调的问题（`#948 <https://github.com/ros2/rcl/issues/948>`__）
