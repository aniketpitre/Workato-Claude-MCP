---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/account-credentials-refresh-failed.md
description: >-
  The Account credentials refresh failed trigger in the RecipeOps connector
  fires when OAuth 2.0 or Multi-digest connections fail to refresh access
  credentials.
---

# RecipeOps - Account credentials refresh failed trigger

The **Account credentials refresh failed** trigger monitors only OAuth 2.0 and Multi-digest connections and creates a job if these connections fail to refresh their access credentials. This trigger doesn't monitor connections that use Basic, API key, or other static API credentials, as these types of connections lack a mechanism for refreshing API credentials.

## Input

This trigger doesn't require any input.

## Output

| Output field | Description |
| --- | --- |
| Connection ID | The ID of the connection that failed to refresh its access credentials. |
| Connection name | The name of the connection that failed to refresh its access credentials. |
| Application | The name of the application. |
| Initial connection time | The initial connection datetime. |
| Connection lost at | The datetime the connection was lost. |
| Connection lost reason | The reason the connection was lost. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)
