---
url: 'https://docs.workato.com/en/developing-connectors/http/troubleshoot-graph.md'
description: >-
  Fix Microsoft Graph API disconnects after one hour by adding the
  offline_access scope so the HTTP connection can refresh its token.
---

# Microsoft Graph API disconnects after one hour

The connection to Microsoft Graph API may fail after one hour when using the HTTP connector. This typically occurs when the OAuth access token expires and the connector can't refresh it automatically.

## Why it happens

Microsoft Graph uses OAuth 2.0 for authentication. By default, access tokens expire after one hour. The HTTP connection loses access after the token expires if it doesn't receive a refresh token to request a new one.

This issue occurs when the initial OAuth scope doesn't include `offline_access`. Without this scope, Microsoft doesn't return a refresh token, and Workato can't refresh the session after the access token expires.

## How to troubleshoot

Complete the following steps to prevent the HTTP connector from disconnecting after the access token expires:

1. Set the **OAuth 2.0 scope** field to include `offline_access` when configuring the HTTP connection. This allows the connection to receive a refresh token and automatically renew the access token after it expires.
   
   ![Error message with response headers](/assets/offline-access-http.DOIjsvPJ.png)_Include `offline_access` scope_
   
2. Reconnect the HTTP connection after you save the updated configuration.

---
