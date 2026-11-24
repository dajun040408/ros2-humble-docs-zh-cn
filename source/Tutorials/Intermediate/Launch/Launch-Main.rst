.. redirect-from::

    Tutorials/Launch-Files/Launch-Main
    Tutorials/Launch/Launch-Main

.. _LaunchFilesMain:

启动系统（Launch）
==================

ROS 2 启动文件允许你同时启动和配置多个包含 ROS 2 节点的可执行程序。

.. toctree::
   :hidden:

   Creating-Launch-Files
   Launch-system
   Using-Substitutions
   Using-Event-Handlers
   Using-ROS2-Launch-For-Large-Projects

#. :doc:`创建启动文件 <./Creating-Launch-Files>`。

   学习如何创建启动文件，一次性启动节点并加载其配置。

#. :doc:`启动和监控多个节点 <./Launch-system>`。

   深入了解启动文件的工作方式。

#. :doc:`使用替换 <./Using-Substitutions>`。

   使用替换机制，让可复用启动文件的描述更加灵活。

#. :doc:`使用事件处理器 <./Using-Event-Handlers>`。

   使用事件处理器监控进程状态，或定义一组复杂规则，以便动态修改启动文件。

#. :doc:`管理大型项目 <./Using-ROS2-Launch-For-Large-Projects>`。

   为大型项目组织启动文件，使其能够在不同场景中尽可能复用。教程还将展示参数、YAML 文件、重映射、命名空间、默认参数和 RViz 配置等启动工具的使用示例。

.. note::

   如果你从 ROS 1 迁移而来，可以参考 :doc:`ROS Launch 迁移指南 <../../../How-To-Guides/Migrating-from-ROS1/Migrating-Launch-Files>`，帮助你将启动文件迁移到 ROS 2。
