# Prompt For New Chat

当前项目：

PVESS（Photovoltaic and Energy Storage Simulation System）

这是一个长期演化的工商业光储仿真平台。

请优先阅读：

docs/

中的全部文档。

尤其优先阅读：

- 00_project_overview.md
- 01_architecture.md
- 04_current_progress.md
- 05_next_tasks.md
- 06_decision_log.md
- 07_developer_profile.md
- 08_ai_collaboration_rules.md
- 09_coding_convention.md
- 10_glossary.md

这些文件构成项目的 Project Memory。

目标：

恢复项目认知。

保持开发风格一致。

不要重新设计整个系统。

不要默认重构。

不要为了理论上的优雅而改变当前架构。

优先保持：

- 目录稳定；
- 接口稳定；
- 类职责稳定；
- 正负号定义稳定；
- 已验证模块稳定。

项目当前采用：

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

正确性。

简单性。

工程实用性。

避免：

复杂设计模式。

避免：

过度抽象。

避免：

一次输出大量代码。

允许：

逐步讨论。

逐步验证。

逐步修改。

---

# 当前系统状态

当前开发阶段：

V1.0 基础框架阶段。

目标：

建立完整仿真闭环：

Weather

↓

PV

↓

Load

↓

Battery

↓

Result

当前已经完成：

### WeatherModel

Weather Engine V0.3

支持：

- 气象数据读取；
- 日尺度数据；
- 年统计；
- 月统计；
- 温度；
- 风速；
- 典型日。

### PVModel

支持：

根据 GHI 生成光伏输出功率。

### LoadModel

支持：

生成时序负载曲线。

### BatteryModel V0.6

支持：

- 最大功率限制；
- SOC上下限保护；
- 充放电效率；
- SOC更新；
- Grid功率计算。

### ResultModel

已经建立。

正在完善。

### EMSModel

文件已建立。

尚未开发。

未来负责：

控制策略。

BatteryModel 不负责控制策略。

---

# 当前真实架构

main.py

↓

WeatherModel

↓

PVModel

↓

LoadModel

↓

BatteryModel

↓

ResultModel

未来：

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

请优先描述当前架构。

不要提前采用未来架构。

---

# 正负号约定（必须保持）

PV Power：

正。

Load Power：

正。

Battery Power：

正：

放电。

负：

充电。

Grid Power：

正：

购电。

负：

上网。

Energy Change：

正：

能量增加。

负：

能量减少。

SOC Change：

正：

SOC增加。

负：

SOC减少。

禁止在局部重新定义。

---

# BatteryModel 的职责

负责：

- 功率限制；
- SOC限制；
- 效率；
- SOC更新；
- Grid功率计算。

不负责：

什么时候充电。

什么时候放电。

控制策略属于：

EMSModel。

---

# AI 协作要求

优先：

讨论算法。

讨论状态机。

讨论变量意义。

讨论数据流。

最后再编码。

不要默认重构。

不要自动修改目录。

不要自动改变变量名。

不要整体重写文件。

优先：

增量修改。

小步迭代。

逐步验证。

允许开发者自己完成部分代码。

AI 的职责：

帮助理解。

帮助分析。

帮助调试。

帮助优化。

而不是代替开发。

---

# 开发者特点

具有：

电力系统和新能源工程背景。

熟悉：

光伏；

储能；

EMS；

峰平谷；

削峰填谷；

电池寿命；

工程项目。

Python 水平：

初级向中级过渡。

喜欢：

工程角度解释。

状态机。

数据流。

变量意义。

不喜欢：

复杂设计模式。

复杂继承体系。

优先：

简单。

稳定。

可读。

可维护。

---

# 长期目标

通过 PVESS 项目逐步学习：

Python；

面向对象；

软件架构；

Git；

AI协同开发；

长期工程开发。

目标不仅是完成一个项目。

而是形成长期的软件开发能力。

---

docs 是项目的大脑。

代码是项目的身体。

Git 是项目的时间机器。

Project Memory 是长期开发能力的核心。

请在开始任何开发工作之前，优先恢复项目认知。