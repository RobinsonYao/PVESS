# Storage Sizing Architecture

---

# 1. 定位

PVESS 不仅是一个光储仿真工具。

项目最终目标是：

根据真实气象、负荷、光伏和运行策略，

自动确定：

* 储能功率（kW）
* 储能容量（kWh）

并进一步完成：

* 经济性分析；
* 寿命分析；
* 方案推荐；
* 自动报告生成。

因此：

Storage Sizing 是整个系统未来最核心的功能。

EMSModel、BatteryModel、EconomicModel、LifeModel 等模块，本质上都是为 SizingModel 服务的基础能力。

---

# 2. 核心问题

给定：

* Weather
* PV
* Load
* EMS Strategy

确定：

* Battery Power（kW）
* Battery Capacity（kWh）

即：

最佳储能配置。

工程上的核心问题不是：

“储能如何充放电？”

而是：

“储能应该配多大？”

---

# 3. 不存在脱离策略的最佳容量

最佳储能配置与控制策略强相关。

不存在脱离运行策略的最佳容量。

不同 EMS 对应不同的最佳配置。

例如：

自发自用策略：

50kW / 100kWh

峰谷套利：

100kW / 200kWh

削峰填谷：

150kW / 80kWh

备用电源：

80kW / 300kWh

因此：

最佳容量

=

f(负荷，光伏，EMS)

而不是：

f(负荷，光伏)

---

# 4. 系统架构

SizingModel 是顶层调度器。

系统结构：

SizingModel

├── EMSModel

├── BatteryModel

├── EconomicModel

├── LifeModel

└── ReportModel

其中：

EMSModel

负责：

控制策略。

BatteryModel

负责：

执行。

EconomicModel

负责：

经济性评价。

LifeModel

负责：

寿命评价。

ReportModel

负责：

自动生成结果。

---
# 4.1 当前主链

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

python main.py

作为系统唯一入口。

当前所有功能开发均围绕该主链展开。

# 5. 模块职责

## SizingModel

负责：

确定：

* power_kw
* capacity_kwh

不负责：

* 功率限制；
* SOC更新；
* 效率；
* Grid计算；
* 控制策略。

---

## EMSModel

负责：

产生：

target_battery_power。

属于：

决策层。

---

## BatteryModel

负责：

执行：

target_battery_power。

产生：

* actual_battery_power；
* SOC；
* grid_power。

属于：

执行层。

---
## EconomicModel

负责：

价值评价。

包括：

- 光伏消纳收益；
- 峰谷套利收益；
- 循环寿命成本；

输出：

annual_saving。

属于：

评价层。

不参与：

控制策略。

## ResultModel

负责：

观察系统运行结果。

输出：

* CSV；
* PNG。

属于：

观察层。

---
## DoubleCycleModel

负责：

统计层。

输出：

- daily_cycle
- equivalent_cycle

用于：

EconomicModel

和

LifeModel。

不参与：

控制策略。

当前倾向：

属于统计层，

而不是决策层。

# 6. 输入

SizingModel 输入：

* pv_power
* load_power
* ems_model

未来扩展：

* electricity_price
* demand_charge
* battery_cost
* pv_cost

---

# 7. 输出

输出：

* optimal_power_kw
* optimal_capacity_kwh

未来扩展：

* annual_saving
* payback_period
* irr
* npv

---
# 7.1 Golden Path

采用：

python main.py

作为：

- 开发入口；
- 集成测试入口；
- 发布入口。

保持：

系统持续可运行。

优先：

渐进式演化。

避免：

整体重构。

# 8. V1.2
# V1.2-alpha

已经完成：

DataModel

EMSModel V0.2

main.py Golden Path

标准测试数据

output 标准输出

系统主链已经建立完成。
# V1.2
第一阶段：

固定功率。

扫描容量。

例如：

100kW

×

20kWh

40kWh

60kWh

...

500kWh

