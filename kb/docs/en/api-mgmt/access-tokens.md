---
url: 'https://docs.workato.com/en/api-mgmt/access-tokens.md'
description: >-
  Learn how Workato access tokens authenticate API recipe clients, and compare
  Auth Token, OAuth 2.0, JWT, and OpenID Connect formats.
---

# Access tokens

Access tokens are strings that identify the client of an API recipe. The token value is a secret that is shared between a client and the Workato server. A token is passed to the API in an authorization header. The header must have a valid value for the call to succeed.

Workato supports five token formats:

- [Auth Token](/en/api-mgmt/auth-token)
- [OAuth 2.0](/en/api-mgmt/oauth2)
- [JSON Web Token (JWT)](/en/api-mgmt/jwt-token)
- [OpenID Connect](/en/api-mgmt/oidc)
- [OAuth 2.0 (Token Introspection)](/en/api-mgmt/oauth2-token-introspection)

## Access token comparison

The following table compares the supported token formats based on setup simplicity, reuse, and token lifecycle. Use this comparison to choose the method that fits your security model and integration requirements:

|  | Auth Token | OAuth 2.0 | OAuth 2.0 (Token Introspection) | JSON Web Token (JWT) | OpenID Connect |
| --- | --- | --- | --- | --- | --- |
| Simple to set up and use in API requests. | Yes | Yes | No | Yes | Yes |
| Represents a Workato access profile or API key. | Yes | Yes | Yes | Yes | Yes |
| Can be reused for multiple web applications. | Not recommended | Yes | Yes | Not recommended | Yes |
| Tokens with limited validity. | No | Yes | Yes | Optional | Yes |

Auth Token and JWT aren't recommended for reuse across multiple web applications. Assign a unique token to each application to maintain access isolation and reduce security risk.

> **SHORTER ACCESS TOKENS**
> 
> Workato issues shorter Auth Tokens, OAuth 2.0 client IDs and secrets, and OAuth 2.0 access tokens as of **October 20, 2026**. New tokens are 50 characters long instead of 64 and use URL-safe base64 encoding, which prevents them from breaking URL syntax. The shorter length doesn't change the level of security.
> 
> Existing Auth Tokens and OAuth 2.0 client credentials continue to work and require no action. Workato issues them in the new format only when you create or refresh them. OAuth 2.0 access tokens expire after one hour, so your integration receives a new-format access token the next time it requests one.
> 
> Update any rule in your integration that checks token length or format, such as one that expects exactly 64 characters or only hexadecimal characters. You can [create a new application](/en/api-mgmt/api-client-mgmt#create-a-new-application) alongside the existing one and move your integration to its Auth Token or client credentials. This lets you switch without interrupting live integrations.

---
