# 当前进展

## 当前版本

V1.2-alpha

---

## 已完成模块

### WeatherModel

状态：

Freeze

功能：

* 日数据提取
* 月统计
* 年统计
* 典型日提取

WeatherModel 不再承担系统数据入口。

csv读取逐步迁移至：

DataModel。

---
### DataModel V0.2

状态：

Stable

职责：

数据层

负责：

* csv读取
* datetime转换
* DatetimeIndex建立
* 列名标准化

输出：

标准 DataFrame

当前标准列：

* dataset
* datetime
* temperature
* ghi
* load
* tou_period

### PVModel

状态：

Freeze

功能：

* GHI → 光伏功率转换

---

### LoadModel

状态：

Freeze

功能：

* 负荷曲线生成

---

### BatteryModel

状态：

Freeze

职责：

执行层

负责：

* 功率限制
* SOC限制
* 充放电效率
* SOC更新
* Grid功率计算

Battery Power：

正：

放电

负：

充电

Grid Power：

正：

购电

负：

上网

BatteryModel 不负责控制策略。

---

### EMSModel V0.2

状态：

Stable

职责：

决策层

功能：

* PV Self-consumption
* Peak-Valley Arbitrage
* Demand Control Skeleton

采用：

Multi-objective + Priority-based 框架。

输入：

* pv_power
* load_power

输出：

* target_battery_power

---

### ResultModel

状态：

Freeze

职责：

观察层

功能：

* build()
* export_csv()
* plot_soc()
* plot_power()
* plot_energy_balance()

输出：

* csv
* png

---

## 已完成测试体系

完成：

* Unit Test
* Scenario Test
* Long-term Test
* EMS + Battery 联合测试

建立标准测试数据集：

* historical
* stress

采用标准数据接口：

* dataset
* datetime
* temperature
* ghi
* load
* tou_period

时间轴：

DatetimeIndex

测试结果采用：

csv + png

进行分析。

---

## 当前系统流程

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

result.csv

↓

png

---
## 当前入口

python main.py

状态：

Stable

作为：

* 开发入口
* 集成测试入口
* 发布入口

采用：

Golden Path 开发模式。

## 当前主线

EMSModel V0.2

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

---

## 当前开发原则

修改一个模块

↓

python main.py

↓

检查：

result.csv

↓

检查：

soc.png

power.png

energy_balance.png

↓

分析结果

↓

Debug

↓

git

↓

更新 docs

↓

进入下一功能

始终保持：

python main.py

能够正常运行。
