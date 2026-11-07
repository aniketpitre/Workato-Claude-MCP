---
url: >-
  https://docs.workato.com/en/connectors/zendesk/get-organization-by-external-id-action.md
description: >-
  The Get organizations by external IDs action in the Zendesk connector lets you
  retrieve organizations that match a search by external IDs.
---

# Zendesk - Get organizations by external IDs action (batch)

This action retrieves a list of organizations that matches a search by external IDs. Only records in your Zendesk instance that matches the criteria will be returned.

![Get organizations by external IDs action](/assets/get-organization-external-id.BK8UdyTt.png)_Get organizations by external IDs action_

## Input

| Input field | Description |
| --- | --- |
| External ID | The external ID of the organizations. You can query multiple external IDs with the `,` separator. |

## Output

The output of this action contains the full set of columns from the selected organizations. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the organization. This is automatically assigned when the organization is created. |
| Group ID | The unique Zendesk ID of the group of this organization. |
| Organization custom fields | Includes data of organization custom fields. |
| List size | The size of the list, corresponding to the number of organizations retrieved. |

Click here for a full list of [organization outputs](/en/connectors/zendesk/organization-fields#organization-output-fields).
