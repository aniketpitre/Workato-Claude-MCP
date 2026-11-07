---
url: 'https://docs.workato.com/en/connectors/wrike/search-timelogs-action.md'
description: >-
  The Search timelogs action in the Wrike connector retrieves timelog records
  that match all of the search criteria you specify.
---

# Wrike - Search timelogs action

This action retrieves a list of timelog records that matches your search criteria. Only records in your Wrike instance that match all the criteria will be returned.

![Search timelogs action](/assets/search-timelogs-action.BKMN9U4N.png)_Search timelogs action_

## Input

| Input field | Description |
| --- | --- |
| Timelog category | Select the category for your timelog record. This will be blank by default. |
| Created date | Retrieve timelog records created after this date. |
| Updated date | Retrieve timelog records updated after this date. |
| Tracked date | Retrieve timelog records tracked after this date. |
| Descendants | Select `Yes` to add all descendant tasks to search scope, otherwise select `No`. |

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
| Tracked date | The date this timelog record was recorded. |
| Comment | The comment to this timelog record. |
| List size | The size of the list, corresponding to the number of timelog records retrieved. |

---
