使用 ROS 2 软件包变体
======================

元功能包（metapackage）本身不直接提供软件，而是依赖一组相关软件包，从而为整组软件包提供方便的安装方式。``注 1`` ``注 2``

变体（variant）是 ROS 官方提供的元功能包列表，用于定义常见且实用的软件包组合。

.. [注 1] https://wiki.debian.org/metapackage
.. [注 2] https://help.ubuntu.com/community/MetaPackages

ROS 2 中的不同变体由 `REP-2001 <https://reps.openrobotics.org/rep-2001/>`_ 规定。

除官方变体外，也可能存在面向特定机构或机器人的元功能包，具体说明请参阅 `REP-108 <https://reps.openrobotics.org/rep-0108/#institution-specific>`_。

添加变体
--------

可以通过向 ``REP-2001`` 提交 Pull Request，提出对该规范的更新，以增加对 ROS 社区普遍有用的变体。新变体的提案应描述其中包含的软件包。

机构和机器人专用变体可以由相应维护者直接发布，无需更新 REP-2001。

创建项目专用变体
----------------

如果你正在为自己的私有项目创建 ROS 软件包，可以参考官方变体，为项目创建专用变体。只需要创建两个文件：

#. 创建一个最小化变体功能包：使用 ``ament_cmake`` 构建类型，将 ``ament_cmake`` 声明为 ``buildtool_depend``，并为希望纳入变体的每个软件包添加 ``exec_depend`` 条目。

   .. code-block:: xml

    <?xml version="1.0"?>
    <?xml-model href="http://download.ros.org/schema/package_format2.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
    <package format="2">
      <name>my_project_variant</name>
      <version>1.0.0</version>
      <description>A package to aggregate all packages in my_project.</description>
      <maintainer email="maintainer-email">Maintainer Name</maintainer>
      <license>Apache License 2.0</license>
      <!-- packages in my_project -->
      <exec_depend>my_project_msgs</exec_depend>
      <exec_depend>my_project_services</exec_depend>
      <exec_depend>my_project_examples</exec_depend>

      <export>
        <build_type>ament_cmake</build_type>
      </export>
    </package>

#. 创建一个最小化的 ament_cmake 功能包，其中包含 ``CMakeLists.txt``，用于将 ``package.xml`` 注册为 ROS 2 可用的 ament 功能包。

   .. code-block:: cmake

    cmake_minimum_required(VERSION 3.5)

    project(my_project_variant NONE)
    find_package(ament_cmake REQUIRED)
    ament_package()

随后，你就可以像安装其他私有软件包一样，构建并安装自己的变体功能包。

使用平台专用工具创建自定义变体
******************************

某些平台提供了创建基础软件包的工具，不需要完整的 ROS 构建农场环境或同等基础设施。可以使用这些工具创建依赖于特定平台的变体。

这种方式不支持 ROS 软件包工具，并且依赖于具体平台，但如果你要组合的是现有软件包，而不是混合使用公共和私有 ROS 软件包，那么所需基础设施会少得多。

例如，在 Debian 或 Ubuntu 系统上，可以使用 ``equivs`` 工具。Debian 管理员手册中有一节介绍 `元软件包 <https://www.debian.org/doc/manuals/debian-handbook/sect.building-first-package.en.html#id-1.18.5.2>`_。
