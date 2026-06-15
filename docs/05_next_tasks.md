# Next Tasks

记录项目未来开发计划。

采用：

渐进式演化。

优先：

正确性。

简单性。

工程实用性。

---

# 1. Current Goal

当前阶段：

V1.0 基础框架。

目标：

建立完整仿真闭环。

实现：

```text
Weather

↓

PV

↓

Load

↓

Battery

↓

Result
```

确保：

整个系统能够运行。

输出完整结果。

---

# 2. Short-term Tasks

优先级：

最高。

---

## Task 001

完善 ResultModel

目标：

建立统一结果对象。

保存：

- PV Power；
- Load Power；
- Battery Power；
- SOC；
- Grid Power。

形成：

```text
Datetime

PV

Load

Battery

SOC

Grid
```

状态：

进行中。

优先级：

★★★★★

依赖：

BatteryModel。

---

## Task 002

Result 输出功能

支持：

- DataFrame；
- head()；
- tail()；
- show_info()。

状态：

待开发。

优先级：

★★★★★

依赖：

ResultModel。

---

## Task 003

结果绘图

支持：

- PV曲线；
- Load曲线；
- Battery曲线；
- SOC曲线；
- Grid曲线。

状态：

待开发。

优先级：

★★★★☆

依赖：

ResultModel。

---

## Task 004

CSV导出

支持：

保存：

仿真结果。

状态：

待开发。

优先级：

★★★★☆

依赖：

ResultModel。

---

# 3. Medium-term Tasks

进入：

系统级仿真阶段。

---

## Task 005

EMSModel

建立：

ems_model.py。

职责：

决定：

什么时候充电。

什么时候放电。

输出：

目标电池功率。

状态：

文件已建立。

尚未开发。

优先级：

★★★★★

---

## Task 006

自发自用策略

目标：

优先利用光伏。

剩余电量：

充电。

缺电：

放电。

状态：

待开发。

优先级：

★★★★★

依赖：

EMSModel。

---

## Task 007

峰平谷套利

支持：

谷充；

峰放。

状态：

待开发。

优先级：

★★★★★

依赖：

EMSModel。

---

## Task 008

削峰填谷

支持：

限制最大需量。

状态：

待开发。

优先级：

★★★★☆

依赖：

EMSModel。

---

## Task 009

需量控制

支持：

需量约束。

状态：

待开发。

优先级：

★★★★☆

依赖：

EMSModel。

---

# 4. Long-term Tasks

进入：

项目分析阶段。

---

## EconomicModel

支持：

- 电费计算；
- 节省收益；
- IRR；
- NPV；
- 回收期。

优先级：

★★★★☆

---

## LifeModel

支持：

- 循环寿命；
- 日历寿命；
- SOH模型。

优先级：

★★★★☆

---

## TariffModel

支持：

峰平谷电价。

优先级：

★★★★☆

---

## ReportModel

自动生成：

分析报告。

优先级：

★★★☆☆

---

## GUI

图形界面。

优先级：

★★★☆☆

---

# 5. Future Platform Tasks

未来可能扩展：

---

项目方案设计平台；

工商业储能配置工具；

收益分析平台；

电池寿命评估平台；

清洗效果分析平台；

多项目管理；

云平台。

当前：

仅记录。

不提前实现。

---

# 6. Suggested Development Order

推荐顺序：

```text
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

EMS
    ↓

Economic
    ↓

Life
    ↓

Report
```

优先保证：

每增加一个模块，

系统都能够运行。

避免：

同时开发多个模块。

---

# 7. Module Dependency

```text
Weather
    ↓

PV

Load

↓

Battery

↓

Result

↓

EMS

↓

Economic

↓

Life

↓

Report
```

原则：

下层稳定后，

再开发上层。

---

# 8. Current Priority

当前第一任务：

完善 ResultModel。

当前第二任务：

开发 EMSModel。

当前第三任务：

进入系统级仿真。

---

# 9. Development Strategy

采用：

小步迭代。

逐步验证。

逐步 Freeze。

避免：

大规模重构。

避免：

同时开发多个模块。

优先：

稳定。

可读。

正确。

工程实用。

---

# 10. Final Goal

长期目标：

形成一个能够持续演化的：

Photovoltaic and Energy Storage Simulation System。

支持：

技术分析；

方案设计；

经济评估；

寿命分析；

商业应用。

采用：

长期工程方式逐步发展。

而不是：

一次完成。