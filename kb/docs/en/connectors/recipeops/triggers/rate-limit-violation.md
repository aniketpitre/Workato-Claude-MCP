---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/rate-limit-violation.md
description: >-
  The API policy rate limit violation trigger in the RecipeOps connector fires
  when an access profile exceeds its assigned API rate limits.
---

# RecipeOps - API policy rate limit violation trigger

Actively monitors API usage across all access profiles and generates events when an access profile exceeds its assigned rate limits. It creates trigger events every five minutes for each unique access profile that goes beyond these quotas. To reduce noise, it generates only one event per access profile within this interval, even if rate limits are exceeded multiple times. For example, even if an access profile exceeds its rate limit three times within the same five-minute interval, this trigger only registers one trigger event.

Learn more about our [API access policies](/en/api-mgmt/api-access-policies#create-new-access-policy).

## Input

This trigger doesn't require any input.

## Output

| Field name | Description |
| --- | --- |
| Event message | `The rate limits for your API policy have been exceeded` |
| API policy ID | The unique identifier of the API policy. |
| API policy name | The name of the API policy. |
| Rate limit | The maximum number of API calls allowed within a specified short time interval. |
| Rate limit time interval | The time frame for the rate limit, such as a minute, hour, or day. |
| Client ID | The unique identifier of the client. |
| Client name | The name of the client associated with the event. |
| Access profile ID | The unique identifier of the access profile. |
| Access profile name | The name of the access profile. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)
