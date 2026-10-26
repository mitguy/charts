import matplotlib.pyplot as plt

import data
import util

SECONDS_PER_HOUR = 3600


def run():
    logged_hours = []

    for issue in data.closed_issues:
        if issue.fields.timespent:
            logged_hours.append(issue.fields.timespent / SECONDS_PER_HOUR)

        # https://github.com/pycontribs/jira/blob/main/docs/examples.rst#fields
        # if issue.fields.timetracking.timespentSeconds:
        #     logged_hours.append(issue.fields.timetracking.timespentSeconds / 3600)

    plt.figure()

    plt.hist(logged_hours, bins="auto")

    plt.title("5. Logged Time per Closed Task")
    plt.xlabel("Logged time (hours)")
    plt.ylabel("Tasks")
    plt.tight_layout()

    plt.savefig(f"{util.OUT_DIR}/5.png")
    plt.close()
