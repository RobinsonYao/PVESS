# PVESS Architecture

main.py

↓

SimulationController

↓

WeatherModel

PVModel

LoadModel

BatteryModel

↓

Result

↓

EconomicModel

↓

Output

↓

GUI

原则：

* Model负责计算
* Controller负责调度
* Result负责数据传递
* View负责显示

目标：

建立一个持续演化的光储仿真平台。
