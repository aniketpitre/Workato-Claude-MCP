---
url: 'https://docs.workato.com/en/api-mgmt/unauthenticated-collections.md'
description: >-
  Allow an API proxy collection to accept unauthenticated requests so public
  endpoints, such as OIDC discovery documents, can be served without client
  credentials.
---

# Unauthenticated API collections

Configure an API proxy collection to accept unauthenticated requests so any caller can reach its endpoints without an application, key, or token. By default, every endpoint on the Workato API platform requires an authenticated client.

Use unauthenticated collections to serve endpoints that a standard protocol requires to be reachable without credentials. The most common case is an OpenID Connect (OIDC) discovery document, such as `/.well-known/openid-configuration`, which client applications fetch to auto-discover a provider's authorization, token, and user info endpoints and its signing keys (JWKS). Refer to [OpenID Connect](/en/api-mgmt/oidc) for more information about OIDC on the API platform.

## How unauthenticated access works

Unauthenticated access is a collection-level setting. When you enable it for an API proxy collection, every endpoint in that collection accepts requests without credentials, and Workato doesn't check for a client key or token. The setting applies to the whole collection, not to individual endpoints.

Clients and applications continue to exist for the collection, but they no longer restrict access while unauthenticated access is enabled. The client creation flow does not change. The setting persists when you deactivate and reactivate the API proxy.

> **UNAUTHENTICATED ACCESS**
> 
> Anyone on the public internet can call any endpoint in the collection without credentials when a collection accepts unauthenticated requests. Enable this setting only for collections that are safe to expose publicly, such as OIDC discovery documents.

## Allow unauthenticated requests for a collection

You configure unauthenticated access from the collection details panel of an API proxy collection.

> **PREREQUISITES**
> 
> Ensure you have the following before you begin:
> 
> - An [API proxy collection](/en/api-mgmt/api-collections/proxy-collection)
> - Admin access to the workspace

Complete the following steps to allow unauthenticated requests for an API proxy collection:

1. Go to **Platform > API platform > API collections** and select the API proxy collection you plan to make public.
   
2. Locate **Authentication required** in the collection details panel.
   
   ![Collection details panel](/assets/collection-panel-auth.XfaE7K1-.png)_Collection details panel_
   
3. Click **Allow unauthenticated requests**. A confirmation modal displays.
   
4. Review the **Allow unauthenticated requests?** confirmation.
   
   ![Allow unauthenticated requests](/assets/allow-unauth-requests.D0uqDwaN.png)_Allow unauthenticated requests_
   
   Click **Allow unauthenticated requests** to confirm, or **Cancel** to keep authentication in place.
   
5. The collection details panel updates to **Authentication not required** and confirms that all endpoints in the collection accept unauthenticated requests.
   
   ![Authentication not required](/assets/auth-not-required.VmjGEd9q.png)_Authentication not required_
   

### Deny unauthenticated requests

Complete the following steps to restore authentication for the collection:

1. Locate **Authentication not required** in the collection details panel and click **Deny unauthenticated requests**.
   
   ![Deny unauthenticated requests](/assets/deny-unauth-requests.Civ0jNdn.png)_Deny unauthenticated requests_
   
2. Workato restores authentication for the collection. The details panel returns to **Authentication required**, and clients must again provide credentials to call the collection.
   

## Client access for unauthenticated collections

When a collection accepts unauthenticated requests, the clients listed on the collection's **Clients** tab can't restrict access, because any caller can reach the endpoints without credentials.

On the **API collections** page, a collection that accepts unauthenticated requests displays an **Authentication not required** indicator on its card in place of the client access count.

## Call an unauthenticated endpoint

A consumer calls an endpoint in an unauthenticated collection through the collection's URL, with no `Authorization` header, key, or token. For example:

```shell
curl https://api.example.com/oidc/.well-known/openid-configuration
```

When the collection accepts unauthenticated requests and the proxy is active, Workato returns the response.

## Response caching

Response caching remains available for endpoints in an unauthenticated collection. Enable caching for each endpoint as usual. Refer to [API endpoint caching](/en/api-mgmt/api-caching) for more information.

## Limitations

Unauthenticated API collections have the following limitations:

- Unauthenticated access is available only for API proxy collections. API recipe and AI gateway collections are not supported.
- [API access policies](/en/api-mgmt/api-access-policies), including rate limits and request quotas, don't apply to unauthenticated collections.
- Allowed and blocked IP rules don't apply to unauthenticated collections.

---
