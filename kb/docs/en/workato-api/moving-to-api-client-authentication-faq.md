---
url: >-
  https://docs.workato.com/en/workato-api/moving-to-api-client-authentication-faq.md
description: >-
  Learn how to migrate from deprecated legacy API keys to Developer API client
  authentication using Authorization Bearer headers.
---

# Legacy API key deprecation

Workato moved from legacy API key authentication to API client authentication on January 11, 2023. During this transition, legacy API keys were automatically moved to an API client named "Migrated API client" to maintain functionality.

**As of July 14, 2025, legacy API keys are fully deprecated.** API requests authenticated through legacy API keys are rejected. Email notifications were sent to affected users on April 14, 2025, with a second batch sent in July for those still using legacy API keys. From October 14, 2025 onwards, legacy API key functionality will be completely removed for all users.

> **ACTION REQUIRED**
> 
> You must migrate to API client authentication immediately. All API requests must use **Authorization: Bearer headers** instead of **x-user-token** and **x-user-email** headers.

## Does this affect me?

This affects you if you're currently using legacy API key authentication with:

- `x-user-token` and `x-user-email` headers in API requests
- API key and email in query parameters
- The "Migrated API client" in your workspace

## Your legacy API key location

Your legacy API key was moved to [**Workspace admin > API clients**](https://app.workato.com/members/api/clients) as "Migrated API client" with **Admin** permissions. The client token is your original API key.

Workspaces with environments enabled automatically had separate clients created for each environment: `Migrated API client - {Environment name}`.

## Migrate to API client authentication

Complete the following steps to migrate from legacy API key authentication to API client authentication:

1. Create a new API client following the [API client configuration guide](/en/workato-api/api-clients).
   
2. Update your applications to use the new API token with `Authorization: Bearer` headers.
   
3. Test your integration to ensure it works with the new authentication method.
   
4. Delete the "Migrated API client" that uses your legacy API key.
   

### Authentication format change

**Legacy format (deprecated):**

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/users/me \
     -H 'x-user-token: <legacy_api_key>' \
     -H 'x-user-email: <user_email>'
```

</api-code>

**New format (required):**

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/users/me \
     -H 'Authorization: Bearer <api_client_token>'
```

</api-code>

  

> **DELETING THE LEGACY API CLIENT**
> 
> Deleting your "Migrated API client" immediately revokes access for all applications using legacy authentication. Only delete this client after completing your migration.
