* 从 PlayerClock/TimeControllerClock 中移除 JumpHandler 的复制实现（`#935 <https://github.com/ros2/rosbag2/issues/935>`__）
* 自动检测 Reader 的 storage_id（如果可行）（`#918 <https://github.com/ros2/rosbag2/issues/918>`__）
* 为 ``ros2 bag play`` 添加 ``--start-paused`` 选项（`#904 <https://github.com/ros2/rosbag2/issues/904>`__）
* 使用 message_introspection 头文件获取 MessageMember（`#903 <https://github.com/ros2/rosbag2/issues/903>`__）
* 更新功能包维护者（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 修复 record 命令的 converter 插件选项（`#897 <https://github.com/ros2/rosbag2/issues/897>`__）
* 仅在代码确实能够运行时启用 sanitizers（`#572 <https://github.com/ros2/rosbag2/issues/572>`__）
* 必须向 converter 插件传递 introspection TS，才能使其发挥作用（`#896 <https://github.com/ros2/rosbag2/issues/896>`__）
* 避免对同一个存储文件进行多次预处理（`#895 <https://github.com/ros2/rosbag2/issues/895>`__）
* 修复使用“MESSAGE”压缩时无效指针地址的问题（`#866 <https://github.com/ros2/rosbag2/issues/866>`__）
* 为每个文件添加元数据信息（`#870 <https://github.com/ros2/rosbag2/issues/870>`__）
* 修复使用 clang 线程分析构建时出现的 TSA 警告（`#877 <https://github.com/ros2/rosbag2/issues/877>`__）
* 实现快照机制及对应的 ROS Service（`#850 <https://github.com/ros2/rosbag2/issues/850>`__）
* 为快照功能实现循环消息缓存（`#844 <https://github.com/ros2/rosbag2/issues/844>`__）
* 修复发现未知消息类型后发现过程会静默停止的问题（`#848 <https://github.com/ros2/rosbag2/issues/848>`__）
* 添加 seek 接口（`#836 <https://github.com/ros2/rosbag2/issues/836>`__）
* 重构插件查询机制，并统一 trait 管理方式（`#833 <https://github.com/ros2/rosbag2/issues/833>`__）
* 修复顺序读取器切换到下一个文件的策略（`#839 <https://github.com/ros2/rosbag2/issues/839>`__）
* 通过插件查询加载压缩和序列化选项（`#827 <https://github.com/ros2/rosbag2/issues/827>`__）
* 规避时间控制器 jump 回调 API 中 clang 线程安全分析产生的误报（`#799 <https://github.com/ros2/rosbag2/issues/799>`__）
* 为 PlayerClock::jump(time_point) API 添加回调，并修复 CI（`#779 <https://github.com/ros2/rosbag2/issues/779>`__）
* 撤销“为 PlayerClock::jump(time_point) API 添加回调”的修改（`#775 <https://github.com/ros2/rosbag2/issues/775>`__），撤销提交为（`#778 <https://github.com/ros2/rosbag2/issues/778>`__）
* 为 PlayerClock::jump(time_point) API 添加回调（`#775 <https://github.com/ros2/rosbag2/issues/775>`__）
* 贡献者：Audrow Nash、Barry Xu、Cameron Miller、Chris Lalancette、Emerson Knapp、Ivan Santiago Paunovic、Jacob Perron、Jorge Perez、Lei Liu、Michael Orlov、Michel Hidalgo、Shane Loretz、Tony Peng、Wojciech Jaworski、sonia


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosbag2_interfaces <https://github.com/ros2/rosbag2/tree/humble/rosbag2_interfaces/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 提升版本号，以避免冲突
* 为 Player 添加 burst-mode（突发模式）（`#977 <https://github.com/ros2/rosbag2/issues/977>`__）
* 更新功能包维护者（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 实现快照机制及对应的 ROS Service（`#850 <https://github.com/ros2/rosbag2/issues/850>`__）：为 recorder 节点添加快照服务；简化并明确双缓冲模式。
* 贡献者：Cameron Miller、Chris Lalancette、Geoffrey Biggs、Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosbag2_performance_benchmarking <https://github.com/ros2/rosbag2/tree/humble/rosbag2_performance/rosbag2_performance_benchmarking/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 提升版本号，以避免冲突
* 将头文件安装到 include/${PROJECT_NAME}（`#958 <https://github.com/ros2/rosbag2/issues/958>`__）
* 为 RecordOptions 和 StorageOptions 启用 YAML 编码/解码（`#916 <https://github.com/ros2/rosbag2/issues/916>`__）：支持这两类选项的 YAML 编码和解码。
* 更新功能包维护者（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 将节点的 declare_parameter 更新为新语法（`#882 <https://github.com/ros2/rosbag2/issues/882>`__）
* 更新基准测试功能包，改用 writer 的 close()，替代旧的 reset()（`#881 <https://github.com/ros2/rosbag2/issues/881>`__）
* 贡献者：Adam Dąbrowski、Chris Lalancette、Emerson Knapp、Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosbag2_py <https://github.com/ros2/rosbag2/tree/humble/rosbag2_py/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 支持以 loaned message（借用消息）的形式发布（`#981 <https://github.com/ros2/rosbag2/issues/981>`__）
* 撤销“在 metadata.yaml 的 'custom' 字段中记录任意键值对”的功能（`#976 <https://github.com/ros2/rosbag2/issues/976>`__），对应撤销提交为（`#984 <https://github.com/ros2/rosbag2/issues/984>`__）
* 在 metadata.yaml 的 'custom' 字段中记录任意键值对（`#976 <https://github.com/ros2/rosbag2/issues/976>`__）
* 支持以 loaned message（借用消息）的形式发布（`#981 <https://github.com/ros2/rosbag2/issues/981>`__）
* 再次撤销“在 metadata.yaml 的 'custom' 字段中记录任意键值对”的功能（`#976 <https://github.com/ros2/rosbag2/issues/976>`__），对应撤销提交为（`#984 <https://github.com/ros2/rosbag2/issues/984>`__）
* 在 metadata.yaml 的 'custom' 字段中记录任意键值对（`#976 <https://github.com/ros2/rosbag2/issues/976>`__）
* 提升版本号，以避免冲突
* 确保播放模式下发布的消息得到确认（`#951 <https://github.com/ros2/rosbag2/issues/951>`__）
* 修复 cpplint 的相对路径语法（`#947 <https://github.com/ros2/rosbag2/issues/947>`__）
* 更新至 pybind11 2.7.1（`#945 <https://github.com/ros2/rosbag2/issues/945>`__）
* 添加 start-offset 播放选项（`#931 <https://github.com/ros2/rosbag2/issues/931>`__）
* 将 bag_rewrite 暴露为 ``ros2 bag convert`` 命令（`#921 <https://github.com/ros2/rosbag2/issues/921>`__）
* 为 recorder 添加“忽略叶子话题”选项（`#925 <https://github.com/ros2/rosbag2/issues/925>`__）
* 添加 ReaderWriterFactory 工具，以便复用共享逻辑（`#923 <https://github.com/ros2/rosbag2/issues/923>`__）
* 为 bag recorder 添加暂停/恢复选项（`#905 <https://github.com/ros2/rosbag2/issues/905>`__）
* 为 ``ros2 bag play`` 添加 ``--start-paused`` 选项（`#904 <https://github.com/ros2/rosbag2/issues/904>`__）
* 更新功能包维护者（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 修复 record 命令的 converter 插件选项（`#897 <https://github.com/ros2/rosbag2/issues/897>`__）
* 为每个文件添加元数据信息（`#870 <https://github.com/ros2/rosbag2/issues/870>`__）
* 添加用于暂停/恢复切换及播放下一条消息的键盘控制（`#847 <https://github.com/ros2/rosbag2/issues/847>`__）
* 为 record 命令添加 ``--snapshot-mode`` 参数（`#851 <https://github.com/ros2/rosbag2/issues/851>`__）
* 在 rosbag2_py 中添加 stopRecording（`#854 <https://github.com/ros2/rosbag2/issues/854>`__）
* 添加 seek 接口（`#836 <https://github.com/ros2/rosbag2/issues/836>`__）
* 重构插件查询机制，并统一 trait 管理方式（`#833 <https://github.com/ros2/rosbag2/issues/833>`__）
* 将 ``PlayOptions::delay`` 更新为 ``rclcpp::Duration``，以获得纳秒级分辨率（`#843 <https://github.com/ros2/rosbag2/issues/843>`__）
* 通过插件查询加载压缩和序列化选项（`#827 <https://github.com/ros2/rosbag2/issues/827>`__）
* 添加 delay 选项（`#789 <https://github.com/ros2/rosbag2/issues/789>`__）
* 在录制过程中优雅地处理 SIGTERM（`#792 <https://github.com/ros2/rosbag2/issues/792>`__）
* 贡献者：Abrar Rahman Protyasha、Afonso da Fonseca Braga、Audrow Nash、Barry Xu、Cameron Miller、Chris Lalancette、Emerson Knapp、Ivan Santiago Paunovic、Jacob Perron、Jorge Perez、Kosuke Takeuchi、Michel Hidalgo、Tony Peng、Wojciech Jaworski、sonia


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosbag2_storage <https://github.com/ros2/rosbag2/tree/humble/rosbag2_storage/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 撤销“在 metadata.yaml 的 'custom' 字段中记录任意键值对”的功能（`#976 <https://github.com/ros2/rosbag2/issues/976>`__），对应撤销提交为（`#984 <https://github.com/ros2/rosbag2/issues/984>`__）
* 在 metadata.yaml 的 'custom' 字段中记录任意键值对（`#976 <https://github.com/ros2/rosbag2/issues/976>`__）
* 再次撤销“在 metadata.yaml 的 'custom' 字段中记录任意键值对”的功能（`#976 <https://github.com/ros2/rosbag2/issues/976>`__），对应撤销提交为（`#984 <https://github.com/ros2/rosbag2/issues/984>`__）
* 在 metadata.yaml 的 'custom' 字段中记录任意键值对（`#976 <https://github.com/ros2/rosbag2/issues/976>`__）
* 提升版本号，以避免冲突
* 将头文件安装到 include/${PROJECT_NAME}（`#958 <https://github.com/ros2/rosbag2/issues/958>`__）
* 移除不必要的 public 定义（`#950 <https://github.com/ros2/rosbag2/issues/950>`__）
* 为 RecordOptions 和 StorageOptions 启用 YAML 编码/解码（`#916 <https://github.com/ros2/rosbag2/issues/916>`__）
* 更新功能包维护者（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 提供 MetadataIO 接口，除文件 I/O 方式外，还可以在内存中将元数据转换为字符串（`#894 <https://github.com/ros2/rosbag2/issues/894>`__）
* 为每个文件添加元数据信息（`#870 <https://github.com/ros2/rosbag2/issues/870>`__）
* 实现快照机制及对应的 ROS Service（`#850 <https://github.com/ros2/rosbag2/issues/850>`__）
* 添加 seek 接口（`#836 <https://github.com/ros2/rosbag2/issues/836>`__）
* 重构插件查询机制，并统一 trait 管理方式（`#833 <https://github.com/ros2/rosbag2/issues/833>`__）
* 贡献者：Audrow Nash、Cameron Miller、Chris Lalancette、Emerson Knapp、Jorge Perez、Michel Hidalgo、Shane Loretz、Tony Peng、Wojciech Jaworski、sonia


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosbag2_storage_default_plugins <https://github.com/ros2/rosbag2/tree/humble/rosbag2_storage_default_plugins/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 提升版本号，以避免冲突
* 将头文件安装到 include/${PROJECT_NAME}（`#958 <https://github.com/ros2/rosbag2/issues/958>`__）
* 当消息对于 SQLite 来说过大时，发出警告而不是直接崩溃（`#919 <https://github.com/ros2/rosbag2/issues/919>`__）
* 为 RecordOptions 和 StorageOptions 启用 YAML 编码/解码（`#916 <https://github.com/ros2/rosbag2/issues/916>`__）
* 更新功能包维护者（`#899 <https://github.com/ros2/rosbag2/issues/899>`__）
* 添加 seek 接口（`#836 <https://github.com/ros2/rosbag2/issues/836>`__）
* 贡献者：Chris Lalancette、Emerson Knapp、Michel Hidalgo、Shane Loretz、William Woodall、sonia
