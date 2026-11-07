---
url: 'https://docs.workato.com/en/connectors/salesforce/custom-oauth.md'
description: >-
  Learn how to create a custom OAuth profile and external client app for
  Salesforce.
---

# Create a custom OAuth profile for Salesforce

This guide explains how to create a [custom OAuth profile](/en/custom-oauth-profiles) for Salesforce. The process includes the following steps:

1. [Create a custom OAuth profile in Workato](#create-workato-profile)
2. [Set up an external client app in Salesforce](#salesforce-external-app)
3. [Retrieve the client ID and secret](#retrieve-id-secret)
4. [Complete setup in Workato](#complete-setup)

> **SALESFORCE APPEXCHANGE SECURITY REQUIREMENTS**
> 
> Starting May 11, 2026, Salesforce requires AppExchange Partners to enable additional security settings on Connected Apps and External Client Apps. These settings include: PKCE extension, refresh token rotation (RTR), token TTL quotas, and IP allowlisting for token exchange.
> 
> No changes to your Workato configuration are required, but we recommend testing with a new custom OAuth profile in a non-production environment. Contact [Workato Support](https://support.workato.com) if you experience any issues. If your app requires an IP allowlist in Salesforce, refer to [Workato's IP addresses](/en/security/ip-allowlists#traffic-from-workato) for the values to add.
> 
> Salesforce may grant deadline extensions for these requirements on a case-by-case basis. Contact your Salesforce Partner Account Manager for details specific to your account and timeline.

## Create a custom OAuth profile in Workato

Complete the following steps to create a new custom OAuth profile:

1. Sign in to Workato.
   
2. Go to **Tools > Custom OAuth profiles**.
   
3. Click **\+ New custom profile**.
   
4. Select **Salesforce** from the **Application** drop-down menu.
   
   ![Select Salesforce](/assets/select-application.CEdHCz73.png)_Select Salesforce_
   
5. Enter a name for your custom OAuth profile in the **Name** field.
   
   ![Name your custom OAuth profile](/assets/name-profile.CHWA93aB.png)_Name your custom OAuth profile_
   
6. Click **Create new app**.
   

## Create an external client app in Salesforce

Complete the following steps to create an external client app in Salesforce. Refer to Salesforce's [Create an External Client App](https://help.salesforce.com/s/articleView?id=xcloud.create_a_local_external_client_app.htm&language=en_US&type=5) documentation for more information.

1. Open a new tab and sign in to your Salesforce account.
   
2. Go to **Setup > Apps > External Client Apps > External Client App Manager**.
   
3. Click **New External Client App**.
   
4. Enter a name in the **External Client App Name** field, such as `Workato`.
   
5. Enter a name in the **API Name** field that meets the following requirements:
   
   - Contains only underscores and alphanumeric characters.
   - Is unique.
   - Starts with a letter.
   - Doesn't include spaces.
   - Doesn't end with an underscore.
   - Doesn't contain consecutive underscores.
6. Enter the contact email address for your app in the **Contact Email** field.
   
7. Use the **Distribution State** drop-down menu to select either **Local** or **Packaged**.
   
8. Expand the **API (Enable OAuth Settings)** section and select the **Enable OAuth** checkbox.
   
9. Enter the following URL in the **Callback URL** field:
   
   ```plaintext
   https://www.workato.com/oauth/callback
   ```
   
10. Select your OAuth scopes in the **OAuth Scopes** field, then click the **Move selection to Selected OAuth Scopes** arrow to apply them.
    
    ![Configure scopes for your external client app](/assets/oauth-scopes.B-mGtuor.png)_Configure scopes for your external client app_
    
    > **SCOPES**
    > 
    > Select the scopes Workato requests in the **Requested permissions** field in the [OAuth 2.0 connection](/en/connectors/salesforce#oauth2-0-connection)'s advanced settings. Workato doesn't send a scope with the authorization request if you leave the field blank. Salesforce then grants the scopes in **Selected OAuth Scopes**. Add every requested scope to **Selected OAuth Scopes** because Salesforce grants access only to the scopes added there. Refer to [Requested scopes](/en/connectors/salesforce#oauth2-scopes) for the scopes Workato requests in addition to the scopes you select.
    > 
    > **Full access** doesn't include **Perform requests at any time (refresh\_token, offline\_access)**. Add this scope to **Selected OAuth Scopes** too, or Workato's refresh calls fail silently and the connection disconnects when the access token expires.
    
11. Configure the following settings:
    
    - In the **Flow Enablement** section, select only the **Enable Authorization Code and Credentials Flow** checkbox.
    - In the **Security** section, configure the following:
      - Select the **Require secret for Web Server Flow** and **Require secret for Refresh Token Flow** checkboxes. These settings are required for the connection to work.
      - Leave the **Issue JSON Web Token (JWT)-based access tokens for named users** checkbox unselected.
      - The following settings are generally optional, but may be required depending on your AppExchange partnership status with Salesforce:
        - **Require Proof Key for Code Exchange (PKCE) extension for Supported Authorization Flows**
        - **Enable Refresh Token Rotation**
        - **Quota Idle Refresh Token Time-to-Live (TTL) to 30 Days**. Test this setting in a non-production environment before enabling it broadly. This setting may cause connection instability in some configurations. If you experience issues after enabling it, disable it and contact [Workato Support](https://support.workato.com).
        - **Enforce Refresh Token IP Allowlist**. If you enable this setting, refer to [Workato's IP addresses](/en/security/ip-allowlists#traffic-from-workato) for the values to add.
    
    ![Configure the Flow Enablement and Security fields](/assets/flow-config.Bieu0uZg.png)_Configure the Flow Enablement and Security fields_
    
12. Click **Create** to create the external client app.
    

Refer to Salesforce's [Configure the External Client App OAuth Settings](https://help.salesforce.com/s/articleView?id=xcloud.configure_external_client_app_oauth_settings.htm&type=5) documentation for more information.

## Retrieve the client ID and secret

Complete the following steps to retrieve the client ID and client secret for your app:

1. Click the **Settings** tab for your external client app.
   
2. Expand the **OAuth Settings** section.
   
3. Click **Consumer Key and Secret**.
   
   ![Click Consumer Key and Secret](/assets/consumer-key-and-secret.D5BF6kne.png)_Click **Consumer Key and Secret**_
   
4. Enter your credentials and provide the one-time password (OTP) if prompted.
   
5. Copy the **Consumer Key** and **Consumer Secret**. These values are required to configure Workato to communicate with your app.
   
   ![Retrieve the consumer key and consumer secret](/assets/retrieve-consumer-key-and-secret.BPRxpSja.png)_Retrieve the consumer key and consumer secret_
   

## Complete setup in Workato

Complete the following steps to finish setting up your custom OAuth profile:

1. Return to the Workato tab.
   
2. Paste the consumer key from Salesforce into the **Client ID** field.
   
3. Paste the consumer secret from Salesforce into the **Client secret** field.
   
   ![Fill in the client ID and client secret fields](/assets/client-id-and-secret.DpSb5MXJ.png)_Fill in the client ID and client secret fields_
   
4. Click **Save**, then click **Done**.
   

You can now use this custom OAuth profile when [creating a new Salesforce connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato).

---
