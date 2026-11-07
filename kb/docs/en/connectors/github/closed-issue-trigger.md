---
url: 'https://docs.workato.com/en/connectors/github/closed-issue-trigger.md'
description: >-
  The Closed issue trigger monitors a GitHub repository and triggers when an
  issue is closed.
---

# GitHub - Closed issue trigger

The **Closed issue** trigger monitors a GitHub repository and triggers when an issue closes.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Select a start date and time to start retrieving events. Leave this blank to start from one hour ago. After you run or test the recipe, you can't change this value. |
| Organization | Select from the drop-down menu or enter the organization name. You can find the organization name in your GitHub URL. For example, `https://github.com/organization/repo_name/`. |
| Repository name | Enter the repository name you plan to monitor for closed issues. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the closed GitHub issue. |
| URL | The URL of the closed GitHub issue. For example, `https://api.github.com/repos/test-demo-check/demo-repository/issues/2`. |
| Repository URL | The URL of the GitHub repository where the issue was created. For example, `https://api.github.com/repos/test-demo-check/demo-repository`. |
| Labels URL | The issue URL that contains any labels associated with the issue. For example, `https://api.github.com/repos/test-demo-check/demo-repository/issues/2/labels{/name}`. |
| Comments URL | The URL linking to the issue's comments. For example, `https://api.github.com/repos/test-demo-check/demo-repository/issues/2/comments`. |
| Events URL | The URL linking to any events associated with the issue. For example, `https://api.github.com/repos/test-demo-check/demo-repository/issues/2/events`. |
| HTML URL | The URL linking to the issue in HTML format. |
| Number | The number of the issue. |
| State | The state that the issue is in. Such as, `Open`. |
| Locked | Indicates if the issue is locked or not. |
| Title | The title of the issue. |
| Body | The contents of the body of the issue. |
| Score | The score of the user calculated by GitHub. |
| User | Information of the user that created the issue. |
| Labels | Details about each label associated with the issue. |
| Assignee | Details about the user assigned to the issue. |
| Assignees | Information included if there are multiple assignees. |
| Milestone | Information about any milestones associated with the issue. |
| Comments | Lists any comments associated with the issue. |
| Pull request | Information about any pull requests associated with the issue, such as the pull request URL. |
| Closed at | The date and time when the issue was closed. |
| Created at | The date and time when the issue was created. |
| Updated at | The date and time when the issue was updated. |
| Closed by | Information about the user that closed the issue. |

---
