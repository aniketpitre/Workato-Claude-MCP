---
url: 'https://docs.workato.com/en/connectors/percolate/updated-object-trigger.md'
description: >-
  The New or updated object trigger in the Percolate connector fires in real
  time when an object is created or updated for a selected object type and team.
---

# Percolate - New or updated object trigger (real-time)

The **New or updated object** real-time trigger activates when an object is created or updated in Percolate. This trigger operates in real-time.

![New or updated object in Percolate trigger](/assets/new-or-updated-object-trigger.C1qzTL5N.png)_Percolate - New or updated object trigger_

## Input

| Input field | Description |
| --- | --- |
| Object name | Select the object type you plan to monitor for new instances or updates. |
| Team | Choose the team or specify the team ID for the objects you plan to track. |
| Team Metadata | Choose this option if you require metadata for the team, particularly if your object is linked to the team ID input field or if you select more than 100 teams. Selecting a team overrides this field's input. |
| Time to live (in seconds) | Specify the retention period for undelivered event messages. The default is 0, which means there is no time limit. The maximum duration you can set is 72 hours (259200 seconds). |

## Output

The output of this action varies based on the type of object you select.

---
