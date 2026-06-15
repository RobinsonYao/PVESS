# Glossary

记录项目中的统一术语。

目标：

统一定义。

统一单位。

统一正负号。

避免不同模块采用不同解释。

---

# A

## AC

Alternating Current

交流电。

---

# B

## Battery

储能电池系统。

用于：

充放电。

调节功率。

能量转移。

---

## Battery Power

电池功率。

单位：

kW。

约定：

正：

放电。

负：

充电。

---

## BMS

Battery Management System

电池管理系统。

负责：

- 电芯保护；
- 均衡；
- SOC估算。

不属于当前仿真范围。

---

# C

## Cycle Life

循环寿命。

指：

电池能够完成的循环次数。

单位：

Cycle。

---

# D

## DHI

Diffuse Horizontal Irradiance

散射水平辐照度。

单位：

W/m²。

---

## DNI

Direct Normal Irradiance

法向直射辐照度。

单位：

W/m²。

---

# E

## EMS

Energy Management System

能量管理系统。

职责：

决定：

什么时候充电。

什么时候放电。

什么时候购电。

什么时候上网。

输出：

目标电池功率。

---

## Energy

能量。

单位：

kWh。

---

# G

## GHI

Global Horizontal Irradiance

总水平辐照度。

单位：

W/m²。

是光伏发电模型的主要输入。

---

## Grid Power

电网功率。

单位：

kW。

约定：

正：

购电。

负：

上网。

---

# L

## Load

负荷。

用户用电功率。

单位：

kW。

始终为正。

---

## Load Power

负载功率。

单位：

kW。

始终为正。

---

# P

## PCS

Power Conversion System

储能变流器。

负责：

交流和直流之间的能量转换。

不属于当前仿真范围。

---

## PR

Performance Ratio

性能比。

用于评价光伏系统性能。

---

## PV

Photovoltaic

光伏系统。

---

## PV Power

光伏输出功率。

单位：

kW。

始终为正。

---

# S

## SOC

State of Charge

荷电状态。

表示：

剩余电量百分比。

单位：

%。

范围：

0~100%。

当前系统：

10~95%。

---

## SOH

State of Health

健康状态。

表示：

电池剩余寿命。

单位：

%。

属于未来模型。

---

# T

## TOU

Time Of Use

分时电价。

包括：

峰；

平；

谷。

---

# U

## Self-consumption

自发自用。

优先利用光伏。

剩余电量：

充电。

不足部分：

购电。

---

# V

## Valley Charging

谷充。

利用低电价时段充电。

---

# P

## Peak Shaving

削峰。

降低最大功率。

减少需量费用。

---

## Peak-valley Arbitrage

峰谷套利。

利用峰谷电价差获取收益。

---

# F

## Fill Valley

填谷。

利用储能提高低负荷时段负荷。

---

# D

## Demand

需量。

某一统计周期内的最大平均功率。

单位：

kW。

---

## Demand Charge

需量电费。

根据最大需量计算。

---

# C

## Calendar Life

日历寿命。

即使不循环，

电池也会随时间衰减。

单位：

年。

---

# R

## Round-trip Efficiency

循环效率。

一次充放电的综合效率。

单位：

%。

---

# W

## Weather Engine

气象引擎。

负责：

读取气象数据。

生成：

辐照度；

温度；

风速；

典型日。

---

# Result

仿真结果对象。

统一保存：

- PV Power；
- Load Power；
- Battery Power；
- SOC；
- Grid Power。

---

# Power Sign Convention

整个工程统一约定：

PV Power：

正。

---

Load Power：

正。

---

Battery Power：

正：

放电。

负：

充电。

---

Grid Power：

正：

购电。

负：

上网。

---

Energy Change：

正：

能量增加。

负：

能量减少。

---

SOC Change：

正：

SOC增加。

负：

SOC减少。

---

# Unit Convention

功率：

kW。

能量：

kWh。

辐照度：

W/m²。

辐照量：

kWh/m²。

温度：

℃。

风速：

m/s。

SOC：

%。

SOH：

%。

循环寿命：

Cycle。

日历寿命：

Year。

---

本术语表适用于整个 PVESS 工程。

未来新增模块应优先遵循本文件定义。

禁止在局部重新定义术语和正负号。