import pandas as pd

from models.result_model import ResultModel


datetime_index = pd.date_range(
    start="2025-01-01 00:00:00",
    periods=5,
    freq="1h"
)

pv_power = [0, 0, 2, 5, 3]

load_power = [3, 4, 4, 6, 5]

battery_power = [-2, -1, 1, 2, 0]

soc = [52, 54, 53, 50, 50]

grid_power = [1, 3, 1, -1, 2]


result = ResultModel()

result.build(
    datetime_index,
    pv_power,
    load_power,
    battery_power,
    soc,
    grid_power
)

print(result.head())

print()

print(result.tail())

print()

result.show_info()
result.export_csv("output/test_result.csv")