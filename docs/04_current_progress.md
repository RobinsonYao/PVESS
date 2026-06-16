# 当前进展

## 当前版本

V1.1-alpha

---

## 已完成模块

### WeatherModel V0.3

状态：

Freeze

功能：

* 气象数据读取
* 日数据提取
* 典型日分析
* 月统计
* 绘图功能

---

### PVModel V0.1

状态：

稳定

功能：

* GHI → 光伏功率转换

---

### LoadModel V0.1

状态：

稳定

功能：

* 负载曲线生成

---

### BatteryModel V0.6

状态：

Freeze

功能：

* 功率限制
* SOC限制
* 充放电效率
* SOC更新
* Grid功率计算

正负号定义：

Battery Power

正：

放电

负：

充电

Grid Power

正：

购电

负：

上网

BatteryModel 只负责执行。

控制策略属于 EMSModel。

### BatteryModel V0.8

状态：

Freeze

功能：

* execute()
* execute_series()

职责：

执行层

负责：

* 功率限制
* SOC限制
* 效率
* SOC更新
* Grid功率计算

BatteryModel 不负责控制策略。

控制策略属于 EMSModel。


---

### EMSModel V0.1

状态：

Stable

功能：

* 自发自用策略

输入：

* pv_power
* load_power

输出：

* target_battery_power

职责：

决策层

---



### ResultModel V0.4

状态：

Freeze

功能：

* build()
* to_dataframe()
* head()
* tail()
* show_info()
* export_csv()
* plot_soc()
* plot_power()
* plot_energy_balance()

输出文件：

* result.csv
* soc.png
* power.png
* energy_balance.png

---

## 当前系统流程

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

## 当前阶段

当前版本：

V1.2-alpha

当前重点：

Storage Sizing

已完成：

WeatherModel

PVModel

LoadModel

EMSModel

BatteryModel

ResultModel

长期周期数据支持

Double Cycle Mechanism

下一阶段：

Warm-up / Evaluation 分离

MetricModel

Capacity Scan

Power Scan

2D Scan

2026年06月16日11:17:27
V1.2-alpha

完成：

EMS MVP

完成：

pytest 测试体系

完成：

Unit Test

完成：

Scenario Test

完成：

Long-term Test

完成：

EMS + Battery 联合测试

完成：

标准测试数据集 test_dataset.csv

包含：

normal

stress

historical

三个一年期（10min）数据集。

标准测试数据集基于北京2016气象数据生成。
