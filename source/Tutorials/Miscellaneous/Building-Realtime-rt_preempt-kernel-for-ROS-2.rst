.. redirect-from::

    Building-Realtime-rt_preempt-kernel-for-ROS-2
    Tutorials/Building-Realtime-rt_preempt-kernel-for-ROS-2

构建实时 Linux 内核（社区贡献）
===============================

本教程以 Intel x86_64 平台上的 Ubuntu 20.04.1 全新安装为基础。原始示例使用内核 ``5.4.0-54-generic``，并安装稳定版 RT_PREEMPT 内核。构建内核至少需要 30 GB 可用磁盘空间。

请查看`Linux Foundation 实时 Linux 页面 <https://wiki.linuxfoundation.org/realtime/start>`_ 获取最新稳定版本。原始教程使用 ``5.4-rt`` 系列，对应补丁为 ``patch-5.4.78-rt44.patch.gz``。

准备源码
--------

创建工作目录：

.. code-block:: console

   $ mkdir ~/kernel
   $ cd ~/kernel

从 kernel.org 下载对应 Linux 内核源码，例如：

.. code-block:: console

   $ wget https://mirrors.edge.kernel.org/pub/linux/kernel/v5.x/linux-5.4.78.tar.gz
   $ tar -xzf linux-5.4.78.tar.gz

下载与内核版本匹配的 RT_PREEMPT 补丁：

.. code-block:: console

   $ wget http://cdn.kernel.org/pub/linux/kernel/projects/rt/5.4/older/patch-5.4.78-rt44.patch.gz
   $ gunzip patch-5.4.78-rt44.patch.gz

进入内核源码目录并应用补丁：

.. code-block:: console

   $ cd linux-5.4.78/
   $ patch -p1 < ../patch-5.4.78-rt44.patch

配置内核
--------

希望复用当前 Ubuntu 内核配置，可以复制现有配置文件：

.. code-block:: console

   $ cp /boot/config-5.4.0-54-generic .config

打开 Ubuntu 的 Software & Updates，在 Ubuntu Software 选项卡中勾选 Source code。

安装内核构建依赖：

.. code-block:: console

   $ sudo apt-get build-dep linux
   $ sudo apt-get install libncurses-dev flex bison openssl libssl-dev dkms libelf-dev libudev-dev libpci-dev libiberty-dev autoconf fakeroot

应用现有配置：

.. code-block:: console

   $ yes '' | make oldconfig

运行菜单配置：

.. code-block:: console

   $ make menuconfig

启用以下内核选项：

.. code-block:: text

   CONFIG_PREEMPT_RT
   General Setup -> Preemption Model -> Fully Preemptible Kernel (Real-Time)

   CONFIG_HIGH_RES_TIMERS
   General setup -> Timers subsystem -> High Resolution Timer Support

   CONFIG_NO_HZ_FULL
   General setup -> Timers subsystem -> Full dynticks system (tickless)

   CONFIG_HZ_1000
   Processor type and features -> Timer frequency -> 1000 HZ

   CPU_FREQ_DEFAULT_GOV_PERFORMANCE
   Power management and ACPI options -> CPU Frequency scaling -> performance

保存并退出 menuconfig。

构建内核
--------

构建过程需要较长时间，现代 CPU 通常需要约 10 到 30 分钟：

.. code-block:: console

   $ make -j $(nproc) deb-pkg

构建完成后检查生成的 deb 软件包：

.. code-block:: console

   $ ls ../*deb

安装生成的软件包：

.. code-block:: console

   $ sudo dpkg -i ../*.deb

重启系统：

.. code-block:: console

   $ sudo reboot

验证实时内核
------------

重启后检查内核版本：

.. code-block:: console

   $ uname -a

输出中应包含新安装的 RT_PREEMPT 内核版本和 PREEMPT_RT 标识。

.. warning::

   本教程使用较旧的 Ubuntu 和 Linux 内核版本作为示例。实际部署时应根据当前系统、硬件和 ROS 2 发行版选择匹配的内核与补丁版本。构建和安装内核存在系统启动风险，建议先备份重要数据并保留可回退的内核。
