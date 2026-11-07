---
url: >-
  https://docs.workato.com/en/connectors/marketo/new-updated-lead-batch-trigger.md
description: >-
  The New/updated lead trigger (batch) in the Marketo connector picks up new or
  updated leads in batches each poll interval, processed as separate jobs.
---

# Marketo - New/updated lead trigger (batch)

This trigger picks up new or updated leads in batches in your Marketo instance. It checks for new or updated leads once every poll interval and Workato processes each batch as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up leads modified from this specified date and time. Defaults to fetching leads modified an hour ago if left blank. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| List / List ID | Select or provide the list ID to monitor for new or updated leads. |
| Fields to monitor | Select the fields you plan to monitor for changes and use in the recipe. All fields are selected if left blank. However, leaving this field blank isn't recommended as it can result in timeout errors. |
| Batch size | The size of the batch to be returned. The minimum value is `1` and the maximum is `1000`. Defaults to `1000`. |

Refer to the Marketo documentation for a [list of standard fields](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/assets/list-of-standard-fields) available through the API. This list includes common fields but may not cover all input fields specific to this action.

## Output

The output datatree contains information about the leads, including all the fields defined under **Fields to monitor** in the trigger configuration.

| Field | Description |
| --- | --- |
| First lead ID | The ID of the first lead in the batch. |
| Last lead ID | The ID of the last lead in the batch. |
| Total leads | The total number of leads in the batch. |
| Leads | The leads in the batch. |
