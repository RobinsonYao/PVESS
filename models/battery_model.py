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

            power_diff = (
                pv_power[time]
                - load_power[time]
            )

            battery_power[time] = -power_diff
            if battery_power[time] > self.power_kw:

            battery_power[time] = self.power_kw

            if battery_power[time] < -self.power_kw:

            battery_power[time] = -self.power_kw
            # SOC下限保护
            if (
                battery_power[time] > 0
                and current_soc <= self.soc_min
            ):

                battery_power[time] = 0
            energy_change = (
                -battery_power[time]
                / 6
            )

            soc_change = (
                energy_change
                / self.capacity_kwh
                * 100
            )

            current_soc += soc_change
            soc[time] = current_soc
        return (
            battery_power,
            soc,
            grid_power
        )
    print("simulate() finished")