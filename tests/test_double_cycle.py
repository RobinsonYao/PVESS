from models.weather_model import WeatherModel
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


# ======================================
# Original Period
# ======================================

period_df = (
    weather.get_period_data(
        "2016-01-01",
        "2020-12-31"
    )
)


# ======================================
# Double Cycle
# ======================================

sizing = SizingModel()

double_df = (
    sizing.build_double_cycle(
        period_df
    )
)


# ======================================
# Output
# ======================================

print()

print("========== Original Period ==========")

print()

print(period_df.head())

print()

print(period_df.tail())

print()

print("Rows:")

print(
    len(period_df)
)


print()

print("========== Double Cycle ==========")

print()

print(double_df.head())

print()

print(double_df.tail())

print()

print("Rows:")

print(
    len(double_df)
)
print()

print("Start:")

print(
    double_df.index[0]
)

print()

print("Middle:")

print(
    double_df.index[
        len(period_df)
    ]
)

print()

print("End:")

print(
    double_df.index[-1]
)