# Known Issues

---

## EMS V0.2 尚未 Freeze；

当前已实现：

- PV Self-consumption；
- Peak-Valley Arbitrage；
- Demand Control Skeleton；

需要进一步验证：

- battery_power；
- soc；
- grid_power；

Priority：

High。

## DoubleCycleModel 尚未建立。

需要：

- daily cycle；
- equivalent cycle；
- 一充一放；
- 两充两放；

Priority：

High。

## EconomicModel MVP 尚未建立。

需要：

- 峰谷套利收益；
- 光伏消纳收益；
- 年充放电量；
- 循环寿命成本；

Priority：

High。

## TOUModel Skeleton 尚未建立。

需要：

- 峰；
- 平；
- 谷；
- 尖峰；
- 深谷；
- 地区差异；
- 季节变化；

Priority：

Medium。

## TariffModel Skeleton 尚未建立。

需要：

- 购电电价；
- 上网电价；
- 容量电费；
- 需量电费；

Priority：

Medium。

## 当前采用：

print。

尚未建立：

logging

logs/

日志系统。

当前不影响开发。

Priority：

Low。

##  project_tree 已建立；

## ataModel V0.2 已建立。

当前需要：

长期验证接口稳定性。

避免频繁修改。

Priority：

Low。

## WeatherModel 仍保留部分数据入口功能。

后续逐步迁移至：

DataModel。

Priority：

Low。

## 当前大量 test_xxx.py 仍然保留。

尚未统一整理。

当前开发入口已经转移至：

python main.py

专项测试文件后续再整理。

Priority：

Low。