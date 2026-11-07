---
url: 'https://docs.workato.com/en/connectors/percolate/deleted-object-trigger.md'
description: >-
  The Deleted object trigger in the Percolate connector fires in real time when
  an object of a selected type is deleted for a chosen team.
---

# Percolate - Deleted object trigger (real-time)

The **Deleted object** real-time trigger activates when an object is deleted in Percolate. This trigger operates in real-time.

![Deleted object in Percolate trigger](/assets/deleted-object-trigger.Km1v391O.png)_Percolate - Deleted object trigger_

## Input

| Input field | Description |
| --- | --- |
| Object name | Select the type of object you plan to monitor for deletion. |
| Team | Choose the team or specify the team ID for the objects you plan to track. |
| Team Metadata | Choose this option if you require metadata for the team, particularly if your object is linked to the team ID input field or if you select more than 100 teams. Selecting a team overrides this field's input. |
| Time to live (in seconds) | Specify the retention period for undelivered event messages. The default is 0, which means there is no time limit. The maximum duration you can set is 72 hours (259200 seconds). |

## Output

The output of this action varies based on the type of object you select.

---
