---
url: 'https://docs.workato.com/en/connectors/github/list-statuses-for-ref-action.md'
description: >-
  The List statuses for a ref (batch) action lists all statuses associated with
  a reference (ref) in GitHub. A ref is a commit SHA, branch name, or tag in
  GitHub.
---

# GitHub - List statuses for a ref (batch) action

The **List statuses for a ref (batch)** action lists all statuses associated with a reference (ref) in GitHub. A ref is a commit SHA, branch name, or tag in GitHub.

## Input

| Input field | Description |
| --- | --- |
| Organization | Select from the drop-down menu or enter the organization name. You can find the organization name in your GitHub URL. For example, `https://github.com/organization/repo_name/`. |
| Repository name | Enter the repository name you plan to monitor for new issues. |
| Reference | Enter the reference you plan to list statuses from. For example, a commit SHA, branch name, or tag in GitHub. |

## Output

| Output field | Description |
| --- | --- |
| Created at | The date and time when the status was created. |
| Updated at | The date and time when the status was updated. |
| State | The state that the status is in. For example, `Open`. |
| Target URL | The URL associated with a specified reference. |
| Description | The description associated with the reference. |
| ID | The ID of the new GitHub status. |
| Context | An identifier for the source of a commit status. |
| Creator | Information about the user that created the status. |
| List size | The number of statuses in the list. |
| List index | The position of the returned status in the list. |

---
