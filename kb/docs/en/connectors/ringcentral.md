---
url: 'https://docs.workato.com/en/connectors/ringcentral.md'
description: Learn how to connect to RingCentral on Workato.
---

# RingCentral

[RingCentral](https://www.ringcentral.com/) is a cloud-based communication and collaboration platform that provides voice, video, team messaging, and collaboration solutions for businesses.

## API version

The RingCentral connector uses [RingCentral API v1](https://developer.ringcentral.com/api-docs/latest/index.html).

## How to connect to RingCentral

Complete the following steps to connect to RingCentral:

1. Sign in to your Workato account.
   
2. Click **Create > Connection** or press C+C.
   
3. Select **RingCentral** on the **New connection** page.
   
4. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to RingCentral](/assets/connect.CXZBMG6Y.png)_Connect to RingCentral_
   
5. Use the **Location** drop-down menu to specify the project or folder where you plan to store your connection.
   
6. Optional. Expand **Advanced settings** and enter the **Client ID** and **Client secret** associated with your RingCentral app. Refer to the [Generate a client ID and secret](#generate-a-client-id-and-secret) section to learn how to obtain these values.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a profile to use for this connection. [Create a new profile](https://app.workato.com/custom_oauth_keys/new?provider=ringcentral).
   
8. Click **Connect**.
   
9. Sign in to your RingCentral account in the dialog that appears.
   
10. Click **Authorize** to grant Workato or your RingCentral OAuth app access to your account with the following permissions:
    
    - Control and manage phone calls in real-time
    - View and update extension information, including name, extension number, phone number, email, etc.
    - Send, and edit intra-company text messages
    - View user account information, e.g. name, business name, and contact info
    - View user call log records
    - View personal address book contacts
    - View message store data, including SMS, fax, voicemail, etc.
    - View user presence status
    - Perform two-legged ring out phone calls
    - Send and receive SMS/MMS messages
    - Manage and subscribe to webhook notifications
    
    ![Authorize Workato to access your RingCentral account](/assets/authorize-workato.CRjCFymO.png)_Authorize Workato to access your RingCentral account_
    

### Generate a client ID and secret

Complete the following steps to create a new RingCentral app, which generates a client ID and secret:

1. Sign in to the [RingCentral Developer Portal](https://developer.ringcentral.com/).
   
2. Click **Register App** to register a new application.
   
   ![Register a new RingCentral app](/assets/register-app.CVyGZhjT.png)_Register a new RingCentral app_
   
3. Select **REST API App** as the **App Type**.
   
4. Click **Next**.
   
5. Enter a name for your app in the **App Name** field. For example, `Workato`.
   
6. Enter a description for your app in the **App Description** field. The description must contain a minimum of 20 characters.
   
7. Select **No** in the **Do you intend to promote this app in the RingCentral App Gallery?** field.
   
8. Select **Server-side web app (most common)** in the **From what type of app will you be calling the API?** field.
   
9. Enter the Workato callback URI that corresponds to your data center in the **OAuth Redirect URI** field:
   
   - US Data Center: `https://www.workato.com/oauth/callback`
   - EU Data Center: `https://app.eu.workato.com/oauth/callback`
   - JP Data Center: `https://app.jp.workato.com/oauth/callback`
   - SG Data Center: `https://app.sg.workato.com/oauth/callback`
   - AU Data Center: `https://app.au.workato.com/oauth/callback`
   - IL Data Center: `https://app.il.workato.com/oauth/callback`
   - CN Data Center: `https://app.workatoapp.cn/oauth/callback`
   - KR Data Center: `https://app.kr.workato.com/oauth/callback`
   - UK Data Center: `https://app.uk.workato.com/oauth/callback`
   
   > **RINGCENTRAL SELF-SERVICE (WORKATO FREE, WORKATO PRO, OR DEVELOPER SANDBOX) ENVIRONMENT REMOVED**
   > 
   > RingCentral has deprecated its Self-service environment and replaced it with a new development environment. The `https://app.trial.workato.com/oauth/callback` URI is no longer supported.
   
10. Specify whether to enable refresh tokens in the **Issue refresh tokens?** field. When enabled, RingCentral can issue refresh tokens to extend session duration without requiring reauthentication.
    
11. Select the necessary OAuth 2.0 scopes for your application. The connection requires the following scopes:
    
    - **Call Control**
    - **Edit Extensions**
    - **Internal Messages**
    - **Read Accounts**
    - **Read Call Log**
    - **Read Contacts**
    - **Read Messages**
    - **Read Presence**
    - **Ring Out**
    - **SMS**
    - **Webhook Subscriptions**
12. Choose one of the following options in the **Who will be authorized to access your app?** field:
    
    - This app is public and will be callable via any RingCentral customer.
    - This app is private and will only be callable using credentials from the same RingCentral account.
13. Click **Create** to create the application. RingCentral generates a **Client ID** and **Client secret**.
    
14. Copy the **Client ID** and **Client secret**. Use these credentials when [connecting to RingCentral in Workato](#how-to-connect-to-ringcentral).

---
