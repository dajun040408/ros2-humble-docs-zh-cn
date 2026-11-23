使用回调组
==========

当节点运行在多线程执行器（Multi-Threaded Executor）中时，ROS 2 提供回调组（Callback Groups）作为控制不同回调执行方式的工具。本页面介绍如何高效使用回调组。假设读者已经了解 :doc:§执行器 <../Concepts/Intermediate/About-Executors>§ 的基本概念。

.. contents:: 目录
   :local:

回调组基础
----------

当节点运行在多线程执行器中时，ROS 2 提供两种回调组，用于控制回调的执行方式：

* 互斥回调组（Mutually Exclusive Callback Group）
* 可重入回调组（Reentrant Callback Group）

这两种回调组对其回调的执行方式有不同限制。简而言之：

* 互斥回调组会阻止组内回调并行执行，效果相当于组内回调由单线程执行器（SingleThreadedExecutor）执行。
* 可重入回调组允许执行器以任意方式调度和执行组内回调，不施加限制。这意味着不同回调可以并行执行，同一个回调的不同实例也可以同时执行。
* 属于不同回调组（无论类型如何）的回调始终可以并行执行。

还需要注意，不同 ROS 2 实体会将其回调组传递给自己创建的所有回调。例如，如果为动作客户端分配了一个回调组，那么该客户端创建的所有回调都会分配到同一个回调组。

在 rclcpp 中，可以通过节点的 §create_callback_group§ 函数创建回调组；在 rclpy 中，可以通过调用回调组的构造函数创建。创建后，可以在创建订阅者、定时器等实体时，将回调组作为参数/选项传入。

必须保留对回调组的引用，否则执行器不会调用与该回调组关联的回调。

.. tabs::

  .. group-tab:: C++

    .. code-block:: cpp

      my_callback_group = create_callback_group(rclcpp::CallbackGroupType::MutuallyExclusive);

      rclcpp::SubscriptionOptions options;
      options.callback_group = my_callback_group;

      my_subscription = create_subscription<Int32>("/topic", rclcpp::SensorDataQoS(),
                                                    callback, options);

  .. group-tab:: Python

    .. code-block:: python

      my_callback_group = MutuallyExclusiveCallbackGroup()
      my_subscription = self.create_subscription(Int32, "/topic", self.callback, qos_profile=1,
                                                  callback_group=my_callback_group)

如果创建订阅者、定时器等实体时没有指定回调组，该实体就会分配到节点的默认回调组。默认回调组是一个互斥回调组，可以通过 rclcpp 中的 §NodeBaseInterface::get_default_callback_group()§ 或 rclpy 中的 §Node.default_callback_group§ 查询。

关于回调
^^^^^^^^

在 ROS 2 和执行器的语境下，回调是指由执行器负责调度和执行的函数。此处的回调示例包括：

* 订阅回调（接收并处理话题数据）。
* 定时器回调。
* 服务回调（在服务端处理服务请求）。
* 动作服务端和客户端中的不同回调。
* Future 的完成回调（done-callback）。

使用回调组时，需要牢记以下几点：

* ROS 2 中几乎所有由执行器执行的操作都是回调！从定义上讲，执行器运行的每个函数都是回调。ROS 2 系统中的非回调函数主要位于系统边缘，例如用户输入和传感器输入等。
* 有时回调是隐藏的，其存在可能不会直接体现在用户/开发者 API 中。尤其是在 rclpy 中进行服务或动作的“同步”调用时。例如，对服务调用 §Client.call(request)§ 会添加一个 Future 完成回调，该回调必须在函数调用期间执行，但用户无法直接看到它。

控制执行方式
------------

为了通过回调组控制执行方式，可以参考以下指导原则。

对于单个回调与其自身之间的执行关系：

* 如果希望回调能够与自身并行执行，应将其注册到可重入回调组。例如，需要并行处理多个动作调用或服务调用的动作/服务端。
* 如果希望回调**绝不**与自身并行执行，应将其注册到互斥回调组。例如，负责控制循环并发布控制命令的定时器回调。

对于不同回调之间的执行关系：

* 如果希望不同回调**绝不**并行执行，可以将它们注册到同一个互斥回调组。例如，这些回调访问共享的关键资源，且这些资源不是线程安全的。

如果希望不同回调并行执行，则可以根据回调实例是否允许重叠，选择以下两种方式：

* 将它们注册到不同的互斥回调组（单个回调实例不会与自身重叠执行）。
* 将它们注册到同一个可重入回调组（单个回调实例也允许重叠执行）。

不同回调并行执行的一个示例是：某个节点包含一个同步服务客户端和一个调用该服务的定时器。详细示例见下文。

