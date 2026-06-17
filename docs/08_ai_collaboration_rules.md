# AI Collaboration Rules

用于规范 AI 与开发者之间的协作方式。

目标：

保持长期开发过程中的一致性。

避免上下文切换导致开发风格变化。

---

# 1. Collaboration Philosophy

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

---

# 2. Standard Development Process

采用：

理解问题

↓

讨论算法

↓

设计结构

↓

实现代码

↓

调试

↓

Freeze

↓

继续扩展

禁止：

直接进入大量编码。

---

# 3. Algorithm First

优先：

算法。

其次：

结构。

最后：

代码。

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

先写代码，

再理解算法。

---

# 4. Small Increment Strategy

采用：

小步迭代。

每次：

只增加一个功能。

每次：

只修改少量代码。

每完成一步：

立即运行。

立即验证。

避免：

一次性生成大量代码。

避免：

大规模修改。
# 4.1 Main.py First Principle

采用：

Golden Path 开发模式。

python main.py

作为：

* 开发入口；
* 集成测试入口；
* 发布入口。

优先保证：

系统整体可运行。

而不是：

优先追求测试覆盖率。

任何功能修改后，

首先验证：

python main.py

能够正常运行。

随后再进行：

专项测试。

---

# 5. Incremental Modification

优先：

增量修改。

而不是：

整体重写。

保持：

已有代码结构。

保持：

已有接口。

保持：

已有目录。

避免：

因为追求优雅而重构。

---

# 6. Rebuild Only When Necessary

只有：

发现错误；

增加功能；

收益明确；

时才允许重构。

重构前：

先说明：

为什么重构。

收益是什么。

可能影响哪些模块。

禁止：

默认重构。

禁止：

频繁调整目录。

禁止：

频繁改变接口。

---

# 7. Keep Architecture Stable

保持：

目录稳定。

接口稳定。

类职责稳定。

优先：

真实架构。

而不是：

理想架构。

避免：

为了设计而设计。

---

# 8. Prefer Simplicity

优先：

简单。

可读。

容易调试。

允许：

适当重复。

不追求：

复杂设计模式。

不追求：

高度抽象。

不追求：

一次到位。

---

# 9. Respect Existing Code

默认：

已有代码是正确的。

新增功能时：

优先在现有基础上扩展。

不要：

自动重写整个文件。

不要：

自动改变变量名。

不要：

自动改变目录结构。

不要：

自动引入复杂框架。
# 9.1 Respect Existing Models

默认：

已有 Model 是正确的。

优先：

调整 main.py。

而不是：

重构已有 Model。

重构前：

先说明：

收益；

影响范围；

是否值得。

禁止：

为了理想架构，

自动重写稳定模块。

优先：

真实架构。

而不是：

理想架构。

---

# 10. Explain Before Coding

复杂问题：

先讨论。

先推导。

先确认。

再编码。

必要时：

先画流程。

先分析状态机。

避免：

直接输出大量代码。

---

# 11. Developer Participation

允许开发者：

自己编写代码。

自己调试。

自己修改。

AI 的职责：

帮助理解。

帮助分析。

帮助发现问题。

帮助优化。

而不是：

代替开发。

---

# 12. Debugging Strategy

发现问题时：

优先：

增加 print。

查看变量。

查看状态。

逐步定位。

避免：

整体重写。

避免：

盲目修改。

采用：

一步一步验证。
# 12.1 Integration-first Strategy

优先：

系统集成验证。

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

避免：

同时修改多个模块。

避免：

整体重写。

采用：

逐层 Debug。

逐步修复。

---

# 13. Freeze Strategy

算法验证完成后：

进入 Freeze 状态。

减少：

print；

临时变量；

调试代码。

稳定模块：

尽量不修改。

只有：

发现错误；

增加功能；

收益明确；

时才修改。

---

# 14. Understanding Variables

优先理解：

变量含义。

变量单位。

变量正负号。

变量物理意义。

优先理解：

数据流。

状态机。

功率流。

能量流。

避免：

只理解代码语法。

---

# 15. Class-Oriented Thinking

项目采用：

面向对象方式。

一个对象对应一个 Model。

例如：

WeatherModel；

PVModel；

LoadModel；

BatteryModel；

EMSModel；

ResultModel。

类负责：

维护状态。

完成计算。

输出结果。

避免：

全部写入 main.py。

避免：

单文件脚本。
# 15.1 Data Layer Principle

项目逐步形成：

Data Layer

↓

Business Layer

↓

Result Layer

三层结构。

DataModel

负责：

* csv读取；
* datetime转换；
* DatetimeIndex；
* 列名标准化。

Business Layer

负责：

状态和算法。

Result Layer

负责：

结果组织和输出。

避免：

单个对象承担过多职责。

避免：

形成上帝对象。

---

# 16. Cross-Conversation Continuity

优先保持：

Project Memory。

未来开启新对话时：

优先读取：

docs/

恢复项目认知。

避免：

重新解释整个项目。

---

# 17. Coding Style

优先：

工程风格。

而不是：

竞赛风格。

代码要求：

容易阅读；

容易调试；

容易维护；

容易扩展。

---

# 18. Preferred Interaction Style

开发过程中：

允许：

多轮讨论。

逐步推进。

逐步验证。

不要求：

一次得到最终答案。

项目采用：

长期演化模式。

而不是：

一次性交付模式。

---

# 19. Final Principle

先理解。

再设计。

最后编码。

docs 是项目的大脑。

代码是项目的身体。

Git 是项目的时间机器。

Project Memory 是长期开发能力的核心。

2026年06月16日11:19:12
推荐开发流程：

讨论

↓

实现

↓

python main.py

↓

输出：

result.csv

↓

输出：

png

↓

分析结果

↓

Debug

↓

git

↓

更新 docs

↓

Freeze

↓

进入下一模块

始终保持：

系统可运行。

2026年06月18日

形成：

DataModel

↓

Business Layer

↓

Result Layer

三层结构。

形成：

main.py Golden Path

开发模式。

系统进入稳定演化阶段。