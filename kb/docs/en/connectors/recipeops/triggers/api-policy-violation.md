---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/api-policy-violation.md
description: >-
  The API policy quota violation trigger in the RecipeOps connector fires when
  an access profile exceeds a policy quota threshold of 80, 90, or 100 percent.
---

# RecipeOps - API policy quota violation trigger

This trigger monitors API usage for the workspace. A trigger event occurs each time an access profile exceeds a policy quota threshold. For policies with longer quota intervals, duplicate events occur if the same threshold is exceeded every 30 days.

Learn more about our [API access policies](/en/api-mgmt/api-access-policies#create-new-access-policy).

## Trigger behavior

For each workspace, this trigger captures instances when a unique access profile exceeds the following policy request thresholds:

- 80% of quota
- 90% of quota
- 100% of quota

> **RECIPEOPS BEHAVIOR**
> 
> The 30-day reference only affects policies with a quota interval longer than 30 days. For example, with a policy of 1,000 requests and a 90-day interval, the system triggers an event if you reach 800 requests (80% threshold) in the first month. If there are no new requests in the following month and the usage still stands at 800 requests (80%), a second event triggers. For longer quota intervals, every 30 days, a trigger event is created when hitting the same threshold.

## Input

This trigger doesn't require any input.

## Output

| Field name | Description |
| --- | --- |
| Event message | `Your API policy has reached X% of its usage quota.` |
| API policy ID | The unique identifier of the API policy. |
| API policy name | The name of the API policy. |
| Usage limit | The total number of API calls that can be made within a specific longer time period, typically 30 days. |
| Limit time interval | The duration of the time period for the usage quota, such as 30 days. |
| Client ID | The unique identifier of the client. |
| Client name | The name of the client associated with the event. |
| Access profile ID | The unique identifier of the access profile. |
| Access profile name | The name of the access profile. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)
