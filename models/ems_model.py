import pandas as pd


class EMSModel:

    def __init__(self):
        pass

    def dispatch(
            self,
            pv_power,
            load_power):
        """
        自发自用策略

        Parameters
        ----------
        pv_power : Series

        load_power : Series

        Returns
        -------
        target_battery_power : Series

        正：放电

        负：充电
        """

        target_battery_power = (
            load_power
            - pv_power
        )

        return pd.Series(
            target_battery_power,
            index=pv_power.index
        )