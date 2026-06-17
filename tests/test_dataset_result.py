import pandas as pd

from models.pv_model import PVModel
from models.ems_model import EMSModel
from models.battery_model import BatteryModel
from models.result_model import ResultModel


def main():

    # ======================================
    # 读取测试数据
    # ======================================

    #df = pd.read_csv(
    #   "tests/data/test_dataset.csv"
    #)

    df = pd.read_csv(
    "tests/data/test_dataset_charge.csv"
    )

    # datetime
    datetime_index = pd.to_datetime(
        df["datetime"]
    )

    # 调试信息
    print()
    print("========== Dataset ==========")
    print(df.columns)
    print()
    print(df.dtypes)
    print()

    # ======================================
    # PV
    # ======================================

    pv_model = PVModel()

    pv_power = (
        pv_model.calculate(
            df["ghi"]
        )
    )

    # ======================================
    # Load
    # ======================================

    load_power = (
        df["load"]
    )

    # ======================================
    # TOU
    # ======================================

    tou_period = (
        df["tou_period"]
    )

    # ======================================
    # EMS
    # ======================================

    ems = EMSModel()

    target_battery_power = (
        ems.dispatch(
            pv_power,
            load_power,
            tou_period
        )
    )

    # ======================================
    # EMS Debug
    # ======================================

    ems_debug_df = pd.DataFrame({

        "datetime":
            datetime_index,

        "pv_power":
            pv_power,

        "load_power":
            load_power,

        "tou_period":
            tou_period,

        "target_battery_power":
            target_battery_power

    })

    ems_debug_df.to_csv(
        "output/ems_dispatch.csv",
        index=False
    )

    print()

    print("========== EMS ==========")

    print(
        target_battery_power.describe()
    )

    print()

    print(
        ems_debug_df.head(30)
    )

    print()

    # ======================================
    # Battery
    # ======================================

    battery = BatteryModel()

    (
        battery_power,
        soc,
        grid_power
    ) = (
        battery.execute_series(
            target_battery_power,
            pv_power,
            load_power
        )
    )

    # ======================================
    # EMS + Battery Debug
    # ======================================

    ems_battery_debug_df = pd.DataFrame({

        "datetime":
            datetime_index,

        "pv_power":
            pv_power,

        "load_power":
            load_power,

        "tou_period":
            tou_period,

        "target_battery_power":
            target_battery_power,

        "actual_battery_power":
            battery_power,

        "soc":
            soc,

        "grid_power":
            grid_power

    })

    ems_battery_debug_df.to_csv(
        "output/ems_battery_debug.csv",
        index=False
    )

    print()

    print("========== EMS + Battery ==========")

    print(
        ems_battery_debug_df.head(50)
    )

    print()

    # ======================================
    # Result
    # ======================================

    result_model = ResultModel()

    result_model.build(
        datetime_index,
        pv_power,
        load_power,
        battery_power,
        soc,
        grid_power
    )

    # ======================================
    # 输出 csv
    # ======================================

    result_model.export_csv(
        "output/test_dataset_result.csv"
    )

    # ======================================
    # 输出图像
    # ======================================

    result_model.plot_soc(
        "output/soc.png"
    )

    result_model.plot_power(
        "output/power.png"
    )

    result_model.plot_energy_balance(
        "output/energy_balance.png"
    )

    # ======================================
    # 信息
    # ======================================

    result_model.show_info()

    print()
    print("========== Test Finished ==========")
    print()
    print()

    print(type(pv_power.index))
    print(type(load_power.index))
    print(type(target_battery_power.index))
    print(type(battery_power.index))
    print(type(soc.index))
    print(type(grid_power.index))

    print()

    print(pv_power.index[:5])
    print(target_battery_power.index[:5])
    print(battery_power.index[:5])

    print()

if __name__ == "__main__":

    main()