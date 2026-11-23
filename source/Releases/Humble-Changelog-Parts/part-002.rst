* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_core <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_core/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 修复多项 ament_lint 代码检查违规（`#360 <https://github.com/ament/ament_cmake/issues/360>`__）。由于不同仓库之间会形成循环依赖，无法按常规方式在 ament_cmake 中添加 ament_lint 检查器。虽然无法自动强制执行代码检查，但仍建议在条件允许时尽可能保持规范一致。
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 支持以可执行目标作为命令（`#352 <https://github.com/ament/ament_cmake/issues/352>`__）
* 修正 doc/resource_index 中列表子项的缩进（`#342 <https://github.com/ament/ament_cmake/issues/342>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Michal Sojka、Scott K Logan、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_cppcheck <https://github.com/ament/ament_lint/tree/humble/ament_cmake_cppcheck/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* [ament_cmake_cppcheck] 修复文件排除行为（`#329 <https://github.com/ament/ament_lint/issues/329>`__）。``ament_cppcheck`` CMake 函数的 ``EXCLUDE`` 参数是一个列表，即支持多个值的关键字。因此，在调用 ``cmake_parse_arguments`` 时，该参数必须放在单值关键字之后。
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 增加 cppcheck 库选项（`#323 <https://github.com/ament/ament_lint/issues/323>`__）：新增 ament_cppcheck 库选项，并通过 CMake 传递该选项。共同作者：William Wedler <william.wedler@resquared.com>。
* 贡献者：Abrar Rahman Protyasha、Audrow Nash、Will


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_cpplint <https://github.com/ament/ament_lint/tree/humble/ament_cmake_cpplint/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_export_definitions <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_definitions/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_export_dependencies <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_dependencies/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 修复多项 ament_lint 代码检查违规（`#360 <https://github.com/ament/ament_cmake/issues/360>`__）。由于不同仓库之间会形成循环依赖，无法按常规方式在 ament_cmake 中添加 ament_lint 检查器。虽然无法自动强制执行代码检查，但仍建议在条件允许时尽可能保持规范一致。
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Scott K Logan、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_export_include_directories <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_include_directories/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_export_interfaces <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_interfaces/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_export_libraries <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_libraries/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 修复多项 ament_lint 代码检查违规（`#360 <https://github.com/ament/ament_cmake/issues/360>`__）。由于不同仓库之间会形成循环依赖，无法按常规方式在 ament_cmake 中添加 ament_lint 检查器。虽然无法自动强制执行代码检查，但仍建议在条件允许时尽可能保持规范一致。
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 增加有关接口库的说明（`#339 <https://github.com/ament/ament_cmake/issues/339>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Bjar Ne、Chris Lalancette、Scott K Logan、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_export_link_flags <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_link_flags/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_export_targets <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_targets/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_flake8 <https://github.com/ament/ament_lint/tree/humble/ament_cmake_flake8/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
