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

# Module Principles

一个对象对应一个 Model。

main.py 负责调度。

算法放入 Model 内部。

新增功能优先增加新的 Model。

---

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

# Documentation Principles

docs 是项目的大脑。

代码是项目的身体。

Git 是项目的时间机器。

优先维护：

Project Memory。