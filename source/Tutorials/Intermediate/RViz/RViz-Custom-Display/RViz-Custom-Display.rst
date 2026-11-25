构建自定义 RViz Display
=======================

背景
----

RViz 已经支持多种数据类型的可视化。但如果某种消息类型尚无对应的显示插件，可以选择两种方式在 RViz 中查看数据：

1. 将消息转换为其他类型，例如 ``visualization_msgs/msg/Marker``。
2. 编写自定义 RViz Display。

第一种方式实现快速且灵活，但会增加网络流量，并限制数据的表达能力。第二种方式需要更多开发工作，但能够提供更加丰富的可视化效果。本教程将介绍第二种方式。

本教程所有代码都可以在 `rviz_plugin_tutorial 仓库 <https://github.com/MetroRobots/rviz_plugin_tutorial>`_ 中找到。为了展示插件开发的渐进过程，该仓库提供了 ``step2``、``step3`` 等分支，每个分支都可以单独编译和运行。

Point2D 消息
------------

本教程将使用 ``rviz_plugin_tutorial_msgs`` 功能包中的示例消息 ``Point2D.msg``：

.. code-block:: text

   std_msgs/Header header
   float64 x
   float64 y

基础插件框架
------------

先准备基础插件代码。完整的第一阶段代码可以在仓库的 ``step1`` 分支中查看。

头文件
^^^^^^

``point_display.hpp`` 内容如下：

.. code-block:: c++

   #ifndef RVIZ_PLUGIN_TUTORIAL__POINT_DISPLAY_HPP_
   #define RVIZ_PLUGIN_TUTORIAL__POINT_DISPLAY_HPP_

   #include <rviz_common/message_filter_display.hpp>
   #include <rviz_plugin_tutorial_msgs/msg/point2_d.hpp>

   namespace rviz_plugin_tutorial
   {
   class PointDisplay
     : public rviz_common::MessageFilterDisplay<rviz_plugin_tutorial_msgs::msg::Point2D>
   {
     Q_OBJECT

   protected:
     void processMessage(
       const rviz_plugin_tutorial_msgs::msg::Point2D::ConstSharedPtr msg) override;
   };
   }  // namespace rviz_plugin_tutorial

   #endif  // RVIZ_PLUGIN_TUTORIAL__POINT_DISPLAY_HPP_

需要注意：

* 这里继承的是 `MessageFilterDisplay <https://github.com/ros2/rviz/blob/0ef2b56373b98b5536f0f817c11dc2b5549f391d/rviz_common/include/rviz_common/message_filter_display.hpp#L43>`_ 类。它可以用于任何包含 ``std_msgs/Header`` 的消息类型。
* 该类模板使用本教程定义的 ``Point2D`` 消息类型。
* 由于 Qt 元对象系统的要求，需要添加 ``Q_OBJECT`` 宏，才能使 Qt GUI 相关功能正常工作。更多信息可参阅 `Qt 元对象系统说明 <https://doc.qt.io/qt-5/moc.html>`_。
* 只需要实现 ``processMessage()`` 方法，具体实现放在 cpp 文件中。

源文件
^^^^^^

``point_display.cpp``：

.. code-block:: c++

   #include <rviz_plugin_tutorial/point_display.hpp>
   #include <rviz_common/logging.hpp>

   namespace rviz_plugin_tutorial
   {
   void PointDisplay::processMessage(
     const rviz_plugin_tutorial_msgs::msg::Point2D::ConstSharedPtr msg)
   {
     RVIZ_COMMON_LOG_INFO_STREAM(
       "We got a message with frame " << msg->header.frame_id);
   }
   }  // namespace rviz_plugin_tutorial

   #include <pluginlib/class_list_macros.hpp>
   PLUGINLIB_EXPORT_CLASS(rviz_plugin_tutorial::PointDisplay, rviz_common::Display)

需要注意：

* 日志输出不是必须的，但有助于调试。
* 为了让 RViz 找到插件，需要在代码中使用 ``PLUGINLIB_EXPORT_CLASS`` 注册插件类，此外还需要完成后续的插件描述和构建配置。

