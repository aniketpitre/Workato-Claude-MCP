---
url: 'https://docs.workato.com/en/connectors/zoho-crm/actions/search-deals-batch.md'
description: >-
  The Search deals batch action returns records that match the given search
  criteria.
---

# Zoho CRM - Search deals action (batch)

The **Search deals** batch action returns records that match the given search criteria.

- Search input must be at least 2 characters. Partial matching is used for all fields.
- Search supports up to 5 fields maximum.
- At least one search field is required.

## Input

| Input field | Description |
| --- | --- |
| Deal name | Enter the name of the deal to search. |
| Closing date | Enter the expected close date to search. |
| Account name | Enter the account name to search. |
| Stage | Enter the sales stage to search. |
| Type | Enter the type of deal to search. |
| Quantity | Enter the quantity to search. |
| Probability | Enter the probability to search. |
| Lead source | Enter the lead source to search. |
| Campaign source | Enter the campaign source to search. |
| Contact name | Enter the contact name to search. |
| Description | Enter description text to search. |
| Next step | Enter the next step of the sales process. |

## Output

| Output field | Description |
| --- | --- |
| Potentials | The list of deals matching the search criteria. |
| Deal ID (Potentials) | The unique identifier of the deal. |
| SM owner ID (Potentials) | The ID of the user who owns the deal. |
| Deal owner (Potentials) | The user to whom the deal is assigned. |
| Account ID (Potentials) | The unique identifier of the related account. |
| Amount (Potentials) | The amount expected after closing the deal. |
| Contact ID (Potentials) | The unique identifier of the related contact. |
| Campaign ID (Potentials) | The unique identifier of the related campaign. |
| Overall sales duration (Potentials) | The total duration of the sales cycle. |
| SM creator ID (Potentials) | The ID of the user who created the deal. |
| Expected revenue (Potentials) | The calculated expected revenue. |
| Last activity time (Potentials) | The timestamp of the last activity on the deal. |
| Sales cycle duration (Potentials) | The duration of the sales cycle. |
| Created by (Potentials) | The user who created the deal. |
| Modified by ID (Potentials) | The ID of the user who last modified the deal. |
| Modified by (Potentials) | The user who last modified the deal. |
| Lead conversion time (Potentials) | The time taken to convert the lead. |
| Created time (Potentials) | The timestamp when the deal was created. |
| Modified time (Potentials) | The timestamp when the deal was modified. |
| Deal name (Potentials) | The name of the deal. |
| Closing date (Potentials) | The expected close date. |
| Account name (Potentials) | The name of the related account. |
| Stage (Potentials) | The sales stage of the deal. |
| Type (Potentials) | The type of deal. |
| Quantity (Potentials) | The quantity associated with the deal. |
| Probability (Potentials) | The probability of closing the deal. |
| Lead source (Potentials) | The lead source for the deal. |
| Campaign source (Potentials) | The campaign source for the deal. |
| Contact name (Potentials) | The name of the related contact. |
| Description (Potentials) | Additional details about the deal. |
| Next step (Potentials) | The next step of the sales process. |
| Currency symbol (Potentials) | The currency symbol for monetary values. |
| Process flow (Potentials) | The process flow associated with the deal. |
| Approved (Potentials) | Indicates if the deal has been approved. |
| Editable (Potentials) | Indicates if the deal record is editable. |
| Approval (Potentials) | The approval details for the deal. |
| Delegate (Approval) | Indicates if approval can be delegated. |
| Approve (Approval) | Indicates if the deal can be approved. |
| Reject (Approval) | Indicates if the deal can be rejected. |
| Resubmit (Approval) | Indicates if the deal can be resubmitted. |
| Prediction score (Potentials) | The predicted likelihood of closing the deal. |
| Followed (Potentials) | Indicates if the deal is being followed. |
| Followers (Potentials) | The list of users following the deal. |

---
