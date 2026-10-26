from jira import JIRA

# https://jira.readthedocs.io/
jira = JIRA("https://issues.apache.org/jira/")

closed_issues = jira.search_issues(
    jql_str="project = Kafka and Status = Closed ORDER BY created ASC",
    fields="status,created,resolutiondate,timespent",
    expand="changelog",
    maxResults=False,
)

created_resolved_issues = jira.search_issues(
    jql_str="project = Kafka and created >= -365d and resolved >= -365d ORDER BY created ASC",
    fields="created,resolutiondate",
    maxResults=False,
)

created_issues = jira.search_issues(
    jql_str="project = Kafka and created >= -365d ORDER by created ASC",
    fields="assignee,reporter",
    maxResults=False,
)

priority_issues = jira.search_issues(
    jql_str="project = Kafka ORDER by created ASC",
    fields="priority",
    maxResults=False,
)
