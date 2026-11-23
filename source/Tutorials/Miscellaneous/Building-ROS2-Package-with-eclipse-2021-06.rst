.. redirect-from::

    Tutorials/Building-ROS2-Package-with-eclipse-2021-06

使用 Eclipse 2021-06 构建功能包
===============================

.. contents:: 目录
   :depth: 2
   :local:

你不能直接使用 Eclipse 创建 ROS 2 功能包，需要先通过命令行工具创建。请按照 :doc:`创建功能包 <../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package>` 教程操作。

创建项目后，可以使用 Eclipse 编辑源代码并进行构建。

启动 Eclipse，并选择一个 Eclipse 工作空间。

.. image:: images/eclipse_work_dir.png
   :target: ../../_images/eclipse_work_dir.png
   :alt: Eclipse 工作目录

创建一个 C++ 项目。

.. image:: images/eclipse_create_c++_project.png
   :target: ../../_images/eclipse_create_c++_project.png
   :alt: 创建 C++ 项目

.. image:: images/eclipse_c++_project_select_type.png
   :target: ../../_images/eclipse_c++_project_select_type.png
   :alt: 选择 C++ 项目类型

此时可以看到 C++ include 路径。

.. image:: images/eclipse_c++_project_includes.png
   :target: ../../_images/eclipse_c++_project_includes.png
   :alt: C++ include 路径

现在导入 ROS 2 项目。代码仍然保留在原来的位置。

.. image:: images/eclipse_import_project.png
   :target: ../../_images/eclipse_import_project.png
   :alt: 导入项目

.. image:: images/eclipse_import_filesystem.png
   :target: ../../_images/eclipse_import_filesystem.png
   :alt: 从文件系统导入

.. image:: images/eclipse_import_select_my_package.png
   :target: ../../_images/eclipse_import_select_my_package.png
   :alt: 选择功能包

在源代码中可以看到，C++ include 已经解析成功，但 ROS 2 的 include 尚未解析。

.. image:: images/eclipse_c++_wo_ros_includes.png
   :target: ../../_images/eclipse_c++_wo_ros_includes.png
   :alt: 尚未解析 ROS 2 include

.. image:: images/eclipse_c++_path_and_symbols.png
   :target: ../../_images/eclipse_c++_path_and_symbols.png
   :alt: C++ 路径和符号设置

.. image:: images/eclipse_c++_add_directory_path.png
   :target: ../../_images/eclipse_c++_add_directory_path.png
   :alt: 添加目录路径

完成设置后，ROS 2 的 include 也可以正确解析。

.. image:: images/eclipse_c++_indexer_ok.png
   :target: ../../_images/eclipse_c++_indexer_ok.png
   :alt: Eclipse 索引器正常

接下来添加 colcon Builder，这样就可以通过右键项目并选择“Build project”进行构建。

.. image:: images/eclipse_c++_properties_builders.png
   :target: ../../_images/eclipse_c++_properties_builders.png
   :alt: Eclipse 构建器属性

.. image:: images/eclipse_c++_builder_main.png
   :target: ../../_images/eclipse_c++_builder_main.png
   :alt: Eclipse Builder 主界面

通过设置 PYTHONPATH，也可以构建 Python 项目。

.. image:: images/eclipse_c++_builder_env.png
   :target: ../../_images/eclipse_c++_builder_env.png
   :alt: Eclipse Builder 环境变量

.. image:: images/eclipse_c++_properties_builders_with_colcon.png
   :target: ../../_images/eclipse_c++_properties_builders_with_colcon.png
   :alt: 配置 colcon Builder

右键项目并选择“Build Project”。

.. image:: images/eclipse_c++_build_project_with_colcon.png
   :target: ../../_images/eclipse_c++_build_project_with_colcon.png
   :alt: 使用 colcon 构建项目
