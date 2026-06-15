import pandas as pd


class ResultModel:

    def __init__(self):

        self.df = pd.DataFrame(
            columns=[
                "pv_power",
                "load_power",
                "battery_power",
                "soc",
                "grid_power"
            ]
        )


    def show_info(self):

        print()

        print("========== 仿真结果 ==========")

        print()

        print("数据点数量：")

        print(len(self.df))

        print()

        print("数据列：")

        print(self.df.columns.tolist())

        print()