.. redirect-from::

   Concepts/About-Build-System

构建系统
========

.. contents:: 目录
   :local:

.. include:: ../../../global_substitutions.txt

构建系统使开发者能够根据需要构建 ROS 2 代码。ROS 2 高度依赖将代码划分为功能包的方式，每个功能包都包含一个清单文件（``package.xml```）。该清单文件包含功能包的重要元数据，包括它对其他功能包的依赖关系。元构建工具需要该文件才能正常工作。

ROS 2 构建系统由三个主要概念组成。

构建工具
--------

构建工具负责控制单个功能包的编译和测试。在 ROS 2 中，C++ 通常使用 CMake，Python 通常使用 setuptools，但也支持其他构建工具。

构建辅助工具
------------

构建辅助工具是一组接入构建工具的辅助函数，用于改善开发体验。ROS 2 功能包通常依赖 ament 系列功能包来实现这些功能。

``ament``` 由几个重要代码仓库组成，它们都位于 `GitHub 组织 <https://github.com/ament>`__ 中。

ament_package 功能包
~~~~~~~~~~~~~~~~~~~~

该仓库位于 GitHub：`ament/ament_package <https://github.com/ament/ament_package>`__，其中包含一个 ament Python 功能包，为 ament 功能包提供各种实用工具，例如环境钩子模板。

所有 ament 功能包都必须在其根目录中包含一个 ``package.xml``` 文件，而不论底层使用何种构建系统。``package.xml``` 清单文件包含处理和操作功能包所需的信息，包括功能包名称（全局唯一）以及依赖关系。该文件同时也是文件系统中标识功能包位置的标记文件。

``package.xml``` 文件的解析由 ``catkin_pkg``` 提供（与 ROS 1 相同）；而通过搜索文件系统中的 ``package.xml``` 文件来定位功能包，则由 ``colcon``` 等构建工具提供。

.. glossary::

   package.xml
       功能包清单文件，用于标记功能包根目录，并包含功能包的元信息，例如名称、版本、描述、维护者、许可证、依赖关系等。清单内容采用机器可读的 XML 格式，其内容由 REP 127 和 REP 140 描述，未来还可能通过其他 REP 进行修改。

因此，当某个功能包被称为 ament 功能包时，意味着它是一个独立的软件单元（源代码、构建文件、测试、文档和其他资源），并通过 ``package.xml``` 清单文件进行描述。

.. glossary::

   ament package
       任何包含 ``package.xml``` 并遵循 ament 打包规范的功能包，不论其底层使用哪种构建系统。

由于“ament 功能包”这一术语与具体构建系统无关，因此可以存在不同类型的 ament 功能包，例如 ament CMake 功能包、ament Python 功能包等。

在该软件栈中，常见的功能包类型包括：

.. glossary::

    CMake package
        包含普通 CMake 项目和 ``package.xml``` 清单文件的功能包。

    ament CMake package
        同时遵循 ament 打包规范的 CMake 功能包。

    Python package
        包含基于 setuptools 的 Python 项目和 ``package.xml``` 清单文件的功能包。

    ament Python package
        同时遵循 ament 打包规范的 Python 功能包。

ament_cmake 仓库
~~~~~~~~~~~~~~~~

该仓库位于 GitHub：`ament/ament_cmake <https://github.com/ament/ament_cmake>`__，包含许多 ament CMake 功能包和纯 CMake 功能包，提供创建 ament CMake 功能包所需的 CMake 基础设施。

这里所说的 ament CMake 功能包，是指使用 CMake 构建的 ament 功能包。因此，该仓库中的功能包提供必要的 CMake 函数、宏和 CMake 模块，以便创建更多 ament CMake（或 ``ament_cmake```）功能包。这类功能包通过 ``package.xml``` 文件的 ``<export>``` 标签中的 ``<build_type>ament_cmake</build_type>``` 标记进行识别。

