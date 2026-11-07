---
url: >-
  https://docs.workato.com/en/connectors/zendesk/get-organization-details-by-id-action.md
description: >-
  The Get organization details by ID action in the Zendesk connector lets you
  retrieve details about a specific organization found by ID.
---

# Zendesk - Get organization details by ID action

This action retrieves details about a specific organization that matches a search by organization ID. Only records in your Zendesk instance that matches the criteria will be returned.

![Get organization details by ID](/assets/get-organization-details-by-id.BH6Uw019.png)_Get organization details by ID_

## Input

| Input field | Description |
| --- | --- |
| Organization ID | The unique Zendesk ID of the organization. |

## Output

The output of this action contains the full set of columns from the selected organization. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the organization. This is automatically assigned when the organization is created. |
| Group ID | The unique Zendesk ID of the group of this organization. |
| Organization custom fields | Includes data of organization custom fields. |

Click here for a full list of [organization outputs](/en/connectors/zendesk/organization-fields#organization-output-fields).
