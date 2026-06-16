import pandas as pd


class EMSModel:

    def __init__(
            self,
            arbitrage_power=0):
        """
        Parameters
        ----------
        arbitrage_power : float

            峰谷套利功率(kW)

            正值大小，不带方向
        """

        self.arbitrage_power = arbitrage_power

    @staticmethod
    def _get_self_consumption_power(
            pv_power,
            load_power):
        """
        自发自用功率

        Returns
        -------
        Series

        正：放电

        负：充电
        """

        return load_power - pv_power

    def _get_arbitrage_power(
            self,
            net_load,
            tou_period):
        """
        峰谷套利功率

        Parameters
        ----------
        net_load : Series

            load_power - pv_power

        tou_period : Series

            valley
            flat
            peak

        Returns
        -------
        Series

        正：放电

        负：充电
        """

        arbitrage_power = pd.Series(
            0.0,
            index=tou_period.index
        )

        # 谷时允许充电
        arbitrage_power.loc[
            tou_period == "valley"
        ] = -self.arbitrage_power

        # 峰时放电仅用于减少购电
        peak_mask = (
                (tou_period == "peak")
                &
                (net_load > 0)
        )

        arbitrage_power.loc[
            peak_mask
        ] = self.arbitrage_power

        return arbitrage_power

    def dispatch(
            self,
            pv_power,
            load_power,
            tou_period):
        """
        EMS调度

        Returns
        -------
        target_battery_power : Series

        正：放电

        负：充电
        """

        net_load = (
                load_power
                - pv_power
        )

        self_consumption_power = (
            self._get_self_consumption_power(
                pv_power,
                load_power
            )
        )

        arbitrage_power = (
            self._get_arbitrage_power(
                net_load,
                tou_period
            )
        )

        target_battery_power = (
                self_consumption_power
                + arbitrage_power
        )

        return pd.Series(
            target_battery_power,
            index=pv_power.index
        )