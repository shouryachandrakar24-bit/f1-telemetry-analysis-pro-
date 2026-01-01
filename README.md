# f1-telemetry-analysis-pro-
Professional F1 Telemetry Analysis Suite using FastF1. Features distance-based synchronization, delta-time traces, and continuous-gradient track maps

# 🏎️ F1 Telemetry Analysis Suite

This project provides a high-fidelity toolkit for analyzing Formula 1 telemetry data. It moves beyond basic time-series plots to provide engineer-level insights such as **Delta Time** and **Distance-synchronized traces**.

## 🌟 Key Features
- **Distance-Based Analysis**: Synchronizes telemetry data by track position (meters) rather than time, ensuring corner-to-corner accuracy.
- **Delta Time Trace**: A precise calculation of time gained or lost between two drivers across a lap.
- **Continuous Track Maps**: High-resolution track maps using `LineCollection` to visualize speed gradients.
- **Dynamic Team Branding**: Automatically fetches official F1 team colors for professional visualization.



## 📊 Sample Visualizations
| Speed Gradient Map | Multi-Driver Comparison |
| :--- | :--- |
| ![Track Map](output/VER_track_map.png) | ![Comparison](output/VER_vs_NOR_comparison.png) |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [FastF1 Library](https://github.com/theOehrly/Fast-F1)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/f1-telemetry-suite.git](https://github.com/YOUR_USERNAME/f1-telemetry-suite.git)
   cd f1-telemetry-suite

  Install dependencies:

  pip install -r requirements.txt

  Run the analysis:
  
  python analysis.py


"""Project Structure"""
analysis.py: Main execution script containing the TelemetrySuite, TrackMapPro, and AdvancedComparison classes.

requirements.txt: List of necessary Python libraries.

output/: Directory where generated plots are saved.

data/: Local cache for FastF1 data (speeds up repeat executions)




