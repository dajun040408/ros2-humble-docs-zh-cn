使用 ROS 2 Launch 启动可组合节点
=================================

.. contents:: 目录
   :depth: 1
   :local:

在 :doc:`组件组合教程 <../Tutorials/Intermediate/Composition>` 中，你已经学习了可组合节点以及如何从命令行使用它们。在 :doc:`Launch 教程 <../Tutorials/Intermediate/Launch/Launch-Main>` 中，你已经学习了启动文件以及如何使用启动文件管理多个节点。

本指南将结合上述两个主题，介绍如何为可组合节点编写启动文件。

环境准备
--------

有关 ROS 2 安装详情，请参阅 :doc:`安装说明 <../Installation>`。

如果你通过软件包安装 ROS 2，请确保已安装 ``ros-{DISTRO}-image-tools``。如果你下载了归档包，或从源码构建了 ROS 2，该软件包已经包含在安装内容中。

启动文件示例
------------

下面展示分别使用 XML、YAML 和 Python 编写的启动文件，用于启动可组合节点。所有启动文件都会执行以下操作：

* 实例化一个 ``cam2image`` 可组合节点，并为其设置重映射、自定义参数和额外参数。
* 实例化一个 ``showimage`` 可组合节点，并为其设置重映射、自定义参数和额外参数。

.. tabs::

  .. group-tab:: XML

    .. literalinclude:: launch/composition_launch.xml
      :language: xml

  .. group-tab:: YAML

    .. literalinclude:: launch/composition_launch.yaml
      :language: yaml

  .. group-tab:: Python

    .. literalinclude:: launch/composition_launch.py
      :language: python

将可组合节点加载到现有容器
--------------------------

有时，容器可能由其他启动文件启动，也可能通过命令行启动。在这种情况下，需要将组件添加到现有容器中。可以使用 ``LoadComposableNodes`` 将组件加载到指定容器。下面的示例启动与前面相同的节点。

.. tabs::

  .. group-tab:: XML

    .. literalinclude:: launch/composition_load_launch.xml
      :language: xml

  .. group-tab:: YAML

    .. literalinclude:: launch/composition_load_launch.yaml
      :language: yaml

  .. group-tab:: Python

    .. literalinclude:: launch/composition_load_launch.py
      :language: python

通过命令行使用启动文件
----------------------

上述任意启动文件都可以通过 ``ros2 launch`` 运行。将对应内容复制到本地文件，然后执行：

.. code-block:: console

  $ ros2 launch <path_to_launch_file>

进程内通信
----------

以上示例都使用了一个额外参数，用于配置节点之间的进程内通信。有关进程内通信的更多信息，请参阅 :doc:`进程内通信教程 <../Tutorials/Demos/Intra-Process-Communication>`。

XML、YAML 还是 Python：应该使用哪一种？
---------------------------------------

更多信息请参阅 :doc:`不同格式启动文件指南 <Launch-file-different-formats>` 中的 :ref:`相关讨论 <launch-file-different-formats-which>`。
