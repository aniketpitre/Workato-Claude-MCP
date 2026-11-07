---
url: 'https://docs.workato.com/en/connectors/wrike/updated-timelog-trigger.md'
description: >-
  The New/updated timelog trigger in the Wrike connector picks up timelog
  records that are created or updated, processing each record as a separate job.
---

# Wrike - New/updated timelog trigger

This trigger picks up timelog records that are created or updated. Each record is processed as a separate job. It checks for new jobs once every poll interval.

![New/updated timelog trigger](/assets/updated-timelog-trigger.CULH6HXi.png)_New/updated timelog trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Timelog records created or updated after this time will be processed by the recipe. If left blank, the default will be set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| Timelog ID | The ID of the timelog record. |
| Task ID | The ID of the task that this timelog record tracks. |
| User ID | The ID of the user who tracked the timelog record. |
| Category ID | The ID of the category of this timelog record. |
| Hours | The hours tracked in the timelog record. |
| Created date | The date this timelog record was created. |
| Updated date | The date this timelog record was updated. |
| Completed date | The date this timelog record was completed. |
| Comment | The comment to this timelog record. |

---
