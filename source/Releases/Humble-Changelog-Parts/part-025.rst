^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_runtime_cpp <https://github.com/ros2/rosidl/tree/humble/rosidl_runtime_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 补充对 rosidl_runtime_c 的缺失依赖（`#666 <https://github.com/ros2/rosidl/issues/666>`__）
* 从 README 和 QUALITY_DECLARATION 中移除重复的 Quality Level 内容（`#661 <https://github.com/ros2/rosidl/issues/661>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#658 <https://github.com/ros2/rosidl/issues/658>`__）
* 将 CXX 标准设置为 17（`#635 <https://github.com/ros2/rosidl/issues/635>`__）
* 更新功能包维护者（`#624 <https://github.com/ros2/rosidl/issues/624>`__）
* 贡献者：Jose Luis Rivero、Michel Hidalgo、Shane Loretz、Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_runtime_py <https://github.com/ros2/rosidl_runtime_py/tree/humble/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 添加 YAML 转储的 flow 样式（`#16 <https://github.com/ros2/rosidl_runtime_py/issues/16>`__）
* 更新维护者信息（`#15 <https://github.com/ros2/rosidl_runtime_py/issues/15>`__）：将维护者更新为 Shane Loretz；更新 Shane 的电子邮箱。共同署名：Shane Loretz <sloretz@openrobotics.org>
* 贡献者：Audrow Nash、Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_typesupport_c <https://github.com/ros2/rosidl_typesupport/tree/humble/rosidl_typesupport_c/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 在单一 typesupport 场景下使用 target_link_libraries(... PRIVATE ...)（`#124 <https://github.com/ros2/rosidl_typesupport/issues/124>`__）
* 清理 rosidl_typesupport_c 中的 rosidl CMake 逻辑（`#123 <https://github.com/ros2/rosidl_typesupport/issues/123>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#121 <https://github.com/ros2/rosidl_typesupport/issues/121>`__）
* 使用 FindPython3（`#118 <https://github.com/ros2/rosidl_typesupport/issues/118>`__）
* 撤销“打包并确保导出 rosidl 生成的 targets”的修改（`#116 <https://github.com/ros2/rosidl_typesupport/issues/116>`__）
* 在 CLI 扩展中支持可用的 typesupport 规范（`#112 <https://github.com/ros2/rosidl_typesupport/issues/112>`__）
* 打包并确保导出 rosidl 生成的 targets（`#113 <https://github.com/ros2/rosidl_typesupport/issues/113>`__）
* 修复 C 和 C++ typesupport CLI 扩展（`#111 <https://github.com/ros2/rosidl_typesupport/issues/111>`__）
* 贡献者：Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_typesupport_cpp <https://github.com/ros2/rosidl_typesupport/tree/humble/rosidl_typesupport_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 在单一 typesupport 场景下使用 target_link_libraries(... PRIVATE ...)（`#124 <https://github.com/ros2/rosidl_typesupport/issues/124>`__）
* 清理 rosidl_typesupport_cpp 中的 rosidl CMake 逻辑（`#123 <https://github.com/ros2/rosidl_typesupport/issues/123>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#121 <https://github.com/ros2/rosidl_typesupport/issues/121>`__）
* 确保正确检查 typesupport handles 是否为 nullptr（`#119 <https://github.com/ros2/rosidl_typesupport/issues/119>`__）
* 使用 FindPython3（`#118 <https://github.com/ros2/rosidl_typesupport/issues/118>`__）
* 撤销“打包并确保导出 rosidl 生成的 targets”的修改（`#116 <https://github.com/ros2/rosidl_typesupport/issues/116>`__）
* 在 CLI 扩展中支持可用的 typesupport 规范（`#112 <https://github.com/ros2/rosidl_typesupport/issues/112>`__）
* 打包并确保导出 rosidl 生成的 targets（`#113 <https://github.com/ros2/rosidl_typesupport/issues/113>`__）
* 修复 C 和 C++ typesupport CLI 扩展（`#111 <https://github.com/ros2/rosidl_typesupport/issues/111>`__）
* 贡献者：Chris Lalancette、Michel Hidalgo、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_typesupport_fastrtps_c <https://github.com/ros2/rosidl_typesupport_fastrtps/tree/humble/rosidl_typesupport_fastrtps_c/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将生成的头文件安装到 include/${PROJECT_NAME}（`#88 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/88>`__）
* 清理 fastrtps typesupport 生成器中的若干内容（`#87 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/87>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#86 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/86>`__）
* 修复 cpplint 的头文件包含顺序（`#84 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/84>`__）
* 将维护者更新为 Shane Loretz（`#83 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/83>`__）
* 显式使用 FindPython3，而不是隐式使用 PythonInterp（`#78 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/78>`__）
* 撤销 rosidl targets 和依赖项的导出（`#76 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/76>`__）：撤销“导出 rosidl_typesupport_fastrtps_c* 依赖”（`#75 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/75>`__）以及“打包并确保导出 rosidl 生成的 targets”（`#73 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/73>`__）。
* 正确说明 BoundedSequence 是有界序列（`#71 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/71>`__）
* 导出 rosidl_typesupport_fastrtps_c* 依赖（`#75 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/75>`__）
* 打包并确保导出 rosidl 生成的 targets（`#73 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/73>`__）
* 修复 Fast-RTPS C++ typesupport CLI 扩展（`#72 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/72>`__）
* Fast DDS 类型支持扩展（`#67 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/67>`__）
* 移除 fastrtps 依赖（`#68 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/68>`__）
* 贡献者：Andrea Sorbini、Audrow Nash、Jacob Perron、Michel Hidalgo、Miguel Company、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_typesupport_fastrtps_cpp <https://github.com/ros2/rosidl_typesupport_fastrtps/tree/humble/rosidl_typesupport_fastrtps_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将生成的头文件安装到 include/${PROJECT_NAME}（`#88 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/88>`__）
* 清理 fastrtps typesupport 生成器中的若干内容（`#87 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/87>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#86 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/86>`__）
* 修复 cpplint 的头文件包含顺序（`#84 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/84>`__）：修复头文件包含顺序；相关问题参见 https://github.com/ament/ament_lint/pull/324；其他头文件包含改用双引号，以兼容较旧版本的 cpplint。
* 将维护者更新为 Shane Loretz（`#83 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/83>`__）
* 重新引入 C++ typesupport 对原始有界序列序列化的改进（`#81 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/81>`__）
* 撤销“改进……”的修改（`#79 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/79>`__），对应撤销提交为（`#80 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/80>`__）
* 改进 C++ typesupport 中原始有界序列的序列化（`#79 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/79>`__）
* 显式使用 FindPython3，而不是隐式使用 PythonInterp（`#78 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/78>`__）
* 撤销 rosidl targets 和依赖项的导出（`#76 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/76>`__）：撤销“导出 rosidl_typesupport_fastrtps_c* 依赖”（`#75 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/75>`__）以及“打包并确保导出 rosidl 生成的 targets”（`#73 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/73>`__）。
* 正确说明 BoundedSequence 是有界序列（`#71 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/71>`__）
* 导出 rosidl_typesupport_fastrtps_c* 依赖（`#75 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/75>`__）
* 打包并确保导出 rosidl 生成的 targets（`#73 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/73>`__）
* 修复 Fast-RTPS C++ typesupport CLI 扩展（`#72 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/72>`__）
* Fast DDS 类型支持扩展（`#67 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/67>`__）
* 移除 fastrtps 依赖（`#68 <https://github.com/ros2/rosidl_typesupport_fastrtps/issues/68>`__）
* 贡献者：Andrea Sorbini、Audrow Nash、Jacob Perron、Jorge Perez、Michel Hidalgo、Miguel Company、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_typesupport_interface <https://github.com/ros2/rosidl/tree/humble/rosidl_typesupport_interface/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 从 README 和 QUALITY_DECLARATION 中移除重复的 Quality Level 内容（`#661 <https://github.com/ros2/rosidl/issues/661>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#658 <https://github.com/ros2/rosidl/issues/658>`__）
* 添加 ROSIDL_TYPESUPPORT_INTERFACE__LIBRARY_NAME() 宏（`#649 <https://github.com/ros2/rosidl/issues/649>`__）
* 将 CXX 标准设置为 17（`#635 <https://github.com/ros2/rosidl/issues/635>`__）
* 更新功能包维护者（`#624 <https://github.com/ros2/rosidl/issues/624>`__）
* 贡献者：Jose Luis Rivero、Michel Hidalgo、Shane Loretz、Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rosidl_typesupport_introspection_c <https://github.com/ros2/rosidl/tree/humble/rosidl_typesupport_introspection_c/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将生成的头文件安装到 include/${PROJECT_NAME}（`#670 <https://github.com/ros2/rosidl/issues/670>`__）
* 清理 rosidl generator 扩展中的若干内容（`#662 <https://github.com/ros2/rosidl/issues/662>`__）
* 从 README 和 QUALITY_DECLARATION 中移除重复的 Quality Level 内容（`#661 <https://github.com/ros2/rosidl/issues/661>`__）
* 将 instrospection 功能包的 README 中的 Quality 声明更新为 Level 1（`#659 <https://github.com/ros2/rosidl/issues/659>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#658 <https://github.com/ros2/rosidl/issues/658>`__）
* 将 rosidl_typesupport_introspection_cpp 的质量声明升级为 Q1（`#657 <https://github.com/ros2/rosidl/issues/657>`__）
* 将 rosidl_typesupport_introspection_c 的质量声明升级为 Q1（`#656 <https://github.com/ros2/rosidl/issues/656>`__）
* 为 generators 和 API 添加文档（`#646 <https://github.com/ros2/rosidl/issues/646>`__）
