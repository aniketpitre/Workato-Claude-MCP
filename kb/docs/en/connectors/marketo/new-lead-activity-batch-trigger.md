---
url: >-
  https://docs.workato.com/en/connectors/marketo/new-lead-activity-batch-trigger.md
description: >-
  The New lead activity trigger (batch) in the Marketo connector detects new
  lead activities each poll interval, processed as separate jobs.
---

# Marketo - New lead activity trigger (batch)

This trigger detects new lead activities in your Marketo instance. It checks for new activities once every poll interval and Workato processes each activity as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up lead activities from this specified date and time. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Activity | The activity types to monitor. You can select up to ten activities. |
| List | The list to monitor for lead activities. If empty, lead activities from all lists are included. |
| Enrich lead data | If you select **Yes**, the trigger output performs additional requests to supplement each activity record with the associated lead data. Select **No** to exclude lead enrichment requests to reduce the number of API requests. |

## Output

| Field | Description |
| --- | --- |
| First lead ID | The unique identifier of the first lead in the list. |
| Last lead ID | The unique identifier of the last lead in the list. |
| Activities | A list containing details about each lead activity. |
