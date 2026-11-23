* 导出现代 CMake targets（`#357 <https://github.com/ros2/rmw_cyclonedds/issues/357>`__）
* 在 rmw_destroy_node 中使用相同的 allocator 释放内存（`#355 <https://github.com/ros2/rmw_cyclonedds/issues/355>`__）
* 新增客户端/服务 QoS 获取接口（`#343 <https://github.com/ros2/rmw_cyclonedds/issues/343>`__）
* 更新版本号和质量等级（`#349 <https://github.com/ros2/rmw_cyclonedds/issues/349>`__）
* 更新功能包维护者信息（`#351 <https://github.com/ros2/rmw_cyclonedds/issues/351>`__）
* 修复零拷贝数据路径中不必要的内存初始化（`#348 <https://github.com/ros2/rmw_cyclonedds/issues/348>`__）
* 修复客户端/服务的 QoS depth 设置被忽略的问题（`#340 <https://github.com/ros2/rmw_cyclonedds/issues/340>`__）
* 在质量声明中添加 Cyclone DDS 链接（`#342 <https://github.com/ros2/rmw_cyclonedds/issues/342>`__）
* 更新 rmw_context_impl_t 定义（`#337 <https://github.com/ros2/rmw_cyclonedds/issues/337>`__）
* 为 rmw_cyclonedds_cpp 添加质量声明（`#335 <https://github.com/ros2/rmw_cyclonedds/issues/335>`__）
* 修复对已弃用 is_loan_available 的使用（`#336 <https://github.com/ros2/rmw_cyclonedds/issues/336>`__）
* 为 RISC-V 添加 -latomic（`#332 <https://github.com/ros2/rmw_cyclonedds/issues/332>`__）
* 使用 tracetools 为 pub/sub 初始化、发布和获取操作添加插桩（`#329 <https://github.com/ros2/rmw_cyclonedds/issues/329>`__）
* 如果存在 CRL，则将其传递给 CycloneDDS（`#325 <https://github.com/ros2/rmw_cyclonedds/issues/325>`__）
* 使用新的 rmw_dds_common::get_security_files API（`#323 <https://github.com/ros2/rmw_cyclonedds/issues/323>`__）
* 新增 rmw_publisher_wait_for_all_acked 支持（`#294 <https://github.com/ros2/rmw_cyclonedds/issues/294>`__）
* 修复零拷贝问题（`#309 <https://github.com/ros2/rmw_cyclonedds/issues/309>`__）
* 处理消息反序列化过程中的内存分配错误（`#313 <https://github.com/ros2/rmw_cyclonedds/issues/313>`__）
* 在 rcutils/get_env.h 弃用后更新头文件包含（`#312 <https://github.com/ros2/rmw_cyclonedds/issues/312>`__）
* 贡献者：Barry Xu、Chen Lihui、Chris Lalancette、Christophe Bedard、Dietrich Krönke、Erik Boasson、Haowei Wen、Ivan Santiago Paunovic、Jacob Perron、Joe Speed、Michel Hidalgo、Shane Loretz、Sumanth Nirmal、eboasson、guillaume-pais-siemens、iRobot ROS、mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rmw_dds_common <https://github.com/ros2/rmw_dds_common/tree/humble/rmw_dds_common/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 依赖 rosidl_typesupport_cpp 生成的 target（`#58 <https://github.com/ros2/rmw_dds_common/issues/58>`__）
* 使用 rosidl_get_typesupport_target() 和 target_link_libraries()（`#57 <https://github.com/ros2/rmw_dds_common/issues/57>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#56 <https://github.com/ros2/rmw_dds_common/issues/56>`__）
* 修复 cpplint 的头文件包含顺序（`#55 <https://github.com/ros2/rmw_dds_common/issues/55>`__）
* 修复使用 rosdoc2 时 rmw_dds_common 的文档问题（`#54 <https://github.com/ros2/rmw_dds_common/issues/54>`__）
* 新增证书吊销列表（CRL）文件支持（`#52 <https://github.com/ros2/rmw_dds_common/issues/52>`__）
* 消除 clang 的 range-loop-construct 警告（`#53 <https://github.com/ros2/rmw_dds_common/issues/53>`__）
* 新增安全文件通用函数（`#51 <https://github.com/ros2/rmw_dds_common/issues/51>`__）
* 根据 DDS 规范规范化 rmw_time_t（`#48 <https://github.com/ros2/rmw_dds_common/issues/48>`__）
* 贡献者：Andrea Sorbini、Chris Lalancette、Jacob Perron、Karsten Knese、Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rmw_fastrtps_cpp <https://github.com/ros2/rmw_fastrtps/tree/humble/rmw_fastrtps_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 使用 tracetools 为 pub/sub 初始化、发布和获取操作添加插桩（`#591 <https://github.com/ros2/rmw_fastrtps/issues/591>`__）
* 新增内容过滤话题功能（`#513 <https://github.com/ros2/rmw_fastrtps/issues/513>`__）
* 为消息信息结构添加序列号（`#587 <https://github.com/ros2/rmw_fastrtps/issues/587>`__）
* 移除 rmw_serialize.cpp 中的部分堆内存操作（`#590 <https://github.com/ros2/rmw_fastrtps/issues/590>`__）
* 新增 EventsExecutor（`#468 <https://github.com/ros2/rmw_fastrtps/issues/468>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#578 <https://github.com/ros2/rmw_fastrtps/issues/578>`__）
* 新增客户端/服务 QoS 获取接口（`#560 <https://github.com/ros2/rmw_fastrtps/issues/560>`__）
* 正确重新计算有界序列的序列化大小（`#540 <https://github.com/ros2/rmw_fastrtps/issues/540>`__）
* 修复类型大小对齐问题（`#550 <https://github.com/ros2/rmw_fastrtps/issues/550>`__）
* 将链接从 index.ros.org 更改为 docs.ros.org（`#539 <https://github.com/ros2/rmw_fastrtps/issues/539>`__）
* 新增 rmw_publisher_wait_for_all_acked 支持（`#519 <https://github.com/ros2/rmw_fastrtps/issues/519>`__）
* 实现 loaned message（`#523 <https://github.com/ros2/rmw_fastrtps/issues/523>`__）：为基础 TypeSupport 添加 is_plain_ 属性；新增基础 TypeSupport 方法；实现 rmw_borrow_loaned_message 和 rmw_return_loaned_message_from_publisher；为 plain 类型的 publisher 和 subscription 启用 loaned message；实现 loaned message 获取功能。
* 贡献者：Barry Xu、Chen Lihui、Chris Lalancette、Christophe Bedard、Ivan Santiago Paunovic、Miguel Company、Shane Loretz、WideAwakeTN、iRobot ROS、mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rmw_fastrtps_dynamic_cpp <https://github.com/ros2/rmw_fastrtps/tree/humble/rmw_fastrtps_dynamic_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 新增内容过滤话题功能（`#513 <https://github.com/ros2/rmw_fastrtps/issues/513>`__）
* 为消息信息结构添加序列号（`#587 <https://github.com/ros2/rmw_fastrtps/issues/587>`__）
* 新增 EventsExecutor（`#468 <https://github.com/ros2/rmw_fastrtps/issues/468>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#578 <https://github.com/ros2/rmw_fastrtps/issues/578>`__）
* 新增客户端/服务 QoS 获取接口（`#560 <https://github.com/ros2/rmw_fastrtps/issues/560>`__）
* 正确重新计算有界序列的序列化大小（`#540 <https://github.com/ros2/rmw_fastrtps/issues/540>`__）
* 修复类型大小对齐问题（`#550 <https://github.com/ros2/rmw_fastrtps/issues/550>`__）
* 新增 rmw_publisher_wait_for_all_acked 支持（`#519 <https://github.com/ros2/rmw_fastrtps/issues/519>`__）
* 实现 loaned message（`#523 <https://github.com/ros2/rmw_fastrtps/issues/523>`__）：为基础 TypeSupport 添加 is_plain_ 属性；新增基础 TypeSupport 方法；实现 rmw_borrow_loaned_message 和 rmw_return_loaned_message_from_publisher；为 plain 类型的 publisher 和 subscription 启用 loaned message；实现 loaned message 获取功能。
* 贡献者：Barry Xu、Chen Lihui、Ivan Santiago Paunovic、Miguel Company、Shane Loretz、iRobot ROS、mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rmw_fastrtps_shared_cpp <https://github.com/ros2/rmw_fastrtps/tree/humble/rmw_fastrtps_shared_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 Windows 平台上的代码检查警告（`#592 <https://github.com/ros2/rmw_fastrtps/issues/592>`__）
* 使用 tracetools 为 pub/sub 初始化、发布和获取操作添加插桩（`#591 <https://github.com/ros2/rmw_fastrtps/issues/591>`__）
* 新增内容过滤话题功能（`#513 <https://github.com/ros2/rmw_fastrtps/issues/513>`__）
* 为消息信息结构添加序列号（`#587 <https://github.com/ros2/rmw_fastrtps/issues/587>`__）
* 新增 EventsExecutor（`#468 <https://github.com/ros2/rmw_fastrtps/issues/468>`__）
* 完成事件支持（`#583 <https://github.com/ros2/rmw_fastrtps/issues/583>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#578 <https://github.com/ros2/rmw_fastrtps/issues/578>`__）
* 将默认行为更改为 synchronous（`#571 <https://github.com/ros2/rmw_fastrtps/issues/571>`__）
* 修复 cpplint 错误（`#574 <https://github.com/ros2/rmw_fastrtps/issues/574>`__）
* 修复与 uncrustify 0.72 的兼容问题（`#572 <https://github.com/ros2/rmw_fastrtps/issues/572>`__）
* 新增客户端/服务 QoS 获取接口（`#560 <https://github.com/ros2/rmw_fastrtps/issues/560>`__）
* 修复客户端/服务的 QoS depth 设置被忽略的问题（`#564 <https://github.com/ros2/rmw_fastrtps/issues/564>`__）
* 更新 rmw_context_impl_t 定义（`#558 <https://github.com/ros2/rmw_fastrtps/issues/558>`__）
* 更新 LoanManager，使其在内部执行锁定（`#552 <https://github.com/ros2/rmw_fastrtps/issues/552>`__）
* 如果 CRL 可用，则将其传递给 Fast-DDS（`#546 <https://github.com/ros2/rmw_fastrtps/issues/546>`__）
* 使用新的 rmw_dds_common::get_security_files（`#544 <https://github.com/ros2/rmw_fastrtps/issues/544>`__）
* 支持 SubscriptionOptions::ignore_local_publications（`#536 <https://github.com/ros2/rmw_fastrtps/issues/536>`__）
* 将链接从 index.ros.org 更改为 docs.ros.org（`#539 <https://github.com/ros2/rmw_fastrtps/issues/539>`__）
* 新增 rmw_publisher_wait_for_all_acked 支持（`#519 <https://github.com/ros2/rmw_fastrtps/issues/519>`__）
* 实现 loaned message（`#523 <https://github.com/ros2/rmw_fastrtps/issues/523>`__）：为基础 TypeSupport 添加 is_plain_ 属性；新增基础 TypeSupport 方法；实现 rmw_borrow_loaned_message 和 rmw_return_loaned_message_from_publisher；为 plain 类型的 publisher 和 subscription 启用 loaned message；实现 loaned message 获取功能。
* 将 rmw_dds_common 导出为 rmw_fastrtps_shared_cpp 的依赖（`#530 <https://github.com/ros2/rmw_fastrtps/issues/530>`__）
* 在 rcutils/get_env.h 弃用后更新头文件包含（`#529 <https://github.com/ros2/rmw_fastrtps/issues/529>`__）
* 贡献者：Audrow Nash、Barry Xu、Chen Lihui、Chris Lalancette、Christophe Bedard、Ivan Santiago Paunovic、Jacob Perron、Jose Antonio Moral、Michel Hidalgo、Miguel Company、Shane Loretz、Tomoya Fujita、iRobot ROS、mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rmw_implementation <https://github.com/ros2/rmw_implementation/tree/humble/rmw_implementation/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 新增内容过滤话题接口（`#181 <https://github.com/ros2/rmw_implementation/issues/181>`__）
* 新增 rmw_feature_supported()（`#204 <https://github.com/ros2/rmw_implementation/issues/204>`__）
* 新增 EventsExecutor（`#161 <https://github.com/ros2/rmw_implementation/issues/161>`__）
* 修复 cpplint 的相对路径包含语法（`#203 <https://github.com/ros2/rmw_implementation/issues/203>`__）
* 支持并优先使用 rmw 实现导出的 targets（`#201 <https://github.com/ros2/rmw_implementation/issues/201>`__）
* 新增客户端/服务 QoS 获取接口（`#196 <https://github.com/ros2/rmw_implementation/issues/196>`__）
* 将维护者更新为 Audrow Nash 和 Michael Carroll（`#199 <https://github.com/ros2/rmw_implementation/issues/199>`__）
* 修复重命名后的 ``rcpputils`` 头文件（`#198 <https://github.com/ros2/rmw_implementation/issues/198>`__）
* 修复 rmw_implementation 生成的文档（`#197 <https://github.com/ros2/rmw_implementation/issues/197>`__）
* 新增 rmw_publisher_wait_for_all_acked（`#188 <https://github.com/ros2/rmw_implementation/issues/188>`__）
* 尝试加载所有可用的 RMW 实现（`#189 <https://github.com/ros2/rmw_implementation/issues/189>`__）
* 在 rcutils/get_env.h 弃用后更新头文件包含（`#190 <https://github.com/ros2/rmw_implementation/issues/190>`__）
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Barry Xu、Chen Lihui、Chris Lalancette、Christophe Bedard、Ivan Santiago Paunovic、Jacob Perron、Michel Hidalgo、Shane Loretz、iRobot ROS、mauropasse
