import pandas as pd


class PVModel:

    def __init__(self):

        # 装机容量（kW）
        self.capacity_kw = 100

        # 输出功率
        self.power = pd.Series(dtype=float)

    def calculate(
            self,
            ghi):
        """
        光伏功率计算

        Parameters
        ----------
        ghi : Series

            辐照度（W/m²）

        Returns
        -------
        power : Series

            光伏功率（kW）
        """

        self.power = (
            ghi
            / 1000
            * self.capacity_kw
        )

        return self.power
    