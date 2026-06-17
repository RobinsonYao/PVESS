# Coding Convention

用于记录当前项目已经形成的代码风格。

目标：

保持代码风格稳定。

提高可读性。

方便长期维护。

不追求复杂规范。

---

# 1. Naming Convention

采用：

snake_case。

例如：

```python
battery_power

grid_power

current_soc

energy_change

soc_change
```

函数：

```python
calculate_year_ghi()

build_daily_data()

plot_day_ghi()

get_typical_day()
```

类：

采用 PascalCase。

例如：

```python
WeatherModel

PVModel

LoadModel

BatteryModel

ResultModel

EMSModel
```

常量：

未来采用：

全大写。

例如：

```python
DEBUG

PI

MAX_SOC
```
# 1.1 Column Naming Convention

DataFrame 列名统一采用：

snake_case。

全部小写。

单词之间使用：

下划线。

例如：

```python
datetime

temperature

ghi

wind_speed

load

tou_period

pv_power

battery_power

grid_power

current_soc


---

# 2. Variable Naming

优先：

完整表达意义。

允许：

变量名较长。

例如：

```python
current_soc

charge_efficiency

discharge_efficiency

battery_power

grid_power
```

避免：

过短变量。

例如：

```python
a

b

tmp

x
```

除循环变量：

```python
i

time
```

允许使用。

---

# 3. Function Naming

函数名采用：

动词 + 对象。

例如：

```python
load()

build_daily_data()

calculate_year_ghi()

calculate_month_temperature()

plot_day_ghi()
```

避免：

无意义名称。

例如：

```python
run()

do()

calc()
```

---

# 4. Class Naming

一个对象对应一个 Model。

采用：

对象名 + Model。

例如：

```python
WeatherModel

PVModel

LoadModel

BatteryModel

ResultModel

EMSModel
```

避免：

复杂继承体系。

避免：

Manager；

Factory；

Base；

Abstract。

---

# 5. Comment Convention

重视注释。

优先解释：

为什么。

变量意义。

单位。

正负号。

物理意义。

例如：

```python
# 最大充放电功率限制

# SOC下限保护

# 放电时，考虑放电效率

# Grid 正值表示购电
```

避免：

重复代码本身。

例如：

```python
# current_soc 加上 soc_change
current_soc += soc_change
```

这种注释意义较小。

---

# 6. Blank Line Style

模块之间：

两个空行。

函数之间：

两个空行。

逻辑块之间：

一个空行。

适当增加空行。

提高可读性。

不追求紧凑。

---

# 7. Line Length

优先：

可读性。

允许：

适当换行。

例如：

```python
energy_change = (
    battery_power[time]
    / self.discharge_efficiency
    / 6
)
```

避免：

一行过长。

---

# 8. Indentation

统一使用：

4个空格。

禁止：

Tab 和空格混用。

原因：

容易产生：

```text
IndentationError
```

VS Code 设置：

Tab Size = 4

Insert Spaces = true

---

# 9. Print Debug

Debug阶段：

允许：

大量 print。

例如：

```python
print()

print("SOC最后5个点")

print(
    soc.tail()
)
```

Freeze阶段：

逐步删除。

减少输出。

保持模块稳定。

---

# 10. Data Structure

核心数据结构：

Series

DataFrame

DatetimeIndex

统一使用：

pandas。

避免：

list；

dict；

numpy数组；

混杂使用。
# 10.1 Data Layer Convention

统一由：

DataModel

负责：

- csv读取；
- datetime转换；
- DatetimeIndex建立；
- 列名标准化。

输出：

标准 DataFrame。

Business Model

不直接读取 csv。

避免：

多个 Model 重复处理数据。

避免：

形成上帝对象。

---

# 11. Time Axis

统一时间轴：

DatetimeIndex。

当前时间间隔：

10分钟。

整个系统保持一致。

避免：

不同模块使用不同时间尺度。

---

# 12. Units

强调单位。

例如：

功率：

kW。

能量：

kWh。

SOC：

%。

辐照度：

W/m²。

辐照量：

kWh/m²。

温度：

℃。

风速：

m/s。

注释中尽量说明单位。

---

# 13. Power Sign Convention

统一约定：

PV Power：

正。

Load Power：

正。

Battery Power：

正：

放电。

负：

充电。

Grid Power：

正：

购电。

负：

上网。

SOC：

0~100%。

整个项目必须保持一致。

禁止：

局部重新定义正负号。

---

# 14. Function Length

优先：

简单。

可读。

建议：

50~100行以内。

超过：

150行。

考虑拆分。

不强制。

避免：

过度拆分。

---

# 15. Class Length

优先：

一个类对应一个对象。

允许：

逐步增长。

不提前拆分。

避免：

为了优雅而重构。

---

# 16. Module Division

采用：

一个对象一个文件。

例如：

```text
weather_model.py

pv_model.py

load_model.py

battery_model.py
```

避免：

一个文件包含大量对象。
# 16.1 Main.py Convention

main.py

作为系统唯一入口。

负责：

- 数据读取；
- 模型调用；
- 输出文件；
- 系统测试。

禁止：

将核心算法放入：

main.py。

算法应位于：

Model。

main.py

负责组织调用顺序。

不负责具体计算。

---

# 17. Error Handling

当前阶段：

优先：

暴露错误。

允许：

程序直接报错。

方便调试。

暂不追求：

复杂异常处理。

未来再增加：

try；

except。

---

# 18. Testing

当前采用：

python main.py

↓

result.csv

↓

png

↓

分析

↓

Debug

↓

Freeze

逐步验证。

专项测试：

保留：

tests/

未来逐步增加：

pytest。

单元测试。
# 18.1 Freeze Convention

模块稳定后：

优先 Freeze。

原则：

删除：

- print
- 临时变量
- 调试代码

保留：

- tests/
- docs/

保持：

接口稳定。

避免：

频繁重构。

优先：

增加新的 Model。

而不是：

修改稳定模块。

---

# 19. Logging

当前：

使用 print。

未来：

增加：

logging。

logs/

日志系统。

当前不提前实现。

---

# 20. File Organization

稳定目录。

避免频繁调整。

新增功能：

优先增加新的 Model。

而不是：

修改已有稳定模块。

# 20.1 Output Convention

统一输出目录：

output/

当前输出：

- result.csv
- soc.png
- power.png
- energy_balance.png

输出动作优先由：

main.py

完成。

避免：

多个模块分别保存文件。

保持输出结构统一。
---

# 21. Final Principle

正确性优先。

简单优先。

工程实用优先。

优先可读性。

优先长期维护。

保持风格稳定。

渐进式演化。

不要为了规范而改变已经稳定的代码。