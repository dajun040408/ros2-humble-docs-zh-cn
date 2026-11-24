ROS 1 功能包迁移
================

.. contents:: 目录
   :depth: 2
   :local:

功能包迁移主要分为两种不同类型：

* 将现有功能包的源代码从 ROS 1 迁移到 ROS 2，并希望源代码中的很大一部分保持不变或至少保持相似。例如 `pluginlib <https://github.com/ros/pluginlib>`_：其源代码在同一仓库的不同分支中维护，必要时可以在这些分支之间移植通用补丁。
* 在 ROS 2 中重新实现 ROS 1 功能包的相同或类似功能，但预计源代码会有较大差异。例如 ROS 1 中的 `roscpp <https://github.com/ros/ros_comm/tree/melodic-devel/clients/roscpp>`_ 与 ROS 2 中的 `rclcpp <https://github.com/ros2/rclcpp/tree/rolling/rclcpp>`_，它们位于不同仓库，彼此不共享代码。

前置条件
--------

在迁移 ROS 1 功能包到 ROS 2 之前，必须确保该功能包的所有依赖项都已在 ROS 2 中提供。

package.xml 格式版本
--------------------

ROS 2 仅支持 ``package.xml`` 格式版本 2 及更高版本。如果功能包的 ``package.xml`` 使用格式 1，请使用 :doc:`package.xml 格式 1 迁移到格式 2 指南 <./Migrating-Package-XML>` 进行更新。

依赖项名称
----------

通过 :doc:`rosdep <../../Tutorials/Intermediate/Rosdep>` 引入的依赖项名称通常无需更改，因为 ROS 1 和 ROS 2 共用这些名称。某些已发布到 ROS 生态中的功能包在 ROS 2 中可能使用不同名称，因此可能需要相应更新依赖项。

元功能包
--------

ROS 2 没有专门的元功能包类型。元功能包仍然可以作为普通功能包存在，只包含运行时依赖项。从 ROS 1 迁移元功能包时，只需从功能包清单中删除 ``<metapackage />`` 标签。有关元功能包/变体的更多信息，请参阅 :doc:`使用变体 <../Using-Variants>`。

许可证
------

在 ROS 1 中，我们推荐使用 `BSD 三条款许可证 <https://opensource.org/licenses/BSD-3-Clause>`__；在 ROS 2 中，我们推荐使用 `Apache 2.0 许可证 <https://www.apache.org/licenses/LICENSE-2.0>`__。对于任何新项目，无论使用 ROS 1 还是 ROS 2，我们都建议采用 Apache 2.0 许可证。

但是，将代码从 ROS 1 迁移到 ROS 2 时，不能直接更改许可证。对于已有贡献，必须保留其原有许可证。因此，如果迁移某个功能包，我们建议保留现有许可证，并继续按照该功能包原有的 OSI 许可证贡献代码。对于核心组件，我们预计原有许可证为 BSD 许可证。

这样可以使许可证关系清晰、易于理解。

更改许可证
^^^^^^^^^^

许可证可以更改，但需要联系所有贡献者并取得许可。对于大多数功能包而言，这可能需要投入大量工作，通常不值得考虑。如果功能包的贡献者数量较少，则可能具备可行性。
