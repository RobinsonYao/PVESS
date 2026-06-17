# Developer Profile

用于描述当前开发者的知识背景、开发习惯和协作方式。

不记录隐私信息。

目标：

帮助未来对话自动匹配解释深度。

---

# 1. Professional Background

开发者具有：

电力系统和新能源相关背景。

熟悉：

- 工商业光伏；
- 工商业储能；
- EMS；
- 峰平谷电价；
- 削峰填谷；
- 功率因数；
- 电池系统；
- 电力工程；

具有较强的工程经验。

项目目标偏向：

工程应用。

而不是：

学术研究。

---

# 2. Familiar Domains

较熟悉：

### 电力系统

- 功率流；
- 有功；
- 无功；
- 功率因数；
- 配电系统。

### 光伏系统

- PR；
- 自发自用；
- 余电上网；
- 工商业光伏。

### 储能系统

- PCS；
- EMS；
- SOC；
- 峰平谷套利；
- 削峰填谷；
- 电池寿命。

### 工程项目

- 项目建设；
- 技术方案；
- 经济分析；
- 商业模式。

### 数据分析

- Excel；
- 时间序列；
- 工程计算。

---

# 3. Less Familiar Domains

相对不熟悉：

### Python高级特性

例如：

- 装饰器；
- 元类；
- 生成器；
- 上下文管理器。

### 软件架构

例如：

- 设计模式；
- 大型框架；
- 微服务。

### 计算机理论

例如：

- 编译原理；
- 操作系统；
- 网络协议。

### 前端开发

例如：

- Web框架；
- JavaScript。

---

# 4. Current Python Level

当前水平：

初级向中级过渡。

已经理解：

- 变量；
- 函数；
- 类；
- import；
- self；
- pandas；
- DataFrame；
- Series；
- 时间索引。

正在逐步理解：

- 面向对象；
- 类之间关系；
- 状态机；
- 项目结构；
- Git。

尚未追求：

复杂语法。

---

# 5. Learning Style

采用：

项目驱动学习。

特点：

先做项目。

再学习知识。

通过实际问题理解概念。

不采用：

系统教材学习。

不追求：

一次掌握全部知识。

---

# 6. Preferred Explanation Depth

喜欢：

从工程角度解释。

先说明：

为什么。

再说明：

是什么。

最后说明：

怎么做。

优先：

物理意义。

状态机。

数据流。

变量意义。

避免：

直接讲语法。

---

# 7. Development Style

采用：

渐进式开发。

特点：

小步迭代。

逐步验证。

逐步理解。

先运行。

再优化。

不追求：

一次写完。
# 7.1 Main.py First Development

已经形成：

Golden Path 开发模式。

采用：

修改一个模块

↓

python main.py

↓

分析：

result.csv

↓

分析：

png

↓

Debug

↓

git

↓

更新 docs

↓

进入下一功能

优先保证：

系统整体可运行。

而不是：

优先追求测试覆盖率。

main.py

同时作为：

* 开发入口；
* 集成测试入口；
* 发布入口。

---

# 8. Acceptable Complexity

能够接受：

中等复杂度。

不希望：

复杂框架。

复杂设计模式。

复杂继承结构。

优先：

简单。

稳定。

容易理解。

---

# 9. Coding Habits

采用：

Python 工程风格。

习惯：

变量名较长。

大量注释。

强调物理意义。

强调单位。

强调正负号。

喜欢：

一步一步展开。

不喜欢：

过度压缩代码。

---

# 10. Debug Style

发现问题时：

优先：

print。

观察变量。

逐步定位。

逐步分析。

不采用：

整体重写。

不采用：

大量猜测。
# 10.1 Integration-first Debug

采用：

集成优先。

通过：

python main.py

进行系统验证。

当出现错误时：

优先：

定位接口；

观察数据流；

逐层分析；

逐步修复。

避免：

整体重写。

避免：

一次修改多个模块。

采用：

小步迭代。

逐层 Debug。

---

# 11. AI Collaboration Expectations

希望 AI：

帮助理解。

帮助分析。

帮助发现问题。

帮助优化。

而不是：

代替开发。

优先：

讨论算法。

讨论状态机。

讨论数据流。

最后再编码。

---

# 12. Class-Oriented Understanding

已经形成认知：

类是项目组织的核心。

一个对象对应一个 Model。

例如：

WeatherModel；

PVModel；

LoadModel；

BatteryModel；

EMSModel；

ResultModel。

随着项目推进，

逐步加深对类的理解。
# 12.1 Data-Oriented Understanding

逐步形成：

Data Layer

↓

Business Layer

↓

Result Layer

三层结构认知。

已经理解：

DataModel

负责：

* csv读取；
* datetime转换；
* DatetimeIndex；
* 列名标准化。

Business Model

负责：

状态和算法。

ResultModel

负责：

结果组织和输出。

逐步理解：

职责边界。

数据流。

模块解耦。

避免：

一个对象承担过多职责。

---

# 13. Long-term Goal

通过 PVESS 项目，

逐步学习：

Python；

面向对象；

工程化开发；

软件架构；

Git；

AI协同开发。

目标：

形成长期的软件开发能力。

而不仅完成一个项目。

---

# 14. Interaction Preference

喜欢：

多轮讨论。

逐步推进。

逐步验证。

允许：

边做边学。

优先：

理解。

而不是：

快速生成大量代码。

---

# 15. Overall Characteristics

工程思维较强。

抽象能力逐步建立。

适合：

长期演化项目。

适合：

AI协同开发。

项目驱动学习能力较强。

目标：

逐步成长为能够独立维护复杂工程的人。