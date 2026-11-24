构建自定义 RViz Display
=======================

背景
----

RViz 已经支持多种数据类型的可视化。但如果某种消息类型尚无对应显示插件，可以选择：

1. 将消息转换为其他类型，例如 ``visualization_msgs/Marker``。
2. 编写自定义 RViz Display。

第一种方式实现简单且灵活，但会增加网络流量，并限制数据表达能力。第二种方式需要更多开发工作，但能够提供更丰富的可视化效果。

本教程代码位于 ``rviz_plugin_tutorial`` 仓库中。仓库提供 ``step2``、``step3`` 等分支，便于逐步查看插件实现过程。

Point2D 消息
------------

本教程使用 ``rviz_plugin_tutorial_msgs`` 功能包中的示例消息 ``Point2D.msg``：

.. code-block:: text

   std_msgs/Header header
   float64 x
   float64 y

基础插件框架
------------

首先创建插件头文件 ``point_display.hpp``：

.. code-block:: cpp

   #ifndef RVIZ_PLUGIN_TUTORIAL__POINT_DISPLAY_HPP_
   #define RVIZ_PLUGIN_TUTORIAL__POINT_DISPLAY_HPP_

   #include <rviz_common/message_filter_display.hpp>
   #include <rviz_plugin_tutorial_msgs/msg/point2_d.hpp>

   namespace rviz_plugin_tutorial
   {
   class PointDisplay :
     public rviz_common::MessageFilterDisplay<
       rviz_plugin_tutorial_msgs::msg::Point2D>
   {
     Q_OBJECT
   protected:
     void processMessage(
       const rviz_plugin_tutorial_msgs::msg::Point2D::ConstSharedPtr msg)
       override;
   };
   }
   #endif

该类继承自 ``rviz_common::MessageFilterDisplay``，适用于包含 ``std_msgs/Header`` 的消息。RViz 会负责订阅消息并处理坐标变换，插件只需实现 ``processMessage()``，将消息内容转换为可视化对象。

实现显示逻辑
------------

在 ``processMessage()`` 中读取消息的 x、y 值，并使用 RViz 的渲染接口创建或更新可视化对象。插件需要正确处理消息坐标系和时间戳，以确保显示位置与 TF 变换一致。

插件导出
--------

自定义 Display 需要使用 pluginlib 导出类，并在插件描述文件中声明插件类型和基类。随后在 CMake 中安装插件描述文件并导出插件信息，使 RViz 能够发现和加载该显示插件。

总结
----

当 RViz 没有现成的消息显示插件时，可以通过继承 ``MessageFilterDisplay`` 创建自定义 Display。插件处理消息内容并创建渲染对象，从而扩展 RViz 的可视化能力。
