---
url: 'https://docs.workato.com/en/api-mgmt/api-governance.md'
description: >-
  Govern your APIs in Workato with access policies, RecipeOps monitoring
  triggers, and recipe version management for rate limits and quota control.
---

# API governance

Effective governance ensures that your APIs are secure, compliant, and managed according to best practices. This includes activity auditing, versioning, and lifecycle management. Implement granular access control and policies to manage usage and access. API access policies allow you to enforce rate limiting and quota management. These policies prevent overuse by a single client and ensure efficient and secure use of your APIs.

## API access policies

[API access policies](/en/api-mgmt/api-access-policies) enable control over the client's usage of APIs.

This helps prevent the overuse of an API by a single client, which could result in degraded performance for the community of API users. While an access policy is optional, if you do not create and associate an access policy with a client, then there are no API usage quotas on the client.

## RecipeOps

[RecipeOps](/en/connectors/recipeops) connectors enable you to build recipes to monitor and manage active recipes.

- [Concurrency threshold exceeded](/en/connectors/recipeops/triggers/concurrency-exceeded).
  
  Monitors API requests across your workspace and triggers when requests exceed 80% of your concurrency quota. Additional trigger events are created for each 5% increment, up to the workspace quota. This trigger is limited to one event per threshold every five minutes to reduce noise. Subsequent requests for the same threshold within a five-minute window will not result in a job.
  
- [API policy quota violation trigger](/en/connectors/recipeops/triggers/api-policy-violation)
  
  This trigger monitors API usage for the workspace. A trigger event occurs each time an access profile exceeds a policy quota threshold. For policies with longer quota intervals, duplicate events occur if the same threshold is exceeded every 30 days.
  
- [API policy rate limit violation trigger](/en/connectors/recipeops/triggers/rate-limit-violation)
  
  Actively monitors API usage across all access profiles and generates events when an access profile exceeds its assigned rate limits. It creates trigger events every five minutes for each unique access profile that goes beyond these quotas. To reduce noise, it generates only one event per access profile within this interval, even if rate limits are exceeded multiple times. For example, even if an access profile exceeds its rate limit three times within the same five-minute interval, this trigger only registers one trigger event.
  
- [Recipe version management](/en/recipes/version-management#version-management) allows for API development versioning.
  
  Every time a recipe is saved, a version of the recipe is created. Previous versions of a recipe can be restored at any time. Recipe versions can be viewed in the **Versions** tab and are denoted by their version number.

---
