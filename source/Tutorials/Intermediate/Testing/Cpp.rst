.. _TestingCpp:

使用 GTest 编写基础 C++ 测试
============================

本教程假设你已经创建了一个基础的 :ref:`ament_cmake 功能包 <CreatePkg>`，现在希望为它添加一些测试。

本教程将使用 `gtest <https://google.github.io/googletest/primer.html>`_。

功能包配置
----------

源代码
^^^^^^

首先，在名为 `test/tutorial_test.cpp` 的文件中编写测试代码：

.. code-block:: c++

    #include <gtest/gtest.h>

    TEST(package_name, a_first_test)
    {
      ASSERT_EQ(4, 2 + 2);
    }

    int main(int argc, char ** argv)
    {
      testing::InitGoogleTest(&argc, argv);
      return RUN_ALL_TESTS();
    }

package.xml
^^^^^^^^^^^

在 `package.xml` 中添加以下一行：

.. code-block:: xml

    <test_depend>ament_cmake_gtest</test_depend>

CMakeLists.txt
^^^^^^^^^^^^^^

.. code-block:: cmake

    if(BUILD_TESTING)
      find_package(ament_cmake_gtest REQUIRED)
      ament_add_gtest(${PROJECT_NAME}_tutorial_test test/tutorial_test.cpp)
      target_include_directories(${PROJECT_NAME}_tutorial_test PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
      )
      # target_link_libraries(${PROJECT_NAME}_tutorial_test name_of_local_library)
    endif()

测试代码被放在 `if/endif` 块中，以便在可能的情况下避免构建测试。`ament_add_gtest` 的工作方式与 `add_executable` 类似，因此你需要像平时一样调用 `target_include_directories` 和 `target_link_libraries`。

示例中的 `target_link_libraries` 调用被注释掉了，因为 `name_of_local_library` 只是占位符。只有当测试依赖于本功能包中构建的库时，才需要取消注释，并将占位符替换为 `add_library()` 调用中实际定义的目标名称。

运行测试
--------

有关如何运行测试以及检查测试结果的更多信息，请参阅 :doc:`通过命令行运行测试的教程 <CLI>`。
