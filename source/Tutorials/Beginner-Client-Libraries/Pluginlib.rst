.. redirect-from::

    Tutorials/Pluginlib

创建和使用插件（C++）
=====================

**目标：** 学习如何使用 ``pluginlib`` 创建并加载简单插件。

**教程级别：** 初级 | **预计时间：** 20 分钟

.. contents:: 目录
   :depth: 3
   :local:

背景
----

本教程参考 ``pluginlib`` 的 ROS 1 教程。``pluginlib`` 是一个 C++ 库，用于在 ROS 功能包中加载和卸载插件。插件是可在运行时从共享库动态加载的类。使用 pluginlib 时，应用程序无需显式链接包含插件类的库；pluginlib 可以在运行时打开包含已导出类的库，而应用程序事先不必知道该库或类头文件。

前置条件
--------

需要具备基本 C++ 知识，并成功 :doc:`安装 ROS 2 <../../Installation>`。

任务
----

本教程创建两个功能包：一个定义基类，另一个提供插件。基类定义通用多边形接口，插件实现具体形状。

1. 创建基类功能包
^^^^^^^^^^^^^^^^^

在 ``ros2_ws/src`` 中创建功能包：

.. code-block:: console

   $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 --dependencies pluginlib --node-name area_node polygon_base

在 ``include/polygon_base/regular_polygon.hpp`` 中定义抽象基类：

.. code-block:: cpp

   #ifndef POLYGON_BASE_REGULAR_POLYGON_HPP
   #define POLYGON_BASE_REGULAR_POLYGON_HPP

   namespace polygon_base
   {
     class RegularPolygon
     {
     public:
       virtual void initialize(double side_length) = 0;
       virtual double area() = 0;
       virtual ~RegularPolygon() {}

     protected:
       RegularPolygon() {}
     };
   }  // namespace polygon_base

   #endif  // POLYGON_BASE_REGULAR_POLYGON_HPP

``initialize`` 用于传递初始化参数，因为 pluginlib 要求插件类提供无参数构造函数。

在 ``CMakeLists.txt`` 中上面的代码创建了名为 ``RegularPolygon`` 的抽象类。需要注意 ``initialize`` 方法：``pluginlib`` 要求插件类具有无参数构造函数，因此如果初始化时需要传入参数，就通过该方法将参数传递给对象。

将基类头文件导出为接口库，并安装头文件及导出 target：

.. code-block:: cmake

   add_library(${PROJECT_NAME} INTERFACE)
   add_library(${PROJECT_NAME}::${PROJECT_NAME} ALIAS ${PROJECT_NAME})
   target_compile_features(${PROJECT_NAME} INTERFACE c_std_99 cxx_std_17)
   target_include_directories(${PROJECT_NAME} INTERFACE
     $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
     $<INSTALL_INTERFACE:include/${PROJECT_NAME}>)
   target_link_libraries(${PROJECT_NAME} INTERFACE ${pluginlib_TARGETS})
   install(DIRECTORY include/ DESTINATION include/${PROJECT_NAME})
   install(TARGETS ${PROJECT_NAME} EXPORT export_${PROJECT_NAME})
   install(EXPORT export_${PROJECT_NAME}
     NAMESPACE ${PROJECT_NAME}::
     DESTINATION share/${PROJECT_NAME}/cmake)

在 ``ament_package()`` 之前导出 target：

.. code-block:: cmake

   ament_export_include_directories(include)
   ament_export_targets(export_${PROJECT_NAME})

2. 创建插件功能包
^^^^^^^^^^^^^^^^^

创建第二个功能包：

.. code-block:: console

   $ ros2 pkg create --build-type ament_cmake --license Apache-2.0 --dependencies polygon_base pluginlib --library-name polygon_plugins polygon_plugins

2.1 编写插件源码
~~~~~~~~~~~~~~~~

在 ``src/polygon_plugins.cpp`` 中实现正方形和三角形：

.. code-block:: cpp

   #include <polygon_base/regular_polygon.hpp>
   #include <cmath>

   namespace polygon_plugins
   {
     class Square : public polygon_base::RegularPolygon
     {
     public:
       void initialize(double side_length) override
       {
         side_length_ = side_length;
       }
       double area() override
       {
         return side_length_ * side_length_;
       }
     protected:
       double side_length_;
     };

     class Triangle : public polygon_base::RegularPolygon
     {
     public:
       void initialize(double side_length) override
       {
         side_length_ = side_length;
       }
       double area() override
       {
         return 0.5 * side_length_ * getHeight();
       }
       double getHeight()
       {
         return sqrt(side_length_ * side_length_ -
           (side_length_ / 2) * (side_length_ / 2));
       }
     protected:
       double side_length_;
     };
   }

   #include <pluginlib/class_list_macros.hpp>
   PLUGINLIB_EXPORT_CLASS(polygon_plugins::Square, polygon_base::RegularPolygon)
   PLUGINLIB_EXPORT_CLASS(polygon_plugins::Triangle, polygon_base::RegularPolygon)

``PLUGINLIB_EXPORT_CLASS`` 宏注册插件类，参数分别是插件类的完整类型和基类的完整类型。

``Square`` 和 ``Triangle`` 类的实现比较直接：保存边长，并使用边长计算面积。与 pluginlib 相关的关键部分是文件末尾的 ``PLUGINLIB_EXPORT_CLASS`` 宏，它会将类注册为插件。

该宏接收两个参数：

1. 插件类的完整类型，例如 ``polygon_plugins::Square``。
2. 基类的完整类型，例如 ``polygon_base::RegularPolygon``。

