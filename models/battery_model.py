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

        # 充放电效率
        self.charge_efficiency = 0.95
        self.discharge_efficiency = 0.95

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
            # 根据功率差计算电池充放电功率，负数表示充电，正数表示放电
            battery_power[time] = -power_diff
            # 最大充放电功率限制
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

            
            # SOC上限保护
            if (
                battery_power[time] < 0
                and current_soc >= self.soc_max
            ):
                battery_power[time] = 0
            # 根据最终电池功率计算能量变化
            if battery_power[time] > 0:
                # 放电时，考虑放电效率，电池内部释放的能量比输出的功率更大（battery_power[time]已经在前面考虑了正负号，在此直接带入）
                energy_change = (
                    -battery_power[time]
                    / self.discharge_efficiency
                    / 6
                )
            else:
                # 充电时，考虑充电效率，电池内部吸收的能量比输入的功率小
                energy_change = (
                    -battery_power[time]
                    * self.charge_efficiency
                    / 6
                )
            # 计算SOC变化并更新SOC
            soc_change = (
                energy_change
                / self.capacity_kwh
                * 100
            )
            #更新SOC
            current_soc += soc_change
            current_soc = max(
                self.soc_min,
                min(
                    current_soc,
                    self.soc_max
                )
            )
            grid_power[time] = (
                load_power[time]
                - pv_power[time]
                - battery_power[time]
            )
            soc[time] = current_soc
        print("simulate() finished")
        print()

        print("SOC最后5个点")

        print(
            soc.tail()
        )

        print()

        print("Battery最后5个点")

        print(
            battery_power.tail()
        )

        print()

        print("Grid最后5个点")

        print(
            grid_power.tail()
        )
        print()

        print("PV最后5个点")

        print(
            pv_power.tail()
        )

        print()

        print("Load最后5个点")

        print(
            load_power.tail()
        )
        return (
            battery_power,
            soc,
            grid_power
        )
    