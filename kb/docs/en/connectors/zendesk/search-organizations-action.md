---
url: 'https://docs.workato.com/en/connectors/zendesk/search-organizations-action.md'
description: >-
  The Search organizations action in the Zendesk connector lets you retrieve a
  list of organizations that match your search criteria.
---

# Zendesk - Search organizations action (batch)

This action retrieves a list of organizations that matches your search criteria. Only records in your Zendesk instance that matches all the criteria will be returned.

![Search organizations action](/assets/search-organization-action.CnIytkWD.png)_Search organizations action_

## Input

| Input field | Description |
| --- | --- |
| Name | The name of the organization. |
| Tags | The tags applied to this organization. You can add multiple tags with the `,` separator. |
| Details | Details about the organization. |
| Notes | Notes about the organization. |
| Organization custom fields | Provide data for organization custom fields. |

## Output

The output of this action contains a list of organizations with their respective outputs. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | Unique Zendesk organization ID. This is automatically assigned when the organization is created. |
| Group ID | The unique Zendesk ID of the group of this organization. |
| Organization custom fields | Includes data of organization custom fields. |
| List size | The size of the list, corresponding to the number of organizations retrieved. |

Click here for a full list of [organization outputs](/en/connectors/zendesk/organization-fields#organization-output-fields).

---