2.2 插件声明 XML
~~~~~~~~~~~~~~~~

创建 ``plugins.xml``：

.. code-block:: xml

   <library path="polygon_plugins">
     <class type="polygon_plugins::Square" base_class_type="polygon_base::RegularPolygon">
       <description>This is a square plugin.</description>
     </class>
     <class type="polygon_plugins::Triangle"
            base_class_type="polygon_base::RegularPolygon"
            name="awesome_triangle">
       <description>This is a triangle plugin.</description>
     </class>
   </library>

``library`` 指定包含插件的库路径；ROS 2 中只需填写库名称。``class`` 声明需要导出的插件，其中 ``type`` 是插件完整类型，``base_class_type`` 是基类完整类型，``description`` 是说明，``name`` 是可选的查找名称。

2.3 在 CMake 中导出插件
~~~~~~~~~~~~~~~~~~~~~~~

ROS 2 与 ROS 1 不同，插件导出在 ``CMakeLists.txt`` 中完成，而不是 ``package.xml``。在 ``find_package(pluginlib REQUIRED)`` 之后添加：

.. code-block:: cmake

   pluginlib_export_plugin_description_file(polygon_base plugins.xml)

两个参数分别是基类所在功能包和插件声明 XML 的相对路径。

3. 使用插件
^^^^^^^^^^^

现在可以使用插件。插件可以在任何功能包中加载，本教程选择在基类功能包中使用它们。

编辑 ``ros2_ws/src/polygon_base/src/area_node.cpp``，内容如下：

.. code-block:: c++

   #include <pluginlib/class_loader.hpp>
   #include <polygon_base/regular_polygon.hpp>

   int main(int argc, char ** argv)
   {
     // 避免未使用参数警告
     (void) argc;
     (void) argv;

     pluginlib::ClassLoader<polygon_base::RegularPolygon> poly_loader(
       "polygon_base", "polygon_base::RegularPolygon");

     try
     {
       std::shared_ptr<polygon_base::RegularPolygon> triangle =
         poly_loader.createSharedInstance("awesome_triangle");
       triangle->initialize(10.0);

       std::shared_ptr<polygon_base::RegularPolygon> square =
         poly_loader.createSharedInstance("polygon_plugins::Square");
       square->initialize(10.0);

       printf("Triangle area: %.2f\\n", triangle->area());
       printf("Square area: %.2f\\n", square->area());
     }
     catch (pluginlib::PluginlibException & ex)
     {
       printf("The plugin failed to load for some reason. Error: %s\\n", ex.what());
     }

     return 0;
   }

``ClassLoader`` 是理解 pluginlib 的关键类：

* 模板参数是基类类型，即 ``polygon_base::RegularPolygon``。
* 第一个构造参数是基类所在的功能包名称，即 ``polygon_base``。
* 第二个构造参数是插件基类的完整类型，即 ``polygon_base::RegularPolygon``。

本例使用共享指针创建插件实例。调用 ``createSharedInstance()`` 时，可以传入插件类的完整类型（XML 中的 ``type`` 属性，例如 ``polygon_plugins::Square``），也可以传入 XML 中可选的 ``name`` 查找名称，例如 ``awesome_triangle``。

注意：定义该节点的 ``polygon_base`` 功能包并不依赖 ``polygon_plugins``。插件会在运行时动态加载，因此无需声明对插件功能包的直接依赖。本例将插件名称写死在代码中，实际应用中也可以通过参数等方式动态选择插件。

3. 使用插件
^^^^^^^^^^^

在基类功能包的 ``src/area_node.cpp`` 中使用 ``pluginlib::ClassLoader``：

.. code-block:: cpp

   pluginlib::ClassLoader<polygon_base::RegularPolygon> poly_loader(
     "polygon_base", "polygon_base::RegularPolygon");

   auto triangle = poly_loader.createSharedInstance("awesome_triangle");
   triangle->initialize(10.0);

   auto square = poly_loader.createSharedInstance("polygon_plugins::Square");
   square->initialize(10.0);

   printf("Triangle area: %.2f\n", triangle->area());
   printf("Square area: %.2f\n", square->area());

``ClassLoader`` 的模板参数是基类类型。第一个构造参数是基类所属功能包名称，第二个参数是基类完整类型。``createSharedInstance()`` 可以使用插件完整类型，也可以使用 XML 中配置的可选查找名称。

注意，定义该节点的 ``polygon_base`` 功能包不依赖 ``polygon_plugins``。插件会在运行时动态加载，无需声明直接依赖。

4. 构建和运行
^^^^^^^^^^^^^

在工作空间根目录构建两个功能包：

.. code-block:: console

   $ colcon build --packages-select polygon_base polygon_plugins

source 工作空间环境。若未安装 ``ros2 plugin`` 命令，可安装：

.. code-block:: console

   $ sudo apt install ros-{DISTRO}-ros2plugin

列出已注册插件：

.. code-block:: console

   $ ros2 plugin list
   polygon_plugins:
      Plugin(name='polygon_plugins::Square', type='polygon_plugins::Square', base='polygon_base::RegularPolygon')
      Plugin(name='polygon_plugins::Triangle', type='polygon_plugins::Triangle', base='polygon_base::RegularPolygon')

.. code-block:: console

   $ ros2 plugin list

运行节点：

.. code-block:: console

   $ ros2 run polygon_base area_node
   Triangle area: 43.30
   Square area: 100.00

总结
----

本教程介绍了如何定义插件基类、实现插件、使用 XML 声明插件，并通过 ``pluginlib::ClassLoader`` 在运行时加载和使用插件。
