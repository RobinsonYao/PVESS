from models.weather_model import WeatherModel


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


period_df = (
    weather.get_period_data(
        "2016-01-01",
        "2020-12-31"
    )
)


print()

print("========== Period Data ==========")

print()

print(period_df.head())

print()

print(period_df.tail())

print()

print("Rows:")

print(
    len(period_df)
)