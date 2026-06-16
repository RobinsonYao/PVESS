import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from models.ems_model import EMSModel
from models.battery_model import BatteryModel


def test_ems_battery_system():

    # ==========================================================
    # 时间轴（365天）
    # ==========================================================

    index = pd.date_range(
        start="2025-01-01",
        periods=365 * 24,
        freq="h"
    )

    hour = index.hour

    # ==========================================================
    # 光伏曲线
    # ==========================================================

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
    # 负荷曲线
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

    target_battery_power = (
        ems_model.dispatch(
            pv_power=pv_power,
            load_power=load_power,
            tou_period=tou_period
        )
    )

    # ==========================================================
    # Battery
    # ==========================================================

    battery_model = BatteryModel()

    (
        actual_battery_power,
        soc,
        grid_power
    ) = (
        battery_model.execute_series(
            target_battery_power,
            pv_power,
            load_power
        )
    )

    # ==========================================================
    # 保存详细结果
    # ==========================================================

    result_df = pd.DataFrame(
        {
            "pv_power": pv_power,
            "load_power": load_power,

            "target_battery_power": target_battery_power,

            "actual_battery_power": actual_battery_power,

            "soc": soc,

            "grid_power": grid_power,

            "tou_period": tou_period
        }
    )

    result_df.to_csv(
        "output/ems_battery_results.csv"
    )

    # ==========================================================
    # 年统计
    # ==========================================================

    annual_charge_energy = (
        actual_battery_power[
            actual_battery_power < 0
        ]
        .abs()
        .sum()
        / 6
    )

    annual_discharge_energy = (
        actual_battery_power[
            actual_battery_power > 0
        ]
        .sum()
        / 6
    )

    equivalent_cycles = (
        annual_discharge_energy
        / battery_model.capacity_kwh
    )

    annual_purchase_energy = (
        grid_power[
            grid_power > 0
        ]
        .sum()
        / 6
    )

    annual_export_energy = (
        grid_power[
            grid_power < 0
        ]
        .abs()
        .sum()
        / 6
    )

    summary_df = pd.DataFrame(
        {
            "value": [
                annual_charge_energy,
                annual_discharge_energy,
                equivalent_cycles,
                soc.min(),
                soc.max(),
                soc.iloc[-1],
                annual_purchase_energy,
                annual_export_energy
            ]
        },
        index=[
            "annual_charge_energy",
            "annual_discharge_energy",
            "equivalent_cycles",
            "soc_min",
            "soc_max",
            "final_soc",
            "annual_purchase_energy",
            "annual_export_energy"
        ]
    )

    summary_df.to_csv(
        "output/ems_battery_summary.csv"
    )

    print()
    print(summary_df)

    # ==========================================================
    # 前7天功率图
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
        plot_df["actual_battery_power"],
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
        "EMS + Battery (First 7 Days)"
    )

    plt.tight_layout()

    plt.savefig(
        "output/ems_battery_power_plot.png",
        dpi=300
    )

    plt.close()

    # ==========================================================
    # 前7天SOC图
    # ==========================================================

    plt.figure(
        figsize=(15, 4)
    )

    plt.plot(
        plot_df.index,
        plot_df["soc"]
    )

    plt.grid()

    plt.ylim(
        0,
        100
    )

    plt.title(
        "SOC (First 7 Days)"
    )

    plt.tight_layout()

    plt.savefig(
        "output/ems_battery_soc_plot.png",
        dpi=300
    )

    plt.close()


if __name__ == "__main__":

    test_ems_battery_system()