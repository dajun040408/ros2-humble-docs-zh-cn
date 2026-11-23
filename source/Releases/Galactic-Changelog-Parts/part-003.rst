* 版本 0.10.3
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_gmock <https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_gmock/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新功能包维护者（`#286 <https://github.com/ament/ament_cmake/issues/286>`__）
* 贡献者：Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_google_benchmark <https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_google_benchmark/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 默认在 CTest 中串行运行基准测试（`#308 <https://github.com/ament/ament_cmake/issues/308>`__）
* 处理 Google Benchmark 的运行时失败（`#294 <https://github.com/ament/ament_cmake/issues/294>`__）：将 Google Benchmark 的错误信息同时传递给 CTest 和 Jenkins 基准测试插件。
* 统一字符串格式并解决 flake8 问题（`#295 <https://github.com/ament/ament_cmake/issues/295>`__），这是对提交 a5fb3112b5c46c42b1824c96af4171d469eb13bf 的后续修复。
* 将 ament_cmake_test 设为 ament_cmake_google_benchmark 的依赖（`#293 <https://github.com/ament/ament_cmake/issues/293>`__）
* 捕获 JSONDecodeError 并输出调试信息（`#291 <https://github.com/ament/ament_cmake/issues/291>`__）
* 更新功能包维护者（`#286 <https://github.com/ament/ament_cmake/issues/286>`__）
* 将 AMENT_RUN_PERFORMANCE_TESTS 设置为 CMake 选项（`#280 <https://github.com/ament/ament_cmake/issues/280>`__）
* 使用 CMake 变量跳过性能测试（`#278 <https://github.com/ament/ament_cmake/issues/278>`__）：这些测试开销较大，因此默认不应运行。理想情况下，应提供一种默认跳过、但可在运行时明确启用的机制；不过，除环境变量外，尚未找到可通过 CMake 或 CTest 实现该行为的方法。
* 处理 Google Benchmark 的 'aggregate' 结果（`#276 <https://github.com/ament/ament_cmake/issues/276>`__）：此前假设 Google Benchmark 生成的所有结果均为 'iteration' 类型。现在也会生成包含不同属性的 aggregate 结果。本次修改增加了对 aggregate 结果的支持，并便于将来扩展其他结果模式。为保持向前兼容，不支持的类型只会产生警告，不会导致测试失败；因此，即使 Google Benchmark 为现有机制增加新度量，转换过程也能保持兼容。
* 初步实现 Google Benchmark 结果转换（`#275 <https://github.com/ament/ament_cmake/issues/275>`__）
* 处理 Google Benchmark 结果文件缺失的情况（`#265 <https://github.com/ament/ament_cmake/issues/265>`__）
* 初始创建 ament_cmake_google_benchmark 功能包（`#261 <https://github.com/ament/ament_cmake/issues/261>`__）
* 贡献者：Michel Hidalgo、Scott K Logan、brawner


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_gtest <https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_gtest/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 在 Release 构建中禁用 gtest 警告（`#298 <https://github.com/ament/ament_cmake/issues/298>`__），参见 https://github.com/google/googletest/issues/1303
* 更新功能包维护者（`#286 <https://github.com/ament/ament_cmake/issues/286>`__）
* [ament_cmake_gtest] 确保 gtest 使用正确的头文件（`#267 <https://github.com/ament/ament_cmake/issues/267>`__）：确保 gtest 使用正确的头文件，并添加另一项补丁。
* 贡献者：Michel Hidalgo、Sean Yen、Victor Lopez


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_include_directories <https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_include_directories/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新功能包维护者（`#286 <https://github.com/ament/ament_cmake/issues/286>`__）
* 贡献者：Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_libraries <https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_libraries/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新功能包维护者（`#286 <https://github.com/ament/ament_cmake/issues/286>`__）
* 贡献者：Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_lint_cmake <https://github.com/ament/ament_lint/tree/galactic/ament_cmake_lint_cmake/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* ament_lint_cmake：为保持一致，在 argumentparser 中设置默认行长度（`#306 <https://github.com/ament/ament_lint/issues/306>`__）
* 版本 0.10.3
* 修复 ament_lint_cmake 的行长度表达式（`#236 <https://github.com/ament/ament_lint/issues/236>`__）：该正则表达式使用 re.VERBOSE 标志，因此未转义的 '#' 字符后面的内容会被解释为注释，而不会成为表达式的一部分。同时将默认最大行长度设置为 140 列。
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 使 CMake 代码检查器的行长度可配置（`#235 <https://github.com/ament/ament_lint/issues/235>`__）。共同署名：Miaofei <miaofei@amazon.com>
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang、Emerson Knapp、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_mypy <https://github.com/ament/ament_lint/tree/galactic/ament_cmake_mypy/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 版本 0.10.3
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_nose <https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_nose/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新功能包维护者（`#286 <https://github.com/ament/ament_cmake/issues/286>`__）
* 贡献者：Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_pclint <https://github.com/ament/ament_lint/tree/galactic/ament_cmake_pclint/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 版本 0.10.3
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_pep257 <https://github.com/ament/ament_lint/tree/galactic/ament_cmake_pep257/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 版本 0.10.3
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang、Scott K Logan
