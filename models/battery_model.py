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
    
    def execute(
        self,
        target_battery_power,
        current_soc,
        pv_power,
        load_power):
        """
        执行 EMS 下发的目标功率

        Parameters
        ----------
        target_battery_power : float

            正：放电

            负：充电

        current_soc : float

        pv_power : float

        load_power : float

        Returns
        -------
        actual_battery_power

        next_soc

        grid_power
        """

        actual_battery_power = target_battery_power

        # 最大功率限制
        if actual_battery_power > self.power_kw:
            actual_battery_power = self.power_kw

        if actual_battery_power < -self.power_kw:
            actual_battery_power = -self.power_kw

        # SOC下限保护
        if (
                actual_battery_power > 0
                and current_soc <= self.soc_min
        ):
            actual_battery_power = 0

        # SOC上限保护
        if (
                actual_battery_power < 0
                and current_soc >= self.soc_max
        ):
            actual_battery_power = 0

        # 能量变化
        if actual_battery_power > 0:

            energy_change = (
                    -actual_battery_power
                    / self.discharge_efficiency
                    / 6
            )

        else:

            energy_change = (
                    -actual_battery_power
                    * self.charge_efficiency
                    / 6
            )

        soc_change = (
                energy_change
                / self.capacity_kwh
                * 100
        )

        next_soc = current_soc + soc_change

        next_soc = max(
            self.soc_min,
            min(
                next_soc,
                self.soc_max
            )
        )

        grid_power = (
                load_power
                - pv_power
                - actual_battery_power
        )

        return (
            actual_battery_power,
            next_soc,
            grid_power
        )
    def execute_series(
            self,
            target_battery_power,
            pv_power,
            load_power):
        """
        批量执行 EMS 下发的目标功率

        Parameters
        ----------
        target_battery_power : Series

            正：放电

            负：充电

        pv_power : Series

        load_power : Series

        Returns
        -------
        battery_power

        soc

        grid_power
        """

        battery_power = pd.Series(
            index=target_battery_power.index,
            dtype=float
        )

        soc = pd.Series(
            index=target_battery_power.index,
            dtype=float
        )

        grid_power = pd.Series(
            index=target_battery_power.index,
            dtype=float
        )

        current_soc = self.soc_initial

        # ==================================
        # 逐时间步执行
        # ==================================
        for i in range(len(target_battery_power)):

            (
                actual_battery_power,
                next_soc,
                grid_power_value
            ) = (
                self.execute(
                    target_battery_power.iloc[i],
                    current_soc,
                    pv_power.iloc[i],
                    load_power.iloc[i]
                )
            )

            battery_power.iloc[i] = (
                actual_battery_power
            )

            soc.iloc[i] = (
                next_soc
            )

            grid_power.iloc[i] = (
                grid_power_value
            )

            current_soc = (
                next_soc
            )

        return (
            battery_power,
            soc,
            grid_power
        )