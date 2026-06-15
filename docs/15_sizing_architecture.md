# Storage Sizing Architecture

---

# 1. 定位

PVESS 不仅是一个光储仿真工具。

项目最终目标是：

根据真实气象、负荷、光伏和运行策略，

自动确定：

* 储能功率（kW）
* 储能容量（kWh）

并进一步完成：

* 经济性分析；
* 寿命分析；
* 方案推荐；
* 自动报告生成。

因此：

Storage Sizing 是整个系统未来最核心的功能。

EMSModel、BatteryModel、EconomicModel、LifeModel 等模块，本质上都是为 SizingModel 服务的基础能力。

---

# 2. 核心问题

给定：

* Weather
* PV
* Load
* EMS Strategy

确定：

* Battery Power（kW）
* Battery Capacity（kWh）

即：

最佳储能配置。

工程上的核心问题不是：

“储能如何充放电？”

而是：

“储能应该配多大？”

---

# 3. 不存在脱离策略的最佳容量

最佳储能配置与控制策略强相关。

不存在脱离运行策略的最佳容量。

不同 EMS 对应不同的最佳配置。

例如：

自发自用策略：

50kW / 100kWh

峰谷套利：

100kW / 200kWh

削峰填谷：

150kW / 80kWh

备用电源：

80kW / 300kWh

因此：

最佳容量

=

f(负荷，光伏，EMS)

而不是：

f(负荷，光伏)

---

# 4. 系统架构

SizingModel 是顶层调度器。

系统结构：

SizingModel

├── EMSModel

├── BatteryModel

├── EconomicModel

├── LifeModel

└── ReportModel

其中：

EMSModel

负责：

控制策略。

BatteryModel

负责：

执行。

EconomicModel

负责：

经济性评价。

LifeModel

负责：

寿命评价。

ReportModel

负责：

自动生成结果。

---

# 5. 模块职责

## SizingModel

负责：

确定：

* power_kw
* capacity_kwh

不负责：

* 功率限制；
* SOC更新；
* 效率；
* Grid计算；
* 控制策略。

---

## EMSModel

负责：

产生：

target_battery_power。

属于：

决策层。

---

## BatteryModel

负责：

执行：

target_battery_power。

产生：

* actual_battery_power；
* SOC；
* grid_power。

属于：

执行层。

---

## ResultModel

负责：

观察系统运行结果。

输出：

* CSV；
* PNG。

属于：

观察层。

---

# 6. 输入

SizingModel 输入：

* pv_power
* load_power
* ems_model

未来扩展：

* electricity_price
* demand_charge
* battery_cost
* pv_cost

---

# 7. 输出

输出：

* optimal_power_kw
* optimal_capacity_kwh

未来扩展：

* annual_saving
* payback_period
* irr
* npv

---

# 8. V1.2

第一阶段：

固定功率。

扫描容量。

例如：

100kW

×

20kWh

40kWh

60kWh

...

500kWh

寻找收益开始饱和的位置。

---

# 9. V1.3

固定容量。

扫描功率。

例如：

100kWh

×

20kW

40kW

60kW

...

200kW

寻找收益开始饱和的位置。

---

# 10. V1.4

二维扫描：

功率 × 容量。

形成：

收益热力图。

得到：

optimal_power_kw

optimal_capacity_kwh。

---

# 11. V1.5

建立 EconomicModel。

计算：

* 电费；
* 年收益；
* 投资回收期；
* IRR；
* NPV。

---

# 12. V1.6

建立 LifeModel。

计算：

* 循环寿命；
* 日历寿命；
* SOH；
* 更换周期。

---

# 13. V2.0

建立多目标优化。

综合考虑：

* 收益；
* 寿命；
* 削峰；
* 需量；
* 电价。

形成：

综合最优配置。

---

# 14. V3.0

AI 辅助容量配置。

自动生成：

* 推荐功率；
* 推荐容量；
* 推荐策略；
* 推荐 PCS；
* 自动报告。

---

# 15. SOC 平衡约束

Sizing 中必须避免利用初始 SOC 获得虚假收益。

对于不同容量的比较：

要求：

SOC_end ≈ SOC_initial。

否则：

大容量电池会因为初始储能更多而产生虚假优势。

因此：

Sizing 应优先采用：

长期仿真。

例如：

月仿真；

年仿真；

多周期仿真。

而不是单日仿真。

---

# 16. 项目主线

PVESS 的长期主线：

Weather

↓

PV

↓

Load

↓

SizingModel

↓

EMSModel

↓

BatteryModel

↓

EconomicModel

↓

LifeModel

↓

Recommendation

↓

Report

其中：

SizingModel 是整个系统未来最核心的模块。

其余模块均服务于 SizingModel。

项目最终目标：

实现储能系统自动定型。
