---
url: 'https://docs.workato.com/en/connectors/percolate/new-object-trigger.md'
description: >-
  The New object trigger in the Percolate connector fires in real time when an
  object of a selected type is created for a chosen team.
---

# Percolate - New object trigger (real-time)

The **New object** real-time trigger activates when an object is created in Percolate. This trigger operates in real-time.

![New object in Percolate trigger](/assets/new-object-trigger.C6CjQ0a5.png)_Percolate - New object trigger_

## Input

| Input field | Description |
| --- | --- |
| Object name | Select the type of object you plan to monitor for new events. |
| Team | Choose the team or specify the team ID for the objects you plan to track. |
| Team Metadata | Choose this option if you require metadata for the team, particularly if your object is linked to the team ID input field or if you select more than 100 teams. Selecting a team overrides this field's input. |
| Time to live (in seconds) | Specify the retention period for undelivered event messages. The default is 0, which means there is no time limit. The maximum duration you can set is 72 hours (259200 seconds). |

## Output

The output of this action varies based on the type of object you select.

---
