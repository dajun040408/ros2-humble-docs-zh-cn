^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_flake8 <https://github.com/ament/ament_lint/tree/humble/ament_cmake_flake8/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 新增 flake8 自定义配置文件支持（`#331 <https://github.com/ament/ament_lint/issues/331>`__）
* 贡献者：Audrow Nash、Kenji Miyake


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_gen_version_h <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_gen_version_h/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 新增 ament_generate_version_header，并将 ament_cmake_gen_version_h 标记为弃用（`#377 <https://github.com/ament/ament_cmake/issues/377>`__）
* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 新增 ament_cmake_gen_version_h 功能包（`#198 <https://github.com/ament/ament_cmake/issues/198>`__）
* 贡献者：Audrow Nash、Shane Loretz、serge-nikulin


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_gmock <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_gmock/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_google_benchmark <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_google_benchmark/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 修复多项 ament_lint 代码检查违规（`#360 <https://github.com/ament/ament_cmake/issues/360>`__）。由于不同仓库之间会形成循环依赖，无法按常规方式在 ament_cmake 中添加 ament_lint 检查器。虽然无法自动强制执行代码检查，但仍建议在条件允许时尽可能保持规范一致。
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Scott K Logan、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_gtest <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_gtest/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_include_directories <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_include_directories/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将 ament_include_directories_order 改为函数，以支持 Windows 上包含反斜杠的路径（`#371 <https://github.com/ament/ament_cmake/issues/371>`__）。相关调整包括：在 Windows 上将反斜杠替换为正斜杠；修正拼写；替换 ARGN 中的斜杠；移除不必要的引号；在执行 string(REPLACE) 前检查 ARGN 是否有值；并将 ament_include_directories_order 实现为函数。
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_libraries <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_libraries/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 修复多项 ament_lint 代码检查违规（`#360 <https://github.com/ament/ament_cmake/issues/360>`__）。由于不同仓库之间会形成循环依赖，无法按常规方式在 ament_cmake 中添加 ament_lint 检查器。虽然无法自动强制执行代码检查，但仍建议在条件允许时尽可能保持规范一致。
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Scott K Logan、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_lint_cmake <https://github.com/ament/ament_lint/tree/humble/ament_cmake_lint_cmake/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 贡献者：Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_mypy <https://github.com/ament/ament_lint/tree/humble/ament_cmake_mypy/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 通过明确不同工具的用途来改进文档（`#357 <https://github.com/ament/ament_lint/issues/357>`__）
* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 贡献者：Audrow Nash、Bi0T1N


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_nose <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_nose/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#362 <https://github.com/ament/ament_cmake/issues/362>`__）
* 使用 FindPython3 替代 FindPythonInterp（`#355 <https://github.com/ament/ament_cmake/issues/355>`__）
* 支持以可执行目标作为命令（`#352 <https://github.com/ament/ament_cmake/issues/352>`__）
* 更新维护者信息（`#336 <https://github.com/ament/ament_cmake/issues/336>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_pclint <https://github.com/ament/ament_lint/tree/humble/ament_cmake_pclint/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 通过明确不同工具的用途来改进文档（`#357 <https://github.com/ament/ament_lint/issues/357>`__）
* 更新变更日志中的后续版本信息
* 将维护者更新为 Michael Jeronimo 和 Michel Hidalgo（`#340 <https://github.com/ament/ament_lint/issues/340>`__）
* 贡献者：Audrow Nash、Bi0T1N


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_pep257 <https://github.com/ament/ament_lint/tree/humble/ament_cmake_pep257/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
