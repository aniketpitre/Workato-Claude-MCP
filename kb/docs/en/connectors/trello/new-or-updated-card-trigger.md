---
url: 'https://docs.workato.com/en/connectors/trello/new-or-updated-card-trigger.md'
description: >-
  The New or updated card trigger in the Trello connector fires in real time
  when a card is created or updated on a board you specify.
---

# Trello - New or updated card trigger (real-time)

The **New or updated card** trigger detects when a card is created or updated on a board you specify. The trigger checks for new cards and updates in real time and processes each event as a separate job.

## Input

| Field | Description |
| --- | --- |
| Board name | Select the board to monitor for new and updated cards. |
| Events | Select the type of change for the trigger to monitor. For example: `Created card`, `Deleted card`, `Created comment`, `Updated comment`, `Added label`, `Removed label` |

## Output

| Field | Description |
| --- | --- |
| ID | The ID of the card that triggered the job. |
| Creator ID | The ID of account that triggered the job. |
| Type | The type of update that triggered the job. |
| Date | A timestamp of when the job was triggered. |
| Member creator | An object that contains information about the account that created or updated the card, such as its `ID`, `Username`, and `Full name`. |
| Data | An object that contains information about the board, list, and card where the trigger event took place, such as their `ID` and `Name`. |

---
