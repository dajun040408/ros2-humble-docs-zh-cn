* 更新 launch 测试，以适配 launch 中环境变量相关变更（`#354 <https://github.com/ros2/rcutils/issues/354>`__）
* 移除 strlen 使用中的 dst_size 参数（`#353 <https://github.com/ros2/rcutils/issues/353>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#351 <https://github.com/ros2/rcutils/issues/351>`__）
* 使用 static_cast 替代 C 风格转换（`#349 <https://github.com/ros2/rcutils/issues/349>`__）
* 修复使用 rosdoc2 时的文档构建问题（`#344 <https://github.com/ros2/rcutils/issues/344>`__）
* 停止重复定义结构体（`#333 <https://github.com/ros2/rcutils/issues/333>`__）
* 显式使用 FindPython3，替代隐式使用 FindPythonInterp（`#345 <https://github.com/ros2/rcutils/issues/345>`__）
* 修复 Android 构建（`#342 <https://github.com/ros2/rcutils/issues/342>`__）
* 弃用 get_env.h，并将内容迁移到 env.{h,c}（`#340 <https://github.com/ros2/rcutils/issues/340>`__）
* 贡献者：Chris Lalancette、Christophe Bedard、Ivan Santiago Paunovic、Jacob Perron、Jorge Perez、Shane Loretz、William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`resource_retriever <https://github.com/ros/resource_retriever/tree/humble/resource_retriever/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}（`#72 <https://github.com/ros/resource_retriever/issues/72>`__）
* 修复 cpplint 的头文件包含顺序（`#69 <https://github.com/ros/resource_retriever/issues/69>`__）
* 更新维护者信息（`#66 <https://github.com/ros/resource_retriever/issues/66>`__）
* 移除已弃用的 retriever.h 头文件（`#63 <https://github.com/ros/resource_retriever/issues/63>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Jacob Perron、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rmw <https://github.com/ros2/rmw/tree/humble/rmw/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 新增内容过滤话题支持（`#302 <https://github.com/ros2/rmw/issues/302>`__）
* 为 rmw_message_info_t 添加序列号（`#318 <https://github.com/ros2/rmw/issues/318>`__）
* 新增 rmw_feature_supported()（`#318 <https://github.com/ros2/rmw/issues/318>`__）
* 新增 EventsExecutor（`#286 <https://github.com/ros2/rmw/issues/286>`__）
* 说明 rmw_wait() 应使用单调时钟（`#316 <https://github.com/ros2/rmw/issues/316>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#317 <https://github.com/ros2/rmw/issues/317>`__）
* 更新 rmw_server_is_available() API 文档（`#277 <https://github.com/ros2/rmw/issues/277>`__）
* 新增客户端/服务 QoS 获取接口（`#314 <https://github.com/ros2/rmw/issues/314>`__）
* 修复使用 rosdoc2 时 rmw 的文档构建问题（`#313 <https://github.com/ros2/rmw/issues/313>`__）
* 修复 Doxygen 文档中的错误（`#311 <https://github.com/ros2/rmw/issues/311>`__）
* 修复 rmw_get_gid_for_publisher API 文档中的复制粘贴错误（`#310 <https://github.com/ros2/rmw/issues/310>`__）
* 新增 rmw_publisher_wait_for_all_acked 支持（`#296 <https://github.com/ros2/rmw/issues/296>`__）
* 贡献者：Barry Xu、Chen Lihui、Chris Lalancette、Christophe Bedard、Ivan Santiago Paunovic、Michel Hidalgo、Shane Loretz、iRobot ROS、mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rmw_connextdds <https://github.com/ros2/rmw_connextdds/tree/humble/rmw_connextdds/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 构建 rmw_connextddsmicro 时排除缺失的 sample info 字段（`#79 <https://github.com/ros2/rmw_connextdds/issues/79>`__）
* 更新 launch_testing_ros 的输出过滤前缀，以适配 Connext6（`#80 <https://github.com/ros2/rmw_connextdds/issues/80>`__）
* 支持用户指定的内容过滤器（`#68 <https://github.com/ros2/rmw_connextdds/issues/68>`__）
* 为内容过滤话题添加存根实现（`#77 <https://github.com/ros2/rmw_connextdds/issues/77>`__）
* 新增 rmw listener API（`#44 <https://github.com/rticommunity/rmw_connextdds/issues/44>`__）
* 新增客户端/服务 QoS 获取接口（`#67 <https://github.com/ros2/rmw_connextdds/issues/67>`__）
* 新增 rmw_publisher_wait_for_all_acked 支持（`#20 <https://github.com/rticommunity/rmw_connextdds/issues/20>`__）
* 贡献者：Andrea Sorbini、Barry Xu、Chen Lihui、Ivan Santiago Paunovic、iRobot ROS、mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rmw_connextdds_common <https://github.com/ros2/rmw_connextdds/tree/humble/rmw_connextdds_common/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 构建 rmw_connextddsmicro 时排除缺失的 sample info 字段（`#79 <https://github.com/ros2/rmw_connextdds/issues/79>`__）
* 在使用 CDR 流进行过滤前正确初始化它（`#81 <https://github.com/ros2/rmw_connextdds/issues/81>`__）
* 支持用户指定的内容过滤器（`#68 <https://github.com/ros2/rmw_connextdds/issues/68>`__）
* 为内容过滤话题添加存根实现（`#77 <https://github.com/ros2/rmw_connextdds/issues/77>`__）
* 为消息信息结构添加序列号（`#74 <https://github.com/ros2/rmw_connextdds/issues/74>`__）
* 新增 rmw listener API（`#44 <https://github.com/rticommunity/rmw_connextdds/issues/44>`__）
* 修复 cpplint 错误（`#69 <https://github.com/ros2/rmw_connextdds/issues/69>`__）
* 新增客户端/服务 QoS 获取接口（`#67 <https://github.com/rticommunity/rmw_connextdds/issues/67>`__）
* 更新 rmw_context_impl_t 定义（`#65 <https://github.com/ros2/rmw_connextdds/issues/65>`__）
* 使用新的 rmw_dds_common::get_security_files API（`#61 <https://github.com/ros2/rmw_connextdds/issues/61>`__）
* 新增 rmw_publisher_wait_for_all_acked 支持（`#20 <https://github.com/rticommunity/rmw_connextdds/issues/20>`__）
* 支持 rosidl_typesupport_fastrtps_cpp 中 ``message_type_support_callbacks_t::max_serialized_size()`` 的扩展签名（`#14 <https://github.com/ros2/rmw_connextdds/issues/14>`__）
* 在 rcutils/get_env.h 弃用后更新头文件包含（`#55 <https://github.com/ros2/rmw_connextdds/issues/55>`__）
* 无论覆盖策略如何，始终修改 UserObjectQosPolicy（`#53 <https://github.com/ros2/rmw_connextdds/issues/53>`__）
* 改进 ROS 与 DDS 格式之间的时间值转换（`#43 <https://github.com/ros2/rmw_connextdds/issues/43>`__）
* 允许与 C++ 应用共享 DomainParticipant（`#25 <https://github.com/ros2/rmw_connextdds/issues/25>`__）
* 新增环境变量，以控制 DomainParticipantQos 的覆盖（`#41 <https://github.com/ros2/rmw_connextdds/issues/41>`__）
* 贡献者：Andrea Sorbini、Barry Xu、Chen Lihui、Chris Lalancette、Christophe Bedard、Ivan Santiago Paunovic、Jacob Perron、Michel Hidalgo、Miguel Company、iRobot ROS、mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rmw_connextddsmicro <https://github.com/ros2/rmw_connextdds/tree/humble/rmw_connextddsmicro/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 构建 rmw_connextddsmicro 时排除缺失的 sample info 字段（`#79 <https://github.com/ros2/rmw_connextdds/issues/79>`__）
* 支持用户指定的内容过滤器（`#68 <https://github.com/ros2/rmw_connextdds/issues/68>`__）
* 为内容过滤话题添加存根实现（`#77 <https://github.com/ros2/rmw_connextdds/issues/77>`__）
* 为消息信息结构添加序列号（`#74 <https://github.com/ros2/rmw_connextdds/issues/74>`__）
* 新增 rmw listener API（`#44 <https://github.com/rticommunity/rmw_connextdds/issues/44>`__）
* 新增客户端/服务 QoS 获取接口（`#67 <https://github.com/ros2/rmw_connextdds/issues/67>`__）
* 新增 rmw_publisher_wait_for_all_acked 支持（`#20 <https://github.com/rticommunity/rmw_connextdds/issues/20>`__）
* 贡献者：Andrea Sorbini、Barry Xu、Chen Lihui、Ivan Santiago Paunovic、iRobot ROS、mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rmw_cyclonedds_cpp <https://github.com/ros2/rmw_cyclonedds/tree/humble/rmw_cyclonedds_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 get_topic_name 和长服务名称的处理
* 为 SDK_DATA 添加序列化支持
* 为 loan API 增加额外检查
* 仅依赖 rmw_dds_common::rmw_dds_common_library（`#385 <https://github.com/ros2/rmw_cyclonedds/issues/385>`__）
* 修复 rmw_init_options_copy() 中的错误消息（`#380 <https://github.com/ros2/rmw_cyclonedds/issues/380>`__）
* 新增内容过滤话题功能的空存根（`#289 <https://github.com/ros2/rmw_cyclonedds/issues/289>`__）
* 更新以适配 Cyclone 0.9.0 和 Iceoryx 2.0（`#379 <https://github.com/ros2/rmw_cyclonedds/issues/379>`__）
* 将消息信息序列号标记为不支持，并实现 rmw_feature_supported()（`#381 <https://github.com/ros2/rmw_cyclonedds/issues/381>`__）
* 通过将指针设为 nullptr 修复警告（`#375 <https://github.com/ros2/rmw_cyclonedds/issues/375>`__）
* 将 QDs 升级到 QL2（`#371 <https://github.com/ros2/rmw_cyclonedds/issues/371>`__）
* 新增 EventsExecutor（`#256 <https://github.com/ros2/rmw_cyclonedds/issues/256>`__）
* 在 rmw_destroy_subscription 中调用 dissociate_reader
* 使用 try-catch 块包裹新 serdata_rmw 的创建过程
* 修复 SHM 发布端错误场景中的内存泄漏
* 修复 SHM 获取端的内存泄漏
* 将 _cyclonedds_has_shm 重命名，以符合命名约定
* 将 iceoryx_binding_c 添加为 rmw_cyclonedds_cpp 依赖
* 如果 iox_chunk 仍可用，则在 serdata_free 中将其释放回 iceoryx
* 从 iox chunk 构建 serdata 时同步更新 iceoryx_subscriber
* 修复 cpplint 错误（`#363 <https://github.com/ros2/rmw_cyclonedds/issues/363>`__）
* 更新以适配 uncrustify 0.72（`#358 <https://github.com/ros2/rmw_cyclonedds/issues/358>`__）
* 仅向下游目标导出 rmw::rmw（`#360 <https://github.com/ros2/rmw_cyclonedds/issues/360>`__）
