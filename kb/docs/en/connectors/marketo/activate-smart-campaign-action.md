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
