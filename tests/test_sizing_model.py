from models.weather_model import WeatherModel
from models.pv_model import PVModel
from models.load_model import LoadModel
from models.sizing_model import SizingModel


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

weather.load(
    weather_path
)

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
# Sizing
# ======================================

sizing = SizingModel()


power_kw = 100


capacity_list = [

    20,
    40,
    60,
    80,
    100,
    150,
    200,
    300,
    500

]


result_df = (
    sizing.scan_capacity(
        pv_power=pv_power,
        load_power=load_power,
        power_kw=power_kw,
        capacity_list=capacity_list
    )
)


# ======================================
# Output
# ======================================

print()

print("========== Sizing Result ==========")

print()

print(result_df)