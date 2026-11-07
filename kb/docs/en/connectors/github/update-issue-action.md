---
url: 'https://docs.workato.com/en/connectors/github/update-issue-action.md'
description: The update issue action updates a selected issue in GitHub.
---

# GitHub - Update issue action

The **Update issue** action updates a selected issue in GitHub.

## Input

| Input field | Description |
| --- | --- |
| Issue number | Enter the number associated with the issue. You can find the number at the end of the issue URL. |
| Organization | Select from the drop-down menu or enter the organization name. You can find the organization name in your GitHub URL. For example, `https://github.com/organization/repo_name/`. |
| Repository name | Enter the repository name where you plan to update an issue. |
| State | Select the new state for the issue. For example, `Open`. |
| Labels | Enter any labels associated with the issue you plan to update. |
| Milestone ID | The ID of the milestone associated with the issue you plan to update. |
| Issue title | Optional. Enter the title of the issue you plan to update. |
| Body | Optional. Enter the contents of the body of the issue. |
| Assignees | Optional. Enter the GitHub usernames of the assignees of the issue. The usernames must be comma separated. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the GitHub issue. |
| URL | The URL of the issue. |
| Repository URL | The URL of the repository where the action resides. |
| Labels URL | The issue URL that contains any labels associated with the issue. |
| Comments URL | The URL linking to the issue's comments. |
| Events URL | The URL linking to any events associated with the issue. |
| HTML URL | The URL linking to the issue in HTML format. |
| Number | The number of the issue. |
| State | The state that the issue is in. For example, `Open`. |
| Locked | Indicates if the newly created issue is locked or not. |
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
