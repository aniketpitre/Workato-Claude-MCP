---
url: 'https://docs.workato.com/en/connectors/marketo/schedule-campaign-action.md'
description: >-
  The Schedule campaign or smart campaign action in the Marketo connector lets
  you schedule a campaign in a program to run at a time you specify.
---

# Marketo - Schedule campaign or smart campaign action

This action schedules a campaign or smart campaign to run at a given time in Marketo. Only campaigns or smart campaigns created in a program can be scheduled.

## Input

| Field | Description |
| --- | --- |
| Campaign ID / Campaign | Select the campaign from the list or provide the ID of the campaign to schedule. Only the first 300 campaigns are displayed in the list. If you do not find your campaign in the list, set the toggle to **Enter campaign ID**. |
| Run at | The date and time to run the campaign. |
| Clone to program name | The name of the resulting program. |
| Tokens | An array of tokens to be used in the campaign. |
| Tokens source list | Input a list datapill from which the tokens are derived. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Name | The name of the token. |
| Value | The value of the token. |

## Output

| Field | Description |
| --- | --- |
| Campaign ID | The identifier of the campaign. |

---
