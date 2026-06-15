import pandas as pd
import matplotlib.pyplot as plt
from config.settings import DEBUG
from config.settings import DEBUG_TAGS

class WeatherModel:

    def __init__(self):

        # 原始10分钟数据
        self.df = None

        # 日尺度数据
        self.daily_ghi = None

        self.daily_temperature = None

        self.daily_wind_speed = None

    def load(self, file_path):

        # ======================
        # 读取 CSV 文件
        # ======================

        self.df = pd.read_csv(file_path)

        # Datetime 列转换为时间格式
        self.df["Datetime"] = pd.to_datetime(
            self.df["Datetime"]
        )

        # 设置时间索引
        self.df.set_index(
            "Datetime",
            inplace=True
        )
    def build_daily_data(self):

        """
        建立日尺度数据层
        """

        # ------------------------
        # 日辐照量（kWh/m²）
        # ------------------------

        self.daily_ghi = (
            self.df["GHI"]
            .resample("D")
            .sum()
            * 10
            / 60
            / 1000
        )

        # 去掉夜晚造成的0值
        self.daily_ghi = self.daily_ghi[
            self.daily_ghi > 0
        ]


        # ------------------------
        # 日平均温度
        # ------------------------

        self.daily_temperature = (
            self.df["Temperature"]
            .resample("D")
            .mean()
        )


        # ------------------------
        # 日平均风速
        # ------------------------

        self.daily_wind_speed = (
            self.df["Wind Speed"]
            .resample("D")
            .mean()
        )


        if DEBUG and "daily_data" in DEBUG_TAGS:

            print("========== 日尺度数据建立完成 ==========")

            print()

            print("日辐照量天数：")
            print(len(self.daily_ghi))

            print()

            print("温度天数：")
            print(len(self.daily_temperature))

            print()

            print("风速天数：")
            print(len(self.daily_wind_speed))

            print()

    def show_info(self):

        # ======================
        # 数据基本信息
        # ======================
        if DEBUG and "show_info" in DEBUG_TAGS: 
            print()
            print("========== 数据读取成功 ==========")

            print()
            print("记录数：")
            print(len(self.df))

            print()
            print("开始时间：")
            print(self.df.index.min())

            print()
            print("结束时间：")
            print(self.df.index.max())

            print()
            print("数据列：")
            print(self.df.columns.tolist())

            print()
            print("缺失值统计：")
            print(self.df.isnull().sum())

            print()

    def calculate_year_ghi(self):

        # ======================
        # 年总辐照量
        # ======================
        #
        # GHI单位：
        # W/m²
        #
        # 数据间隔：
        # 10分钟
        #
        # 1小时 = 6个点
        #
        # 因此：
        #
        # ΣGHI / 6 /1000
        #
        # 单位变成：
        #
        # kWh/m²
        #

        ghi_year = (
            self.df["GHI"]
            .resample("YE")
            .sum()
            / 6
            / 1000
        )

        if DEBUG and "year_ghi" in DEBUG_TAGS:

            print("========== 年总辐照量 ==========")

            print()

            for year, value in ghi_year.items():

                print(
                    f"{year.year} : "
                    f"{value:.1f} kWh/m²"
                )

            print()

            print(
                "五年平均年辐照量：",
                round(
                    ghi_year.mean(),
                    1
                ),
                "kWh/m²"
            )

            print()

        return ghi_year

    def calculate_month_ghi(self):

        # ======================
        # 月总辐照量
        # ======================

        month_ghi = (
            self.df["GHI"]
            .resample("ME")
            .sum()
            / 6
            / 1000
        )

        if DEBUG and "month_ghi" in DEBUG_TAGS:

            print()
            print("========== 月总辐照量 ==========")
            print()

            for date, value in month_ghi.items():

                print(
                    f"{date.strftime('%Y-%m')} : "
                    f"{value:.1f} kWh/m²"
                )

            print()

        return month_ghi
    def calculate_month_temperature(self):

        # ======================
        # 月平均气温
        # ======================
        #
        # Temperature 列单位：
        #
        # ℃
        #
        # resample("ME")
        # 表示按月统计
        #
        # mean()
        # 表示求平均值
        #

        month_temperature = (

            self.df["Temperature"]

            # 按月统计
            .resample("ME")

            # 求平均值
            .mean()

        )
        if DEBUG and "month_temperature" in DEBUG_TAGS:
            print()
            print("========== 月平均气温 ==========")
            print()

            for date, value in month_temperature.items():

                print(

                    f"{date.strftime('%Y-%m')} : "

                    f"{value:.1f} ℃"

                )

            print()

        return month_temperature
    def calculate_month_wind_speed(self):

        # ======================
        # 月平均风速
        # ======================
        #
        # Wind Speed 单位：
        #
        # m/s
        #
        # resample("ME")
        # 表示按月统计
        #
        # mean()
        # 表示求平均值
        #
        # 后续 PVModel 中
        # 风速将参与组件温度计算
        #

        month_wind_speed = (

            self.df["Wind Speed"]

            # 按月统计
            .resample("ME")

            # 求平均值
            .mean()

        )

        if DEBUG and "month_wind_speed" in DEBUG_TAGS:
            print()

            print("========== 月平均风速 ==========")

            print()

        # 遍历每个月数据
            for date, value in month_wind_speed.items():

                print(

                    f"{date.strftime('%Y-%m')} : "

                    f"{value:.2f} m/s"

                )

            print()

        # 返回 Series
        return month_wind_speed
    def get_day_data(self, date_string):

        # ======================
        # 获取某一天气象数据
        # ======================
        #
        # 输入：
        #
        # 2020-06-21
        #
        # 返回：
        #
        # 当天144个点的DataFrame
        #
        # 后续用于：
        #
        # 光伏功率曲线
        # 温度曲线
        # 风速曲线
        #

        day_df = self.df.loc[date_string]

        if DEBUG and "day_data" in DEBUG_TAGS:
            print()

            print("========== 典型日数据 ==========")

            print()

            print("日期：")

            print(date_string)

            print()

            print("数据点数量：")

            print(len(day_df))

            print()

            print(day_df.head())

            print()

        return day_df
    
    def get_period_data(
        self,
        start_date,
        end_date):
        """
        获取指定时间段数据

        Parameters
        ----------
        start_date : str

            例如：
            "2016-01-01"

        end_date : str

            例如：
            "2020-12-31"

        Returns
        -------
        DataFrame
        """

        period_df = self.df.loc[
            start_date:end_date
        ]

        return period_df


    def plot_day_ghi(self, date_string):

        # ======================
        # 绘制某日GHI曲线
        # ======================
        #
        # 输入：
        #
        # 2020-06-21
        #
        # 输出：
        #
        # GHI曲线图
        #

        day_df = self.df.loc[date_string]
        if DEBUG and "plot_day_ghi" in DEBUG_TAGS:
                plt.figure(
                    figsize=(12, 5)
                )

                plt.plot(

                    day_df.index,

                    day_df["GHI"]

                )

                plt.title(

                    f"GHI Curve - {date_string}"

                )

                plt.xlabel(
                    "Time"
                )

                plt.ylabel(
                    "GHI (W/m²)"
                )

                plt.grid(True)

                plt.tight_layout()

                plt.show()
# ==========================================
# 获取指定月份范围内的典型日
# month_list 例如：[3,4,5]
# ==========================================
    def get_typical_day(self, month_list):

        # 提取对应月份的数据
        # 先计算全部日期的日辐照量
        daily_ghi = self.daily_ghi

        # 再筛选指定月份
        daily_ghi = daily_ghi[
            daily_ghi.index.month.isin(month_list)
        ]

        # 计算这些天的平均日辐照量
        average_ghi = daily_ghi.mean()

        # 找出最接近平均值的日期
        typical_date = (
            abs(daily_ghi - average_ghi)
        ).idxmin()
        if DEBUG and "typical_day" in DEBUG_TAGS:
            print("\n========== 典型日 ==========")

            print("\n月份：")
            print(month_list)

            print("\n平均日辐照量：")
            print(round(average_ghi,2),"kWh/m²")

            print("\n典型日：")
            print(typical_date.date())

        return typical_date