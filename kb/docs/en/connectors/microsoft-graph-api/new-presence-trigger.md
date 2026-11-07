---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/new-presence-trigger.md
description: The New presence trigger activates when there is a new presence change.
---

# Microsoft Graph API - New presence trigger

The **New presence** trigger activates when a new presence change occurs.

## Input

| Input field | Description |
| --- | --- |
| User IDs | Select the user IDs to subscribe to multiple users' presence events. Leave blank to select all the users from the list. |

## Output

| Output field | Description |
| --- | --- |
| OData type | Specifies the type of the resource in OData format. It indicates that the returned object is of type `microsoft.graph.presence`. |
| Odata id | Unique identifier for the OData resource. |
| ID | Unique identifier of the presence record associated with a specific user. |
| Availability | Represents the user's availability status. |
| Activity | Represents the specific presence activity of the user. |
