---
url: 'https://docs.workato.com/en/connectors/box/action-list-sign.md'
description: >-
  The List sign requests action (Batch) retrieves all sign requests created by a
  user in Box.
---

# Box - List sign requests action (batch)

The **List sign requests** batch action retrieves all sign requests created by a user in Box. If the files (`sign_files`) or the parent folder (`parent_folder`) associated with the request are deleted, Box excludes the request from the returned list.

## Input

| Input field | Description |
| --- | --- |
| Limit | Specify the maximum number of items to return per page. This field defaults to 100. |
| Next page marker | Set the position marker at which to begin returning results. This is used for paginating results. |

## Output

| Output field | Description |
| --- | --- |
| Sign requests | The list of sign requests retrieved. |
| Limit | The quota that was applied to the number of items returned. |
| Next page marker | The marker used to fetch the next page of results. |

---
