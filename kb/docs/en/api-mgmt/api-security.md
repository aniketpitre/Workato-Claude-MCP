---
url: 'https://docs.workato.com/en/api-mgmt/api-security.md'
description: >-
  Learn security best practices for Workato APIs, including protecting API
  tokens, refreshing tokens, and using IP allowlists.
---

# Security Best Practices for APIs

Workato API recipes are a powerful feature that allows access to Workato functionality from sources external to Workato. But, since recipes can perform operations on your business systems, it is important to avoid unauthorized access to them through APIs.

* * *

## Treat API tokens like a password

API tokens should be treated like a password. Tokens grant API access to anyone who possesses them.

As a best practice, don't distribute them to clients through insecure channels. Use a secure messaging system or a document system to which both the API owner and the intended client have access.

* * *

## Don't re-use the same API token

An API token identifies a client and enables monitoring requests in the API dashboard on a per-client basis. If multiple people have the same API token, there's no reliable way to determine who is making calls to your API.

* * *

## Periodically refresh API tokens

By periodically refreshing (or changing) API tokens, you can ensure compromise of an API token doesn't provide long-term access. Refreshing an API token is similar to the way passwords expire.

Alternatively, distribute a JWT token and set an expiration time. This will give the token a limited lifetime.

* * *

## Use IP allowlists

Adding IP addresses to the allowlist restricts the originating IP addresses that have API access. This can be done as part of a client's [application](/en/api-mgmt/api-client-mgmt#api-keys).

An allowlist is a best practice from a security perspective, but there are a few things to consider:

- **Some clients may not have a fixed IP address.** If a client connects from a home network, for example, their internet provider may assign a different IP for each session.
- **Some clients may connect from multiple IP addresses.** If a client is traveling, for example, they may not have the same IP that they would from their usual network.

In these cases, it may not be readily possible to add IP addresses to the allowlist.

* * *

## Consider using JWT tokens

Instead of distributing auth secrets directly, use a JWT token. A JWT token encapsulates the Auth Token secret instead of the secret itself. JWT tokens are signed, include the client identity and can have an expiration. Learn how to set up a [JWT token](/en/api-mgmt/jwt-token).

* * *

## Monitor user access to APIs

If a person should no longer have access to APIs, such as a terminated employee, ensure that person's client profile is disabled or deleted in Workato.

---
