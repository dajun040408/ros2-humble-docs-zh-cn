* 将 logging 宏中的 stringstream 重命名为更独特的名称（`#1862 <https://github.com/ros2/rclcpp/issues/1862>`__）
* 为进程内通信增加非 transform 能力（`#1849 <https://github.com/ros2/rclcpp/issues/1849>`__）
* 修复 rclcpp 文档构建问题（`#1779 <https://github.com/ros2/rclcpp/issues/1779>`__）
* 使用 UninitializedStaticallyTypedParameterException（`#1689 <https://github.com/ros2/rclcpp/issues/1689>`__）
* 新增 wait_for_all_acked 支持（`#1662 <https://github.com/ros2/rclcpp/issues/1662>`__）
* 为 declare_parameter 的函数模板添加测试（`#1747 <https://github.com/ros2/rclcpp/issues/1747>`__）
* 修复与 uncrustify 0.72 的兼容问题（`#1844 <https://github.com/ros2/rclcpp/issues/1844>`__）
* 使用私有成员保存底层的全部引用（`#1845 <https://github.com/ros2/rclcpp/issues/1845>`__）
* 使 node base 可共享（`#1832 <https://github.com/ros2/rclcpp/issues/1832>`__）
* 新增 Clock::sleep_for()（`#1828 <https://github.com/ros2/rclcpp/issues/1828>`__）
* 在 Clock::sleep_until 中同步 rcl 与 std::chrono steady clock（`#1830 <https://github.com/ros2/rclcpp/issues/1830>`__）
* 使用 rclcpp::guard_condition（`#1612 <https://github.com/ros2/rclcpp/issues/1612>`__）
* 调用 CMake 函数生成版本头文件（`#1805 <https://github.com/ros2/rclcpp/issues/1805>`__）
* 在日志宏参数周围添加括号（`#1820 <https://github.com/ros2/rclcpp/issues/1820>`__）
* 根据请求移除作者信息（`#1818 <https://github.com/ros2/rclcpp/issues/1818>`__）
* 更新维护者信息（`#1817 <https://github.com/ros2/rclcpp/issues/1817>`__）
* min_forward 和 min_backward 阈值不得被禁用（`#1815 <https://github.com/ros2/rclcpp/issues/1815>`__）
* 重新添加 Clock::sleep_until（`#1814 <https://github.com/ros2/rclcpp/issues/1814>`__）
* 修复 context 生命周期，确保其依赖的 node handle 仍在使用时 context 保持存活（`#1754 <https://github.com/ros2/rclcpp/issues/1754>`__）
* 新增 pre-shutdown callback 接口（`#1714 <https://github.com/ros2/rclcpp/issues/1714>`__）
* 从移动后的 LoanedMessage 接管消息所有权（`#1808 <https://github.com/ros2/rclcpp/issues/1808>`__）
* 抑制基准测试中的 clang dead-store 警告（`#1802 <https://github.com/ros2/rclcpp/issues/1802>`__）
* 等待发布者和订阅者匹配（`#1777 <https://github.com/ros2/rclcpp/issues/1777>`__）
* 修复 clock 订阅中未使用的 QoS profile，并将 ClockQoS 设为默认值（`#1801 <https://github.com/ros2/rclcpp/issues/1801>`__）
* 修复 TimeSource 实现中危险的 std::bind 捕获（`#1768 <https://github.com/ros2/rclcpp/issues/1768>`__）
* 修复 ParameterEventHandler 实现中危险的 std::bind 捕获（`#1770 <https://github.com/ros2/rclcpp/issues/1770>`__）
* 以与 SIGINT 相同的方式处理 SIGTERM（`#1771 <https://github.com/ros2/rclcpp/issues/1771>`__）
* rclcpp::Node 复制构造函数：复制 ``node_waitables_`` 成员（`#1799 <https://github.com/ros2/rclcpp/issues/1799>`__）
* 扩展 NodeGraph，使其与 rcl 提供的功能一致（`#1484 <https://github.com/ros2/rclcpp/issues/1484>`__）
* Context::sleep_for()：将递归替换为 do-while，以避免潜在的栈溢出（`#1765 <https://github.com/ros2/rclcpp/issues/1765>`__）
* extend_sub_namespace()：调用 string::front() 前先验证 string::empty()（`#1764 <https://github.com/ros2/rclcpp/issues/1764>`__）
* 弃用 ``void shared_ptr<MessageT>`` 形式的订阅回调签名（`#1713 <https://github.com/ros2/rclcpp/issues/1713>`__）
* 移除 QNX 情况下的 can_be_nullptr 赋值检查（`#1752 <https://github.com/ros2/rclcpp/issues/1752>`__）
* 更新客户端 API，使其能够移除待处理请求（`#1734 <https://github.com/ros2/rclcpp/issues/1734>`__）
* 修复 StaticSingleThreadedExecutor 在 spin 过程中添加节点的问题（`#1690 <https://github.com/ros2/rclcpp/issues/1690>`__）
* 为 executor 和消息获取操作添加 tracing 插桩（`#1738 <https://github.com/ros2/rclcpp/issues/1738>`__）
* 修复 StaticSingleThreadedExecutor 在执行前重置定时器触发时间的问题（`#1739 <https://github.com/ros2/rclcpp/issues/1739>`__）
* 使用 FindPython3，并显式声明 python3 依赖（`#1745 <https://github.com/ros2/rclcpp/issues/1745>`__）
* 使用 rosidl_get_typesupport_target()（`#1729 <https://github.com/ros2/rclcpp/issues/1729>`__）
* 修复 sub_namespace 为空时返回无效命名空间的问题（`#1658 <https://github.com/ros2/rclcpp/issues/1658>`__）
* 新增等待订阅消息的自由函数（`#1705 <https://github.com/ros2/rclcpp/issues/1705>`__）
* 使用 rcpputils/scope_exit.hpp，并移除 rclcpp/scope_exit.hpp（`#1727 <https://github.com/ros2/rclcpp/issues/1727>`__）
* 移除不安全的 get_callback_groups API。调用方应改用 for_each_callback_group()，或在内部保存所需的回调组。
* 新增 ``callback_groups_for_each()``。该方法主要用于确保对 ``callback_groups_`` 向量的访问具备线程安全性。通过接收 std::function，调用方可以传入所需回调，由该方法负责加锁；同时将所有使用 get_callback_groups() 的位置改为 callback_groups_for_each()。
* 使用另一种机制，避免 MultiThreadedExecutor 多次调度定时器（`#1692 <https://github.com/ros2/rclcpp/issues/1692>`__）
* 修复 Windows CI（`#1726 <https://github.com/ros2/rclcpp/issues/1726>`__）：修复 ``#1709`` 引入的 AnyServiceCallback 缺陷。
* 支持在服务中延迟发送响应（`#1709 <https://github.com/ros2/rclcpp/issues/1709>`__）。Signed-off-by: Ivan Santiago Paunovic <ivanpauno@ekumenlabs.com>
* 修复文档缺陷（`#1719 <https://github.com/ros2/rclcpp/issues/1719>`__）。Signed-off-by: William Woodall <william@osrfoundation.org>
* 移除遗留的 ``is_initialized()`` 实现（`#1711 <https://github.com/ros2/rclcpp/issues/1711>`__），该实现来自 https://github.com/ros2/rclcpp/pull/1622。
* 修复 int 和 float 向量的 declare parameter 方法（`#1696 <https://github.com/ros2/rclcpp/issues/1696>`__）
* 清理进程内管理器的实现（`#1695 <https://github.com/ros2/rclcpp/issues/1695>`__）
* 在 executor 的 ``runtime_error`` 中添加节点名称（`#1686 <https://github.com/ros2/rclcpp/issues/1686>`__）
* 修正拼写错误：“Attack” 更正为 “Attach”（`#1687 <https://github.com/ros2/rclcpp/issues/1687>`__）
* 移除对 std::allocator<>::rebind 的使用（`#1678 <https://github.com/ros2/rclcpp/issues/1678>`__）；rebind 在 C++17 中已弃用，并在 C++20 中移除。
* 允许声明未初始化的参数（`#1673 <https://github.com/ros2/rclcpp/issues/1673>`__）
* 修复 GCC 语法问题（`#1674 <https://github.com/ros2/rclcpp/issues/1674>`__）
* [service] 不再使用 weak_ptr，以避免泄漏（`#1668 <https://github.com/ros2/rclcpp/issues/1668>`__）
* 修复文档拼写错误（`#1663 <https://github.com/ros2/rclcpp/issues/1663>`__）
* [rclcpp] 类型适配功能（`#1557 <https://github.com/ros2/rclcpp/issues/1557>`__）
* 不再尝试使用 void allocator 分配内存（`#1657 <https://github.com/ros2/rclcpp/issues/1657>`__）
* 确保 publisher 和 subscription 选项中的自定义 allocator 保持存活（`#1647 <https://github.com/ros2/rclcpp/issues/1647>`__）
* 修复 test_node.cpp 中 get_publishers_subscriptions_info_by_topic 测试（`#1648 <https://github.com/ros2/rclcpp/issues/1648>`__）
* 使用 OnShutdown callback handle 替代 OnShutdown callback（`#1639 <https://github.com/ros2/rclcpp/issues/1639>`__）
* 在进程内管理器中使用 dynamic_pointer_cast 检测 allocator 不匹配（`#1643 <https://github.com/ros2/rclcpp/issues/1643>`__）
* 贡献者：Abrar Rahman Protyasha、Ahmed Sobhy、Alberto Soragna、Andrea Sorbini、Audrow Nash、Barry Xu、Bi0T1N、Chen Lihui、Chris Lalancette、Christophe Bedard、Doug Smith、Emerson Knapp、Gaël Écorchard、Geoffrey Biggs、Gonzo、Grey、Ivan Santiago Paunovic、Jacob Perron、Jorge Perez、Karsten Knese、Kenji Miyake、M. Hofstätter、M. Mostafa Farzan、Mauro Passerino、Michel Hidalgo、Miguel Company、Nikolai Morin、Petter Nilsson、Scott K Logan、Shane Loretz、Steve Macenski、Tomoya Fujita、William Woodall、Yong-Hao Zou、iRobot ROS、livanov93、mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rclcpp_action <https://github.com/ros2/rclcpp/tree/humble/rclcpp_action/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Galactic 发行版期间已弃用的内容（`#1913 <https://github.com/ros2/rclcpp/issues/1913>`__）
* 为 waitable 新增 take_data_by_entity_id API（`#1892 <https://github.com/ros2/rclcpp/issues/1892>`__）
* 修复 rosdoc2 相关问题（`#1897 <https://github.com/ros2/rclcpp/issues/1897>`__）
* 新增 RMW listener API（`#1579 <https://github.com/ros2/rclcpp/issues/1579>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#1888 <https://github.com/ros2/rclcpp/issues/1888>`__）
* 修复 cpplint 的头文件包含顺序和相对路径问题（`#1859 <https://github.com/ros2/rclcpp/issues/1859>`__）
* 修复与 uncrustify 0.72 的兼容问题（`#1844 <https://github.com/ros2/rclcpp/issues/1844>`__）
* 使用 rclcpp::guard_condition（`#1612 <https://github.com/ros2/rclcpp/issues/1612>`__）
* 根据请求移除作者信息（`#1818 <https://github.com/ros2/rclcpp/issues/1818>`__）
* 更新维护者信息（`#1817 <https://github.com/ros2/rclcpp/issues/1817>`__）
* 抑制基准测试中的 clang dead-store 警告（`#1802 <https://github.com/ros2/rclcpp/issues/1802>`__）
* 弃用 ``void shared_ptr<MessageT>`` 形式的订阅回调签名（`#1713 <https://github.com/ros2/rclcpp/issues/1713>`__）
* 使用 rcpputils/scope_exit.hpp，并移除 rclcpp/scope_exit.hpp（`#1727 <https://github.com/ros2/rclcpp/issues/1727>`__）
* 修复因竞态条件导致偶尔缺失目标结果的问题（`#1677 <https://github.com/ros2/rclcpp/issues/1677>`__）
* 增加 benchmark_action_client 的基准测试超时时间（`#1671 <https://github.com/ros2/rclcpp/issues/1671>`__）
* 当目标句柄无法转换到 CANCELING 状态时，返回 CancelResponse::REJECT（`#1641 <https://github.com/ros2/rclcpp/issues/1641>`__）
* 修复 CancelCallback 中其他互斥锁已锁定时导致的 action server 死锁（`#1635 <https://github.com/ros2/rclcpp/issues/1635>`__）
* 贡献者：Abrar Rahman Protyasha、Alberto Soragna、Chris Lalancette、Christophe Bedard、Jacob Perron、Kaven Yau、Shane Loretz、Tomoya Fujita、William Woodall、iRobot ROS、mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rclcpp_components <https://github.com/ros2/rclcpp/tree/humble/rclcpp_components/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 在节点注册时选择 executor（`#1898 <https://github.com/ros2/rclcpp/issues/1898>`__）
* 修复 rclcpp 中的 rosdoc2 问题（`#1897 <https://github.com/ros2/rclcpp/issues/1897>`__）
* 修复 node_main.cpp.in 中的 bugprone-exception-escape 问题（`#1895 <https://github.com/ros2/rclcpp/issues/1895>`__）
* 对 node_main.cpp.in 进行小幅改进
* 将头文件安装到 include/${PROJECT_NAME}（`#1888 <https://github.com/ros2/rclcpp/issues/1888>`__）
* 在 component_manager_isolated.hpp 中使用 spin()（`#1881 <https://github.com/ros2/rclcpp/issues/1881>`__）
* 为组件节点的 node options 添加 use_global_arguments（`#1776 <https://github.com/ros2/rclcpp/issues/1776>`__）
* 新增 rclcpp_components::component（`#1855 <https://github.com/ros2/rclcpp/issues/1855>`__）
* 新增配置线程数量的参数（`#1708 <https://github.com/ros2/rclcpp/issues/1708>`__）
* 从 ComponentManagerIsolated 类中移除 RCLCPP_COMPONENTS_PUBLIC（`#1843 <https://github.com/ros2/rclcpp/issues/1843>`__）
* 创建 component_container_isolated（`#1781 <https://github.com/ros2/rclcpp/issues/1781>`__）
* 根据请求移除作者信息（`#1818 <https://github.com/ros2/rclcpp/issues/1818>`__）
* 更新维护者信息（`#1817 <https://github.com/ros2/rclcpp/issues/1817>`__）
* 抑制基准测试中的 clang dead-store 警告（`#1802 <https://github.com/ros2/rclcpp/issues/1802>`__）
* 更新客户端 API，使其能够移除待处理请求（`#1734 <https://github.com/ros2/rclcpp/issues/1734>`__）
* 弃用 rclcpp_components 中使用 CamelCase 的方法名称（`#1716 <https://github.com/ros2/rclcpp/issues/1716>`__）
* 为 ComponentManager 添加生成节点选项的钩子（`#1702 <https://github.com/ros2/rclcpp/issues/1702>`__）
* 贡献者：Alberto Soragna、Chris Lalancette、Daisuke Nishimatsu、Hirokazu Ishida、Ivan Santiago Paunovic、Jacob Perron、Rebecca Butler、Shane Loretz、gezp


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rclcpp_lifecycle <https://github.com/ros2/rclcpp/tree/humble/rclcpp_lifecycle/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Galactic 发行版期间已弃用的内容（`#1913 <https://github.com/ros2/rclcpp/issues/1913>`__）
