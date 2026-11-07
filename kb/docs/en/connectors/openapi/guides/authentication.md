---
url: 'https://docs.workato.com/en/connectors/openapi/guides/authentication.md'
description: >-
  Reference for the authentication methods supported by the OpenAPI connector,
  including None, Basic, Header, Query params, and OAuth 2.0 grants.
---

# OpenAPI Connector Authentication

This guide serves as a reference for the authentication methods supported by the [OpenAPI connector](/en/connectors/openapi/).

* * *

## Swagger Files And Authentication Methods

In some cases, the Swagger file for an application describes the required authentication method for the application. If the file contains this info, it can be useful for [selecting the correct authentication method while setting up the connection](/en/connectors/openapi/guides/setting-up-the-openapi-connector).

> **INFO**
> 
> The connector currently doesn't support automatically reading the authentication method from Swagger files, even if present.

* * *

## Supported Methods

The OpenAPI connector supports the following authentication methods:

- [None](#none)- [Basic](#basic)- [Header](#header)- [Query params](#query-params)- [OAuth 2.0: Authorization code grant](#oauth-2-auth-code-grant)- [OAuth 2.0: Client credentials grant](#oauth-2-client-credentials-grant)- [OAuth 2.0: Resource owner password grant](#oauth-2-resource-owner-password-grant)

In some cases, we support other authentication methods only when customizing the OpenAPI connector. Refer to the [Setting up custom connectors](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors#implement-authentication) guide for more information.

## None

This method doesn't require any authentication details. Use this method if:

- The application doesn't require authentication
- Authentication is performed from the input you provide in the recipe

## Basic

[Basic authentication](https://swagger.io/docs/specification/authentication/basic-authentication/) validates requests using a username and password. This is encoded with Base64 in transit over SSL; it is a common authentication flow.

### Input

<dl><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#basic-auth-user">Basic auth user</a></dt><dd>The name of the application user/account.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#basic-auth-password">Basic auth password</a></dt><dd>The password of the user. An alternative to your password would be an API key or API token, retrieved from your account settings.</dd><dd>This should be kept secret.</dd></dl>

## Header

For applications that require additional headers outside of the usual username and password or API key, or if you want to customize the headers sent in the request, use header authentication. You can also use header authentication when you already have a generated token.

### Input field

<dl><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#header-authorization">Header authorization</a></dt><dd>Add custom auth headers, one on each line.</dd><dd><p>Example:</p><div class="language- vp-adaptive-theme"><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>X-api-token: secret42</span></span>
<span class="line"><span>Authorization: Bearer AbC123XyZ789uje4</span></span></code></pre></div></dd></dl>

## Query params

For applications where the authentication structure depends on validating URL query parameters, use the query params authentication.

### Input

<dl><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#query-param-auth">Query param authorization</a></dt><dd>Add custom URL query params, one on each line.</dd><dd><p>Example:</p><div class="language- vp-adaptive-theme"><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>token: 872943684629</span></span>
<span class="line"><span>api-key: DKDF34KD8DD</span></span></code></pre></div></dd></dl>

## OAuth 2.0: Authorization code grant

The [Authorization code grant flow](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow) is the authentication standard adopted by a number of cloud apps. It is popular because it allows you to give third parties access to your apps without having to disclose your username and password to the third party. In this case, Workato simply redirects you to your app, where you key in your login credentials. This is sufficient for the app to trust that Workato is acting on your behalf when it makes API requests.

The Authorization Code grant type is for use by confidential and public clients to exchange an authorization code for an access token. In addition, it requires that you have the following input information.

### Input

<dl><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#authorization-url">OAuth2 authorization URL</a></dt><dd>This is the URL where Workato redirects you when you click <strong>Connect</strong>. This is usually the log in screen of your app.</dd><dd>This should be publicly available from the API documentation of the app you’re connecting to, under the <strong>Authentication</strong> section.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#token-url">OAuth2 token URL</a></dt><dd>The URL where Workato retrieves an auth token. The auth token is used to verify that we have permission to access your app and its data.</dd><dd>This should be publicly available from the API documentation of the app you’re connecting to, under the <strong>Authentication</strong> section.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#access-token-request-mode">How does the API require credentials to be sent to request a token?</a></dt><dd>Depending on the app you’re connecting to, you may have to send your credentials either in the request body, or as a header.</dd><dd>This should be publicly available from the API documentation of the app you’re connecting to, under the <strong>Authentication</strong> section.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#client-id">Client ID</a></dt><dd>Public ID of the OAuth app that should be tied to Workato.</dd><dd>This is usually found in the <strong>Settings</strong> or <strong>Integrations</strong> page (or equivalent) of your logged in app account, where you plan to connect, and should be kept secret.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#client-secret">Client secret</a></dt><dd>Matching private key that the application verifies along with the Client ID.</dd><dd>This is usually found in the <strong>Settings</strong> or <strong>Integrations</strong> page (or equivalent) of your logged in app account, where you plan to connect, and should be kept secret.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#scopes">OAuth2 scopes</a></dt><dd>Scopes are permissions that you can request from the app.</dd><dd>This is usually found in the <strong>Settings</strong> or <strong>Integrations</strong> page (or equivalent) of your logged in app account, where you plan to connect.</dd></dl>

## OAuth 2.0: Client credentials grant

Use the [Client credentials grant flow](https://auth0.com/docs/get-started/authentication-and-authorization-flow/client-credentials-flow) when Workato requests an access token using only client credentials.

This approach is ideal when requesting access to the protected resources under your control, or for machine-to-machine authentication where a specific user’s permission to access data is not required.

### Input

<dl><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#token-url">OAuth2 token URL</a></dt><dd>URL where Workato retrieves the auth token. This auth token verifies that we have permission to access your app and its data.</dd><dd>This should be publicly available from the API documentation of the app you’re connecting to, under the <strong>Authentication</strong> section.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#access-token-request-mode">How does the API require credentials to be sent to request a token?</a></dt><dd>Depending on the app you’re connecting to, you may send your credentials either in the request body, or as a header.</dd><dd>This should be publicly available from the API documentation of the app you’re connecting to, under the <strong>Authentication</strong> section.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#client-id">Client ID</a></dt><dd>Public ID of the OAuth app that should be tied to Workato.</dd><dd>This is usually found in the <strong>Settings</strong> or <strong>Integrations</strong> page (or equivalent) of your logged in app account where you plan to connect, and should be kept secret.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#client-secret">Client secret</a></dt><dd>Matching private key that the application verifies along with the Client ID.</dd><dd>This is usually found in the <strong>Settings</strong> or <strong>Integrations</strong> page (or equivalent) of your logged in app account where you plan to connect, and should be kept secret.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#scopes">OAuth2 scopes</a></dt><dd>Scopes are permissions that you can request from the app.</dd><dd>This is usually found in the <strong>Settings</strong> or <strong>Integrations</strong> page (or equivalent) of your logged in app account where you plan to connect.</dd></dl>

## OAuth 2.0: Resource owner password grant

Use the [Resource owner password grant flow](https://auth0.com/docs/get-started/authentication-and-authorization-flow/resource-owner-password-flow) when Workato requests a token to access application resources using user credential (username and password).

### Input

<dl><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#token-url">OAuth2 token URL</a></dt><dd>URL where Workato retrieves the auth token. This auth token is used to verify that we have permission to access your app and its data.</dd><dd>This should be publicly available from the API documentation of the app you’re connecting to, under the <strong>Authentication</strong> section.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#client-id">Client ID</a></dt><dd>Public ID of the OAuth app that is tied to Workato.</dd><dd>This is usually found in the <strong>Settings</strong> or <strong>Integrations</strong> page (or equivalent) of your logged in app account where you plan to connect, and should be kept secret.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#client-secret">Client secret</a></dt><dd>Matching private key that the application verifies along with the Client ID.</dd><dd>This is usually found in the <strong>Settings</strong> or <strong>Integrations</strong> page (or equivalent) of your logged in app account where you plan to connect, and should be kept secret.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#username">Username</a></dt><dd>The name of the user who sends these API calls.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#password">Password</a></dt><dd>The password of the user who sends these API calls.</dd><dd>This should be kept secret.</dd><dt><a href="/en/connectors/openapi/reference/default-connection-fields.html#scopes">OAuth2 scopes</a></dt><dd>Scopes are permissions that you request from the app.</dd><dd>This is usually found in the <strong>Settings</strong> or <strong>Integrations</strong> page (or equivalent) of your logged in app account where you plan to connect.</dd></dl>

---

---
url: >-
  https://docs.workato.com/en/connectors/openapi/guides/setting-up-the-openapi-connector.md
description: >-
  Install and set up an OpenAPI connector in Workato, including providing a
  Swagger file and configuring authentication and connection fields.
---

# Setting Up The OpenAPI Connector

In this guide, we'll walk you through installing and setting up an OpenAPI connector in your Workato account.

> **INFO**
> 
> Refer to the [Using OpenAPI connector to create custom connectors guide](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors) if you want to fully customize your connector.

* * *

## Requirements

To set up an OpenAPI connection, you'll need:

- **Privileges in Workato that allow you to create connections.**
  
- **A Swagger file that**:
  
  - Conforms to the OpenAPI v2 or v3 [specifications](https://swagger.io/specification/v3/)
  - Is valid JSON or YAML
  
  **Note**: We recommend using the connector with [RESTful APIs](https://restfulapi.net/). Refer to the [Limitations section in the OpenAPI overview](/en/connectors/openapi/#limitations) for more info.
  

* * *

## Step 1: Install The Connector

The first step is to install the connector in your Workato account:

1. Open [the connector in the community library](https://app.workato.com/custom_adapters/50046/details?community=true).
   
2. Click **Install connector**.
   
3. Click **Release latest version**.
   

* * *

## Step 2: Configure The Connection In Workato

- [Step 2.1: Provide The OpenAPI Document](#provide-api-definition)
- [Step 2.2: Define The Authentication Settings](#define-auth)
- [Step 2.3: Define Server And Testing URLs](#define-server-testing-urls)
- [Step 2.4: Customize The Interface](#customize-interface)

### Step 2.1: Provide The OpenAPI Document

In this step, you'll provide the Swagger file containing the API definition.

How you accomplish this is dependent on whether the file is publicly accessible on the internet:

My file is publicly accessible

If the Swagger file is publicly accessible:

1. Select **Document URL** as the **OpenAPI document source**.
   
2. In the **Document URL** field, paste the document URL to the file.
   

**Note**: Files are only downloaded and parsed at recipe design time. When recipes are run - or when OpenAPI actions are executed - the file won't be downloaded.

My file is not publicly accessible

If the Swagger file isn't hosted or isn't publicly accessible, you can copy and paste the file into Workato:

1. Select **Download content** as the **OpenAPI document source**.
   
2. In the **Document content** field, paste the contents of the file.
   

### Step 2.2: Define The Authentication Settings

Next, you'll define the authentication method for the connection. Learn more about the supported authentication methods [in the OpenAPI overview guide](/en/connectors/openapi/guides/authentication).

Select the method you're using from the **Authentication Method** menu.

### Step 2.3: Define Server And Testing URLs

Next, you'll define the server and testing URLs for the connector:

- **Server URL**: Enter the URL to the application's target host or service, including the `https://`. This is the base URL for requests sent by the connector. For example: `https://api.example.com`
  
  Relative endpoint paths from the [API definition](#provide-api-definition) will be appended to this URL to construct the full endpoint URL.
  
- **Test Request URL**: Enter the relative path of an API endpoint that Workato can use to verify the connection. This path will be appended to the **Server URL** to construct a full endpoint URL for testing. For example: `/user/profile`
  
  Connections are successful when the API responds with a `2XX` status code.
  

For example: A **Server URL** of `https://api.example.com` and a **Test Request URL** of `/users/profile` creates a full request URL of: `https://api.example.com/users/profile`

### Step 2.4: Customize The Interface

The OpenAPI connector automatically generates the user interface based on the content of the provided [Swagger file](#provide-api-definition). The following elements can be customized to improve the user experience:

- Object names
- Object hints
- Field names
- Field hints
- Links to external documentation
- API operation grouping
- Fields to ignore

Check out the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces) for more info and examples.

* * *

## Step 3: Test The Connection

When finished configuring the connection, click **Connect** to save and test the connection.

---
