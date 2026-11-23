* 使 rosidl_get_typesupport_target 在找不到目标时返回 -NOTFOUND，而不是触发 FATAL_ERROR（`#672 <https://github.com/ros2/rosidl/issues/672>`__）
* 为 C/C++ 消息添加 introspection typesupport 测试（`#651 <https://github.com/ros2/rosidl/issues/651>`__）
* 导出 typesupport 库时使用 target 的输出名称（`#625 <https://github.com/ros2/rosidl/issues/625>`__）
* 更新功能包维护者（`#624 <https://github.com/ros2/rosidl/issues/624>`__）
* 撤销“打包并确保导出 rosidl 生成的 targets”的修改（`#611 <https://github.com/ros2/rosidl/issues/611>`__）
* 新增 rosidl_get_typesupport_target，并弃用 rosidl_target_interfaces（`#606 <https://github.com/ros2/rosidl/issues/606>`__）
* 打包并确保导出 rosidl 生成的 targets（`#601 <https://github.com/ros2/rosidl/issues/601>`__）
* 贡献者：Jonathan Selling、Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_default_generators <https://github.com/ros2/rosidl_defaults/tree/humble/rosidl_default_generators/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 展开组依赖（`#20 <https://github.com/ros2/rosidl_defaults/issues/20>`__）
* 贡献者：Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_default_runtime <https://github.com/ros2/rosidl_defaults/tree/humble/rosidl_default_runtime/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 展开组依赖（`#20 <https://github.com/ros2/rosidl_defaults/issues/20>`__）
* 贡献者：Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_generator_c <https://github.com/ros2/rosidl/tree/humble/rosidl_generator_c/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复复制 C 序列消息时的错误处理（`#671 <https://github.com/ros2/rosidl/issues/671>`__）
* 将生成的头文件安装到 include/${PROJECT_NAME}（`#670 <https://github.com/ros2/rosidl/issues/670>`__）
* 清理 rosidl generator 扩展中的若干内容（`#662 <https://github.com/ros2/rosidl/issues/662>`__）
* 复制序列时始终设置输出大小（`#669 <https://github.com/ros2/rosidl/issues/669>`__）
* 为 C 消息实现复制函数（`#650 <https://github.com/ros2/rosidl/issues/650>`__）
* 为 C 消息实现相等运算符函数（`#648 <https://github.com/ros2/rosidl/issues/648>`__）
* 根据 ROS 接口注释，在生成的 C 头文件中生成文档（`#593 <https://github.com/ros2/rosidl/issues/593>`__）
* 更新功能包维护者（`#624 <https://github.com/ros2/rosidl/issues/624>`__）
* 使 rosidl 功能包使用 FindPython3，而不是 FindPythonInterp（`#612 <https://github.com/ros2/rosidl/issues/612>`__）
* 撤销“打包并确保导出 rosidl 生成的 targets”的修改（`#611 <https://github.com/ros2/rosidl/issues/611>`__）
* 打包并确保导出 rosidl 生成的 targets（`#601 <https://github.com/ros2/rosidl/issues/601>`__）
* 修复 cpplint 中 allocator 相关的回归问题（`#590 <https://github.com/ros2/rosidl/issues/590>`__）
* 在 rosidl_generator_c 中使用 RCUtils 分配器（`#584 <https://github.com/ros2/rosidl/issues/584>`__）
* 贡献者：Chris Lalancette、Ivan Santiago Paunovic、Michel Hidalgo、Nikolai Morin、Pablo Garrido、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_generator_cpp <https://github.com/ros2/rosidl/tree/humble/rosidl_generator_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将生成的头文件安装到 include/${PROJECT_NAME}（`#670 <https://github.com/ros2/rosidl/issues/670>`__）
* 清理 rosidl generator 扩展中的若干内容（`#662 <https://github.com/ros2/rosidl/issues/662>`__）
* 补充缺失的 build_export_depend 依赖（`#665 <https://github.com/ros2/rosidl/issues/665>`__）
* 修复未依赖 rosidl_runtime_cpp 的问题（`#660 <https://github.com/ros2/rosidl/issues/660>`__）
* 修复 cpplint 的头文件包含顺序（`#644 <https://github.com/ros2/rosidl/issues/644>`__）
* 将 CXX 标准设置为 17（`#635 <https://github.com/ros2/rosidl/issues/635>`__）
* 更新功能包维护者（`#624 <https://github.com/ros2/rosidl/issues/624>`__）
* 使 rosidl 功能包使用 FindPython3，而不是 FindPythonInterp（`#612 <https://github.com/ros2/rosidl/issues/612>`__）
* 支持以 flow 样式输出 YAML（`#613 <https://github.com/ros2/rosidl/issues/613>`__）
* 撤销“打包并确保导出 rosidl 生成的 targets”的修改（`#611 <https://github.com/ros2/rosidl/issues/611>`__）
* 将 to_yaml() 移至 message 命名空间下（`#609 <https://github.com/ros2/rosidl/issues/609>`__）
* 打包并确保导出 rosidl 生成的 targets（`#601 <https://github.com/ros2/rosidl/issues/601>`__）
* 贡献者：Jacob Perron、Jorge Perez、Michel Hidalgo、Shane Loretz、Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_generator_dds_idl <https://github.com/ros2/rosidl_dds/tree/humble/rosidl_generator_dds_idl/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 添加变更日志（`#56 <https://github.com/ros2/rosidl_dds/issues/56>`__）
* 贡献者：Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_generator_py <https://github.com/ros2/rosidl_python/tree/humble/rosidl_generator_py/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除错误的、未匹配的右括号（`#125 <https://github.com/ros2/rosidl_python/issues/125>`__）
* 要求使用 Python 3.6，因为多个位置使用了格式化字符串（`#152 <https://github.com/ros2/rosidl_python/issues/152>`__）
* 修复 rosidl_generator_py 对库名称判断错误的问题（`#149 <https://github.com/ros2/rosidl_python/issues/149>`__）
* 修复 msg 文件中的 property 字段不位于末尾时的处理问题（`#151 <https://github.com/ros2/rosidl_python/issues/151>`__）
* 更新功能包维护者（`#147 <https://github.com/ros2/rosidl_python/issues/147>`__）
* 使用 rosidl_get_typesupport_target()（`#139 <https://github.com/ros2/rosidl_python/issues/139>`__）
* 在 CLI 扩展中支持可用的 typesupport 规范（`#133 <https://github.com/ros2/rosidl_python/issues/133>`__）
* 在 Debug 模式下，为 test_cli_extension 使用 python_d（`#136 <https://github.com/ros2/rosidl_python/issues/136>`__）
* 添加缺失的 float/double 边界检查（`#128 <https://github.com/ros2/rosidl_python/issues/128>`__）
* 优化使用 buffer protocol 复制数组的操作（`#129 <https://github.com/ros2/rosidl_python/issues/129>`__）
* 为 CLI 扩展添加冒烟测试（`#132 <https://github.com/ros2/rosidl_python/issues/132>`__）
* 将生成的 Python 接口安装到 Python 软件包中（`#131 <https://github.com/ros2/rosidl_python/issues/131>`__）
* 贡献者：Charles Cross、Chen Lihui、Michel Hidalgo、Seulbae Kim、Shane Loretz、William Woodall、ksuszka


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_parser <https://github.com/ros2/rosidl/tree/humble/rosidl_parser/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 为兼容 lark 1.+，将 maybe_placeholders 设置为 False（`#664 <https://github.com/ros2/rosidl/issues/664>`__）
* 根据 ROS 接口注释，在生成的 C 头文件中生成文档（`#593 <https://github.com/ros2/rosidl/issues/593>`__）
* 将 ROS 接口常量中的注释传递到生成的 .idl 文件（`#630 <https://github.com/ros2/rosidl/issues/630>`__）
* 更新功能包维护者（`#624 <https://github.com/ros2/rosidl/issues/624>`__）
* 修复字符串字面量中的转义问题（`#595 <https://github.com/ros2/rosidl/issues/595>`__）
* 贡献者：Ivan Santiago Paunovic、Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_runtime_c <https://github.com/ros2/rosidl/tree/humble/rosidl_runtime_c/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复复制 C 序列消息时的错误处理（`#671 <https://github.com/ros2/rosidl/issues/671>`__）
* 复制序列时始终设置输出大小（`#669 <https://github.com/ros2/rosidl/issues/669>`__）
* 从 README 和 QUALITY_DECLARATION 中移除重复的 Quality Level 内容（`#661 <https://github.com/ros2/rosidl/issues/661>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#658 <https://github.com/ros2/rosidl/issues/658>`__）
* 为 C 消息实现复制函数（`#650 <https://github.com/ros2/rosidl/issues/650>`__）
* 为 C 消息实现相等运算符函数（`#648 <https://github.com/ros2/rosidl/issues/648>`__）
* 将 CXX 标准设置为 17（`#635 <https://github.com/ros2/rosidl/issues/635>`__）
* 更新功能包维护者（`#624 <https://github.com/ros2/rosidl/issues/624>`__）
* 在 rosidl_generator_c 中使用 RCUtils 分配器（`#584 <https://github.com/ros2/rosidl/issues/584>`__）
* 贡献者：Jose Luis Rivero、Michel Hidalgo、Nikolai Morin、Pablo Garrido、Shane Loretz、Øystein Sture
