---
url: 'https://docs.workato.com/en/connectors/github/create-issue-action.md'
description: The Create issue action creates a new issue in GitHub.
---

# GitHub - Create issue action

The **Create issue** action creates a new issue in GitHub.

## Input

| Input field | Description |
| --- | --- |
| Organization | Select from the drop-down menu or enter the organization name. You can find the organization name in your GitHub URL. For example, `https://github.com/organization/repo_name/`. |
| Repository name | Enter the repository name you plan to monitor for new pull requests. |
| Issue title | Enter the title of the issue. This first comment typically describes the issue. |
| Body | Enter the text to include in the issue. |
| Assignees | Enter GitHub usernames to assign to the issue. Separate multiple usernames with commas. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the newly created issue. |
| URL | The URL of the newly created issue. |
| Repository URL | The URL of the GitHub repository where the issue was created. |
| Labels URL | The issue URL that contains any labels associated with the newly created issue. |
| Comments URL | The URL linking to the newly created issue's comments. |
| Events URL | The URL linking to any events associated with the newly created issue. |
| HTML URL | The URL linking to the newly created issue in HTML format. |
| Number | The number of the newly created issue. |
| State | The state that the newly created issue is in. For example, `Open`. |
| Locked | Indicates if the newly created issue is locked or not. |
| Title | The title of the newly created issue. |
| Body | The contents of the body of the newly created issue. |
| Score | The score of the user calculated by GitHub. |
| User | Information of the user that created the issue. |
| Labels | Details about each label associated with the newly created issue. |
| Assignee | Details about the user assigned to the newly created issue. |
| Assignees | Information included if there are multiple assignees. |
| Milestone | Information about any milestones associated with the newly created issue. |
| Comments | Lists any comments associated with the newly created issue. |
| Pull request | Information about any pull requests associated with the newly created issue, such as the pull request URL. |
| Closed at | The date and time when the issue was closed. |
| Created at | The date and time when the issue was created. |
| Updated at | The date and time when the issue was updated. |
| Closed by | Information about the user that closed the issue. |

---
