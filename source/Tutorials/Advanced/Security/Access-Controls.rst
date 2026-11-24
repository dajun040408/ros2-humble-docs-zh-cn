.. redirect-from::

    Tutorials/Security/Access-Controls

.. _Access-Controls:

设置访问控制
============

**目标：** 限制节点可以使用的话题。

**教程级别：** 高级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

权限配置具有很高的灵活性，可以控制 ROS 计算图中的许多行为。本教程演示一种策略：只允许节点在默认 chatter 话题上发布消息。这会阻止启动 listener 时重映射话题，也会阻止将同一安全 enclave 用于其他用途。

要强制执行该策略，需要更新 permissions.xml 文件并重新签名，然后再启动节点。可以手动修改权限文件，也可以使用 XML 模板。

修改 permissions.xml
^^^^^^^^^^^^^^^^^^^^

首先备份权限文件，并打开 permissions.xml 编辑：

.. code-block:: console

  $ cd ~/sros2_demo/demo_keys/enclaves/talker_listener/talker
  $ mv permissions.p7s permissions.p7s~
  $ mv permissions.xml permissions.xml~
  $ vi permissions.xml

我们将修改 publish 和 subscribe 对应的 allow_rule。该 XML 文件中的话题使用 DDS 命名格式，而不是 ROS 名称。ROS 与 DDS 话题名称之间的映射关系，请参阅`话题和服务名称设计文档 <https://design.ros2.org/articles/topic_and_service_names.html#mapping-of-ros-2-topic-and-service-names-to-dds-concepts>`_。

将以下 XML 内容粘贴到 permissions.xml，保存并退出编辑器。这里将 ROS 话题 chatter 和 rosout 分别映射为 DDS 话题 rt/chatter 和 rt/rosout：

.. code-block:: xml
  :emphasize-lines: 15,16,17,18,23,24

  <dds xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.omg.org/spec/DDS-SECURITY/20170901/omg_shared_ca_permissions.xsd">
    <permissions>
      <grant name="/talker_listener/talker">
        <subject_name>CN=/talker_listener/talker</subject_name>
        <validity>
          <not_before>2021-06-01T16:57:53</not_before>
          <not_after>2031-05-31T16:57:53</not_after>
        </validity>
        <allow_rule>
          <domains>
            <id>0</id>
          </domains>
          <publish>
            <topics>
              <topic>rt/chatter</topic>
              <topic>rt/rosout</topic>
              <topic>rt/parameter_events</topic>
              <topic>*/talker/*</topic>
            </topics>
          </publish>
          <subscribe>
            <topics>
              <topic>rt/parameter_events</topic>
              <topic>*/talker/*</topic>
            </topics>
          </subscribe>
        </allow_rule>
        <allow_rule>
          <domains>
            <id>0</id>
          </domains>
          <publish>
            <topics>
              <topic>ros_discovery_info</topic>
            </topics>
          </publish>
          <subscribe>
            <topics>
              <topic>ros_discovery_info</topic>
            </topics>
          </subscribe>
        </allow_rule>
        <default>DENY</default>
      </grant>
    </permissions>
  </dds>

该策略允许 talker 在 chatter 和 rosout 话题上发布消息，同时包含 talker 管理参数所需的发布和订阅权限。发现相关权限保持原模板不变。

签署策略文件
^^^^^^^^^^^^

使用以下命令，根据更新后的 XML 文件生成新的 S/MIME 签名策略文件 permissions.p7s。该文件必须使用 Permissions CA 证书签名，因此需要能够访问 Permissions CA 私钥。如果私钥受到保护，则可能需要根据安全计划执行额外步骤来解锁和使用它。

.. code-block:: console

  $ openssl smime -sign -text -in permissions.xml -out permissions.p7s \
    --signer permissions_ca.cert.pem \
    -inkey ~/sros2_demo/demo_keys/private/permissions_ca.key.pem

启动节点
^^^^^^^^

更新权限后，可以使用之前教程中的命令成功启动节点：

.. code-block:: console

  $ ros2 run demo_nodes_cpp talker --ros-args --enclave /talker_listener/talker

但是，如果尝试重映射 chatter 话题，节点将无法启动（需要将 ROS_SECURITY_STRATEGY 设置为 Enforce）：

.. code-block:: console

  $ ros2 run demo_nodes_cpp talker --ros-args --enclave /talker_listener/talker \
    --remap chatter:=not_chatter

使用模板
^^^^^^^^

安全策略可能很快变得复杂，因此 sros2 工具支持通过模板创建策略。这里使用 sros2 仓库提供的`示例策略文件 <https://github.com/ros2/sros2/blob/{REPOS_FILE_BRANCH}/sros2/test/policies/sample.policy.xml#L1>`_。

本例为 talker 和 listener 创建策略，只允许它们使用 chatter 话题。首先下载包含示例策略文件的 sros2 仓库：

.. code-block:: console

  $ git clone https://github.com/ros2/sros2.git /tmp/sros2

然后使用 create_permission 子命令，并指定示例策略，生成 XML 权限文件：

.. code-block:: console

  $ ros2 security create_permission demo_keystore \
    /talker_listener/talker \
    /tmp/sros2/sros2/test/policies/sample.policy.xml
  $ ros2 security create_permission demo_keystore \
    /talker_listener/listener \
    /tmp/sros2/sros2/test/policies/sample.policy.xml

这些权限文件只允许节点在 chatter 话题上发布或订阅，同时允许参数通信所需的操作。

在一个已按照前面安全教程启用安全功能的终端中，运行 talker 演示：

.. code-block:: console

  $ ros2 run demo_nodes_cpp talker --ros-args -e /talker_listener/talker

在另一个终端中运行 listener：

.. code-block:: console

  $ ros2 run demo_nodes_py listener --ros-args -e /talker_listener/listener

此时 talker 和 listener 将通过显式访问控制列表进行安全通信。但是，如果尝试让 listener 订阅 chatter 以外的话题，则会失败：

.. code-block:: console

  $ ros2 run demo_nodes_py listener --ros-args --enclave /talker_listener/listener \
    --remap chatter:=not_chatter
