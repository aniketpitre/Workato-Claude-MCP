---
url: >-
  https://docs.workato.com/en/connectors/cornerstone-hr/lock-or-unlock-goal-action.md
description: >-
  The Lock or unlock goal action locks or unlocks a goal's results in
  Cornerstone.
---

# Cornerstone HR - Lock or unlock goal action

The **Lock or unlock goal** action locks or unlocks a goal's results in Cornerstone HR.

## Input

| Input field | Description |
| --- | --- |
| Goal ID | Enter the internal ID of the goal you plan to lock or unlock. |
| User ID | Enter the ID of the user who owns the goal. |
| Title | Enter the title of the goal you plan to lock or unlock. |
| Lock results | Select whether to lock or unlock the goal's results. |

## Output

| Output field | Description |
| --- | --- |
| Data | An array containing the updated goal record, including its **Status**. |
| Status | The HTTP status code of the response. |
| Updated records | The number of goal records updated. |
| Timestamp | The date and time the goal was locked or unlocked. |
