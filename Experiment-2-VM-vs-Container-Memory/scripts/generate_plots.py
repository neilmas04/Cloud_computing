"""Generate comparison charts for Experiment 2 (Sysbench memory: VM vs Docker container).

Values are taken from the captured screenshots in ../images/.
Run from the experiment folder:  python scripts/generate_plots.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

labels = ["VM (Ubuntu / VMware)", "Docker Container"]
colors = ["#1f77b4", "#2ca02c"]
throughput = [108900.87, 123725.89]   # MiB/sec
total_time = [0.0931, 0.0819]         # seconds
max_latency = [3.04, 1.13]            # ms

os.makedirs("images", exist_ok=True)
fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
for ax, data, title, unit in zip(
    axes,
    [throughput, total_time, max_latency],
    ["Memory Throughput (higher is better)", "Total Time (lower is better)", "Max Latency (lower is better)"],
    ["MiB/sec", "seconds", "ms"],
):
    bars = ax.bar(labels, data, color=colors)
    ax.set_title(title, fontsize=10)
    ax.set_ylabel(unit)
    ax.tick_params(axis="x", labelsize=8)
    for b, v in zip(bars, data):
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v:,}", ha="center", va="bottom", fontsize=9)
fig.suptitle("Experiment 2: Sysbench Memory (1M block, 10G total, 4 threads, write)")
plt.tight_layout()
plt.savefig("images/memory-comparison.png", dpi=150)
print("Saved images/memory-comparison.png")
