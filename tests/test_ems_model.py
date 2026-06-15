from models.ems_model import EMSModel


ems = EMSModel()


# 场景1

pv_power = 10
load_power = 30

target_battery_power = (
    ems.dispatch(
        pv_power,
        load_power
    )
)

print("场景1")

print(
    f"PV = {pv_power}"
)

print(
    f"Load = {load_power}"
)

print(
    f"Target Battery = {target_battery_power}"
)

print()


# 场景2

pv_power = 40
load_power = 20

target_battery_power = (
    ems.dispatch(
        pv_power,
        load_power
    )
)

print("场景2")

print(
    f"PV = {pv_power}"
)

print(
    f"Load = {load_power}"
)

print(
    f"Target Battery = {target_battery_power}"
)