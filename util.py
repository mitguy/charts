import matplotlib.pyplot as plt

OUT_DIR = "out"
BAR_CHARTS = False

plt.style.use("dark_background")

plt.rcParams.update(
    {
        "figure.figsize": (20, 11.25),
        "figure.dpi": 96,
        "savefig.dpi": 96,
        "font.family": "JetBrainsMonoNL Nerd Font",
        "font.size": 14,
        "axes.titlesize": 22,
        "axes.labelsize": 16,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "legend.fontsize": 14,
    }
)
