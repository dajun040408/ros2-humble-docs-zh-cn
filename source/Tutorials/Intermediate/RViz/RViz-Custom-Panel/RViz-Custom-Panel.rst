构建自定义 RViz 面板
====================

本教程适用于希望在 RViz 环境中显示数据，或在二维界面中与数据交互的开发者。

本教程将介绍如何在 RViz 中完成三项工作：

* 在 RViz 中创建新的 Qt 面板。
* 在 RViz 面板中创建话题订阅者，监控话题消息并在面板中显示内容。
* 创建话题发布者，使 RViz 面板中的按钮操作能够向 ROS 话题发布消息。

本教程所有代码都可以在 `rviz_panel_tutorial 仓库 <https://github.com/MetroRobots/rviz_panel_tutorial>`_ 中找到。

基础代码
--------

头文件
^^^^^^

``demo_panel.hpp`` 内容如下：

.. code-block:: c++

   #ifndef RVIZ_PANEL_TUTORIAL__DEMO_PANEL_HPP_
   #define RVIZ_PANEL_TUTORIAL__DEMO_PANEL_HPP_

   #include <rviz_common/panel.hpp>

   namespace rviz_panel_tutorial
   {
   class DemoPanel
     : public rviz_common::Panel
   {
     Q_OBJECT
   public:
     explicit DemoPanel(QWidget * parent = 0);
     ~DemoPanel() override;
   };
   }  // namespace rviz_panel_tutorial

   #endif  // RVIZ_PANEL_TUTORIAL__DEMO_PANEL_HPP_

* 该类继承自 `rviz_common::Panel <https://github.com/ros2/rviz/blob/9a94bdf2f5f92ccdac4037c9268b95940845d609/rviz_common/include/rviz_common/panel.hpp#L46>`_。
* 由于 Qt 元对象系统的要求，需要添加 ``Q_OBJECT`` 宏，才能使 Qt GUI 相关功能正常工作。更多信息可参阅 `Qt 元对象系统说明 <https://doc.qt.io/qt-5/moc.html>`_。
* 首先只声明构造函数和析构函数，具体实现放在 cpp 文件中。

源文件
^^^^^^

``demo_panel.cpp``：

.. code-block:: c++

   #include <rviz_panel_tutorial/demo_panel.hpp>

   namespace rviz_panel_tutorial
   {
   DemoPanel::DemoPanel(QWidget* parent) : Panel(parent)
   {
   }

   DemoPanel::~DemoPanel() = default;
   }  // namespace rviz_panel_tutorial

   #include <pluginlib/class_list_macros.hpp>
   PLUGINLIB_EXPORT_CLASS(rviz_panel_tutorial::DemoPanel, rviz_common::Panel)

* 构造函数和析构函数并非必须重写，但后续可以在其中完成更多工作。
* 为了让 RViz 找到插件，需要在代码中使用 ``PLUGINLIB_EXPORT_CLASS`` 注册插件类，此外还需要完成后续的插件描述和构建配置。

package.xml
^^^^^^^^^^^

在 ``package.xml`` 中添加以下依赖：

.. code-block:: xml

   <depend>pluginlib</depend>
   <depend>rviz_common</depend>

rviz_common_plugins.xml
^^^^^^^^^^^^^^^^^^^^^^

创建 ``rviz_common_plugins.xml``：

.. code-block:: xml

   <library path="demo_panel">
     <class type="rviz_panel_tutorial::DemoPanel" base_class_type="rviz_common::Panel">
       <description></description>
     </class>
   </library>

这是标准的 ``pluginlib`` 配置：

* ``library`` 的 ``path`` 是稍后在 CMake 中指定的库名称。
* ``class`` 的类型必须与前面源代码中的 ``PLUGINLIB_EXPORT_CLASS`` 注册信息一致。
* 插件描述稍后还会补充。

CMakeLists.txt
^^^^^^^^^^^^^^

在标准 CMake 模板代码的顶部添加以下内容：

