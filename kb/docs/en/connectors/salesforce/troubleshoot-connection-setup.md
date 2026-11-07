---
url: >-
  https://docs.workato.com/en/connectors/salesforce/troubleshoot-connection-setup.md
description: >-
  Use this guide to troubleshoot errors when you connect to the Salesforce
  connector in Workato.
---

# Troubleshoot Salesforce connection setup

Use this guide to troubleshoot errors when you connect to the Salesforce connector in Workato.

## Salesforce connection failed: Action failed due to server error

The `action failed due to server error` message displays when you click **Connect** to establish a Salesforce connection and it fails.

![action failed due to server error](/assets/sffailconnect.CL_57-mN.png)_Salesforce connection fails with an `action failed due to server error` message_

Complete the following steps to resolve this error and successfully establish a Salesforce connection:

1. Verify the domain. Use the correct Salesforce domain or custom domain:
   
   - Set the **Sandbox** field to Yes if your Salesforce domain ends with `.sandbox.my.salesforce.com`, or **No** if it ends with `.my.salesforce.com`.
2. If you're using a custom OAuth profile, confirm your external client app's OAuth and security settings match the configuration in [Create a custom OAuth profile for Salesforce](/en/connectors/salesforce/custom-oauth), including the **Flow Enablement** and **Security** settings.
   
3. Add Workato IPs to your allowlist. Refer to [IP allowlists](/en/security/ip-allowlists#traffic-from-workato) for more information.
   
4. Confirm that Salesforce doesn't block Workato. If the Workato connector is blocked, go to **Manage Apps** > **Connected Apps OAuth Usage**, then click **Unblock** next to the app name.
   
   ![Unblock Workato in SFDC](/assets/resolve.GOP1yHKb.png)_Unblock Workato in SFDC_
   

## Salesforce connection disconnects repeatedly

A connection that repeatedly shows **Connection lost** and requires reconnecting usually means Salesforce isn't returning a refresh token. A Refresh Token Policy or IP Relaxation setting can cause the same symptom.

![Connection lost banner on a Salesforce connection's detail page.](/assets/connection-lost.BQSzyd70.png)_Connection lost banner on a Salesforce connection_

Salesforce only issues a refresh token when your Salesforce app's OAuth policies explicitly grant the **Perform requests at any time** scope. **Full access** doesn't include this scope by default. Refer to [Token expiration](/en/connectors/salesforce#token-expiration) for how this works.

Add **Perform requests at any time (refresh\_token, offline\_access)** to your external client app's Selected OAuth Scopes if you're using a [custom OAuth profile](/en/connectors/salesforce/custom-oauth).

Complete the following steps for the default OAuth 2.0 connection:

1. Sign in to Salesforce and go to **Setup > Apps > App Manager**.
   
2. Open the Connected App named `Workato connector`. Salesforce creates it automatically, or an admin installs it, the first time your org connects. Refer to [OAuth restrictions](/en/connectors/salesforce#oauth-restrictions) if you don't see the Connected App.
   
3. Select **Manage**.
   
4. Check the **OAuth Policies > Application Permissions** list for the **Perform requests at any time** scope.
   

Check the following settings on the same app if disconnections continue:

- **Refresh Token Policy (Idle Expiration Time Limit Enforced)**: avoid **Immediately expire refresh token**, and set any idle-expiration window longer than how often your recipes actually use the connection.
- **IP Relaxation**: set to **Relax IP restrictions**, or [add Workato's IPs](/en/security/ip-allowlists#traffic-from-workato) to **Setup > Security > Network Access** or the integration user's **Login IP Ranges** instead if you need to keep **Enforce IP restrictions**. Workato connects from a rotating range of IPs, so an enforced policy without an allowlist can revoke the session in a way that looks like a disconnect.
- **Lock sessions to the IP address from which they originated** (**Setup > Security > Session Settings**) can cause the same symptom if set too strictly alongside IP Relaxation.

Refer to Salesforce's [Manage OAuth Access Policies for a Connected App](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_manage_oauth.htm&type=5) and [OAuth Tokens and Scopes](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_tokens_scopes.htm&type=5) for additional token expiration options and configuration steps.
