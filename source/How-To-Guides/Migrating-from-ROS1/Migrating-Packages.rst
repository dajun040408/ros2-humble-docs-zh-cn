功能包迁移
==========

.. contents:: 目录
   :depth: 2
   :local:

功能包迁移主要有两种不同类型：

* 将现有 ROS 1 功能包的源代码迁移到 ROS 2，并希望其中相当一部分源代码保持不变或基本相似。例如 `pluginlib <https://github.com/ros/pluginlib>`_，其源代码在同一个仓库的不同分支中维护，必要时可以在这些分支之间移植通用补丁。
* 在 ROS 2 中实现 ROS 1 功能包相同或相似的功能，但假设源代码会有较大差异。例如 ROS 1 中的 `roscpp <https://github.com/ros/ros_comm/tree/melodic-devel/clients/roscpp>`_ 和 ROS 2 中的 `rclcpp <https://github.com/ros2/rclcpp/tree/rolling/rclcpp>`_，它们位于不同仓库，并不共享代码。

前置条件
--------

在将 ROS 1 功能包迁移到 ROS 2 之前，必须确保该功能包的所有依赖项都已在 ROS 2 中提供。

package.xml 格式版本
--------------------

ROS 2 仅支持 `package.xml` 格式版本 2 及更高版本。如果你的功能包使用格式 1，请按照 :doc:`Package.xml 格式 1 到 2 迁移指南 <./Migrating-Package-XML>` 更新文件。

依赖项名称
----------

来自 :doc:`rosdep <../../Tutorials/Intermediate/Rosdep>` 的依赖项名称通常不需要修改，因为 ROS 1 和 ROS 2 共享这些名称。

某些发布到 ROS 的功能包在 ROS 2 中可能使用不同名称，因此需要相应更新依赖项。

元功能包
--------

ROS 2 不再为元功能包（metapackage）提供特殊的软件包类型。元功能包仍然可以作为普通功能包存在，只包含运行时依赖项。

从 ROS 1 迁移元功能包时，只需从功能包清单中删除 `<metapackage />` 标签。有关元功能包/变体的更多信息，请参阅 :doc:`使用变体 <../Using-Variants>`。

许可证
------

在 ROS 1 中，我们推荐使用 `3-Clause BSD License <https://opensource.org/licenses/BSD-3-Clause>`_。在 ROS 2 中，我们推荐使用 `Apache 2.0 License <https://www.apache.org/licenses/LICENSE-2.0>`_。

对于任何新项目，无论使用 ROS 1 还是 ROS 2，我们都建议采用 Apache 2.0 许可证。

但是，从 ROS 1 向 ROS 2 迁移代码时，不能简单地更改许可证。所有既有贡献的原有许可证都必须保留。

因此，对于迁移中的功能包，我们建议保留原有许可证，并继续按照原有 OSI 许可证进行贡献；核心组件通常使用 BSD 许可证。

这样可以使许可证情况更加清晰、易于理解。

更改许可证
^^^^^^^^^^

更改许可证是可行的，但需要联系所有贡献者并获得许可。对于大多数功能包来说，这可能是一项工作量很大的任务，通常不值得考虑。如果功能包的贡献者数量较少，则可能比较容易实现。
