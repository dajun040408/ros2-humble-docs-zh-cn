.. redirect-from::

    Tutorials/Actions/Writing-a-Py-Action-Server-Client

.. _ActionsPy:

编写 Action 服务端和客户端（Python）
===========================================================================

**目标：** 使用 Python 实现 Action 服务端和客户端。

**教程级别：** 中级 | **预计时间：** 15 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
------

Action 是 ROS 2 中的一种异步通信方式。Action 客户端向 Action 服务端发送目标请求；Action 服务端向客户端发送目标执行反馈和最终结果。

前置条件
------------

需要先完成 :doc:`创建 Action 接口 <../Creating-an-Action>` 教程，并准备 ``action_tutorials_interfaces`` 功能包及其中定义的 ``Fibonacci.action``。

任务
------

1. 编写 Action 服务端
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

本节实现一个使用前面创建的 Fibonacci Action 接口计算斐波那契数列的服务端。

此前的教程中，你已经创建了功能包并使用 ``ros2 run`` 运行节点。为了让本教程更简单，这里将 Action 服务端写在单个 Python 文件中。如果希望查看完整的 Action 教程功能包，可以参考 ``action_tutorials`` 示例仓库。

在主目录中新建文件 ``fibonacci_action_server.py``，并添加以下代码：

.. literalinclude:: scripts/server_0.py
   :language: python

第 8 行定义了 ``FibonacciActionServer`` 类，该类继承自 ``Node``。初始化类时会调用 ``Node`` 的构造函数，并将节点命名为 ``fibonacci_action_server``：

.. literalinclude:: scripts/server_0.py
   :language: python
   :lines: 11

构造函数中还会实例化一个新的 Action 服务端：

.. literalinclude:: scripts/server_0.py
   :language: python
   :lines: 12-16

创建 Action 服务端需要四个参数：

1. 要添加 Action 服务端的 ROS 2 节点：``self``。
2. Action 类型：Fibonacci（在第 5 行导入）。
3. Action 名称：``fibonacci``。
4. 用于执行已接受目标的回调函数：``self.execute_callback``。该回调函数必须返回对应 Action 类型的结果消息。

类中还定义了 ``execute_callback`` 方法：

.. literalinclude:: scripts/server_0.py
   :language: python
   :lines: 18-21

目标被接受后，就会调用该方法执行目标。

尝试运行 Action 服务端：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ python3 fibonacci_action_server.py

  .. group-tab:: macOS

    .. code-block:: console

       $ python3 fibonacci_action_server.py

  .. group-tab:: Windows

    .. code-block:: console

       $ python fibonacci_action_server.py

在另一个终端中，可以使用命令行接口发送目标：

.. code-block:: console

   $ ros2 action send_goal fibonacci action_tutorials_interfaces/action/Fibonacci "{order: 5}"

在运行 Action 服务端的终端中，应该能看到 ``Executing goal...`` 日志，随后出现一条警告，提示目标状态尚未设置。

默认情况下，如果执行回调没有设置目标句柄状态，系统会将目标视为 aborted（已中止）。

可以在目标句柄上调用 ``succeed()`` 方法，明确表示目标执行成功：

.. literalinclude:: scripts/server_1.py
   :language: python
   :lines: 18-22
   :emphasize-lines: 3

重启 Action 服务端并再次发送目标后，应该能看到目标以 ``SUCCEEDED`` 状态完成。

接下来，让目标执行过程真正计算并返回所请求的斐波那契数列：

.. literalinclude:: scripts/server_2.py
   :language: python
   :lines: 18-30
   :emphasize-lines: 4-7,12

计算完成后，将数列赋给结果消息的对应字段，然后返回结果。

再次重启 Action 服务端并发送目标，应该能看到目标以正确的数列结果完成。

1.2 发布反馈
~~~~~~~~~~~~~~~~~~~~~~~~

Action 的一个重要优势是：在目标执行过程中，可以向 Action 客户端持续提供反馈。

Action 服务端可以调用目标句柄的 ``publish_feedback()`` 方法向客户端发布反馈。

这里将原来的 ``sequence`` 变量替换为反馈消息，用它保存当前数列。每次在循环中更新反馈消息后，都发布一次反馈，并通过休眠控制发布节奏：

.. literalinclude:: scripts/server_3.py
   :language: python
   :emphasize-lines: 1,23,24,27-31,36

重启 Action 服务端后，可以在命令行工具中添加 ``--feedback`` 选项，确认服务端正在发布反馈：

.. code-block:: console

   $ ros2 action send_goal --feedback fibonacci action_tutorials_interfaces/action/Fibonacci "{order: 5}"

2. 编写 Action 客户端
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

本教程同样将 Action 客户端写在单个 Python 文件中。

新建文件 ``fibonacci_action_client.py``，并添加以下基础代码：

.. literalinclude:: scripts/client_0.py
   :language: python

这里定义了 ``FibonacciActionClient`` 类，该类继承自 ``Node``。初始化时调用 ``Node`` 构造函数，并将节点命名为 ``fibonacci_action_client``：

.. literalinclude:: scripts/client_0.py
   :language: python
   :lines: 11

