* 贡献者：Barry Xu、Chen Lihui、Emerson Knapp、Jorge Perez、Jose Antonio Moral、Michel Hidalgo、Miguel Company、mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`test_security <https://github.com/ros2/system_tests/tree/humble/test_security/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新维护者信息（`#489 <https://github.com/ros2/system_tests/issues/489>`__）
* 修复已弃用订阅回调的警告（`#483 <https://github.com/ros2/system_tests/issues/483>`__）
* 新增变更日志（`#473 <https://github.com/ros2/system_tests/issues/473>`__）
* 简化 test_secure_subscriber 代码（`#471 <https://github.com/ros2/system_tests/issues/471>`__）
* 在 rcutils/get_env.h 弃用后更新头文件包含（`#472 <https://github.com/ros2/system_tests/issues/472>`__）
* 贡献者：Abrar Rahman Protyasha、Aditya Pande、Chris Lalancette、Christophe Bedard、Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`test_tf2 <https://github.com/ros2/geometry2/tree/humble/test_tf2/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 RHEL 上更多 Eigen 相关问题（`#515 <https://github.com/ros2/geometry2/issues/515>`__）
* 将头文件安装到 include/${PROJECT_NAME} 并使用现代 CMake（`#493 <https://github.com/ros2/geometry2/issues/493>`__）
* 修复使用 rclcpp::Time::seconds() 导致的精度损失（`#511 <https://github.com/ros2/geometry2/issues/511>`__）
* 改进静态变换发布器的命令行接口，使其更直观（`#392 <https://github.com/ros2/geometry2/issues/392>`__）
* 为 toMsg() 添加转换测试（`#423 <https://github.com/ros2/geometry2/issues/423>`__）
* 弃用 tf2_geometry_msgs.h（`#418 <https://github.com/ros2/geometry2/issues/418>`__）
* 弃用 tf2_kdl.h（`#414 <https://github.com/ros2/geometry2/issues/414>`__）
* 弃用 tf2_bullet.h（`#412 <https://github.com/ros2/geometry2/issues/412>`__）
* 贡献者：Bjar Ne、Chris Lalancette、Hunter L. Allen、Kenji Brameld、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`test_tracetools <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/test_tracetools/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 为 tracepoint 名称引入常量
* 将实际测试从 tracetools_test 移至新建的 test_tracetools 功能包
* 贡献者：Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`test_tracetools_launch <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/test_tracetools_launch/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 添加预加载 pthread 和 dl 插桩共享库的支持
* 移除 profile_fast 选项，并考虑同时通过 LD_PRELOAD 预加载这两个库
* 修复多个 LdPreload actions 无法正常工作的问题，并添加测试
* 弃用 'context_names' 参数，改用 'context_fields'
* 将部分测试从 tracetools_launch 移至 test_tracetools_launch
* 贡献者：Christophe Bedard、Ingo Lütkebohle


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tf2 <https://github.com/ros2/geometry2/tree/humble/tf2/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME} 并使用现代 CMake（`#493 <https://github.com/ros2/geometry2/issues/493>`__）
* 前置声明 fromMsg，以避免下游库中出现符号缺失（`#485 <https://github.com/ros2/geometry2/issues/485>`__）
* tf2：启用通用代码检查测试（`#469 <https://github.com/ros2/geometry2/issues/469>`__）
* 将时间函数移入 time.cpp
* 将 for 循环改为 while 循环
* 改用 C++ 风格的类型转换
* 移除完全未使用且无法到达的代码
* 将 NULL 替换为 nullptr
* 修正部分注释
* 在适用场景使用 std::make_shared
* 将两处与空字符串的比较改为 empty()
* 确保遵循 include-what-you-use
* 移除不必要的内部方法
* 移除已长期弃用的 walkToTopParent 重载
* 移除不必要的测试依赖
* 移除部分 ROS 1 wiki 引用
* 将 rosidl_runtime_cpp 添加为 build_depend 和 build_export_depend
* 对 CMakeLists.txt 进行小幅清理
* 移除不存在的 include 目录
* 移除完全不必要的 target_link_libraries
* 从 tf2 中移除未使用的 speed_test
* 抑制 clang 关于枚举器属性的警告（`#463 <https://github.com/ros2/geometry2/issues/463>`__）
* 使 TF2Error 名称更具描述性（`#349 <https://github.com/ros2/geometry2/issues/349>`__）
* 修复因头文件链接缺失导致的错误（`#432 <https://github.com/ros2/geometry2/issues/432>`__）
* 弃用 tf2_geometry_msgs.h（`#418 <https://github.com/ros2/geometry2/issues/418>`__）
* 加快协方差解包速度（`#399 <https://github.com/ros2/geometry2/issues/399>`__）
* 贡献者：Abrar Rahman Protyasha、Chris Lalancette、Dima Dorezyuk、João C. Monteiro、Shane Loretz、Shivam Pandey


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tf2_bullet <https://github.com/ros2/geometry2/tree/humble/tf2_bullet/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME} 并使用现代 CMake（`#493 <https://github.com/ros2/geometry2/issues/493>`__）
* 导出 tf2_bullet::tf2_bullet target（`#495 <https://github.com/ros2/geometry2/issues/495>`__）
* 修复 cpplint 错误（`#497 <https://github.com/ros2/geometry2/issues/497>`__）
* 移除部分 ROS 1 wiki 引用
* 修复 tf2_bullet 依赖项导出（`#428 <https://github.com/ros2/geometry2/issues/428>`__）
* 弃用 tf2_bullet.h（`#412 <https://github.com/ros2/geometry2/issues/412>`__）
* 贡献者：Bjar Ne、Chris Lalancette、Jacob Perron、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tf2_eigen <https://github.com/ros2/geometry2/tree/humble/tf2_eigen/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 规避 RHEL FindEigen3.cmake 的缺陷（`#513 <https://github.com/ros2/geometry2/issues/513>`__）
* 将头文件安装到 include/${PROJECT_NAME} 并使用现代 CMake（`#493 <https://github.com/ros2/geometry2/issues/493>`__）
* 在 aarch64 上禁用内存访问警告（`#506 <https://github.com/ros2/geometry2/issues/506>`__）
* 修复 cpplint 错误（`#497 <https://github.com/ros2/geometry2/issues/497>`__）
* 移除部分 ROS 1 wiki 引用
* 为 twists 或 wrenches 添加 doTransform 函数（`#406 <https://github.com/ros2/geometry2/issues/406>`__）
* 重新启用 stamped Eigen 测试（`#429 <https://github.com/ros2/geometry2/issues/429>`__）
* 弃用 tf2_eigen.h（`#413 <https://github.com/ros2/geometry2/issues/413>`__）
* 贡献者：AndyZe、Bjar Ne、Chris Lalancette、Jacob Perron、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`tf2_eigen_kdl <https://github.com/ros2/geometry2/tree/humble/tf2_eigen_kdl/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 RHEL 上更多 Eigen 相关问题（`#515 <https://github.com/ros2/geometry2/issues/515>`__）
* 依赖 orocos_kdl_vendor（`#473 <https://github.com/ros2/geometry2/issues/473>`__）
* 将头文件安装到 include/${PROJECT_NAME} 并使用现代 CMake（`#493 <https://github.com/ros2/geometry2/issues/493>`__）
* 修复 cpplint 错误（`#497 <https://github.com/ros2/geometry2/issues/497>`__）
