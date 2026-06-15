from models.weather_model import WeatherModel
from models.pv_model import PVModel
from models.load_model import LoadModel
from models.battery_model import BatteryModel
from models.result_model import ResultModel


# ======================================
# Weather
# ======================================

weather_path = (
    "/Users/yaozhenhua/Documents/"
    "000-My Document/2024/"
    "241115-2016_2020 weather data/"
    "City/an_hui_an_qing.csv"
)

weather = WeatherModel()

weather.load(weather_path)

weather.build_daily_data()

day_df = weather.get_day_data(
    "2020-06-21"
)


# ======================================
# PV
# ======================================

pv = PVModel()

pv_power = pv.calculate(
    day_df
)


# ======================================
# Load
# ======================================

load = LoadModel()

load_power = load.generate(
    day_df.index
)


# ======================================
# Battery
# ======================================

battery = BatteryModel()

battery_power, soc, grid_power = (
    battery.simulate(
        pv_power,
        load_power
    )
)


# ======================================
# Result
# ======================================

result = ResultModel()

result.build(
    datetime_index=day_df.index,
    pv_power=pv_power,
    load_power=load_power,
    battery_power=battery_power,
    soc=soc,
    grid_power=grid_power
)

result.export_csv(
    "output/result.csv"
)

result.plot_soc()

result.plot_power()

result.plot_energy_balance()

print()

print("Simulation finished.")

print("Results saved to:")

print("output/result.csv")

print("output/soc.png")

print("output/power.png")


# ======================================
# Finish
# ======================================

print()

print("Simulation finished.")

print("Result saved to:")

print("output/result.csv")