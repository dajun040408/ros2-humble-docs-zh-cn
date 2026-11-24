Python 功能包迁移示例
==================================

本指南演示如何将一个示例 Python 功能包从 ROS 1 迁移到 ROS 2。

.. contents:: 目录
   :depth: 2
   :local:

前置条件
-------------

你需要一个可正常工作的 ROS 2 安装环境，例如 :doc:`ROS {DISTRO} <../../Installation>`。

ROS 1 代码
--------------

本指南不会使用 `catkin <https://index.ros.org/p/catkin/>`__，因此不需要可运行的 ROS 1 安装环境。这里将改用 ROS 2 的构建工具 `Colcon <https://colcon.readthedocs.io/>`__。

本节提供一个 ROS 1 Python 功能包的代码。该功能包名为 ``talker_py``，其中包含一个名为 ``talker_py_node`` 的节点。为了便于后续运行 Colcon，以下步骤会指导你在 `Colcon 工作空间 <https://colcon.readthedocs.io/en/released/user/what-is-a-workspace.html>`__ 中创建该功能包。

首先，在 ``~/ros2_talker_py`` 创建一个目录，作为 Colcon 工作空间的根目录。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

        $ mkdir -p ~/ros2_talker_py/src

  .. group-tab:: macOS

    .. code-block:: console

        $ mkdir -p ~/ros2_talker_py/src

  .. group-tab:: Windows

    .. code-block:: console

        $ md \ros2_talker_py\src

接下来，为 ROS 1 功能包创建所需文件。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

        $ cd ~/ros2_talker_py
        $ mkdir -p src/talker_py/src/talker_py
        $ mkdir -p src/talker_py/scripts
        $ touch src/talker_py/package.xml
        $ touch src/talker_py/CMakeLists.txt
        $ touch src/talker_py/src/talker_py/__init__.py
        $ touch src/talker_py/scripts/talker_py_node
        $ touch src/talker_py/setup.py

  .. group-tab:: macOS

    .. code-block:: console

        $ cd ~/ros2_talker_py
        $ mkdir -p src/talker_py/src/talker_py
        $ mkdir -p src/talker_py/scripts
        $ touch src/talker_py/package.xml
        $ touch src/talker_py/CMakeLists.txt
        $ touch src/talker_py/src/talker_py/__init__.py
        $ touch src/talker_py/scripts/talker_py_node
        $ touch src/talker_py/setup.py

  .. group-tab:: Windows

    .. code-block:: console

        $ cd \ros2_talker_py
        $ md src\talker_py\src\talker_py
        $ md src\talker_py\scripts
        $ type nul > src\talker_py\package.xml
        $ type nul > src\talker_py\CMakeLists.txt
        $ type nul > src\talker_py\src\talker_py\__init__.py
        $ type nul > src\talker_py\scripts/talker_py_node
        $ type nul > src\talker_py\setup.py

将以下内容分别写入各个文件。

``src/talker_py/package.xml``:

.. code-block:: xml

    <?xml version="1.0"?>
    <?xml-model href="http://download.ros.org/schema/package_format2.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
    <package format="2">
        <name>talker_py</name>
        <version>1.0.0</version>
        <description>The talker_py package</description>
        <maintainer email="gerkey@example.com">Brian Gerkey</maintainer>
        <license>BSD</license>

        <buildtool_depend>catkin</buildtool_depend>

        <depend>rospy</depend>
        <depend>std_msgs</depend>
    </package>

``src/talker_py/CMakeLists.txt``:

.. code-block:: cmake

    cmake_minimum_required(VERSION 3.0.2)
    project(talker_py)

    find_package(catkin REQUIRED)

    catkin_python_setup()

    catkin_package()

    catkin_install_python(PROGRAMS
        scripts/talker_py_node
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
    )

``src/talker/src/talker_py/__init__.py``:

