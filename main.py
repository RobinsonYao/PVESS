"""
PVESS
Photovoltaic Energy Storage Simulation System

Stage 1:
Industrial and Commercial ESS Sizing

Entry:
python main.py
"""


# ==========================================================
# Imports
# ==========================================================

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ==========================================================
# Global Config
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_FILE = (
    PROJECT_ROOT
    / "tests"
    / "data"
    / "historical.csv"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "output"
)

OUTPUT_DIR.mkdir(
    exist_ok=True
)


# ==========================================================
# Constants
# ==========================================================

BATTERY_POWER_KW = 100

BATTERY_CAPACITY_KWH = 200

ARBITRAGE_POWER_KW = 50

PV_CAPACITY_KW = 100

# ==========================================================
# DataModel
#
# Responsibility
#
# csv
# ↓
# pandas.DataFrame
#
# Functions
#
# - Read csv file
# - Standardize column names
# - Convert datetime
# - Build DatetimeIndex
#
# Output
#
# Standardized DataFrame
#
# Position in system
#
# Dataset
# ↓
# DataModel
# ↓
# WeatherModel
#
# ==========================================================

class DataModel:

    def __init__(self):

        self.df = None


    def load(
            self,
            file_path):
        """
        Read csv file.

        Parameters
        ----------
        file_path : Path

        Returns
        -------
        pandas.DataFrame
        """

        # --------------------------------------------------
        # Step 1
        # Read csv file
        # --------------------------------------------------

        self.df = pd.read_csv(
            file_path
        )


        # --------------------------------------------------
        # Step 2
        # Standardize column names
        #
        # Example
        #
        # Wind Speed
        # →
        # wind_speed
        #
        # Datetime
        # →
        # datetime
        #
        # Purpose
        #
        # Avoid spaces and upper-case
        # problems.
        # --------------------------------------------------

        self.standardize_columns()


        # --------------------------------------------------
        # Step 3
        # Convert datetime column
        #
        # string
        #
        # "2020-01-01 00:10"
        #
        # ↓
        #
        # pandas.Timestamp
        #
        # Purpose
        #
        # Enable time-series processing.
        # --------------------------------------------------

        self.df["datetime"] = (
            pd.to_datetime(
                self.df["datetime"]
            )
        )


        # --------------------------------------------------
        # Step 4
        # Build DatetimeIndex
        #
        # datetime column
        # ↓
        # DataFrame index
        #
        # Purpose
        #
        # Support:
        #
        # resample()
        # rolling()
        # shift()
        # time slicing
        # --------------------------------------------------

        self.df.set_index(
            "datetime",
            inplace=True
        )

        return self.df


    def standardize_columns(self):
        """
        Standardize column names.

        Example

        Wind Speed
        →
        wind_speed

        Datetime
        →
        datetime
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


# ==========================================================
# WeatherModel
# ==========================================================

# ==========================================================
# WeatherModel
#
# Responsibility
#
# DataFrame
# ↓
# Weather statistics
#
# Functions
#
# - Annual GHI
# - Monthly GHI
# - Weather information
#
# Position in system
#
# DataModel
# ↓
# WeatherModel
# ↓
# PVModel
#
# ==========================================================

class WeatherModel:

    def __init__(
            self,
            df):

        # Reference to DataFrame

        self.df = df


    def show_info(self):
        """
        Show basic information
        of weather dataset.
        """

        print()

        print(
            "========== Weather Info =========="
        )

        print()

        print(
            "Time steps :",
            len(self.df)
        )

        print()

        print(
            "Start :",
            self.df.index.min()
        )

        print()

        print(
            "End :",
            self.df.index.max()
        )

        print()


    def calculate_year_ghi(self):
        """
        Annual solar irradiation.

        Unit:

        kWh/m²
        """

        # --------------------------------------------------
        # GHI unit:
        #
        # W/m²
        #
        # Time interval:
        #
        # 10 min
        #
        # 1 hour = 6 samples
        #
        # Therefore:
        #
        # sum(GHI)
        # ----------
        # 6 × 1000
        #
        # Unit:
        #
        # kWh/m²
        # --------------------------------------------------

        year_ghi = (

            self.df["ghi"]

            .resample(
                "YE"
            )

            .sum()

            / 6

            / 1000

        )

        return year_ghi


    def calculate_month_ghi(self):
        """
        Monthly solar irradiation.

        Unit:

        kWh/m²
        """

        month_ghi = (

            self.df["ghi"]

            .resample(
                "ME"
            )

            .sum()

            / 6

            / 1000

        )

        return month_ghi


# ==========================================================
# LoadModel
# ==========================================================

# ==========================================================
# LoadModel
#
# Responsibility
#
# Load input layer
#
# Functions
#
# - Real load profile
# - Typical load profile
#
# Position in system
#
# User
# ↓
# LoadModel
# ↓
# EMSModel
#
# ==========================================================

class LoadModel:

    def __init__(self):

        self.load_power = pd.Series(
            dtype=float
        )


    def from_dataframe(
            self,
            df):
        """
        Load power from DataFrame.

        Input

        DataFrame

        Output

        pandas.Series
        """

        self.load_power = df[
            "load"
        ]

        return self.load_power


    def generate_typical_profile(
            self,
            time_index):
        """
        Generate simple load profile.

        00:00~06:00

        30 kW

        06:00~18:00

        80 kW

        18:00~24:00

        50 kW
        """

        load_list = []

        # --------------------------------------------------
        # Generate load point by point
        # --------------------------------------------------

        for time in time_index:

            hour = time.hour

            # Night

            if hour < 6:

                load = 30

            # Daytime

            elif hour < 18:

                load = 80

            # Evening

            else:

                load = 50

            load_list.append(
                load
            )

        self.load_power = pd.Series(

            load_list,

            index=time_index

        )

        return self.load_power


# ==========================================================
# PVModel
# ==========================================================

# ==========================================================
# PVModel
#
# Responsibility
#
# Weather
# ↓
# PV Power
#
# Functions
#
# - Convert GHI to PV power
#
# Position in system
#
# WeatherModel
# ↓
# PVModel
# ↓
# EMSModel
#
# ==========================================================

class PVModel:

    def __init__(
            self,
            capacity_kw=100):

        self.capacity_kw = (
            capacity_kw
        )

        self.power = pd.Series(
            dtype=float
        )


    def calculate(
            self,
            ghi):
        """
        Calculate PV power.

        Parameters
        ----------
        ghi : pandas.Series

            Global horizontal irradiance

            Unit:

            W/m²

        Returns
        -------
        power : pandas.Series

            PV power

            Unit:

            kW
        """

        # --------------------------------------------------
        # Step 1
        # Convert irradiance to per-unit output
        #
        # 1000 W/m²
        #
        # ↓
        #
        # 1.0 p.u.
        # --------------------------------------------------

        normalized_ghi = (
            ghi / 1000
        )


        # --------------------------------------------------
        # Step 2
        # Calculate PV power
        #
        # Power
        #
        # = irradiance ratio
        #
        # × installed capacity
        #
        # Unit:
        #
        # kW
        # --------------------------------------------------

        self.power = (

            normalized_ghi

            * self.capacity_kw

        )

        return self.power



# ==========================================================
# EMSModel
#
# Responsibility
#
# PV + Load
# ↓
# Battery dispatch target
#
# Functions
#
# - PV self-consumption
# - Peak-valley arbitrage
# - Demand control
# - Priority coordination
#
# Output
#
# Positive
#
# Discharge
#
# Negative
#
# Charge
#
# Position in system
#
# PVModel
# ↓
# EMSModel
# ↓
# BatteryModel
#
# ==========================================================

class EMSModel:

    def __init__(
            self,
            battery_power_kw=100,
            arbitrage_power=50,
            demand_limit_kw=None):
        """
        Parameters
        ----------
        battery_power_kw

            Battery rated power

            Unit:

            kW

        arbitrage_power

            Peak-valley arbitrage power

            Unit:

            kW

        demand_limit_kw

            Demand limit

            Unit:

            kW
        """

        # --------------------------------------------------
        # Battery rated power
        # --------------------------------------------------

        self.battery_power_kw = (
            battery_power_kw
        )

        # --------------------------------------------------
        # Arbitrage power
        # --------------------------------------------------

        self.arbitrage_power = (
            arbitrage_power
        )

        # --------------------------------------------------
        # Demand limit
        # --------------------------------------------------

        self.demand_limit_kw = (
            demand_limit_kw
        )


    def _get_self_consumption_power(
            self,
            pv_power,
            load_power):
        """
        PV self-consumption

        Only absorb surplus PV.

        Returns
        -------
        Series

        Positive

        Discharge

        Negative

        Charge
        """

        # --------------------------------------------------
        # PV surplus
        #
        # PV
        #
        # -
        #
        # Load
        # --------------------------------------------------

        pv_surplus = (

            pv_power

            -

            load_power

        )


        # --------------------------------------------------
        # Charge battery with surplus PV
        #
        # Negative value means charging
        # --------------------------------------------------

        self_consumption_power = (

            -pv_surplus.clip(

                lower=0,

                upper=self.battery_power_kw

            )

        )

        return self_consumption_power


    def _get_arbitrage_power(
            self,
            net_load,
            tou_period):
        """
        Peak-valley arbitrage.

        Returns
        -------
        Series

        Positive

        Discharge

        Negative

        Charge
        """

        arbitrage_power = pd.Series(
            0.0,
            index=tou_period.index
        )

        # --------------------------------------------------
        # Valley charging
        # --------------------------------------------------

        valley_mask = (
            tou_period
            ==
            "valley"
        )

        arbitrage_power.loc[
            valley_mask
        ] = (
            -self.arbitrage_power
        )


        # --------------------------------------------------
        # Peak discharging
        # --------------------------------------------------

        peak_mask = (

            (tou_period == "peak")

            &

            (net_load > 0)

        )

        arbitrage_power.loc[
            peak_mask
        ] = (

            net_load.loc[
                peak_mask
            ]

            .clip(
                upper=self.arbitrage_power
            )

        )

        return arbitrage_power


    def _get_demand_control_power(
            self,
            net_load):
        """
        Demand control.

        Skeleton.

        Returns
        -------
        Series

        Positive

        Discharge
        """

        demand_control_power = pd.Series(
            0.0,
            index=net_load.index
        )

        if self.demand_limit_kw is None:

            return demand_control_power


        # --------------------------------------------------
        # Excess load
        #
        # Load above demand limit
        # --------------------------------------------------

        excess_load = (

            net_load

            -

            self.demand_limit_kw

        )


        demand_control_power = (

            excess_load.clip(

                lower=0,

                upper=self.battery_power_kw

            )

        )

        return demand_control_power


    def _merge_power(
            self,
            self_consumption_power,
            arbitrage_power,
            demand_control_power):
        """
        Strategy priority

        1 Demand Control

        Highest priority

        ↓

        2 PV Self-consumption

        ↓

        3 Peak-Valley Arbitrage

        Lowest priority

        Final:

        Power clipping
        """

        target_power = pd.Series(
            0.0,
            index=self_consumption_power.index
        )


        # --------------------------------------------------
        # Step 1
        #
        # Demand control
        #
        # Highest priority
        # --------------------------------------------------

        target_power = (

            target_power

            +

            demand_control_power

        )


        # --------------------------------------------------
        # Step 2
        #
        # PV self-consumption
        #
        # Use remaining charging capability
        # --------------------------------------------------

        remain_charge_power = (

            self.battery_power_kw

            +

            target_power.clip(
                upper=0
            )

        )

        pv_charge = (

            self_consumption_power.clip(
                upper=0
            )

        )

        pv_charge = (

            pv_charge.clip(
                lower=-remain_charge_power
            )

        )

        target_power = (

            target_power

            +

            pv_charge

        )


        # --------------------------------------------------
        # Step 3
        #
        # Peak-valley arbitrage
        #
        # Use remaining power margin
        # --------------------------------------------------

        remain_discharge_power = (

            self.battery_power_kw

            -

            target_power.clip(
                lower=0
            )

        )

        remain_charge_power = (

            self.battery_power_kw

            +

            target_power.clip(
                upper=0
            )

        )

        arbitrage_discharge = (

            arbitrage_power.clip(
                lower=0
            )

        )

        arbitrage_charge = (

            arbitrage_power.clip(
                upper=0
            )

        )

        arbitrage_discharge = (

            arbitrage_discharge.clip(
                upper=remain_discharge_power
            )

        )

        arbitrage_charge = (

            arbitrage_charge.clip(
                lower=-remain_charge_power
            )

        )

        target_power = (

            target_power

            +

            arbitrage_discharge

            +

            arbitrage_charge

        )


        # --------------------------------------------------
        # Step 4
        #
        # Final power clipping
        #
        # Ensure:
        #
        # -Pmax ≤ power ≤ Pmax
        # --------------------------------------------------

        target_power = (

            target_power.clip(

                lower=-self.battery_power_kw,

                upper=self.battery_power_kw

            )

        )

        return target_power


    def dispatch(
            self,
            pv_power,
            load_power,
            tou_period):
        """
        EMS dispatch.

        Returns
        -------
        Series

        Positive

        Discharge

        Negative

        Charge
        """

        # --------------------------------------------------
        # Net load
        #
        # Load
        #
        # -
        #
        # PV
        # --------------------------------------------------

        net_load = (

            load_power

            -

            pv_power

        )


        # --------------------------------------------------
        # Strategy 1
        #
        # PV self-consumption
        # --------------------------------------------------

        self_consumption_power = (

            self._get_self_consumption_power(
                pv_power,
                load_power
            )

        )


        # --------------------------------------------------
        # Strategy 2
        #
        # Peak-valley arbitrage
        # --------------------------------------------------

        arbitrage_power = (

            self._get_arbitrage_power(
                net_load,
                tou_period
            )

        )


        # --------------------------------------------------
        # Strategy 3
        #
        # Demand control
        # --------------------------------------------------

        demand_control_power = (

            self._get_demand_control_power(
                net_load
            )

        )


        # --------------------------------------------------
        # Merge strategies
        #
        # According to priority
        # --------------------------------------------------

        target_power = (

            self._merge_power(
                self_consumption_power,
                arbitrage_power,
                demand_control_power
            )

        )

        return pd.Series(
            target_power,
            index=pv_power.index
        )



# ==========================================================
# BatteryModel
# ==========================================================

# ==========================================================
# BatteryModel
#
# Responsibility
#
# Target battery power
# ↓
# Actual battery power
#
# Functions
#
# - Power limit
# - SOC protection
# - Charge / discharge efficiency
# - Grid power calculation
#
# Output
#
# Battery power
#
# SOC
#
# Grid power
#
# Position in system
#
# EMSModel
# ↓
# BatteryModel
# ↓
# ResultModel
#
# ==========================================================

class BatteryModel:

    def __init__(
            self,
            capacity_kwh=200,
            power_kw=100):

        # Battery capacity

        self.capacity_kwh = (
            capacity_kwh
        )

        # Rated power

        self.power_kw = (
            power_kw
        )

        # SOC upper limit

        self.soc_max = 95

        # SOC lower limit

        self.soc_min = 10

        # Initial SOC

        self.soc_initial = 50

        # Efficiency

        self.charge_efficiency = 0.95

        self.discharge_efficiency = 0.95


    def execute(
            self,
            target_battery_power,
            current_soc,
            pv_power,
            load_power):
        """
        Execute one time step.

        Parameters
        ----------
        target_battery_power : float

            Positive

            Discharge

            Negative

            Charge

        current_soc : float

        pv_power : float

        load_power : float

        Returns
        -------
        actual_battery_power

        next_soc

        grid_power
        """

        # --------------------------------------------------
        # Step 1
        #
        # Start from EMS target power
        # --------------------------------------------------

        actual_battery_power = (
            target_battery_power
        )


        # --------------------------------------------------
        # Step 2
        #
        # Power limit
        #
        # Ensure:
        #
        # -Pmax ≤ P ≤ Pmax
        # --------------------------------------------------

        if actual_battery_power > self.power_kw:

            actual_battery_power = (
                self.power_kw
            )

        if actual_battery_power < -self.power_kw:

            actual_battery_power = (
                -self.power_kw
            )


        # --------------------------------------------------
        # Step 3
        #
        # SOC lower protection
        #
        # Prevent over-discharge
        # --------------------------------------------------

        if (

                actual_battery_power > 0

                and

                current_soc <= self.soc_min

        ):

            actual_battery_power = 0


        # --------------------------------------------------
        # Step 4
        #
        # SOC upper protection
        #
        # Prevent over-charge
        # --------------------------------------------------

        if (

                actual_battery_power < 0

                and

                current_soc >= self.soc_max

        ):

            actual_battery_power = 0


        # --------------------------------------------------
        # Step 5
        #
        # Calculate energy change
        #
        # Time step:
        #
        # 10 min
        #
        # = 1 / 6 hour
        # --------------------------------------------------

        if actual_battery_power > 0:

            # discharge

            energy_change = (

                -actual_battery_power

                / self.discharge_efficiency

                / 6

            )

        else:

            # charge

            energy_change = (

                -actual_battery_power

                * self.charge_efficiency

                / 6

            )


        # --------------------------------------------------
        # Step 6
        #
        # Convert energy change
        #
        # to SOC change
        # --------------------------------------------------

        soc_change = (

            energy_change

            / self.capacity_kwh

            * 100

        )


        # --------------------------------------------------
        # Step 7
        #
        # Update SOC
        # --------------------------------------------------

        next_soc = (

            current_soc

            + soc_change

        )


        # --------------------------------------------------
        # Step 8
        #
        # Final SOC clipping
        #
        # Ensure:
        #
        # SOCmin ≤ SOC ≤ SOCmax
        # --------------------------------------------------

        next_soc = max(

            self.soc_min,

            min(
                next_soc,
                self.soc_max
            )

        )


        # --------------------------------------------------
        # Step 9
        #
        # Grid power
        #
        # Load
        #
        # -
        #
        # PV
        #
        # -
        #
        # Battery
        # --------------------------------------------------

        grid_power = (

            load_power

            -

            pv_power

            -

            actual_battery_power

        )


        return (

            actual_battery_power,

            next_soc,

            grid_power

        )


    def execute_series(
            self,
            target_battery_power,
            pv_power,
            load_power):
        """
        Execute entire time series.

        Parameters
        ----------
        target_battery_power : Series

            Positive

            Discharge

            Negative

            Charge

        pv_power : Series

        load_power : Series

        Returns
        -------
        battery_power

        soc

        grid_power
        """

        # --------------------------------------------------
        # Create output Series
        # --------------------------------------------------

        battery_power = pd.Series(

            index=target_battery_power.index,

            dtype=float

        )

        soc = pd.Series(

            index=target_battery_power.index,

            dtype=float

        )

        grid_power = pd.Series(

            index=target_battery_power.index,

            dtype=float

        )


        # --------------------------------------------------
        # Initial SOC
        # --------------------------------------------------

        current_soc = (
            self.soc_initial
        )


        # --------------------------------------------------
        # Step 1
        #
        # Execute time step one by one
        # --------------------------------------------------

        for i in range(

                len(
                    target_battery_power
                )):

            (

                actual_battery_power,

                next_soc,

                grid_power_value

            ) = (

                self.execute(

                    target_battery_power.iloc[i],

                    current_soc,

                    pv_power.iloc[i],

                    load_power.iloc[i]

                )

            )


            # --------------------------------------------------
            # Save battery power
            # --------------------------------------------------

            battery_power.iloc[i] = (
                actual_battery_power
            )


            # --------------------------------------------------
            # Save SOC
            # --------------------------------------------------

            soc.iloc[i] = (
                next_soc
            )


            # --------------------------------------------------
            # Save grid power
            # --------------------------------------------------

            grid_power.iloc[i] = (
                grid_power_value
            )


            # --------------------------------------------------
            # Prepare next time step
            # --------------------------------------------------

            current_soc = (
                next_soc
            )


        return (

            battery_power,

            soc,

            grid_power

        )


# ==========================================================
# ResultModel
# ==========================================================

# ==========================================================
# ResultModel
#
# Responsibility
#
# Simulation results
#
# Functions
#
# - Build result DataFrame
# - Export csv
# - Plot figures
# - Show information
#
# Position in system
#
# BatteryModel
# ↓
# ResultModel
# ↓
# csv + png
#
# ==========================================================

class ResultModel:
    """
    Simulation result model

    battery_power

        Positive

        Discharge

        Negative

        Charge

    grid_power

        Positive

        Import from grid

        Negative

        Export to grid
    """

    def __init__(self):

        # --------------------------------------------------
        # Result DataFrame
        # --------------------------------------------------

        self.df = None


    def build(
            self,
            datetime_index,
            pv_power,
            load_power,
            battery_power,
            soc,
            grid_power):
        """
        Build result DataFrame.
        """

        self.df = pd.DataFrame({

            "datetime":

                pd.Series(
                    datetime_index
                ).values,

            "pv_power":

                pd.Series(
                    pv_power
                ).values,

            "load_power":

                pd.Series(
                    load_power
                ).values,

            "battery_power":

                pd.Series(
                    battery_power
                ).values,

            "soc":

                pd.Series(
                    soc
                ).values,

            "grid_power":

                pd.Series(
                    grid_power
                ).values

        })


    def to_dataframe(self):
        """
        Return result DataFrame.
        """

        return self.df


    def head(
            self,
            n=5):
        """
        Return first n rows.
        """

        return self.df.head(
            n
        )


    def tail(
            self,
            n=5):
        """
        Return last n rows.
        """

        return self.df.tail(
            n
        )


    def show_info(self):
        """
        Show result information.
        """

        if self.df is None:

            print(
                "ResultModel is empty."
            )

            return


        print()

        print(
            "========== Simulation Result =========="
        )

        print()

        print(
            "Time steps :",
            len(self.df)
        )

        print()

        print(
            "Columns:"
        )

        print()

        for col in self.df.columns:

            print(
                " ",
                col
            )

        print(
            "======================================="
        )

        print()


    def export_csv(
            self,
            filepath):
        """
        Export result csv.
        """

        if self.df is None:

            print(
                "ResultModel is empty."
            )

            return


        self.df.to_csv(

            filepath,

            index=False

        )


        print(

            "Result exported to:",

            filepath

        )


    def plot_soc(
            self,
            filepath="output/soc.png"):
        """
        Plot SOC curve.
        """

        if self.df is None:

            print(
                "ResultModel is empty."
            )

            return


        plt.figure(

            figsize=(10, 5)

        )


        # --------------------------------------------------
        # SOC curve
        # --------------------------------------------------

        plt.plot(

            self.df["datetime"],

            self.df["soc"]

        )


        plt.xlabel(
            "Time"
        )

        plt.ylabel(
            "SOC (%)"
        )

        plt.title(
            "SOC"
        )

        plt.grid()

        plt.tight_layout()

        plt.savefig(

            filepath,

            dpi=300

        )


        print(

            "SOC figure saved to:",

            filepath

        )

        plt.close()


    def plot_power(
            self,
            filepath="output/power.png"):
        """
        Plot power curves.
        """

        if self.df is None:

            print(
                "ResultModel is empty."
            )

            return


        plt.figure(

            figsize=(12, 6)

        )


        # --------------------------------------------------
        # PV
        # --------------------------------------------------

        plt.plot(

            self.df["datetime"],

            self.df["pv_power"],

            label="PV",

            color="blue",

            linewidth=2

        )


        # --------------------------------------------------
        # Load
        # --------------------------------------------------

        plt.plot(

            self.df["datetime"],

            self.df["load_power"],

            label="Load",

            color="black",

            linewidth=2

        )


        # --------------------------------------------------
        # Battery
        # --------------------------------------------------

        plt.plot(

            self.df["datetime"],

            self.df["battery_power"],

            label="Battery",

            color="green",

            linewidth=3

        )


        # --------------------------------------------------
        # Grid
        # --------------------------------------------------

        plt.plot(

            self.df["datetime"],

            self.df["grid_power"],

            label="Grid",

            color="red",

            linewidth=2

        )


        plt.xlabel(
            "Time"
        )

        plt.ylabel(
            "Power (kW)"
        )

        plt.title(
            "Power"
        )

        plt.grid()

        plt.legend()

        plt.tight_layout()

        plt.savefig(

            filepath,

            dpi=300

        )


        print(

            "Power figure saved to:",

            filepath

        )

        plt.close()


    def plot_energy_balance(
            self,
            filepath="output/energy_balance.png"):
        """
        Plot energy balance.

        PV + Battery + Grid = Load
        """

        if self.df is None:

            print(
                "ResultModel is empty."
            )

            return


        # --------------------------------------------------
        # Supply side
        #
        # PV
        #
        # +
        #
        # Battery
        #
        # +
        #
        # Grid
        # --------------------------------------------------

        supply = (

            self.df["pv_power"]

            +

            self.df["battery_power"]

            +

            self.df["grid_power"]

        )


        plt.figure(

            figsize=(12, 6)

        )


        # --------------------------------------------------
        # Supply
        # --------------------------------------------------

        plt.plot(

            self.df["datetime"],

            supply,

            label="PV + Battery + Grid",

            linewidth=3

        )


        # --------------------------------------------------
        # Load
        # --------------------------------------------------

        plt.plot(

            self.df["datetime"],

            self.df["load_power"],

            label="Load",

            linewidth=2

        )


        plt.xlabel(
            "Time"
        )

        plt.ylabel(
            "Power (kW)"
        )

        plt.title(
            "Energy Balance"
        )

        plt.grid()

        plt.legend()

        plt.tight_layout()

        plt.savefig(

            filepath,

            dpi=300

        )


        print(

            "Energy balance figure saved to:",

            filepath

        )

        plt.close()


# ==========================================================
# TariffModel
# ==========================================================

class TariffModel:

    pass


# ==========================================================
# EconomicModel
# ==========================================================

class EconomicModel:

    pass


# ==========================================================
# StressTestModel
# ==========================================================

class StressTestModel:

    pass


# ==========================================================
# SizingModel
# ==========================================================

class SizingModel:

    pass


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
# ======================================================
# Simulation Flow
#
# Data
# ↓
# Weather
# ↓
# Load
# ↓
# PV
# ↓
# EMS
# ↓
# Battery
# ↓
# Result
# ↓
# Output
#
# ======================================================
    # ------------------------------------------------------
    # Data
    # ------------------------------------------------------

    data_model = DataModel()

    df = data_model.load(
        DATA_FILE
    )

    # ------------------------------------------------------
    # Weather
    # ------------------------------------------------------

    weather_model = WeatherModel(
        df
    )
    # ------------------------------------------------------
    # Load
    # ------------------------------------------------------

    load_model = LoadModel()

    load_power = (
        load_model.from_dataframe(
            df
        )
    )
    time_index = df.index

    ghi = df["ghi"]


    tou_period = df["tou_period"]


    # ------------------------------------------------------
    # PV
    # ------------------------------------------------------

    pv_model = PVModel(
    capacity_kw=PV_CAPACITY_KW
    )

    pv_power = (
        pv_model.calculate(
            ghi
        )
    )


    # ------------------------------------------------------
    # EMS
    # ------------------------------------------------------

    ems_model = EMSModel(
        battery_power_kw=BATTERY_POWER_KW,
        arbitrage_power=ARBITRAGE_POWER_KW
    )

    target_battery_power = (
        ems_model.dispatch(
            pv_power,
            load_power,
            tou_period
        )
    )


    # ------------------------------------------------------
    # Battery
    # ------------------------------------------------------

    battery_model = BatteryModel(

    capacity_kwh=BATTERY_CAPACITY_KWH,

    power_kw=BATTERY_POWER_KW

)

    (
        battery_power,
        soc,
        grid_power
    ) = (
        battery_model.execute_series(
            target_battery_power,
            pv_power,
            load_power
        )
    )


    # ------------------------------------------------------
    # Result
    # ------------------------------------------------------

    result_model = ResultModel()

    result_model.build(
        datetime_index=time_index,
        pv_power=pv_power,
        load_power=load_power,
        battery_power=battery_power,
        soc=soc,
        grid_power=grid_power
    )

    result_model.show_info()


    # ------------------------------------------------------
    # Output
    # ------------------------------------------------------

    result_model.export_csv(
        OUTPUT_DIR / "result.csv"
    )

    result_model.plot_soc(
        OUTPUT_DIR / "soc.png"
    )

    result_model.plot_power(
        OUTPUT_DIR / "power.png"
    )

    result_model.plot_energy_balance(
        OUTPUT_DIR / "energy_balance.png"
    )


    # ------------------------------------------------------
    # Finish
    # ------------------------------------------------------

    print()

    print(
        "Simulation finished."
    )

    print(
        "Result saved to output/"
    )

    print()