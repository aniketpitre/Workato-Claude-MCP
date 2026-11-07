---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/account-disconnected.md
description: >-
  The Account disconnected trigger in the RecipeOps connector monitors selected
  connections and fires when those connections are disconnected.
---

# RecipeOps - Account disconnected trigger

This monitors selected connections and triggers when they are disconnected.

* * *

## Input

| Field | Description |
| --- | --- |
| **Apps to monitor** | Select app connections to monitor for disconnections. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Connection ID** | The ID of the connection. |
| **Name** | The display name of the connection. |
| **Application** | The type of the connection. For example: **PostgreSQL** |
| **Authorization error** | If an authorization error occurred, this will contain the error message. |
| **Authorized at** | The time the connection was last authorized. |
| **Disconnected by user** | Details about the user who disconnected the connection. This field has some additional sub-fields:
| Field | Description |
| --- | --- |
| **User ID** | The workspace ID where this connection was located. |
| **User name** | The user's name. |
| **User email** | The user's email address. |

 |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)
