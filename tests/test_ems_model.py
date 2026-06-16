import pandas as pd

from models.ems_model import EMSModel


def test_valley_period():
    """
    谷时充电
    """

    index = pd.date_range(
        "2025-01-01",
        periods=1,
        freq="h"
    )

    pv_power = pd.Series(
        [50],
        index=index
    )

    load_power = pd.Series(
        [100],
        index=index
    )

    tou_period = pd.Series(
        ["valley"],
        index=index
    )

    ems_model = EMSModel(
        arbitrage_power=100
    )

    target_battery_power = ems_model.dispatch(
        pv_power,
        load_power,
        tou_period
    )

    assert target_battery_power.iloc[0] == -50


def test_peak_period():
    """
    峰时放电
    """

    index = pd.date_range(
        "2025-01-01",
        periods=1,
        freq="h"
    )

    pv_power = pd.Series(
        [50],
        index=index
    )

    load_power = pd.Series(
        [100],
        index=index
    )

    tou_period = pd.Series(
        ["peak"],
        index=index
    )

    ems_model = EMSModel(
        arbitrage_power=100
    )

    target_battery_power = ems_model.dispatch(
        pv_power,
        load_power,
        tou_period
    )

    assert target_battery_power.iloc[0] == 150


def test_flat_period():
    """
    平时退化为自发自用
    """

    index = pd.date_range(
        "2025-01-01",
        periods=1,
        freq="h"
    )

    pv_power = pd.Series(
        [50],
        index=index
    )

    load_power = pd.Series(
        [100],
        index=index
    )

    tou_period = pd.Series(
        ["flat"],
        index=index
    )

    ems_model = EMSModel(
        arbitrage_power=100
    )

    target_battery_power = ems_model.dispatch(
        pv_power,
        load_power,
        tou_period
    )

    assert target_battery_power.iloc[0] == 50


def test_peak_period_with_pv_surplus():
    """
    峰时光伏过剩

    不允许为了套利主动放电
    """

    index = pd.date_range(
        "2025-01-01",
        periods=1,
        freq="h"
    )

    pv_power = pd.Series(
        [300],
        index=index
    )

    load_power = pd.Series(
        [100],
        index=index
    )

    tou_period = pd.Series(
        ["peak"],
        index=index
    )

    ems_model = EMSModel(
        arbitrage_power=100
    )

    target_battery_power = ems_model.dispatch(
        pv_power,
        load_power,
        tou_period
    )

    assert target_battery_power.iloc[0] == -200


def test_peak_period_with_zero_net_load():
    """
    峰时净负荷为零

    不应套利放电
    """

    index = pd.date_range(
        "2025-01-01",
        periods=1,
        freq="h"
    )

    pv_power = pd.Series(
        [100],
        index=index
    )

    load_power = pd.Series(
        [100],
        index=index
    )

    tou_period = pd.Series(
        ["peak"],
        index=index
    )

    ems_model = EMSModel(
        arbitrage_power=100
    )

    target_battery_power = ems_model.dispatch(
        pv_power,
        load_power,
        tou_period
    )

    assert target_battery_power.iloc[0] == 0


def test_no_arbitrage():
    """
    不开启峰谷套利

    应退化为纯自发自用
    """

    index = pd.date_range(
        "2025-01-01",
        periods=1,
        freq="h"
    )

    pv_power = pd.Series(
        [50],
        index=index
    )

    load_power = pd.Series(
        [100],
        index=index
    )

    tou_period = pd.Series(
        ["peak"],
        index=index
    )

    ems_model = EMSModel(
        arbitrage_power=0
    )

    target_battery_power = ems_model.dispatch(
        pv_power,
        load_power,
        tou_period
    )

    assert target_battery_power.iloc[0] == 50