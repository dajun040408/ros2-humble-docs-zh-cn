.. redirect-from::

    Tutorials/Using-Parameters-In-A-Class-Python

.. _PythonParamNode:

在类中使用参数（Python）
========================

**目标：** 使用 Python 创建并运行包含 ROS 参数的类。

**教程级别：** 初级

**预计时间：** 20 分钟

.. contents:: 目录
   :depth: 2
   :local:

背景
----

创建自己的 :doc:§节点 <../Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes>§ 时，有时需要添加可以从启动文件设置的参数。本教程介绍如何在 Python 类中创建参数，以及如何在启动文件中设置参数。

前置条件
--------

此前的教程已经介绍了如何 :doc:§创建工作空间 <./Creating-A-Workspace/Creating-A-Workspace>§、:doc:§创建功能包 <./Creating-Your-First-ROS2-Package>§，以及 :doc:§参数 <../Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters>§ 的作用。

任务
----

1. 创建功能包
^^^^^^^^^^^^^

source ROS 2 环境，并在 ros2_ws/src 目录中创建新功能包：

.. code-block:: console

  $ ros2 pkg create --build-type ament_python --license Apache-2.0 python_parameters --dependencies rclpy

在 package.xml 中填写描述、维护者信息和许可证：

.. code-block:: xml

  <description>Python parameter tutorial</description>
  <maintainer email="you@email.com">Your Name</maintainer>
  <license>Apache License 2.0</license>

2. 编写 Python 节点
^^^^^^^^^^^^^^^^^^^

在 ros2_ws/src/python_parameters/python_parameters 目录中创建 python_parameters_node.py：

.. code-block:: python

    import rclpy
    import rclpy.node
    import rclpy.parameter

    class MinimalParam(rclpy.node.Node):
        def __init__(self):
            super().__init__('minimal_param_node')
            self.declare_parameter('my_parameter', 'world')
            self.timer = self.create_timer(1, self.timer_callback)

        def timer_callback(self):
            my_param = self.get_parameter(
                'my_parameter').get_parameter_value().string_value
            self.get_logger().info('Hello %s!' % my_param)

            my_new_param = rclpy.parameter.Parameter(
                'my_parameter',
                rclpy.Parameter.Type.STRING,
                'world')
            self.set_parameters([my_new_param])

    def main():
        rclpy.init()
        node = MinimalParam()
        rclpy.spin(node)

    if __name__ == '__main__':
        main()

2.1 理解代码
~~~~~~~~~~~~

构造函数中的 declare_parameter() 创建名为 my_parameter、默认值为 world 的参数。参数类型根据默认值推断，因此这里是字符串类型。

定时器周期为 1 秒，每次执行 timer_callback()。回调函数通过 get_parameter() 读取参数并输出日志，然后使用 set_parameters() 将参数恢复为默认值 world。

2.1.1（可选）添加 ParameterDescriptor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

可以为参数设置描述符，提供文本说明和约束：

.. code-block:: python

    from rcl_interfaces.msg import ParameterDescriptor

    my_parameter_descriptor = ParameterDescriptor(
        description='This parameter is mine!')
    self.declare_parameter(
        'my_parameter', 'world', my_parameter_descriptor)

由于使用了 rcl_interfaces，还需要在 package.xml 中添加依赖：

.. code-block:: xml

    <depend>rclpy</depend>
    <depend>rcl_interfaces</depend>

运行节点后，可以使用 ros2 param describe /minimal_param_node my_parameter 查看参数类型和描述。

2.2 添加入口点
~~~~~~~~~~~~~~

打开 setup.py，在 console_scripts 中添加：

.. code-block:: python

    entry_points={
        'console_scripts': [
            'minimal_param_node = python_parameters.python_parameters_node:main',
        ],
    },

3. 构建并运行
^^^^^^^^^^^^^

建议在工作空间根目录运行 rosdep 检查缺少的依赖项：

.. code-block:: console

    $ rosdep install -i --from-path src --rosdistro {DISTRO} -y

然后构建：

.. code-block:: console

    $ colcon build --packages-select python_parameters

source 工作空间并运行：

.. code-block:: console

    $ source install/setup.bash
    $ ros2 run python_parameters minimal_param_node

终端应该每秒输出一次 Hello world!。

3.1 通过命令行修改参数
~~~~~~~~~~~~~~~~~~~~~~

节点运行时，在另一个终端 source 工作空间并查看参数：

.. code-block:: console

    $ ros2 param list

修改参数：

.. code-block:: console

    $ ros2 param set /minimal_param_node my_parameter earth

如果看到 Set parameter successful，就说明修改成功。另一个终端会输出 Hello earth!。由于节点随后会将参数恢复为 world，因此之后又会输出 Hello world!。

3.2 通过启动文件修改参数
~~~~~~~~~~~~~~~~~~~~~~~~

在 ros2_ws/src/python_parameters/ 中创建 launch 目录，并在其中创建 python_parameters_launch.py。启动文件可以在启动 minimal_param_node 时将 my_parameter 设置为 earth。

在 setup.py 中添加 launch 文件安装规则：

.. code-block:: python

    import os
    from glob import glob

    data_files=[
        # ...
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
    ]

重新构建并 source 工作空间后运行：

.. code-block:: console

    $ ros2 launch python_parameters python_parameters_launch.py

第一次输出应为 Hello earth!，之后由于节点将参数恢复为默认值，会继续输出 Hello world!。

总结
----

你创建了一个包含自定义参数的节点，并学习了如何通过启动文件或命令行设置参数。
