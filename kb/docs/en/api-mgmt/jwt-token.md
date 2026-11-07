---
url: 'https://docs.workato.com/en/api-mgmt/jwt-token.md'
description: >-
  Set up JSON Web Token (JWT) authentication for API platform clients using RSA
  or HMAC signing to authenticate calls with signed tokens.
---

# JSON Web Token (JWT)

You can use JSON Web Tokens (JWT) to authenticate API clients that call recipes exposed through the API platform. JWT offers a secure, flexible alternative to static credentials, enabling systems like internal tools and third-party services to authenticate with signed tokens.

Workato supports both RSA (public/private key) and HMAC (shared secret) signing methods. To authenticate, the client signs a token with its Workato API key. The platform verifies the token to authorize access to endpoints.

JWT is defined by the [RFC 7519](https://tools.ietf.org/html/rfc7519) specification.

## Supported signing methods

Workato supports two signing methods:

| Signing method | Description |
| --- | --- |
| RSA (public key) | **Recommended**. Uses an asymmetric key pair. The client signs tokens with its private key and registers the public key with Workato. |
| HMAC (deprecated) | Uses a symmetric shared secret. The client and Workato use the same 256-bit secret string. |

## Set up JWT authentication for an API client

Complete the following steps to configure JWT authentication and enable secure API access:

1. [Create an API client](#create-new-client)
2. [Set up authentication](#rsa-signing-method)
3. [Create an application](#create-an-api-key)
4. [Generate a JSON web token](#how-to-generate-jwt-tokens)

### Create an API client

Complete the following steps to add and configure a new client:

1. Add an API client
   
   1. Go to **Platform > API Platform**.
      
   2. Select the **Clients** tab.
      
   3. Click **\+ Add new client**.
      
      ![Add new client](/assets/add-a-client.CzD77CsN.png)_Add new client_
      
   
2. Set up client details
   
   1. Enter a **Name** for your client. Use a descriptive identifier, such as the client's company or department name.
      
      ![Set up client details](/assets/add-client-details.DQ-ipDux.png)_Set up client details_
      
   2. Enter a **Description** for the client.
      
   3. Upload a **Client logo**. Drag and drop a JPG/PNG image or click **Upload from device** to select a file. This logo visually identifies your client in the portal.
      
   4. Enable the **Grant client access to portal** toggle to enable portal access. This grants your client permission to browse published API collections and manage their API keys. If your client only requires API tokens for testing or internal purposes, you can leave the toggle disabled.
      
   5. Provide the client identity based on your portal's [authentication method](/en/api-mgmt/configure-developer-portal#configure-authentication-settings):
      
      **Workato Identity**
      
      Use the **Client** drop-down menu to select the client. The list only includes end users already added to Workato Identity.
      
      **Magic link**
      
      Enter the client's email address in the **Email** field. Workato sends the client an email with a portal invitation.
      
   6. Click **Next** to proceed to the **Define access configuration** screen, where you can configure your client's API access.
      
   
3. Define access configuration
   
   1. Select **JSON Web Token** as the **Authentication method**.
      
   2. Optional. Toggle **Enforce mutual TLS (mTLS)** to require clients to present a valid certificate during the SSL handshake. This enforces two-way authentication. Refer to the [mTLS authentication](/en/api-mgmt/mtls) guide for more information.
      
      > **Note**: This setting appears only if you configure your workspace with a custom domain.
      
   3. Use the **API collections to include** drop-down menu to select one or more API collections. This defines the APIs your client can access and invoke in the portal. You can also create a client without collections to allow discovery before you grant API access.
      
   4. Optional. Assign a **Policy** to control your client’s API usage. Policies define rules such as rate limits or usage quotas.
      
   5. Click **Next**.
      
   

### Set up authentication

Complete the following steps to set up the security credentials required for token verification:

1. Choose a **Signing method**:
   
   - **RSA (public key)** _(recommended)_
   - **HMAC (deprecated)**
   
   ![Select a signing method](/assets/jwt-token-signing-method.ynTaffxU.png)_Select a signing method_
   
2. Follow the appropriate configuration steps below based on your selected signing method:
   
   **RSA (public key)**
   
   Complete the following steps to generate an RSA key pair and configure the public key in Workato:
   
   1. Open a terminal window.
      
   2. Run the following command to generate a key pair:
      
      ```shell
      ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key
      ```
      
      This command generates a private key (`jwtRS256.key`) and a public key (`jwtRS256.key.pub`).
      
      When prompted for a passphrase, leave it empty.
      
   3. Run the following command to convert the public key to PEM-encoded PKCS8 format:
      
      ```shell
      ssh-keygen -f jwtRS256.key.pub -e -m PKCS8 > jwtRS256.key.pub.pem && cat jwtRS256.key.pub.pem
      ```
      
      This creates a new file `jwtRS256.key.pub.pem` with the public key in PEM format.
      
   4. Copy the full output, including `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----`, and paste it into the **RSA public key** field in Workato.
      
      ![Paste the public key into the RSA public key field](/assets/jwt-token-rsa-public-key.BeJ4lRBu.png)_Paste the public key into the RSA public key field_
      
   
   **HMAC (deprecated)**
   
   Complete the following steps to generate an HMAC secret:
   
   1. Open a terminal window.
      
   2. Run the following command to generate an HMAC secret:
      
      ```shell
      openssl rand -base64 32
      ```
      
      ![Generate an HMAC secret](/assets/jwt-token-generate-hmac-secret.Bi4Cwf2K.gif)_Generate an HMAC secret_
      
   3. Copy the generated secret and paste it into the **HMAC secret** field in Workato.
      
      ![Paste the secret into the HMAC secret field](/assets/jwt-token-hmac-secret.BQmYLNh_.png)_Paste the secret into the HMAC secret field_
      
   
3. Click **Next** to create the client.
   

If portal access is enabled, Workato sends an email invitation to the client's email address. Permissions, such as access to API collections and authentication methods, are configured at the client level.

### Create an application

Complete the following steps to create an application and generate an API key. The client must include this key as the `kid` (key ID) claim in the JWT. The platform uses this value to locate and validate the client and its signing method.

> **SELECT API KEY AS THE CREDENTIAL TYPE**
> 
> This procedure requires an API key to embed as the `kid` claim. When prompted for a **Credential type**, select **API key**. [Custom validation](/en/api-mgmt/custom-validation) doesn't generate a key, so it won't produce anything to use in the remaining steps.

1. Go to **API Platform > Clients**, select the client, and go to the **Applications** tab.
   
2. Click **\+ Create application**.
   
   ![Create application](/assets/create-application.DsD4ZywD.png)_Create application_
   
3. Enter an **Application name** to identify the application.
   
   ![Configure new application](/assets/configure-application.Kw7db-IM.png)_Configure new application_
   
4. Select **API key** under **Credential type**.
   
   > **CUSTOM VALIDATION**
   > 
   > To validate JWT tokens using claim and scope rules instead of a Workato-issued key, select **Custom validation** instead. Custom validation is only available for clients using the JWT or OpenID Connect authentication method. Refer to [Custom validation for API applications](/en/api-mgmt/custom-validation) for the complete configuration procedure.
   
5. Click **Next**.
   
6. Optional. Add **Allowed IPs** to restrict requests to specific IP addresses. To allow multiple IPs, separate them with commas or define a range.
   
   ![Configure IP access rules](/assets/configure-ip-rules.DpX9N8hd.png)_Configure IP access rules_
   
7. Optional. Add **Blocked IPs** to prevent requests from specific IP addresses. Blocked IPs take precedence over allowed IPs. For example, if you add the IP address `123.456.123.456` to your allow list, but also block it, users who attempt to access the portal from this IP address are denied access.
   
8. Click **Create application**. Workato displays the authentication token. Save this token securely, as it doesn't display again. You must refresh or create a new application if you lose it.
   

### Generate a JSON web token

Construct and sign a JWT that includes the API key as the `kid` (key ID) claim in the JWT header:

```json
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "<YOUR-API-KEY>"
}
```

The client that initiates the API request is responsible for signing the JWT correctly. The platform will validate this token for authentication and access.

> **ALTERNATIVE CLAIMS**
> 
> In this example, the Workato API key is included in the header as the `kid` claim. Some identity providers may restrict the `kid` claim. If this is the case, you can include the API key in the payload section of the token, under one of the following claims: `https://www.workato.com/sub`, `workato_sub` or `sub`.
> 
> If these claims are used for other purposes in your use case, you may use a custom claim to hold the API key. [Learn more about alternative claims](/en/api-mgmt/jwt-workato-claim#default-claims-for-api-key).

Complete the following steps to generate and sign a JWT that includes the API key:

1. Go to [jwt.io](https://jwt.io/) to generate a JSON web token.
   
2. Click the **JWT Encoder** tab.
   
3. **RS256**
   
   Complete the following steps to create and sign a JWT using the RS256 algorithm:
   
   1. Go to the **HEADER: ALGORITHM & TOKEN TYPE** section and edit the header to include your API key:
      
      ```json
      {
        "alg": "RS256",
        "typ": "JWT",
        "kid": "<YOUR-API-KEY>"
      }
      ```
      
      Replace `<YOUR-API-KEY>` with the [API key](#create-an-api-key) you created in the previous steps.
      
   2. Go to the **SIGN JWT: PRIVATE KEY** section and paste your RSA private key.
      
      To retrieve the **RSA private key**, open a terminal and run the following command:
      
      ```shell
      cat jwtRS256.key
      ```
      
      Ensure the **Private Key Format** drop-down menu is set to **PEM**.
      
      The signed JWT appears in the **JSON WEB TOKEN** section.
      
      ![Generate a JWT using RS256](/assets/jwt-token-rs256.CI7uUICb.png)_Generate a JWT using RS256_
      
   3. Go to the **JSON WEB TOKEN** section and copy the generated JWT. You can use this JWT to authenticate requests to your Workato API endpoints in the following ways:
      
      - **When making HTTP requests** (using curl, Postman, or other tools), include the JWT in the `Authorization` header:
        
        ```http
        Authorization: Bearer <YOUR-JWT-TOKEN>
        ```
        
      - **When making requests in the developer portal**, paste the JWT into the **Auth token** field.
        
   
   **HS256**
   
   Complete the following steps to create and sign a JWT using the HS256 algorithm:
   
   1. Go to the **HEADER: ALGORITHM & TOKEN TYPE** section and edit the header to include your API key:
      
      ```json
      {
        "alg": "HS256",
        "typ": "JWT",
        "kid": "<YOUR-API-KEY>"
      }
      ```
      
      Replace `<YOUR-API-KEY>` with the [API key](#create-an-api-key) you created in the previous steps.
      
   2. Go to the **SIGN JWT: PRIVATE KEY** section and paste the [HMAC secret](#rsa-signing-method) you generated during authentication setup.
      
      The signed JWT appears in the **JSON WEB TOKEN** section.
      
      ![Generate a JWT using HS256](/assets/jwt-token-hs256.sA2GTpf4.png)_Generate a JWT using HS256_
      
   3. Go to the **JSON WEB TOKEN** section and copy the generated JWT. You can use this JWT to authenticate requests to your Workato API endpoints in the following ways:
      
      - **When making HTTP requests** (using curl, Postman, or other tools), include the JWT in the `Authorization` header:
        
        ```http
        Authorization: Bearer <YOUR-JWT-TOKEN>
        ```
        
      - **When making requests in the developer portal**, paste the JWT into the **Auth token** field.
        
   

You can also use an identity provider to issue the JWT with the API key embedded in one of the supported claims. Refer to [JWT Workato claim](/en/api-mgmt/jwt-workato-claim) for more information.

---
