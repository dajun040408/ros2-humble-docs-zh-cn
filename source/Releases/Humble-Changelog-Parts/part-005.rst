^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_copyright <https://github.com/ament/ament_lint/tree/humble/ament_copyright/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 Python 3.10 下的 importlib_metadata 警告（`#365 <https://github.com/ament/ament_lint/issues/365>`__）
* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* [ament_copyright] 修复文件排除行为（`#327 <https://github.com/ament/ament_lint/issues/327>`__）。此提交修复了 Issue #326 报告的文件排除缺陷：排除列表现在会与 crawler 模块遍历到的文件进行匹配。该修改参考了 PR #299。由于文件名不再在整个搜索树中进行无差别匹配，因此版权测试中列出的排除文件路径也调整为相对于功能包根目录。新增测试覆盖单文件名的错误排除、相对/绝对路径的正确排除、通配符路径的正确排除，并为 crawler 模块增加单元测试，以验证搜索和排除行为。
* 为许可证添加 SPDX 标识符（`#315 <https://github.com/ament/ament_lint/issues/315>`__）
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cppcheck <https://github.com/ament/ament_lint/tree/humble/ament_cppcheck/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 禁用 cppcheck 2.x（`#345 <https://github.com/ament/ament_lint/issues/345>`__）
* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 增加 cppcheck 库选项（`#323 <https://github.com/ament/ament_lint/issues/323>`__）：新增 ament_cppcheck 库选项，并通过 CMake 传递该选项。共同作者：William Wedler <william.wedler@resquared.com>。
* 贡献者：Audrow Nash、Chris Lalancette、Will


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cpplint <https://github.com/ament/ament_lint/tree/humble/ament_cpplint/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 忽略带有 clang-tidy 类别的 NOLINT 注释（`#339 <https://github.com/ament/ament_lint/issues/339>`__）
* 更新变更日志中的后续版本信息
* 重新应用补丁：重新应用提交 232428752251de61e84ef013bcd643e35eb9038d 中仍然适用的部分。
* 更新 cpplint 版本：改用 cpplint 的 fork，该版本包含对现代 C++ 标准（例如 C++14 和 C++17）的更新。
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* [ament_copyright] 修复文件排除行为（`#327 <https://github.com/ament/ament_lint/issues/327>`__）：排除列表现在与 crawler 模块遍历到的文件匹配；测试中的排除路径调整为相对于功能包根目录，并新增测试验证单文件名、相对/绝对路径和通配符路径的排除行为。
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Dirk Thomas、Jacob Perron、William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_flake8 <https://github.com/ament/ament_lint/tree/humble/ament_flake8/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除对 distutils.version.LooseVersion 的使用（`#346 <https://github.com/ament/ament_lint/issues/346>`__）
* 更新变更日志中的后续版本信息
* 使 ament_flake8 忽略 .*/_* 目录（`#335 <https://github.com/ament/ament_lint/issues/335>`__）。其他 ament_* 检查工具在遍历文件时会明确忽略以点或下划线开头的目录；它们此前也会隐式执行这一行为。本次修改采用相同模式，以确保行为一致。
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 忽略 flake8-blind-except 的 B902 规则（`#292 <https://github.com/ament/ament_lint/issues/292>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_index_cpp <https://github.com/ament/ament_index/tree/humble/ament_index_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/ 目录（`#83 <https://github.com/ament/ament_index/issues/83>`__）
* 移除 ament_export_include_directories 和 ament_export_libraries（`#81 <https://github.com/ament/ament_index/issues/81>`__）
* 贡献者：Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_index_python <https://github.com/ament/ament_index/tree/humble/ament_index_python/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 当 get_package_share_directory() 指向的目录不存在时打印警告（修复 `#74 <https://github.com/ament/ament_index/issues/74>`__，对应提交 `#77 <https://github.com/ament/ament_index/issues/77>`__）
* 对无效资源名称的查询直接报错（`#69 <https://github.com/ament/ament_index/issues/69>`__）
* 新增 get_package_share_path 方法（`#73 <https://github.com/ament/ament_index/issues/73>`__）
* 贡献者：David V. Lu、rob-clarke


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_lint <https://github.com/ament/ament_lint/tree/humble/ament_lint/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_lint_auto <https://github.com/ament/ament_lint/tree/humble/ament_lint_auto/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_lint_cmake <https://github.com/ament/ament_lint/tree/humble/ament_lint_cmake/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* [ament_copyright] 修复文件排除行为（`#327 <https://github.com/ament/ament_lint/issues/327>`__）：排除列表现在与 crawler 模块遍历到的文件匹配；测试中的排除路径调整为相对于功能包根目录，并新增测试验证单文件名、相对/绝对路径和通配符路径的排除行为。
* 贡献者：Abrar Rahman Protyasha、Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_lint_common <https://github.com/ament/ament_lint/tree/humble/ament_lint_common/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 修复 ament_lint_common/package.xml 中的拼写错误（`#336 <https://github.com/ament/ament_lint/issues/336>`__）
* 贡献者：Audrow Nash、Kenji Miyake


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_mypy <https://github.com/ament/ament_lint/tree/humble/ament_mypy/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 通过明确不同工具的用途来改进文档（`#357 <https://github.com/ament/ament_lint/issues/357>`__）
* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 贡献者：Audrow Nash、Bi0T1N


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_package <https://github.com/ament/ament_package/tree/humble/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将上一版本标记为后续版本
