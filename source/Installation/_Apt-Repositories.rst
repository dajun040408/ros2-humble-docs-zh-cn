你需要将 ROS 2 apt 软件仓库添加到系统中。

首先，确保已启用 `Ubuntu Universe 软件仓库 <https://help.ubuntu.com/community/Repositories/Ubuntu>`_。

.. code-block:: console

   $ sudo apt install software-properties-common
   $ sudo add-apt-repository universe

`ros-apt-source <https://github.com/ros-infrastructure/ros-apt-source/>`_ 软件包为不同 ROS 软件仓库提供密钥和 apt 软件源配置。

安装 ``ros2-apt-source`` 软件包后，系统会自动配置 ROS 2 软件仓库。当该软件包发布新版本时，软件仓库配置也会自动更新。

.. code-block:: console

   $ sudo apt update && sudo apt install curl -y
   $ export ROS_APT_SOURCE_VERSION=$(curl -fsSL -o /dev/null -w '%{url_effective}' https://github.com/ros-infrastructure/ros-apt-source/releases/latest | awk -F/ '{print $NF}')
   $ curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
   $ sudo dpkg -i /tmp/ros2-apt-source.deb
