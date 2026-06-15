import pandas as pd


class BatteryModel:

    def __init__(self):

        # 电池容量
        self.capacity_kwh = 200

        # 最大功率
        self.power_kw = 100

        # SOC上下限
        self.soc_max = 95
        self.soc_min = 10

        # 初始SOC
        self.soc_initial = 50
    def simulate(
            self,
            pv_power,
            load_power
    ):

        battery_power = pd.Series(
            index=pv_power.index,
            dtype=float
        )

        soc = pd.Series(
            index=pv_power.index,
            dtype=float
        )

        grid_power = pd.Series(
            index=pv_power.index,
            dtype=float
        )

        current_soc = self.soc_initial

        for time in pv_power.index:

            soc[time] = current_soc

        return (
            battery_power,
            soc,
            grid_power
        )