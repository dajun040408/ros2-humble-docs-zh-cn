.. redirect-from::

    Tutorials/Actions/Writing-a-Py-Action-Server-Client

.. _ActionsPy:

编写 Action 服务端和客户端（Python）
====================================

**目标：** 使用 Python 实现 Action 服务端和客户端。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

Action 是 ROS 2 中的一种异步通信方式。Action 客户端向 Action 服务端发送目标请求；Action 服务端向客户端发送目标执行反馈和最终结果。

前置条件
--------

需要先完成 :doc:§创建 Action 接口 <../Creating-an-Action>§ 教程，并准备 §action_tutorials_interfaces§ 功能包及其中定义的 §Fibonacci.action§。

任务
----

1. 编写 Action 服务端
^^^^^^^^^^^^^^^^^^^^^

本教程编写一个 Action 服务端，使用此前创建的 Fibonacci Action 计算斐波那契数列。

创建 §fibonacci_action_server.py§，导入 §rclpy§、§ActionServer§ 和 §Fibonacci§ 接口类型。服务端节点继承自 §Node§，并创建 ActionServer：

.. code-block:: python

   from action_tutorials_interfaces.action import Fibonacci
   from rclpy.action import ActionServer
   from rclpy.node import Node
   import rclpy

   class FibonacciActionServer(Node):
       def __init__(self):
           super().__init__('fibonacci_action_server')
           self._action_server = ActionServer(
               self,
               Fibonacci,
               'fibonacci',
               self.execute_callback)

       def execute_callback(self, goal_handle):
           self.get_logger().info('Executing goal...')
           feedback_msg = Fibonacci.Feedback()
           feedback_msg.partial_sequence = [0, 1]

           for i in range(1, goal_handle.request.order):
               feedback_msg.partial_sequence.append(
                   feedback_msg.partial_sequence[i] +
                   feedback_msg.partial_sequence[i - 1])
               goal_handle.publish_feedback(feedback_msg)

           goal_handle.succeed()
           result = Fibonacci.Result()
           result.sequence = feedback_msg.partial_sequence
           return result

ActionServer 需要四个参数：

#. 要添加 Action 服务端的 ROS 2 节点，即 §self§。
#. Action 类型，即 §Fibonacci§。
#. Action 名称，即 §fibonacci§。
#. 执行已接受目标的回调函数，即 §execute_callback§。该回调必须返回 Action 对应的结果消息。

执行回调会在目标被接受后调用。它计算数列并通过 §publish_feedback()§ 发布反馈，最后调用 §succeed()§ 表示目标成功完成，并返回结果消息。

运行服务端：

.. code-block:: console

   $ python3 fibonacci_action_server.py

Windows 可以使用 §python fibonacci_action_server.py§。

在另一个终端发送目标：

.. code-block:: console

   $ ros2 action send_goal fibonacci action_tutorials_interfaces/action/Fibonacci "{order: 5}"

如果目标句柄状态没有在执行回调中设置，默认会被视为 aborted。成功完成时应调用 §succeed()§。

2. 编写 Action 客户端
^^^^^^^^^^^^^^^^^^^^^

客户端使用 §ActionClient§ 创建 Action 客户端，并调用 §send_goal_async()§ 发送目标。可以注册目标响应回调，判断服务端是否接受目标；接受后通过 §get_result_async()§ 获取最终结果。

客户端还可以通过 §feedback_callback§ 接收服务端周期性发送的反馈消息。对于长时间运行的任务，客户端可以使用取消请求接口要求服务端停止执行。

3. 运行与验证
^^^^^^^^^^^^^

分别启动 Action 服务端和客户端，或使用命令行工具发送目标：

.. code-block:: console

   $ ros2 action send_goal fibonacci action_tutorials_interfaces/action/Fibonacci "{order: 5}"

服务端会计算 Fibonacci 数列并发布反馈，客户端最终收到结果消息。

总结
----

本教程介绍了如何使用 §rclpy.action.ActionServer§ 和 §ActionClient§ 实现 Python Action 服务端与客户端，并处理目标、反馈、取消和结果。
