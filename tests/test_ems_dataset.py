from pathlib import Path
import sys

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent.parent
)

sys.path.append(
    str(PROJECT_ROOT)
)

import pandas as pd

from models.ems_model import EMSModel


# ==========================
# 读取测试数据
# ==========================
df = pd.read_csv(
    "tests/data/test_dataset.csv"
)

# datetime 转换
df["datetime"] = pd.to_datetime(
    df["datetime"]
)


# ==========================
# 简单构造 PV 功率
# (先用 GHI 近似)
# ==========================
pv_capacity_kw = 100

df["pv_power"] = (
    df["ghi"]
    / 1000
    * pv_capacity_kw
)


# ==========================
# EMS
# ==========================
ems = EMSModel(
    battery_power_kw=100,
    arbitrage_power=50
)

battery_power = ems.dispatch(
    pv_power=df["pv_power"],
    load_power=df["load"],
    tou_period=df["tou_period"]
)

df["battery_power"] = battery_power


# ==========================
# 电网功率
# 正：购电
# 负：上网
# ==========================
df["grid_power"] = (
    df["load"]
    -
    df["pv_power"]
    -
    df["battery_power"]
)


# ==========================
# 输出结果
# ==========================
output_columns = [
    "dataset",
    "datetime",
    "temperature",
    "ghi",
    "pv_power",
    "load",
    "tou_period",
    "battery_power",
    "grid_power"
]

df[
    output_columns
].to_csv(
    "output/ems_test_result.csv",
    index=False
)

print(
    "Result saved to output/ems_test_result.csv"
)