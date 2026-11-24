.. redirect-from::

  Guides/Overriding-QoS-Policies-For-Recording-And-Playback
  Tutorials/Ros2bag/Overriding-QoS-Policies-For-Recording-And-Playback

.. _ROS2Bag-QoS-Override:

rosbag2：覆盖 QoS 策略
======================

**目标：** 覆盖 rosbag2 在录制和回放时使用的 QoS 配置文件设置。

.. contents:: 目录
   :depth: 2
   :local:

背景知识
--------

ROS 2 引入 DDS 后，在录制和回放数据时，需要考虑发布者/订阅者节点之间的服务质量（QoS）兼容性。有关 QoS 工作原理的更多信息，请参阅 :doc:`此处 <../Concepts/Intermediate/About-Quality-of-Service-Settings>`。对于本指南，只需知道可靠性（Reliability）和持久性（Durability）策略会影响发布者和订阅者是否兼容，以及能否相互接收数据。

rosbag2 在录制/回放话题数据时，会调整其请求/提供的 QoS 配置文件，以避免消息丢失。回放期间，rosbag2 还会尝试保留话题最初提供的策略。

某些情况下，可能需要显式指定 QoS 配置文件设置，rosbag2 才能录制/回放话题。可以通过命令行的 ``--qos-profile-overrides-path`` 标志指定这些 QoS 配置覆盖项。

使用 QoS 覆盖项
---------------

QoS 覆盖配置的 YAML 结构是一个字典，其中包含话题名称以及每个 QoS 策略对应的键值对：

.. code-block:: yaml

    topic_name: str
      qos_policy_name: str
      ...
      qos_duration: object
        sec: int
        nsec: int

如果未指定某项策略的值，则会回退到 rosbag2 使用的默认值。如果指定 ``deadline`` 或 ``lifespan`` 等基于 Duration 的策略，则必须同时指定秒和纳秒。

策略值由策略对应的简写键决定。可以通过 ``ros2topic`` 命令（例如 ``ros2 topic pub --help``）查看这些键。下面列出所有可用值，供参考：

.. code-block:: yaml

    history: [keep_all, keep_last]
    depth: int
    reliability: [system_default, reliable, best_effort, unknown]
    durability: [system_default, transient_local, volatile, unknown]
    deadline:
      sec: int
      nsec: int
    lifespan:
      sec: int
      nsec: int
    liveliness: [system_default, automatic, manual_by_topic, unknown]
    liveliness_lease_duration:
      sec: int
      nsec: int
    avoid_ros_namespace_conventions: [true, false]

示例
----

假设话题 ``/talker`` 提供 ``transient_local`` 持久性策略，而 ROS 2 发布者默认请求 ``volatile`` 持久性策略：

.. code-block:: console

    $ ros2 topic pub -r 0.1 --qos-durability transient_local /talker std_msgs/String "data: Hello World"

为了让 rosbag2 能够录制该话题的数据，需要为这个特定话题覆盖录制策略，例如：

.. code-block:: yaml

    # durability_override.yaml
    /talker:
      durability: transient_local
      history: keep_all

然后通过命令行调用：

.. code-block:: console

    $ ros2 bag record -a -o my_bag --qos-profile-overrides-path durability_override.yaml

如果希望回放 bag 文件时使用不同的 Reliability 策略，可以这样指定：

.. code-block:: yaml

    # reliability_override.yaml
    /talker:
      reliability: best_effort
      history: keep_all

然后通过命令行调用：

.. code-block:: console

    $ ros2 bag play --qos-profile-overrides-path reliability_override.yaml my_bag

可以使用 ``ros2 topic`` 查看结果：

.. code-block:: console

    $ ros2 topic echo --qos-reliability best_effort /talker std_msgs/String
