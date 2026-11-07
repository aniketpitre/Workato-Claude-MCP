---
url: 'https://docs.workato.com/en/api-mgmt/oauth2-token-introspection.md'
description: >-
  Set up OAuth 2.0 token introspection on an API client to validate access
  tokens issued by an external identity provider for each request.
---

# OAuth 2.0 Token Introspection authentication

Workato allows you to authenticate using the [OAuth 2.0 Token Introspection standard](https://datatracker.ietf.org/doc/html/rfc7662). This method enables you to validate access tokens issued by external authorization servers and ensures that only authorized clients can access your APIs.

Workato sends a token introspection request to the Identity Provider (IdP) to validate access tokens for each incoming API request.

> **DYNAMIC CLIENT REGISTRATION**
> 
> You can use a DCR provider to reuse your token introspection configuration across multiple API clients. Refer to [Dynamic client registration](/en/api-mgmt/api-dynamic-client) for more information.

## Set up OAuth 2.0 Token Introspection

Complete the following steps to configure an API client that uses OAuth 2.0 Token Introspection authentication:

1. [Create a new API client](/en/api-mgmt/api-client-mgmt#create-new-client).
   
2. Select **OAuth 2.0 Token introspection** as the authentication method.
   
3. Select or create an HTTP connection to your Identity Provider (IdP). Workato supports HTTP connections with no-auth, query, basic, header, or OAuth 2.0 authentication.
   
4. Provide the **Endpoint path** for the introspection endpoint, such as `/oauth2/introspect`. Workato appends this path to the connection's base URL. The **URL preview** displays the fully constructed endpoint.
   
   ![Set introspection endpoint](/assets/set-intro-endpoint.DybHgeXw.png)_Set introspection endpoint_
   

After you create the API client, the client details page displays the selected authentication method, the associated HTTP connection, and the configured token introspection endpoint URL.

![Client details page](/assets/client-details-intro.Dw3QnWrq.png)_Client details page_

## Validate token introspection responses

Workato sends a token validation request to the configured token introspection endpoint when an API call uses OAuth 2.0 Token Introspection.

The token must include a claim that maps to an API client in Workato to validate the request. You must configure this claim in your Identity Provider (IdP).

Complete the following steps to configure the token and map it to an API client:

1. [Create a new API key](/en/api-mgmt/api-client-mgmt#create-a-new-application) in Workato to represent the client.
   
2. Configure your IdP to include this key as a claim in the issued token. Workato uses this claim to identify and match the token to the correct API client.
   

Workato uses the claim value to identify the matching API client and only accepts the token if it is active. If the introspection response indicates the token is inactive or fails to meet the required format, Workato rejects the request with a **401 Unauthorized** error.

## Use token introspection data in APIs

Workato exposes introspection response data in API recipes and API proxies. You can access fields from both the response headers and body in the **Introspection response** section of the API request output.

Use these datapills in downstream steps in API recipes, in request and response transformations in API proxies, or in custom authorization logic.

---