.. code-block:: cmake

   find_package(ament_cmake_ros REQUIRED)
   find_package(pluginlib REQUIRED)
   find_package(rviz_common REQUIRED)

   set(CMAKE_AUTOMOC ON)
   qt5_wrap_cpp(MOC_FILES
     include/rviz_panel_tutorial/demo_panel.hpp
   )

   add_library(demo_panel src/demo_panel.cpp ${MOC_FILES})
   target_include_directories(demo_panel PUBLIC
     $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
     $<INSTALL_INTERFACE:include>
   )
   ament_target_dependencies(demo_panel
     pluginlib
     rviz_common
   )
   install(TARGETS demo_panel
           EXPORT export_rviz_panel_tutorial
           ARCHIVE DESTINATION lib
           LIBRARY DESTINATION lib
           RUNTIME DESTINATION bin
   )
   install(DIRECTORY include/
           DESTINATION include
   )
   install(FILES rviz_common_plugins.xml
           DESTINATION share/${PROJECT_NAME}
   )
   ament_export_include_directories(include)
   ament_export_targets(export_rviz_panel_tutorial)
   pluginlib_export_plugin_description_file(rviz_common rviz_common_plugins.xml)

其中，Qt 相关配置用于生成正确的 Qt 元对象代码：

* 打开 ``CMAKE_AUTOMOC``。
* 调用 ``qt5_wrap_cpp``，并传入每个包含 ``Q_OBJECT`` 的头文件。
* 将生成的 ``MOC_FILES`` 与其他 cpp 文件一起加入库目标。

其他代码主要用于配置插件的构建和导出。特别是 ``pluginlib_export_plugin_description_file``，它是让 RViz 找到新插件的关键步骤。

测试基础面板
^^^^^^^^^^^^

编译代码、source 工作空间，然后运行 ``rviz2``。

在顶部菜单栏中，应该可以看到 ``Panels`` 菜单。选择其中的 ``Add New Panel``：

.. image:: images/Select0.png
   :target: ../../../../_images/Select0.png
   :alt: 添加新面板对话框截图

弹出的对话框会显示 ROS 环境中所有可用的面板，并按照所属 ROS 功能包分组。

可以双击面板名称，或者选中面板后点击 OK，创建一个新的面板实例。

此时 RViz 窗口中应该会出现新面板，但除了显示面板标题栏外，还没有其他内容：

.. image:: images/RViz0.png
   :target: ../../../../_images/RViz0.png
   :alt: RViz 中显示新建的空面板

完善面板功能
------------

现在为面板添加最基本的 ROS/Qt 交互功能。

大致实现方式是：从 RViz 内部获取 ROS 节点，通过该节点订阅和发布 ROS 话题。

订阅者监听 ROS 中的 ``/input`` 话题，并将发布的 ``String`` 消息显示在面板控件中。发布者则将 RViz 中的按钮操作转换为消息，并发布到 ROS 的 ``/output`` 话题。

更新头文件
^^^^^^^^^^

将 ``demo_panel.hpp`` 更新为以下内容：

.. code-block:: c++

   #include <rviz_common/panel.hpp>
   #include <rviz_common/ros_integration/ros_node_abstraction_iface.hpp>
   #include <std_msgs/msg/string.hpp>
   #include <QLabel>
   #include <QPushButton>

   namespace rviz_panel_tutorial
   {
   class DemoPanel : public rviz_common::Panel
   {
     Q_OBJECT
   public:
     explicit DemoPanel(QWidget * parent = 0);
     ~DemoPanel() override;

     void onInitialize() override;

   protected:
     std::shared_ptr<rviz_common::ros_integration::RosNodeAbstractionIface> node_ptr_;
     rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
     rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;

     void topicCallback(const std_msgs::msg::String & msg);

     QLabel* label_;
     QPushButton* button_;

   private Q_SLOTS:
     void buttonActivated();
   };
   }  // namespace rviz_panel_tutorial

ROS 相关部分：

* 声明一个抽象 ROS 节点指针，后续使用它创建与 ROS 生态系统交互的接口。
* 订阅者用于从 ROS 接收数据，并在 RViz 中显示。
* 发布者用于从 RViz 内部发布数据或事件，使其能够被 ROS 中的其他节点使用。
* ``onInitialize`` 用于初始化 ROS 组件，``topicCallback`` 是订阅者回调函数。

Qt 相关部分：

* 声明一个标签控件 ``QLabel`` 和一个按钮控件 ``QPushButton``。
* 声明按钮回调函数 ``buttonActivated``。

更新源文件
^^^^^^^^^^

将 ``demo_panel.cpp`` 更新为以下内容：

