---
url: 'https://docs.workato.com/en/connectors/smartsheet/new-row.md'
description: >-
  The New row in report trigger in the Smartsheet connector fires when a row is
  added in a Smartsheet report and fetches existing rows first.
---

# Smartsheet - New row in report trigger

The **New row in report** trigger activates when a row is added in a Smartsheet report. This trigger fetches all existing rows in the report initially.

![New or updated row trigger](/assets/new-row-trigger.BHowW7hq.png)_Smartsheet - New row in report trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Determines the frequency of the event check. You can choose a specific interval from the drop-down menu or leave it at the default setting. |
| Report name | The name of the Smartsheet report you are monitoring for new rows. |

## Output

| Output field | Description |
| --- | --- |
| Row ID | The unique identifier for the row that was added. |
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
