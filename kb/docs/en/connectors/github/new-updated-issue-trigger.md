---
url: 'https://docs.workato.com/en/connectors/github/new-updated-issue-trigger.md'
description: >-
  The New or updated issue (real-time) trigger monitors a GitHub repository and
  triggers when an issue is created or updated.
---

# GitHub - New or updated issue (real-time) trigger

The **New or updated issue** (real-time) trigger monitors a GitHub repository and runs when an issue is created or updated.

## Input

| Input field | Description |
| --- | --- |
| Organization | Select from the drop-down menu or enter the organization name. You can find the organization name in your GitHub URL. For example, `https://github.com/organization/repo_name/`. |
| Repository name | Enter the repository name you plan to monitor for new or updated issues. |
| Action | Select the issue status you plan to monitor new or updated issues for in the repository. Available statuses include `All`, `Opened issue`, `Closed issue`, `Reponed issue`, `Assigned issue`, `Unassigned issue`, `Labled issue`, `Unlabeled issue`, `Edited issue`, `Milestoned issue`, and `Demiledstoned issue`. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the new or updated issue. |
| URL | The URL of the new or updated issue. For example, `https://api.github.com/repos/test-demo-check/demo-repository/issues/2`. |
| Repository URL | The URL of the GitHub repository where the new or updated issue was created. For example, `https://api.github.com/repos/test-demo-check/demo-repository`. |
| Labels URL | The issue URL that contains any labels associated with the new or updated issue. For example, `https://api.github.com/repos/test-demo-check/demo-repository/issues/2/labels{/name}`. |
| Commits URL | The URL linking to the commits associated with the new or updated issue. |
| Events URL | The URL linking to any events associated with the new or updated issue. For example, `https://api.github.com/repos/test-demo-check/demo-repository/issues/2/events`. |
| HTML URL | The URL linking to the new or updated issue in HTML format. |
| Number | The number of the new or updated issue. |
| State | The state that the new or updated issue is in. For example, `Open`. |
| Title | The title of the new or updated issue. |
| Body | The contents of the body of the new or updated issue. |
| Comments | Lists any comments associated with the new or updated issue. |
| Closed at | The date and time when the new or updated issue was closed. |
| Created at | The date and time when the new or updated issue was created. |
| Updated at | The date and time when the new or updated issue was updated. |
| Locked | Indicates if the new or updated issue is locked or not. |
| Labels | Details about each label associated with the new or updated issue. |
| Milestone | Information about any milestones associated with the new or updated issue. |
| Assignee | Details about the user assigned to the new or updated issue. |
| Assignees | Information included if there are multiple assignees. |
| User | Information of the user that created the new or updated issue. |
| Closed by | Information about the user that closed the new or updated issue. |

---
