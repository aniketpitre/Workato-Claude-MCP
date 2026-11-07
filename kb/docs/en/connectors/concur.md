---
url: 'https://docs.workato.com/en/connectors/concur.md'
description: >-
  Connect to SAP Concur to manage travel and expense reporting, invoice
  processing, and user provisioning.
---

# SAP Concur

[SAP Concur](https://www.concur.com/) is a cloud-based travel and expense management platform that helps businesses manage travel bookings, expense reporting, and invoice processing.

## API version

The SAP Concur connector uses the following SAP Concur APIs:

- [Expense Group Configurations v3](https://developer.concur.com/api-reference/expense/expense-report/expense-group-configurations.html)
- [Expenses v4](https://developer.concur.com/api-reference/expense/expense-report/v4.expenses.html)
- [Identity v4](https://developer.concur.com/api-reference/profile/v4.identity.html)
- [Image v1.0](https://developer.concur.com/api-reference/image/v1.image.html) and [Image v3](https://developer.concur.com/api-reference/image/v3.image.html)
- [Invoice v3](https://developer.concur.com/api-reference/invoice/v3.payment-request.html)
- [List v4](https://developer.concur.com/api-reference/common/lists/v4.list.html)
- [List Item v4](https://developer.concur.com/api-reference/common/list-item/v4.list-item.html)
- [Payment Batches v1.1](https://developer.concur.com/api-reference/expense/payment-batch/v1.payment-batches.html)
- [Reports v3](https://developer.concur.com/api-reference/expense/expense-report/v3.reports.html) and [Reports v4](https://developer.concur.com/api-reference/expense/expense-report/v4.reports.html)
- [Submit v1.1](https://developer.concur.com/api-reference/expense/expense-report/post-report-submission.html)
- [Travel Extension v4](https://developer.concur.com/api-reference/user-provisioning/travel/v4.travel-extension.html)
- [User Provisioning v4](https://developer.concur.com/api-reference/user-provisioning/v4.user-provisioning.html)
- [Vendor v3.1](https://developer.concur.com/api-reference/invoice/v3.1.vendor.html)

Refer to the [Required scopes by trigger and action](#scopes) section for details on how these APIs relate to specific triggers and actions.

## Connection setup

The SAP Concur connector supports the following OAuth 2.0 authentication types:

- [Refresh token grant](#refresh-token-grant)
- [Password grant](#password-grant)
- [Authorization code grant](#authorization-code-grant)

> **REQUIRED SCOPE**
> 
> You must add the `EXPRPT` scope when connecting to SAP Concur. SAP Concur returns a `Forbidden Request` error without this scope.

### Create an OAuth 2.0 application

All authentication methods require an OAuth 2.0 application in your SAP Concur instance. Complete the following steps to create a OAuth 2.0 application, or refer to the [OAuth 2.0 Application Management Tool](https://preview.developer.concur.com/api-reference/authentication/oauth2-app-mgmt-tool.html) documentation:

1. Sign in to your SAP Concur instance with administrator credentials.
   
2. Go to **Administration > Company > Authentication Admin**.
   
3. Select **OAuth 2.0 Application Management** from the menu.
   
4. Click **Create new app**.
   
5. Enter a descriptive name for your application in the **App Name** field, such as `Workato Integration`.
   
6. Enter a description for your application in the **App Description** field.
   
7. Select your environment in the **App Stage** field. Choose **Development**, **Test**, or **Production**.
   
8. Select your application type in the **Application Type** field. Choose **Web Services (WS) Client** or **Integration with Concur Solutions (ICS) Client**.
   
9. Select the grants your integration requires in the **Allowed Grants** field. Select `password` and `refresh_token` for password grant or refresh token grant authentication, or `authorization_code` for authorization code grant authentication.
   
10. Enter `https://www.workato.com/oauth/callback` in the **Redirect URIs** field for authorization code grant authentication. This field appears only when you select `authorization_code`.
    
11. Configure the allowed scopes for your integration. You must include `EXPRPT` at minimum. Refer to the [Required scopes by trigger and action](/en/connectors/concur#scopes) section to identify additional scopes required by the triggers and actions you plan to use.
    
    Alternatively, you can click **Enter Manually** and copy and paste the following scopes to enable full connector functionality:
    
    ```plaintext
    ATTEND
    CONFIG
    expense.report.read
    expense.report.readwrite
    EXPRPT
    identity.user.core.read
    identity.user.coreenterprise.writeonly
    identity.user.coresensitive.read
    identity.user.enterprise.read
    identity.user.externalID.writeonly
    identity.user.ids.read
    identity.user.sap.read
    IMAGE
    INVPMT
    INVVEN
    LIST
    openid
    spend.list.read
    spend.list.write
    spend.listitem.delete
    spend.listitem.read
    spend.listitem.write
    spend.user.general.read
    spend.user.general.writeonly
    travel.user.general.read
    travel.user.private.read
    user.provision.read
    user.provision.write
    user.read
    user.write
    ```
    
12. Click **Submit**.
    
13. Record your **Client ID** and **Client Secret** in a secure location. These values are required to establish the connection in Workato.
    
    > **SAVE YOUR CREDENTIALS**
    > 
    > The client secret is only displayed once. You must regenerate the client secret or create a new application if you lose it.
    

### Refresh token grant

Use the refresh token grant authentication method for production instances. Contact your Concur account manager to receive refresh token credentials.

#### Generate a company request token

A company request token is a temporary, one-time authentication password used by administrators to connect external apps to the SAP Concur.

Complete the following steps to generate a company request token:

1. Go to the SAP Concur admin panel, and click **Administration > Company > Authentication Admin**.
   
2. Select **Company Request Token** from the menu.
   
3. Enter your **App ID** (Client ID) from the OAuth application you created in the previous section.
   
4. Click **Submit**.
   
5. Record the following information displayed in the success dialog:
   
   - **Company UUID**: Your company's unique identifier.
   - **Company Request Token**: A temporary token that expires in 24 hours.
   
   > **TOKEN EXPIRATION**
   > 
   > The company request token expires after 24 hours. You must regenerate the token if you don't complete the next steps within 24 hours.
   
6. Click **OK** to close the dialog.
   

#### Obtain a refresh token

Complete the following steps to obtain a refresh token using your company request token:

1. Open an API client of your choice, such as Postman or cURL.
   
2. Create a POST request to the SAP Concur OAuth2 token resource using the endpoint that matches your SAP Concur environment:
   
   - **Production**: `https://us.api.concursolutions.com/oauth2/v0/token`
   - **Implementation (Test)**: `https://us-impl.api.concursolutions.com/oauth2/v0/token`
3. Configure the request body with the following parameters in `x-www-form-urlencoded` format:
   
   - **client\_id**: Your Client ID from the OAuth application
   - **client\_secret**: Your Client Secret from the OAuth application
   - **username**: Your Company UUID from the Company Request Token step
   - **password**: Your Company Request Token from the Company Request Token step
   - **grant\_type**: `password`
   - **credtype**: `authtoken`
   
   Example Postman configuration:
   
   ![Postman configuration for refresh token](/assets/postman-refresh-token.8IZpNlvK.png)_Postman configuration_
   
4. Send the request.
   
5. Record the **refresh\_token** value in a secure location. This value is required to establish the SAP Concur connection in Workato.
   

#### Connect to SAP Concur using refresh token grant

Complete the following steps to connect to SAP Concur using refresh token grant authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for `SAP Concur` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field. Give this connection a unique name that identifies which SAP Concur instance it's connected to.
   
   ![Connect to SAP Concur](/assets/refresh-token-grant.Dq-h7TsP.png)_Connect to SAP Concur_
   
4. Use the first **Location** drop-down menu to select the project or folder to store your connection.
   
5. Use the **Implementation instance** drop-down menu to select whether you're connecting to a Concur implementation server. Select **Yes** if connecting to an implementation server. Defaults to **No** for existing connections.
   
6. Use the **Authentication type** drop-down menu to select **Refresh token grant**.
   
7. Use the second **Location** drop-down menu to select the location of your Concur implementation server.
   
8. Enter the [client ID](#create-an-oauth-2-0-application) from your application in the **Client ID** field.
   
9. Enter the [client secret](#create-an-oauth-2-0-application) from your application in the **Client secret** field.
   
10. Enter the [refresh token](#obtain-a-refresh-token) from your application in the **Refresh token** field.
    
11. Click **Connect**.
    

### Password grant

Use the password grant authentication method for sandbox instances.

#### Connect to SAP Concur using password grant

Complete the following steps to connect to SAP Concur using password grant authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for `SAP Concur` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field. Give this connection a unique name that identifies which SAP Concur instance it's connected to.
   
   ![Connect to SAP Concur](/assets/password-grant.GbzcFq-k.png)_Connect to SAP Concur_
   
4. Use the first **Location** drop-down menu to select the project or folder to store your connection.
   
5. Use the **Implementation instance** drop-down menu to select whether you're connecting to a Concur implementation server. Select **Yes** if connecting to an implementation server. Defaults to **No** for existing connections.
   
6. Use the **Authentication type** drop-down menu to select **Password grant**.
   
7. Enter your SAP Concur **Username**.
   
8. Enter your SAP Concur **Password**.
   
9. Use the second **Location** drop-down menu to select the location of your Concur implementation server.
   
10. Enter the **Client ID** from your application.
    
11. Enter the **Client secret** from your application.
    
12. Click **Connect**.
    

### Authorization code grant

Use the authorization code grant authentication method to authenticate with SAP Concur using an interactive OAuth login flow.

Authorization code grant authentication is required if you plan to use [Verified User Access (VUA)](/en/agentic/agent-studio/verified-user-access). VUA isn't compatible with other grant types, including API keys, basic auth, and other OAuth 2.0 flows.

This option requires a [custom OAuth profile](#set-up-a-custom-oauth-profile) configured with your SAP Concur client credentials.

#### Set up a custom OAuth profile

Authorization code grant authentication requires a custom OAuth profile in Workato. The profile stores your SAP Concur client credentials and is required to complete the connection. Workato returns an error if you select authorization code grant without a custom OAuth profile, or if the profile is missing a client ID or client secret.

Complete the following steps to create a custom OAuth profile:

1. Go to **Tools > Custom OAuth profiles**.
   
2. Click **\+ New custom profile**.
   
3. Search for `SAP Concur` and select it as your app.
   
4. Enter a name for the profile.
   
5. Enter the **Client ID** and **Client secret** from the [OAuth application](#create-an-oauth-2-0-application) you created.
   
6. Click **Save**.
   

#### Minimum and default scopes

Ensure [your SAP Concur OAuth app](#create-an-oauth-2-0-application) has every scope you request in the connection settings. The connection fails with a `400 Bad Request` error if a requested scope isn't enabled in your OAuth app.

The minimum required scopes are `openid`, `user.read`, and `EXPRPT`. Ensure your OAuth app has these minimum scopes configured. Workato requests the following default scopes if you leave the **Scopes** field blank:

- `openid`
- `user.read`
- `user.write`
- `EXPRPT`
- `expense.report.read`
- `expense.report.readwrite`
- `LIST`
- `spend.list.read`
- `spend.list.write`
- `spend.listitem.read`
- `spend.listitem.write`
- `spend.listitem.delete`
- `IMAGE`
- `ATTEND`
- `CONFIG`
- `INVPMT`
- `INVVEN`
- `identity.user.core.read`
- `identity.user.coresensitive.read`
- `identity.user.enterprise.read`
- `identity.user.coreenterprise.writeonly`
- `identity.user.externalID.writeonly`
- `identity.user.ids.read`
- `user.provision.read`
- `user.provision.write`
- `spend.user.general.read`
- `spend.user.general.writeonly`
- `travel.user.general.read`

#### Connect to SAP Concur using authorization code grant

Complete the following steps to connect to SAP Concur using authorization code grant:

1. Click **Create > Connection** or press C twice.
   
2. Search for `SAP Concur` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to SAP Concur using authorization code grant](/assets/authorization-code-grant.BQA0Wm3b.png)_Connect to SAP Concur_
   
4. Use the first **Location** drop-down menu to select the project or folder to store your connection.
   
5. Use the **Connection type** drop-down menu to specify whether this is a cloud or on-prem connection.
   
6. Use the **Implementation instance** drop-down menu to specify whether you're connecting to a Concur implementation server. Select **Yes** if connecting to an implementation server. Defaults to **No**.
   
7. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
8. Use the second **Location** drop-down menu to select the location of your Concur implementation server.
   
9. Optional. Expand **Advanced settings** and use the **Scopes** drop-down menu to select OAuth 2.0 scopes. Refer to [Minimum and default scopes](#authorization-code-grant-scopes) for requirements.
   
10. Use the **Custom OAuth profile** drop-down menu to select the [custom OAuth profile](#set-up-a-custom-oauth-profile) configured with your SAP Concur client credentials.
    
11. Click **Connect**. You are redirected to SAP Concur to sign in and authorize access.
    

## Required scopes by trigger and action

The credentials you use to set up the SAP Concur connection must have access to certain scopes depending on the triggers and actions you plan to use.

> **REQUIRED SCOPE**
> 
> The `EXPRPT` scope is required for connection setup.

Each trigger and action in the connector uses a specific API version due to SAP Concur's granular versioning approach.

The following table lists:

- The scopes required for each trigger and action
- The API name and version associated with each trigger and action

Refer to the SAP Concur [API Reference](https://developer.concur.com/api-reference/) documentation for more information.

| Name | Scopes | API group | API name and version |
| --- | --- | --- | --- |
| New expense report trigger | EXPRPT | Expense | Reports v3 |
| New expense report submission trigger | EXPRPT | Expense | Reports v3 |
| New or updated expense report trigger | EXPRPT | Expense | Reports v3 |
| New or updated invoice trigger | INVPMT | Invoice | Invoice v3 |
| New or updated user trigger | identity.user.ids.read, identity.user.core.read, identity.user.coresensitive.read, identity.user.enterprise.read, identity.user.sap.read | User | Identity v4 |
| Create list item action | spend.listitem.write, LIST | Common | List Item v4 |
| Create user action | user.provision.write, identity.user.coreenterprise.writeonly, identity.user.externalID.writeonly, spend.user.general.writeonly | User | User Provisioning v4 |
| Create users action (batch) | user.provision.write, identity.user.coreenterprise.writeonly, identity.user.externalID.writeonly, spend.user.general.writeonly | User | User Provisioning v4 |
| Create vendors action (batch) | INVVEN | Invoice | Vendor v3.1 |
| Delete list item action | spend.listitem.delete | Common | List Item v4 |
| Get all attendee types action (batch) | CONFIG | Expense | Expense Group Configurations v3 |
| Get all expense group configurations action (batch) | CONFIG | Expense | Expense Group Configurations v3 |
| Get all expense types action (batch) | CONFIG | Expense | Expense Group Configurations v3 |
| Get all list item action (batch) | spend.list.read | Common | List Item v4 |
| Get all lists action | spend.list.read | Common | List v4 |
| Get all payment types action (batch) | CONFIG | Expense | Expense Group Configurations v3 |
| Get expense report details action | expense.report.read | Expense | Reports v4 |
| Get invoice details action | INVPMT | Invoice | Invoice v3 |
| Get itemizations of specific expense action | expense.report.read | Expense | Expenses v4 |
| Get user action | travel.user.general.read, travel.user.private.read, spend.user.general.read, user.provision.read | User | Travel Extension v4, User Provisioning v4 |
| Get user provisioning status details action | user.provision.read | User | User Provisioning v4 |
| Retrieve children of list item action | spend.listitem.read | Common | List Item v4 |
| Search expense reports action (batch) | EXPRPT | Expense | Reports v3 |
| Search users action (batch) | identity.user.ids.read, identity.user.core.read, identity.user.coresensitive.read, identity.user.enterprise.read, identity.user.sap.read | User | Identity v4 |
| Search vendors action (batch) | INVVEN | Invoice | Vendor v3.1 |
| Submit an expense report through a workflow action | EXPRPT | Expense | Submit v1.1 |
| Update user action | user.provision.write, identity.user.coreenterprise.writeonly, identity.user.externalID.writeonly, spend.user.general.writeonly | User | User Provisioning v4 |
| Update user action (batch) | user.provision.write, identity.user.coreenterprise.writeonly, identity.user.externalID.writeonly, spend.user.general.writeonly | User | User Provisioning v4 |
| Update vendors action (batch) | INVVEN | Invoice | Vendor v3.1 |
| Upload receipt image action | IMAGE | Receipt Image | Image v3 |
| Get entry image URL action | IMAGE | Receipt Image | Image v1.0 |
| Get expense report details action (deprecated) | expense.report.read | Expense | Expenses v4 |
| Get payment batch list action (deprecated) | PAYBAT | Expense | Payment Batches v1.1 |

---
