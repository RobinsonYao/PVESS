import pandas as pd


class PVModel:

    def __init__(self):

        self.capacity_kw = 100

        self.power = pd.Series()


    def calculate(
            self,
            weather_df
    ):

        self.power = (
            weather_df["GHI"]
            / 1000
            * self.capacity_kw
        )

        return self.power