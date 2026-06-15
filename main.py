from models.weather_model import WeatherModel
from models.battery_model import BatteryModel


weather_path = (
    "/Users/yaozhenhua/Documents/"
    "000-My Document/2024/"
    "241115-2016_2020 weather data/"
    "City/an_hui_an_qing.csv"
)

# 创建对象
weather = WeatherModel()

# 读取数据
weather.load(weather_path)
weather.build_daily_data()

# 显示数据基本信息
weather.show_info()

# 年辐照量
weather.calculate_year_ghi()

# 月辐照量
weather.calculate_month_ghi()
# 月平均温度
weather.calculate_month_temperature()
# 月平均风速
weather.calculate_month_wind_speed()
# 获取夏至数据
weather.get_day_data(
    "2020-06-21"
)
weather.plot_day_ghi(
    "2020-06-21"
)
weather.get_typical_day([3,4,5])

from models.result_model import ResultModel


result = ResultModel()

result.show_info()

from models.pv_model import PVModel
pv = PVModel()
day_df = weather.get_day_data(
    "2020-06-21"
)
pv_power = pv.calculate(
    day_df
)
print()

print("========== PV功率 ==========")

print()

print(pv_power.head())

from models.load_model import LoadModel
load = LoadModel()
load_power = load.generate(
    day_df.index
)
print()
print("========== 负载功率 ==========")
print()
print(load_power.head())

battery = BatteryModel()

battery_power, soc, grid_power = (
    battery.simulate(
        pv_power,
        load_power
    )
)
print()

print("========== Battery ==========")

print()

print(battery_power.head())

print()
print("========== SOC ==========")
print()
print(soc.head(144))
print()
print("========== Battery ==========")
print()
print(battery_power.head(144))