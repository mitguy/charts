// Package jira is for communicating with Jira
package jira

import (
	"fmt"

	jira "github.com/andygrunwald/go-jira"
)

const JiraClientURL = "https://issues.apache.org/jira/"

var JiraClient *jira.Client

func init() {
	var err error

	JiraClient, err = jira.NewClient(nil, JiraClientURL)
	if err != nil {
		panic(err)
	}
}

func getAllIssues(client *jira.Client, searchString string) ([]jira.Issue, error) {
	last := 0

	var issues []jira.Issue

	for {
		opt := &jira.SearchOptions{
			MaxResults: 1000, // max 1000
			StartAt:    last,
		}

		chunk, resp, err := client.Issue.Search(searchString, opt)
		if err != nil {
			return nil, err
		}

		total := resp.Total
		if issues == nil {
			issues = make([]jira.Issue, 0, total)
		}

		issues = append(issues, chunk...)

		last = resp.StartAt + len(chunk)
		if last >= total {
			return issues, nil
		}
	}
}

func Fetch(jql string) jira.Issue {
	fmt.Printf("JQL: \"%s\"\n", jql)

	issue, _, err := JiraClient.Issue.Search(jql,
		&jira.SearchOptions{
			MaxResults: 1,
		},
	)
	if err != nil {
		panic(err)
	}

	return issue[0]
}

func FetchAll(jql string) []jira.Issue {
	fmt.Printf("JQL: \"%s\"\n", jql)

	issues, err := getAllIssues(JiraClient, jql)
	if err != nil {
		panic(err)
	}

	return issues
}