避免死锁
--------

如果节点的回调组配置不正确，可能导致死锁或其他不期望的行为，尤其是在希望同步调用服务或动作时。

事实上，ROS 2 API 文档也指出，不应在回调中同步调用动作或服务，因为这可能导致死锁。异步调用在这方面确实更加安全，但同步调用也可以通过正确配置实现正常工作。另一方面，同步调用也有其优势，例如代码更简单、更容易理解。

因此，本节介绍如何正确配置节点的回调组，以避免死锁。

首先要注意，每个节点的默认回调组都是互斥回调组。如果用户在创建定时器、订阅者、客户端等实体时没有指定其他回调组，那么这些实体当时或之后创建的所有回调都会使用节点的默认回调组。

此外，如果节点中的所有内容都使用同一个互斥回调组，那么即使指定了多线程执行器，该节点的行为本质上也相当于由单线程执行器处理。因此，决定使用多线程执行器时，应始终指定一些回调组，这样选择多线程执行器才有意义。

基于以上说明，以下是避免死锁的建议：

* 如果在任何类型的回调中进行同步调用，则该回调与发起调用的客户端必须属于：
  * 不同的回调组（类型不限）；或者
  * 同一个可重入回调组。

* 如果由于其他要求（例如线程安全、等待结果时需要阻止其他回调执行，或者希望绝对确保不会发生死锁）而无法采用上述配置，则应使用异步调用。

如果不满足第一条要求，就一定会发生死锁。一个例子是在定时器回调中同步调用服务（下一节将展示）。

示例
----

下面通过一些简单示例，展示不同的回调组配置。示例代码考虑在定时器回调中同步调用服务的场景。

示例代码
^^^^^^^^

我们使用两个节点：一个节点提供简单服务。

.. tabs::

   .. group-tab:: C++

      .. code-block:: cpp

        #include <memory>
        #include "rclcpp/rclcpp.hpp"
        #include "std_srvs/srv/empty.hpp"

        using namespace std::placeholders;

        namespace cb_group_demo
        {
        class ServiceNode : public rclcpp::Node
        {
        public:
            ServiceNode() : Node("service_node")
            {
                service_ptr_ = this->create_service<std_srvs::srv::Empty>(
                        "test_service",
                        std::bind(&ServiceNode::service_callback, this, _1, _2, _3)
                );
            }

        private:
            rclcpp::Service<std_srvs::srv::Empty>::SharedPtr service_ptr_;

            void service_callback(
                    const std::shared_ptr<rmw_request_id_t> request_header,
                    const std::shared_ptr<std_srvs::srv::Empty::Request> request,
                    const std::shared_ptr<std_srvs::srv::Empty::Response> response)
            {
                (void)request_header;
                (void)request;
                (void)response;
                RCLCPP_INFO(this->get_logger(), "Received request, responding...");
            }
        };  // class ServiceNode
        }   // namespace cb_group_demo

        int main(int argc, char* argv[])
        {
            rclcpp::init(argc, argv);
            auto service_node = std::make_shared<cb_group_demo::ServiceNode>();

            RCLCPP_INFO(service_node->get_logger(), "Starting server node, shut down with CTRL-C");
            rclcpp::spin(service_node);
            RCLCPP_INFO(service_node->get_logger(), "Keyboard interrupt, shutting down.\n");

            rclcpp::shutdown();
            return 0;
        }

   .. group-tab:: Python

      .. code-block:: python

        import rclpy
        from rclpy.node import Node
        from std_srvs.srv import Empty

        class ServiceNode(Node):
            def __init__(self):
                super().__init__('service_node')
                self.srv = self.create_service(Empty, 'test_service', callback=self.service_callback)

            def service_callback(self, request, result):
                self.get_logger().info('Received request, responding...')
                return result


        if __name__ == '__main__':
            rclpy.init()
            node = ServiceNode()
            try:
                node.get_logger().info("Starting server node, shut down with CTRL-C")
                rclpy.spin(node)
            except KeyboardInterrupt:
                node.get_logger().info('Keyboard interrupt, shutting down.\n')
            node.destroy_node()
            rclpy.shutdown()

另一个节点包含该服务的客户端，以及用于定时发起服务调用的定时器：

