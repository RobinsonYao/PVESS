from models.ems_model import EMSModel
from models.battery_model import BatteryModel


# 创建对象
ems = EMSModel()

battery = BatteryModel()


# 初始 SOC
current_soc = 50


# ==============================
# 场景1
# PV < Load
# 电池应该放电
# ==============================

pv_power = 10

load_power = 30

target_battery_power = (
    ems.dispatch(
        pv_power,
        load_power
    )
)

(
    actual_battery_power,
    next_soc,
    grid_power
) = (
    battery.execute(
        target_battery_power,
        current_soc,
        pv_power,
        load_power
    )
)

print("========== 场景1 ==========")

print(f"PV = {pv_power} kW")

print(f"Load = {load_power} kW")

print(f"Target Battery = {target_battery_power} kW")

print(f"Actual Battery = {actual_battery_power} kW")

print(f"Next SOC = {next_soc:.2f} %")

print(f"Grid Power = {grid_power} kW")

print()


# ==============================
# 场景2
# PV > Load
# 电池应该充电
# ==============================

current_soc = next_soc

pv_power = 40

load_power = 20

target_battery_power = (
    ems.dispatch(
        pv_power,
        load_power
    )
)

(
    actual_battery_power,
    next_soc,
    grid_power
) = (
    battery.execute(
        target_battery_power,
        current_soc,
        pv_power,
        load_power
    )
)

print("========== 场景2 ==========")

print(f"PV = {pv_power} kW")

print(f"Load = {load_power} kW")

print(f"Target Battery = {target_battery_power} kW")

print(f"Actual Battery = {actual_battery_power} kW")

print(f"Next SOC = {next_soc:.2f} %")

print(f"Grid Power = {grid_power} kW")