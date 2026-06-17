# Development Rules

---

# Core Principles

优先：

正确性。

简单性。

工程实用性。

---

# Development Strategy

采用：

渐进式演化。

小步迭代。

逐步验证。

逐步 Freeze。

避免：

大规模重构。

---

# Architecture Principles

组合优于继承。

避免复杂设计模式。

避免过度抽象。

保持目录稳定。

保持接口稳定。

保持真实架构。

---

# Model Independence

模型不应该知道：

自己是否正在被测试。

模型只接受：

Series

DataFrame

参数

并返回计算结果。

模型不关心：

- csv来源；
- GUI；
- API；
- 测试数据；
- SizingModel；

从而保证模型可复用。

# Coding Principles

允许：

适当重复。

优先：

可读性。

可维护性。

可调试性。

不追求：

代码最短。

不追求：

理论最优。

---

# Data Layer Principle

系统采用：

Data Layer

↓

Business Layer

↓

Result Layer

三层结构。

其中：

DataModel

负责：

- csv读取；
- datetime转换；
- DatetimeIndex建立；
- 列名标准化。

输出：

标准 DataFrame。

Business Layer

负责：

算法和状态计算。

Result Layer

负责：

结果组织和输出。

# Module Principles

一个对象对应一个 Model。

main.py 负责调度。

算法放入 Model 内部。

新增功能优先增加新的 Model。

---

# Responsibility Boundary

main.py

负责：

- 数据读取；
- 模型调用；
- 输出文件；
- 系统测试。

models/

负责：

- 状态管理；
- 算法计算。

禁止：

- savefig()
- to_csv()
- print 调试信息
- 测试代码
- 示例代码

# Main.py First Principle

python main.py

是系统唯一入口。

同时作为：

- 开发入口；
- 集成测试入口；
- 发布入口。

采用：

Golden Path 开发模式。

任何功能修改后，

首先验证：

python main.py

能够正常运行。

# Development Workflow

开发流程：

修改一个模块

↓

python main.py

↓

检查：

output/result.csv

↓

检查：

- output/soc.png
- output/power.png
- output/energy_balance.png

↓

结果合理

↓

git commit

↓

更新 docs

↓

进入下一功能

始终保持系统处于可运行状态。

# Debug Strategy

优先：

print。

观察变量。

逐步定位。

避免：

整体重写。

---

# Freeze Strategy

验证正确后：

减少输出。

减少修改。

进入稳定状态。

---
# Freeze Principle

模块稳定后：

优先 Freeze。

原则：

不删除测试文件；

删除模块内部调试代码；

保持接口稳定；

避免频繁重构。

优先增加新 Model，

而不是修改已经稳定的 Model。

# Documentation Principles

docs 是项目的大脑。

代码是项目的身体。

Git 是项目的时间机器。

优先维护：

Project Memory。