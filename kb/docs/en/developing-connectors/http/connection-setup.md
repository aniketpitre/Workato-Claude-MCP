---
url: 'https://docs.workato.com/en/developing-connectors/http/connection-setup.md'
description: >-
  Create an HTTP connection in Workato using auth types like basic, header,
  query params, OAuth2, and AWS to enable HTTP triggers and actions.
---

# Create an HTTP connection

You must set up your connection to the app you plan to use before you can configure HTTP [triggers](/en/developing-connectors/http/building-http-trigger) and [actions](/en/developing-connectors/http/building-http-action).

The steps required to create an HTTP connection in Workato vary based on the authentication type you plan to use. The HTTP connector supports the following authentication types:

- [None](#authentication-type-none)
- [Basic](#authentication-type-basic)
- [Header auth](#authentication-type-header-auth)
- [Query params](#authentication-type-query-params)
- [Custom](#authentication-type-custom)
- [OAuth2 (authorization code grant)](#authentication-type-oauth-2-0-authorization-code-grant)
- [OAuth2 (client credentials grant)](#authentication-type-oauth-2-0-client-credentials)
- [AWS access key auth](#authentication-type-aws-key-auth)
- [AWS IAM role auth](#authentication-type-aws-iam-role-auth)
- [Azure OAuth 2 (authorization code grant)](#azure-oauth2-authorization-code-grant-authentication-type)
- [Azure OAuth 2 (client credentials grant)](#azure-oauth2-client-credentials-grant-authentication-type)

## None authentication type

The None authentication type enables you to create a connection without providing authentication details. Use this authentication type when you plan to receive a webhook trigger from an app. Workato generates a URL to direct your webhooks to, and retrieves information from the webhook payload.

Complete the following steps to set up an HTTP connection with the None authentication type:

1. Provide a **Connection name** that identifies your HTTP instance.
   
   ![HTTP connector authentication type: None](/assets/none-authentication.jLHIHRrY.png)_HTTP connector authentication type: None_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select the connection type you plan to use.
   
4. Use the **Authentication type** drop-down menu to select **None**.
   
5. Use the **Endpoint has case-sensitive headers?** drop-down to set the case sensitivity for your connection.
   
   > **ASYNC MODE LIMITATION**
   > 
   > The **Endpoint has case-sensitive headers?** field has no effect when the **Wait for response** field is set to **Yes** (async mode) in the [HTTP action](/en/developing-connectors/http/building-http-action). Configure this option only when **Wait for response** is set to **No**.
   
6. Provide your base URL in the **Base URL** field. Recipes can't override this setting.
   
7. Use the **Use custom TLS/SSL certificate settings** drop-down menu to determine your certificate settings.
   
8. Click **Connect**.
   

## Basic authentication type

The Basic authentication type requires your username and password. As an alternative to your username and password, you can use an API key or API token retrieved from your account settings. This is a common authentication flow encoded with Base64 in transit over SSL.

1. Provide a **Connection name** that identifies your HTTP instance.
   
   ![HTTP connector authentication type: Basic](/assets/basic-authentication.BVB5H54c.png)_HTTP connector authentication type: Basic_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select the connection type you plan to use.
   
4. Use the **Authentication type** drop-down menu to select **Basic**.
   
5. Provide your user authentication name in the **Basic auth user** field.
   
6. Provide your user authentication password in the **Basic auth password** field.
   
7. Use the **Endpoint has case-sensitive headers?** drop-down menu to set the case sensitivity for your connection.
   
   > **ASYNC MODE LIMITATION**
   > 
   > The **Endpoint has case-sensitive headers?** field has no effect when the **Wait for response** field is set to **Yes** (async mode) in the [HTTP action](/en/developing-connectors/http/building-http-action). Configure this option only when **Wait for response** is set to **No**.
   
8. Provide your base URL in the **Base URL** field. Recipes can't override this setting.
   
9. Use the **Use custom TLS/SSL certificate settings** drop-down menu to determine your certificate settings.
   
10. Click **Connect**.
    

## Header auth authentication type

The Header auth authentication type enables you to customize the headers sent in a request. This is useful if your app requires additional headers beyond the standard username and password or API key. You can also use this authentication type if you have a generated token.

Complete the following steps to create an HTTP connection with the **Header auth** authentication type:

1. Provide a **Connection name** that identifies your HTTP instance.
   
   ![HTTP connector authentication type: Header auth](/assets/header-auth-authentication.ATtQ0TZf.png)_HTTP connector authentication type: Header authorization_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select the connection type you plan to use.
   
4. Use the **Authentication type** drop-down menu to select **Header auth**.
   
5. Optional. Expand **Header authorization** to add custom auth headers.
   
6. Use the **Endpoint has case-sensitive headers?** drop-down menu to set the case sensitivity for your connection.
   
   > **ASYNC MODE LIMITATION**
   > 
   > The **Endpoint has case-sensitive headers?** field has no effect when the **Wait for response** field is set to **Yes** (async mode) in the [HTTP action](/en/developing-connectors/http/building-http-action). Configure this option only when **Wait for response** is set to **No**.
   
7. Provide your base URL in the **Base URL** field. Recipes can't override this setting.
   
8. Use the **Use custom TLS/SSL certificate settings** drop-down menu to determine your certificate settings.
   
9. Click **Connect**.
   

## Query params authentication type

Use the Query params authentication type when you plan to use applications that require a validated API key as a parameter.

1. Provide a **Connection name** that identifies your HTTP instance.
   
   ![HTTP connector authentication type: Query params](/assets/query-params-authentication.CQf7bHLM.png)_HTTP connector authentication type: Query params_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select the connection type you plan to use.
   
4. Use the **Authentication type** drop-down menu to select **Query params**.
   
5. Use the **Endpoint has case-sensitive headers?** drop-down menu to set the case sensitivity for your connection.
   
   > **ASYNC MODE LIMITATION**
   > 
   > The **Endpoint has case-sensitive headers?** field has no effect when the **Wait for response** field is set to **Yes** (async mode) in the [HTTP action](/en/developing-connectors/http/building-http-action). Configure this option only when **Wait for response** is set to **No**.
   
6. Optional. Expand **Url parameters** to add URL parameters.
   
7. Provide your base URL in the **Base URL** field. Recipes can't override this setting.
   
8. Use the **Use custom TLS/SSL certificate settings** drop-down menu to determine your certificate settings.
   
9. Click **Connect**.
   

## Custom authentication type

The Custom authentication type enables you to use a tailored combination of input fields to satisfy custom authentication requirements.

1. Provide a **Connection name** that identifies your HTTP instance.
   
   ![Custom http connector](/assets/custom-authentication.6Rv2Hhh2.png)_HTTP connector authentication type: Custom_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select the connection type you plan to use.
   
4. Use the **Authentication type** drop-down menu to select **Custom**.
   
5. Optional. Provide your user authentication name in the **Basic auth user** field.
   
6. Optional. Provide your user authentication password in the **Basic auth password** field.
   
7. Expand **Header authorization** to add custom auth headers.
   
8. Use the **Endpoint has case-sensitive headers?** drop-down menu to set the case sensitivity for your connection.
   
   > **ASYNC MODE LIMITATION**
   > 
   > The **Endpoint has case-sensitive headers?** field has no effect when the **Wait for response** field is set to **Yes** (async mode) in the [HTTP action](/en/developing-connectors/http/building-http-action). Configure this option only when **Wait for response** is set to **No**.
   
9. Expand **Url parameters** to add URL parameters.
   
10. Provide your base URL in the **Base URL** field. Recipes can't override this setting.
    
11. Use the **Use custom TLS/SSL certificate settings** drop-down menu to determine your certificate settings.
    
12. Click **Connect**.
    

## On-prem NTLM authentication type

Use the NT LAN Manager (NTLM) authentication type if you have a configured Workato [on-prem agent](/en/on-prem) and the application you plan to use requires NTLM authentication.

Complete the following steps to set up your HTTP connection with NTLM authentication:

1. Provide a **Connection name** that identifies your HTTP instance.
   
   ![Custom http connector](/assets/ntlm-authentication.CEwv5YDi.png)_HTTP connector authentication type: On-prem NTLM_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select the connection type you plan to use.
   
4. Use the **Authentication type** drop-down menu to select **On-prem NTLM**.
   
5. Skip the **Endpoint has case-sensitive headers?** field. This option sets the case sensitivity for your connection. However, it has no effect for on-prem connections.
   
6. Provide your NTLM authentication domain or workstation name in the **NTLM authentication** field.
   
7. Provide your NTLM authentication username in the **Username** field.
   
8. Provide your NTLM authentication password in the **Password** field.
   
9. Optional. Expand **Optional properties** to configure additional profile properties.
   
10. Click **Connect**.
    

The following profile properties are supported:

| Property name | Description |
| --- | --- |
| NTLM authentication | NTLM authentication domain and workstation name. |
| Username | Username for NTLM authentication. |
| Password | Password for NTLM authentication. |
| Base URL | The base URL for NTLM resources. |
| Connections per route | **Optional**. Sets the number of connections per route/host (must be a positive number, default 5). |
| Maximum connections | **Optional**. Sets the maximum number of connections (must be a positive number, default 10). |
| Timeout | **Optional** The timeout in milliseconds used when requesting a connection (must be a positive number, default 10000). |
| Connection request timeout | **Optional** The timeout in milliseconds until a connection is established (must be a positive number, default 10000). |
| Socket timeout | **Optional** The socket timeout in milliseconds, which is the timeout for waiting for data or, put differently, a maximum period inactivity between two consecutive data packets (must be a positive number, default 10000). |
| Verify host | **Optional**. Specifies whether to enable verification of the host name for SSL/TLS connections (default true). |
| Trust all | **Optional**. Specifies whether trust all certificates for SSL/TLS connections (default false). |

Refer to the following list for supported HTTP methods for NTLM connections:

- `GET`
- `POST`
- `PUT`
- `PATCH`
- `DELETE`
- `HEAD`

Refer to the [connection profiles documentation](/en/on-prem/agents/connection/profile#ntlm-profile) if your on-prem group connections use `config.yml`.

## OAuth 2.0 authorization code grant authentication type

The OAuth 2.0 authorization code grant authentication type enables you to provide third parties with access to your apps without disclosing your username and password. Confidential and public clients use this authentication type to exchange an authorization code for an access token. Workato redirects you to your app to enter your login credentials when you use this authentication type. This enables Workato to act on your behalf when making API requests.

Complete the following steps to set up your HTTP connection with OAuth 2.0 authorization code grant authentication:

1. Provide a **Connection name** that identifies your HTTP instance.
   
   ![HTTP (OAuth2 auth code grant) connector's connection fields](/assets/oauth-code-grant-authentication.C4eiLNL2.png)_HTTP (OAuth2 authorization code grant) connector's connection fields_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select the connection type you plan to use.
   
4. Use the **Authentication type** drop-down menu to select **OAuth 2 (authorization code grant)**.
   
5. Use the **Endpoint has case-sensitive headers?** drop-down menu to set the case sensitivity for your connection.
   
   > **ASYNC MODE LIMITATION**
   > 
   > The **Endpoint has case-sensitive headers?** field has no effect when the **Wait for response** field is set to **Yes** (async mode) in the [HTTP action](/en/developing-connectors/http/building-http-action). Configure this option only when **Wait for response** is set to **No**.
   
6. Provide your authorization URL in the **OAuth2 authorization URL** field.
   
7. Provide your token in the **OAuth2 token URL** field. This auth token is used to verify that Workato has permission to access your app.
   
8. Provide your client ID in the **OAuth2 client ID** field. The client ID identifies you as the user who’s sending the API requests.
   
9. Use the **How does the API require credentials to be sent to request a token?** drop-down menu to determine whether to send the client ID and secret in the token request body or as a base64 encoded string in the header.
   
10. Provide your base URL in the **Base URL** field. Recipes can't override this setting.
    
11. Use the **Use custom TLS/SSL certificate settings** drop-down menu to determine your certificate settings.
    
12. Optional. Expand **Advanced settings** to configure OAuth2 scopes and token settings.
    
13. Click **Connect**.
    

## OAuth 2.0 client credentials grant authentication type

Use the OAuth 2.0 client credentials grant authentication type if you plan to enable the client to request an access token using only client credentials. This authentication type is usually used when the client is requesting access to the protected resources under its control or for machine-to-machine authentication where a specific user’s permission to access data is not required. The client credentials grant type can only be used by confidential clients.

Complete the following steps to set up your HTTP connection with OAuth2 client credentials grant authentication:

1. Provide a **Connection name** that identifies your HTTP instance.
   
   ![HTTP (OAuth2 client credentials grant) connector's connection fields](/assets/oauth-client-credentials-authentication.Dy_Pk_KP.png)_HTTP (OAuth2 client credentials grant) connector's connection fields_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select the connection type you plan to use.
   
4. Use the **Authentication type** drop-down menu to select **OAuth 2 (client credentials grant)**.
   
5. Use the **Endpoint has case-sensitive headers?** drop-down menu to set the case sensitivity for your connection.
   
   > **ASYNC MODE LIMITATION**
   > 
   > The **Endpoint has case-sensitive headers?** field has no effect when the **Wait for response** field is set to **Yes** (async mode) in the [HTTP action](/en/developing-connectors/http/building-http-action). Configure this option only when **Wait for response** is set to **No**.
   
6. Provide your OAuth2 token URL in the **OAuth2 token URL** field.
   
7. Provide your client ID in the **OAuth2 client ID** field.
   
8. Provide your client secret in the **OAuth2 client secret** field.
   
9. Use the **How does the API require credentials to be sent to request a token?** drop-down menu to determine whether to send the client ID and secret in the token request body or as a base64 encoded string in the header.
   
10. Provide your base URL in the **Base URL** field. Recipes can't override this setting.
    
11. Use the **Use custom TLS/SSL certificate settings** drop-down menu to determine your certificate settings.
    
12. Optional. Expand **Advanced settings** to configure OAuth2 scopes.
    
13. Click **Connect**.
    

OAuth2 client credentials grant example

#### Connect to Eventbrite with OAuth 2.0 client credentials grant

Go to the app's documentation page to obtain your authorization URL and the access token URL. You must append additional parameters to the URL as specified by the app. For example, Eventbrite requires the following format for a post request:

```
https://www.eventbrite.com/oauth/authorize?response_type=code&client_id=YOUR_CLIENT_KEY`
```

![Eventbrite OAuth 2.0 authentication page](/assets/eventbrite-authentication.CS42SO4b.png)_Eventbrite OAuth 2.0 authentication page_

The following information is required to enable Workato to handle the client key:

Eventbrite authorization URL:

```
https://www.eventbrite.com/oauth/authorize?response_type=code
```

Eventbrite access token URL:

```
https://www.eventbrite.com/oauth/token
```

You must have a client ID and client secret to connect to your Eventbrite account successfully. You must register an app with Eventbrite to obtain these credentials.

Complete the following steps to obtain your credentials:

1. Log in to Eventbrite and navigate to **Account Settings > App Management**.
   
   ![Eventbrite's App Management screen](/assets/eventbrite-app-management.DeyvrOEv.png)_Eventbrite's app management screen_
   
2. Locate your client ID (also called key) in the **App Management** page.
   
3. Expand the **Show Client Secret and OAuth Token** section to retrieve the client secret.
   
4. Navigate to the **App Extension** section to input the callback URL: `https://www.workato.com/oauth/callback`
   

## AWS access key auth authentication type

AWS Access key authentication enables you use access keys you have created as either a root user or an IAM user in AWS. You can assign a maximum of two access keys per user (root user or IAM user). A disabled key can't be used, but it does count toward your quota of two access keys. When you delete an access key, it is permanently removed from the app but can be replaced with a new access key. Refer to the [AWS documentation](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#programmatic-access) for more information.

> **AWS IAM AUTHENTICATION RECOMMENDED**
> 
> We recommend that you use AWS IAM authentication instead of access key authentication.

Complete the following steps to set up your HTTP connection with AWS access key authentication:

1. Provide a **Connection name** that identifies your HTTP instance.
   
   ![HTTP (AWS access key auth) connector's connection fields](/assets/aws-access-key-authentication.BgwqkpTV.png)_HTTP (AWS Access key auth)_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select the connection type you plan to use.
   
4. Use the **Authentication type** drop-down menu to select **AWS access key auth**.
   
5. Provide your AWS service name in the **AWS name** field.
   
6. Provide your account region in the **Region** field. Region is typically provided in the account URL. For example, if your account URL is `https://eu-west-1.console.s3.amazon.com`, your region is `eu-west-1`.
   
7. Provide your AWS access key ID in the **AWS access key ID** field. Go to your AWS account and click **My Security Credentials > Users** to find the access key ID.
   
8. Provide your secret access key in the **Secret access key** field. Go to your AWS account and click **My Security Credentials > Users** to find your secret access key.
   
9. Use the **Endpoint has case-sensitive headers?** drop-down menu to set the case sensitivity for your connection.
   
   > **ASYNC MODE LIMITATION**
   > 
   > The **Endpoint has case-sensitive headers?** field has no effect when the **Wait for response** field is set to **Yes** (async mode) in the [HTTP action](/en/developing-connectors/http/building-http-action). Configure this option only when **Wait for response** is set to **No**.
   
10. Provide your base URL in the **Base URL** field. Recipes can't override this setting.
    
11. Click **Connect**.
    

## AWS IAM role auth authentication type

AWS IAM role authentication enables you to provide a dedicated role in your AWS instance for Workato to use. By provisioning a dedicated IAM profile, the owner of the AWS instance can grant Workato access to AWS resources without sharing AWS security credentials. It also helps to maintain permission boundaries, including controlled access to specific AWS services and actions that are permitted by a third-party application, such as Workato.

We recommend that you only grant required permissions, and avoid using AllAccess policies whenever possible.

> **AWS IAM AUTHENTICATION RECOMMENDED**
> 
> We generally recommend that you use AWS IAM authentication instead of access key authentication.

Complete the following steps to set up your HTTP connection with AWS IAM role authentication:

1. Provide a **Connection name** that identifies your HTTP instance.
   
   ![HTTP (AWS IAM) connector's connection fields](/assets/aws-iam-role-authentication.DYPjy0KJ.png)_HTTP (AWS IAM role auth) connector's connection fields_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select the connection type you plan to use.
   
4. Use the **Authentication type** drop-down menu to select **AWS IAM role auth**.
   
5. Provide your AWS service name in the **AWS name** field.
   
6. Provide your account region in the **Region** field. For example, if your account URL is `https://eu-west-1.console.s3.amazon.com`, your region is `eu-west-1`.
   
7. Provide your IAM role ARN in the **IAM role ARN** field. Refer to the [How to retrieve IAM role ARN](/en/developing-connectors/http/connection-setup#authentication-type-aws-iam-role-auth) section for more information.
   
8. Use the **Endpoint has case-sensitive headers?** drop-down menu to set the case sensitivity for your connection.
   
   > **ASYNC MODE LIMITATION**
   > 
   > The **Endpoint has case-sensitive headers?** field has no effect when the **Wait for response** field is set to **Yes** (async mode) in the [HTTP action](/en/developing-connectors/http/building-http-action). Configure this option only when **Wait for response** is set to **No**.
   
9. Provide your base URL in the **Base URL** field. Recipes can't override this setting.
   
10. Click **Connect**.
    

### How to retrieve IAM role ARN

Use the following steps to retrieve the **Role ARN** required for the connection setup. Remember to use the Workato generated external ID found on the connection page.

1. Go to IAM and select **Roles** > **Create role**.
   
   ![AWS IAM authentication page - create role](/assets/create-new-iam-role.CFxiz0jB.png)
   
2. Select **Another AWS account** and input Workato's Account ID.
   
3. Select **Require external ID** and provide the Workato generated **External ID**.Every Workato user has a unique **External id**, for example, `workato_iam_external_id_77630`. You can find this value in the **IAM role ARN** section of the [connection setup](#authentication-type-aws-iam-role-auth).
   
   ![AWS IAM authentication page - entity type - Another AWS account](/assets/select-trusted-entity.C9aV4iGZ.png)
   
   If you require more granular control over how your HTTP connector is used in Workato, you can configure the connection at the project level by changing the scope of the external ID, [learn more](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws)
   
4. Attach permission policies to this role when prompted. This step enables you to provide fine-grained permission controls for Workato. The policies that you attach to this role should be as narrow as possible.
   
5. Select an appropriate tag for the IAM role if you are using object tagging.
   
6. Provide the IAM Role with an appropriate name and description. Workato recommends that you avoid using a non-guessable resource-id in the URN and that you don't include the external ID.
   
   ![Review role](/assets/review-role.Ca7P2F3y.png)
   
   The IAM Role is created.
   
   ![AWS Role summary page](/assets/role-summary-page.pMfl0nA1.png)
   

## Azure OAuth2 authorization code grant authentication type

The Azure OAuth2 authorization code grant authentication type enables you to provide third parties with access to your Azure apps without having to disclose your username and password. Confidential and public clients use this authentication type to exchange an authorization code for an access token.

Complete the following steps to set up your HTTP connection with Azure OAuth2 authorization code grant authentication:

1. Provide a **Connection name** that identifies your HTTP instance.
   
   ![Azure OAuth2 code grant authentication](/assets/azure-oauth-code-grant-authentication.UuG2E7uj.png)_Azure OAuth2 code grant authentication_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select the connection type you plan to use.
   
4. Use the **Authentication type** drop-down menu to select **Azure OAuth 2 (authorization code grant)**.
   
5. Provide your tenant ID in the **Azure Tenant ID** field. If you have an Azure subscription, enter your Tenant ID. Otherwise, use common.
   
6. Use the **Endpoint has case-sensitive headers?** drop-down menu to set the case sensitivity for your connection.
   
   > **ASYNC MODE LIMITATION**
   > 
   > The **Endpoint has case-sensitive headers?** field has no effect when the **Wait for response** field is set to **Yes** (async mode) in the [HTTP action](/en/developing-connectors/http/building-http-action). Configure this option only when **Wait for response** is set to **No**.
   
7. Provide your client ID in the **OAuth2 client ID** field.
   
8. Provide your client secret in the **OAuth2 client secret** field.
   
9. Use the **Azure endpoint version** to select the version of the Azure endpoints to use. Default is 2.0.
   
10. Provide your base URL in the **Base URL** field. Recipes can't override this setting.
    
11. Optional. Expand **Advanced settings** to configure OAuth2 scopes.
    
12. Click **Sign in with Microsoft**.
    

## Azure OAuth2 client credentials grant authentication type

You can use the Azure OAuth 2.0 client credentials grant authentication type if you plan to enable the client to request an access token using only client credentials. This authentication type is usually used when the client is requesting access to the protected resources under its control or for machine-to-machine authentication where a specific user’s permission to access data is not required. The client credentials grant type can only be used by confidential clients.

Complete the following steps to set up your HTTP connection with Azure OAuth2 client credentials grant authentication:

1. Provide a **Connection name** that identifies your HTTP instance.
   
   ![Azure OAuth2 client credentials](/assets/azure-oauth-client-credentials-authentication.Cn90WJtv.png)_Azure OAuth2 client credentials authentication_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select the connection type you plan to use.
   
4. Use the **Authentication type** drop-down menu to select **Azure OAuth 2 (client credentials grant)**.
   
5. Provide your tenant ID in the **Azure Tenant ID** field. If you have an Azure subscription, enter your Tenant ID. Otherwise, use common.
   
6. Use the **Endpoint has case-sensitive headers?** drop-down to set the case sensitivity for your connection.
   
   > **ASYNC MODE LIMITATION**
   > 
   > The **Endpoint has case-sensitive headers?** field has no effect when the **Wait for response** field is set to **Yes** (async mode) in the [HTTP action](/en/developing-connectors/http/building-http-action). Configure this option only when **Wait for response** is set to **No**.
   
7. Provide your client ID in the **OAuth2 client ID** field.
   
8. Provide your client secret in the **OAuth2 client secret** field.
   
9. Use the **Azure endpoint version** to select the version of the Azure endpoints to use. Default is 2.0.
   
10. Provide your base URL in the **Base URL** field. Recipes can't override this setting.
    
11. Optional. Expand **Advanced settings** to configure OAuth2 scopes.
    
12. Click **Sign in with Microsoft**.
    

## More resources

- [Build an HTTP trigger](/en/developing-connectors/http/building-http-trigger)
- [Build an HTTP action](/en/developing-connectors/http/building-http-action)

---