.. code-block:: Python

    import rospy
    from std_msgs.msg import String

    def main():
        rospy.init_node('talker')
        pub = rospy.Publisher('chatter', String, queue_size=10)
        rate = rospy.Rate(10)  # 10hz
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()

``src/talker_py/scripts/talker_py_node``:

.. code-block:: Python

    #!/usr/bin/env python

    import talker_py

    if __name__ == '__main__':
        talker_py.main()

``src/talker_py/setup.py``:

.. code-block:: Python

    from setuptools import setup
    from catkin_pkg.python_setup import generate_distutils_setup

    setup_args = generate_distutils_setup(
        packages=['talker_py'],
        package_dir={'': 'src'}
    )

    setup(**setup_args)

至此，ROS 1 Python 功能包已完整创建。

迁移 ``package.xml``
---------------------------

将功能包迁移到 ROS 2 时，应先迁移构建系统文件，这样就可以在迁移过程中通过构建和运行代码来检查结果。始终从迁移 ``package.xml`` 开始。

首先，ROS 2 不使用 ``catkin``，因此请删除对它的 ``<buildtool_depend>`` 声明。

.. code-block::

    <!-- delete this -->
    <buildtool_depend>catkin</buildtool_depend>


其次，ROS 2 使用 ``rclpy`` 替代 ``rospy``，请删除对 ``rospy`` 的依赖。

.. code-block::

    <!-- Delete this -->
    <depend>rospy</depend>


将其替换为对 ``rclpy`` 的新依赖。

.. code-block:: xml

    <depend>rclpy</depend>

添加 ``<export>`` 节，告知 ROS 2 构建工具 `Colcon <https://colcon.readthedocs.io/>`__，该功能包是 ``ament_python`` 类型，而不是 ``catkin`` 类型。

.. code-block:: xml

     <export>
       <build_type>ament_python</build_type>
     </export>


至此，``package.xml`` 已完成迁移，其内容应如下所示：

.. code-block:: xml

    <?xml version="1.0"?>
    <?xml-model href="http://download.ros.org/schema/package_format2.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
    <package format="2">
        <name>talker_py</name>
        <version>1.0.0</version>
        <description>The talker_py package</description>
        <maintainer email="gerkey@example.com">Brian Gerkey</maintainer>
        <license>BSD</license>

        <depend>rclpy</depend>
        <depend>std_msgs</depend>

        <export>
            <build_type>ament_python</build_type>
        </export>
    </package>

删除 ``CMakeLists.txt``
-----------------------------

ROS 2 的 Python 功能包不使用 CMake，因此请删除 ``CMakeLists.txt``。

迁移 ``setup.py``
------------------------

``setup.py`` 中传递给 ``setup()`` 的参数不能再通过 ``catkin_pkg`` 自动生成。你必须手动传入这些参数，因此其中部分信息会与 ``package.xml`` 重复。

首先，删除从 ``catkin_pkg`` 导入的语句。

.. code-block::

    # Delete this
    from catkin_pkg.python_setup import generate_distutils_setup

将传递给 ``generate_distutils_setup()`` 的所有参数移至 ``setup()`` 调用中，然后添加 ``install_requires`` 和 ``zip_safe`` 参数。``setup()`` 调用应如下所示：

.. code-block:: Python

    setup(
        packages=['talker_py'],
        package_dir={'': 'src'},
        install_requires=['setuptools'],
        zip_safe=True,
    )

删除 ``generate_distutils_setup()`` 调用。

.. code-block::

    # Delete this
    setup_args = generate_distutils_setup(
        packages=['talker_py'],
        package_dir={'': 'src'}
    )

``setup()`` 调用还需要从 ``package.xml`` 复制一些 `附加元数据 <https://docs.python.org/3.11/distutils/setupscript.html#additional-meta-data>`__：

* 通过 ``name`` 参数指定功能包名称。
* 通过 ``version`` 参数指定功能包版本。
* 通过 ``maintainer`` 和 ``maintainer_email`` 参数指定维护者及其邮箱。
* 通过 ``description`` 参数指定描述。
* 通过 ``license`` 参数指定许可证。