寻找收益开始饱和的位置。

---

# 9. V1.3

固定容量。

扫描功率。

例如：

100kWh

×

20kW

40kW

60kW

...

200kW

寻找收益开始饱和的位置。

---

# 10. V1.4

二维扫描：

功率 × 容量。

形成：

收益热力图。

得到：

optimal_power_kw

optimal_capacity_kwh。

---

# 11. V1.5

建立 EconomicModel。

计算：

* 电费；
* 年收益；
* 投资回收期；
* IRR；
* NPV。

---

# 12. V1.6

建立 LifeModel。

计算：

* 循环寿命；
* 日历寿命；
* SOH；
* 更换周期。

---

# 13. V2.0

建立多目标优化。

综合考虑：

* 收益；
* 寿命；
* 削峰；
* 需量；
* 电价。

形成：

综合最优配置。

---

# 14. V3.0

AI 辅助容量配置。

自动生成：

* 推荐功率；
* 推荐容量；
* 推荐策略；
* 推荐 PCS；
* 自动报告。

---

# 15. SOC 平衡约束

Sizing 中必须避免利用初始 SOC 获得虚假收益。

对于不同容量的比较：

要求：

SOC_end ≈ SOC_initial。

否则：

大容量电池会因为初始储能更多而产生虚假优势。

因此：

Sizing 应优先采用：

长期仿真。

例如：

月仿真；

年仿真；

多周期仿真。

而不是单日仿真。

---

# 16. 项目主线

PVESS 的长期主线：

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

DoubleCycleModel

↓

EconomicModel

↓

SizingModel
# 16.1 三层结构

当前系统形成：

Data Layer

↓

Business Layer

↓

Result Layer

其中：

Data Layer

负责：

数据组织。

Business Layer

负责：

状态和算法。

Result Layer

负责：

结果组织和输出。

SizingModel 位于：

Business Layer 顶层。

作为整个系统未来的调度中心。


其中：

SizingModel 是整个系统未来最核心的模块。

其余模块均服务于 SizingModel。

项目最终目标：

实现储能系统自动定型。

# 17. Future Ideas

记录未来可能扩展的方向。

仅记录。

不提前实现。

保持：

渐进式演化。

EMS

进一步支持：

自发自用；
峰谷套利；
削峰填谷；
需量控制；
Backup；
多目标优化。
Economic

支持：

电费模型；
收益模型；
IRR；
NPV；
回收期。
Battery Life

支持：

循环寿命；
日历寿命；
SOH模型；
更换周期。
DoubleCycle

支持：

一充一放；
两充两放；
Equivalent Cycle；
边际收益分析；
循环次数限制。

服务于：

EconomicModel

和

LifeModel。

Report

自动生成：

Word；
Excel；
PDF。

形成：

ReportModel。

Data Platform

支持：

多数据源。

包括：

CSV；
Excel；
API；
数据库。

统一通过：

DataModel

转换为标准 DataFrame。

保持：

Data Layer

↓

Business Layer

↓

Result Layer

三层结构。

Data Analysis

支持：

Typical Day；
Monthly Analysis；
Annual Analysis。

形成：

Weather Analysis Layer。

Visualization

建立统一绘图模块。

支持：

交互式图表；
多项目比较；
Dashboard。
GUI

形成桌面软件。

Web Platform

形成浏览器平台。

Multi-project

支持：

多个项目统一管理。

Cloud Platform

支持：

云端计算。

Digital Twin

形成数字孪生系统。

AI

支持：

参数优化；
策略优化；
智能推荐；
自动生成报告。

形成：

AI Assisted Sizing。

Business Direction

长期可能形成：

工商业储能方案设计平台；
收益分析平台；
光伏清洗效果评估平台；
运维平台；
项目管理平台。
Principle

记录灵感。

不提前实现。

保持系统简单。

按实际需求逐步演化。

避免：

为了未来需求而提前设计。