---
url: 'https://docs.workato.com/en/connectors/github/new-updated-pr-trigger.md'
description: >-
  The New or updated pull request (real-time) trigger monitors a GitHub
  repository and triggers when a pull request is created or updated.
---

# GitHub - New or updated pull request (real-time) trigger

The **New or updated pull request** (real-time) trigger monitors a GitHub repository and runs when a pull request (PR) is created or updated.

## Input

| Input field | Description |
| --- | --- |
| Organization | Select from the drop-down menu or enter the organization name. You can find the organization name in your GitHub URL. For example, `https://github.com/organization/repo_name/`. |
| Repository name | Enter the repository name you plan to monitor for new PRs. |
| Action | Select the PR status you plan to monitor new or updated PRs for in the repository. Available statuses include`All`, `Opened PR`, `Closed PR`, `Reopened PR`, `Assigned PR`, and `Unassigned PR`. |

## Output

| Output field | Description |
| --- | --- |
| URL | The URL of the new or updated PR. |
| ID | The ID of the new or updated PR. |
| HTML URL | The URL linking to the new or updated PR in HTML format. |
| Diff URL | The URL linking to the diff of the new or updated PR. |
| Patch URL | The URL linking to the patch associated with the new or updated PR. |
| Issue URL | The URL linking to the issue associated with the new or updated PR. |
| Number | The number of the new or updated PR. |
| State | The state of the new or updated PR. For example, `Open`. |
| Locked | Indicates if the new or updated PR is locked or not. |
| Title | The title of the new or updated PR. |
| Merged | Indicates if the new or updated PR is merged or not. |
| Mergeable | Indicates if the new or updated PR is eligible to merge or not. |
| Mergeable state | Indicates if the new or updated PR is in a mergeable state or not. |
| Comments | Lists any comments associated with the new or updated PR. |
| Review comments | The review comments associated with the new PR. |
| Maintainer can modify | Indicates if the user with the maintainer role can modify the new or updated PR. |
| Commits | Lists commits associated with the new or updated PR. |
| Additions | Any newly added lines to the PR. |
| Deletions | Any lines deleted from the PR. |
| Changed files | Lists any files changed in the PR. |
| Body | The body of the PR. |
| Created at | The date and time when the new or updated PR was created. |
| Updated at | The date and time when the new or updated PR was updated. |
| Closed at | The date and time when the new or updated PR was closed. |
| Merged at | The date and time when the new or updated PR was merged. |
| Merge commit SHA | The commit SHA associated with the PR. |
| Labels | Any labels associated with the new or updated PR. |
| Milestone | Information about any milestones associated with the new or updated PR. |
| Commits URL | The URL linking to the commits associated with the new or updated PR. |
| Review comments URL | The URL linking to the review comments associated with the new or updated PR. |
| Comments URL | The URL linking to the comments associated with the new or updated PR. |
| Statuses URL | The URL linking to the statuses associated with the new or updated PR. |
| Head | Information about the head commit associated with the new or updated PR. |
| Base | Information about the base commit associated with the new or updated PR. |
| Links | Information about the links associated with the new or updated PR. |
| Merged by | Information about the user that merged the new or updated PR. |
| Assignee | Information about the assignee of the new or updated PR. |
| Assignees | Information about the assignees of the new or updated PR. |
| User | Information about the user of the new or updated PR. |
| Requested reviewers | Information about the requested reviewers of the new or updated PR. |

---
