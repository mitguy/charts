from collections import Counter
from datetime import datetime, timedelta
from itertools import accumulate

import matplotlib.pyplot as plt

import data
import util


def run():
    created_per_day = Counter()
    closed_per_day = Counter()

    for issue in data.created_resolved_issues:
        created_per_day[datetime.fromisoformat(issue.fields.created).date()] += 1

        if issue.fields.resolutiondate:
            closed_per_day[
                datetime.fromisoformat(issue.fields.resolutiondate).date()
            ] += 1

    start = min(created_per_day)
    end = max(max(created_per_day), max(closed_per_day))

    days = [start + timedelta(days=i) for i in range((end - start).days + 1)]

    created_daily = [created_per_day[d] for d in days]
    closed_daily = [closed_per_day[d] for d in days]

    created_cum = list(accumulate(created_daily))
    closed_cum = list(accumulate(closed_daily))

    plt.figure()

    created_bars = plt.bar(days, created_daily, color="tab:blue", alpha=0.5)
    closed_bars = plt.bar(days, closed_daily, color="tab:green", alpha=0.5)

    plt.title("3. Created/Closed Tasks per Day and Cumulative Totals")
    plt.xlabel("Date")
    plt.ylabel("Tasks per day")
    plt.xticks(rotation=30)

    plt.twinx()

    (created_line,) = plt.plot(days, created_cum, color="tab:blue")
    (closed_line,) = plt.plot(days, closed_cum, color="tab:green")

    plt.ylabel("Cumulative tasks")

    plt.legend(
        [created_bars, closed_bars, created_line, closed_line],
        [
            "Created per day",
            "Closed per day",
            "Created (cumulative)",
            "Closed (cumulative)",
        ],
        loc="upper left",
    )
    plt.tight_layout()

    plt.savefig(f"{util.OUT_DIR}/3.png")
    plt.close()
