# Architecture

---

# 1. Project Structure

当前系统主链：

```text
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

output

```
未来演化路径
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

TariffModel

↓

SizingModel


SizingModel 是顶层调度器。

EMSModel 是策略模块。

BatteryModel 是执行模块。

EconomicModel 是评价模块。

LifeModel 是寿命模块。
```

---

# 2. Current System Architecture

当前系统结构：

```text
DataModel
     ↓

PVModel

EMSModel
     ↓

BatteryModel
     ↓

ResultModel
---

# 3. Future Architecture


未来计划增加：

```text
DataModel
     ↓

PVModel

EMSModel
     ↓

BatteryModel
     ↓

DoubleCycleModel
     ↓

EconomicModel
     ↓

SizingModel
```

其中：

EMSModel 决定：

- 什么时候充电；
- 什么时候放电；
- 电池目标功率。

BatteryModel 不负责控制策略。

BatteryModel 只负责执行。

---

# 4. Module Responsibilities

---

## Responsibility Boundary

说明：

main.py：

负责：

数据读取
模型调用
输出文件

models：

负责：

算法
状态

禁止：

savefig
to_csv
测试代码

## WeatherModel

职责：

提供天气统计分析能力。

包括：

- 日尺度数据；
- 月统计；
- 年统计；
- 典型日提取。

不负责：

- csv读取；
- datetime转换；
- 数据格式标准化。

提供：

- GHI；
- 温度；
- 风速；
- 日尺度数据；
- 月统计数据；
- 年统计数据；
- 典型日。


---

## PVModel

职责：

计算光伏输出功率。

输入：

GHI。

输出：

PV功率序列。

单位：

kW。

---

## LoadModel

职责：

生成负载曲线。

输入：

负载参数。

输出：

Load功率序列。

单位：

kW。

---

## BatteryModel

职责：

执行储能计算。

包括：

- 功率限制；
- SOC限制；
- 充放电效率；
- SOC更新；
- Grid功率计算。

不负责：

- EMS策略；
- 峰平谷控制；
- 经济优化。

输入：

PV功率；

Load功率；

未来增加：

目标电池功率。

输出：

Battery功率；

SOC；

Grid功率。

---

## ResultModel

职责：

统一管理仿真结果。

保存：

- PV功率；
- Load功率；
- Battery功率；
- SOC；
- Grid功率。

未来扩展：

- 电价；
- 收益；
- SOH；
- 循环次数。

---

## EMSModel V0.2

职责：

控制策略。

支持：

- PV Self-consumption；
- Peak-Valley Arbitrage；
- Demand Control Skeleton；

采用：

Multi-objective + Priority-based 框架。

后续增加：

- 削峰填谷；
- Backup；
- Cycle Limit；
- 多目标优化。

输出：

目标电池功率。

---

## Data Layer

DataModel

职责：

- csv读取
- datetime转换
- 建立 DatetimeIndex
- 列名标准化

输出：

标准 DataFrame


# 5. Main Data Flow

当前：

```text
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

output
```

未来：

```text
WeatherModel
      ↓

PVModel

LoadModel

EMSModel
      ↓

BatteryModel
      ↓

ResultModel
```

---

# 6. Call Chain

main.py：

负责：

系统调度。

调用顺序：

```text
DataModel.load()

↓

PVModel

↓

EMSModel

↓

BatteryModel

↓

ResultModel
```

main.py 不负责：

具体算法。

算法放在各个 Model 内部。

---

# 7. Class Relationships

当前：

各 Model 相互独立。

采用：

组合关系。

而不是：

继承关系。

```text
main.py

↓

WeatherModel

PVModel

LoadModel

BatteryModel

ResultModel
```

不存在：

父类；

子类；

复杂继承结构。

---

# 8. Core Data Objects

项目主要数据对象：

---

## DataFrame

用于：

二维数据。

例如：

天气数据；

结果数据。

---

## Series

用于：

时间序列。

例如：

PV功率；

Load功率；

Battery功率；

SOC。

---

## DatetimeIndex

作为统一时间轴。

整个系统使用：

pandas 时间索引。

时间间隔：

10分钟。

---

# 9. Power Sign Convention

统一规定：

PV Power：

始终为正。

Load Power：

始终为正。

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

SOC：

0~100%。

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

该约定适用于整个工程。

---

# 10. Extension Principles

扩展原则：

新增功能优先增加新的 Model。

例如：

```text
EconomicModel

LifeModel

TariffModel

SOHModel

ReportModel
```

尽量避免：

修改已有稳定模块。

已经验证正确的模块进入：

Freeze 状态。

仅在：

- 发现错误；
- 增加功能；
- 收益明确；

时进行修改。

---

# 11. Architecture Principles

当前项目遵循：

简单优先；

正确性优先；

工程实用优先；

组合优于继承；

避免过度抽象；

保持目录稳定；

保持接口稳定；

避免频繁重构；

渐进式演化。

优先记录真实架构。

而不是理想架构。