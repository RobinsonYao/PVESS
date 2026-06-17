import pandas as pd
import matplotlib.pyplot as plt

class ResultModel:
    """
    仿真结果模型

    battery_power:
        正 -> 放电
        负 -> 充电

    grid_power:
        正 -> 购电
        负 -> 上网
    """

    def __init__(self):
        self.df = None

    def build(
            self,
            datetime_index,
            pv_power,
            load_power,
            battery_power,
            soc,
            grid_power):
        """
        构建结果 DataFrame
        """

        self.df = pd.DataFrame({

            "datetime":
                pd.Series(datetime_index).values,

            "pv_power":
                pd.Series(pv_power).values,

            "load_power":
                pd.Series(load_power).values,

            "battery_power":
                pd.Series(battery_power).values,

            "soc":
                pd.Series(soc).values,

            "grid_power":
                pd.Series(grid_power).values

        })

    def to_dataframe(self):
        """
        返回整个 DataFrame
        """
        return self.df

    def head(self, n=5):
        """
        返回前 n 行
        """
        return self.df.head(n)

    def tail(self, n=5):
        """
        返回后 n 行
        """
        return self.df.tail(n)

    def show_info(self):
        """
        输出结果基本信息
        """

        if self.df is None:
            print("ResultModel is empty.")
            return

        print("\n========== Simulation Result ==========")

        print(f"Time steps : {len(self.df)}")

        print("\nColumns:")

        for col in self.df.columns:
            print(f"  {col}")

        print("=======================================\n")
    def export_csv(self, filepath):
        """
        导出 csv 文件

        Parameters
        ----------
        filepath : str
            输出文件路径
        """

        if self.df is None:
            print("ResultModel is empty.")
            return

        self.df.to_csv(filepath, index=False)

        print(f"Result exported to: {filepath}")
    def plot_soc(
            self,
            filepath="output/soc.png"):
        """
        保存 SOC 曲线
        """

        if self.df is None:
            print("ResultModel is empty.")
            return

        plt.figure(figsize=(10, 5))

        plt.plot(
            self.df["datetime"],
            self.df["soc"]
        )

        plt.xlabel("Time")

        plt.ylabel("SOC (%)")

        plt.title("SOC")

        plt.grid()

        plt.tight_layout()

        plt.savefig(
            filepath,
            dpi=300
        )

        print(
            f"SOC figure saved to: {filepath}"
        )

        plt.close()
    def plot_power(
        self,
        filepath="output/power.png"):
        """
        保存功率曲线
        """

        if self.df is None:
            print("ResultModel is empty.")
            return

        plt.figure(figsize=(12, 6))

        # PV
        plt.plot(
            self.df["datetime"],
            self.df["pv_power"],
            label="PV",
            color="blue",
            linewidth=2
        )

        # Load
        plt.plot(
            self.df["datetime"],
            self.df["load_power"],
            label="Load",
            color="black",
            linewidth=2
        )

        # Battery
        plt.plot(
            self.df["datetime"],
            self.df["battery_power"],
            label="Battery",
            color="green",
            linewidth=3
        )

        # Grid
        plt.plot(
            self.df["datetime"],
            self.df["grid_power"],
            label="Grid",
            color="red",
            linewidth=2
        )

        plt.xlabel("Time")

        plt.ylabel("Power (kW)")

        plt.title("Power")

        plt.grid()

        plt.legend()

        plt.tight_layout()

        plt.savefig(
            filepath,
            dpi=300
        )

        print(
            f"Power figure saved to: {filepath}"
        )

        plt.close()
    def plot_energy_balance(
        self,
        filepath="output/energy_balance.png"):
        """
        绘制能量平衡图

        PV + Battery + Grid = Load
        """

        if self.df is None:
            print("ResultModel is empty.")
            return

        supply = (
            self.df["pv_power"]
            + self.df["battery_power"]
            + self.df["grid_power"]
        )

        plt.figure(figsize=(12, 6))

        plt.plot(
            self.df["datetime"],
            supply,
            label="PV + Battery + Grid",
            linewidth=3
        )

        plt.plot(
            self.df["datetime"],
            self.df["load_power"],
            label="Load",
            linewidth=2
        )

        plt.xlabel("Time")

        plt.ylabel("Power (kW)")

        plt.title("Energy Balance")

        plt.grid()

        plt.legend()

        plt.tight_layout()

        plt.savefig(
            filepath,
            dpi=300
        )

        print(
            f"Energy balance figure saved to: {filepath}"
        )

        plt.close()