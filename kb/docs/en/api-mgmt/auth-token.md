---
url: 'https://docs.workato.com/en/api-mgmt/auth-token.md'
description: >-
  Learn how to retrieve and refresh an Auth token, the simplest way to
  authenticate an API request with the Workato API platform.
---

# Auth token

## Header

An Auth token is the simplest way to authenticate an API request with Workato.

How can I retrieve a new Auth token?

You can retrieve an Auth token when you [create a new API key](/en/api-mgmt/api-client-mgmt#create-a-new-application). You can only view this token once. If you lose the token, you will need to refresh and retrieve a new token.

1. Go to **Platform > API Platform > Clients** and select the client, then go to the **Applications** tab.
   
2. Click the **Refresh** button next to the API key you plan to retrieve an Auth token for. Refreshing your Auth token revokes access for clients using the current Auth token.
   
   ![Refresh the Auth token](/assets/refresh-auth-token.Bf7WGeQw.png)_Refresh the Auth token_
   
3. Save your Auth token in a secure place.
   

Configure a header with your Auth token. For example:

```shell
-H 'api-token: ed776fdfbf5003b4aa6bcaafea8f9003ffb6986454822ce7ebb3c1a8efc08348'
```

Workato reads this header value and recognizes that the request is from a verified API key when an API request is made.

## Basic authentication

You can authenticate the API request using the [basic auth scheme](https://datatracker.ietf.org/doc/html/rfc7617). Use `api-token` as the username and your token value as the password. For example, in curl, you can pass the following credentials with the `-u` option:

```shell
-u api-token:ed776fdfbf5003b4aa6bcaafea8f9003ffb6986454822ce7ebb3c1a8efc08348
```

This command automatically constructs the `Authorization` header in the following format:

```shell
-H 'Authorization: Basic <encoded api-token:token>'
```

---
