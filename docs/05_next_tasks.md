# Next Tasks

## Priority 1

Battery + EMS 联合验证

目标：

验证：

* battery_power
* soc
* grid_power

输出：

* result.csv
* soc.png
* power.png
* energy_balance.png

确保：

python main.py

稳定运行。

逐步完成：

EMSModel V0.2 Freeze。

---

## Priority 2

DoubleCycleModel

统计：

* daily cycle
* equivalent cycle


进一步支持：

* 一充一放
* 两充两放

分析：

边际收益变化。
---

## Priority 3

EconomicModel MVP

建立：

* 峰谷套利收益
* 光伏消纳收益
* 年充放电量
* 循环寿命成本

形成：

EconomicModel MVP。
---

## Priority 4

TOUModel Skeleton

负责：

* 峰谷时段
* 尖峰
* 深谷
* 地区差异
* 季节变化

---

## Priority 5

TariffModel Skeleton

负责：

* 购电电价
* 上网电价
* 峰谷电价
* 容量电费
* 需量电费

---

保持：

渐进式演化。

避免一次设计完成。

## Priority 6

SizingModel Skeleton

目标：

形成：

长期气象

↓

运行策略

↓

经济分析

↓

自动确定：

* 储能功率（kW）
* 储能容量（kWh）

SizingModel 是整个系统未来最核心模块。

采用：

Golden Path 开发模式。

开发流程：

修改一个模块

↓

python main.py

↓

分析：

output/result.csv

↓

分析：

output/*.png

↓

git

↓

更新 docs

↓

进入下一功能

始终保持系统可运行。