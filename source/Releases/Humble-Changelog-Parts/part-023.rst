`rosbag2_test_common <https://github.com/ros2/rosbag2/tree/humble/rosbag2_test_common/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 提升版本号，以避免冲突
* 将头文件安装到 include/${PROJECT_NAME}（`#958 <https://github.com/ros2/rosbag2/issues/958>`__）
* 更新功能包维护者（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 在发布消息之前，确保订阅关系已经建立（`#804 <https://github.com/ros2/rosbag2/issues/804>`__）
* 在录制过程中优雅地处理 SIGTERM（`#792 <https://github.com/ros2/rosbag2/issues/792>`__）
* 为 PublicationManager 添加 spin_and_wait_for_matched，并更新相应测试用例（`#797 <https://github.com/ros2/rosbag2/issues/797>`__）
* 避免将 KeyboardInterrupt 异常传递到上层（`#788 <https://github.com/ros2/rosbag2/issues/788>`__）
* 贡献者：Barry Xu、Chris Lalancette、Emerson Knapp、Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosbag2_tests <https://github.com/ros2/rosbag2/tree/humble/rosbag2_tests/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 撤销“在 metadata.yaml 的 'custom' 字段中记录任意键值对”的功能（`#976 <https://github.com/ros2/rosbag2/issues/976>`__），对应撤销提交为（`#984 <https://github.com/ros2/rosbag2/issues/984>`__）
* 在 metadata.yaml 的 'custom' 字段中记录任意键值对（`#976 <https://github.com/ros2/rosbag2/issues/976>`__）
* 再次撤销上述“在 metadata.yaml 的 'custom' 字段中记录任意键值对”的功能（`#976 <https://github.com/ros2/rosbag2/issues/976>`__），对应撤销提交为（`#984 <https://github.com/ros2/rosbag2/issues/984>`__）
* 在 metadata.yaml 的 'custom' 字段中记录任意键值对（`#976 <https://github.com/ros2/rosbag2/issues/976>`__）
* 提升版本号，以避免冲突
* 为 bag recorder 添加暂停/恢复选项（`#905 <https://github.com/ros2/rosbag2/issues/905>`__）
* 更新功能包维护者（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 修复使用“MESSAGE”压缩时无效指针地址的问题（`#866 <https://github.com/ros2/rosbag2/issues/866>`__）
* 为每个文件添加元数据信息（`#870 <https://github.com/ros2/rosbag2/issues/870>`__）
* 根据插件查询机制的变化修复 record 测试（`#838 <https://github.com/ros2/rosbag2/issues/838>`__）
* 在发布消息之前，确保订阅关系已经建立（`#804 <https://github.com/ros2/rosbag2/issues/804>`__）
* 在录制过程中优雅地处理 SIGTERM（`#792 <https://github.com/ros2/rosbag2/issues/792>`__）
* 为 PublicationManager 添加 spin_and_wait_for_matched，并更新相应测试用例（`#797 <https://github.com/ros2/rosbag2/issues/797>`__）
* 从 rosbag2_tests 中移除 rmw_fastrtps_cpp 的 find_package（`#774 <https://github.com/ros2/rosbag2/issues/774>`__）
* 贡献者：Audrow Nash、Barry Xu、Cameron Miller、Chris Lalancette、Emerson Knapp、Ivan Santiago Paunovic、Jorge Perez、Michel Hidalgo、Tony Peng、Wojciech Jaworski


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosbag2_transport <https://github.com/ros2/rosbag2/tree/humble/rosbag2_transport/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 支持以 loaned message（借用消息）的形式发布（`#981 <https://github.com/ros2/rosbag2/issues/981>`__）
* 支持以 loaned message（借用消息）的形式发布（`#981 <https://github.com/ros2/rosbag2/issues/981>`__）
* 提升版本号，以避免冲突
* 为 Player 添加 burst-mode（突发模式）（`#977 <https://github.com/ros2/rosbag2/issues/977>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#958 <https://github.com/ros2/rosbag2/issues/958>`__）
* 确保播放模式下发布的消息得到确认（`#951 <https://github.com/ros2/rosbag2/issues/951>`__）
* 适配 uncrustify 0.72（`#937 <https://github.com/ros2/rosbag2/issues/937>`__）
* TopicFilter 使用 regex_search 替代 regex_match（`#932 <https://github.com/ros2/rosbag2/issues/932>`__）
* 添加 start-offset 播放选项（`#931 <https://github.com/ros2/rosbag2/issues/931>`__）
* 在 OSX 上添加 Clang 建议的括号，以修复构建警告（`#930 <https://github.com/ros2/rosbag2/issues/930>`__）
* Bag 重写功能（C++）（`#920 <https://github.com/ros2/rosbag2/issues/920>`__）
* 为 recorder 添加“忽略叶子话题”选项（`#925 <https://github.com/ros2/rosbag2/issues/925>`__）
* 重写 TopicFilter，使其可通过单次调用重复使用（`#924 <https://github.com/ros2/rosbag2/issues/924>`__）
* 添加 ReaderWriterFactory 工具，以便复用共享逻辑（`#923 <https://github.com/ros2/rosbag2/issues/923>`__）
* 为 bag recorder 添加暂停/恢复选项（`#905 <https://github.com/ros2/rosbag2/issues/905>`__）
* 为 rosbag2_transport 添加日志宏（`#917 <https://github.com/ros2/rosbag2/issues/917>`__）
* 为 RecordOptions 和 StorageOptions 启用 YAML 编码/解码（`#916 <https://github.com/ros2/rosbag2/issues/916>`__）
* 暴露 QoS 对象封装器（`#910 <https://github.com/ros2/rosbag2/issues/910>`__）
* 为 ``ros2 bag play`` 添加 ``--start-paused`` 选项（`#904 <https://github.com/ros2/rosbag2/issues/904>`__）
* 更新功能包维护者（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 添加 Seek 服务（`#874 <https://github.com/ros2/rosbag2/issues/874>`__）
* 为播放速率添加简单的键盘控制（`#893 <https://github.com/ros2/rosbag2/issues/893>`__）
* 修复使用“MESSAGE”压缩时无效指针地址的问题（`#866 <https://github.com/ros2/rosbag2/issues/866>`__）
* 修复拼写错误（`#880 <https://github.com/ros2/rosbag2/issues/880>`__）
* 在 Player 中使用 Reader 的 seek() 方法进行定位/跳转（`#873 <https://github.com/ros2/rosbag2/issues/873>`__）
* 添加用于暂停/恢复切换及播放下一条消息的键盘控制（`#847 <https://github.com/ros2/rosbag2/issues/847>`__）
* 实现快照机制及对应的 ROS Service（`#850 <https://github.com/ros2/rosbag2/issues/850>`__）
* 为快照功能实现循环消息缓存（`#844 <https://github.com/ros2/rosbag2/issues/844>`__）
* 为 Player 类添加 jump/seek API（`#826 <https://github.com/ros2/rosbag2/issues/826>`__）
* 将 test_play_timing 重构为每种情况对应一个测试，以便定位超时用例（`#863 <https://github.com/ros2/rosbag2/issues/863>`__）
* 修复发现未知消息类型后发现过程会静默停止的问题（`#848 <https://github.com/ros2/rosbag2/issues/848>`__）
* 修复已弃用订阅回调的警告（`#852 <https://github.com/ros2/rosbag2/issues/852>`__）
* 修复 Player::peek_next_message_from_queue() 中的竞态条件（`#849 <https://github.com/ros2/rosbag2/issues/849>`__）
* 添加 seek 接口（`#836 <https://github.com/ros2/rosbag2/issues/836>`__）
* 将 ``PlayOptions::delay`` 更新为 ``rclcpp::Duration``，以获得纳秒级分辨率（`#843 <https://github.com/ros2/rosbag2/issues/843>`__）
* 将“已准备好播放”的通知移入 play_messages_from_queue()（`#832 <https://github.com/ros2/rosbag2/issues/832>`__）
* 在 Player::play_next() 方法中等待 Player 准备好播放（`#814 <https://github.com/ros2/rosbag2/issues/814>`__）
* 在发布消息之前，确保订阅关系已经建立（`#804 <https://github.com/ros2/rosbag2/issues/804>`__）
* 添加 delay 选项（`#789 <https://github.com/ros2/rosbag2/issues/789>`__）
* 将 recorder 的 QoS 配置文件复制到局部变量，避免临时值被清除（`#803 <https://github.com/ros2/rosbag2/issues/803>`__）
* test_play_services：在 future 出错时优雅地失败（`#798 <https://github.com/ros2/rosbag2/issues/798>`__）
* 修复同时使用 --all 和 --exclude 进行录制的问题（`#765 <https://github.com/ros2/rosbag2/issues/765>`__）
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Barry Xu、Bastian Jäger、Cameron Miller、Chris Lalancette、Emerson Knapp、Geoffrey Biggs、Ivan Santiago Paunovic、Kosuke Takeuchi、Lei Liu、Louise Poubel、Michael Orlov、Michel Hidalgo、Piotr Jaroszek、Shane Loretz、sonia


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosgraph_msgs <https://github.com/ros2/rcl_interfaces/tree/humble/rosgraph_msgs/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Chris Lalancette（`#130 <https://github.com/ros2/rcl_interfaces/issues/130>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_adapter <https://github.com/ros2/rosidl/tree/humble/rosidl_adapter/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 重命名嵌套循环的索引变量（`#643 <https://github.com/ros2/rosidl/issues/643>`__）
* 修复 action 接口中注释的处理方式（`#632 <https://github.com/ros2/rosidl/issues/632>`__）
* 将 ROS 接口常量中的注释传递到生成的 .idl 文件（`#630 <https://github.com/ros2/rosidl/issues/630>`__）
* 更新功能包维护者（`#624 <https://github.com/ros2/rosidl/issues/624>`__）
* 使 rosidl 功能包使用 FindPython3，而不是 FindPythonInterp（`#612 <https://github.com/ros2/rosidl/issues/612>`__）
* 修复字符串字面量中的转义问题（`#595 <https://github.com/ros2/rosidl/issues/595>`__）
* 忽略多个 ``#`` 字符并对注释取消缩进（`#594 <https://github.com/ros2/rosidl/issues/594>`__）
* 贡献者：Ivan Santiago Paunovic、Michel Hidalgo、Shane Loretz、ibnHatab


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_cli <https://github.com/ros2/rosidl/tree/humble/rosidl_cli/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 Python 3.10 下的 importlib_metdata 警告（`#674 <https://github.com/ros2/rosidl/issues/674>`__）
* 将维护者更新为 Michel Hidalgo 和 Shane Loretz（`#633 <https://github.com/ros2/rosidl/issues/633>`__）
* 更新功能包维护者（`#624 <https://github.com/ros2/rosidl/issues/624>`__）
* 支持向 rosidl CLI 扩展传递关键字参数（`#597 <https://github.com/ros2/rosidl/issues/597>`__）
* 为格式化字符串补充缺失的 f 前缀（`#600 <https://github.com/ros2/rosidl/issues/600>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_cmake <https://github.com/ros2/rosidl/tree/humble/rosidl_cmake/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
