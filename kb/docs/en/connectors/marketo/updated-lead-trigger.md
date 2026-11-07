---
url: 'https://docs.workato.com/en/connectors/marketo/updated-lead-trigger.md'
description: >-
  The New/updated lead trigger in the Marketo connector picks up new or updated
  leads each poll interval, processed as separate jobs.
---

# Marketo - New/updated lead trigger

This trigger picks up new or updated leads in your Marketo instance. It checks for new or updated leads once every poll interval and Workato processes each lead as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up leads modified from this specified date and time. Defaults to fetching leads modified an hour ago if left blank. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Output fields | Select the fields you plan to use in your recipe. All fields are returned if left blank. However, leaving this field blank isn't recommended as it can result in timeout errors. |

Refer to the Marketo documentation for a [list of standard fields](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/assets/list-of-standard-fields) available through the API. This list includes common fields but may not cover all input fields specific to this action.

## Output

The output datatree contains information about the lead, including all the fields defined under **Output fields** in the trigger configuration. By default, Workato retrieves the **Lead ID** and **Updated at** fields.

| Field | Description |
| --- | --- |
| Lead ID | The unique identifier of the lead. |
| Updated at | The time when the lead was last updated. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/marketo/activate-smart-campaign-action.md
description: >-
  The Activate smart campaign action in the Marketo connector lets you activate
  a smart campaign by its ID in your instance.
---

# Marketo - Activate smart campaign action

This action activates a smart campaign in Marketo.

## Input

| Field | Description |
| --- | --- |
| Smart campaign ID / Select campaign | Enter the smart campaign's unique identifier or select the smart campaign. The smart campaign ID is the first contiguous set of numbers after the `SC` in the URL. For example, if the URL ends with `SC1900A1`, the smart campaign ID is `1900`. |

## Output

| Field | Description |
| --- | --- |
| Success | Indicates whether the activation of the smart campaign was successful. |
| Request ID | A unique identifier for the request. |
| Errors | An array of error objects, if any, that were encountered during the activation process. |
| Code (errors) | An error code corresponding to the encountered issue. |
| Message (errors) | A message describing the cause of the error. |
| Warnings | An array of warnings (strings), if any, that were encountered during the activation process. |
| Result | An array containing the ID of the smart campaign. |
| ID (result) | The unique identifier of the smart campaign that was activated. |

Refer to the [Marketo documentation](https://developer.adobe.com/marketo-apis/api/asset/#tag/Smart-Campaigns/operation/activateSmartCampaignUsingPOST) to learn more about this action.

---
