from collections import Counter

import matplotlib.pyplot as plt

import data
import util

TOP_N = 30


def run():
    assignee_count = Counter()
    reporter_count = Counter()

    for issue in data.created_issues:
        if issue.fields.assignee:
            assignee_count[issue.fields.assignee.displayName] += 1

        if issue.fields.reporter:
            reporter_count[issue.fields.reporter.displayName] += 1

    total_count = assignee_count + reporter_count
    top_users = [name for name, _ in total_count.most_common(TOP_N)][::-1]

    as_reporter = [reporter_count[name] for name in top_users]
    as_assignee = [assignee_count[name] for name in top_users]

    plt.figure()

    plt.barh(top_users, as_reporter, color="tab:blue", label="Reporter")
    plt.barh(
        top_users, as_assignee, left=as_reporter, color="tab:green", label="Assignee"
    )

    plt.title(f"4. Top {TOP_N} Users by Number of Tasks (Assignee + Reporter)")
    plt.xlabel("Tasks")
    plt.ylabel("User")
    plt.legend(loc="lower right")
    plt.grid(True, axis="x", alpha=0.3)
    plt.tight_layout()

    plt.savefig(f"{util.OUT_DIR}/4.png")
    plt.close()
