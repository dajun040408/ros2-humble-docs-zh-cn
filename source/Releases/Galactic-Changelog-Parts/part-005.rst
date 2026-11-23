* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 添加 BSD 2-Clause Simplified 许可证作为 ament_copyright 的支持许可证（`#267 <https://github.com/ament/ament_lint/issues/267>`__）
* 从 ament_lint 中移除 pkg_resources，改用较新的 importlib_metadata 库（`#260 <https://github.com/ament/ament_lint/issues/260>`__）。这样做有几个原因：首先，pkg_resources 导入速度较慢；在作者的计算机上，启动 Python 解释器约需 35 毫秒，启动后导入 pkg_resources 则约需 175 毫秒，而导入 importlib_metadata 约需 70 毫秒。每次命令行调用减少约 100 毫秒，既能提升用户体验，也能加快频繁调用命令行的测试。其次，pkg_resources 已在一定程度上被弃用，正逐步由 importlib 取代。更多说明参见 https://importlib-metadata.readthedocs.io/en/latest/using.html。注意：仅靠此修改还不能完全移除对 pkg_resources 的依赖，还需要处理 setup.py 生成的 console_scripts，这将作为单独工作完成。
* 添加 pytest.ini，避免本地测试显示警告（`#259 <https://github.com/ament/ament_lint/issues/259>`__）
* 贡献者：Alfi Maulana、Audrow Nash、Chris Lalancette、Christophe Bedard、Claire Wang、Evan Flynn、M. Mei、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cppcheck <https://github.com/ament/ament_lint/tree/galactic/ament_cppcheck/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 版本 0.10.3
* 修复 ament_cppcheck 和 ament_cpplint 的文件排除行为（`#299 <https://github.com/ament/ament_lint/issues/299>`__）：修复排除行为、修复 flake8 错误，并补充缺失的 realpath() 转换。
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 抑制 unknownMacro（`#268 <https://github.com/ament/ament_lint/issues/268>`__）：当 cppcheck 无法解析某个宏时会产生 unknownMacro 错误。由于没有传入所有依赖头文件，因此并不期望 cppcheck 能发现全部宏。
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 添加 pytest.ini，避免本地测试显示警告（`#259 <https://github.com/ament/ament_lint/issues/259>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang、Dan Rose、M. Mei、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cpplint <https://github.com/ament/ament_lint/tree/galactic/ament_cpplint/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 版本 0.10.3
* 修复 ament_cppcheck 和 ament_cpplint 的文件排除行为（`#299 <https://github.com/ament/ament_lint/issues/299>`__）：修复排除行为、修复 flake8 错误，并补充缺失的 realpath() 转换。
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 添加 pytest.ini，避免本地测试显示警告（`#259 <https://github.com/ament/ament_lint/issues/259>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang、M. Mei、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_flake8 <https://github.com/ament/ament_lint/tree/galactic/ament_flake8/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 版本 0.10.3
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 添加 pytest.ini，避免本地测试显示警告（`#259 <https://github.com/ament/ament_lint/issues/259>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_index_cpp <https://github.com/ament/ament_index/tree/galactic/ament_index_cpp/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#71 <https://github.com/ament/ament_index/issues/71>`__）
* 将链接从 index.ros.org 更改为 docs.ros.org（`#70 <https://github.com/ament/ament_index/issues/70>`__）
* 将 Audrow 添加为维护者（`#68 <https://github.com/ament/ament_index/issues/68>`__）
* 更新维护者信息（`#67 <https://github.com/ament/ament_index/issues/67>`__）
* 将质量声明更新为质量等级 1（`#66 <https://github.com/ament/ament_index/issues/66>`__）
* 补充 ament_index 功能包不包含显式性能测试的原因说明（`#65 <https://github.com/ament/ament_index/issues/65>`__）
* 修复 Doxygen 警告（`#63 <https://github.com/ament/ament_index/issues/63>`__）
* 从 README.md 中移除质量等级（`#62 <https://github.com/ament/ament_index/issues/62>`__）
* 将 ament_index_cpp 的质量声明更新为 QL 2（`#59 <https://github.com/ament/ament_index/issues/59>`__）
* 添加指向 REP-2006 的安全漏洞策略（`#57 <https://github.com/ament/ament_index/issues/57>`__）
* [质量声明] 将版本稳定性更新为 stable（`#58 <https://github.com/ament/ament_index/issues/58>`__）
* 贡献者：Alejandro Hernández Cordero、Audrow Nash、Chris Lalancette、Claire Wang、Dirk Thomas、brawner


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_index_python <https://github.com/ament/ament_index/tree/galactic/ament_index_python/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#71 <https://github.com/ament/ament_index/issues/71>`__）
* 将链接从 index.ros.org 更改为 docs.ros.org（`#70 <https://github.com/ament/ament_index/issues/70>`__）
* 将 Audrow 添加为维护者（`#68 <https://github.com/ament/ament_index/issues/68>`__）
* 更新维护者信息（`#67 <https://github.com/ament/ament_index/issues/67>`__）
* 补充 ament_index 功能包不包含显式性能测试的原因说明（`#65 <https://github.com/ament/ament_index/issues/65>`__）
* 从 README.md 中移除质量等级（`#62 <https://github.com/ament/ament_index/issues/62>`__）
* 修复文档链接（`#61 <https://github.com/ament/ament_index/issues/61>`__）
* [质量声明] 将版本稳定性更新为 stable（`#58 <https://github.com/ament/ament_index/issues/58>`__）
* 贡献者：Alejandro Hernández Cordero、Audrow Nash、Chris Lalancette、Claire Wang、Dirk Thomas、Matthijs van der Burgh


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_lint <https://github.com/ament/ament_lint/tree/galactic/ament_lint/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 版本 0.10.3
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 添加 pytest.ini，避免本地测试显示警告（`#259 <https://github.com/ament/ament_lint/issues/259>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_lint_auto <https://github.com/ament/ament_lint/tree/galactic/ament_lint_auto/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 版本 0.10.3
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 使用正确的代码检查功能包依赖项（`#278 <https://github.com/ament/ament_lint/issues/278>`__）
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang、Esteve Fernandez、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_lint_cmake <https://github.com/ament/ament_lint/tree/galactic/ament_lint_cmake/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* ament_lint_cmake：为保持一致，在 argumentparser 中设置默认行长度（`#306 <https://github.com/ament/ament_lint/issues/306>`__）
* 版本 0.10.3
* 修复 ament_lint_cmake 的行长度表达式（`#236 <https://github.com/ament/ament_lint/issues/236>`__）：该正则表达式使用 re.VERBOSE 标志，因此未转义的 '#' 字符后面的内容会被解释为注释，而不会成为表达式的一部分。同时将默认最大行长度设置为 140 列。
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 使 CMake 代码检查器的行长度可配置（`#235 <https://github.com/ament/ament_lint/issues/235>`__）。共同署名：Miaofei <miaofei@amazon.com>
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 添加 pytest.ini，避免本地测试显示警告（`#259 <https://github.com/ament/ament_lint/issues/259>`__）
