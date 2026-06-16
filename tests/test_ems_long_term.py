import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from models.ems_model import EMSModel


def test_ems_long_term():

    # ==========================================================
    # 时间轴（365天）
    # ==========================================================

    index = pd.date_range(
        start="2025-01-01",
        periods=365 * 24,
        freq="h"
    )

    n = len(index)

    # ==========================================================
    # 光伏功率
    # ==========================================================

    hour = index.hour

    pv_profile = np.maximum(
        0,
        np.sin(
            (hour - 6)
            * np.pi
            / 12
        )
    )

    pv_power = pd.Series(
        200 * pv_profile,
        index=index
    )

    # ==========================================================
    # 负荷功率
    # ==========================================================

    load_power = pd.Series(
        120.0,
        index=index
    )

    load_power.loc[
        (hour >= 8)
        &
        (hour <= 20)
    ] = 180

    # ==========================================================
    # 峰平谷
    # ==========================================================

    tou_period = pd.Series(
        "flat",
        index=index
    )

    tou_period.loc[
        (hour >= 0)
        &
        (hour < 7)
    ] = "valley"

    tou_period.loc[
        (hour >= 17)
        &
        (hour < 22)
    ] = "peak"

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
    #
    # 正：购电
    # 负：上网
    # ==========================================================

    grid_power = (
            load_power
            - pv_power
            - battery_power
    )

    # ==========================================================
    # 保存结果
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

    result_df.to_csv(
        "output/ems_long_term_results.csv"
    )

    # ==========================================================
    # 绘图（前7天）
    # ==========================================================

    plot_df = result_df.iloc[:24 * 7]

    plt.figure(
        figsize=(15, 8)
    )

    plt.plot(
        plot_df.index,
        plot_df["pv_power"],
        label="PV"
    )

    plt.plot(
        plot_df.index,
        plot_df["load_power"],
        label="Load"
    )

    plt.plot(
        plot_df.index,
        plot_df["battery_power"],
        label="Battery"
    )

    plt.plot(
        plot_df.index,
        plot_df["grid_power"],
        label="Grid"
    )

    plt.axhline(
        y=0,
        color="black"
    )

    plt.grid()

    plt.legend()

    plt.title(
        "EMS Long Term Test (First 7 Days)"
    )

    plt.tight_layout()

    plt.savefig(
        "output/ems_long_term_plot.png",
        dpi=300
    )

    plt.close()

    # ==========================================================
    # 年统计
    # ==========================================================

    annual_charge_energy = (
        battery_power[battery_power < 0]
        .abs()
        .sum()
    )

    annual_discharge_energy = (
        battery_power[battery_power > 0]
        .sum()
    )

    annual_purchase_energy = (
        grid_power[grid_power > 0]
        .sum()
    )

    annual_export_energy = (
        grid_power[grid_power < 0]
        .abs()
        .sum()
    )

    summary_df = pd.DataFrame(
        {
            "value": [
                annual_charge_energy,
                annual_discharge_energy,
                annual_purchase_energy,
                annual_export_energy
            ]
        },
        index=[
            "annual_charge_energy",
            "annual_discharge_energy",
            "annual_purchase_energy",
            "annual_export_energy"
        ]
    )

    summary_df.to_csv(
        "output/ems_long_term_summary.csv"
    )

    print()
    print(summary_df)


if __name__ == "__main__":

    test_ems_long_term()