import pandas as pd


class EMSModel:

    def __init__(
            self,
            battery_power_kw=100,
            arbitrage_power=50,
            demand_limit_kw=None):
        """
        Parameters
        ----------
        battery_power_kw

            电池额定功率(kW)

        arbitrage_power

            峰谷套利功率(kW)

        demand_limit_kw

            需量上限(kW)
        """

        self.battery_power_kw = (
            battery_power_kw
        )

        self.arbitrage_power = (
            arbitrage_power
        )

        self.demand_limit_kw = (
            demand_limit_kw
        )

    def _get_self_consumption_power(
            self,
            pv_power,
            load_power):
        """
        光伏消纳

        仅吸收富余光伏

        Returns
        -------
        Series

        正：放电

        负：充电
        """

        pv_surplus = (
            pv_power
            -
            load_power
        )

        self_consumption_power = (
            -pv_surplus.clip(
                lower=0,
                upper=self.battery_power_kw
            )
        )

        return self_consumption_power

    def _get_arbitrage_power(
            self,
            net_load,
            tou_period):
        """
        峰谷套利

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

        # 谷时充电
        valley_mask = (
                tou_period
                ==
                "valley"
        )

        arbitrage_power.loc[
            valley_mask
        ] = (
            -self.arbitrage_power
        )

        # 峰时放电
        peak_mask = (
                (tou_period == "peak")
                &
                (net_load > 0)
        )

        arbitrage_power.loc[
            peak_mask
        ] = (
            net_load.loc[
                peak_mask
            ].clip(
                upper=self.arbitrage_power
            )
        )

        return arbitrage_power

    def _get_demand_control_power(
            self,
            net_load):
        """
        需量控制

        Skeleton

        Returns
        -------
        Series

        正：放电
        """

        demand_control_power = pd.Series(
            0.0,
            index=net_load.index
        )

        if self.demand_limit_kw is None:

            return demand_control_power

        excess_load = (
                net_load
                -
                self.demand_limit_kw
        )

        demand_control_power = (
            excess_load.clip(
                lower=0,
                upper=self.battery_power_kw
            )
        )

        return demand_control_power

    def _merge_power(
            self,
            self_consumption_power,
            arbitrage_power,
            demand_control_power):
        """
        优先级：

        Constraint Protection
        ↓
        PV Self-consumption
        ↓
        Peak-Valley Arbitrage
        """

        target_power = pd.Series(
            0.0,
            index=self_consumption_power.index
        )

        #
        # 1 需量控制
        #
        target_power = (
            target_power
            +
            demand_control_power
        )

        #
        # 2 光伏消纳
        #
        remain_charge_power = (
            self.battery_power_kw
            +
            target_power.clip(
                upper=0
            )
        )

        pv_charge = (
            self_consumption_power.clip(
                upper=0
            )
        )

        pv_charge = (
            pv_charge.clip(
                lower=-remain_charge_power
            )
        )

        target_power = (
            target_power
            +
            pv_charge
        )

        #
        # 3 峰谷套利
        #
        remain_discharge_power = (
            self.battery_power_kw
            -
            target_power.clip(
                lower=0
            )
        )

        remain_charge_power = (
            self.battery_power_kw
            +
            target_power.clip(
                upper=0
            )
        )

        arbitrage_discharge = (
            arbitrage_power.clip(
                lower=0
            )
        )

        arbitrage_charge = (
            arbitrage_power.clip(
                upper=0
            )
        )

        arbitrage_discharge = (
            arbitrage_discharge.clip(
                upper=remain_discharge_power
            )
        )

        arbitrage_charge = (
            arbitrage_charge.clip(
                lower=-remain_charge_power
            )
        )

        target_power = (
                target_power
                +
                arbitrage_discharge
                +
                arbitrage_charge
        )

        #
        # 最终限幅
        #
        target_power = (
            target_power.clip(
                lower=-self.battery_power_kw,
                upper=self.battery_power_kw
            )
        )

        return target_power

    def dispatch(
            self,
            pv_power,
            load_power,
            tou_period):
        """
        EMS调度

        Returns
        -------
        Series

        正：放电

        负：充电
        """

        net_load = (
                load_power
                -
                pv_power
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

        demand_control_power = (
            self._get_demand_control_power(
                net_load
            )
        )

        target_power = (
            self._merge_power(
                self_consumption_power,
                arbitrage_power,
                demand_control_power
            )
        )

        return pd.Series(
            target_power,
            index=pv_power.index
        )