import pandas as pd


class DataModel:

    def __init__(self):

        self.df = None

    def load(
            self,
            file_path):

        self.df = pd.read_csv(
            file_path
        )

        # 标准化列名
        self.standardize_columns()

        # datetime
        self.df["datetime"] = (
            pd.to_datetime(
                self.df["datetime"]
            )
        )

        # 时间索引
        self.df.set_index(
            "datetime",
            inplace=True
        )

        return self.df
    
    def standardize_columns(self):
        """
        标准化列名

        Datetime
        →

        datetime

        Wind Speed
        →

        wind_speed
        """

        self.df.columns = (

            self.df.columns

            .str.strip()

            .str.lower()

            .str.replace(
                " ",
                "_"
            )

        )