功能包名称将在多个位置使用。请在 ``setup()`` 调用之前创建一个名为 ``package_name`` 的变量。

.. code-block:: Python

    package_name = 'talker_py'

将其余信息复制到 ``setup.py`` 中 ``setup()`` 的参数里。调用内容应如下所示：

.. code-block:: Python

    setup(
        name=package_name,
        version='1.0.0',
        install_requires=['setuptools'],
        zip_safe=True,
        packages=['talker_py'],
        package_dir={'': 'src'},
        maintainer='Brian Gerkey',
        maintainer_email='gerkey@example.com',
        description='The talker_py package',
        license='BSD',
    )


ROS 2 功能包必须安装两个数据文件：

* 一个 ``package.xml`` 文件。
* 一个功能包标记文件。

功能包已经包含 ``package.xml``，其中描述了功能包的依赖项。功能包标记文件则用于告知 ``ros2 run`` 等工具到哪里查找该功能包。

在 ``package.xml`` 同级目录下创建 ``resource`` 目录，并在其中创建一个与功能包同名的空文件。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

        $ mkdir resource
        $ touch resource/talker_py

  .. group-tab:: macOS

    .. code-block:: console

        $ mkdir resource
        $ touch resource/talker_py

  .. group-tab:: Windows

    .. code-block:: console

        $ md resource
        $ type nul > resource\talker_py

``setup.py`` 中的 ``setup()`` 调用必须告知 ``setuptools`` 如何安装这些文件。请向 ``setup()`` 添加以下 ``data_files`` 参数。

.. code-block:: Python

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],

``setup.py`` 几乎完成。

迁移 Python 脚本并创建 ``setup.cfg``
-----------------------------------------------

ROS 2 Python 功能包使用 ``console_scripts`` `入口点 <https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point>`__ 将 Python 脚本安装为可执行程序。`配置文件 <https://setuptools.pypa.io/en/latest/userguide/declarative_config.html>`__ ``setup.cfg`` 告知 ``setuptools`` 将这些可执行程序安装到功能包专属目录，以便 ``ros2 run`` 等工具找到它们。请在 ``package.xml`` 同级目录下创建 ``setup.cfg`` 文件。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

        $ touch setup.cfg

  .. group-tab:: macOS

    .. code-block:: console

        $ touch setup.cfg

  .. group-tab:: Windows

    .. code-block:: console

        $ type nul > touch setup.cfg

在文件中写入以下内容：

.. code-block:: ini

    [develop]
    script_dir=$base/lib/talker_py
    [install]
    install_scripts=$base/lib/talker_py

你需要使用 ``console_scripts`` 入口点定义要安装的可执行程序。每个条目的格式为 ``executable_name = some.module:function``。第一部分指定要创建的可执行程序名称，第二部分指定该程序启动时应调用的函数。本功能包需要创建名为 ``talker_py_node`` 的可执行程序，并调用 ``talker_py`` 模块中的 ``main`` 函数。请将以下入口点配置作为另一个参数添加到 ``setup.py`` 的 ``setup()`` 调用中。

.. code-block:: Python

    entry_points={
        'console_scripts': [
            'talker_py_node = talker_py:main',
        ],
    },

现在不再需要 ``talker_py_node`` 文件。请删除该文件以及 ``scripts/`` 目录。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

        $ rm scripts/talker_py_node
        $ rmdir scripts

  .. group-tab:: macOS

    .. code-block:: console

        $ rm scripts/talker_py_node
        $ rmdir scripts

  .. group-tab:: Windows

    .. code-block:: console

        $ del scripts/talker_py_node
        $ rd scripts

添加 ``console_scripts`` 是对 ``setup.py`` 的最后一项修改。最终的 ``setup.py`` 应如下所示：

