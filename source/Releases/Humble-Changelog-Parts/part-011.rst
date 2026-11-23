* 修复 Python 3.10 下 importlib_metadata 产生的警告（`#307 <https://github.com/ros2/launch_ros/issues/307>`__）
* 为可组合节点评估参数文件时使用正确的命名空间（`#303 <https://github.com/ros2/launch_ros/issues/303>`__）
* 评估参数时处理空字符串（`#300 <https://github.com/ros2/launch_ros/issues/300>`__）
* 新增参数替换功能（`#297 <https://github.com/ros2/launch_ros/issues/297>`__）
* 修复入口点加载失败时警告信息中的缺陷（`#243 <https://github.com/ros2/launch_ros/issues/243>`__）
* 提供更有帮助的错误消息（`#275 <https://github.com/ros2/launch_ros/issues/275>`__）
* 更新 setup.py 中的维护者信息（`#287 <https://github.com/ros2/launch_ros/issues/287>`__）
* 支持从文件为可组合节点设置参数（`#281 <https://github.com/ros2/launch_ros/issues/281>`__）
* 更新功能包维护者信息（`#284 <https://github.com/ros2/launch_ros/issues/284>`__）
* 更新节点名称匹配器（`#282 <https://github.com/ros2/launch_ros/issues/282>`__）
* 支持可组合节点的两种参数文件配置方式（`#259 <https://github.com/ros2/launch_ros/issues/259>`__）
* 在 RosTimer 中处理替换项（`#264 <https://github.com/ros2/launch_ros/issues/264>`__）
* 新增 SetParametersFromFile 动作（`#260 <https://github.com/ros2/launch_ros/issues/260>`__）
* 通过 launch 前端正确支持 ros_args 属性（`#253 <https://github.com/ros2/launch_ros/issues/253>`__）
* 为 push-ros-namespace 添加 push_ros_namespace 别名（`#250 <https://github.com/ros2/launch_ros/issues/250>`__）
* 为 Node 动作新增 ros_arguments 选项（`#249 <https://github.com/ros2/launch_ros/issues/249>`__）
* 重构 RosTimer，使其扩展 TimerAction（`#248 <https://github.com/ros2/launch_ros/issues/248>`__）
* 新增 ROS Timer Action（`#244 <https://github.com/ros2/launch_ros/issues/244>`__）
* 在前端支持 container（`#235 <https://github.com/ros2/launch_ros/issues/235>`__）
* 修复注释中的一个小拼写错误（`#237 <https://github.com/ros2/launch_ros/issues/237>`__）
* 更详细地记录 Node 的参数处理方式（`#234 <https://github.com/ros2/launch_ros/issues/234>`__）
* 修复 ros2 launch 命令（launch_ros `#201 <https://github.com/ros2/launch_ros/issues/201>`__）
* 新增 LaunchLogger 类（launch `#145 <https://github.com/ros2/launch/issues/145>`__）
* 将已弃用的 logger.warn 替换为 logger.warning（launch `#199 <https://github.com/ros2/launch/issues/199>`__）
* 将 rclpy.init 上下文接入 get_default_launch_description（launch `#193 <https://github.com/ros2/launch/issues/193>`__）
* 新增 normalize_parameters 和 evaluate_paramters（launch `#192 <https://github.com/ros2/launch/issues/192>`__）
* 新增 normalize_remap_rule 及相关类型（launch `#173 <https://github.com/ros2/launch/issues/173>`__）
* 重命名 transitions，使其与 ``lifecycle_msgs`` 中的变更一致（launch `#153 <https://github.com/ros2/launch/issues/153>`__）
* 支持以字典形式向 Node 传递参数（launch `#138 <https://github.com/ros2/launch/issues/138>`__）
* 修复 Node 动作中传递的 remapping，并补充相关测试（launch `#137 <https://github.com/ros2/launch/issues/137>`__）
* 贡献者：Aditya Pande、Audrow Nash、Chris Lalancette、Christophe Bedard、David V. Lu!!、Felix Divo、Jacob Perron、Kenji Miyake、Michel Hidalgo、Rebecca Butler、William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`launch_testing <https://github.com/ros2/launch/tree/humble/launch_testing/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除已弃用的 ``ready_fn`` 功能（`#589 <https://github.com/ros2/launch/issues/589>`__）
* 在 resolveProcess 函数中增加对 ExecuteLocal 实例的处理（`#587 <https://github.com/ros2/launch/issues/587>`__）
* 增加与 pytest 7 的兼容性（`#592 <https://github.com/ros2/launch/issues/592>`__）
* 重命名 example_processes 中的三个文件（`#573 <https://github.com/ros2/launch/issues/573>`__）
* 修复 launch_testing README.md 中将 proc 关键字误写为 process 的问题（`#554 <https://github.com/ros2/launch/issues/554>`__、`#560 <https://github.com/ros2/launch/issues/560>`__）
* 声明 frontend group 依赖，并在 launch_testing 中使用显式依赖（`#520 <https://github.com/ros2/launch/issues/520>`__）
* 将维护者更新为 Aditya Pande 和 Michel Hidalgo（`#559 <https://github.com/ros2/launch/issues/559>`__）
* 更新维护者信息（`#555 <https://github.com/ros2/launch/issues/555>`__）
* 首个基于 launch 测试的原生 pytest 插件原型（`#528 <https://github.com/ros2/launch/issues/528>`__）
* 新增 Executable 描述类（`#454 <https://github.com/ros2/launch/issues/454>`__）
* 新增“hello world”风格示例（`#532 <https://github.com/ros2/launch/issues/532>`__）
* 贡献者：Aditya Pande、Audrow Nash、Christophe Bedard、Ivan Santiago Paunovic、Jacob Perron、Khush Jain、Matt Lanting、Shane Loretz、William Woodall、roger-strain


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`launch_testing_ament_cmake <https://github.com/ros2/launch/tree/humble/launch_testing_ament_cmake/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* [launch_testing_ament_cmake] 添加测试标签（`#584 <https://github.com/ros2/launch/issues/584>`__）
* 将维护者更新为 Aditya Pande 和 Michel Hidalgo（`#559 <https://github.com/ros2/launch/issues/559>`__）
* 更新维护者信息（`#555 <https://github.com/ros2/launch/issues/555>`__）
* 贡献者：Aditya Pande、Audrow Nash、Keisuke Shima


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`launch_testing_examples <https://github.com/ros2/examples/tree/humble/launch_testing/launch_testing_examples/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 重新添加 WaitForTopics 工具（`#333 <https://github.com/ros2/examples/issues/333>`__）
* 完成最后一批示例（`#327 <https://github.com/ros2/examples/issues/327>`__）
* 将维护者更新为 Aditya Pande 和 Shane Loretz（`#332 <https://github.com/ros2/examples/issues/332>`__）
* 更新维护者信息（`#329 <https://github.com/ros2/examples/issues/329>`__）
* 回退 WaitForTopics 工具的使用（`#326 <https://github.com/ros2/examples/issues/326>`__）
* 移动示例（`#324 <https://github.com/ros2/examples/issues/324>`__）
* 贡献者：Aditya Pande、Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`launch_testing_ros <https://github.com/ros2/launch_ros/tree/humble/launch_testing_ros/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 为 ``talker.py`` 添加 ``hz`` 参数，以修复 wait_for_topic_launch_test（`#309 <https://github.com/ros2/launch_ros/issues/309>`__）
* 回退 WaitForTopics（`#288 <https://github.com/ros2/launch_ros/issues/288>`__）
* 更新 setup.py 中的维护者信息（`#287 <https://github.com/ros2/launch_ros/issues/287>`__）
* 将 pytest 入口点移动到独立模块（`#278 <https://github.com/ros2/launch_ros/issues/278>`__）
* 更新功能包维护者信息（`#284 <https://github.com/ros2/launch_ros/issues/284>`__）
* 检查 future 是否完成，并始终调用 rclpy.shutdown（`#273 <https://github.com/ros2/launch_ros/issues/273>`__）
* 回退“launch testing：等待话题发布”（`#274 <https://github.com/ros2/launch_ros/issues/274>`__），对应回退提交 `#276 <https://github.com/ros2/launch_ros/issues/276>`__。
* 新增用于等待发布者的 WaitForTopics 工具（`#274 <https://github.com/ros2/launch_ros/issues/274>`__）
* 移除未使用代码；Future.result() 已经会抛出异常（`#270 <https://github.com/ros2/launch_ros/issues/270>`__）
* 为示例中的服务响应等待添加超时（`#271 <https://github.com/ros2/launch_ros/issues/271>`__）
* 新增示例（`#263 <https://github.com/ros2/launch_ros/issues/263>`__）
* 贡献者：Aditya Pande、Audrow Nash、Jacob Perron、Jorge Perez、Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`launch_xml <https://github.com/ros2/launch/tree/humble/launch_xml/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复用于交叉引用 Launch 方法的 Sphinx 指令（`#605 <https://github.com/ros2/launch/issues/605>`__）
* 新增布尔值替换功能（`#598 <https://github.com/ros2/launch/issues/598>`__）
* 支持对环境变量设置作用域（`#601 <https://github.com/ros2/launch/issues/601>`__）
* 在 XML/YAML 文件中将 output 作为替换项展开（`#577 <https://github.com/ros2/launch/issues/577>`__）
* 声明 frontend group 依赖，并在 launch_testing 中使用显式依赖（`#520 <https://github.com/ros2/launch/issues/520>`__）
* 将维护者更新为 Aditya Pande 和 Michel Hidalgo（`#559 <https://github.com/ros2/launch/issues/559>`__）
* 更新维护者信息（`#555 <https://github.com/ros2/launch/issues/555>`__）
* 新增 AppendEnvironmentVariable 动作（`#543 <https://github.com/ros2/launch/issues/543>`__）
* 新增清除 launch 配置的功能（`#515 <https://github.com/ros2/launch/issues/515>`__）
* 修复 ``DeclareLaunchArgument`` 的 XML 解析和构造函数（`#529 <https://github.com/ros2/launch/issues/529>`__）
* 将 launch 添加到 launch 文件扩展名集合中（`#518 <https://github.com/ros2/launch/issues/518>`__）
* 使每个解析器扩展提供一组文件扩展名（`#516 <https://github.com/ros2/launch/issues/516>`__）
* 贡献者：Abrar Rahman Protyasha、Aditya Pande、Audrow Nash、Christophe Bedard、Derek Chopp、Ivan Santiago Paunovic、Jacob Perron、Kenji Miyake、Khush Jain


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`launch_yaml <https://github.com/ros2/launch/tree/humble/launch_yaml/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复用于交叉引用 Launch 方法的 Sphinx 指令（`#605 <https://github.com/ros2/launch/issues/605>`__）
* 新增布尔值替换功能（`#598 <https://github.com/ros2/launch/issues/598>`__）
* 支持对环境变量设置作用域（`#601 <https://github.com/ros2/launch/issues/601>`__）
* 在 XML/YAML 文件中将 output 作为替换项展开（`#577 <https://github.com/ros2/launch/issues/577>`__）
