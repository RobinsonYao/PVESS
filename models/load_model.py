import pandas as pd


class LoadModel:

    def __init__(self):

        self.load_power = pd.Series()


    def generate(
            self,
            time_index
    ):

        load_list = []

        for time in time_index:

            hour = time.hour

            if hour < 6:

                load = 30

            elif hour < 18:

                load = 80

            else:

                load = 50

            load_list.append(load)

        self.load_power = pd.Series(
            load_list,
            index=time_index
        )

        return self.load_power
    