编写基础集成测试（launch_testing）
====================================

**目标：** 为 ROS 2 turtlesim 节点创建并运行集成测试。

**教程级别：** 中级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

前置条件
--------

开始本教程之前，建议先完成以下启动节点相关教程：

* :doc:`启动多个节点 <../../Beginner-CLI-Tools/Launching-Multiple-Nodes/Launching-Multiple-Nodes>`
* :doc:`创建启动文件 <../../Intermediate/Launch/Creating-Launch-Files>`

背景
----

单元测试侧重验证某个非常具体的功能，而集成测试侧重验证多个代码部分之间的交互。

在 ROS 2 中，通常通过启动一个或多个节点组成的系统来完成集成测试，例如 `Gazebo 仿真器 <https://gazebosim.org/home>`_ 和 `Nav2 导航栈 <https://github.com/ros-planning/navigation2.git>`_。因此，集成测试的配置和运行都更加复杂。

ROS 2 集成测试的一个关键要求是：不同测试中的节点不应相互通信，即使这些测试并行运行也应如此。本教程将使用一个专门的测试运行器，为每个测试分配唯一的 :doc:`ROS Domain ID <../../../Concepts/Intermediate/About-Domain-ID>`。

此外，集成测试必须融入整体测试流程。标准做法是确保每个测试都输出 XUnit 文件，以便常见测试工具轻松解析。

概述
----

本教程主要使用 `launch_testing` 软件包（`launch_testing 仓库 <https://github.com/ros2/launch/tree/{REPOS_FILE_BRANCH}/launch_testing>`_）。

这项与 ROS 无关的功能可以扩展 Python 启动文件，同时支持两类测试：

* **活动测试（active tests）：** 节点运行期间执行。
* **关闭后测试（post-shutdown tests）：** 所有节点退出后执行。

`launch_testing` 使用 Python 标准模块 `unittest` 执行实际测试。为了让这些集成测试成为 `colcon test` 的一部分，需要在 `CMakeLists.txt` 中注册启动文件。

步骤
----

1. 在测试启动文件中描述测试
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

被测节点和测试本身都通过 Python 启动文件启动，其结构与 ROS 2 Python 启动文件类似。按照惯例，集成测试启动文件的名称采用 `test/test_*.py` 格式。

集成测试通常包含两类测试：被测节点运行期间执行的活动测试，以及节点退出后执行的关闭后测试。本教程将介绍这两种测试。

1.1 导入模块
~~~~~~~~~~~~

首先导入需要使用的 Python 模块。只有两个模块专门用于测试：通用测试框架 `unittest` 和 `launch_testing`。

.. code-block:: python

  import os
  import sys
  import time
  import unittest

  import launch
  import launch_ros
  import launch_testing.actions
  import rclpy
  from turtlesim.msg import Pose

1.2 生成测试描述
~~~~~~~~~~~~~~~

`generate_test_description` 函数描述需要启动的内容，类似于 ROS 2 Python 启动文件中的 `generate_launch_description`。

下面的示例会启动 turtlesim 节点，并在半秒后启动测试。

在更复杂的集成测试中，可能需要启动由多个节点组成的系统，并添加用于模拟行为或与被测节点交互的辅助节点。

.. code-block:: python

  def generate_test_description():
      return (
          launch.LaunchDescription(
              [
                  # 被测节点
                  launch_ros.actions.Node(
                      package='turtlesim',
                      namespace='',
                      executable='turtlesim_node',
                      name='turtle1',
                  ),
                  # 0.5 秒后开始测试
                  launch.actions.TimerAction(
                      period=0.5, actions=[launch_testing.actions.ReadyToTest()]),
              ]
          ), {},
      )

1.3 活动测试
~~~~~~~~~~~~

活动测试会与正在运行的节点交互。本教程将检查 turtlesim 节点是否发布位姿消息（通过监听 `turtle1/pose` 话题），以及它是否通过 stderr 输出生成海龟的日志。

活动测试定义为继承自 `unittest.TestCase` 的类的方法。这里的子类 `TestTurtleSim` 包含以下方法：

* `test_*`：测试方法，每个方法都会与被测节点进行 ROS 通信，和/或监听进程输出（通过 `proc_output` 传入）。这些方法按顺序执行。
* `setUp`、`tearDown`：分别在每个测试方法执行之前和之后运行，用于准备和清理测试夹具。通过在 `setUp` 中创建节点，每个测试都会使用不同的节点实例，从而降低测试之间相互通信的风险。
* `setUpClass`、`tearDownClass`：分别在所有测试方法执行之前和之后运行一次的类方法。

