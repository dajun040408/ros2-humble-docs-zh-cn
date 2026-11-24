.. _Releases:

ROS 2 发行版
============

什么是发行版？
--------------

ROS 发行版是一组带有版本号的 ROS 功能包集合，其概念类似于 Linux 发行版（例如 Ubuntu）。

ROS 发行版的目的是让开发者能够基于相对稳定的代码库开展工作，直到准备好将整个系统升级到新版本。因此，发行版发布后，我们会尽量限制核心功能包（即 ros-desktop-full 下的所有内容）的变更范围，主要接受缺陷修复和不破坏兼容性的改进。

这一原则通常适用于整个社区；但对于更高层级的功能包，规则相对宽松，因此相应功能包的维护者需要负责避免引入破坏性变更。

.. _list_of_distributions:

发行版列表
----------

以下列出了当前和历史上的 ROS 2 发行版。表格中以蓝色标记的行表示当前仍受支持的发行版。

.. toctree::
   :hidden:

   Lyrical Luth 发行说明 <Releases/Release-Lyrical-Luth>
   Kilted Kaiju 发行说明 <Releases/Release-Kilted-Kaiju>
   Jazzy Jalisco 发行说明 <Releases/Release-Jazzy-Jalisco>
   Humble Hawksbill 发行说明 <Releases/Release-Humble-Hawksbill>
   Rolling Ridley 发行说明 <Releases/Release-Rolling-Ridley>
   开发版 <Releases/Development>
   已终止支持的发行版 <Releases/End-of-Life>
   发行流程 <Releases/Release-Process>


.. raw:: html

   <!--
     This CSS overrides the styles of certain rows to mark them blue, indicating they are supported releases.
     For the odd number rows, a line like the following must be used:

       .rst-content table.distros:not(.field-list) tr:nth-child(1) td {...}

     For the even number rows, a line like the following must be used:

       .rst-content tr:nth-child(2) {...}

     No other combination I've found has worked.  Yes, this is extremely fragile.  No, I don't understand
     why it is like this.
   -->
   <style>
     /* Targeting the cells and rows for the background and plain text */
    .rst-content table.distros:not(.field-list) tr:nth-child(1) td,
    .rst-content table.distros tr:nth-child(2),
    .rst-content table.distros:not(.field-list) tr:nth-child(3) td,
    .rst-content table.distros:not(.field-list) tr:nth-child(5) td {
      background-color: #22314E;
      color: white;
    }

    /* Targeting the links inside those specific rows to force them to be not-blue */
    .rst-content table.distros:not(.field-list) tr:nth-child(1) td a,
    .rst-content table.distros tr:nth-child(2) a,
    .rst-content table.distros:not(.field-list) tr:nth-child(3) td a,
    .rst-content table.distros:not(.field-list) tr:nth-child(3) td a {
      color: #B0B0B0 !important;
    }
   </style>

.. |rolling| image:: Releases/rolling-small.png
   :alt: Rolling logo

.. |lyrical| image:: Releases/lyrical-small.png
   :alt: Lyrical logo

.. |kilted| image:: Releases/kilted-small.png
   :alt: Kilted logo

.. |jazzy| image:: Releases/jazzy-small.png
   :alt: Jazzy logo

.. |iron| image:: Releases/iron-small.png
   :alt: Iron logo

.. |humble| image:: Releases/humble-small.png
   :alt: Humble logo

.. |galactic| image:: Releases/galactic-small.png
   :alt: Galactic logo

.. |foxy| image:: Releases/foxy-small.png
   :alt: Foxy logo

.. |eloquent| image:: Releases/eloquent-small.png
   :alt: Eloquent logo

.. |dashing| image:: Releases/dashing-small.png
   :alt: Dashing logo

.. |crystal| image:: Releases/crystal-small.png
   :alt: Crystal logo

.. |bouncy| image:: Releases/bouncy-small.png
   :alt: Bouncy logo

.. |ardent| image:: Releases/ardent-small.png
   :alt: Ardent logo

