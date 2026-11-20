确保系统使用支持 ``UTF-8`` 的区域语言。如果你使用的是精简环境（例如 Docker 容器），当前区域语言可能非常精简，例如 ``POSIX``。

我们使用以下设置进行测试。如果你使用其他支持 UTF-8 的区域语言，通常也没有问题。

.. code-block:: console

   $ locale  # 检查是否支持 UTF-8

   $ sudo apt update && sudo apt install locales
   $ sudo locale-gen en_US en_US.UTF-8
   $ sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
   $ export LANG=en_US.UTF-8

   $ locale  # 验证设置
