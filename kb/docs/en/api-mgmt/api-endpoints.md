---
url: 'https://docs.workato.com/en/api-mgmt/api-endpoints.md'
description: >-
  Manage and expose recipe-based and proxy-based API endpoints with the Workato
  API platform, and organize them into API collections for consistent access.
---

# API endpoints

The [API Platform](https://www.workato.com/platform/api-management?utm_source=docs&utm_medium=referral&utm_campaign=api-management) enables you to manage and expose two types of API endpoints:

- Recipe-based endpoints
  
- [Recipe-based endpoints](/en/api-mgmt/api-recipes/) connect external systems with [API recipes](/en/api-mgmt/api-recipes/#api-recipes). API recipes are internal workflows composed of triggers and actions that automate tasks such as data retrieval, processing, and updates. Recipe-based endpoints securely expose API recipes to external applications, supporting complex business processes without requiring extensive DevOps resources.
  
- Proxy-based endpoints
  
- [Proxy-based endpoints](/en/api-mgmt/api-proxy-endpoints) securely expose your APIs through Workato’s API gateway. These API proxies can handle high-volume traffic—up to 10,000 requests per second—offering a scalable solution to centralize and secure external API interactions.
  

You can organize both types of endpoints into [API collections](/en/api-mgmt/api-collections) to group related APIs, maintain consistent configurations, and simplify access management.

> **ENDPOINT TYPES**
> 
> You can't mix endpoint types within a collection. API recipe collections can only contain recipe-based endpoints, and API proxy collections can only contain proxy-based endpoints.

## Setting up and managing API endpoints

To set up, manage, and test your API endpoints, refer to the following guides:

- [Configure a new endpoint](#configuring-a-new-api-endpoint): Choose either a [recipe-based](/en/api-mgmt/api-recipes/) or [proxy-based](/en/api-mgmt/api-proxy-endpoints) endpoint, depending on your requirements. Ensure you follow the configuration steps for the specific endpoint type.
- [Define path parameters with path templating](#path-templating): Add flexibility to endpoint URLs by using dynamic path parameters.
- [Follow endpoint path guidelines](#endpoint-path-guidelines): Ensure each endpoint’s path is unique, consistent, and easy to understand.
- [Activate or deactivate the endpoint](#activating-or-deactivating-an-endpoint): Control access to each endpoint by setting it to active or inactive.
- [Test the endpoint](/en/api-mgmt/testing-endpoints#test-recipe-endpoint): Verify functionality before going live. Recipe endpoints require an active recipe, and proxy endpoints can be tested immediately.
- [Enable caching](/en/api-mgmt/api-caching): For performance optimization, enable caching on GET requests to reduce duplicate calls and speed up response times.

## Configure a new endpoint

To create and configure an API endpoint, refer to the relevant guide for each endpoint type:

- [Configure a new API proxy endpoint](/en/api-mgmt/configure-proxy-endpoint)
- [Configure a new API recipe endpoint](/en/api-mgmt/configure-recipe-endpoint)

> **API ENDPOINT TYPES**
> 
> For more information about API proxy and recipe endpoints, as well as guidance on selecting the right option, refer to [API collection types](/en/api-mgmt/api-collections#collection-types).

### Schema validation

For recipe-based endpoints, you can enforce data integrity by validating incoming requests against a predefined schema. Learn more about [schema validation](/en/api-mgmt/configure-recipe-endpoint#schema-validation).

## Activating or deactivating an endpoint

Endpoints can be either **Active** or **Inactive**:

| State | Description |
| --- | --- |
| Active | Active endpoints are callable through API requests. For recipe-based endpoints, the associated recipe must be running before the endpoint can be set to **Active**. |
| Inactive | Inactive endpoints cannot be accessed remotely, and the API gateway rejects any calls. However, recipes associated with inactive endpoints continue to run in the background. |

You can control whether an endpoint is callable through API requests by clicking the **Activate endpoint** or **Deactivate endpoint** button on the **Details** tab of the endpoint configuration page. Newly created or added endpoints are **Inactive** by default.

![Activate API proxy endpoint in a collection](/assets/api-proxy-collection-activate-endpoint.Bn3od9fk.png)_Activate API proxy endpoint in a collection_

> **DELETING ENDPOINTS**
> 
> Deleting an endpoint removes it from the collection and makes it inaccessible to any clients previously granted access to it through the collection.

While both recipe and proxy endpoints have an active/inactive state, their activation requirements differ:

- Recipe endpoints must be activated before they can be tested or accessed through API requests.
- Proxy endpoints can be tested without activation but must be activated for external clients to call them.

## Path templating

Path templating enables you to specify resource identifiers in the URL path using path parameters. When an API request is made, the values in the path parameters are either:

- Passed to the associated datapills in an API recipe (for recipe-based endpoints).
- Forwarded to the target URL (for proxy-based endpoints).

> **FEATURE AVAILABILITY**
> 
> Path templating is only available for collections with [API prefixes](/en/api-mgmt/api-prefix) enabled.

When using recipe-based endpoints, we recommend that you first configure the datapills in the [New API request trigger](/en/api-mgmt/api-recipes/trigger-new-api-request), then configure the endpoint path parameters.

Use curly braces `{}` to mark parts of the URL as a path parameter. For example: `users/{salesforce_id}`

![URL path templating](/assets/url-path-templating.CHdw7D0O.png)_URL path templating_

## Endpoint path guidelines

Use the following guidelines when configuring proxy and recipe endpoint paths:

- Include one or more segments in an endpoint path, separated by a `/`.
  - For example, use `users/{user_id}` to specify a user's endpoint.
- Ensure each segment is either a static path (`users`) or a [parameter](#path-templating) (`{user_id}`).
- Use alphanumeric or `_` characters for path parameter names to match datapill naming conventions.
- Avoid using multiple parameters with the same name in an endpoint path.
- Enter new or updated endpoint paths with the intended casing, as they are case-sensitive and preserved exactly. For example, `/Path123/` remains `Path123/`.
- Ensure each endpoint has a unique method and path combination.
  - For example, do not create `/user/{id}` if `/user/{ID}` exists in the same collection, **unless their HTTP methods differ**.
  - Similarly, do not create `/user/{id}` if `/user/{user_id}` exists in the same collection, **unless their HTTP methods differ**.
    - Path matching is performed from left to right, with static segments taking priority over parameterized segments.

> **WARNING**
> 
> Changing an endpoint used by a recipe or API client may require you to update the corresponding recipe or script to prevent errors.

### Example

If the API endpoint requires a `salesforce_id`, you can use a path parameter to provide the Salesforce id (`5003000000D8cuI`).

```shell
curl -X PUT 'https://apim.workato.com/api-collection/users/5003000000D8cuI' \
    -d '{"Email": "Matt.Jones@example.com","displayName": "Matt Jones","BillingCity": "San Francisco"}'
```

The recipe trigger returns the following output:

```json
{
    "request": {
        "salesforce_id" : "5003000000D8cuI",
        "Email": "Matt.Jones@example.com",
        "displayName": "Matt Jones",
        "BillingCity": "San Francisco"
    },
    "Context": {+}
}
```

  

> **OVERLAPPING KEYS**
> 
> If the same namespace exists in the path parameter, query parameter, or request body, the path parameter value takes precedence.
> 
> When you send the following API request, the salesforce\_id datapill will take the value of the path parameter (`5003000000D8cuI`) instead of the value supplied in the request body (`068D00000000pgOIAQ`):
> 
> ```shell
> curl -X PUT 'https://apim.workato.com/api-collection/users/5003000000D8cuI' \
>      -d '{"salesforce_id" : "068D00000000pgOIAQ","Email": "Matt.Jones@example.com","displayName": "Matt Jones","BillingCity": "San Francisco"}'
> ```

---
