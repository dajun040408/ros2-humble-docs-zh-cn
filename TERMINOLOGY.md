# ROS 2 Humble 中文术语表

本术语表用于统一全站翻译。API、类型、命令、代码标识符和配置键保留原文，不因术语表而改写代码。

| English | 简体中文 | 使用说明 |
|---|---|---|
| ROS (Robot Operating System) | 机器人操作系统（ROS） | ROS 是中间件及工具生态，不是传统意义上的操作系统 |
| Node | 节点 | |
| Topic | 话题 | |
| Publisher | 发布者 | |
| Subscriber | 订阅者 | |
| Service | 服务 | |
| Client | 客户端 | |
| Action | 动作 | ROS 2 通信机制 |
| Parameter | 参数 | |
| Message | 消息 | |
| Interface | 接口 | |
| Executor | 执行器 | |
| Callback | 回调函数 | |
| Callback Group | 回调组 | |
| Lifecycle | 生命周期 | |
| Lifecycle Node | 生命周期节点 | |
| Middleware | 中间件 | |
| Quality of Service (QoS) | 服务质量（QoS） | 首次出现使用中英文对照 |
| Reliability | 可靠性 | QoS 策略 |
| Durability | 持久性 | QoS 策略 |
| History | 历史记录 | QoS 策略 |
| Deadline | 截止时间 | QoS 策略 |
| Liveliness | 活跃性 | QoS 策略 |
| Discovery | 发现机制 | |
| Domain ID | 域 ID | |
| DDS | DDS | 数据分发服务，首次出现可补充全称 |
| RMW | ROS 中间件接口（RMW） | |
| Launch | Launch（启动系统） | 作为工具/框架名称时保留 Launch |
| Workspace | 工作空间 | |
| Package | 功能包 | |
| Colcon | colcon | 保留原名 |
| Composition | 组件组合 | ROS 2 组件化机制 |
| Component | 组件 | |
| Node graph | 节点图 | |
| Transform (TF) | 坐标变换（TF） | |
| TF2 | TF2 | 保留 |
| Build system | 构建系统 | |
| Overlay | 覆盖工作空间 | |
| Underlay | 底层工作空间 | |
| Cross-compilation | 交叉编译 | |
| Tracing | 跟踪 | ROS 2 性能分析语境 |
| rosbag2 | rosbag2 | 产品名保留 |
| CLI (Command Line Interface) | 命令行接口 | |

## 翻译约定

1. 首次出现且容易产生歧义的术语，采用“中文（English）”形式。
2. 后续正文优先使用中文；ROS 生态中约定俗成的名称保留英文。
3. 类名、函数名、命名空间、变量名、命令、文件名、路径、Topic/Service/Action 名称及消息类型不翻译。
4. QoS 策略名称在解释性文字中可翻译，但代码、CLI 参数和配置字段保持原样。
5. 术语出现语义差异时，以具体上下文为准，并在本文件补充说明。
