.. redirect-from::

    About-ROS-Interfaces
    Concepts/About-ROS-Interfaces

接口（Interfaces）
==================

.. contents:: 目录
   :local:

背景
------

ROS 应用通常通过三种接口之一进行通信：:doc:`话题 <About-Topics>``、:doc:`服务 <About-Services>`` 或 :doc:`动作 <About-Actions>`。

ROS 2 使用一种简化的描述语言——接口定义语言（Interface Definition Language，IDL）来描述这些接口。这种描述方式使 ROS 工具能够自动为多种目标编程语言生成相应接口类型的源代码。

本文将介绍支持的接口类型：

* msg：``.msg`` 文件是简单的文本文件，用于描述 ROS 消息的字段。它们用于生成不同语言中的消息源代码。
* srv：``.srv`` 文件用于描述服务，由请求和响应两部分组成。请求和响应本身都是消息声明。
* action：``.action`` 文件用于描述动作，由目标、结果和反馈三部分组成。每一部分本身都是一条消息声明。

消息
------

消息是 ROS 2 节点向网络中的其他 ROS 节点发送数据的一种方式，不需要对方返回响应。例如，如果某个 ROS 2 节点从传感器读取温度数据，就可以使用 ``Temperature`` 消息将数据发布到 ROS 2 网络中。网络中的其他节点可以订阅该数据并接收 ``Temperature`` 消息。

消息在 ROS 功能包的 ``msg/`` 目录下通过 ``.msg`` 文件描述和定义。``.msg`` 文件由两个部分组成：字段和常量。

字段
^^^^^^

每个字段由类型和名称组成，两者之间用空格分隔，例如：

.. code-block:: bash

   fieldtype1 fieldname1
   fieldtype2 fieldname2
   fieldtype3 fieldname3

例如：

.. code-block:: bash

   int32 my_int
   string my_string

字段类型
~~~~~~~~~~

字段类型可以是：

* 内置类型（built-in type）。
* 独立定义的消息描述名称，例如 ``geometry_msgs/PoseStamped``。

*当前支持的内置类型：*

.. list-table::
   :header-rows: 1

   * - 类型名称
     - `C++ <https://design.ros2.org/articles/generated_interfaces_cpp.html>`__
     - `Python <https://design.ros2.org/articles/generated_interfaces_python.html>`__
     - `DDS 类型 <https://design.ros2.org/articles/mapping_dds_types.html>`__
   * - bool
     - bool
     - builtins.bool
     - boolean
   * - byte
     - uint8_t
     - builtins.bytes*
     - octet
   * - char
     - char
     - builtins.int*
     - char
   * - float32
     - float
     - builtins.float*
     - float
   * - float64
     - double
     - builtins.float*
     - double
   * - int8
     - int8_t
     - builtins.int*
     - octet
   * - uint8
     - uint8_t
     - builtins.int*
     - octet
   * - int16
     - int16_t
     - builtins.int*
     - short
   * - uint16
     - uint16_t
     - builtins.int*
     - unsigned short
   * - int32
     - int32_t
     - builtins.int*
     - long
   * - uint32
     - uint32_t
     - builtins.int*
     - unsigned long
   * - int64
     - int64_t
     - builtins.int*
     - long long
   * - uint64
     - uint64_t
     - builtins.int*
     - unsigned long long
   * - string
     - std::string
     - builtins.str
     - string
   * - wstring
     - std::u16string
     - builtins.str
     - wstring

*所有内置类型都可以用于定义数组：*

.. list-table::
   :header-rows: 1

   * - 类型名称
     - `C++ <https://design.ros2.org/articles/generated_interfaces_cpp.html>`__
     - `Python <https://design.ros2.org/articles/generated_interfaces_python.html>`__
     - `DDS 类型 <https://design.ros2.org/articles/mapping_dds_types.html>`__
   * - 静态数组
     - std::array<T, N>
     - builtins.list*
     - T[N]
   * - 无界动态数组
     - std::vector
     - builtins.list
     - sequence
   * - 有界动态数组
     - custom_class<T, N>
     - builtins.list*
     - sequence<T, N>
   * - 有界字符串
     - std::string
     - builtins.str*
     - string

（*）对于比 ROS 定义更宽松的类型，软件会在范围和长度方面强制执行 ROS 约束。

*使用数组和有界类型定义消息的示例：*

