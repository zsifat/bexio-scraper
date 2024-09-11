import matplotlib.pyplot as plt
import numpy as np

# List of all available styles
styles = plt.style.available
n = len(styles)
rows = (n + 4) // 5

# Create a grid of subplots
fig, axes = plt.subplots(rows, 5, figsize=(15, rows * 2))
for ax, style_name in zip(axes.flat, styles):
    plt.style.use(style_name)

    # Generate data for plotting
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Plot using the current style
    ax.plot(x, y)
    ax.set_title(style_name, fontsize=8)
    ax.grid(True)
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()
