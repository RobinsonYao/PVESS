from pathlib import Path

from models.data_model import DataModel
from models.weather_model import WeatherModel
from models.pv_model import PVModel
from models.ems_model import EMSModel
from models.battery_model import BatteryModel
from models.result_model import ResultModel


# ==================================================
# Path
# ==================================================

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_FILE = (
    PROJECT_ROOT
    / "tests"
    / "data"
    / "historical.csv"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "output"
)

OUTPUT_DIR.mkdir(
    exist_ok=True
)


# ==================================================
# Weather
# ==================================================

data_model = DataModel()


# ==================================================
# 获取时序数据
# ==================================================

df = data_model.load(
    DATA_FILE
)

time_index = df.index

ghi = df["ghi"]

load_power = df["load"]

tou_period = df["tou_period"]


# ==================================================
# PV
# ==================================================

pv_model = PVModel()

pv_power = (
    pv_model.calculate(
        ghi
    )
)


# ==================================================
# EMS
# ==================================================

ems_model = EMSModel(
    battery_power_kw=100,
    arbitrage_power=50
)

target_battery_power = (
    ems_model.dispatch(
        pv_power,
        load_power,
        tou_period
    )
)


# ==================================================
# Battery
# ==================================================

battery_model = BatteryModel()

(
    battery_power,
    soc,
    grid_power
) = (
    battery_model.execute_series(
        target_battery_power,
        pv_power,
        load_power
    )
)


# ==================================================
# Result
# ==================================================

result_model = ResultModel()

result_model.build(
    datetime_index=time_index,
    pv_power=pv_power,
    load_power=load_power,
    battery_power=battery_power,
    soc=soc,
    grid_power=grid_power
)

result_model.show_info()


# ==================================================
# Output
# ==================================================

result_model.export_csv(
    OUTPUT_DIR / "result.csv"
)

result_model.plot_soc(
    OUTPUT_DIR / "soc.png"
)

result_model.plot_power(
    OUTPUT_DIR / "power.png"
)

result_model.plot_energy_balance(
    OUTPUT_DIR / "energy_balance.png"
)


# ==================================================
# Finish
# ==================================================

print()

print(
    "Simulation finished."
)

print(
    "Result saved to output/"
)

print()