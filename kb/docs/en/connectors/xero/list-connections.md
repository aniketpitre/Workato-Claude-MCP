---
url: 'https://docs.workato.com/en/connectors/xero/list-connections.md'
description: >-
  The List connections action in the Xero connector lets you retrieve a list of
  connections from your connected Xero account.
---

# Xero - List connections action

The **List connections** action allows you to retrieve a list of connections from your connected Xero account.

![List accounts action](/assets/list-connections-action.C9EAggQt.png)_Xero - List connections action_

## Input

This action does not require any input.

## Output

| Output field | Description |
| --- | --- |
| Connection ID | The unique identifier for the connection between your application and a specific Xero organization. |
| Authentication event ID that connected this tenant | The ID of the event that authenticated or established the connection. |
| Tenant ID | The unique identifier for the tenant (organization or entity) in Xero that the connection is associated with. |
| Tenant type | The type of tenant, which generally refers to whether the tenant is an "ORGANISATION" or another entity within Xero. |
| Tenant name | The name of the Xero organization or tenant. |
| Created date UTC: | The timestamp (in UTC) when the connection to the Xero tenant was initially created. |
| Updated date UTC | The timestamp (in UTC) when the connection was last updated. |

---
