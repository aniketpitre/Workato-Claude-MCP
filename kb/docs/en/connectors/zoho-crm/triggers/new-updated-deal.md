---
url: 'https://docs.workato.com/en/connectors/zoho-crm/triggers/new-updated-deal.md'
description: >-
  The New/updated deal trigger checks for new or updated deals once every
  polling interval.
---

# Zoho CRM - New/updated deal trigger

The **New/updated deal** trigger checks for new or updated deals once every polling interval.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. You can't change this value after running or testing the recipe. |

## Output

| Output field | Description |
| --- | --- |
| Deal ID | The unique identifier of the deal. |
| SM owner ID | The ID of the user who owns the deal. |
| Deal owner | The user to whom the deal is assigned. |
| Account ID | The unique identifier of the related account. |
| Amount | The amount expected after closing the deal. |
| Contact ID | The unique identifier of the related contact. |
| Campaign ID | The unique identifier of the related campaign. |
| Overall sales duration | The total duration of the sales cycle. |
| SM creator ID | The ID of the user who created the deal. |
| Expected revenue | The calculated expected revenue. |
| Last activity time | The timestamp of the last activity on the deal. |
| Sales cycle duration | The duration of the sales cycle. |
| Created by | The user who created the deal. |
| Modified by ID | The ID of the user who last modified the deal. |
| Modified by | The user who last modified the deal. |
| Lead conversion time | The time taken to convert the lead. |
| Created time | The timestamp when the deal was created. |
| Modified time | The timestamp when the deal was modified. |
| Deal name | The name of the deal. |
| Closing date | The expected close date. |
| Account name | The name of the related account. |
| Stage | The sales stage of the deal. |
| Type | The type of deal. |
| Quantity | The quantity associated with the deal. |
| Probability | The probability of closing the deal. |
| Lead source | The lead source for the deal. |
| Campaign source | The campaign source for the deal. |
| Contact name | The name of the related contact. |
| Description | Additional details about the deal. |
| Next step | The next step of the sales process. |
| Currency symbol | The currency symbol for monetary values. |
| Process flow | The process flow associated with the deal. |
| Approved | Indicates if the deal has been approved. |
| Editable | Indicates if the deal record is editable. |
| Approval | The approval details for the deal. |
| Delegate (Approval) | Indicates if approval can be delegated. |
| Approve (Approval) | Indicates if the deal can be approved. |
| Reject (Approval) | Indicates if the deal can be rejected. |
| Resubmit (Approval) | Indicates if the deal can be resubmitted. |
| Prediction score | The predicted likelihood of closing the deal. |
| Followed | Indicates if the deal is being followed. |
| Followers | The list of users following the deal. |

---