package.xml
^^^^^^^^^^^

在 ``package.xml`` 中添加以下三个依赖：

.. code-block:: xml

   <depend>pluginlib</depend>
   <depend>rviz_common</depend>
   <depend>rviz_plugin_tutorial_msgs</depend>

rviz_common_plugins.xml
^^^^^^^^^^^^^^^^^^^^^^

创建插件描述文件 ``rviz_common_plugins.xml``：

.. code-block:: xml

   <library path="point_display">
     <class type="rviz_plugin_tutorial::PointDisplay" base_class_type="rviz_common::Display">
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
   find_package(rviz_plugin_tutorial_msgs REQUIRED)

   set(CMAKE_AUTOMOC ON)
   qt5_wrap_cpp(MOC_FILES
     include/rviz_plugin_tutorial/point_display.hpp
   )

   add_library(point_display src/point_display.cpp ${MOC_FILES})
   target_include_directories(point_display PUBLIC
     $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
     $<INSTALL_INTERFACE:include>
   )
   ament_target_dependencies(point_display
     pluginlib
     rviz_common
     rviz_plugin_tutorial_msgs
   )
   install(TARGETS point_display
           EXPORT export_rviz_plugin_tutorial
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
   ament_export_targets(export_rviz_plugin_tutorial)
   pluginlib_export_plugin_description_file(rviz_common rviz_common_plugins.xml)

为了生成正确的 Qt 文件，需要：

* 打开 ``CMAKE_AUTOMOC``。
* 调用 ``qt5_wrap_cpp``，并传入每个包含 ``Q_OBJECT`` 的头文件。
* 将生成的 ``MOC_FILES`` 与其他 cpp 文件一起加入库目标。

如果没有对头文件进行包装，在运行时加载插件时可能会出现错误，例如：

.. code-block:: text

   [rviz2]: PluginlibFactory: The plugin for class 'rviz_plugin_tutorial::PointDisplay' failed to load.
   Error: Failed to load library .../libpoint_display.so.
   undefined symbol: _ZTVN20rviz_plugin_tutorial12PointDisplayE

其他代码主要用于配置插件的构建和导出。特别是 ``pluginlib_export_plugin_description_file``，它是让 RViz 找到新插件的关键步骤。

测试插件
^^^^^^^^

编译代码、source 工作空间，然后运行 ``rviz2``。

点击左下角的 ``Add`` 按钮，选择你的功能包和插件，即可添加新显示插件。

.. image:: images/Step1A.png
   :target: ../../../../_images/Step1A.png
   :alt: 添加 Display 的截图

最初，Display 会处于错误状态，因为还没有为它指定话题。

.. image:: images/Step1B.png
   :target: ../../../../_images/Step1B.png
   :alt: Display 错误状态截图

如果将话题设置为 ``/point``，错误状态应该会消失，但目前仍然不会显示任何内容。

.. image:: images/Step1C.png
   :target: ../../../../_images/Step1C.png
   :alt: 正常运行但尚无可视化内容的 Display

可以使用以下命令发布消息：

.. code-block:: console

   $ ros2 topic pub /point rviz_plugin_tutorial_msgs/msg/Point2D "{header: {frame_id: map}, x: 1, y: 2}" -r 0.5

此时，RViz 的标准输出（stdout）中应该会出现 ``We got a message`` 日志。

实际可视化
----------

第二阶段的完整代码可以在仓库的 ``step2`` 分支中查看。

首先，需要在 ``CMakeLists.txt`` 和 ``package.xml`` 中添加对 ``rviz_rendering`` 功能包的依赖。

然后在头文件中增加三项内容：

* 添加 ``#include <rviz_rendering/objects/shape.hpp>``。``rviz_rendering`` 功能包中提供了 `多种可视化对象 <https://github.com/ros2/rviz/tree/ros2/rviz_rendering/include/rviz_rendering/objects>`_，本例使用简单的形状对象。
* 在类中添加新的受保护虚函数声明：``void onInitialize() override;``。
* 添加形状对象指针：``std::unique_ptr<rviz_rendering::Shape> point_shape_;``。

随后在 cpp 文件中定义 ``onInitialize`` 方法：

.. code-block:: c++

   void PointDisplay::onInitialize()
   {
     MFDClass::onInitialize();
     point_shape_ =
       std::make_unique<rviz_rendering::Shape>(
         rviz_rendering::Shape::Type::Cube,
         scene_manager_,
         scene_node_);
   }

需要注意：

* ``MFDClass`` 是 `模板父类的类型别名 <https://github.com/ros2/rviz/blob/0ef2b56373b98b5536f0f817c11dc2b5549f391d/rviz_common/include/rviz_common/message_filter_display.hpp#L57>`_，用于简化代码。
* 形状对象必须在 ``onInitialize`` 方法中创建，而不是在构造函数中创建。因为只有到 ``onInitialize`` 执行时，``scene_manager_`` 和 ``scene_node_`` 才准备就绪。

接下来更新 ``processMessage`` 方法：

.. code-block:: c++

   void PointDisplay::processMessage(
     const rviz_plugin_tutorial_msgs::msg::Point2D::ConstSharedPtr msg)
   {
     RVIZ_COMMON_LOG_INFO_STREAM(
       "We got a message with frame " << msg->header.frame_id);

     Ogre::Vector3 position;
     Ogre::Quaternion orientation;

     if (!context_->getFrameManager()->getTransform(
       msg->header, position, orientation))
     {
       RVIZ_COMMON_LOG_DEBUG_STREAM(
         "Error transforming from frame '" << msg->header.frame_id <<
         "' to frame '" << qPrintable(fixed_frame_) << "'");
     }

     scene_node_->setPosition(position);
     scene_node_->setOrientation(orientation);

     Ogre::Vector3 point_pos;
     point_pos.x = msg->x;
     point_pos.y = msg->y;
     point_shape_->setPosition(point_pos);
   }

这里需要完成两项工作：

* 获取消息对应的坐标变换，并据此设置 ``scene_node_``。这样可视化对象就不会始终相对于固定坐标系显示。
* 最后几行代码实现了真正的可视化：将形状对象的位置设置为消息中的点坐标。

最终效果应类似下图：

.. image:: images/Step2A.png
   :target: ../../../../_images/Step2A.png
   :alt: 正常显示点的 Display 截图

如果方块没有出现在预期位置，可能是以下原因：

* 当前没有发布该话题。
* 最近 2 秒内没有发布消息。
* 没有在 RViz 中正确设置话题。

为可视化添加选项
----------------

如果希望允许用户自定义可视化的不同属性，需要添加 `rviz_common::Property 对象 <https://github.com/ros2/rviz/tree/ros2/rviz_common/include/rviz_common/properties>`_。

第三阶段的完整代码可以在仓库的 ``step3`` 分支中查看。

更新头文件
^^^^^^^^^^

首先包含颜色属性头文件：``#include <rviz_common/properties/color_property.hpp>``。颜色只是可配置属性中的一种。

然后添加 ``updateStyle`` 声明。用户通过 Qt 的 SIGNAL/SLOT 机制修改 GUI 属性时，会调用该函数：

.. code-block:: c++

   private Q_SLOTS:
     void updateStyle();

再添加一个属性对象指针，用于保存颜色属性：

.. code-block:: c++

   std::unique_ptr<rviz_common::properties::ColorProperty> color_property_;

更新源文件
^^^^^^^^^^

首先添加头文件 ``#include <rviz_common/properties/parse_color.hpp>``，其中包含将属性颜色转换为 OGRE 颜色的辅助函数。

在 ``onInitialize`` 中添加：

.. code-block:: c++

   color_property_ = std::make_unique<rviz_common::properties::ColorProperty>(
     "Point Color",
     QColor(36, 64, 142),
     "Color to draw the point.",
     this,
     SLOT(updateStyle()));
   updateStyle();

这里创建颜色属性对象，并设置属性名称、默认值、描述和回调函数。

直接调用一次 ``updateStyle``，可以确保在用户修改属性之前，形状也已经设置了初始颜色。

接下来定义回调函数：

.. code-block:: c++

   void PointDisplay::updateStyle()
   {
     Ogre::ColourValue color =
       rviz_common::properties::qtToOgre(color_property_->getColor());
     point_shape_->setColor(color);
   }

最终效果如下：

.. image:: images/Step3A.png
   :target: ../../../../_images/Step3A.png
   :alt: 带有颜色属性的 Display

可以看到，颜色现在可以修改为粉色：

.. image:: images/Step3B.png
   :target: ../../../../_images/Step3B.png
   :alt: 修改颜色后的 Display

状态报告
--------

第四阶段的完整代码可以在仓库的 ``step4`` 分支中查看。

还可以设置 Display 的状态。作为一个示例，当 x 坐标为负数时，让 Display 显示警告状态：

在 ``processMessage`` 中添加：

.. code-block:: c++

   if (msg->x < 0) {
     setStatus(
       StatusProperty::Warn,
       "Message",
       "I will complain about points with negative x values.");
   } else {
     setStatus(StatusProperty::Ok, "Message", "OK");
   }

这里假设已经声明：

.. code-block:: cpp

   using rviz_common::properties::StatusProperty;

可以将状态理解为一组键值对：键是一个字符串（本例使用 ``"Message"``），值包含状态级别（Error、Warn 或 OK）以及描述信息。

.. image:: images/Step4A.png
   :target: ../../../../_images/Step4A.png
   :alt: 正常状态截图

.. image:: images/Step4B.png
   :target: ../../../../_images/Step4B.png
   :alt: 警告状态截图

清理和完善
----------

现在可以进一步完善插件外观。第四阶段的完整代码可以在仓库的 ``step5`` 分支中查看。

首先更新插件声明文件 ``rviz_common_plugins.xml``：

.. code-block:: xml

   <library path="point_display">
     <class name="Point2D" type="rviz_plugin_tutorial::PointDisplay" base_class_type="rviz_common::Display">
       <description>Tutorial to display a point</description>
       <message_type>rviz_plugin_tutorial_msgs/msg/Point2D</message_type>
     </class>
   </library>

需要注意：

* 在 ``class`` 标签中添加 ``name`` 字段，可以修改 RViz 中显示的插件名称。代码中使用 ``PointDisplay`` 作为类名没有问题，但在 RViz 中可以使用更简洁的名称。
* 为插件填写实际描述，不要留空。
* 声明具体的消息类型后，当用户通过话题添加 Display 时，RViz 就可以根据话题类型推荐该插件。

接下来为插件添加图标，文件路径为 ``icons/classes/Point2D.png``。该目录是固定的，图标文件名应与插件声明中的名称一致；如果没有单独指定名称，则应与类名一致。

图标来源：`Free software icon <https://commons.wikimedia.org/wiki/File:Free_software_icon.svg>`_。

需要在 CMake 中安装图像文件：

.. code-block:: cmake

   install(FILES icons/classes/Point2D.png
           DESTINATION share/${PROJECT_NAME}/icons/classes
   )

现在添加 Display 时，应该会同时显示图标和描述：

.. image:: images/Step5A.png
   :target: ../../../../_images/Step5A.png
   :alt: 带有自定义图标和描述的 Display 添加对话框

通过话题添加 Display 时，也会显示相应插件：

.. image:: images/Step5B.png
   :target: ../../../../_images/Step5B.png
   :alt: 通过话题添加 Display 的对话框

最后，这是插件在标准界面中显示的图标：

.. image:: images/Step5C.png
   :target: ../../../../_images/Step5C.png
   :alt: 标准界面中的插件图标

注意：如果修改插件名称，以前保存的 RViz 配置将不再能够正常使用该插件。
