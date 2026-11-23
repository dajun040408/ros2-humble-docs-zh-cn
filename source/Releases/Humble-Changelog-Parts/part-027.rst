^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rviz_assimp_vendor <https://github.com/ros2/rviz/tree/humble/rviz_assimp_vendor/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 确保将编译器及其标志传递给 assimp（`#844 <https://github.com/ros2/rviz/issues/844>`__）
* 修复对 assimp 5.1.0 的支持（`#817 <https://github.com/ros2/rviz/issues/817>`__）
* 贡献者：Chris Lalancette、Silvio Traversaro


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rviz_common <https://github.com/ros2/rviz/tree/humble/rviz_common/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 为 cancel 接口添加实现（`#809 <https://github.com/ros2/rviz/issues/809>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#829 <https://github.com/ros2/rviz/issues/829>`__）
* 移除 PLUGINLIB_DISABLE_BOOST 的定义（`#821 <https://github.com/ros2/rviz/issues/821>`__）
* 修复对 assimp 5.1.0 的支持（`#817 <https://github.com/ros2/rviz/issues/817>`__）
* 修复 cpplint 错误（`#818 <https://github.com/ros2/rviz/issues/818>`__）
* 为 ros topic display 设置消息类型（`#800 <https://github.com/ros2/rviz/issues/800>`__）
* 修复与 uncrustify 0.72 的兼容问题（`#807 <https://github.com/ros2/rviz/issues/807>`__）
* 打开 display panel 对话框时，不阻塞 visualization manager 的更新（`#795 <https://github.com/ros2/rviz/issues/795>`__）
* RViz 改用 Qt::MiddleButton（`#802 <https://github.com/ros2/rviz/issues/802>`__）
* 移除 renderPanel 中的跟踪代码（`#777 <https://github.com/ros2/rviz/issues/777>`__）
* 将 yaml_config_writer.hpp 移至公共头文件目录（`#764 <https://github.com/ros2/rviz/issues/764>`__）
* 更新 displays_panel.cpp（`#745 <https://github.com/ros2/rviz/issues/745>`__）
* Robot：报告网格模型加载问题（`#744 <https://github.com/ros2/rviz/issues/744>`__）
* 暴露 tool_manager 头文件（`#767 <https://github.com/ros2/rviz/issues/767>`__）
* 重构：将 const getter 方法改为 const（`#756 <https://github.com/ros2/rviz/issues/756>`__）
* 高效处理 3 字节像素格式（`#743 <https://github.com/ros2/rviz/issues/743>`__）
* 报告样本丢失事件（`#686 <https://github.com/ros2/rviz/issues/686>`__）
* 更新窗口关闭图标（`#734 <https://github.com/ros2/rviz/issues/734>`__）
* 修复面板关闭按钮中缺失“X”图标的问题（`#731 <https://github.com/ros2/rviz/issues/731>`__）
* 为 rviz_common 添加 rviz_rendering 依赖（`#727 <https://github.com/ros2/rviz/issues/727>`__）
* 从启动画面中移除“Alpha”一词（`#696 <https://github.com/ros2/rviz/issues/696>`__）
* 修复 rviz_rendering 和 rviz_rendering_tests 中的部分内存泄漏（`#710 <https://github.com/ros2/rviz/issues/710>`__）
* 贡献者：ANDOU Tetsuo、Alejandro Hernández Cordero、Chen Lihui、Chris Lalancette、Daisuke Nishimatsu、Gonzo、Ivan Santiago Paunovic、Jacob Perron、Joseph Schornak、Rebecca Butler、Shane Loretz、Silvio Traversaro、davidorchansky


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rviz_default_plugins <https://github.com/ros2/rviz/tree/humble/rviz_default_plugins/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 为相机添加远裁剪平面距离属性（`#849 <https://github.com/ros2/rviz/issues/849>`__）
* 从 rviz_default_plugins 的链接接口中移除 ignition-math6（`#833 <https://github.com/ros2/rviz/issues/833>`__）
* 为 cancel 接口添加实现（`#809 <https://github.com/ros2/rviz/issues/809>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#829 <https://github.com/ros2/rviz/issues/829>`__）
* 移除 PLUGINLIB_DISABLE_BOOST 的定义（`#821 <https://github.com/ros2/rviz/issues/821>`__）
* 从 ImageTransportDisplay 中移除 TF filter（`#788 <https://github.com/ros2/rviz/issues/788>`__）
* 在材质名称中添加下划线（`#811 <https://github.com/ros2/rviz/issues/811>`__）
* 导出 image_transport 依赖（`#813 <https://github.com/ros2/rviz/issues/813>`__）
* 修复与 uncrustify 0.72 的兼容问题（`#807 <https://github.com/ros2/rviz/issues/807>`__）
* RViz 改用 Qt::MiddleButton（`#802 <https://github.com/ros2/rviz/issues/802>`__）
* 为 tf_wrapper 添加 tf_buffer_cache_time_ns（`#792 <https://github.com/ros2/rviz/issues/792>`__）
* 将代码编译为库，避免重复编译文件（`#774 <https://github.com/ros2/rviz/issues/774>`__）
* 使用 ignition-math 计算惯性（`#751 <https://github.com/ros2/rviz/issues/751>`__）
* 修复在取消勾选“Selectable”选项时更改 pointcloud2 渲染参数导致崩溃的问题（`#768 <https://github.com/ros2/rviz/issues/768>`__）
* Robot：报告网格模型加载问题（`#744 <https://github.com/ros2/rviz/issues/744>`__）
* 处理 Wrench 消息中的 NaN 值（`#746 <https://github.com/ros2/rviz/issues/746>`__）
* 三角形列表支持纹理（`#719 <https://github.com/ros2/rviz/issues/719>`__）
* 报告样本丢失事件（`#686 <https://github.com/ros2/rviz/issues/686>`__）
* 修复 Path 消息的方向错误（`#736 <https://github.com/ros2/rviz/issues/736>`__）
* 在交互式标记显示中设置话题命名空间（`#725 <https://github.com/ros2/rviz/issues/725>`__）
* 质量属性可视化（`#714 <https://github.com/ros2/rviz/issues/714>`__）
* 导出 InteractiveMarker（`#718 <https://github.com/ros2/rviz/issues/718>`__）
* YUV 转 RGB 相关修改（`#701 <https://github.com/ros2/rviz/issues/701>`__）
* 在 ImageTransportDisplay 中提取消息类型（`#711 <https://github.com/ros2/rviz/issues/711>`__）
* 消除 RobotJoint 中的重复代码（`#702 <https://github.com/ros2/rviz/issues/702>`__）
* 不再尝试对不包含 QOBJECT 的文件生成 moc 文件（`#690 <https://github.com/ros2/rviz/issues/690>`__）
* 改为包含 tf2_geometry_msgs.hpp（`#689 <https://github.com/ros2/rviz/issues/689>`__）
* 正确导出 Qt5 依赖（`#687 <https://github.com/ros2/rviz/issues/687>`__）
* 为 Marker displays 添加命名空间范围的 DELETEALL action 支持（`#685 <https://github.com/ros2/rviz/issues/685>`__）
* 使用 image_transport 订阅图像消息（`#523 <https://github.com/ros2/rviz/issues/523>`__）
* 贡献者：Akash、Alejandro Hernández Cordero、Audrow Nash、Chen Lihui、Chris Lalancette、Cory Crean、Gonzo、Greg Balke、Ivan Santiago Paunovic、Jacob Perron、Martin Idel、Michel Hidalgo、Paul、Rebecca Butler、Scott K Logan、Shane Loretz、bailaC、brian soe、cturcotte-qnx、ketatam


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rviz_ogre_vendor <https://github.com/ros2/rviz/tree/humble/rviz_ogre_vendor/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 ogre vendor 中的接口链接库问题（`#761 <https://github.com/ros2/rviz/issues/761>`__）
* 修复 Ubuntu Jammy arm64 上的构建问题（`#828 <https://github.com/ros2/rviz/issues/828>`__）
* 从已安装的 Ogre 二进制文件中移除 RPATH（`#688 <https://github.com/ros2/rviz/issues/688>`__）
* 贡献者：Chris Lalancette、Laszlo Turanyi、Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rviz_rendering <https://github.com/ros2/rviz/tree/humble/rviz_rendering/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将 getVerticesPerPoint 方法设为 public，并改进测试（`#843 <https://github.com/ros2/rviz/issues/843>`__）
* 禁用 Eigen 的 class-memaccess 警告（`#838 <https://github.com/ros2/rviz/issues/838>`__）
* 禁用包含 Eigen 时产生的警告（`#835 <https://github.com/ros2/rviz/issues/835>`__）
* 将头文件安装到 include/${PROJECT_NAME}（`#829 <https://github.com/ros2/rviz/issues/829>`__）
* 修复对 assimp 5.1.0 的支持（`#817 <https://github.com/ros2/rviz/issues/817>`__）
* 修复 cpplint 错误（`#818 <https://github.com/ros2/rviz/issues/818>`__）
* 修复与 uncrustify 0.72 的兼容问题（`#807 <https://github.com/ros2/rviz/issues/807>`__）
* 在 rviz_rendering 构建中抑制 assimp 警告（`#775 <https://github.com/ros2/rviz/issues/775>`__）
* 修复材质已存在时 ogre 失败的问题（`#729 <https://github.com/ros2/rviz/issues/729>`__）
* 修复 rviz_rendering 和 rviz_rendering_tests 中的部分内存泄漏（`#710 <https://github.com/ros2/rviz/issues/710>`__）
* 正确导出 Qt5 依赖（`#687 <https://github.com/ros2/rviz/issues/687>`__）
* 将 GLSL 1.50 资源重新放回 RenderSystem（`#668 <https://github.com/ros2/rviz/issues/668>`__）
* 贡献者：Alejandro Hernández Cordero、Chris Lalancette、Jacob Perron、Jorge Perez、Michel Hidalgo、Piotr Jaroszek、Scott K Logan、Shane Loretz、Silvio Traversaro、Wolf Vollprecht


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rviz_rendering_tests <https://github.com/ros2/rviz/tree/humble/rviz_rendering_tests/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 修复 rviz_rendering 和 rviz_rendering_tests 中的部分内存泄漏（`#710 <https://github.com/ros2/rviz/issues/710>`__）
* 贡献者：Alejandro Hernández Cordero


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`rviz_visual_testing_framework <https://github.com/ros2/rviz/tree/humble/rviz_visual_testing_framework/CHANGELOG.rst>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 将头文件安装到 include/${PROJECT_NAME}（`#829 <https://github.com/ros2/rviz/issues/829>`__）
* 修复与 uncrustify 0.72 的兼容问题（`#807 <https://github.com/ros2/rviz/issues/807>`__）
* 在 rcutils/get_env.h 弃用后更新头文件包含（`#677 <https://github.com/ros2/rviz/issues/677>`__）