在类构造函数中，还会使用前一个 :doc:`创建 Action 接口 <../Creating-an-Action>` 教程中定义的自定义 Action 类型创建 Action 客户端：

.. literalinclude:: scripts/client_0.py
   :language: python
   :lines: 12

创建 ``ActionClient`` 需要传入三个参数：

1. 要添加 Action 客户端的 ROS 2 节点：``self``。
2. Action 类型：``Fibonacci``。
3. Action 名称：``fibonacci``。

Action 客户端只能与 Action 名称和类型相同的服务端通信。

``FibonacciActionClient`` 类中还定义了 ``send_goal`` 方法：

.. literalinclude:: scripts/client_0.py
   :language: python
   :lines: 14-20

该方法会等待 Action 服务端可用，然后向服务端发送目标，并返回一个 future 对象，之后可以等待该对象完成。

类定义之后，程序定义 ``main()`` 函数，用于初始化 ROS 2 并创建 ``FibonacciActionClient`` 节点实例。随后发送目标，并等待目标执行完成。

最后，在 Python 程序入口处调用 ``main()``。

先运行前面创建的 Action 服务端，再测试 Action 客户端：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ python3 fibonacci_action_server.py

  .. group-tab:: macOS

    .. code-block:: console

       $ python3 fibonacci_action_server.py

  .. group-tab:: Windows

    .. code-block:: console

       $ python fibonacci_action_server.py

在另一个终端中运行 Action 客户端：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ python3 fibonacci_action_client.py

  .. group-tab:: macOS

    .. code-block:: console

       $ python3 fibonacci_action_client.py

  .. group-tab:: Windows

    .. code-block:: console

       $ python fibonacci_action_client.py

此时应该能看到 Action 服务端成功执行目标时输出的日志：

.. code-block:: console

   [INFO] [fibonacci_action_server]: Executing goal...
   [INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1])
   [INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2])
   [INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3])
   [INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3, 5])
   ...

Action 客户端启动后会很快结束。此时客户端已经能够发送目标，但还没有显示结果，也没有获取反馈。接下来完善这两部分功能。

2.1 获取结果
~~~~~~~~~~~~~~~~~~~~~~~~

客户端发送目标后，如何知道目标何时执行完成？

需要分两步处理：首先获取已发送目标对应的目标句柄，然后通过目标句柄请求执行结果。

下面是这一示例的完整代码：

.. literalinclude:: scripts/client_1.py
   :language: python

``ActionClient.send_goal_async()`` 方法会返回一个指向目标句柄的 future。首先注册一个回调函数，在 future 完成时执行：

.. literalinclude:: scripts/client_1.py
   :language: python
   :lines: 22

注意：当 Action 服务端接受或拒绝目标请求时，该 future 就会完成。

接下来查看 ``goal_response_callback``。可以先检查目标是否被拒绝。如果目标被拒绝，就提前返回，因为此时不会有结果：

.. literalinclude:: scripts/client_1.py
   :language: python
   :lines: 24-30

获取目标句柄后，可以调用 ``get_result_async()`` 请求结果。与发送目标类似，该方法也会返回一个 future，当结果准备好时该 future 就会完成。

为结果 future 注册回调函数：

.. literalinclude:: scripts/client_1.py
   :language: python
   :lines: 32-33

在回调函数中输出结果数列，并关闭 ROS 2，以便程序正常退出：

.. literalinclude:: scripts/client_1.py
   :language: python
   :lines: 35-38

确保另一个终端中运行着 Action 服务端，然后尝试运行 Fibonacci Action 客户端：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

       $ python3 fibonacci_action_client.py

  .. group-tab:: macOS

    .. code-block:: console

       $ python3 fibonacci_action_client.py

  .. group-tab:: Windows

    .. code-block:: console

       $ python fibonacci_action_client.py

现在应该能看到目标被接受以及最终结果的日志。

2.2 获取反馈
~~~~~~~~~~~~~~~~~~~~~~~~

Action 客户端已经可以发送目标了。接下来，还需要获取 Action 服务端在目标执行期间发布的反馈。

下面是这一示例的完整代码：

.. literalinclude:: scripts/client_2.py
   :language: python

反馈消息的回调函数如下：

.. literalinclude:: scripts/client_2.py
   :language: python
   :lines: 40-42

回调函数会读取反馈消息中的 ``partial_sequence`` 字段，并将当前数列输出到屏幕。

还需要在发送目标时，将该回调函数注册到 Action 客户端：

.. literalinclude:: scripts/client_2.py
   :language: python
   :lines: 20

完成后运行 Action 客户端，就可以看到反馈消息持续输出。

总结
------

本教程逐步实现了一个 Python Action 服务端和客户端，并配置它们交换目标请求、反馈和最终结果。

相关内容
------------

Python Action 服务端和客户端还有其他实现方式。可以查看 ``ros2/examples`` 仓库中的 ``minimal_action_server`` 和 ``minimal_action_client`` 功能包：`ros2/examples 仓库 <https://github.com/ros2/examples/tree/{REPOS_FILE_BRANCH}/rclpy/actions>`_。

有关 ROS 2 Actions 的更多详细信息，请参阅 `ROS 2 Actions 设计文章 <http://design.ros2.org/articles/actions.html>`_。
