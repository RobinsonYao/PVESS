import pandas as pd

from models.ems_model import EMSModel
from models.battery_model import BatteryModel


class SizingModel:

    def __init__(self):

        pass

    def build_double_cycle(
            self,
            df):
            """
            构建双周期数据

            Parameters
            ----------
            df : DataFrame

                原始周期数据

            Returns
            -------
            double_df : DataFrame

                双周期连续数据
            """

            # 第一周期
            df1 = df.copy()

            # 第二周期
            df2 = df.copy()

            # 一个时间步长（10分钟）
            time_step = (
                df.index[1]
                - df.index[0]
            )

            # 周期长度
            time_shift = (
                len(df)
                * time_step
            )

            # 第二周期整体后移
            df2.index = (
                df2.index
                + time_shift
            )

            # 拼接
            double_df = pd.concat(
                [
                    df1,
                    df2
                ]
            )

            return double_df

def scan_capacity(
        self,
        pv_power,
        load_power,
        power_kw,
        capacity_list):
        """
        固定功率，扫描容量

        Parameters
        ----------
        pv_power : Series

        load_power : Series

        power_kw : float

            固定储能功率

        capacity_list : list

            储能容量列表

        Returns
        -------
        DataFrame
        """

        result_list = []

        for capacity_kwh in capacity_list:

            # EMS
            ems = EMSModel()

            target_battery_power = (
                ems.dispatch(
                    pv_power,
                    load_power
                )
            )

            # Battery
            battery = BatteryModel()

            battery.power_kw = power_kw

            battery.capacity_kwh = capacity_kwh

            battery_power, soc, grid_power = (
                battery.execute_series(
                    target_battery_power,
                    pv_power,
                    load_power
                )
            )

            # 购电量（kWh）
            import_energy = (
                grid_power
                .clip(lower=0)
                .sum()
                / 6
            )

            # 上网电量（kWh）
            export_energy = (
                (-grid_power)
                .clip(lower=0)
                .sum()
                / 6
            )

            # 光伏发电量（kWh）
            pv_energy = (
                pv_power.sum()
                / 6
            )

            # 自发自用量（kWh）
            self_consumption_energy = (
                    pv_energy
                    - export_energy
            )

            # 自发自用率
            if pv_energy > 0:

                self_consumption_ratio = (
                        self_consumption_energy
                        / pv_energy
                )

            else:

                self_consumption_ratio = 0

            result_dict = {

                "power_kw":
                    power_kw,

                "capacity_kwh":
                    capacity_kwh,

                "import_energy_kwh":
                    import_energy,

                "export_energy_kwh":
                    export_energy,

                "self_consumption_ratio":
                    self_consumption_ratio

            }

            result_list.append(
                result_dict
            )

        return pd.DataFrame(
            result_list
        )