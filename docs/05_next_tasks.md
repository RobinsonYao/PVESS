# Priority 1
Battery + EMS 联合验证

目标：

验证：

battery_power；
soc；
grid_power。

输出：

result.csv；
soc.png；
power.png；
energy_balance.png。

确保：

python main.py

稳定运行。

逐步完成：

EMSModel V0.2 Freeze。

# Priority 2
DoubleCycleModel

建立：

daily_cycle；
equivalent_cycle。

进一步支持：

一充一放；
两充两放。

分析：

边际收益变化。

# Priority 3
EconomicModel MVP

建立：

峰谷套利收益；
光伏消纳收益；
年充放电量；
循环寿命成本。

形成：

EconomicModel MVP。

# Priority 4
TOUModel Skeleton

负责：

峰；
平；
谷；
尖峰；
深谷；
地区差异；
季节变化。
# Priority 5
TariffModel Skeleton

负责：

购电电价；
上网电价；
峰谷电价；
容量电费；
需量电费。
# Priority 6
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

储能功率（kW）

储能容量（kWh）

SizingModel 是整个系统未来最核心模块。

Development Strategy

采用：

Golden Path。

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

避免一次设计完成。

Known Issues
High
EMSModel V0.2 尚未 Freeze

当前已实现：

PV Self-consumption；
Peak-Valley Arbitrage；
Demand Control Skeleton。

需要进一步验证：

battery_power；
soc；
grid_power。
DoubleCycleModel 尚未建立

需要：

daily_cycle；
equivalent_cycle；
一充一放；
两充两放。
EconomicModel MVP 尚未建立

需要：

峰谷套利收益；
光伏消纳收益；
年充放电量；
循环寿命成本。
Medium
TOUModel Skeleton 尚未建立

需要：

峰；
平；
谷；
尖峰；
深谷；
地区差异；
季节变化。
TariffModel Skeleton 尚未建立

需要：

购电电价；
上网电价；
容量电费；
需量电费。
Low
logging 系统尚未建立

当前：

采用：

print()

未来建立：

logs/

logging

当前不影响开发。

DataModel V0.2 需要长期稳定性验证

避免频繁修改接口。

WeatherModel 仍保留部分数据入口功能

后续逐步迁移至：

DataModel。

tests/ 尚未统一整理

当前：

开发入口已经转移至：

python main.py

专项测试文件后续再整理。

Open Questions
DoubleCycleModel 属于哪一层？

尚未完全确定。

当前倾向：

统计层。

而不是：

决策层。

服务于：

EconomicModel；
LifeModel。
EconomicModel 与 EMS 的耦合关系

尚未最终确定。

需要进一步观察。

长期是否建立 logging 系统？

当前优先级较低。

暂不影响开发。