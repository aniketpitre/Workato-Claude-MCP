---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/relate-member-to-campaign.md
description: >-
  The Relate a member to a campaign action relates a lead or contact to a
  campaign in Zoho CRM.
---

# Zoho CRM - Relate a member to a campaign action

The **Relate a member to a campaign** action relates a lead or contact to a campaign in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Member ID | Enter the lead or contact ID. The action does nothing if the member is already a campaign member. |
| Campaign ID | Enter the unique identifier of the campaign. |
| Member type | Specify the type of member: `Leads` or `Contacts`. |
| Member status | Specify the status of the member in the campaign. |

## Output

| Output field | Description |
| --- | --- |
| Added member IDs | The list of member IDs that were added. |
| Updated member IDs | The list of member IDs that were updated. |
