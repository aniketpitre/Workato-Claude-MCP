---
url: 'https://docs.workato.com/en/connectors/uipath/search-items-in-queue-action.md'
description: >-
  The Search items in queue action allows you to retrieve a list of items in a
  queue in UiPath Orchestrator.
---

# UiPath - Search items in queue action

The **Search items in queue** action allows you to retrieve a list of items in a queue in UiPath Orchestrator.

## Input

| Input field | Description |
| --- | --- |
| Expand | Indicates the related entities to be represented inline. The maximum depth is 2. |
| Filter | Restricts the set of items returned. The maximum number of expressions is 100. For example, `FolderType` eq 'Standard'. Refer to the [UiPath documentation](https://docs.uipath.com/orchestrator/automation-cloud/latest/api-guide/building-api-requests#%24filter) for more information. |
| Select | Limits the properties returned in the result. |
| Order by | Specifies the order in which items are returned. The maximum number of expressions is 5, for example. |
| Top | Limits the number of items returned from a collection. The maximum value is 1000. |
| Skip | Excludes the specified number of items of the queried collection from the result. |
| Count | Indicates whether the total count of items within a collection are returned in the result. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the queue item. |
| Key | Internal key associated with the queue item. |
| Ancestor unique key | Unique key of the ancestor queue item, if applicable. |
| Manual ancestor unique key | Unique key of the manually linked ancestor item. |
| Robot ID | Identifier of the robot that processed the item. |
| Parent operation ID | ID of the parent operation linked to this queue item. |
| Operation ID | ID of the operation associated with the current processing attempt. |
| Output data | Output result data from processing the item. |
| Analytics data | Analytics or telemetry data captured during processing. |
| Reviewer user ID | ID of the user who reviewed the queue item, if review status is set. |
| Ancestor ID | System ID of the ancestor queue item. |
| Manual ancestor ID | System ID of the manually assigned ancestor item. |
| Retry number | Number of times the item has been retried. |
| Creation time | Timestamp when the queue item was created. |
| Progress | Text indicating the progress or stage of processing. |
| Processing exception type | Type of exception encountered (for example, Application, Business). |
| Has video recorded | Boolean indicating if a video was recorded during processing. |
| Processing exception | Details of the exception if the item failed during processing. |
| Reference | Custom reference provided when the item was added to the queue. |
| Start processing | Timestamp when the item began processing. |
| End processing | Timestamp when the item completed processing. |
| Defer date | Date/time after which the item becomes available for processing. |
| Risk SLA date | Date/time before which the item should be processed to meet SLA. |
| Due date | Optional due date for the queue item. |
| Status | Current status of the queue item (for example, New, Successful, Failed). |
| Review status | Status indicating whether the item was reviewed (for example, Pending, Accepted). |
| Priority | Priority level assigned to the item (for example, Low, Normal, High). |
| Unique key | A unique string key that ensures queue item uniqueness. |
| Organization unit ID | ID of the folder (organization unit) where the item exists. |
| Organization unit fully qualified name | Full path of the folder hierarchy for the queue item. |
| Seconds in previous attempts | Total time spent in all previous processing attempts. |
| Manual retry number | Number of times the item has been manually retried. |
| Specific data | Input data used for processing the queue item. |
| Row version | Version tracking token for concurrency control. |
| Encrypted | Indicates whether the queue item data is encrypted. |
| Queue definition ID | Identifier of the queue to which this item belongs. |
| Specific content | A list of custom input fields added to the queue item; in this case, it contains a single field named `Date` representing a date value used during item creation. |
| Output | Final output/result generated after processing. |
| Analytics | Analytical data tied to the transaction, typically used for reporting. |
| Count | Count of items returned. |

---
