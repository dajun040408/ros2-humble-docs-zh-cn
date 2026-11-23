^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_pycodestyle <https://github.com/ament/ament_lint/tree/galactic/ament_cmake_pycodestyle/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 版本 0.10.3
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_pyflakes <https://github.com/ament/ament_lint/tree/galactic/ament_cmake_pyflakes/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 版本 0.10.3
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_pytest <https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_pytest/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复较新版本 pytest 中的 ament_get_pytest_cov_version（`#315 <https://github.com/ament/ament_cmake/issues/315>`__）
* 更新功能包维护者（`#286 <https://github.com/ament/ament_cmake/issues/286>`__）
* 贡献者：Christophe Bedard、Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_python <https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_python/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 在构建 Python egg-info 之前，为 setup.cfg 和源文件创建符号链接（`#327 <https://github.com/ament/ament_cmake/issues/327>`__）
* 简化 ament_python_install_package() 宏（`#326 <https://github.com/ament/ament_cmake/issues/326>`__）：不再委托给 setuptools，而是手动安装 egg-info。
* 在 ament_python_install_package() 中对所有位置的 $ENV{DESTDIR} 进行转义（`#324 <https://github.com/ament/ament_cmake/issues/324>`__），这是对提交 f80071e2216e766f7bf1b0792493a5f6523e9226 的后续修复。
* 在 ament_python_install_package() 中使用 DESTDIR（`#323 <https://github.com/ament/ament_cmake/issues/323>`__）
* 使 ament_python_install_package() 安装扁平化的 Python egg（`#316 <https://github.com/ament/ament_cmake/issues/316>`__）
* [ament_cmake_python] 将 ament_cmake_python_get_python_install_dir 设为公共接口（`#300 <https://github.com/ament/ament_cmake/issues/300>`__）
* 更新功能包维护者（`#286 <https://github.com/ament/ament_cmake/issues/286>`__）
* 贡献者：Michel Hidalgo、Naveau


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_ros <https://github.com/ros2/ament_cmake_ros/tree/galactic/ament_cmake_ros/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新功能包维护者（`#11 <https://github.com/ros2/ament_cmake_ros/issues/11>`__）
* 贡献者：Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_target_dependencies <https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_target_dependencies/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 强制在 ament_target_dependencies() 开始处使用 SYSTEM 关键字（`#303 <https://github.com/ament/ament_cmake/issues/303>`__）
* 为 ament_target_dependencies 添加 SYSTEM 关键字选项（`#297 <https://github.com/ament/ament_cmake/issues/297>`__），并补充该选项的文档说明。
* 更新功能包维护者（`#286 <https://github.com/ament/ament_cmake/issues/286>`__）
* 对 interface include 目录排序，并将其设为私有，以确保工作空间中的目录顺序正确（`#260 <https://github.com/ament/ament_cmake/issues/260>`__）
* 贡献者：Andre Nguyen、Dirk Thomas、Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_test <https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_test/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新功能包维护者（`#286 <https://github.com/ament/ament_cmake/issues/286>`__）
* 修复 CTest 中跳过测试的报告问题（`#279 <https://github.com/ament/ament_cmake/issues/279>`__）：这是对提交 c67cdf2 的后续修复。当 SKIP_RETURN_CODE 被设置为 0 时，该值会被解释为 'false'，因此测试属性实际上从未被添加。
* 将测试时间精度限制为小数点后三位（`#271 <https://github.com/ament/ament_cmake/issues/271>`__）
* 在 xUnit 结果文件中添加实际测试耗时（`#270 <https://github.com/ament/ament_cmake/issues/270>`__）：修复问题 `#269 <https://github.com/ament/ament_cmake/issues/269>`__；即使测试被跳过也报告 test_time；为 testcase 元素设置 time 属性。
* 为 ament_add_test 添加 SKIP_RETURN_CODE 参数（`#264 <https://github.com/ament/ament_cmake/issues/264>`__）：使 run_test.py 包装脚本能够识别 CTest 测试的 SKIP_RETURN_CODE 属性。此前，包装脚本检测到未生成结果文件时，会覆盖测试返回的特殊代码，导致 CTest 功能完全失效。此次修改使包装脚本能够识别该特殊返回码，并在检测到时写入 'skipped' 结果文件，而不是 'failed' 结果文件，同时原样传递特殊返回码。启用该功能后，gtest 和 ctest 结果都会将测试标记为 'skipped'。该行为默认不启用；只有明确支持此功能的测试才应使用它，以免测试失败时意外返回被定义为“跳过”的特殊代码。
* 贡献者：Dirk Thomas、Michel Hidalgo、Ruffin、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_uncrustify <https://github.com/ament/ament_lint/tree/galactic/ament_cmake_uncrustify/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 版本 0.10.3
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 以不区分大小写的方式解析 LANGUAGE 参数（`#255 <https://github.com/ament/ament_lint/issues/255>`__）
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang、Karsten Knese、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_version <https://github.com/ament/ament_cmake/tree/galactic/ament_cmake_version/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 更新功能包维护者（`#286 <https://github.com/ament/ament_cmake/issues/286>`__）
* 贡献者：Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_cmake_xmllint <https://github.com/ament/ament_lint/tree/galactic/ament_cmake_xmllint/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 版本 0.10.3
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 更新维护者信息（`#274 <https://github.com/ament/ament_lint/issues/274>`__）：更新维护者并添加作者。
* 贡献者：Audrow Nash、Chris Lalancette、Claire Wang、Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ament_copyright <https://github.com/ament/ament_lint/tree/galactic/ament_copyright/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 移除 Claire 的维护者身份（`#312 <https://github.com/ament/ament_lint/issues/312>`__）：移除 Claire 作为维护者的记录；删除失效的电子邮箱地址；继续清理其他失效邮箱；将 setup.py 中的维护者更新为 Audrow。
* 使用非盲目的 except 处理 open()（`#307 <https://github.com/ament/ament_lint/issues/307>`__）
* 添加可选的文件头样式（`#304 <https://github.com/ament/ament_lint/issues/304>`__），并修复 ament_copyright 测试。
* 版本 0.10.3
* 将 Audrow 添加为维护者（`#294 <https://github.com/ament/ament_lint/issues/294>`__）
* 移除功能包清单末尾的制表符（`#291 <https://github.com/ament/ament_lint/issues/291>`__），这是对提交 8bf194aa1ac282db5483dd0d3fefff8f325b0db8 的后续修复。
* 将 mit-0 添加为 ament_copyright 的有效许可证（`#284 <https://github.com/ament/ament_lint/issues/284>`__）
* 支持 Python 3.8 提供的 importlib.metadata（`#290 <https://github.com/ament/ament_lint/issues/290>`__）：importlib_metadata 软件包是 Python 3.8 importlib.metadata 模块的回移植版本。Fedora（以及可能的其他发行版）不再单独打包 importlib_metadata，因为它们提供的 Python 版本已经内置了该功能。