该仓库中的功能包具有高度模块化的特点，但其中有一个汇总入口功能包 ``ament_cmake```。任何功能包都可以依赖 ``ament_cmake```，以获得该仓库中所有功能包提供的聚合功能。

仓库中的常见功能包及其用途如下：

* ``ament_cmake```：聚合该仓库中的其他功能包，用户只需依赖它即可。
* ``ament_cmake_auto```：提供便捷的 CMake 函数，自动处理编写功能包 ``CMakeLists.txt``` 时的大量繁琐工作。
* ``ament_cmake_core```：提供 ament 的核心内置概念，例如环境钩子、资源索引、符号链接安装等。
* ``ament_cmake_gmock```：为基于 gmock 的单元测试提供便捷函数。
* ``ament_cmake_gtest```：为基于 gtest 的自动化测试提供便捷函数。
* ``ament_cmake_nose```：为基于 nosetests 的 Python 自动化测试提供便捷函数。
* ``ament_cmake_python```：为包含 Python 代码的功能包提供 CMake 函数，参阅 :doc:`ament_cmake_python 用户文档 <../../How-To-Guides/Ament-CMake-Python-Documentation>`。
* ``ament_cmake_test```：使用 CTest 将不同类型的测试（例如 gtest 和 nosetests）聚合到同一个目标中。

``ament_cmake_core``` 功能包包含大量 CMake 基础设施，使不同功能包能够通过约定俗成的接口清晰地传递信息。这使功能包之间的构建接口更加解耦，促进功能包复用，并推动不同功能包构建系统之间形成一致约定。例如，它提供了标准方式，用于在功能包之间传递 include 目录、库、定义和依赖关系。

``ament_cmake_core``` 还提供 ament 构建系统的符号链接安装功能。该功能可以将源空间或构建空间中的文件以符号链接方式安装到安装空间，而不是复制文件。这样只需安装一次，之后修改 Python 代码和配置文件等非生成资源时，无需重新执行安装步骤即可生效。该功能基本上取代了 catkin 的 devel space，保留了其大部分优点，同时减少了复杂性和缺点。

``ament_cmake_core``` 还提供功能包资源索引，使功能包能够声明自己包含某种类型的资源。该设计让查询某个前缀（例如 ``/usr/local```）中有哪些功能包更加高效，因为只需列出该前缀下一个可能位置中的文件即可。更多信息请参阅资源索引的 `设计文档 <https://github.com/ament/ament_cmake/blob/{REPOS_FILE_BRANCH}/ament_cmake_core/doc/resource_index.md>`__。

与 catkin 类似，``ament_cmake_core``` 还提供环境设置文件和功能包专属的环境钩子。环境设置文件通常命名为 ``setup.bash```，功能包开发者可以在其中定义使用该功能包所需的环境变更。开发者通过“环境钩子”实现这些变更，本质上就是一段任意 Shell 代码，可以设置或修改环境变量、定义 Shell 函数、配置自动补全规则等。例如，ROS 1 正是通过这种方式设置 ``ROS_DISTRO``` 环境变量，而 catkin 本身并不需要了解 ROS 发行版的具体信息。

ament_lint 仓库
~~~~~~~~~~~~~~~

该仓库位于 GitHub：`ament/ament_lint <https://github.com/ament/ament_lint>`__，提供多个功能包，以方便且一致的方式提供代码检查和测试服务。

目前，这些功能包支持使用 ``uncrustify``` 检查 C++ 代码风格、使用 ``cppcheck``` 执行 C++ 静态代码检查、检查源代码版权声明、使用 ``pep8``` 检查 Python 代码风格等。未来辅助功能包列表还可能继续扩展。

元构建工具
----------

元构建工具负责确定一组功能包的拓扑顺序，并按照正确的依赖顺序构建或测试这些功能包。它会调用构建工具，实际执行功能包的编译、测试和安装工作。

在 ROS 2 中，使用的元构建工具是 `colcon <https://colcon.readthedocs.io/en/released/>`__。
