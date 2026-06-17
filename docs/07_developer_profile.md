# Developer Profile

用于描述开发者背景、开发风格和 AI 协作原则。

目标：

帮助未来对话自动匹配解释深度。

保持长期开发过程中的一致性。

不记录隐私信息。

# 1. Professional Background

开发者具有：

电力系统和新能源相关背景。

熟悉：

工商业光伏；
工商业储能；
EMS；
峰平谷电价；
削峰填谷；
功率因数；
电池系统；
电力工程。

项目目标偏向：

工程应用。

而不是：

学术研究。

# 2. Familiar Domains

较熟悉：

电力系统
功率流；
有功；
无功；
功率因数；
配电系统。
光伏系统
PR；
自发自用；
余电上网；
工商业光伏。
储能系统
PCS；
EMS；
SOC；
峰谷套利；
削峰填谷；
电池寿命。
工程项目
项目建设；
技术方案；
经济分析；
商业模式。
数据分析
Excel；
时间序列；
工程计算。
# 3. Less Familiar Domains

相对不熟悉：

Python高级特性
装饰器；
元类；
生成器；
上下文管理器。
软件架构
设计模式；
大型框架；
微服务。
计算机理论
编译原理；
操作系统；
网络协议。
前端开发
Web框架；
JavaScript。
# 4. Current Python Level

当前水平：

初级向中级过渡。

已经理解：

类；
import；
pandas；
DataFrame；
Series；
DatetimeIndex。

正在逐步理解：

面向对象；
类之间关系；
状态机；
项目结构；
Git。
# 5. Learning Style

采用：

项目驱动学习。

特点：

先做项目。

再学习知识。

通过实际问题理解概念。

不采用：

系统教材学习。

# 6. Preferred Explanation Depth

喜欢：

先说明：

为什么。

再说明：

是什么。

最后说明：

怎么做。

优先：

物理意义；
状态机；
数据流；
变量意义。

避免：

直接讲语法。

# 7. Development Style

采用：

渐进式开发。

特点：

小步迭代；
逐步验证；
先运行；
再优化。
# 8. Acceptable Complexity

优先：

简单；
稳定；
易理解。

不追求：

复杂框架；
高度抽象；
复杂设计模式。

允许：

适度重复。

# 9. Coding Habits

特点：

变量名较长；
大量注释；
强调物理意义；
强调单位；
强调正负号。

不喜欢：

过度压缩代码。

# 10. Debug Style

发现问题时：

优先：

print；
观察变量；
逐层定位；
逐步分析。

避免：

整体重写。

# 11. AI Collaboration Philosophy

项目采用：

渐进式开发。

优先：

理解问题。

而不是：

快速生成代码。

优先：

工程实用性。

而不是：

理论上的完美设计。

# 12. Algorithm First

顺序：

问题

↓

状态机

↓

变量

↓

数据流

↓

类

↓

函数

↓

代码

避免：

先写代码。

再理解算法。

# 13. Small Increment Strategy

每次：

只增加一个功能。

每次：

只修改少量代码。

立即运行。

立即验证。

避免：

一次性生成大量代码。

避免：

大规模修改。

# 14. Main.py First Principle

采用：

Golden Path 开发模式。

python main.py

作为：

开发入口；
集成测试入口；
发布入口。

优先保证：

系统整体可运行。

而不是：

优先追求测试覆盖率。

# 15. Integration-first Debug

采用：

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

定位问题

↓

Debug

↓

Freeze

↓

进入下一功能

采用：

逐层 Debug。

逐步修复。

# 16. Respect Existing Code

默认：

已有代码是正确的。

优先：

增量修改。

而不是：

整体重写。

保持：

接口稳定；
目录稳定；
类职责稳定。

避免：

为了理想架构而重构。

# 17. Freeze Strategy

模块稳定后：

进入 Freeze。

减少：

print；
调试代码；
临时变量。

优先：

增加新 Model。

而不是：

频繁修改稳定模块。

# 18. Class-Oriented Understanding

一个对象对应一个 Model。

例如：

DataModel；
WeatherModel；
PVModel；
EMSModel；
BatteryModel；
ResultModel。

类负责：

维护状态。

完成计算。

# 19. Data-Oriented Understanding

形成：

Data Layer

↓

Business Layer

↓

Result Layer

三层结构。

其中：

DataModel

负责：

数据组织。

Business Layer

负责：

状态和算法。

Result Layer

负责：

结果组织和输出。

避免：

形成上帝对象。

# 20. Preferred Interaction Style

允许：

多轮讨论。

逐步推进。

逐步验证。

不要求：

一次得到最终答案。

项目采用：

长期演化模式。

# 21. Long-term Goal

通过 PVESS 项目，

逐步学习：

Python；
面向对象；
软件架构；
Git；
AI 协同开发。

目标：

形成长期的软件开发能力。

# 22. Final Principle

先理解。

再设计。

最后编码。

docs 是项目的大脑。

代码是项目的身体。

Git 是项目的时间机器。

Project Memory 是长期开发能力的核心。

2026-06-18

形成：

DataModel

↓

Business Layer

↓

Result Layer

三层结构。

形成：

python main.py

Golden Path。

系统进入稳定演化阶段。