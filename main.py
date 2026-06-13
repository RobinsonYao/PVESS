from models.weather_model import WeatherModel


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