# Version History

记录 PVESS 项目主要版本演化过程。

重点记录：

- 增加了什么；
- 修复了什么；
- 为什么升级；

而不是记录具体代码。

---

# V0.1

项目初始化。

建立：

- main.py
- WeatherModel

目标：

读取气象数据。

---

# V0.2

完成气象数据读取。

支持：

- CSV读取；
- DatetimeIndex；
- 基础统计。

目标：

建立 Weather Engine。

---

# V0.3

完成 Weather Engine。

支持：

- 日尺度数据；
- 年总辐照量；
- 月总辐照量；
- 月平均温度；
- 月平均风速；
- 典型日提取；
- 典型日绘图。

WeatherModel 基本进入 Freeze 状态。

---

# V0.4

增加：

PVModel。

支持：

根据 GHI 生成光伏输出功率。

建立：

LoadModel。

支持：

时序负荷生成。

形成：

Weather

↓

PV

↓

Load

基础链路。

---

# V0.5

建立：

BatteryModel。

增加：

- 最大功率限制；
- SOC上下限；
- 充放电效率；
- SOC更新。

开始研究：

功率流和能量流。

---

# V0.6

完成 BatteryModel 主要算法。

统一：

正负号定义。

规定：

Battery Power

正：

放电。

负：

充电。

Grid Power

正：

购电。

负：

上网。

增加：

Grid功率计算。

BatteryModel 接近 Freeze。

---

# V1.0（进行中）

目标：

建立完整仿真闭环。

结构：

Weather

↓

PV

↓

Load

↓

Battery

↓

Result

当前正在开发：

ResultModel。

---

# V1.x

计划增加：

EMSModel。

支持：

- 自发自用；
- 峰平谷套利；
- 削峰填谷；
- 需量控制。

形成：

系统级仿真。

---

# V2.x

计划增加：

EconomicModel。

支持：

- 电费计算；
- 收益分析；
- IRR；
- NPV；
- 回收期。

---

# V3.x

计划增加：

LifeModel。

支持：

- 循环寿命；
- 日历寿命；
- SOH模型。

---

# V4.x

计划增加：

- ReportModel；
- GUI；
- 自动报表；
- 商业化平台。

---

# Development Philosophy

采用：

渐进式演化。

优先：

正确性。

简单性。

工程实用性。

避免：

大规模重构。

保持：

长期可维护性。

docs 是项目的大脑。

代码是项目的身体。

Git 是项目的时间机器。

# PVESS V1.0-alpha

时间：

2026-06

---

## 重要里程碑

完成第一个完整仿真闭环。

系统流程：

Weather

↓

PV

↓

Load

↓

Battery

↓

Result

↓

CSV

↓

PNG

---

## ResultModel V0.4

新增：

* export_csv()
* plot_soc()
* plot_power()
* plot_energy_balance()

输出：

* result.csv
* soc.png
* power.png
* energy_balance.png

---

## BatteryModel V0.6

进入 Freeze 状态。

职责：

* 功率限制
* SOC限制
* 效率模型
* SOC更新
* Grid功率计算

控制策略不属于 BatteryModel。

---

## 当前架构状态

执行层已经建立完成。

下一阶段：

EMSModel V0.1

开始建立决策层。

# PVESS V1.1-alpha

时间：

2026-06

---

## 重要里程碑

完成控制层与执行层分离。

系统流程：

Weather

↓

PV

↓

Load

↓

EMS

↓

Battery

↓

Result

↓

CSV

↓

PNG

---

## EMSModel V0.1

新增：

自发自用策略。

输出：

target_battery_power

职责：

决策层。

---

## BatteryModel V0.8

删除：

simulate()

保留：

* execute()
* execute_series()

职责：

执行层。

---

## 架构状态

三层结构已经建立：

EMS

↓

Battery

↓

Result

对应：

决策层

↓

执行层

↓

观察层

---

下一阶段：

EMSModel V0.2

峰谷套利策略。


# V1.1-alpha

重要架构变化：

决策层与执行层完成分离。

形成：

EMS

↓

Battery

↓

Result

三层结构。

---

重要方向调整：

项目主线由：

建立仿真模型

转向：

储能系统定型（Sizing）。

SizingModel 被定义为未来系统的顶层模块。

EMSModel、BatteryModel、EconomicModel、LifeModel 等模块，均服务于 SizingModel。

V1.2-alpha

重要架构变化：

项目主线由：

光储仿真

转向：

储能容量定型

2026年06月16日11:19:29
V1.2-alpha

新增：

EMS MVP

新增：

pytest测试体系

新增：

EMS + Battery 联合测试

新增：

标准测试数据集

normal

stress

historical

建立：

csv + png 分析模式。
# PVESS V1.2-alpha

时间：

2026-06-18

---

## 重要里程碑

建立：

Data Layer

↓

Business Layer

↓

Result Layer

三层结构。

形成：

python main.py

Golden Path。

系统进入稳定演化阶段。

---

## DataModel V0.2

新增：

DataModel。

负责：

* csv读取；
* datetime转换；
* DatetimeIndex建立；
* 列名标准化。

输出：

标准 DataFrame。

当前标准列：

* dataset
* datetime
* temperature
* ghi
* load
* tou_period

系统数据入口逐步统一。

---

## EMSModel V0.2

新增：

* PV Self-consumption；
* Peak-Valley Arbitrage；
* Demand Control Skeleton。

采用：

Multi-objective

+

Priority-based

架构。

形成：

决策层。

↓

执行层。

结构。

---

## Main Workflow

形成：

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

系统主链已经建立完成。

---

## Golden Path

正式采用：

python main.py

作为：

* 开发入口；
* 集成测试入口；
* 发布入口。

开发流程调整为：

修改一个模块

↓

python main.py

↓

分析：

result.csv

↓

分析：

png

↓

Debug

↓

git

↓

更新 docs

↓

进入下一功能

优先保证：

系统持续可运行。

---

## Test Dataset

标准测试数据调整为：

* historical
* stress

取消：

normal

采用：

csv + png

分析模式。

---

## ResultModel

统一输出：

* result.csv
* soc.png
* power.png
* energy_balance.png

output/

正式成为标准输出目录。

---

## Architecture Status

当前已经完成：

Data Layer

↓

PV

↓

EMS

↓

Battery

↓

Result

主链。

下一阶段：

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

项目重心逐步转向：

储能容量定型。