import re
from collections import defaultdict
from datetime import datetime

import matplotlib.pyplot as plt

import data
import util

MAX_TRANSITION_DAYS = 365
SECONDS_PER_DAY = 86400
BIN_WIDTH_DAYS = 1


def run():
    status_days = defaultdict(list)

    for issue in data.closed_issues:
        transitions = []

        for history in issue.changelog.histories:
            for item in history.items:
                if item.field == "status":
                    transitions.append(
                        (
                            datetime.fromisoformat(history.created),
                            item.fromString,
                            item.toString,
                        )
                    )

        if not transitions:
            continue

        # sort only by 1st item
        transitions.sort(key=lambda x: x[0])

        time_in_status = defaultdict(float)
        prev_time = datetime.fromisoformat(issue.fields.created)

        for changed_at, from_status, _ in transitions:
            seconds = (changed_at - prev_time).total_seconds()
            prev_time = changed_at

            # skip transitions longer than 365 days
            if seconds / SECONDS_PER_DAY > MAX_TRANSITION_DAYS:
                continue

            time_in_status[from_status] += seconds

        for status, seconds in time_in_status.items():
            status_days[status].append(seconds / SECONDS_PER_DAY)

    bins = list(range(0, MAX_TRANSITION_DAYS + BIN_WIDTH_DAYS, BIN_WIDTH_DAYS))

    for status, durations in status_days.items():
        plt.figure()

        if util.BAR_CHARTS:
            counts = [0] * (len(bins) - 1)
            for days in durations:
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
            plt.hist(durations, bins=bins, color="tab:blue")

        plt.xticks(range(0, MAX_TRANSITION_DAYS + 1, 30))

        plt.title(f'Time in status "{status}"')
        plt.xlabel("Days")
        plt.ylabel("Tasks")
        plt.tight_layout()

        filename = re.sub(r"[^\w-]+", "_", status)
        plt.savefig(f"{util.OUT_DIR}/2_status_{filename}.png")
        plt.close()
