当前项目：

PVESS（Photovoltaic and Energy Storage Simulation System）

上一卷：

《光储仿真系统说明书V2》

已经结束。

当前上传内容包括：

- 完整项目源码；
- docs 文件夹；
- tests 文件夹；
- Git 历史；

请优先阅读 docs 文件夹。

尤其优先阅读：

00_project_overview.md

01_architecture.md

04_current_progress.md

05_next_tasks.md

06_decision_log.md

07_developer_profile.md

08_ai_collaboration_rules.md

09_coding_convention.md

10_glossary.md

13_prompt_for_new_chat.md

14_version_history.md

15_sizing_architecture.md

这些文件构成 Project Memory。

代码是项目的身体。

Git 是项目的时间机器。

目标：

恢复项目认知。

保持开发风格连续。

不要重新设计整个系统。

不要默认重构。

不要为了理论上的优雅改变当前架构。

优先描述真实架构。

优先保持：

- 目录稳定；
- 接口稳定；
- 正负号定义稳定；
- 已验证模块稳定。

项目采用：

渐进式演化。

开发流程：

理解问题

↓

讨论算法

↓

设计结构

↓

实现代码

↓

调试

↓

Freeze

↓

继续扩展

优先：

正确性；

简单性；

工程实用性。

避免：

复杂设计模式；

过度抽象；

整体重写文件；

一次输出大量代码。

允许：

逐步讨论；

逐步验证；

增量修改；

开发者自己完成部分代码。

AI 的职责：

帮助理解；

帮助分析；

帮助调试；

帮助优化；

而不是代替开发。

------------------------------------------------

当前版本：

V1.2-alpha

项目主线：

Storage Sizing

整个系统最终目标：

根据：

- 长期气象数据；
- 负荷数据；
- 光伏系统；
- EMS策略；

自动确定：

- 储能功率（kW）；
- 储能容量（kWh）。

之后进一步完成：

EconomicModel

↓

LifeModel

↓

OptimizationModel

↓

RecommendationModel

↓

ReportModel

------------------------------------------------

当前模型：

WeatherModel

↓

PVModel

↓

LoadModel

↓

EMSModel

↓

BatteryModel

↓

ResultModel

↓

SizingModel

其中：

WeatherModel V0.4：

支持长期数据读取。

BatteryModel：

负责执行层。

EMSModel：

负责决策层。

ResultModel：

负责观察层。

SizingModel：

负责容量定型。

------------------------------------------------

Battery Power：

正：放电；

负：充电。

Grid Power：

正：购电；

负：上网。

整个工程禁止重新定义正负号。

BatteryModel 不负责控制策略。

控制策略属于 EMSModel。

------------------------------------------------

当前 V1.2-alpha 最重要架构：

Double Cycle Mechanism。

原始数据：

2016-2020

↓

复制

↓

形成：

2016-2025

连续时间轴。

其中：

2016-2020

Warm-up

不统计。

2021-2025

Evaluation

用于正式统计。

目的：

消除 Initial SOC 污染。

禁止利用初始 SOC 获得虚假收益。

------------------------------------------------

开发者背景：

具有新能源、电力系统工程背景。

熟悉：

- 光伏；
- 储能；
- EMS；
- 峰平谷套利；
- 削峰填谷；
- 电池寿命；
- 工程项目。

Python 水平：

初级向中级过渡。

采用：

项目驱动学习。

喜欢：

从工程角度解释；

状态机；

数据流；

变量意义；

物理意义；

为什么。

不喜欢：

复杂设计模式；

复杂继承体系；

过度抽象。

优先：

简单；

稳定；

可读；

可维护。

------------------------------------------------

开始工作前：

请先阅读 docs。

恢复项目认知。

然后检查代码。

确认当前状态。

最后继续 V1.2 开发。

不要立即输出代码。

先同步认知。

确认之后，再开始下一阶段开发。