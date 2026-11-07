---
url: 'https://docs.workato.com/en/connectors/github/new-pr-trigger.md'
description: >-
  The New PR trigger monitors a GitHub repository and triggers when a new PR is
  created.
---

# GitHub - New PR trigger

The **New PR** trigger monitors a GitHub repository and triggers when a new pull request (PR) is created.

## Input

| Input field | Description |
| --- | --- |
| Organization | Select from the drop-down menu or enter the organization name. You can find the organization name in your GitHub URL. For example, `https://github.com/organization/repo_name/`. |
| Repository name | Enter the repository name you plan to monitor for new PRs. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the new PR. |
| URL | The URL of the new PR. For example,`https://api.github.com/repos/test-demo-check/demo-repository/issues/2`. |
| HTML URL | The URL linking to the PR in HTML format. |
| Diff URL | The URL linking to the diff of the PR. |
| Patch URL | The URL linking to the patch associated with the PR. |
| Issue URL | The URL linking to the issue associated with the PR. |
| Commits URL | The URL linking to the commits associated with the PR. |
| Review comments | The review comments associated with the new PR. |
| Review comment URL | The URL linking to the PR's review comment. |
| Comments URL | The URL linking to the PR's comments. For example, `https://api.github.com/repos/test-demo-check/demo-repository/issues/2/comments`. |
| Statuses URL | The URL linking to the status associated with the PR. |
| Number | The number of the PR. |
| State | The state that the PR is in. For example, `Open`. |
| Title | The title of the PR. |
| Body | The contents of the body of the PR. |
| Assignee | Details about the user assigned to the PR. |
| Milestone | Information about any milestones associated with the PR. |
| Locked | Indicates if the PR is locked or not. |
| Created at | The date and time when the PR was created. |
| Updated at | The date and time when the PR was updated. |
| Closed at | The date and time when the PR was closed. |
| Merged at | The date and time when the PR was merged. |
| Head | Information about the head commit associated with the PR. |
| Base | Information about the base commit associated with the PR. |
| Links | Information about any links associated with the PR. |
| User | Information about the user associated with the PR. |

---

---
url: >-
  https://docs.workato.com/en/connectors/github/new-updated-issue-comment-trigger.md
description: >-
  The New or updated issue comment (real-time) trigger monitors a GitHub
  repository and triggers when a comment on an issue is created or updated.
---

# GitHub - New or updated issue comment (real-time) trigger

The **New or updated issue comment** (real-time) trigger monitors a GitHub repository. This trigger runs when a comment on an issue is created or updated.

## Input

| Input field | Description |
| --- | --- |
| Organization | Select from the drop-down menu or enter the organization name. You can find the organization name in your GitHub URL. For example, `https://github.com/organization/repo_name/`. |
| Repository name | Enter the repository name you plan to monitor for new pull requests. |

## Output

| Output field | Description |
| --- | --- |
| Action | The issue status monitored for new or updated issue comments in the repository. |
| Comment | Information about the issue comment. |
| Issue | Information about the issue the comment is associated with. |

---