.. code-block:: Python

    from setuptools import setup

    package_name = 'talker_py'

    setup(
        name=package_name,
        version='1.0.0',
        packages=['talker_py'],
        package_dir={'': 'src'},
        install_requires=['setuptools'],
        zip_safe=True,
        data_files=[
            ('share/ament_index/resource_index/packages',
                ['resource/' + package_name]),
            ('share/' + package_name, ['package.xml']),
        ],
        maintainer='Brian Gerkey',
        maintainer_email='gerkey@example.com',
        description='The talker_py package',
        license='BSD',
        entry_points={
            'console_scripts': [
                'talker_py_node = talker_py:main',
            ],
        },
    )

迁移 ``src/talker_py/__init__.py`` 中的 Python 代码
----------------------------------------------------

ROS 2 对 Python 代码的最佳实践进行了许多调整。首先按原样迁移代码；等代码能够正常工作后，再进行重构会更容易。

使用 ``rclpy`` 替代 ``rospy``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ROS 2 功能包使用 `rclpy <https://index.ros.org/p/rclpy>`__ 替代 ``rospy``。使用 ``rclpy`` 需要完成两件事：

    1. 导入 ``rclpy``。
    2. 初始化 ``rclpy``。

删除导入 ``rospy`` 的语句。

.. code-block:: Python

    # Remove this
    import rospy

将其替换为导入 ``rclpy`` 的语句。

.. code-block:: Python

    import rclpy

在 ``main()`` 函数的第一条语句处添加 ``rclpy.init()`` 调用。

.. code-block:: Python

    def main():
        # Add this line
        rclpy.init()

在后台执行回调
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ROS 1 和 ROS 2 都使用 `回调函数 <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`__。在 ROS 1 中，回调始终在后台线程中执行，因此用户可以通过 ``rate.sleep()`` 等调用阻塞主线程。在 ROS 2 中，``rclpy`` 使用 :doc:`执行器 <../../Concepts/Intermediate/About-Executors>`，让用户更灵活地控制回调的执行位置。迁移包含 ``rate.sleep()`` 等阻塞调用的代码时，必须确保这些调用不会干扰执行器。一种方法是为执行器创建专用线程。

首先，添加以下两个导入语句。

.. code-block:: Python

    import threading

    from rclpy.executors import ExternalShutdownException

接下来，添加一个顶层函数 ``spin_in_background()``。该函数让默认执行器持续执行回调，直到执行器被关闭。

.. code-block:: Python

    def spin_in_background():
        executor = rclpy.get_global_executor()
        try:
            executor.spin()
        except ExternalShutdownException:
            pass

在 ``main()`` 函数中紧接 ``rclpy.init()`` 调用之后添加以下代码，以启动一个调用 ``spin_in_background()`` 的线程。

.. code-block:: Python

        # In rospy callbacks are always called in background threads.
        # Spin the executor in another thread for similar behavior in ROS 2.
        t = threading.Thread(target=spin_in_background)
        t.start()


最后，在 ``main()`` 函数末尾添加以下语句，以便程序结束时等待该线程退出。

.. code-block:: Python

        t.join()


创建节点
~~~~~~~~~~~~~

在 ROS 1 中，每个进程中的 Python 脚本只能创建一个节点，并通过 ``init_node()`` API 创建。在 ROS 2 中，一个 Python 脚本可以创建多个节点，创建节点的 API 名为 ``create_node``。

删除 ``rospy.init_node()`` 调用：

.. code-block::

    rospy.init_node('talker')

添加 ``rclpy.create_node()`` 调用，并将返回值保存到名为 ``node`` 的变量中：

.. code-block:: Python

    node = rclpy.create_node('talker')

还需要将该节点添加到执行器中。在创建节点的语句下方添加以下代码：

.. code-block:: Python

    rclpy.get_global_executor().add_node(node)

创建发布者
~~~~~~~~~~~~~~~~~~

