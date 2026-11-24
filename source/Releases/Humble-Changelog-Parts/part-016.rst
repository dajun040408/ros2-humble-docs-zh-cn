* 修复 rosdoc2 相关问题（`#1897 <https://github.com/ros2/rclcpp/issues/1897>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#1888 <https://github.com/ros2/rclcpp/issues/1888>`__）
* LifecycleNode::on_deactivate 停用所有受管理实体（`#1885 <https://github.com/ros2/rclcpp/issues/1885>`__）
* 节点发生状态转换时，自动转换生命周期实体（`#1863 <https://github.com/ros2/rclcpp/issues/1863>`__）
* 根据请求移除作者信息（`#1818 <https://github.com/ros2/rclcpp/issues/1818>`__）
* 更新维护者信息（`#1817 <https://github.com/ros2/rclcpp/issues/1817>`__）
* 抑制基准测试中的 clang dead-store 警告（`#1802 <https://github.com/ros2/rclcpp/issues/1802>`__）
* 更新 ``rcl_lifecycle`` 类型的前向声明（`#1788 <https://github.com/ros2/rclcpp/issues/1788>`__）
* 弃用 ``void shared_ptr<MessageT>`` 形式的订阅回调签名（`#1713 <https://github.com/ros2/rclcpp/issues/1713>`__）
* 更新客户端 API，使其能够移除待处理请求（`#1734 <https://github.com/ros2/rclcpp/issues/1734>`__）
* 更改 lifecycle_publisher 的日志级别（`#1715 <https://github.com/ros2/rclcpp/issues/1715>`__）
* 将 RCLCPP_PUBLIC 修正为 RCLCPP_LIFECYCLE_PUBLIC（`#1732 <https://github.com/ros2/rclcpp/issues/1732>`__）
* 使用 rcpputils/scope_exit.hpp，并移除 rclcpp/scope_exit.hpp（`#1727 <https://github.com/ros2/rclcpp/issues/1727>`__）
* 移除不安全的 get_callback_groups API。调用方应改用 for_each_callback_group()，或在内部保存所需的回调组。
* 新增 ``callback_groups_for_each()``，以确保对 ``callback_groups_`` 向量的访问具备线程安全性。该方法接收 std::function，由调用方提供回调，内部负责加锁；并将原先使用 get_callback_groups() 的位置改为 callback_groups_for_each()。
* 修复生命周期基准测试中的析构顺序（`#1675 <https://github.com/ros2/rclcpp/issues/1675>`__）
* [rclcpp] 类型适配功能（`#1557 <https://github.com/ros2/rclcpp/issues/1557>`__）
* 贡献者：Abrar Rahman Protyasha、Alberto Soragna、Audrow Nash、Chris Lalancette、Christophe Bedard、Ivan Santiago Paunovic、Jacob Perron、Michel Hidalgo、Shane Loretz、Tomoya Fujita、William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rclpy <https://github.com/ros2/rclpy/tree/humble/rclpy/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 显式声明 rclpy 依赖（`#906 <https://github.com/ros2/rclpy/issues/906>`__）
* 使用 override 设置 use_sim_time 时，避免在 Node 构造函数中抛出异常（`#896 <https://github.com/ros2/rclpy/issues/896>`__）
* 定时器取消后，time_until_next_call 返回最大值（`#910 <https://github.com/ros2/rclpy/issues/910>`__）
* 正确实现 action server/client 句柄清理（`#905 <https://github.com/ros2/rclpy/issues/905>`__）
* 确保从 Action{Client,Server} 中移除 contexts（`#904 <https://github.com/ros2/rclpy/issues/904>`__）
* 使用完毕后确保释放 goal_status_array（`#902 <https://github.com/ros2/rclpy/issues/902>`__）
* 修复 Node.destroy_rate() 的返回结果（`#901 <https://github.com/ros2/rclpy/issues/901>`__）
* 移除测试中的 fastrtps 定制（`#895 <https://github.com/ros2/rclpy/issues/895>`__）
* 修复拼写错误（`#890 <https://github.com/ros2/rclpy/issues/890>`__）
* 说明 Future.result() 可能返回 None（`#884 <https://github.com/ros2/rclpy/issues/884>`__）
* 更新文档中的发行版编号（`#885 <https://github.com/ros2/rclpy/issues/885>`__）
* 修复 client.call_async 中的多线程竞态条件（`#871 <https://github.com/ros2/rclpy/issues/871>`__）
* 修复 cpplint 的头文件包含顺序（`#877 <https://github.com/ros2/rclpy/issues/877>`__）
* 修复 Duration 到消息类型转换时的精度问题（`#876 <https://github.com/ros2/rclpy/issues/876>`__）
* 更新至 pybind11 2.7.1（`#874 <https://github.com/ros2/rclpy/issues/874>`__）
* 只有使用 KEEP_LAST 时，QoS history depth 才可用（`#869 <https://github.com/ros2/rclpy/issues/869>`__）
* 实现受管理节点（`#865 <https://github.com/ros2/rclpy/issues/865>`__）
* 使 rclpy.try_shutdown() 的行为更接近 rclpy.shutdown()（`#868 <https://github.com/ros2/rclpy/issues/868>`__）
* 更新 TopicEndpointTypeEnum.__str__()，使其包含 history kind 和 history depth（`#849 <https://github.com/ros2/rclpy/issues/849>`__）
* 使用 Clock.sleep_until() 实现 Clock.sleep_for()（`#864 <https://github.com/ros2/rclpy/issues/864>`__）
* 新增 Clock.sleep_until()（`#858 <https://github.com/ros2/rclpy/issues/858>`__）
* 为 JumpHandle 添加 __enter__ 和 __exit__（`#862 <https://github.com/ros2/rclpy/issues/862>`__）
* 不覆盖 rclpy._rclpy_pybind11 文档（`#863 <https://github.com/ros2/rclpy/issues/863>`__）
* 改进 JumpThreshold 文档并禁止零时长（`#861 <https://github.com/ros2/rclpy/issues/861>`__）
* 修复 time.py 和 clock.py 的循环导入（`#860 <https://github.com/ros2/rclpy/issues/860>`__）
* 使 context.on_shutdown() 支持自由函数（`#859 <https://github.com/ros2/rclpy/issues/859>`__）
* 修复自动声明参数的描述符类型（`#853 <https://github.com/ros2/rclpy/issues/853>`__）
* 收到 SIGINT 时异步关闭（`#844 <https://github.com/ros2/rclpy/issues/844>`__）
* 更新维护者信息（`#845 <https://github.com/ros2/rclpy/issues/845>`__）
* 在将实体提供给 executor 前先将其加入 callback group，以避免竞态条件（`#839 <https://github.com/ros2/rclpy/issues/839>`__）
* 避免 client.call() 中的竞态条件（`#838 <https://github.com/ros2/rclpy/issues/838>`__）
* 处理 SIGTERM（`#830 <https://github.com/ros2/rclpy/issues/830>`__）
* 使用 pybind11 处理信号，并删除已不再使用的 rclpy_common、pycapsule 和 handle 代码（`#814 <https://github.com/ros2/rclpy/issues/814>`__）
* 修复 Service::take_request() 和 Client::take_response() 中的内存泄漏（`#828 <https://github.com/ros2/rclpy/issues/828>`__）
* 新增 Publisher.wait_for_all_acked()（`#793 <https://github.com/ros2/rclpy/issues/793>`__）
* 在 Executor 中只为一个 future 添加一个 done callback（`#816 <https://github.com/ros2/rclpy/issues/816>`__）
* 新增从 ParameterValue 转换为 Python 内置类型的函数（`#819 <https://github.com/ros2/rclpy/issues/819>`__）
* 在 Context.try_shutdown() 中调用 Context._logging_fini()（`#800 <https://github.com/ros2/rclpy/issues/800>`__）
* 将 LoggingSeverity 枚举提升为 logging 和 rcutils_logger 模块的公共依赖（`#785 <https://github.com/ros2/rclpy/issues/785>`__）
* 在 __init__() 中将 Context.__context 设置为 None（`#812 <https://github.com/ros2/rclpy/issues/812>`__）
* 移除未使用的 make_mock_subscription 函数（`#809 <https://github.com/ros2/rclpy/issues/809>`__）
* 移除 common.c/h（`#789 <https://github.com/ros2/rclpy/issues/789>`__）
* 允许声明未初始化的参数（`#798 <https://github.com/ros2/rclpy/issues/798>`__）
* 如果无法转换到 CANCEL_GOAL 状态，则拒绝取消请求（`#791 <https://github.com/ros2/rclpy/issues/791>`__）
* 删除不应再使用的 handle（`#786 <https://github.com/ros2/rclpy/issues/786>`__）
* 移除 common.c 中的部分函数，并在 utils.cpp 中替代实现（`#787 <https://github.com/ros2/rclpy/issues/787>`__）
* 将 exception.cpp/hpp 移动到 _rclpy_pybind11 模块（`#788 <https://github.com/ros2/rclpy/issues/788>`__）
* 在话题端点信息中，将无限时长显示为 Infinite（`#722 <https://github.com/ros2/rclpy/issues/722>`__）
* 如果配置的严重级别过高，则尽快中断日志函数执行（`#776 <https://github.com/ros2/rclpy/issues/776>`__）
* 将 Node 和 Context 转换为 C++ 类（`#771 <https://github.com/ros2/rclpy/issues/771>`__）
* 改进 action server 的若干问题（`#774 <https://github.com/ros2/rclpy/issues/774>`__）
* 改进 action goal handle 的若干问题（`#767 <https://github.com/ros2/rclpy/issues/767>`__）
* 将 GuardCondition 转换为 C++ 类（`#772 <https://github.com/ros2/rclpy/issues/772>`__）
* 移除未使用的 rclpy_client_t 和 rclpy_service_t 结构体（`#770 <https://github.com/ros2/rclpy/issues/770>`__）
* 将 WaitSet 转换为 C++ 类（`#769 <https://github.com/ros2/rclpy/issues/769>`__）
* 将 ActionServer 转换为 C++ 类（`#766 <https://github.com/ros2/rclpy/issues/766>`__）
* 将 ActionClient 转换为 C++ 类（`#759 <https://github.com/ros2/rclpy/issues/759>`__）
* 对 rcl_action_goal_handle_t 使用 py::class_（`#751 <https://github.com/ros2/rclpy/issues/751>`__）
* 将 Publisher 和 Subscription 转换为 C++ 类（`#756 <https://github.com/ros2/rclpy/issues/756>`__）
* 将:code:`QoS*Policy`  枚举重命名为 ``\*Policy``（`#379 <https://github.com/ros2/rclpy/issues/379>`__）
* 从参数 YAML 文件中读取节点 ``/**`` 的参数（`#370 <https://github.com/ros2/rclpy/issues/370>`__）
* 更新实现，以从参数 YAML 文件中读取节点 ``/**`` 的参数（`#399 <https://github.com/ros2/rclpy/issues/399>`__）
* 贡献者：Alejandro Hernández Cordero、Anthony、Artem Shumov、Auguste Lalande、Barry Xu、Chris Lalancette、Emerson Knapp、Erki Suurjaak、Greg Balke、Ivan Santiago Paunovic、Jacob Perron、Lei Liu、Louise Poubel、Miguel Company、Shane Loretz、Tomoya Fujita、ksuszka


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rcpputils <https://github.com/ros2/rcpputils/tree/humble/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}（`#160 <https://github.com/ros2/rcpputils/issues/160>`__）
* 修复 cpplint 的头文件包含顺序（`#158 <https://github.com/ros2/rcpputils/issues/158>`__）
* [path] 声明默认赋值运算符（`#156 <https://github.com/ros2/rcpputils/issues/156>`__）
* 修复与 uncrustify 0.72 的兼容问题（`#154 <https://github.com/ros2/rcpputils/issues/154>`__）
* 将 BSD 许可证头修正为标准版本（`#153 <https://github.com/ros2/rcpputils/issues/153>`__）
* 将维护者更新为 Chris Lalancette（`#152 <https://github.com/ros2/rcpputils/issues/152>`__）
* 新增经过检查的 convert_to_nanoseconds() 函数（`#145 <https://github.com/ros2/rcpputils/issues/145>`__）
* 补充 docs/FEATURES.md 目录中缺失的章节（`#151 <https://github.com/ros2/rcpputils/issues/151>`__）
* [env] 新增 ``set_env_var`` 函数（`#150 <https://github.com/ros2/rcpputils/issues/150>`__）
* 添加缺失的 cstddef 头文件包含（`#147 <https://github.com/ros2/rcpputils/issues/147>`__）
* 在 CMakeLists.txt 中增加 accumulator 测试（`#144 <https://github.com/ros2/rcpputils/issues/144>`__）
* ``rcpputils::fs``：修复 doxygen 参数标识符（`#142 <https://github.com/ros2/rcpputils/issues/142>`__）
* 使线程安全宏符合 C++ 标准（`#141 <https://github.com/ros2/rcpputils/issues/141>`__）
* 修复 API 文档，以支持 rosdoc2 正常构建（`#139 <https://github.com/ros2/rcpputils/issues/139>`__）
* 改进 ``rcppmath`` Doxygen 文档（`#138 <https://github.com/ros2/rcpputils/issues/138>`__）
* 改进 docs/FEATURES.md 中工具的文档说明（`#137 <https://github.com/ros2/rcpputils/issues/137>`__）
* 将 ``rcppmath`` 工具纳入 docs/FEATURES.md（`#136 <https://github.com/ros2/rcpputils/issues/136>`__）
* 修复 FEATURES 中对 ``IllegalStateException`` 的引用（`#135 <https://github.com/ros2/rcpputils/issues/135>`__）
* 将 rolling mean 从 ros2_controllers 迁移到 rcppmath（`#133 <https://github.com/ros2/rcpputils/issues/133>`__）
* 在 rcutils/get_env.h 弃用后更新头文件包含（`#132 <https://github.com/ros2/rcpputils/issues/132>`__）
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Barry Xu、Chris Lalancette、Christophe Bedard、Jacob Perron、Karsten Knese、Octogonapus、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rcutils <https://github.com/ros2/rcutils/tree/humble/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
