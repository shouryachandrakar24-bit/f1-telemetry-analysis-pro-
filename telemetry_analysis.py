!pip install fastf1

import fastf1
import fastf1.plotting as f1plot
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap

# Setup FastF1 styling
f1plot.setup_mpl(mpl_mpl_mods=False, color_scheme='fastf1', misc_mpl_mods=False)

class TelemetrySuite:
    """Professional F1 Telemetry Analysis Suite."""

    def __init__(self, year, location, session_type='R'):
        self.session = fastf1.get_session(year, location, session_type)
        self.session.load(telemetry=True, weather=False)
        self.event_name = f"{year} {self.session.event['EventName']}"

    def get_driver_lap(self, driver_code, lap_number):
        """Fetches and processes lap data with distance calculation."""
        lap = self.session.laps.pick_driver(driver_code).pick_lap(lap_number)
        # add_distance() is critical for synchronizing two different laps
        telemetry = lap.get_telemetry().add_distance()
        return lap, telemetry

class TrackMapPro:
    """Generates high-fidelity track maps with continuous color gradients."""

    def plot_map(self, telemetry, value_col='Speed', title="Track Analysis"):
        x = telemetry['X'].values
        y = telemetry['Y'].values
        color = telemetry[value_col].values

        # Create segments for LineCollection (this creates the continuous line)
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        fig, ax = plt.subplots(figsize=(12, 8), facecolor='black')

        # Professional "Plasma" or "Viridis" styling
        norm = plt.Normalize(color.min(), color.max())
        lc = LineCollection(segments, cmap='plasma', norm=norm, linestyle='-', linewidth=4)
        lc.set_array(color)

        line = ax.add_collection(lc)
        ax.axis('equal')
        ax.set_axis_off() # Professional maps don't need X/Y coordinates

        # Add sophisticated colorbar
        cbar = fig.colorbar(line, ax=ax, fraction=0.046, pad=0.04)
        cbar.set_label(f'{value_col}', color='white', fontsize=12)
        cbar.ax.yaxis.set_tick_params(color='white', labelcolor='white')

        plt.title(f"{title.upper()}", color='white', fontsize=15, fontweight='bold')
        plt.show()

class AdvancedComparison:
    """Engineer-level telemetry comparison with Delta Time."""

    def compare_drivers(self, lap1_data, lap2_data):
        lap1, tel1 = lap1_data
        lap2, tel2 = lap2_data

        # Calculate Delta Time (The difference in time at every meter of the track)
        delta_time, ref_tel, target_tel = fastf1.utils.delta_time(lap1, lap2)

        fig, axs = plt.subplots(4, 1, figsize=(14, 12), sharex=True,
                               gridspec_kw={'height_ratios': [1, 2, 1, 1]})

        # Get official team colors
        color1 = f1plot.get_driver_color(lap1.Driver.item(), session=lap1.session)
        color2 = f1plot.get_driver_color(lap2.Driver.item(), session=lap2.session)

        # 1. Delta Time (Crucial for engineers)
        axs[0].plot(ref_tel['Distance'], delta_time, color='white', linewidth=1)
        axs[0].axhline(0, color='grey', linestyle='--', alpha=0.5)
        axs[0].set_ylabel(f"Delta (s)\n<-- {lap1['Driver']} Faster", fontsize=9)
        axs[0].set_title(f"{lap1['Driver']} vs {lap2['Driver']} | {lap1.session.event['EventName']}")

        # 2. Speed Trace
        axs[1].plot(tel1['Distance'], tel1['Speed'], color=color1, label=lap1['Driver'])
        axs[1].plot(tel2['Distance'], tel2['Speed'], color=color2, label=lap2['Driver'])
        axs[1].set_ylabel("Speed (km/h)")
        axs[1].legend(loc='upper right')

        # 3. Throttle
        axs[2].plot(tel1['Distance'], tel1['Throttle'], color=color1)
        axs[2].plot(tel2['Distance'], tel2['Throttle'], color=color2)
        axs[2].set_ylabel("Throttle %")

        # 4. Brake
        axs[3].plot(tel1['Distance'], tel1['Brake'], color=color1)
        axs[3].plot(tel2['Distance'], tel2['Brake'], color=color2)
        axs[3].set_ylabel("Brake")
        axs[3].set_xlabel("Distance (m)")

        for ax in axs:
            ax.grid(True, linestyle=':', alpha=0.4)
            ax.label_outer()

        plt.tight_layout()
        plt.show()

# --- EXECUTION ---
# 1. Initialize Session
suite = TelemetrySuite(2023, 'Zandvoort')

# 2. Get Data for two drivers (Verstappen vs Norris)
ver_lap = suite.get_driver_lap('VER', 5)
nor_lap = suite.get_driver_lap('NOR', 5)

# 3. Plot Advanced Track Map
map_tool = TrackMapPro()
map_tool.plot_map(ver_lap[1], value_col='Speed', title="Verstappen Speed Map - Zandvoort")

# 4. Plot Multi-Metric Comparison
compare_tool = AdvancedComparison()
compare_tool.compare_drivers(ver_lap, nor_lap)
