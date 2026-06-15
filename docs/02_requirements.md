# Requirements

---

# 1. Project Objective

建立一个面向工商业光储系统的仿真平台。

支持：

- 光伏发电分析；
- 储能运行分析；
- EMS策略分析；
- 峰平谷套利分析；
- 削峰填谷分析；
- 电费收益分析；
- 电池寿命分析；
- 项目方案评估。

优先：

工程实用性。

不追求：

学术研究平台。

---

# 2. Input Data

系统输入包括：

---

## 气象数据

当前：

CSV 文件。

包含：

- GHI；
- DNI；
- DHI；
- 温度；
- 风速；
- 湿度；
- 压力；

时间分辨率：

10分钟。

---

## 系统参数

例如：

### 光伏参数

- 装机容量；
- PR；

### 电池参数

- 容量；
- 最大功率；
- SOC上下限；
- 充放电效率；

### EMS参数

- 峰平谷时段；
- 电价；
- 目标策略；

### 负荷参数

- 时序负荷曲线。

---

# 3. Output Results

输出：

时间序列结果。

包括：

- PV Power；
- Load Power；
- Battery Power；
- Grid Power；
- SOC。

未来增加：

- SOH；
- 收益；
- 电费；
- 循环次数。

---

# 4. Time Scale

统一时间尺度：

10分钟。

统一时间轴：

DatetimeIndex。

所有模块保持一致。

---

# 5. Power Sign Convention

统一规定：

PV：

正。

Load：

正。

Battery：

正：

放电。

负：

充电。

Grid：

正：

购电。

负：

上网。

整个工程保持一致。

---

# 6. Current Supported Functions

已经支持：

### Weather

- 气象数据读取；
- 日尺度数据；
- 年统计；
- 月统计；
- 典型日。

### PV

- 光伏输出。

### Load

- 时序负荷。

### Battery

- 功率限制；
- SOC限制；
- 效率；
- SOC更新。

### Result

框架已经建立。

---

# 7. Planned Functions

未来支持：

### EMS

- 自发自用；
- 峰平谷套利；
- 削峰填谷；
- 需量控制。

### Economic

- 电费；
- 收益；
- IRR；
- NPV。

### Life

- 循环寿命；
- 日历寿命；
- SOH。

### Report

自动生成分析报告。

---

# 8. User Focus Indicators

用户重点关注：

- 年发电量；
- 自发自用率；
- 上网电量；
- 储能利用率；
- 峰平谷收益；
- 削峰效果；
- 最大需量；
- 年收益；
- 回收期；
- 电池寿命。

---

# 9. Engineering Constraints

采用：

Python。

数据结构：

pandas。

时间驱动。

面向对象。

渐进开发。

保持目录稳定。

保持接口稳定。

---

# 10. Unsupported Scope

当前不支持：

- 潮流计算；
- 暂态仿真；
- 电磁仿真；
- BMS控制；
- PCS控制；
- 实时系统；
- 多机并行；
- 分布式计算。

---

# 11. Development Principle

优先：

正确性。

简单性。

工程实用性。

逐步演化。

避免：

复杂架构。

避免：

过度抽象。