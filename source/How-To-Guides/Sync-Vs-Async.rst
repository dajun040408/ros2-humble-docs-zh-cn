.. redirect-from::

  Guides/Sync-Vs-Async
  Tutorials/Sync-Vs-Async

.. _SyncAsync:

同步与异步服务客户端
====================

**级别：** 中级

**预计时间：** 10 分钟

.. contents:: 目录
   :depth: 2
   :local:

简介
----

本指南旨在提醒用户注意 Python 同步服务客户端 ``call()`` API 的风险。同步调用服务时很容易意外造成死锁，因此我们不建议使用 ``call()``。

对于有经验、希望使用同步调用并了解其陷阱的用户，本指南提供了正确使用 ``call()`` 的示例，同时指出可能导致死锁的场景。

由于我们建议避免同步调用，本指南也会介绍推荐替代方案——异步调用（``call_async()``）的功能和用法。

C++ 服务调用 API 仅提供异步方式，因此本指南中的比较和示例针对 Python 服务和客户端。这里对异步的定义通常也适用于 C++，但存在少数例外。

1 同步调用
----------

同步客户端发送服务请求后，会阻塞调用线程，直到收到响应。在此期间，该线程无法执行其他工作。调用可能需要任意长的时间才能完成。完成后，响应会直接返回给客户端。

以下示例展示如何在客户端节点中正确执行同步服务调用，类似于 :doc:`简单服务和客户端 <../Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client>` 教程中的异步节点。

.. code-block:: python

  import sys
  from threading import Thread

  from example_interfaces.srv import AddTwoInts
  import rclpy
  from rclpy.node import Node

  class MinimalClientSync(Node):

      def __init__(self):
          super().__init__('minimal_client_sync')
          self.cli = self.create_client(AddTwoInts, 'add_two_ints')
          while not self.cli.wait_for_service(timeout_sec=1.0):
              self.get_logger().info('service not available, waiting again...')
          self.req = AddTwoInts.Request()

      def send_request(self):
          self.req.a = int(sys.argv[1])
          self.req.b = int(sys.argv[2])
          return self.cli.call(self.req)
          # 只有在下面的独立线程中调用 rclpy.spin() 时才有效。
          # 如果在 main() 中稍后才 spin，或从定时器回调中调用此方法，则会导致死锁。

  def main():
      rclpy.init()

      minimal_client = MinimalClientSync()

      spin_thread = Thread(target=rclpy.spin, args=(minimal_client,))
      spin_thread.start()

      response = minimal_client.send_request()
      minimal_client.get_logger().info(
          'Result of add_two_ints: for %d + %d = %d' %
          (minimal_client.req.a, minimal_client.req.b, response.sum))

      minimal_client.destroy_node()
      rclpy.shutdown()


  if __name__ == '__main__':
      main()

注意 ``main()`` 中的客户端在单独线程中调用 ``rclpy.spin``。``send_request`` 和 ``rclpy.spin`` 都是阻塞操作，因此必须放在不同线程中。

1.1 同步调用导致死锁
--------------------

同步 ``call()`` API 有多种可能导致死锁的情况。

如上面示例中的注释所述，如果没有创建独立线程来执行 ``rclpy`` 的 spin 操作，就可能发生死锁。当客户端阻塞某个线程并等待响应，而响应又只能在同一个线程中返回时，客户端将永远等待下去，线程中的其他工作也无法执行。

另一个死锁原因是在订阅、定时器或服务回调中同步调用服务，从而阻塞 ``rclpy.spin``。例如，将同步客户端的 ``send_request`` 放入回调中：

.. code-block:: python

  def trigger_request(msg):
      response = minimal_client.send_request()  # 这会导致死锁
      minimal_client.get_logger().info(
          'Result of add_two_ints: for %d + %d = %d' %
          (minimal_client.req.a, minimal_client.req.b, response.sum))
  subscription = minimal_client.create_subscription(String, 'trigger', trigger_request, 10)

  rclpy.spin(minimal_client)

发生死锁是因为 ``rclpy.spin`` 不会抢占正在执行 ``send_request`` 的回调。通常，回调中只应执行轻量且快速的操作。

.. warning::

  发生死锁时，你不会收到服务阻塞的任何提示。不会有警告或异常，也不会在堆栈跟踪中看到相关提示，并且调用不会失败返回。

2 异步调用
----------

``rclpy`` 中的异步调用完全安全，是推荐的服务调用方式。与同步调用不同，可以从任何位置发起异步调用，而不会阻塞其他 ROS 或非 ROS 进程。

异步客户端发送服务请求后会立即返回一个 ``future``。该值用于表示调用和响应是否完成，而不是响应本身。你可以随时查询返回的 ``future``，以获取响应。

由于发送请求不会阻塞线程，因此可以在同一个线程中通过循环同时执行 ``rclpy`` spin 和检查 ``future``：

.. code-block:: python

    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            # 获取响应

Python :doc:`简单服务和客户端 <../Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client>`` 教程展示了如何执行异步服务调用，并通过循环获取 ``future`。

也可以通过定时器或回调（例如 `此示例 <https://github.com/ros2/examples/blob/{REPOS_FILE_BRANCH}/rclpy/services/minimal_client/examples_rclpy_minimal_client/client_async_callback.py>`_）、专用线程或其他方式获取 ``future``。如何存储 ``future`、检查其状态并获取响应，由调用方自行决定。

总结
----

不建议实现同步服务客户端。同步调用容易发生死锁，而且死锁发生时不会提供任何提示。

如果必须使用同步调用，可以参考第 1 节中的安全示例，同时应了解第 1.1 节中列出的死锁条件。我们建议优先使用异步服务客户端。
