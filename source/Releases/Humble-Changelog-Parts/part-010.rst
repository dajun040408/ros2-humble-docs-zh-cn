* 修复简单 IT 插件关闭问题（`#225 <https://github.com/ros-perception/image_common/issues/225>`__）
* 移除 PLUGINLIB__DISABLE_BOOST_FUNCTIONS 定义（`#226 <https://github.com/ros-perception/image_common/issues/226>`__）
* 修复 cpplint 的头文件包含顺序（`#221 <https://github.com/ros-perception/image_common/issues/221>`__），相关问题参见 ament_lint PR #324。
* 导出现代 CMake 目标以替代变量，并将头文件安装到 include/${PROJECT_NAME}（`#218 <https://github.com/ros-perception/image_common/issues/218>`__）
* 修复 SimpleSubscriberPlugin（`#195 <https://github.com/ros-perception/image_common/issues/195>`__）
* 确保被重写的方法均标记为 override（`#192 <https://github.com/ros-perception/image_common/issues/192>`__）
* 暴露订阅选项（`#186 <https://github.com/ros-perception/image_common/issues/186>`__）
* 修正文件名拼写：cammera_publisher.hpp 更正为 camera_publisher.hpp（`#177 <https://github.com/ros-perception/image_common/issues/177>`__）
* 更新维护者信息（`#173 <https://github.com/ros-perception/image_common/issues/173>`__）
* 修复 CameraPublisher::getNumSubscribers()（`#163 <https://github.com/ros-perception/image_common/issues/163>`__）
* 贡献者：Alejandro Hernández Cordero、Audrow Nash、Chris Lalancette、Hye-Jong KIM、Ivan Santiago Paunovic、Jacob Perron、Michael Ferguson、RoboTech Vision、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`interactive_markers <https://github.com/ros-visualization/interactive_markers/tree/humble/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 关闭期间如果上下文无效，则不发布消息（`#89 <https://github.com/ros-visualization/interactive_markers/issues/89>`__）
* 将头文件安装到 include/，并修复其他 CMake 问题（`#85 <https://github.com/ros-visualization/interactive_markers/issues/85>`__）
* 修复客户端 API 更新后引入的弃用警告（`#83 <https://github.com/ros-visualization/interactive_markers/issues/83>`__）
* 修复已弃用的订阅回调警告（`#84 <https://github.com/ros-visualization/interactive_markers/issues/84>`__）
* 使用 tf2_geometry_msgs.hpp 替代 .h 文件（`#82 <https://github.com/ros-visualization/interactive_markers/issues/82>`__）
* 贡献者：Abrar Rahman Protyasha、Chris Lalancette、Ivan Santiago Paunovic、Jacob Perron、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`intra_process_demo <https://github.com/ros2/demos/tree/humble/intra_process_demo/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 为 cv::putText 添加 opencv_imgproc 依赖（`#554 <https://github.com/ros2/demos/issues/554>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#548 <https://github.com/ros2/demos/issues/548>`__）
* 修复 cpplint 的头文件包含顺序和相对路径问题（`#551 <https://github.com/ros2/demos/issues/551>`__）
* 将维护者更新为 Audrow Nash 和 Michael Jeronimo（`#543 <https://github.com/ros2/demos/issues/543>`__）
* 修复 demos 文档中的其他问题（`#538 <https://github.com/ros2/demos/issues/538>`__）
* 修复已弃用的订阅者回调警告（`#532 <https://github.com/ros2/demos/issues/532>`__）
* 回退“新增类型伪装示例”的修改（`#482 <https://github.com/ros2/demos/issues/482>`__），对应回退提交 `#520 <https://github.com/ros2/demos/issues/520>`__。
* 新增类型伪装示例（`#482 <https://github.com/ros2/demos/issues/482>`__）
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Chris Lalancette、Jacob Perron、Shane Loretz、William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`kdl_parser <https://github.com/ros/kdl_parser/tree/humble/kdl_parser/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 依赖 orocos-kdl vendor 功能包（`#58 <https://github.com/ros/kdl_parser/issues/58>`__）
* 将头文件安装到 include/，并修复其他 CMake 问题（`#61 <https://github.com/ros/kdl_parser/issues/61>`__）
* 更新至 uncrustify 0.72（`#60 <https://github.com/ros/kdl_parser/issues/60>`__）
* 贡献者：Chris Lalancette、Jacob Perron、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`laser_geometry <https://github.com/ros-perception/laser_geometry/tree/humble/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}（`#86 <https://github.com/ros-perception/laser_geometry/issues/86>`__）
* 显式转换为 double，以避免精度损失
* 修复导致无法执行去畸变的 Duration 类型转换问题
* 修复 Windows Debug 模式下的构建和运行问题（`#82 <https://github.com/ros-perception/laser_geometry/issues/82>`__）
* 更新 ROS 2 对应的 Python 代码和测试（`#80 <https://github.com/ros-perception/laser_geometry/issues/80>`__）
* 贡献者：Chris Lalancette、Jonathan Binney、Marco Lampacrescia、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`launch <https://github.com/ros2/launch/tree/humble/launch/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 在测试中使用沙箱环境，以修复重复出现的作业失败（`#609 <https://github.com/ros2/launch/issues/609>`__）
* 在 test_execute_processs_shutdown 中更快启动 Python，以避免不稳定的测试失败（`#608 <https://github.com/ros2/launch/issues/608>`__）
* 修复 Python 3.10 下 importlib_metdata 产生的警告（`#606 <https://github.com/ros2/launch/issues/606>`__）
* 新增布尔值替换功能（`#598 <https://github.com/ros2/launch/issues/598>`__）
* 支持对环境变量设置作用域（`#601 <https://github.com/ros2/launch/issues/601>`__）
* 修复 launch 上下文中的等待关闭逻辑（`#603 <https://github.com/ros2/launch/issues/603>`__）
* 修复 respawn 变量解析（`#569 <https://github.com/ros2/launch/issues/569>`__）
* 美化 ExecuteLocal 中记录的命令（`#594 <https://github.com/ros2/launch/issues/594>`__）
* 在 XML/YAML 文件中将 output 作为替换项展开（`#577 <https://github.com/ros2/launch/issues/577>`__）
* 如果警告已经发生，则跳过警告测试（`#585 <https://github.com/ros2/launch/issues/585>`__）
* 使用带超时的 asyncio.wait 替代 sleep（`#576 <https://github.com/ros2/launch/issues/576>`__）
* 使 test_parser 兼容低于 3.8 的 Python 版本（`#575 <https://github.com/ros2/launch/issues/575>`__）
* 将已完成动作的异常传播到 launch service 主循环（`#566 <https://github.com/ros2/launch/issues/566>`__）
* 加载 launch 扩展失败时发出警告（`#572 <https://github.com/ros2/launch/issues/572>`__）
* 为 Jammy 添加两项修复（`#571 <https://github.com/ros2/launch/issues/571>`__）
* 在 Python 表达式中计算数学符号和函数（`#557 <https://github.com/ros2/launch/issues/557>`__）
* 记录 TimerAction 参数文档（`#558 <https://github.com/ros2/launch/issues/558>`__）
* 改进 launch 参数内省（`#556 <https://github.com/ros2/launch/issues/556>`__）
* 将维护者更新为 Aditya Pande 和 Michel Hidalgo（`#559 <https://github.com/ros2/launch/issues/559>`__）
* 更新维护者信息（`#555 <https://github.com/ros2/launch/issues/555>`__）
* 首个基于 launch 测试的原生 pytest 插件原型（`#528 <https://github.com/ros2/launch/issues/528>`__）
* 允许在 IncludeLaunchDescription 中直接指定原始路径（`#544 <https://github.com/ros2/launch/issues/544>`__）
* 新增 Executable 描述类（`#454 <https://github.com/ros2/launch/issues/454>`__）
* 事件处理器支持通过可调用对象匹配目标动作，而不局限于对象实例（`#540 <https://github.com/ros2/launch/issues/540>`__）
* 新增 AppendEnvironmentVariable 动作（`#543 <https://github.com/ros2/launch/issues/543>`__）
* 记录 EnvironmentVariable 替换解析上下文的注意事项（`#541 <https://github.com/ros2/launch/issues/541>`__）
* 新增清除 launch 配置的功能（`#515 <https://github.com/ros2/launch/issues/515>`__）
* 为 ExecuteProcess 文档添加示例（`#525 <https://github.com/ros2/launch/issues/525>`__）
* 修复 ``DeclareLaunchArgument`` 的 XML 解析和构造函数（`#529 <https://github.com/ros2/launch/issues/529>`__）
* 修复 Windows 上的 pytest 运行问题（`#526 <https://github.com/ros2/launch/issues/526>`__）
* 改进文档（`#523 <https://github.com/ros2/launch/issues/523>`__）
* 为可执行文件前缀应用增加过滤机制（`#522 <https://github.com/ros2/launch/issues/522>`__）
* 使每个解析器扩展提供一组文件扩展名（`#516 <https://github.com/ros2/launch/issues/516>`__）
* 增加缺失的 PyYAML 执行依赖（`#493 <https://github.com/ros2/launch/issues/493>`__）
* 重构 TimerAction，使 RosTimer 可以扩展它（`#512 <https://github.com/ros2/launch/issues/512>`__）
* 改进 (Not)Equals 条件的类型提示（`#510 <https://github.com/ros2/launch/issues/510>`__）
* 贡献者：Aditya Pande、Audrow Nash、Cameron Miller、Chris Lalancette、Christophe Bedard、David V. Lu!!、Derek Chopp、HMellor、Immanuel Martini、Ivan Santiago Paunovic、Jacob Perron、Kenji Miyake、Khush Jain、Kosuke Takeuchi、Rebecca Butler、Scott K Logan、Shane Loretz、roger-strain、tumtom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`launch_pytest <https://github.com/ros2/launch/tree/humble/launch_pytest/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Aditya Pande 和 Michel Hidalgo（`#559 <https://github.com/ros2/launch/issues/559>`__）
* [launch_pytest] 修改 wait_for_output()/wait_for_stderr() 的工作方式，并新增 assert_*() 替代方法（`#553 <https://github.com/ros2/launch/issues/553>`__）
* 更新维护者信息（`#555 <https://github.com/ros2/launch/issues/555>`__）
* [launch_pytest] 修复使用 colcon --retest-until-fail 标志时出现的问题（`#552 <https://github.com/ros2/launch/issues/552>`__）
* 首个基于 launch 测试的原生 pytest 插件原型（`#528 <https://github.com/ros2/launch/issues/528>`__）
* 贡献者：Aditya Pande、Audrow Nash、Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`launch_ros <https://github.com/ros2/launch_ros/tree/humble/launch_ros/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
