.. redirect-from::

   Concepts/About-Cross-Compilation

交叉编译
========

.. contents:: 目录
   :local:

概述
----

Open Robotics 为多个平台提供预构建的 ROS 2 软件包，但仍有许多开发者出于不同原因依赖 `交叉编译 <https://en.wikipedia.org/wiki/Cross_compiler>`__，例如：

* 开发机器与目标系统不一致。
* 需要针对特定核心架构调整构建参数（例如为 Raspberry Pi 3 构建时设置 ``-mcpu=cortex-a53 -mfpu=neon-fp-armv8``）。
* 目标文件系统不属于 Open Robotics 发布的预构建镜像所支持的文件系统。

交叉编译如何工作？
------------------

交叉编译简单软件（例如不依赖外部库的软件）相对容易，只需要使用交叉编译工具链替代本机工具链即可。

但以下因素会使这一过程变得更加复杂：

* 正在构建的软件必须支持目标架构。架构相关代码必须正确隔离，并在构建时根据目标架构启用，例如汇编代码。
* 在交叉编译使用这些依赖的软件之前，所有依赖项（例如库）都必须已经存在，可以是预构建的软件包，也可以是交叉编译得到的软件包。
* 构建软件栈（而不是独立软件）时，如果使用 colcon 等构建工具，构建工具需要提供机制，使开发者能够对软件栈中每个软件所使用的底层构建系统启用交叉编译。

替代方案
--------

交叉编译的一种替代方案是使用 ``docker buildx`` `构建多平台 Docker 镜像 <https://github.com/docker/buildx#building-multi-platform-images>`__。
