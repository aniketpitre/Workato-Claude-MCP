---
url: 'https://docs.workato.com/en/connectors/marketo/trigger-campaign-action.md'
description: >-
  The Trigger campaign or smart campaign action in the Marketo connector lets
  you run a campaign for specific leads, with optional tokens passed in.
---

# Marketo - Trigger campaign or smart campaign for specific leads action

This action triggers a campaign or smart campaign for specific leads in Marketo.

## Input

| Field | Description |
| --- | --- |
| Campaign / Campaign ID | Select or provide the ID of the campaign to trigger. Only the first 300 campaigns are displayed in the list. If you do not find your campaign in the list, set the toggle to **Enter campaign ID**. |
| Leads | Expand to configure the array of lead IDs to trigger the campaign for. |
| Leads source list (leads) | Input a list datapill from which leads are derived. Learn more about [list input](/en/features/list-management#list-batch-action). |
| ID (leads) | Provide the ID of the lead to trigger the campaign for. |
| Tokens | Expand to configure the array of tokens to be used in the campaign. |
| Tokens source list (tokens) | Input a list datapill from which tokens are derived. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Name (tokens) | Provide the name of the token. |
| Value (tokens) | Provide the value of the token. |

## Output

| Field | Description |
| --- | --- |
| Campaign ID | The ID of the campaign. |

---