.. code-block:: c++

   #include <rviz_panel_tutorial/demo_panel.hpp>
   #include <QVBoxLayout>
   #include <rviz_common/display_context.hpp>

   namespace rviz_panel_tutorial
   {

   DemoPanel::DemoPanel(QWidget* parent) : Panel(parent)
   {
     // 创建垂直布局（VBox 中的 V 表示 Vertical，即垂直）
     const auto layout = new QVBoxLayout(this);

     // 创建按钮和标签
     label_ = new QLabel("[no data]");
     button_ = new QPushButton("GO!");

     // 将控件添加到界面布局中
     layout->addWidget(label_);
     layout->addWidget(button_);

     // 将按钮释放事件连接到回调函数
     // 按下并释放按钮后，会调用 buttonActivated
     QObject::connect(
       button_, &QPushButton::released,
       this, &DemoPanel::buttonActivated);
   }

   DemoPanel::~DemoPanel() = default;

   void DemoPanel::onInitialize()
   {
     // 从 RViz 获取抽象 ROS 节点，并锁定该节点以供当前操作使用
     node_ptr_ = getDisplayContext()->getRosNodeAbstraction().lock();

     // 获取常用的 rclcpp::Node 指针，以便创建订阅者和发布者
     rclcpp::Node::SharedPtr node = node_ptr_->get_raw_node();

     // 创建 String 发布者，发布到 /output
     publisher_ = node->create_publisher<std_msgs::msg::String>("/output", 10);

     // 创建 String 订阅者，并绑定本类中的 topicCallback
     subscription_ = node->create_subscription<std_msgs::msg::String>(
       "/input", 10,
       std::bind(&DemoPanel::topicCallback, this, std::placeholders::_1));
   }

   // 收到订阅消息时调用该回调，将消息内容更新到界面标签
   void DemoPanel::topicCallback(const std_msgs::msg::String & msg)
   {
     label_->setText(QString(msg.data.c_str()));
   }

   // 用户按下按钮时调用该回调，并向 ROS 话题发布新消息
   void DemoPanel::buttonActivated()
   {
     auto message = std_msgs::msg::String();
     message.data = "Button clicked!";
     publisher_->publish(message);
   }

   }  // namespace rviz_panel_tutorial

   #include <pluginlib/class_list_macros.hpp>

   PLUGINLIB_EXPORT_CLASS(rviz_panel_tutorial::DemoPanel, rviz_common::Panel)

使用 ROS 测试面板
^^^^^^^^^^^^^^^^

重新编译代码，并再次启动 RViz2。

现在应该能看到面板中已经包含标签和按钮：

.. image:: images/RViz1.png
   :target: ../../../../_images/RViz1.png
   :alt: RViz 面板的默认状态

要修改标签内容，只需向 ``/input`` 话题发布一条消息。例如：

.. code-block:: console

   $ ros2 topic pub /input std_msgs/msg/String "{data: 'Please be kind.'}"

由于面板订阅了该话题，因此收到消息后会触发回调函数，并更新标签文本。

.. image:: images/RViz2.png
   :target: ../../../../_images/RViz2.png
   :alt: 显示自定义字符串消息的 RViz 面板

按下按钮后，面板会发布一条消息。可以通过 echo ``/output`` 话题查看：

.. code-block:: console

   $ ros2 topic echo /output

清理和完善
----------

现在可以进一步完善面板外观和使用体验。以下修改不是插件运行的必要条件，但可以让界面更加美观，也更容易使用。

首先，更新 ``rviz_common_plugins.xml`` 中插件的描述信息。

然后为插件添加图标，文件路径为 ``icons/classes/DemoPanel.png``。该目录是固定的，图标文件名应与插件声明中的名称一致；如果没有单独指定名称，则应与类名一致。

还需要在 CMake 中安装图像文件：

.. code-block:: cmake

   install(FILES icons/classes/DemoPanel.png
           DESTINATION share/${PROJECT_NAME}/icons/classes
   )

现在添加面板时，应该会同时显示图标和描述：

.. image:: images/Select1.png
   :target: ../../../../_images/Select1.png
   :alt: 带有自定义图标和描述的添加面板对话框

面板本身也会显示更新后的图标：

.. image:: images/RViz3.png
   :target: ../../../../_images/RViz3.png
   :alt: 带有自定义图标的 RViz 面板
