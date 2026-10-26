from collections import Counter

import matplotlib.pyplot as plt

import data
import util

# curl -s "https://issues.apache.org/jira/rest/api/2/priority" | jq .
PRIORITY_ORDER = [
    "Blocker",
    "Urgent",
    "Critical",
    "High",
    "Major",
    "Normal",
    "Minor",
    "Low",
    "Trivial",
    "P0",
    "P1",
    "P2",
    "P3",
    "P4",
    "Not a Priority",
    "None",
]


def run():
    priority_count = Counter()

    for issue in data.priority_issues:
        name = issue.fields.priority.name if issue.fields.priority else "None"
        priority_count[name] += 1

    priorities = [p for p in PRIORITY_ORDER if priority_count[p]]
    priorities += [p for p in priority_count if p not in PRIORITY_ORDER]
    counts = [priority_count[p] for p in priorities]

    plt.figure()

    plt.bar(priorities, counts, color="tab:blue")

    plt.title("6. Tasks by Priority")
    plt.xlabel("Priority")
    plt.ylabel("Tasks")
    plt.grid(True, axis="y", alpha=0.3)

    for i, count in enumerate(counts):
        plt.text(i, count, str(count), ha="center", va="bottom")

    plt.tight_layout()

    plt.savefig(f"{util.OUT_DIR}/6.png")
    plt.close()
