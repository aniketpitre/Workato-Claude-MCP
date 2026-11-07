---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/api-request-timeout.md
description: >-
  The API request timeout trigger in the RecipeOps connector fires when an API
  request to any workspace endpoint exceeds its configured timeout limit.
---

# RecipeOps - API request timeout trigger

The **API request timeout** trigger monitors the API request runtime for all endpoints in the workspace. The trigger activates when an API request exceeds the timeout limit of N seconds.

## Input

This trigger doesn't require user input.

## Output

| Output field | Description |
| --- | --- |
| API collection ID | Unique identifier of the API collection containing the timed-out endpoint. |
| API endpoint ID | Unique identifier of the specific endpoint that timed out. |
| API endpoint name | The name of the endpoint that exceeded the timeout limit. |
| Endpoint timeout limit (seconds) | The configured timeout threshold that was exceeded. |
