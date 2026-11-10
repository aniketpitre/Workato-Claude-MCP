---
url: 'https://docs.workato.com/en/connectors/redmine/search-records-action.md'
description: >-
  The Search records action retrieves a list of issues from Redmine that match
  your search criteria.
---

# Redmine - Search records action

The **Search records** action retrieves a list of issues from Redmine that match your search criteria. The action returns only open issues unless you set **Status** to **All** or to a specific status.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type. **Issue** is the only supported object type. |
| Project | Select the project to filter issues by. Click **Use custom value** to enter a project ID manually. Use the numeric ID of the project, not its identifier. |
| Tracker | Select the tracker to filter issues by. Click **Use custom value** to enter a tracker ID manually. |
| Status | Select the status to filter issues by. Select **All** to return open and closed issues. Click **Use custom value** to enter a status ID, or `open`, `closed`, or `*`. |
| Assigned to | Select the user or group to filter issues by. Select **Me** for the user who authorized the connection. Click **Use custom value** to enter a user or group ID, or `me`. |
| Custom field filters | Enter custom fields to filter records by. |

## Output

This action returns many output fields. Refer to the [Redmine documentation](https://www.redmine.org/projects/redmine/wiki/Rest_Issues) for a representative set of output fields.

---
