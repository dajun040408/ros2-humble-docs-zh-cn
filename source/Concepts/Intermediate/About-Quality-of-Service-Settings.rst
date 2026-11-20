.. redirect-from::

    About-Quality-of-Service-Settings
    Concepts/About-Quality-of-Service-Settings

服务质量（QoS）设置
===================

.. contents:: 目录
   :local:

概述
----

ROS 2 提供了丰富的服务质量（Quality of Service，QoS）策略，可以用来调整节点之间的通信行为。

通过选择合适的 QoS 策略组合，ROS 2 的通信可靠性既可以接近 TCP，也可以像 UDP 一样采用尽力而为（best effort）方式，并且可以在两者之间配置许多不同状态。

与主要支持 TCP 的 ROS 1 不同，ROS 2 可以利用底层 DDS 传输机制的灵活性。例如，在容易丢包的无线网络环境中，尽力而为策略可能更合适；而在实时计算系统中，则需要选择合适的 QoS 配置来满足截止时间要求。

一组 QoS“策略（policies）”组合起来构成一个 QoS“配置（profile）”。考虑到为不同场景选择合适 QoS 策略的复杂性，ROS 2 为常见用例（例如传感器数据）提供了预定义 QoS 配置。同时，开发者也可以灵活地控制这些 QoS 配置中的具体策略。

QoS 配置可以分别指定给发布者、订阅者、服务端和客户端。上述每个实体实例都可以独立应用 QoS 配置；但如果使用了不同配置，它们之间可能不兼容，从而导致消息无法传递。

.. _about_qos_policies:

QoS 策略
--------

当前基础 QoS 配置包含以下策略设置：

* 历史记录（History）

  * *Keep last（保留最近 N 条）*：只存储最多 N 条样本，N 可通过队列深度选项配置。
  * *Keep all（全部保留）*：存储所有样本，但仍受底层中间件配置的资源限制约束。

* 深度（Depth）

  * *队列大小（Queue size）*：只有在历史记录策略设置为 ``keep last`` 时才生效。

* 可靠性（Reliability）

  * *Best effort（尽力而为）*：尝试传递样本，但在网络状况不佳时可能丢失样本。
  * *Reliable（可靠）*：保证样本能够送达，必要时可能进行多次重试。

* 持久性（Durability）

  * *Transient local（本地暂存）*：由发布者负责持久保存样本，以便“后加入”的订阅者能够接收。
  * *Volatile（易失）*：不尝试持久保存样本。

* 截止时间（Deadline）

  * *Duration（持续时间）*：同一话题连续两条消息发布之间预期的最大时间间隔。

* 生命周期（Lifespan）

  * *Duration（持续时间）*：从消息发布到消息接收之间允许的最长时间。超过该时间后，消息会被视为过期并静默丢弃，实际上不会被接收。

* 活跃性（Liveliness）

  * *Automatic（自动）*：只要节点的任意一个发布者发布了消息，系统就会认为该节点的所有发布者在接下来的一个“租约时长”内仍然存活。
  * *Manual by topic（按话题手动声明）*：如果发布者通过发布者 API 手动声明自身仍然存活，系统就会认为该发布者在接下来的一个“租约时长”内仍然存活。

* 租约时长（Lease Duration）

  * *Duration（持续时间）*：发布者必须声明自身存活的最大时间间隔。超过该时间后，系统会认为发布者已失去活跃性（失去活跃性可能意味着发生故障）。

对于非持续时间类型的策略，还可以选择“system default（系统默认）”，即使用底层中间件的默认值。

对于持续时间类型的策略，也有“default（默认）”选项，表示未指定持续时间；底层中间件通常会将其解释为无限长的持续时间。

与 ROS 1 的比较
^^^^^^^^^^^^^^^

ROS 2 中的“历史记录（history）”和“深度（depth）”策略组合起来，提供了与 ROS 1 队列大小（queue size）类似的功能。

