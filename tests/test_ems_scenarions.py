import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from models.ems_model import EMSModel


def test_ems_scenario():

    # ==========================================================
    # 时间轴
    # ==========================================================

    index = pd.date_range(
        "2025-01-01",
        periods=24,
        freq="h"
    )

    # ==========================================================
    # 光伏曲线
    # ==========================================================

    pv_power = pd.Series(
        [
            0, 0, 0, 0, 0, 0,
            20, 50, 100, 150, 200, 250,
            250, 200, 150, 100, 50, 20,
            0, 0, 0, 0, 0, 0
        ],
        index=index
    )

    # ==========================================================
    # 负荷曲线
    # ==========================================================

    load_power = pd.Series(
        [
            60, 60, 60, 60, 60, 60,
            80, 100, 120, 140, 160, 180,
            180, 180, 180, 180, 180, 180,
            150, 120, 100, 80, 70, 60
        ],
        index=index
    )

    # ==========================================================
    # 峰平谷时段
    # ==========================================================

    tou_period = pd.Series(
        [
            "valley", "valley", "valley", "valley",
            "valley", "valley", "valley",

            "flat", "flat", "flat", "flat",
            "flat", "flat", "flat", "flat",
            "flat", "flat",

            "peak", "peak", "peak", "peak", "peak",

            "valley", "valley"
        ],
        index=index
    )

    # ==========================================================
    # EMS
    # ==========================================================

    ems_model = EMSModel(
        arbitrage_power=100
    )

    battery_power = ems_model.dispatch(
        pv_power=pv_power,
        load_power=load_power,
        tou_period=tou_period
    )

    # ==========================================================
    # Grid Power
    # 正：购电
    # 负：上网
    # ==========================================================

    grid_power = (
            load_power
            - pv_power
            - battery_power
    )

    # ==========================================================
    # 输出结果
    # ==========================================================

    result_df = pd.DataFrame(
        {
            "pv_power": pv_power,
            "load_power": load_power,
            "battery_power": battery_power,
            "grid_power": grid_power,
            "tou_period": tou_period
        }
    )

    print()
    print(result_df)

    # ==========================================================
    # Plot 1
    # ==========================================================

    plt.figure(figsize=(12, 5))

    plt.plot(
        pv_power,
        label="PV"
    )

    plt.plot(
        load_power,
        label="Load"
    )

    plt.plot(
        battery_power,
        label="Battery"
    )

    plt.plot(
        grid_power,
        label="Grid"
    )

    plt.axhline(
        y=0,
        color="black"
    )

    plt.legend()

    plt.title(
        "EMS Scenario Test"
    )

    plt.grid()

    plt.show()


if __name__ == "__main__":

    test_ems_scenario()