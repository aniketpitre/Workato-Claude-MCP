---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/search-campaigns-batch.md
description: >-
  The Search campaigns batch action returns records that match the given search
  criteria.
---

# Zoho CRM - Search campaigns action (batch)

The **Search campaigns** batch action returns records that match the given search criteria.

- Search input must be at least 2 characters. Partial matching is used for all fields.
- Search supports up to 5 fields maximum.
- At least one search field is required.

## Input

| Input field | Description |
| --- | --- |
| Campaign name | Enter the name of the campaign to search. |

## Output

| Output field | Description |
| --- | --- |
| Campaigns | The list of campaigns matching the search criteria. |
| Campaign owner (Campaigns) | The user to whom the campaign is assigned. |
| Campaign ID (Campaigns) | The unique identifier of the campaign. |
| Campaign name (Campaigns) | The name of the campaign. |
| Type (Campaigns) | The type of the campaign. |
| Status (Campaigns) | The status of the campaign. |
| Start date (Campaigns) | The date on which the campaign starts. |
| End date (Campaigns) | The date on which the campaign ends. |
| Expected revenue (Campaigns) | The revenue expected after launching the campaign. |
| Actual cost (Campaigns) | The actual amount spent on the campaign. |
| Budgeted cost (Campaigns) | The planned amount to be spent on the campaign. |
| Expected response (Campaigns) | The campaign turnout percentage. |
| Number sent (Campaigns) | The number of leads or contacts who received details. |
| Description (Campaigns) | Additional details about the campaign. |
| Currency symbol (Campaigns) | The currency symbol for monetary values. |
| Process flow (Campaigns) | The process flow associated with the campaign. |
| Approved (Campaigns) | Indicates if the campaign has been approved. |
| Editable (Campaigns) | Indicates if the campaign record is editable. |
| Approval (Campaigns) | The approval details for the campaign. |
| Delegate (Approval) | Indicates if approval can be delegated. |
| Approve (Approval) | Indicates if the campaign can be approved. |
| Reject (Approval) | Indicates if the campaign can be rejected. |
| Resubmit (Approval) | Indicates if the campaign can be resubmitted. |
| SM owner ID (Campaigns) | The ID of the user who owns the campaign. |
| SM creator ID (Campaigns) | The ID of the user who created the campaign. |
| Created by (Campaigns) | The user who created the campaign. |
| Modified by (ID) (Campaigns) | The ID of the user who last modified the campaign. |
| Modified by (Campaigns) | The user who last modified the campaign. |
| Created time (Campaigns) | The timestamp when the campaign was created. |
| Modified time (Campaigns) | The timestamp when the campaign was modified. |
| Survey Department (Campaigns) | The department responsible for the survey. |
| Survey Type (Campaigns) | The type of survey associated with the campaign. |
| Survey (Campaigns) | The survey name or identifier. |
| Survey URL (Campaigns) | The URL for the survey. |
| Department ID (Campaigns) | The unique identifier for the department. |