ROS 2 的“可靠性（reliability）”策略与 ROS 1 中的 UDPROS（仅在 ``roscpp`` 中支持，对应尽力而为）或 TCPROS（ROS 1 默认方式，对应可靠传输）类似。不过需要注意，即使 ROS 2 选择可靠策略，底层仍然使用 UDP 实现，因此在适当情况下可以支持多播。

ROS 2 的“持久性（durability）”策略中的“transient local”，结合任意深度设置，可以提供类似“锁存（latching）”发布者的功能。

ROS 2 中其余策略在 ROS 1 中没有直接对应的功能，因此在这方面 ROS 2 提供了更丰富的能力。未来 ROS 2 还可能提供更多 QoS 策略。

QoS 配置
--------

QoS 配置使开发者能够专注于应用本身，而不必逐一考虑所有可能的 QoS 设置。一个 QoS 配置定义了一组预期能够协同工作的策略，用于满足特定使用场景。

目前定义的 QoS 配置如下：

* 发布者和订阅者的默认 QoS 设置

  为了让从 ROS 1 迁移到 ROS 2 更加容易，默认情况下希望采用相似的网络行为。因此，ROS 2 中发布者和订阅者默认使用以下设置：历史记录为 ``keep last``，队列大小为 10；可靠性为 ``reliable``；持久性为 ``volatile``；活跃性为 ``system default``。截止时间、生命周期和租约时长也都设置为 ``default``。

* 服务（Services）

  与发布者和订阅者类似，服务采用可靠传输。服务尤其需要使用易失持久性（volatile durability），否则重启后的服务端可能收到过期请求。虽然客户端可以避免接收多个响应，但服务端无法避免处理过期请求所产生的副作用。

* 传感器数据（Sensor data）

  对于传感器数据，大多数情况下，及时收到读数比确保每一条数据都送达更加重要。也就是说，开发者希望尽快获得最新样本，即使可能因此丢失部分样本。为此，传感器数据配置采用尽力而为可靠性，并使用较小的队列大小。

* 参数（Parameters）

  ROS 2 参数基于服务实现，因此采用类似的 QoS 配置。不同之处在于，参数使用更大的队列深度，以便在参数客户端暂时无法连接参数服务端等情况下，请求不容易丢失。

* 系统默认（System default）

  对所有策略都使用 RMW 实现提供的默认值。不同 RMW 实现的默认值可能不同。

`点击此处 <https://github.com/ros2/rmw/blob/{REPOS_FILE_BRANCH}/rmw/include/rmw/qos_profiles.h>`__ 查看上述配置实际使用的具体策略。根据社区反馈，这些配置中的设置可能会继续调整。

.. _about-qos_compatibilities:

QoS 兼容性
----------

**注意：** 本节以发布者和订阅者为例进行说明，但相同内容也适用于服务端和客户端。

发布者和订阅者可以分别配置 QoS 配置。只有当发布者与订阅者的 QoS 配置相互兼容时，二者之间才会建立连接。

QoS 配置兼容性采用“请求与提供（Request vs Offered）”模型判断。订阅者会*请求（request）*一个 QoS 配置，表示它愿意接受的“最低质量”；发布者会*提供（offer）*一个 QoS 配置，表示它能够提供的“最高质量”。只有当请求 QoS 配置中的每项策略都不比提供的 QoS 配置更加严格时，双方才会建立连接。

即使多个订阅者请求的 QoS 配置不同，它们也可以同时连接到同一个发布者。发布者与订阅者之间的兼容性不受其他发布者或订阅者是否存在的影响。

以下表格展示了不同策略设置之间的兼容性及其结果：

*可靠性 QoS 策略的兼容性：*

.. list-table::
   :header-rows: 1

   * - 发布者
     - 订阅者
     - 是否兼容
   * - Best effort
     - Best effort
     - 是
   * - Best effort
     - Reliable
     - 否
   * - Reliable
     - Best effort
     - 是
   * - Reliable
     - Reliable
     - 是

*持久性 QoS 策略的兼容性：*

