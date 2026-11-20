.. redirect-from::

功能包文档
============

ROS 功能包文档，也就是通过 apt 或其他工具安装的特定功能包的文档，可以在多个位置找到。下面简要列出查找 ROS 功能包文档的途径。

* 大多数 ROS 2 功能包的功能包级文档都包含在 `此索引页面 <https://docs.ros.org/en/{DISTRO}/p/>`__ 中。
* 所有 ROS 2 功能包的文档都会与其相关信息一起托管在 `ROS Index <https://index.ros.org/>`__ 上。在 ROS Index 中搜索功能包，可以查看其发布到哪些发行版、README.md 文件、URL 以及其他重要元数据。

大型功能包
------------

MoveIt、Nav2 和 micro-ROS 等大型功能包在 ros.org 上拥有自己的域名或子域名。以下是其中一些项目：

* `MoveIt <https://moveit.ai/>`__
* `Navigation2 <https://nav2.org/>`__
* `Control <https://control.ros.org/master/index.html>`__
* `microROS（嵌入式系统）<https://micro.ros.org/>`__

API 文档
----------

你可以通过以下链接查阅 {DISTRO_TITLE} 发行版中 ROS 客户端库的 API 文档：

* `rclcpp - C++ 客户端库 <https://docs.ros.org/en/{DISTRO}/p/rclcpp/generated/index.html>`__
* `rclcpp_lifecycle - C++ 生命周期库 <https://docs.ros.org/en/{DISTRO}/p/rclcpp_lifecycle/generated/index.html>`__
* `rclcpp_components - C++ 组件库 <https://docs.ros.org/en/{DISTRO}/p/rclcpp_components/generated/index.html>`__
* `rclcpp_action - C++ 动作库 <https://docs.ros.org/en/{DISTRO}/p/rclcpp_action/generated/index.html>`__

将你的功能包添加到 docs.ros.org
---------------------------------

所有已发布的 ROS 2 功能包都会自动添加到 docs.ros.org 和 `ROS Index <https://index.ros.org/>``__。如果你希望启用或配置自己的功能包，请参阅 :doc:`功能包文档编写指南 <./How-To-Guides/Documenting-a-ROS-2-Package>`。
