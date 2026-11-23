.. redirect-from::

  Guides/Cross-compilation
  Tutorials/Cross-compilation

交叉编译
========

`cross_compile <https://github.com/ros-tooling/cross_compile>`_ 工具已不再受支持。

交叉编译的替代方案是使用 `docker buildx <https://github.com/docker/buildx#building-multi-platform-images>`_ 构建多平台 Docker 镜像，例如：

.. code-block:: console

   docker buildx build --platform linux/amd64,linux/arm64 .