在 ROS 1 中，用户通过实例化 ``Publisher`` 类创建发布者。在 ROS 2 中，用户通过节点的 ``create_publisher()`` API 创建发布者。需要注意，``create_publisher()`` API 与 ROS 1 有一个容易混淆的区别：话题名称和话题类型参数的顺序互换了。

删除创建 ``rospy.Publisher`` 实例的语句。

.. code-block::

    pub = rospy.Publisher('chatter', String, queue_size=10)

将其替换为 ``node.create_publisher()`` 调用。

.. code-block:: Python

    pub = node.create_publisher(String, 'chatter', 10)


创建 rate 对象
~~~~~~~~~~~~~~

在 ROS 1 中，用户直接创建 ``Rate`` 实例；在 ROS 2 中，用户通过节点的 ``create_rate()`` API 创建。

删除创建 ``rospy.Rate`` 实例的语句。

.. code-block::

    rate = rospy.Rate(10)  # 10hz

将其替换为 ``node.create_rate()`` 调用。

.. code-block:: Python

    rate = node.create_rate(10)  # 10hz

使用 ``rclpy.ok()`` 作为循环条件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在 ROS 1 中，``rospy.is_shutdown()`` API 用于判断进程是否收到关闭请求。在 ROS 2 中，对应功能由 ``rclpy.ok()`` API 提供。

删除 ``not rospy.is_shutdown()`` 语句。

.. code-block::

    while not rospy.is_shutdown():

将其替换为 ``rclpy.ok()`` 调用。

.. code-block:: Python

    while rclpy.ok():


创建包含当前时间的 ``String`` 消息
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

需要对下面这一行进行几处修改：

.. code-block::

    hello_str = "hello world %s" % rospy.get_time()

在 ROS 2 中：

* 必须从 ``Clock`` 实例获取时间。
* 应使用 `f-string <https://docs.python.org/3/reference/lexical_analysis.html#f-strings>`__ 格式化字符串，因为 ``%`` 格式化方式在当前 Python 版本中已不推荐使用。
* 必须实例化 ``std_msgs.msg.String`` 对象。

首先获取时间。ROS 2 节点具有 ``Clock`` 实例。将 ``rospy.get_time()`` 替换为 ``node.get_clock().now()``，以从节点时钟获取当前时间。

接下来，将 ``%`` 格式化方式替换为 f-string：``f'hello world {node.get_clock().now()}'``。

最后，实例化一个 ``std_msgs.msg.String()`` 对象，并将上面的字符串赋值给该对象的 ``data`` 属性。最终代码如下：

.. code-block:: Python

    hello_str = String()
    hello_str.data = f'hello world {node.get_clock().now()}'

记录一条信息级日志
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在 ROS 2 中，必须通过 ``Logger`` 实例发送日志消息，而节点本身就提供了一个 Logger 实例。

删除 ``rospy.loginfo()`` 调用。

.. code-block::

    rospy.loginfo(hello_str)

将其替换为调用节点 ``Logger`` 实例的 ``info()`` 方法。

.. code-block:: Python

    node.get_logger().info(hello_str.data)

这是对 ``src/talker_py/__init__.py`` 的最后一项修改。文件内容应如下所示：

.. code-block:: Python

    import threading

    import rclpy
    from rclpy.executors import ExternalShutdownException
    from std_msgs.msg import String


    def spin_in_background():
        executor = rclpy.get_global_executor()
        try:
            executor.spin()
        except ExternalShutdownException:
            pass


    def main():
        rclpy.init()
        # In rospy callbacks are always called in background threads.
        # Spin the executor in another thread for similar behavior in ROS 2.
        t = threading.Thread(target=spin_in_background)
        t.start()

        node = rclpy.create_node('talker')
        rclpy.get_global_executor().add_node(node)
        pub = node.create_publisher(String, 'chatter', 10)
        rate = node.create_rate(10)  # 10hz

        while rclpy.ok():
            hello_str = String()
            hello_str.data = f'hello world {node.get_clock().now()}'
            node.get_logger().info(hello_str.data)
            pub.publish(hello_str)
            rate.sleep()

        t.join()


