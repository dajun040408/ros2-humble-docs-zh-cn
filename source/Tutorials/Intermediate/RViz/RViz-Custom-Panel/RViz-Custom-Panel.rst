构建自定义 RViz 面板
====================

本教程适用于希望在 RViz 环境中显示数据，或在二维界面中与数据交互的开发者。

本教程将介绍如何在 RViz 中完成三项工作：

* 创建新的 Qt 面板。
* 在 RViz 面板中创建话题订阅者，监控话题消息并显示内容。
* 创建话题发布者，使 RViz 面板中的按钮操作能够向 ROS 话题发布消息。

本教程所有代码都可以在 §rviz_panel_tutorial§ 仓库中找到。

基础代码
--------

头文件
^^^^^^

§demo_panel.hpp§ 内容如下：

.. code-block:: cpp

   #ifndef RVIZ_PANEL_TUTORIAL__DEMO_PANEL_HPP_
   #define RVIZ_PANEL_TUTORIAL__DEMO_PANEL_HPP_

   #include <rviz_common/panel.hpp>

   namespace rviz_panel_tutorial
   {
   class DemoPanel : public rviz_common::Panel
   {
     Q_OBJECT
   public:
     explicit DemoPanel(QWidget * parent = 0);
     ~DemoPanel() override;
   };
   }
   #endif

该类继承自 §rviz_common::Panel§。由于 Qt 元对象系统的要求，需要添加 §Q_OBJECT§ 宏。这里先声明构造函数和析构函数，具体实现放在 cpp 文件中。

源文件
^^^^^^

§demo_panel.cpp§：

.. code-block:: cpp

   #include <rviz_panel_tutorial/demo_panel.hpp>

   namespace rviz_panel_tutorial
   {
   DemoPanel::DemoPanel(QWidget* parent) : Panel(parent)
   {
   }

   DemoPanel::~DemoPanel() = default;
   }

   #include <pluginlib/class_list_macros.hpp>
   PLUGINLIB_EXPORT_CLASS(rviz_panel_tutorial::DemoPanel, rviz_common::Panel)

构造函数和析构函数并非必须重写，但后续可以在构造函数中创建 UI 控件和 ROS 通信实体。为了让 RViz 找到插件，需要使用 §PLUGINLIB_EXPORT_CLASS§ 注册面板类。

添加订阅者和发布者
------------------

自定义面板可以通过 ROS 节点接口创建订阅者和发布者。订阅者回调可将收到的数据更新到 Qt 控件；按钮回调则可通过发布者向 ROS 话题发送消息。

Qt 与 ROS 回调需要正确管理线程边界。若从非 GUI 线程更新 Qt 控件，应通过 Qt 信号/槽或其他线程安全机制切换到 GUI 线程。

插件导出
--------

除了在源代码中使用插件注册宏，还需要在插件描述 XML 和 CMake 配置中导出插件，使 RViz 能够发现并加载面板。

总结
----

自定义 RViz Panel 可以将 Qt 用户界面与 ROS 2 话题通信结合起来，实现数据显示和交互控制。