.. list-table::
   :class: distros
   :header-rows: 1
   :widths: 35 25 30 20 10

   * - 发行版
     - 发布日期
     - 标识
     - 生命周期结束日期
     - ROS 负责人
   * - :doc:`Lyrical Luth <Releases/Release-Lyrical-Luth>`
     - May 22, 2026
     - |lyrical|
     - May 2031
     - `Shane Loretz <https://github.com/sloretz>`_
   * - :doc:`Kilted Kaiju <Releases/Release-Kilted-Kaiju>`
     - May 23, 2025
     - |kilted|
     - December 2026
     - `Scott K Logan <https://github.com/cottsay>`_
   * - :doc:`Jazzy Jalisco <Releases/Release-Jazzy-Jalisco>`
     - May 23, 2024
     - |jazzy|
     - May 2029
     - `Marco A. Gutiérrez <https://github.com/marcoag>`_
   * - :doc:`Iron Irwini <Releases/Release-Iron-Irwini>`
     - May 23, 2023
     - |iron|
     - December 4, 2024
     - `Yadunund Vijay <https://github.com/Yadunund>`_
   * - :doc:`Humble Hawksbill <Releases/Release-Humble-Hawksbill>`
     - May 23, 2022
     - |humble|
     - May 2027
     - `Christophe Bédard <https://github.com/christophebedard>`_ / `Audrow Nash <https://github.com/audrow>`_
   * - :doc:`Galactic Geochelone <Releases/Release-Galactic-Geochelone>`
     - May 23, 2021
     - |galactic|
     - December 9, 2022
     - `Scott Logan <https://github.com/cottsay/>`_
   * - :doc:`Foxy Fitzroy <Releases/Release-Foxy-Fitzroy>`
     - June 5, 2020
     - |foxy|
     - June 20, 2023
     - `Jacob Perron <https://github.com/jacobperron>`_ / `Dharini Dutia <https://github.com/quarkytale>`_
   * - :doc:`Eloquent Elusor <Releases/Release-Eloquent-Elusor>`
     - November 22, 2019
     - |eloquent|
     - November 2020
     - `Michael Carroll <https://github.com/mjcarroll>`_
   * - :doc:`Dashing Diademata <Releases/Release-Dashing-Diademata>`
     - May 31, 2019
     - |dashing|
     - May 2021
     - `Steven! Ragnarök <https://github.com/nuclearsandwich>`_
   * - :doc:`Crystal Clemmys <Releases/Release-Crystal-Clemmys>`
     - December 14, 2018
     - |crystal|
     - December 2019
     - `Steven! Ragnarök <https://github.com/nuclearsandwich>`_
   * - :doc:`Bouncy Bolson <Releases/Release-Bouncy-Bolson>`
     - July 2, 2018
     - |bouncy|
     - July 2019
     - `Mikael Arguedas <https://github.com/mikaelarguedas>`_ / `Steven! Ragnarök <https://github.com/nuclearsandwich>`_
   * - :doc:`Ardent Apalone <Releases/Release-Ardent-Apalone>`
     - December 8, 2017
     - |ardent|
     - December 2018
     - `Steven! Ragnarök <https://github.com/nuclearsandwich>`_
   * - :doc:`beta3 <Releases/Beta3-Overview>`
     - September 13, 2017
     -
     - December 2017
     -
   * - :doc:`beta2 <Releases/Beta2-Overview>`
     - July 5, 2017
     -
     - September 2017
     -
   * - :doc:`beta1 <Releases/Beta1-Overview>`
     - December 19, 2016
     -
     - Jul 2017
     -
   * - :doc:`alpha1 - alpha8 <Releases/Alpha-Overview>`
     - August 31, 2015
     -
     - December 2016
     -

未来发行版
----------

有关未来功能的详细信息，请参阅 :doc:`路线图 <The-ROS2-Project/Roadmap>`。

ROS 2 每年都会在 5 月 23 日（`世界海龟日 <https://www.worldturtleday.org/>`_）发布一个新发行版。

.. list-table::
   :class: future-distros
   :header-rows: 1
   :widths: 35 25 30 20 10

   * - 发行版
     - 发布日期
     - 标识
     - 生命周期结束日期
     - ROS 负责人
   * - :doc:`Makoa Mata-mata <Releases/Release-Makoa-Mata-mata>`
     - May 2027
     - TBD
     - Dec 2028
     - `Christophe Bédard <https://github.com/christophebedard>`_

.. _rolling_distribution:

Rolling 发行版
--------------

:doc:`ROS 2 Rolling Ridley <Releases/Release-Rolling-Ridley>` 是 ROS 2 的滚动开发发行版。它在 `REP 2002 <https://reps.openrobotics.org/rep-2002/>`_ 中进行了说明，并于 2020 年 6 月首次推出。

ROS 2 Rolling 发行版有两个用途：

1. 作为未来稳定版 ROS 2 发行版的预备区。
2. 汇集最新的开发版本。

顾名思义，Rolling 会持续更新，**并且可能在原有版本上直接引入包含破坏性变更的更新**。我们建议大多数用户使用最新的稳定发行版（参见 :ref:`发行版列表 <list_of_distributions>`）。

发布到 Rolling 发行版的软件包，未来会自动发布到后续的 ROS 2 稳定发行版中。将 ROS 2 功能包发布到 Rolling 的流程与其他 ROS 2 发行版相同，具体请参阅 :doc:`发布 ROS 2 功能包 <../How-To-Guides/Releasing/Releasing-a-Package>`。

跨发行版通信
------------

不能保证不同 ROS 发行版之间的节点一定能够通信。例如，基于 Humble 构建并运行的节点，不保证能够与基于 Iron 构建并运行的节点正确通信。它们之间可能可以通信，也可能无法通信；这种通信不受支持，因此不应依赖。

请注意，:ref:`跨供应商（同一发行版）通信也不受保证 <different-middleware-vendors-cross-vendor-communication>`。
