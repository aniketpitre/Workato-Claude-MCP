---
url: 'https://docs.workato.com/en/connectors/uipath/start-jobs-action.md'
description: >-
  The Start job(s) action allows you to start job(s) for a selected process in
  UiPath Orchestrator.
---

# UiPath - Start job(s) action

The **Start job(s)** action allows you to start job(s) for a selected process in UiPath Orchestrator.

## Input

| Input field | Description |
| --- | --- |
| Process | Select the process to execute from the drop-down menu. |
| Jobs count | Enter the number of jobs to start. |
| Job type | Select the runtime type of the machine session to consume for the job(s). |
| Job parameters | Set the values for the job parameters for the job(s). |
| User/Robot | Select the user/robot on which to execute the process. |
| Machine | Select the machine on which to execute the process. |

## Output

| Output field | Description |
| --- | --- |
| Job IDs | A unique identifier for the job. |

---

---
url: >-
  https://docs.workato.com/en/connectors/uipath/start-processing-queue-items-action.md
description: >-
  The Start processing queue items action allows you to start processing a queue
  item in UiPath Orchestrator.
---

# UiPath - Start processing queue items action

The **Start processing queue items** action allows you to start processing a queue item in UiPath Orchestrator.

## Input

| Input field | Description |
| --- | --- |
| Queue name | Provide the queue name to which the item belongs. |
| Robot identifier | The unique key identifying the robot that sent the request. Must be in the form of UUID. |
| Queue item content | Set the data to pass to the queue item. |
| Postpone until | Set the earliest date and time at which the item is available for processing. If empty, the item can be processed as soon as possible. |
| Deadline | Set the latest date and time at which the item should be processed. If empty, the item can be processed at any given time. |
| Reference | Custom reference value provided when the item was added to the queue. |
| Reference filter option | Select the suitable value from the drop-down menu. |
| Parent operation ID | Provide the unique ID for parent operation. |

## Output

| Output field | Description |
| --- | --- |
| Queue definition ID | Unique identifier of the queue to which the item belongs. It links the queue item to its parent queue definition in Orchestrator. |
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

---
