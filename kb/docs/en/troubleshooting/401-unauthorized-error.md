---
url: 'https://docs.workato.com/en/troubleshooting/401-unauthorized-error.md'
description: >-
  Learn why the 401 Unauthorized error occurs in Workato when credentials are
  rejected, and how to reconnect the app to resolve it.
---

# 401 Unauthorized

The **401 Unauthorized** error occurs when the external service rejects the authentication credentials provided in a request. This prevents the recipe from accessing the requested resource.

![Example of 401 Unauthorized error](/assets/401-unauthorized-error.DoYNdP4i.png)_Example of **401 Unauthorized** error_

## Why it happens

The following issues may trigger a **401 Unauthorized** error in Workato:

- The app connection uses outdated or invalid credentials.
- The external service revoked the credentials, such as after a password change or due to a security policy.
- The connection lacks the required authentication method, such as an OAuth token or API key.

You may encounter this error in both built-in app connections and custom HTTP requests.

## How to troubleshoot

Complete the following steps to resolve the error:

1. Go to the connection in your Workato account.
   
2. Disconnect the app connection.
   
3. Reconnect the app using valid and current credentials.
   
   > **CUSTOM OR HTTP CONNECTORS**
   > 
   > If you're using a custom connector or HTTP connector, confirm the request includes the correct authentication method and required headers, such as an API key or Bearer token.
   

Contact [Workato support](https://support.workato.com) if the issue persists.

---
