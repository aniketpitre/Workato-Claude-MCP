---
url: 'https://docs.workato.com/en/connectors/smartsheet/new-updated-report.md'
description: >-
  The New or updated row in report trigger in the Smartsheet connector fires
  when a row is added or changed in a Smartsheet report.
---

# Smartsheet - New or updated row in report trigger

The **New or updated row in report** trigger activates when a row is added or changed in a Smartsheet report. This trigger fetches all existing rows in the report initially, and then captures updates to rows as they occur. It does not pick up comments or attachments when they are added or updated in a row.

![New or updated row trigger](/assets/new-or-updated-row-trigger.CwlPVtQw.png)_Smartsheet - New or updated row in report trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Determines the frequency of the event check. You can choose a specific interval from the drop-down menu or leave it at the default setting. |
| Report name | The name of the Smartsheet report you plan to monitor for new or updated rows. |

## Output

| Output field | Description |
| --- | --- |
| Row ID | The unique identifier for the row that was added or updated. |
| Sheet ID | The identifier of the sheet where the row is located. |
| Row number | The number of the row within the sheet. |
| Sibling ID | The identifier of the adjacent row. |
| Expanded | Indicates whether the row is expanded. |
| Access level | The level of access the user has to the row. |
| Created at | The timestamp when the row was originally created. |
| Modified at | The timestamp of the most recent update to the row. |
| Cells | The content of the cells within the row. |
| Discussions | A count or list of discussions associated with the row. |
| Attachments | A count or list of attachments associated with the row. |

---