构建并运行 ``talker_py_node``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

打开三个终端：

1. 一个用于构建 ``talker_py``。
2. 一个用于运行 ``talker_py_node``。
3. 一个用于查看 ``talker_py_node`` 发布的消息。

在第一个终端中构建工作空间。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

        $ cd ~/ros2_talker_py
        $ . /opt/ros/{DISTRO}/setup.bash
        $ colcon build

  .. group-tab:: macOS

    .. code-block:: console

        $ cd ~/ros2_talker_py
        $ . /opt/ros/{DISTRO}/setup.bash
        $ colcon build

  .. group-tab:: Windows

    .. code-block:: console

        $ cd \ros2_talker_py
        $ call C:\dev\ros2\local_setup.bat
        $ colcon build

在第二个终端中 source 工作空间，并运行 ``talker_py_node``。

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

        $ cd ~/ros2_talker_py
        $ . install/setup.bash
        $ ros2 run talker_py talker_py_node

  .. group-tab:: macOS

    .. code-block:: console

        $ cd ~/ros2_talker_py
        $ . install/setup.bash
        $ ros2 run talker_py talker_py_node

  .. group-tab:: Windows

    .. code-block:: console

        $ cd \ros2_talker_py
        $ call install\setup.bat
        $ ros2 run talker_py talker_py_node

在第三个终端中查看该节点发布的消息：

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

        $ . /opt/ros/{DISTRO}/setup.bash
        $ ros2 topic echo /chatter

  .. group-tab:: macOS

    .. code-block:: console

        $ . /opt/ros/{DISTRO}/setup.bash
        $ ros2 topic echo /chatter

  .. group-tab:: Windows

    .. code-block:: console

        $ call C:\dev\ros2\local_setup.bat
        $ ros2 topic echo /chatter


你应该能在第二个终端中看到带有当前时间的消息持续发布，并在第三个终端中接收到相同的消息。

按照 ROS 2 约定重构代码
--------------------------------------

你已经成功将一个 ROS 1 Python 功能包迁移到 ROS 2！现在代码已经能够运行，可以考虑进一步重构，使其更符合 ROS 2 的 Python API 习惯。请遵循以下两项原则：

* 创建一个继承自 ``Node`` 的类。
* 将工作放在回调中执行，绝不要阻塞这些回调。

例如，创建一个继承自 ``Node`` 的 ``Talker`` 类。为了在回调中执行工作，可以使用带回调函数的 ``Timer``，而不是调用 ``rate.sleep()``。让定时器回调发布消息后直接返回。让 ``main()`` 创建 ``Talker`` 实例，而不是调用 ``rclpy.create_node()``，并让执行器在主线程中运行。

重构后的代码示例如下：

.. code-block:: Python

    import rclpy
    from rclpy.node import Node
    from rclpy.executors import ExternalShutdownException
    from std_msgs.msg import String


    class Talker(Node):

        def __init__(self, **kwargs):
            super().__init__('talker', **kwargs)

            self._pub = self.create_publisher(String, 'chatter', 10)
            self._timer = self.create_timer(1 / 10, self.do_publish)

        def do_publish(self):
            hello_str = String()
            hello_str.data = f'hello world {self.get_clock().now()}'
            self.get_logger().info(hello_str.data)
            self._pub.publish(hello_str)


    def main():
        rclpy.init()
        try:
            rclpy.spin(Talker())
        except (ExternalShutdownException, KeyboardInterrupt):
            pass
        finally:
            rclpy.try_shutdown()

总结
----------

现在，你已经了解如何将一个示例 Python ROS 1 功能包迁移到 ROS 2。迁移自己的 Python 功能包时，请参考 :doc:`Python 功能包迁移参考 <./Migrating-Python-Packages>`。
