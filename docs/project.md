# PVESS Project

---

# 1 Mission

PVESS

Photovoltaic Energy Storage Simulation System

当前阶段：

V1-alpha

第一阶段目标：

建立工商业光储系统智能配置平台。

输入：

* 地理位置；
* 负荷信息；
* 光伏容量；
* 电价参数；
* 用户目标；
* 设计约束。

利用：

* 历史气象数据库；
* EMS控制策略；
* 储能模型；
* 经济模型；
* 压力测试。

自动输出：

* 推荐储能功率（kW）；
* 推荐储能容量（kWh）；
* 年收益；
* IRR；
* 投资回收期；
* 自发自用率；
* 削峰效果；
* SOC统计；
* 可靠性评价。

最终形成工商业储能系统自动定型（Sizing）能力。

---

# 2 Development Principle

采用：

Monolith First

Refactor Later

原则。

优先级：

持续可运行

>

持续可验证

>

持续演化

>

功能数量

避免：

* 大规模重构；
* 提前抽象；
* 过度设计；
* 一次加入多个复杂功能。

---

# 3 Workflow

统一入口：

```bash
python main.py
```

开发流程：

修改代码

↓

python main.py

↓

检查 output

↓

确认结果正常

↓

git

↓

更新 project.md

↓

更新 session_summary.md

↓

继续开发

main.py 同时承担：

* 开发入口；
* 集成测试入口；
* 发布入口。

系统始终保持可运行状态。

---

# 4 User Workflow

## Step 1

选择地理位置。

自动匹配历史气象数据库。

---

## Step 2

输入负荷。

支持：

### Detailed Mode

负荷曲线。

### Bill Mode

峰平谷电量。

### Simple Mode

月用电量。

---

## Step 3

输入光伏容量。

---

## Step 4

输入电价参数。

包括：

* 尖；
* 峰；
* 平；
* 谷；
* 需量电价。

---

## Step 5

选择运行目标。

包括：

* 收益最大；
* 自发自用最大；
* 扩容替代；
* 削峰填谷；
* 备用电源。

系统自动生成 EMS 策略。

---

## Step 6

设置设计约束。

包括：

* 最大投资额；
* 最大PCS；
* 最大容量；
* 循环寿命要求。

---

## Step 7

运行仿真。

---

## Step 8

输出推荐方案。

---

# 5 Simulation Flow

Location

↓

DatasetManager

↓

PVModel

↓

EMSModel

↓

BatteryModel

↓

EconomicModel

↓

StressTest

↓

SizingModel

↓

Output

---

# 6 Current Architecture

采用：

Input Layer

↓

Simulation Layer

↓

Economic Layer

↓

Sizing Layer

↓

Output Layer

其中：

### Input Layer

负责：

* 用户输入；
* 参数管理；
* 数据集选择。

### Simulation Layer

负责：

* 光伏模型；
* EMS；
* 电池模型；
* 功率流计算。

### Economic Layer

负责：

* 电价计算；
* 收益计算；
* 财务指标。

### Sizing Layer

负责：

* 储能选型；
* 多方案比较；
* 推荐结果生成。

### Output Layer

负责：

* csv输出；
* 图形输出；
* 报告输出。

---

# 7 Current Modules

已经完成：

* DataModel；
* WeatherModel；
* LoadModel；
* PVModel；
* EMSModel；
* BatteryModel；
* ResultModel。

未来模块：

* DatasetManager；
* EconomicModel；
* StressTest；
* SizingModel；
* DoubleCycleModel；
* TariffModel；
* TOUModel。

---

# 8 Dataset

历史数据库：

2016~2020

全国城市

10分钟间隔

多参数气象数据。

未来支持：

### Typical Dataset

典型年。

### Stress Dataset

压力测试数据。

### Extreme Dataset

极端工况数据。

---

# 9 Tests

采用：

Main.py First

原则。

统一运行：

```bash
python main.py
```

专项调试允许：

```text
tests/

battery_test.py

ems_test.py

pv_test.py
```

tests 不作为系统入口。

长期测试资产：

```text
tests/data/

historical.csv

stress.csv
```

---

# 10 Output

运行自动生成：

```text
output/

result.csv

soc.png

power.png

energy_balance.png
```

output 不保存历史结果。

分析结束后允许清空。

---

# 11 Directory

```text
PVESS/

main.py

config/

models/

controllers/

charts/

tests/

data/

output/

docs/

snapshots/

archives/
```

其中：

archives/

用于版本归档。

snapshots/

用于开启新对话。

---

# 12 Current Priority

Priority 1

EconomicModel。

Priority 2

StressTest。

Priority 3

SizingModel MVP。

Priority 4

DoubleCycleModel。

Priority 5

TariffModel。

Priority 6

TOUModel。

---

# 13 Long-term Evolution

V1

Rule-based EMS。

↓

V2

Economic Optimization。

↓

V3

Multi-objective Optimization。

↓

V4

MPC。

↓

V5

MILP。

↓

V6

GUI。

↓

V7

Cloud Platform。

始终保持渐进式演化。

---

# 14 Version History

## 2026-06

建立 PVESS 工程。

完成：

* DataModel；
* WeatherModel；
* LoadModel；
* PVModel；
* EMSModel；
* BatteryModel；
* ResultModel。

统一入口：

```bash
python main.py
```

采用：

Monolith First

Refactor Later

策略。

取消多文档体系。

docs 最终收敛为：

```text
docs/

project.md
```

snapshots 用于开启新对话。

新对话仅需要：

* main.py；
* project.md；
* session_summary.md。

第一阶段目标确定为：

工商业光储系统智能配置平台。
