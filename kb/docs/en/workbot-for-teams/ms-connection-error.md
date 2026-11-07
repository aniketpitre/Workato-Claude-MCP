---
url: 'https://docs.workato.com/en/workbot-for-teams/ms-connection-error.md'
description: >-
  Learn how to resolve connection errors when connecting Workbot for Microsoft
  Teams.
---

# Workbot for Microsoft Teams - Connection error

You may encounter the following error when you connect to Workbot for Microsoft Teams:

```text
Error on operation:team_info, exception: RestClient::InternalServerError
```

## Why it happens

This error typically occurs when the connected Microsoft account is a personal account that authenticates through `live.com`. These accounts support consumer services such as Outlook and OneDrive but aren't supported by Workato.

Workbot for Microsoft Teams requires a work or school account that authenticates through `login.microsoftonline.com`. The connection must also use the correct permissions and scopes.

This error can also occur due to the following:

- The connection uses invalid or excessive scopes.
- The Microsoft account lacks required roles.
- The Teams tenant blocks third-party app access.

## How to troubleshoot

Complete the following steps to resolve the issue:

1. Sign in with a Microsoft account that authenticates through `login.microsoftonline.com`. Workato doesn't support personal accounts that authenticate through `live.com`.
   
2. Open the connection settings and go to **Advanced settings**. Remove unnecessary API scopes and keep only those required for Workbot to access Microsoft Teams.
   
   ![Configure Microsoft Teams API scopes](/assets/configure-ms-scopes.CTt48wh9.png)_Configure Microsoft Teams API scopes_
   
   Excessive or unsupported scopes can cause the connection to fail if the Microsoft tenant blocks them or the app registration doesn't support them. Limiting scopes ensures the request matches what the account and app can authorize.
   
3. Ensure that the Microsoft account has one of the supported roles. Refer to the Workbot [Required roles](/en/workbot-for-teams/getting-started#required-roles) section for more information.
   
4. Reconnect the Workbot for Microsoft Teams account. Confirm that your Microsoft Teams tenant allows third-party app access if the error persists.

---
