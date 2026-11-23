^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rmw_implementation_cmake <https://github.com/ros2/rmw/tree/humble/rmw_implementation_cmake/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将 FastDDS 设为默认 DDS（`#315 <https://github.com/ros2/rmw/issues/315>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`robot_state_publisher <https://github.com/ros/robot_state_publisher/tree/humble/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 依赖 orocos_kdl_vendor（`#191 <https://github.com/ros/robot_state_publisher/issues/191>`__）
* 导出依赖，以便将 robot_state_publisher 作为组件使用（`#193 <https://github.com/ros/robot_state_publisher/issues/193>`__）
* 修复 cpplint 的头文件包含顺序（`#186 <https://github.com/ros/robot_state_publisher/issues/186>`__）
* 更改参数更新的处理方式（`#180 <https://github.com/ros/robot_state_publisher/issues/180>`__）
* 将头文件安装到 instal/${PROJECT_NAME}（`#184 <https://github.com/ros/robot_state_publisher/issues/184>`__）
* 增强 change_fixed_joint 测试的健壮性（`#183 <https://github.com/ros/robot_state_publisher/issues/183>`__）
* 新增测试，确保 fixed transform 会在更新时发生变化
* 对测试代码进行少量 C++ 风格改进
* 测试改用 target_include_directories
* URDF 更新时发布新的 fixed transform
* 使 joint_states 订阅的 QoS 可配置；默认使用 SensorDataQoS（`#179 <https://github.com/ros/robot_state_publisher/issues/179>`__）
* 移除对 urdfdom_headers 的依赖（`#168 <https://github.com/ros/robot_state_publisher/issues/168>`__）
* 修复已弃用的订阅者回调（`#173 <https://github.com/ros/robot_state_publisher/issues/173>`__）
* 清理 RobotStatePublisher 类的文档（`#172 <https://github.com/ros/robot_state_publisher/issues/172>`__）
* 始终将固定坐标系发布到 /tf_static（`#158 <https://github.com/ros/robot_state_publisher/issues/158>`__）
* 修正 README 中 publish_frequency 的默认值（`#166 <https://github.com/ros/robot_state_publisher/issues/166>`__）
* 新增 tf frame_prefix 参数（`#159 <https://github.com/ros/robot_state_publisher/issues/159>`__）
* 贡献者：Abrar Rahman Protyasha、Anthony Deschamps、Chris Lalancette、Jacob Perron、Kenji Brameld、Nils Schulte、Russell Joyce、Shane Loretz、Steve Nogar


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ros2action <https://github.com/ros2/ros2cli/tree/humble/ros2action/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 为终止挂起的测试添加超时（`#701 <https://github.com/ros2/ros2cli/issues/701>`__）
* 依赖 launch 功能包，而不是 ros_testing，以避免循环依赖（`#685 <https://github.com/ros2/ros2cli/issues/685>`__）
* 将维护者更新为 Aditya Pande、Audrow Nash 和 Michael Jeronimo（`#673 <https://github.com/ros2/ros2cli/issues/673>`__）
* 更新维护者信息（`#670 <https://github.com/ros2/ros2cli/issues/670>`__）
* 新增变更日志（`#635 <https://github.com/ros2/ros2cli/issues/635>`__）
* 贡献者：Aditya Pande、Audrow Nash、Ivan Santiago Paunovic、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ros2bag <https://github.com/ros2/rosbag2/tree/humble/ros2bag/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 支持以 loaned message 形式发布（`#981 <https://github.com/ros2/rosbag2/issues/981>`__）
* 回退“允许在 metadata.yaml 的 custom 字段中记录任意键值对”的修改（`#976 <https://github.com/ros2/rosbag2/issues/976>`__），对应回退提交 `#984 <https://github.com/ros2/rosbag2/issues/984>`__。
* 新增在 metadata.yaml 的 custom 字段中记录任意键值对的能力（`#976 <https://github.com/ros2/rosbag2/issues/976>`__）
* 支持以 loaned message 形式发布（`#981 <https://github.com/ros2/rosbag2/issues/981>`__）
* 再次记录回退上述 custom 字段功能的修改（`#984 <https://github.com/ros2/rosbag2/issues/984>`__）
* 新增在 metadata.yaml 的 custom 字段中记录任意键值对的能力（`#976 <https://github.com/ros2/rosbag2/issues/976>`__）
* 提升版本号，以避免冲突
* 确保 play 模式下已发布消息得到确认（`#951 <https://github.com/ros2/rosbag2/issues/951>`__）
* TopicFilter 使用 regex_search 替代 regex_match（`#932 <https://github.com/ros2/rosbag2/issues/932>`__）
* 新增 start-offset 播放选项（`#931 <https://github.com/ros2/rosbag2/issues/931>`__）
* 将 bag_rewrite 暴露为 ``ros2 bag convert``（`#921 <https://github.com/ros2/rosbag2/issues/921>`__）
* 为 recorder 新增“忽略叶子话题”选项（`#925 <https://github.com/ros2/rosbag2/issues/925>`__）
* 尽可能自动检测 Reader 的 storage_id（`#918 <https://github.com/ros2/rosbag2/issues/918>`__）
* 为 bag recorder 添加暂停/恢复选项（`#905 <https://github.com/ros2/rosbag2/issues/905>`__）
* 为 ``ros2 bag play`` 添加 --start-paused 选项（`#904 <https://github.com/ros2/rosbag2/issues/904>`__）
* 更新功能包维护者信息（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 修复 record 的 converter 插件选择（`#897 <https://github.com/ros2/rosbag2/issues/897>`__）
* 修复错误消息中缺少空格的问题（`#875 <https://github.com/ros2/rosbag2/issues/875>`__）
* 新增用于暂停/恢复切换和播放下一条消息的键盘控制（`#847 <https://github.com/ros2/rosbag2/issues/847>`__）
* 为 record 命令添加 --snapshot-mode 参数（`#851 <https://github.com/ros2/rosbag2/issues/851>`__）
* 重构插件查询机制，并统一 trait 管理（`#833 <https://github.com/ros2/rosbag2/issues/833>`__）
* 将 ``PlayOptions::delay`` 更新为 ``rclcpp::Duration``，以获得纳秒级分辨率（`#843 <https://github.com/ros2/rosbag2/issues/843>`__）
* 通过插件查询加载压缩和序列化选项（`#827 <https://github.com/ros2/rosbag2/issues/827>`__）
* 新增 delay 选项（`#789 <https://github.com/ros2/rosbag2/issues/789>`__）
* 避免将 KeyboardInterrupt 异常传递到上层（`#788 <https://github.com/ros2/rosbag2/issues/788>`__）
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Barry Xu、Cameron Miller、Chris Lalancette、Emerson Knapp、Ivan Santiago Paunovic、Jacob Perron、Jorge Perez、Kosuke Takeuchi、Michel Hidalgo、Sonia Jin、Tony Peng


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ros2cli <https://github.com/ros2/ros2cli/tree/humble/ros2cli/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 Python 3.10 下 importlib_metadata 产生的警告（`#706 <https://github.com/ros2/ros2cli/issues/706>`__）
* 为终止挂起的测试添加超时（`#701 <https://github.com/ros2/ros2cli/issues/701>`__）
* 在 DirectNode.__exit__() 中使用 try_shutdown() 替代 shutdown()（`#683 <https://github.com/ros2/ros2cli/issues/683>`__）
* 将维护者更新为 Aditya Pande、Audrow Nash 和 Michael Jeronimo（`#673 <https://github.com/ros2/ros2cli/issues/673>`__）
* 更新维护者信息（`#670 <https://github.com/ros2/ros2cli/issues/670>`__）
* 重新应用 `#659 <https://github.com/ros2/ros2cli/issues/659>`__（`#661 <https://github.com/ros2/ros2cli/issues/661>`__）
* 回退“使 ros2cli 输出始终按行缓冲”的修改（`#659 <https://github.com/ros2/ros2cli/issues/659>`__），对应回退提交 `#660 <https://github.com/ros2/ros2cli/issues/660>`__。
* 使 ros2cli 输出始终按行缓冲（`#659 <https://github.com/ros2/ros2cli/issues/659>`__）
* 在 ros2 daemon 节点名称中添加 uuid（`#658 <https://github.com/ros2/ros2cli/issues/658>`__）
* 启动时转移 daemon socket 的所有权（`#652 <https://github.com/ros2/ros2cli/issues/652>`__）
* 新增变更日志（`#635 <https://github.com/ros2/ros2cli/issues/635>`__）
* 贡献者：Aditya Pande、Audrow Nash、Chris Lalancette、Ivan Santiago Paunovic、Michel Hidalgo、Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ros2cli_test_interfaces <https://github.com/ros2/ros2cli/tree/humble/ros2cli_test_interfaces/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Aditya Pande、Audrow Nash 和 Michael Jeronimo（`#673 <https://github.com/ros2/ros2cli/issues/673>`__）
* 更新维护者信息（`#670 <https://github.com/ros2/ros2cli/issues/670>`__）
* 新增变更日志（`#635 <https://github.com/ros2/ros2cli/issues/635>`__）
* 贡献者：Aditya Pande、Audrow Nash、Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ros2component <https://github.com/ros2/ros2cli/tree/humble/ros2component/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 为终止挂起的测试添加超时（`#701 <https://github.com/ros2/ros2cli/issues/701>`__）
* 将维护者更新为 Aditya Pande、Audrow Nash 和 Michael Jeronimo（`#673 <https://github.com/ros2/ros2cli/issues/673>`__）
* 更新维护者信息（`#670 <https://github.com/ros2/ros2cli/issues/670>`__）
* 移除已弃用的 get_container_components_info() API（`#647 <https://github.com/ros2/ros2cli/issues/647>`__）
* 新增变更日志（`#635 <https://github.com/ros2/ros2cli/issues/635>`__）
* 贡献者：Aditya Pande、Audrow Nash、Ivan Santiago Paunovic、Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ros2doctor <https://github.com/ros2/ros2cli/tree/humble/ros2doctor/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