强烈建议阅读 `launch_testing` 关于该主题的`详细文档 <https://docs.ros.org/en/{DISTRO}/p/launch_testing/index.html>`_。

.. code-block:: python

  # 活动测试
  class TestTurtleSim(unittest.TestCase):
      @classmethod
      def setUpClass(cls):
          rclpy.init()

      @classmethod
      def tearDownClass(cls):
          rclpy.shutdown()

      def setUp(self):
          self.node = rclpy.create_node('test_turtlesim')

      def tearDown(self):
          self.node.destroy_node()

      def test_publishes_pose(self, proc_output):
          """检查是否发布位姿消息"""
          msgs_rx = []
          sub = self.node.create_subscription(
              Pose, 'turtle1/pose',
              lambda msg: msgs_rx.append(msg), 100)
          try:
              # 监听位姿话题 10 秒
              end_time = time.time() + 10
              while time.time() < end_time:
                  # 执行 spin，以触发订阅回调
                  rclpy.spin_once(self.node, timeout_sec=1)
              # 应至少收到 100 条消息
              assert len(msgs_rx) > 100
          finally:
              self.node.destroy_subscription(sub)

      def test_logs_spawning(self, proc_output):
          """检查日志是否正确输出"""
          proc_output.assertWaitFor(
              'Spawning turtle [turtle1] at x=',
              timeout=5, stream='stderr')

注意，`test_publishes_pose` 中监听 `turtle1/pose` 话题的方式与 :doc:`通常使用的方法 <../../Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber>` 不同。

这里没有调用阻塞式 `rclpy.spin`，而是触发 `spin_once` 方法。该方法会执行第一个可用回调（如果 1 秒内收到消息，就是订阅回调），直到收集到最近 10 秒内发布的所有消息。

`launch_testing_ros` 软件包提供了一些便捷函数来实现类似行为，例如 `WaitForTopics`。详情请参阅`launch_testing_ros 文档 <https://docs.ros.org/en/{DISTRO}/p/launch_testing_ros/index.html>`_。

如果希望进一步扩展，可以添加第三个测试：发布 Twist 消息让海龟移动，然后检查位姿消息是否发生变化。这相当于自动化执行部分 :doc:`Turtlesim 入门教程 <../../Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim>`。

1.4 关闭后测试
~~~~~~~~~~~~~~

使用 `launch_testing.post_shutdown_test` 装饰器标记的类，会在被测节点退出后执行。常见测试是检查节点是否正常退出，`launch_testing` 为此提供了 `asserts.assertExitCodes` 方法。

.. code-block:: python

  # 关闭后测试
  @launch_testing.post_shutdown_test()
  class TestTurtleSimShutdown(unittest.TestCase):
      def test_exit_codes(self, proc_info):
          """检查进程是否正常退出"""
          launch_testing.asserts.assertExitCodes(proc_info)

2. 在 CMakeLists.txt 中注册测试
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 `CMakeLists.txt` 中注册测试有两个作用：

* 将测试集成到 ROS 2 基于 CMake 的功能包所依赖的 `CTest` 框架中，因此运行 `colcon test` 时会执行这些测试。
* 可以指定测试的运行方式。本例中会为测试分配唯一的 Domain ID，以确保测试隔离。

后一项通过特殊测试运行器 `run_test_isolated.py` 实现。该运行器会在每个测试中设置唯一的 ROS Domain ID。

在 `CMakeLists.txt` 中添加：

.. code-block:: cmake

   if(BUILD_TESTING)
     find_package(launch_testing_ament_cmake REQUIRED)
     add_launch_test(test/test_turtlesim.py)
   endif()

并在 `package.xml` 中添加测试依赖：

.. code-block:: xml

   <test_depend>launch_testing_ament_cmake</test_depend>

3. 构建并运行测试
^^^^^^^^^^^^^^^^^

从工作空间根目录构建功能包：

.. code-block:: console

   $ colcon build

随后运行测试：

.. code-block:: console

   $ colcon test

可以使用以下命令查看测试结果：

.. code-block:: console

   $ colcon test-result --verbose

总结
----

本教程介绍了如何使用 `launch_testing` 为 ROS 2 节点编写集成测试，包括活动测试、关闭后测试，以及如何将测试注册到 CMake/colcon 测试流程中。
