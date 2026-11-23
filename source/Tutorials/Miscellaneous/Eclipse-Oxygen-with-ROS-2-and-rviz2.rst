.. redirect-from::

    Eclipse-Oxygen-with-ROS-2-and-rviz2
    Tutorials/Eclipse-Oxygen-with-ROS-2-and-rviz2

在 Eclipse Oxygen 中使用 rviz2（社区贡献）
=========================================

.. contents:: 目录
   :depth: 1
   :local:

环境准备
--------

本教程假设已经安装 Eclipse Oxygen、Git 和 EGit 插件。

教程中将 Eclipse 工作空间命名为与 ROS 2 功能包相同的名称，但这并非强制要求。示例采用嵌套项目结构，每个 ROS 2 功能包使用一个 Eclipse 工作空间。

创建 C++ 项目
-------------

在 Eclipse 中创建 C++ Project。项目名称使用 ROS 2 功能包名称，项目类型选择 Makefile Project，并选择 Other Toolchain。

.. image:: images/eclipse-oxygen-01.png

.. image:: images/eclipse-oxygen-02.png

.. image:: images/eclipse-oxygen-03.png

完成创建后，项目应显示在 Project Explorer 中。

.. image:: images/eclipse-oxygen-04.png

在项目中创建 §src§ 目录。

导入 Git 仓库
-------------

使用 Import 功能导入 Git 仓库，填写仓库 URL。目标目录应使用前面创建的项目源码目录。

.. image:: images/eclipse-oxygen-08.png

.. image:: images/eclipse-oxygen-09.png

.. note::

   目标目录应指向之前创建项目的源码目录。如果 Eclipse 对话框无法选择目标路径，可能需要在名称字段中填写项目名称。

使用 New Project Wizard 导入仓库，并创建 General → Project。项目名称使用 Git 仓库名称，Location 选择刚才克隆仓库所在目录。

.. image:: images/eclipse-oxygen-11.png

.. image:: images/eclipse-oxygen-12.png

.. image:: images/eclipse-oxygen-13.png

Project Explorer 中会同时显示 Git 项目和新建项目。相同文件可能出现多次，但只有一个项目与 EGit 关联。

对 §pluginlib§ 和 §tinyxml2_vendor§ 仓库重复上述导入步骤。最终 Project Explorer 中应包含主项目和相关依赖项目。

项目视图
--------

Project Explorer 右上角可以将 Project Presentation 切换为 Hierarchical。该视图更接近硬盘上的 ROS 2 项目目录结构，但会失去 EGit 关联。因此，如果需要查看文件作者和代码行修改记录，建议使用 Flat Project Presentation。

配置构建命令
------------

打开项目属性中的 C/C++ Build 部分，将 Build command 设置为 §ament§。

在 Behavior 选项卡中取消选择 §clean§，并将 Build 文本框设置为 §build§。

在执行 Build project 之前，需要关闭 Eclipse。打开 Shell，source ROS 2 的 §setup.bash§，进入 Eclipse 项目目录，然后从该目录启动 Eclipse。

.. image:: images/eclipse-oxygen-23.png

完成后，代码补全、EGit 注释和 Eclipse C/C++ 工具应能够正常工作。

配置 Eclipse Indexer
-------------------

打开 rviz2 的 §main.cpp§ 时，可能会出现大量 unresolved inclusion 警告。可以在 Project → Properties → C/C++ General → Paths and Symbols 中进行配置。

在 References 选项卡中选择 §ros2_ws§。随后进入 Source locations 选项卡，使用 Link folder 添加 Qt5 include 目录。

.. image:: images/eclipse-oxygen-27.png

建议在 Source locations 中添加排除目录，避免对 Build 和 Install 等目录建立索引。

在 C/C++ General → Preprocessor includes 中选择 §CDT GCC Built in compiler settings [Shared]§，并在编译器规格命令中加入：

.. code-block:: bash

   -std=c++14

随后在 C/C++ General → Indexer 中配置索引选项，并对 rviz2 项目执行 Indexer → Rebuild。

.. image:: images/eclipse-oxygen-31.png

调试 Eclipse 项目
-----------------

在 C/C++ Build 中为构建命令添加：

.. code-block:: bash

   -DCMAKE_BUILD_TYPE=Debug

然后在 Eclipse 中打开 Run → Debug Configurations，创建调试配置并启动调试。

.. image:: images/eclipse-oxygen-34.png

总结
----

本教程介绍了如何在 Eclipse Oxygen 中导入 ROS 2 Git 仓库、配置 CMake 构建命令、设置代码索引和调试环境，以便使用 Eclipse 开发 RViz 及其他 ROS 2 C++ 项目。
