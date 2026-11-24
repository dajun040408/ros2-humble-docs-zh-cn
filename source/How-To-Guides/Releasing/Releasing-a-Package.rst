.. redirect-from::

    Releasing-a-ROS-2-package-with-bloom
    Guides/Releasing-a-ROS-2-package-with-bloom
    Tutorials/Releasing-a-ROS-2-package-with-bloom
    How-To-Guides/Releasing-a-ROS-2-package-with-bloom

发布 ROS 2 功能包
=================

.. toctree::
   :hidden:

   Index-Your-Packages
   First-Time-Release
   Subsequent-Releases
   Release-Team-Repository
   Release-Track

**发布功能包意味着让你的功能包能够在 ROS 2 公共构建农场（buildfarm）中构建和分发。** 这将带来以下效果：

* 你的功能包可以通过软件包管理器安装（例如 Ubuntu 上的 ``apt``），并面向某个 ROS 发行版支持的所有 Linux 平台提供，具体说明参见 `REP 2000 <https://reps.openrobotics.org/rep-2000/>`_。
* 系统可以自动为你的功能包生成 API 文档。
* 你的功能包会被收录到 `ROS Index <https://index.ros.org>`_。
* （可选）可以为代码仓库中的 Pull Request 启用自动 CI。

**请根据以下情况选择相应指南完成发布：**

* :doc:`为功能包建立索引 <Index-Your-Packages>`：如果这是该功能包第一次发布。
* :doc:`首次发布 <First-Time-Release>`：如果这是第一次发布，但功能包已经建立索引。
* :doc:`后续版本发布 <Subsequent-Releases>`：如果要发布已经发布过的功能包的新版本。

成功完成上述步骤后，你的功能包将在下一次 ROS 发行版同步时发布到 ROS 生态系统中。