.. tabs::

  .. group-tab:: C++

    *注意：* rclcpp 中的服务客户端 API 没有提供与 rclpy 类似的同步调用方法，因此这里通过等待 future 对象来模拟同步调用效果。

    .. code-block:: cpp

      #include <chrono>
      #include <memory>
      #include "rclcpp/rclcpp.hpp"
      #include "std_srvs/srv/empty.hpp"

      using namespace std::chrono_literals;

      namespace cb_group_demo
      {
      class DemoNode : public rclcpp::Node
      {
      public:
          DemoNode() : Node("client_node")
          {
              client_cb_group_ = nullptr;
              timer_cb_group_ = nullptr;
              client_ptr_ = this->create_client<std_srvs::srv::Empty>("test_service", rmw_qos_profile_services_default,
                                                                      client_cb_group_);
              timer_ptr_ = this->create_wall_timer(1s, std::bind(&DemoNode::timer_callback, this),
                                                  timer_cb_group_);
          }

      private:
          rclcpp::CallbackGroup::SharedPtr client_cb_group_;
          rclcpp::CallbackGroup::SharedPtr timer_cb_group_;
          rclcpp::Client<std_srvs::srv::Empty>::SharedPtr client_ptr_;
          rclcpp::TimerBase::SharedPtr timer_ptr_;

          void timer_callback()
          {
              RCLCPP_INFO(this->get_logger(), "Sending request");
              auto request = std::make_shared<std_srvs::srv::Empty::Request>();
              auto result_future = client_ptr_->async_send_request(request);
              std::future_status status = result_future.wait_for(10s);  // timeout to guarantee a graceful finish
              if (status == std::future_status::ready) {
                  RCLCPP_INFO(this->get_logger(), "Received response");
              }
          }
      };  // class DemoNode
      }   // namespace cb_group_demo

      int main(int argc, char* argv[])
      {
          rclcpp::init(argc, argv);
          auto client_node = std::make_shared<cb_group_demo::DemoNode>();
          rclcpp::executors::MultiThreadedExecutor executor;
          executor.add_node(client_node);

          RCLCPP_INFO(client_node->get_logger(), "Starting client node, shut down with CTRL-C");
          executor.spin();
          RCLCPP_INFO(client_node->get_logger(), "Keyboard interrupt, shutting down.\n");

          rclcpp::shutdown();
          return 0;
      }

  .. group-tab:: Python

    .. code-block:: python

      import rclpy
      from rclpy.executors import MultiThreadedExecutor
      from rclpy.callback_groups import MutuallyExclusiveCallbackGroup, ReentrantCallbackGroup
      from rclpy.node import Node
      from std_srvs.srv import Empty


      class CallbackGroupDemo(Node):
          def __init__(self):
              super().__init__('client_node')

              client_cb_group = None
              timer_cb_group = None
              self.client = self.create_client(Empty, 'test_service', callback_group=client_cb_group)
              self.call_timer = self.create_timer(1, self._timer_cb, callback_group=timer_cb_group)

          def _timer_cb(self):
              self.get_logger().info('Sending request')
              _ = self.client.call(Empty.Request())
              self.get_logger().info('Received response')


      if __name__ == '__main__':
          rclpy.init()
          node = CallbackGroupDemo()
          executor = MultiThreadedExecutor()
          executor.add_node(node)

          try:
              node.get_logger().info('Beginning client, shut down with CTRL-C')
              executor.spin()
          except KeyboardInterrupt:
              node.get_logger().info('Keyboard interrupt, shutting down.\n')
          node.destroy_node()
          rclpy.shutdown()

客户端节点的构造函数中包含用于设置服务客户端和定时器回调组的选项。上面的默认设置（两者均为 §nullptr§ / §None§）意味着定时器和客户端都会使用节点默认的互斥回调组。

问题
^^^^

由于我们使用 1 秒定时器调用服务，预期结果是每秒调用一次服务，客户端始终能够收到响应并打印 §Received response§。如果在终端中运行服务端和客户端节点，会得到以下输出。

.. tabs::

  .. group-tab:: 客户端

    .. code-block:: console

      [INFO] [1653034371.758739131] [client_node]: Starting client node, shut down with CTRL-C
      [INFO] [1653034372.755865649] [client_node]: Sending request
      ^C[INFO] [1653034398.161674869] [client_node]: Keyboard interrupt, shutting down.

  .. group-tab:: 服务端

    .. code-block:: console

      [INFO] [1653034355.308958238] [service_node]: Starting server node, shut down with CTRL-C
      [INFO] [1653034372.758197320] [service_node]: Received request, responding...
      ^C[INFO] [1653034416.021962246] [service_node]: Keyboard interrupt, shutting down.

结果发现，服务并没有持续调用。第一次调用的响应始终没有被客户端接收，随后客户端节点似乎卡住，不再发起后续调用。也就是说，执行过程发生了死锁！

原因在于，定时器回调和客户端使用了同一个互斥回调组（节点默认回调组）。发起服务调用时，客户端会将自己的回调组传递给 Future 对象（在 Python 版本中，该对象隐藏在 call 方法内部），而 Future 的完成回调必须执行，服务调用结果才能被获取。

