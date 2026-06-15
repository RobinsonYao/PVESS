# 当前进展

## 当前版本

PVESS V1.0-alpha

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

V1.0 基础框架阶段

系统闭环已经完成。

下一阶段：

EMSModel V0.1
