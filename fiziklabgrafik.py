# --- Extrapolation Graph for Glider Velocity Experiment ---
# Works perfectly with Python 3.13

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data from your table
data = {
    "D_cm": [80, 70, 60, 50, 40, 30, 20, 10],
    "v_avg": [0.444, 0.444, 0.444, 0.449, 0.447, 0.455, 0.449, 0.476]
}

# Convert to DataFrame
df = pd.DataFrame(data)
df["D_m"] = df["D_cm"] / 100  # Convert cm → m

# Linear regression (best-fit line)
coeffs = np.polyfit(df["D_m"], df["v_avg"], 1)  # 1 = linear fit
trend_line = np.poly1d(coeffs)

# Extrapolation line (extend distance from 0 to 0.9 m)
x_line = np.linspace(0, 0.9, 200)
y_line = trend_line(x_line)

# Plot
plt.figure(figsize=(8, 5))
plt.scatter(df["D_m"], df["v_avg"], color="darkorange", label="Measured Data", s=70)
plt.plot(x_line, y_line, color="brown", linestyle="--", label="Extrapolated Trend Line")

# Labels and title
plt.title("Extrapolation Graph of Average Velocity vs Distance", fontsize=13)
plt.xlabel("Distance (m)", fontsize=11)
plt.ylabel("Average Velocity (m/s)", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()

# Display the linear equation on the graph (rounded)
slope = coeffs[0]
intercept = coeffs[1]
equation_text = f"v = {slope:.3f}x + {intercept:.3f}"
plt.text(0.05, max(df["v_avg"]) - 0.005, equation_text, fontsize=10, color="black")

# Show the graph
plt.show()

# Print the line equation to the console
print(f"Line equation: v = {slope:.4f}x + {intercept:.4f}")