但是，由于完成回调和定时器回调位于同一个互斥回调组，并且定时器回调仍在执行（等待服务调用结果），完成回调就无法执行。被阻塞的定时器回调也会阻止其自身再次执行，因此定时器不会第二次触发。

解决方案
^^^^^^^^

可以通过将定时器和客户端分配到不同的回调组来解决。将客户端节点构造函数中的前两行改为以下内容（其他代码保持不变）：

.. tabs::

  .. group-tab:: C++

    .. code-block:: cpp

      client_cb_group_ = this->create_callback_group(rclcpp::CallbackGroupType::MutuallyExclusive);
      timer_cb_group_ = this->create_callback_group(rclcpp::CallbackGroupType::MutuallyExclusive);

  .. group-tab:: Python

    .. code-block:: python

      client_cb_group = MutuallyExclusiveCallbackGroup()
      timer_cb_group = MutuallyExclusiveCallbackGroup()

现在就能得到预期结果：定时器会持续触发，每次服务调用都能正确得到结果。

.. tabs::

  .. group-tab:: 客户端

    .. code-block:: console

      [INFO] [1653067523.431731177] [client_node]: Starting client node, shut down with CTRL-C
      [INFO] [1653067524.431912821] [client_node]: Sending request
      [INFO] [1653067524.433230445] [client_node]: Received response
      [INFO] [1653067525.431869330] [client_node]: Sending request
      [INFO] [1653067525.432912803] [client_node]: Received response
      [INFO] [1653067526.431844726] [client_node]: Sending request
      [INFO] [1653067526.432893954] [client_node]: Received response
      [INFO] [1653067527.431828287] [client_node]: Sending request
      [INFO] [1653067527.432848369] [client_node]: Received response
      ^C[INFO] [1653067528.400052749] [client_node]: Keyboard interrupt, shutting down.

  .. group-tab:: 服务端

    .. code-block:: console

      [INFO] [1653067522.052866001] [service_node]: Starting server node, shut down with CTRL-C
      [INFO] [1653067524.432577720] [service_node]: Received request, responding...
      [INFO] [1653067525.432365009] [service_node]: Received request, responding...
      [INFO] [1653067526.432300261] [service_node]: Received request, responding...
      [INFO] [1653067527.432272441] [service_node]: Received request, responding...
      ^C[INFO] [1653034416.021962246] [service_node]: KeyboardInterrupt, shutting down.

可能有人会考虑：只要不使用节点默认回调组就足够了。事实并非如此：将默认组替换为另一个互斥回调组并不会改变结果。以下配置仍然会导致前面发现的死锁：

.. tabs::

  .. group-tab:: C++

    .. code-block:: cpp

      client_cb_group_ = this->create_callback_group(rclcpp::CallbackGroupType::MutuallyExclusive);
      timer_cb_group_ = client_cb_group_;

  .. group-tab:: Python

    .. code-block:: python

      client_cb_group = MutuallyExclusiveCallbackGroup()
      timer_cb_group = client_cb_group

实际上，本例中能够正常工作的准确条件是：定时器和客户端不能属于同一个互斥回调组。

因此，以下所有配置（以及其他一些配置）都能产生预期结果：定时器持续触发，服务调用正常完成。

.. tabs::

  .. group-tab:: C++

    .. code-block:: cpp

      client_cb_group_ = this->create_callback_group(rclcpp::CallbackGroupType::Reentrant);
      timer_cb_group_ = client_cb_group_;

    或

    .. code-block:: cpp

      client_cb_group_ = this->create_callback_group(rclcpp::CallbackGroupType::MutuallyExclusive);
      timer_cb_group_ = nullptr;

    或

    .. code-block:: cpp

      client_cb_group_ = nullptr;
      timer_cb_group_ = this->create_callback_group(rclcpp::CallbackGroupType::MutuallyExclusive);

    或

    .. code-block:: cpp

      client_cb_group_ = this->create_callback_group(rclcpp::CallbackGroupType::Reentrant);
      timer_cb_group_ = nullptr;

  .. group-tab:: Python

    .. code-block:: python

      client_cb_group = ReentrantCallbackGroup()
      timer_cb_group = client_cb_group

    或

    .. code-block:: python

      client_cb_group = MutuallyExclusiveCallbackGroup()
      timer_cb_group = None

    或

    .. code-block:: python

      client_cb_group = None
      timer_cb_group = MutuallyExclusiveCallbackGroup()

    或

    .. code-block:: python

      client_cb_group = ReentrantCallbackGroup()
      timer_cb_group = None
