---
url: 'https://docs.workato.com/en/connectors/kickflow/search-records-action.md'
description: The Search records action retrieves a list of records from Kickflow.
---

# Kickflow - Search records action

The **Search records** action retrieves a list of records from Kickflow.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of record to search, such as a ticket. Additional fields load dynamically based on the object you select. |
| Status | Filter by status. If you select `Tickets` as the object, select one or more statuses to filter by. Options include `Draft`, `In progress`, `Rejected`, `Completed`, `Denied`, and `Archived`. |
| Impersonate user ID | Optional. Enter the ID of the user to impersonate for this request. |

## Output

Output fields dynamically generate based on the object you select. Refer to the [Kickflow](https://developer.kickflow.com/rest/spec) documentation for a complete list of output fields.

---
