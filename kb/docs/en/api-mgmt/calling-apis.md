---
url: 'https://docs.workato.com/en/api-mgmt/calling-apis.md'
description: >-
  Learn how to call API platform endpoints from other recipes or external tools
  using Auth token, OAuth 2.0, or JWT authorization headers.
---

# Calling APIs

Clients can call APIs exposed in the API platform console from recipes in other workspaces that don't own the API collection, or from third-party tools, programs, and scripts. To access any endpoints in the API collection, the API manager must provide the client with an Auth Token or JWT token.

The API platform supports raw content, which lets clients call endpoints with text-based requests such as XML or SOAP and receive custom responses from the exposed API recipes. This setup extends Workato's security features to external API calls. [Learn more](/en/api-mgmt/api-recipes/walkthrough).

## Authorization headers

If the API client specifies the **Auth Token** method of authentication, then the Auth Token value must be passed by the client as the value of the `api-token` header. If the authorization method is **OAuth2.0** or **JSON Web Token**, then the value of the encoded and signed token is passed in the `Authorization` header, using the `Bearer` scheme.

| Header | Authentication method | cURL example |
| --- | --- | --- |
| `api-token` | Auth token | `-H 'api-token: 24ea2bf52b42b7345b9'` |
| `Authorization` | OAuth 2.0 & JWT token | `-H 'Authorization: Bearer 12cb1a7d5233'` |

## Call an API endpoint from a recipe

An API endpoint that belongs to another user can be called from a recipe using the HTTP Connector. Select the **Send request** action of the connector. The following screen shows a typical configuration for this action (in this case a POST request):

![API Client Request](/assets/api-client-request.BlfXE0B3.png)_API Client Request_

Make sure that the type of request (POST, PUT, GET) matches the API that you are calling. Any required fields need to be specified in the body (for POST and PUT) or as query parameters in the URL (for GET).

Also, note that an `api-token` request header has been added. Its value should be set to the token that the API owner has supplied to you. (This assumes the **Auth Token** method of authentication).

> **WARNING**
> 
> Do **not** hard-code API tokens into input fields. Refer to the [security best practices](/en/recipes/recipe-security) guide for more information.

## Response codes

Using the recipe test feature, you can run the recipe a single time and have it generate a call to the API. If successful, the API will return a `200` status and the recipe execution will continue to completion. There are several possible errors that can occur. These are the common ones:

| Error code | Error message | Details |
| --- | --- | --- |
| 401 Unauthorized | `"access to this API has been disallowed"` | There is a problem with the API token, request configuration, or a violation of the access policy. You may also receive this error when the request URL is incorrect or the endpoint you called is not active. |
| 422 Processing error |  | There is an issue with the API recipe and the job failed. It could be due to a mismatch between the request syntax and the expected syntax written in the recipe. |
| 429 Too many requests | `"concurrency limit exceeded"` or `"rate/quota limit exceeded"` | The request exceeded either the concurrency limit or the rate/quota limit set by the access policy. |
| 500 Server error |  | The request parameters were missing or invalid for the API. |
| 504 Gateway timeout | `"recipe execution takes too long"` | The job took too long to respond. The default quota for API endpoints is 30 seconds, which is [customizable](/en/api-mgmt/configure-recipe-endpoint#step-1-create-the-endpoint). |

You may see [custom response codes](/en/api-mgmt/api-recipes/walkthrough) as defined in the API recipe in addition to the standard error codes in the preceding table.

### Response headers

Successful responses from an API-managed endpoint include the following header:

| Header | Description |
| --- | --- |
| `X-Workato-Recipe-Id` | Identifies the recipe that handled the request. |

### Status details for 401 and 404 errors

The **Status details** column in exported logs provides diagnostic messages for `401` and `404` errors to help API admins identify why a request failed.

The following table lists the extended diagnostic codes and their descriptions for common `401` and `404` errors:

| Status message | Code | Description |
| --- | --- | --- |
| Unrecognized token | 4011 | Token value is incorrect but structurally valid. |
| Missing token | 4012 | Token or header is missing or incorrectly named. |
| Invalid credentials | 4013 | Credentials are expired or otherwise invalid. This applies to credentials using JWT or OAuth 2.0. |
| Endpoint not found | 4014 | URL path doesn't match a valid endpoint. |
| Recipe is inactive | 4040 | Request targets an inactive API recipe. |

Workato treats some incorrect URL requests as `401` errors instead of `404` errors as part of its security approach.

---
