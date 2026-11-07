---
url: 'https://docs.workato.com/en/connectors/xero/create-manual-journal.md'
description: >-
  The Create manual journal with line items action in the Xero connector lets
  you create a manual journal with multiple line items.
---

# Xero - Create manual journal with line items action

The **Create manual journal with line items** action allows you to create a manual journal with multiple line items in Xero.

![Create manual journal with line items action](/assets/create-journal-lines-action.B_Hza44E.png)_Xero - Create manual journal with line items action_

## Input

| Input field | Description |
| --- | --- |
| Narration | Enter the description or details of the journal. |
| Status | Specify the status of the journal. Choose `POSTED` for journals that are finalized and `DRAFT` for journals that are preliminary and may require further editing. |
| Date | Set the date for the journal entry. If left blank, it defaults to the current date. |
| Line amount types | Define the line amount type for tax purposes. If left blank, it defaults to `No Tax`. |
| Journal lines | Provide the details for each line in the journal. |
| Journal line source list | Input a list datapill that contains the journal line details. |
| Entry | Details of the individual entry in the journal line. |
| Account (entry) | Specify the account code for the entry. |
| Tax type (entry) | Select the tax type for the entry. |
| Line amount (entry) | Input the financial amount for the entry. |
| Description (entry) | Provide a description for the entry. |
| Opposite entry | Details for the opposing entry in the journal line. |
| Account (opposite entry) | Specify the account code for the opposite entry. |
| Tax type (opposite entry) | Select the tax type for the opposite entry. |
| Line amount (opposite entry) | Input the financial amount for the opposite entry. |
| Description (opposite entry) | Provide a description for the opposite entry. |

## Output

| Output field | Description |
| --- | --- |
| Manual journal ID | The unique identifier for the manual journal entry in Xero. |
| Narration | The description or details provided for the journal entry. |
| Line amount types | The type of line amounts entered, which indicates how taxes are applied. |
| Status | The status of the manual journal. |
| Has attachments | Indicates whether there are attachments linked to the journal entry. |
| Show on cash basis reports | Indicates if the journal entry appears on cash basis reports. |
| Date | The date the manual journal was recorded. |
| Updated date UTC | The UTC date and time the manual journal was last updated. |
| Journal lines | A collection of individual journal lines that make up the journal entry. |

---
