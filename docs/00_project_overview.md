# PVESS Project Overview

---

# 1. Project Goal

PVESS（Photovoltaic and Energy Storage Simulation System）是一个面向工商业光储系统的仿真平台。

项目目标是建立一个能够持续演化的工程化仿真系统，用于：

- 光伏系统发电模拟；
- 储能系统运行模拟；
- 电网功率交互模拟；
- 能量管理策略（EMS）模拟；
- 峰平谷电价优化分析；
- 削峰填谷分析；
- 自发自用率分析；
- 经济性分析；
- 电池寿命分析；
- 工商业光储方案设计与评估。

项目强调工程实用性，而不是学术研究。

---

# 2. System Positioning

PVESS 是一个长期演化的系统级仿真平台。

定位：

输入：

气象数据 + 参数 + 控制策略

↓

仿真计算

↓

输出：

功率流、能量流、经济指标和运行结果

系统定位介于：

- Excel计算工具；
- 单次脚本；
- 商业光储设计软件；

之间。

目标是逐步形成一个可持续扩展的工程平台。

---

# 3. Main Functions

当前及未来主要功能包括：

### 气象模型

- 多年气象数据读取；
- 年辐照量统计；
- 月辐照量统计；
- 温度统计；
- 风速统计；
- 典型日提取。

### 光伏模型

- GHI 转换为光伏输出功率；
- 光伏发电时序曲线。

### 负载模型

- 负载曲线生成；
- 负载时序数据。

### 电池模型

- SOC状态更新；
- 功率限制；
- SOC上下限保护；
- 充放电效率；
- 电网功率计算。

### EMS模型（规划中）

- 自发自用；
- 峰平谷套利；
- 削峰填谷；
- 需量控制；
- 多策略控制。

### Result模型

统一保存：

- PV功率；
- Load功率；
- Battery功率；
- SOC；
- Grid功率；

以及后续扩展指标。

### 经济模型（规划中）

- 电费计算；
- 收益计算；
- IRR；
- NPV；
- 回收期。

### 电池寿命模型（规划中）

- 循环寿命；
- 日历寿命；
- SOH变化。

---

# 4. Current Development Stage

当前处于：

## V1.2-alpha

基础框架已经建立完成。

当前系统主链：

historical.csv

↓

DataModel

↓

PVModel

↓

EMSModel

↓

BatteryModel

↓

ResultModel

↓

output/result.csv

↓

output/*.png

当前重点：

- Battery + EMS 联合验证；
- DoubleCycleModel；
- EconomicModel MVP；
- TOUModel；
- TariffModel；
- SizingModel。

系统已经能够完成完整仿真闭环。

当前开发模式已经进入稳定阶段。

---

# 5. Completed Capabilities

截至目前已经完成：

### DataModel V0.2

支持：

- csv读取；
- datetime转换；
- DatetimeIndex建立；
- 列名标准化；

作为整个系统的数据层。

### Weather Engine V0.3

支持：

- 2016~2020年气象数据读取；
- 日尺度数据建立；
- 年总辐照量统计；
- 月辐照量统计；
- 月平均温度；
- 月平均风速；
- 典型日提取。

### PVModel

支持：

- 根据辐照度生成光伏输出功率。

### LoadModel

支持：

- 时序负载曲线生成。

### BatteryModel V0.6

支持：

- 充放电功率计算；
- 最大功率限制；
- SOC上下限保护；
- 充放电效率；
- SOC更新；
- Grid功率计算。

### ResultModel

支持：

统一保存：

- PV功率；
- Load功率；
- Battery功率；
- SOC；
- Grid功率；

并输出：

- result.csv；
- soc.png；
- power.png；
- energy_balance.png。

### EMSModel V0.2

支持：

- 光伏消纳（PV Self-consumption）；
- 峰谷套利；
- Demand Control Skeleton；
- Multi-objective + Priority-based 框架。

后续继续增加：

- 削峰填谷；
- Backup；
- 循环次数限制；
- 多目标优化。

---

# 6. Future Roadmap

短期目标：

完成：

Battery + EMS 联合验证

↓

DoubleCycleModel

↓

EconomicModel MVP

↓

TOUModel

↓

TariffModel

↓

SizingModel

逐步形成完整的工商业光储分析平台。

---

中期目标：

增加：

EMSModel

实现：

- 自发自用；
- 峰平谷套利；
- 削峰填谷；
- 需量控制。

---

长期目标：

增加：

- 电费模型；
- 电池寿命模型；
- 财务模型；
- 项目评估模型；
- 图形界面；
- 报告自动生成；
- 商业化平台。

---

# 7. Core Design Principles

项目遵循：

### 正确性优先

首先保证结果正确。

### 简单优先

避免复杂设计。

### 工程实用优先

优先解决实际问题。

### 渐进式演化

逐步扩展。

### 组合优于继承

优先采用多个独立模块。

### 避免过度抽象

不为了设计而设计。

### 保持架构稳定

避免频繁重构。

### 真实架构优先

记录当前实际状态。

而不是理想状态。

---

# 8. Engineering Constraints

项目约束：

- Python语言；
- 面向对象开发；
- pandas 为主要数据结构；
- 时间序列驱动；
- 以 DataFrame 和 Series 为核心；
- 增量开发；
- 保持目录稳定；
- 保持接口稳定；
- 尽量避免破坏已有代码。

项目不追求：

- 微服务；
- 分布式架构；
- 高并发；
- 云部署；
- 复杂设计模式。

---

# 9. Application Scenarios

适用于：

- 工商业光伏；
- 工商业储能；
- 光储充系统；
- 峰平谷套利分析；
- 削峰填谷分析；
- 经济性评估；
- 电池寿命分析；
- 项目方案设计；
- 技术研究。

---

# 10. Non-target Scenarios

当前不适用于：

- 电力系统潮流计算；
- 电磁暂态仿真；
- PSCAD级别仿真；
- 电池电化学机理研究；
- 实时控制系统；
- BMS开发；
- PCS控制器开发；
- 分布式计算平台。

---

# 11. Overall Development Philosophy

docs 是项目的大脑。

代码是项目的身体。

Git 是项目的时间机器。

项目采用长期演化方式逐步发展。

优先积累工程认知。

优先保持系统稳定。

优先形成能够跨对话继承的 Project Memory。


## 项目长期目标

PVESS 不仅是一个光储仿真工具。

项目最终目标是：

根据真实气象、负荷、光伏和运行策略，

自动确定：

* 储能功率（kW）
* 储能容量（kWh）

并进一步完成：

* 经济性分析
* 寿命分析
* 方案推荐
* 自动报告生成

因此：

SizingModel 是整个系统未来最核心的模块。

EMSModel、BatteryModel、EconomicModel、LifeModel 等模块，本质上都是为 SizingModel 服务的基础能力。

项目最终目标：

根据长期气象数据、负荷数据、光伏系统和运行策略，

自动确定：

- 储能功率（kW）
- 储能容量（kWh）

并进一步完成：

- 经济性分析；
- 寿命分析；
- 自动推荐；
- 自动报告生成。

SizingModel 是整个系统未来最核心的模块。

EMSModel、BatteryModel、EconomicModel、LifeModel 等模块均服务于 SizingModel。


当前版本：V1.2-alpha

当前系统主链：

historical.csv

↓

DataModel

↓

PVModel

↓

EMSModel

↓

BatteryModel

↓

ResultModel

↓

output/result.csv

↓

output/*.png

当前唯一入口：

python main.py

作为：

- 开发入口
- 集成测试入口
- 发布入口

当前测试数据：

tests/data/

- historical.csv
- stress.csv