.. code-block:: bash

   int32[] unbounded_integer_array
   int32[5] five_integers_array
   int32[<=5] up_to_five_integers_array

   string string_of_unbounded_size
   string<=10 up_to_ten_characters_string

   string[<=5] up_to_five_unbounded_strings
   string<=10[] unbounded_array_of_strings_up_to_ten_characters_each
   string<=10[<=5] up_to_five_strings_up_to_ten_characters_each

字段名称
~~~~~~~~~~

字段名称必须由小写字母、数字和用于分隔单词的下划线组成。字段名称必须以字母开头，不能以下划线结尾，也不能包含连续两个下划线。

字段默认值
~~~~~~~~~~~~

消息类型中的任意字段都可以设置默认值。目前，字符串数组和复杂类型不支持默认值（即上面内置类型表中未列出的类型；这也适用于所有嵌套消息）。

定义默认值时，需要在字段定义行中添加第三个元素：

.. code-block:: bash

   fieldtype fieldname fielddefaultvalue

例如：

.. code-block:: bash

   uint8 x 42
   int16 y -2000
   string full_name "John Doe"
   int32[] samples [-200, -100, 0, 100, 200]

.. note::

  * 字符串值必须使用单引号 ``'`` 或双引号 ``"`` 定义。
  * 当前字符串值不会进行转义处理。

常量
^^^^^^

每个常量定义都类似于带默认值的字段描述，但该值不能通过程序修改。通过使用等号 ``=`` 来指定常量值，例如：

.. code-block:: bash

   constanttype CONSTANTNAME=constantvalue

例如：

.. code-block:: bash

   int32 X=123
   int32 Y=-123
   string FOO="foo"
   string EXAMPLE='bar'

.. note::

   常量名称必须全部使用大写字母。

服务
------

服务是一种请求/响应通信机制。客户端（请求方）会等待服务端（响应方）执行一项短时间计算并返回结果。

服务通过 ROS 功能包 ``srv/`` 目录下的 ``.srv`` 文件描述和定义。

服务描述文件由请求和响应两种消息类型组成，两者之间使用 ``---`` 分隔。将任意两个 ``.msg`` 文件用 ``---`` 连接起来，就构成合法的服务描述。

下面是一个非常简单的服务示例：接收一个字符串并返回一个字符串。

.. code-block:: bash

   string str
   ---
   string str

服务定义也可以更加复杂（如果要引用同一功能包中的消息，则不应写出功能包名称）：

.. code-block:: bash

   # request constants
   int8 FOO=1
   int8 BAR=2
   # request fields
   int8 foobar
   another_pkg/AnotherMessage msg
   ---
   # response constants
   uint32 SECRET=123456
   # response fields
   another_pkg/YetAnotherMessage val
   CustomMessageDefinedInThisPackage value
   uint32 an_integer

不能在一个服务中嵌入另一个服务。

动作
------

动作是一种长时间运行的请求/响应通信机制。动作客户端（请求方）会等待动作服务端（响应方）执行某项操作并返回结果。与服务不同，动作可以持续较长时间（数秒或数分钟），可以在执行过程中提供反馈，也可以被中断。

动作定义采用以下形式：

.. code::

   <request_type> <request_fieldname>
   ---
   <response_type> <response_fieldname>
   ---
   <feedback_type> <feedback_fieldname>

与服务类似，请求字段位于第一组三个连字符（``---``）之前，响应字段位于第一组三个连字符之后。第二组三个连字符之后还有第三组字段，用于在发送反馈时传递数据。

请求字段、响应字段和反馈字段的数量都可以任意，包括零个。

`<request_type>``、``<response_type>`` 和 ``<feedback_type>`` 遵循与消息 ``<type>`` 相同的规则。``<request_fieldname>``、``<response_fieldname>`` 和 ``<feedback_fieldname>`` 遵循与消息 ``<fieldname>`` 相同的规则。

例如，``Fibonacci`` 动作定义如下：

.. code::

   int32 order
   ---
   int32[] sequence
   ---
   int32[] sequence

该动作定义中，动作客户端发送一个 ``int32`` 字段，表示需要计算的斐波那契数列阶数；动作服务端则需要返回一个包含完整计算结果的 ``int32`` 数组。在计算过程中，动作服务端还可以提供一个中间 ``int32`` 数组，用于表示截至某个时间点已经完成的计算结果。
