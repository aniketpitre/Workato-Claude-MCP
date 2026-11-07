---
url: >-
  https://docs.workato.com/en/connectors/marketo/monitor-leads-added-to-list-trigger.md
description: >-
  The Monitor leads added to list trigger (batch) in the Marketo connector picks
  up leads added to a specified list each poll interval, in batches.
---

# Marketo - Monitor leads added to list trigger (batch)

This trigger picks up leads added to a specified list in your Marketo instance. It checks for new leads once every poll interval and Workato processes each lead as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up leads added to the list from this specified date and time. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| List | Select the list to monitor for new leads. Alternatively, switch to **Use list IDs** to enter a comma-separated list of IDs. The list ID is the first contiguous set of numbers after the `ST` in the URL. For example, if the list URL is `https://app-ab.marketo.com/#ST1001A1`, then `1001` is the list ID. |
| Enrich lead data | Select whether to enrich the lead data. If **Yes**, the trigger output performs additional requests to supplement each activity record with the associated lead data. If you plan to reduce the number of API requests, select **No** to exclude lead enrichment requests. |
| Batch size | Provide the number of records to be returned in each job. The minimum batch size is `1` and the maximum is `1000`. This field defaults to `300`. |

## Output

| Field | Description |
| --- | --- |
| First lead ID | The identifier of the first lead in the batch. |
| Last lead ID | The identifier of the last lead in the batch. |
| First batch | Whether this is the first batch of lead activities. |
| Last batch | Whether this is the last batch of lead activities. |
| Total number of records | The total number of records in the batch. |
| Activities | The activities associated with the leads. |
| Activity ID (activities) | The identifier of the activity. |
| Lead ID (activities) | The identifier of the lead associated with the activity. |
| Activity date (activities) | The datetime of the activity. |
| Activity type ID (activities) | The identifier of the activity type. |
| Primary attribute value ID (activities) | The identifier of the primary attribute value. |
| Activity primary attribute (activities) | The primary attribute of the activity. |
| Attributes (activities) | List of attributes associated with the activity. |
| Name (attributes) | The name of the attribute. |
| Value (attributes) | The value of the attribute. |
| Lead (activities) | An object representing the lead associated with the activity. |

Refer to the Marketo documentation for a [list of standard fields](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/assets/list-of-standard-fields) available through the API. This list includes common fields but may not cover all input fields specific to this action.
