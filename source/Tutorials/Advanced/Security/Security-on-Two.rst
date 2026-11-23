.. redirect-from::

    Tutorials/Security/Security-on-Two

.. _Security-on-Two:

确保多台计算机之间的通信安全
============================

**目标：** 让两台不同的计算机安全通信。

**教程级别：** 高级

**预计时间：** 5 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景知识
--------

前面的教程使用同一台计算机上的两个 ROS 节点，所有网络通信都通过 localhost 接口进行。现在将场景扩展到多台计算机，以便更直观地理解身份验证和加密的价值。

假设上一示例中创建密钥库的计算机主机名为 `Alice`，我们还希望使用另一台主机名为 `Bob` 的计算机运行多机 `talker/listener` 示例。为了让 SROS 2 能够验证并加密传输内容，需要将部分密钥从 `Alice` 复制到 `Bob`。

创建第二个密钥库
----------------

首先，在 `Bob` 上创建一个空密钥库；实际上，密钥库只是一个空目录：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ ssh Bob
      $ mkdir ~/sros2_demo
      $ exit

  .. group-tab:: macOS

    .. code-block:: console

      $ ssh Bob
      $ mkdir ~/sros2_demo
      $ exit

  .. group-tab:: Windows

    .. code-block:: console

      $ ssh Bob
      $ md C:\dev\ros2\sros2_demo
      $ exit

复制文件
--------

接下来，将 `talker` 程序的密钥和证书从 `Alice` 复制到 `Bob`。由于密钥只是文本文件，可以使用 `scp` 进行复制。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      $ cd ~/sros2_demo/demo_keystore
      $ scp -r talker USERNAME@Bob:~/sros2_demo/demo_keystore

  .. group-tab:: macOS

    .. code-block:: console

      $ cd ~/sros2_demo/demo_keystore
      $ scp -r talker USERNAME@Bob:~/sros2_demo/demo_keystore

  .. group-tab:: Windows

    .. code-block:: console

      $ cd C:\dev\ros2\sros2_demo\demo_keystore
      $ scp -r talker USERNAME@Bob:/dev/ros2/sros2_demo/demo_keystore

.. warning::

  请注意，在本例中，整个密钥库会在不同计算机之间共享，这可能并非理想做法，因为它会带来安全风险。更多信息请参阅 :doc:`部署指南 <Deployment-Guidelines>`。

由于这里只是复制少量文本文件，因此过程会很快。现在可以运行多机 talker/listener 示例了。

启动节点
--------

环境配置完成后，在 `Bob` 上运行 talker：

.. code-block:: console

  $ ros2 run demo_nodes_cpp talker --ros-args --enclave /talker_listener/talker

然后在 `Alice` 上启动 listener：

.. code-block:: console

  $ ros2 run demo_nodes_py listener --ros-args --enclave /talker_listener/listener

此时，`Alice` 将接收到来自 `Bob` 的加密消息。

两台计算机成功通过加密和身份验证进行通信后，就可以使用相同流程将更多计算机添加到 ROS 计算图中。
