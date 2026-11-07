---
url: 'https://docs.workato.com/en/connectors/marketo/new-lead-trigger.md'
description: >-
  The New lead in list trigger in the Marketo connector picks up new leads added
  to a specified list each poll interval, processed as separate jobs.
---

# Marketo - New lead in list trigger

This trigger picks up new leads added to a specified list in your Marketo instance. It checks for new leads once every poll interval and Workato processes each lead as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| List | Select the list to monitor for new leads. |
| Output fields | Select the fields you plan to use in your recipe. All fields are returned if this field is left blank. However, leaving this field blank isn't recommended as it can result in timeout errors. |

Refer to the Marketo documentation for a [list of standard fields](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/assets/list-of-standard-fields) available through the API. This list includes common fields but may not cover all input fields specific to this action.

## Output

The output datatree contains information about the lead, including all the fields defined under **Output fields** in the trigger configuration. By default, Workato retrieves the **ID**.

| Field | Description |
| --- | --- |
| ID | The unique identifier of the lead record. |

---
