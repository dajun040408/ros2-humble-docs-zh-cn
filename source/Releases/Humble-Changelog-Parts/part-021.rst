`ros2run <https://github.com/ros2/ros2cli/tree/humble/ros2run/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 为终止挂起的测试添加超时（`#701 <https://github.com/ros2/ros2cli/issues/701>`__）
* 将维护者更新为 Aditya Pande、Audrow Nash 和 Michael Jeronimo（`#673 <https://github.com/ros2/ros2cli/issues/673>`__）
* 更新维护者信息（`#670 <https://github.com/ros2/ros2cli/issues/670>`__）
* 检查 subprocess.returncode，以便输出错误消息（`#639 <https://github.com/ros2/ros2cli/issues/639>`__）
* 新增变更日志（`#635 <https://github.com/ros2/ros2cli/issues/635>`__）
* 贡献者：Aditya Pande、Audrow Nash、Ivan Santiago Paunovic、Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ros2service <https://github.com/ros2/ros2cli/tree/humble/ros2service/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 为终止挂起的测试添加超时（`#701 <https://github.com/ros2/ros2cli/issues/701>`__）
* 为 ``ros2 service list`` 命令同时提供 ``--include-hidden-services`` 选项（`#551 <https://github.com/ros2/ros2cli/issues/551>`__）
* 使用 launch 功能包替代 ros_testing 依赖，以避免循环依赖（`#685 <https://github.com/ros2/ros2cli/issues/685>`__）
* 将维护者更新为 Aditya Pande、Audrow Nash 和 Michael Jeronimo（`#673 <https://github.com/ros2/ros2cli/issues/673>`__）
* 更新维护者信息（`#670 <https://github.com/ros2/ros2cli/issues/670>`__）
* 新增变更日志（`#635 <https://github.com/ros2/ros2cli/issues/635>`__）
* 贡献者：Aditya Pande、Audrow Nash、Ivan Santiago Paunovic、Karsten Knese、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ros2test <https://github.com/ros2/ros_testing/tree/humble/ros2test/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 使用新的 domain_coordinator API（`#10 <https://github.com/ros2/ros_testing/issues/10>`__）
* 贡献者：Timo Röhling


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ros2topic <https://github.com/ros2/ros2cli/tree/humble/ros2topic/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 为终止挂起的测试添加超时（`#701 <https://github.com/ros2/ros2cli/issues/701>`__）
* 添加 YAML 转储的 flow 样式（`#698 <https://github.com/ros2/ros2cli/issues/698>`__）
* 支持 ros2topic echo 的 once 选项（`#695 <https://github.com/ros2/ros2cli/issues/695>`__）
* 修复 Fast DDS 不兼容 QoS 的特殊情况（`#694 <https://github.com/ros2/ros2cli/issues/694>`__）
* 使用 launch 功能包替代 ros_testing 依赖，以避免循环依赖（`#685 <https://github.com/ros2/ros2cli/issues/685>`__）
* 在可用时添加 QoS history 和 depth 信息（`#678 <https://github.com/ros2/ros2cli/issues/678>`__）
* 清理标注错误的 BSD 许可证（`#447 <https://github.com/ros2/ros2cli/issues/447>`__）
* 将维护者更新为 Aditya Pande、Audrow Nash 和 Michael Jeronimo（`#673 <https://github.com/ros2/ros2cli/issues/673>`__）
* 更新维护者信息（`#670 <https://github.com/ros2/ros2cli/issues/670>`__）
* 更新丢失消息测试用例（`#669 <https://github.com/ros2/ros2cli/issues/669>`__）
* 为 ros2 实现消息过滤功能（`#654 <https://github.com/ros2/ros2cli/issues/654>`__）
* 更改 pub 命令的默认 QoSProfile（`#653 <https://github.com/ros2/ros2cli/issues/653>`__）
* 为 ``ros2 topic pub`` 添加选项：等待 N 个匹配的订阅者；与 ``--times`` 组合使用时，默认 N=1（`#642 <https://github.com/ros2/ros2cli/issues/642>`__）
* ``ros2 topic pub`` 启动后立即开始发布（`#626 <https://github.com/ros2/ros2cli/issues/626>`__）
* 修复输出“Infinite”时的 Topic Info 测试（`#616 <https://github.com/ros2/ros2cli/issues/616>`__）
* 新增变更日志（`#635 <https://github.com/ros2/ros2cli/issues/635>`__）
* QoS 自动检测（`#613 <https://github.com/ros2/ros2cli/issues/613>`__）
* 默认启用丢失消息选项（`#633 <https://github.com/ros2/ros2cli/issues/633>`__）
* 贡献者：Aditya Pande、Audrow Nash、Chris Lalancette、Emerson Knapp、Gonzo、Ivan Santiago Paunovic、Jorge Perez、Shane Loretz、Tomoya Fujita、Tully Foote、matthews-jca


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ros2trace <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/ros2trace/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 ``ros2 trace`` 的 fini() 错误
* 不再要求必须安装内核跟踪器，并在未安装时进行检测
* 弃用 ``context_names`` 参数，改用 ``context_fields``
* 贡献者：Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosbag2 <https://github.com/ros2/rosbag2/tree/humble/rosbag2/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 提升版本号，以避免冲突
* 更新功能包维护者（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 贡献者：Chris Lalancette、Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosbag2_compression <https://github.com/ros2/rosbag2/tree/humble/rosbag2_compression/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 提升版本号，以避免冲突
* 将头文件安装到 include/${PROJECT_NAME}（`#958 <https://github.com/ros2/rosbag2/issues/958>`__）
* 移除不必要的 public 定义（`#950 <https://github.com/ros2/rosbag2/issues/950>`__）
* 适配 uncrustify 0.72（`#937 <https://github.com/ros2/rosbag2/issues/937>`__）
* 修复使用缓存时 rosbag 分割功能失效的问题（`#936 <https://github.com/ros2/rosbag2/issues/936>`__）
* 更新功能包维护者（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 避免对同一个存储文件进行多次预处理（`#895 <https://github.com/ros2/rosbag2/issues/895>`__）
* 添加 seek 接口（`#836 <https://github.com/ros2/rosbag2/issues/836>`__）
* 重构插件查询机制，并统一 trait 管理方式（`#833 <https://github.com/ros2/rosbag2/issues/833>`__）
* 修复顺序读取器切换到下一个文件的策略（`#839 <https://github.com/ros2/rosbag2/issues/839>`__）
* 通过插件查询加载压缩和序列化选项（`#827 <https://github.com/ros2/rosbag2/issues/827>`__）
* 贡献者：Cameron Miller、Chris Lalancette、Michael Orlov、Michel Hidalgo、Shane Loretz、sonia


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosbag2_compression_zstd <https://github.com/ros2/rosbag2/tree/humble/rosbag2_compression_zstd/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 提升版本号，以避免冲突
* 将头文件安装到 include/${PROJECT_NAME}（`#958 <https://github.com/ros2/rosbag2/issues/958>`__）
* 更新功能包维护者（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 贡献者：Chris Lalancette、Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosbag2_cpp <https://github.com/ros2/rosbag2/tree/humble/rosbag2_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 撤销“在 metadata.yaml 的 'custom' 字段中记录任意键值对”的功能（`#976 <https://github.com/ros2/rosbag2/issues/976>`__），对应撤销提交为（`#984 <https://github.com/ros2/rosbag2/issues/984>`__）
* 在 metadata.yaml 的 'custom' 字段中记录任意键值对（`#976 <https://github.com/ros2/rosbag2/issues/976>`__）
* 再次撤销上述“在 metadata.yaml 的 'custom' 字段中记录任意键值对”的功能（`#976 <https://github.com/ros2/rosbag2/issues/976>`__），对应撤销提交为（`#984 <https://github.com/ros2/rosbag2/issues/984>`__）
* 在 metadata.yaml 的 'custom' 字段中记录任意键值对（`#976 <https://github.com/ros2/rosbag2/issues/976>`__）
* 提升版本号，以避免冲突
* 将头文件安装到 include/${PROJECT_NAME}（`#958 <https://github.com/ros2/rosbag2/issues/958>`__）
* 移除不必要的 public 定义（`#950 <https://github.com/ros2/rosbag2/issues/950>`__）
* 修复 cpplint 的相对路径语法（`#947 <https://github.com/ros2/rosbag2/issues/947>`__）
* 为 message_cache 添加 TSA 注解（`#946 <https://github.com/ros2/rosbag2/issues/946>`__）
* 适配 uncrustify 0.72（`#937 <https://github.com/ros2/rosbag2/issues/937>`__）
* 重新设计 cache consumer 和 circular message cache，以消除忙等待循环（`#941 <https://github.com/ros2/rosbag2/issues/941>`__）
* 修复使用缓存时 rosbag 分割功能失效的问题（`#936 <https://github.com/ros2/rosbag2/issues/936>`__）
