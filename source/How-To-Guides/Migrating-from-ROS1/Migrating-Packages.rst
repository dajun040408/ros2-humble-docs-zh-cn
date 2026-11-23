ROS 1 功能包迁移
================

.. contents:: 目录
   :depth: 2
   :local:

功能包迁移主要分为两种类型：

* 将现有 ROS 1 功能包的源代码迁移到 ROS 2，并希望保留大部分源代码，或至少使其保持相似。例如 pluginlib（https://github.com/ros/pluginlib）：源代码在同一仓库的不同分支中维护，必要时可以在这些分支之间移植通用补丁。
* 在 ROS 2 中重新实现 ROS 1 功能包的相同或类似功能，但预计源代码会有较大差异。例如 ROS 1 中的 roscpp（https://github.com/ros/ros_comm/tree/melodic-devel/clients/roscpp）与 ROS 2 中的 rclcpp（https://github.com/ros2/rclcpp/tree/rolling/rclcpp），它们位于不同仓库，并不共享代码。

前置条件
--------

将 ROS 1 功能包迁移到 ROS 2 之前，必须确保该功能包的所有依赖项都已在 ROS 2 中提供。

package.xml 格式版本
--------------------

ROS 2 仅支持 package.xml 格式版本 2 及更高版本。
如果功能包的 package.xml 使用格式 1，请按照本目录中的 package.xml 格式 1 迁移到格式 2 指南进行更新。

依赖名称
--------

通过 rosdep 引入的依赖名称通常无需更改，因为 ROS 1 和 ROS 2 共用这些名称。
rosdep 文档请参阅：https://docs.ros.org/en/humble/Tutorials/Intermediate/Rosdep.html。

某些已发布到 ROS 生态中的功能包在 ROS 2 中可能使用不同名称，因此需要相应更新依赖项。

元功能包
--------

ROS 2 没有专门的元功能包类型。
元功能包仍然可以作为普通功能包存在，只包含运行时依赖项。
从 ROS 1 迁移元功能包时，只需从功能包清单中删除 <metapackage /> 标签。
有关元功能包/变体的更多信息，请参阅“使用变体”指南。

许可证
------

在 ROS 1 中，我们推荐使用 BSD 三条款许可证（https://opensource.org/licenses/BSD-3-Clause）。
在 ROS 2 中，我们推荐使用 Apache 2.0 许可证（https://www.apache.org/licenses/LICENSE-2.0）。

对于任何新项目，无论使用 ROS 1 还是 ROS 2，我们都建议采用 Apache 2.0 许可证。

但是，将代码从 ROS 1 迁移到 ROS 2 时，不能直接更改许可证。
对于已有贡献，必须保留其原有许可证。

因此，如果迁移某个功能包，我们建议保留其现有许可证，并继续按照原有 OSI 许可证向该功能包贡献代码。对于核心组件，我们预计原有许可证通常为 BSD 许可证。

这样可以使许可证关系清晰、易于理解。

更改许可证
^^^^^^^^^^

许可证可以更改，但需要联系所有贡献者并取得许可。
对于大多数功能包，这可能是一项工作量很大的任务，通常不值得考虑。
如果功能包的贡献者数量较少，则可能具备可行性。