.. list-table::
   :header-rows: 1

   * - 发布者
     - 订阅者
     - 是否兼容
     - 结果
   * - Volatile
     - Volatile
     - 是
     - 仅接收新消息
   * - Volatile
     - Transient local
     - 否
     - 无法通信
   * - Transient local
     - Volatile
     - 是
     - 仅接收新消息
   * - Transient local
     - Transient local
     - 是
     - 接收新消息和历史消息

如果希望实现类似“锁存”的话题，使后加入的订阅者也能看到之前发布的消息，则发布者和订阅者都必须使用 ``Transient Local``。

*截止时间 QoS 策略的兼容性：*

假设 *x* 和 *y* 是任意有效的持续时间值。

.. list-table::
   :header-rows: 1

   * - 发布者
     - 订阅者
     - 是否兼容
   * - Default
     - Default
     - 是
   * - Default
     - *x*
     - 否
   * - *x*
     - Default
     - 是
   * - *x*
     - *x*
     - 是
   * - *x*
     - *y*（其中 *y* > *x*）
     - 是
   * - *x*
     - *y*（其中 *y* < *x*）
     - 否

*活跃性 QoS 策略的兼容性：*

.. list-table::
   :header-rows: 1

   * - 发布者
     - 订阅者
     - 是否兼容
   * - Automatic
     - Automatic
     - 是
   * - Automatic
     - Manual by topic
     - 否
   * - Manual by topic
     - Automatic
     - 是
   * - Manual by topic
     - Manual by topic
     - 是

*租约时长 QoS 策略的兼容性：*

假设 *x* 和 *y* 是任意有效的持续时间值。

.. list-table::
   :header-rows: 1

   * - 发布者
     - 订阅者
     - 是否兼容
   * - Default
     - Default
     - 是
   * - Default
     - *x*
     - 否
   * - *x*
     - Default
     - 是
   * - *x*
     - *x*
     - 是
   * - *x*
     - *y*（其中 *y* > *x*）
     - 是
   * - *x*
     - *y*（其中 *y* < *x*）
     - 否

要建立连接，所有影响兼容性的策略都必须兼容。例如，即使请求和提供的 QoS 配置在可靠性策略上兼容，只要它们的持久性策略不兼容，双方仍然无法建立连接。

连接未建立时，发布者和订阅者之间不会传递任何消息。ROS 2 提供了检测这种情况的机制，后续章节会对此进行介绍。

与 ROS 1 的比较
^^^^^^^^^^^^^^^

在 ROS 1 中，只要发布者和订阅者在同一话题上使用相同的消息类型，就会建立连接。ROS 2 引入了请求 QoS 配置与提供 QoS 配置可能不兼容的情况，这是使用 ROS 2 时需要特别注意的新概念。

.. _about-qos_qos-events:

QoS 事件
--------

某些 QoS 策略可能会触发相关事件。开发者可以为每个发布者和订阅者提供回调函数。当这些 QoS 事件发生时，回调函数会被触发，开发者可以按照自己的需求处理事件，方式类似于处理话题收到的消息。

开发者可以订阅以下与发布者相关的 QoS 事件：

* Offered deadline missed（提供的截止时间未满足）

  发布者未能在截止时间 QoS 策略设定的预期时间内发布消息。

* Liveliness lost（活跃性丢失）

  发布者未能在租约时长内声明自身仍然存活。

* Offered incompatible QoS（提供的 QoS 不兼容）

  发布者发现同一话题上存在订阅者，而该订阅者请求的 QoS 配置超出了发布者所提供配置能够满足的范围，因此发布者与该订阅者无法建立连接。

开发者可以订阅以下与订阅者相关的 QoS 事件：

* Requested deadline missed（请求的截止时间未满足）

  订阅者未能在截止时间 QoS 策略设定的预期时间内收到消息。

* Liveliness changed（活跃性发生变化）

  订阅者发现其订阅话题上的一个或多个发布者未能在租约时长内声明自身仍然存活。

* Requested incompatible QoS（请求的 QoS 不兼容）

  订阅者发现同一话题上存在发布者，而该发布者提供的 QoS 配置无法满足订阅者请求的 QoS 配置，因此订阅者与该发布者无法建立连接。
