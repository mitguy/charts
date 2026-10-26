from datetime import datetime

import matplotlib.pyplot as plt

import data
import util

MAX_RESOLUTION_DAYS = 365
BIN_WIDTH_DAYS = 1


def run():
    resolution_days = []

    for issue in data.closed_issues:
        resolution_time = (
            datetime.fromisoformat(issue.fields.resolutiondate)
            - datetime.fromisoformat(issue.fields.created)
        ).days

        if resolution_time <= MAX_RESOLUTION_DAYS:
            resolution_days.append(resolution_time)

    plt.figure()

    bins = list(range(0, MAX_RESOLUTION_DAYS + BIN_WIDTH_DAYS, BIN_WIDTH_DAYS))

    if util.BAR_CHARTS:
        counts = [0] * (len(bins) - 1)
        for days in resolution_days:
            idx = int(days // BIN_WIDTH_DAYS)
            if idx < len(counts):
                counts[idx] += 1
        plt.bar(
            bins[:-1],
            counts,
            width=BIN_WIDTH_DAYS,
            align="edge",
            color="tab:blue",
        )
    else:
        plt.hist(resolution_days, bins=bins, color="tab:blue")

    plt.xticks(range(0, MAX_RESOLUTION_DAYS + 1, 30))

    plt.title("1. Task/Time Histogram")
    plt.xlabel("Days")
    plt.ylabel("Tasks")
    plt.tight_layout()

    plt.savefig(f"{util.OUT_DIR}/1.png")
    plt.close()
