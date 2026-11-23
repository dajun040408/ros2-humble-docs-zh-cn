* 新增向环境变量追加内容的支持（`#130 <https://github.com/ament/ament_package/issues/130>`__）。其工作方式与“prepend-non-duplicate”（前置且避免重复）基本相同，但会将候选值放在目标变量末尾。
* 将维护者更新为 Audrow Nash（`#135 <https://github.com/ament/ament_package/issues/135>`__）
* 将 Python 可执行文件变量改为 ament_package 专用变量（`#134 <https://github.com/ament/ament_package/issues/134>`__）
* 贡献者：Audrow Nash、Scott K Logan、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_pclint <https://github.com/ament/ament_lint/tree/humble/ament_pclint/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 通过明确不同工具的用途来改进文档（`#357 <https://github.com/ament/ament_lint/issues/357>`__）
* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* [ament_copyright] 修复文件排除行为（`#327 <https://github.com/ament/ament_lint/issues/327>`__）：排除列表现在与 crawler 模块遍历到的文件匹配；测试中的排除路径调整为相对于功能包根目录，并新增测试验证单文件名、相对/绝对路径和通配符路径的排除行为。
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Bi0T1N


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_pep257 <https://github.com/ament/ament_lint/tree/humble/ament_pep257/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 通过明确不同工具的用途来改进文档（`#357 <https://github.com/ament/ament_lint/issues/357>`__）
* 移除对 distutils.version.LooseVersion 的使用（`#346 <https://github.com/ament/ament_lint/issues/346>`__）
* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 贡献者：Audrow Nash、Bi0T1N、Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_pycodestyle <https://github.com/ament/ament_lint/tree/humble/ament_pycodestyle/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 通过明确不同工具的用途来改进文档（`#357 <https://github.com/ament/ament_lint/issues/357>`__）
* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 贡献者：Audrow Nash、Bi0T1N


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_pyflakes <https://github.com/ament/ament_lint/tree/humble/ament_pyflakes/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_uncrustify <https://github.com/ament/ament_lint/tree/humble/ament_uncrustify/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* [ament_uncrustify] 修复文件排除行为（`#334 <https://github.com/ament/ament_lint/issues/334>`__）：排除列表会在遍历搜索路径时与文件和目录进行匹配。该实现尽量与 `#327` 的行为保持一致；同时新增文件排除测试，并移除错误的 pytest 标记。
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* [ament_uncrustify] 新增 ament_lint 测试（`#338 <https://github.com/ament/ament_lint/issues/338>`__）：为 ament_uncrustify 添加 ament_lint 测试，并修复其中的代码检查警告。
* 贡献者：Abrar Rahman Protyasha、Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_xmllint <https://github.com/ament/ament_lint/tree/humble/ament_xmllint/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`builtin_interfaces <https://github.com/ros2/rcl_interfaces/tree/humble/builtin_interfaces/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Chris Lalancette（`#130 <https://github.com/ros2/rcl_interfaces/issues/130>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`camera_calibration_parsers <https://github.com/ros-perception/image_common/tree/humble/camera_calibration_parsers/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 测试依赖 rcpputils（`#236 <https://github.com/ros-perception/image_common/issues/236>`__）
* 移除 YAML_CPP_DLL 定义（`#231 <https://github.com/ros-perception/image_common/issues/231>`__）
* 导出现代 CMake 目标以替代变量，并将头文件安装到 include/${PROJECT_NAME}（`#218 <https://github.com/ros-perception/image_common/issues/218>`__）
* 更新维护者信息（`#173 <https://github.com/ros-perception/image_common/issues/173>`__）
* 贡献者：Akash、Alejandro Hernández Cordero、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`camera_info_manager <https://github.com/ros-perception/image_common/tree/humble/camera_info_manager/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 导出现代 CMake 目标以替代变量，并将头文件安装到 include/${PROJECT_NAME}（`#218 <https://github.com/ros-perception/image_common/issues/218>`__）
* 更新维护者信息（`#173 <https://github.com/ros-perception/image_common/issues/173>`__）
* 贡献者：Alejandro Hernández Cordero、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`class_loader <https://github.com/ros/class_loader/tree/humble/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/ 目录（`#191 <https://github.com/ros/class_loader/issues/191>`__）
* 修复 cpplint 的头文件包含顺序问题（`#192 <https://github.com/ros/class_loader/issues/192>`__）
* 将维护者更新为 Geoffrey Biggs 和 Michael Carroll（`#190 <https://github.com/ros/class_loader/issues/190>`__）
* 修正拼写错误（`#184 <https://github.com/ros/class_loader/issues/184>`__）
* 贡献者：Audrow Nash、David V. Lu!!、Jacob Perron、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`common_interfaces <https://github.com/ros2/common_interfaces/tree/humble/common_interfaces/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Geoffrey Biggs 和 Tully Foote（`#163 <https://github.com/ros2/common_interfaces/issues/163>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`composition <https://github.com/ros2/demos/tree/humble/composition/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将维护者更新为 Audrow Nash 和 Michael Jeronimo（`#543 <https://github.com/ros2/demos/issues/543>`__）
* 修复 demos 文档中的其他问题（`#538 <https://github.com/ros2/demos/issues/538>`__）
