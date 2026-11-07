---
url: 'https://docs.workato.com/en/connectors/shopify.md'
description: >-
  The Shopify connector enables you to automate e-commerce workflows, managing
  online store orders, products, and customers across your applications.
---

# Shopify

[Shopify](https://www.shopify.com/) is an e-commerce platform that allows businesses to create online stores and sell products.

## API version

The Shopify connector uses the [Shopify REST Admin API](https://shopify.dev/docs/api/admin-rest) version `2026-01` and the [Shopify GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql/latest) version `2026-01`. You can monitor the availability of the API and other services through the Shopify Status page. Refer to [Shopify Status](https://www.shopifystatus.com/) for more information.

> **HOW DOES SHOPIFY HANDLE ITS API VERSION UPGRADES?**
> 
> Shopify generally releases a new version every three months, and maintains each release version for a maximum of twelve months. There are four stable versions supported at any point in time.
> 
> After one year, Shopify stops maintaining released versions. API calls to unsupported versions are automatically routed to the oldest currently supported stable version.
> 
> For instance, if the current available stable versions are `2025-07`, `2025-10`, `2026-01`, and `2026-04`, then any API calls requesting for `2025-04` version are automatically routed to the `2025-07` version by Shopify.
> 
> Refer to the Shopify [API versioning](https://shopify.dev/api/usage/versioning#release-schedule) documentation for more information.

## Connection setup

The Shopify connector supports the following authentication types:

- [OAuth 2.0 authentication](#oauth2)
- [Access token authentication](#access-token)

You must have a Shopify Partner account to connect to Shopify in Workato. Refer to the Shopify [Create an account](https://partners.shopify.com/signup) documentation for more information.

### OAuth 2.0 authentication

You must create an OAuth profile to use OAuth 2.0 authentication. Refer to [Create an OAuth profile](#oauth-profile-oauth2) for more information.

#### Minimum and default scopes

Workato requests the following scopes by default when setting up a connection to Shopify:

- `read_customers`
- `write_customers`
- `read_inventory`
- `write_inventory`
- `read_products`
- `write_products`
- `read_orders`
- `write_orders`
- `read_draft_orders`
- `write_draft_orders`

You can grant Workato access to the following scopes in addition to the default scopes:

- `write_reports`
- `read_reports`
- `write_payment_terms`
- `read_payment_terms`
- `read_product_listings`
- `read_assigned_fulfillment_orders`
- `write_assigned_fulfillment_orders`
- `read_merchant_managed_fulfillment_orders`
- `write_merchant_managed_fulfillment_orders`
- `read_third_party_fulfillment_orders`
- `write_third_party_fulfillment_orders`
- `read_all_orders`

The minimum scope required to establish a connection is `read_products`.

#### Shopify setup for OAuth 2.0 authentication

Refer to the following sections to create an OAuth profile and connect to Shopify using OAuth 2.0 authentication:

##### Create an OAuth profile

Workato requires a custom OAuth profile to connect to Shopify using OAuth 2.0. Complete the following steps to create a custom OAuth 2.0 profile:

1. Sign in to the [Shopify Dev Dashboard](https://dev.shopify.com/dashboard) with a Partner account.
   
2. Click **Create app**.
   
3. Enter a name for your app in the **Start from Dev Dashboard** section, then click **Create**.
   
4. Enter the following URL in the **App URL** field:
   
   ```
   https://www.workato.com
   ```
   
5. Enter the following URL in the **Redirect URLs** field:
   
   ```
   https://www.workato.com/oauth/callback
   ```
   
6. Go to **Settings**.
   
7. Copy and save the **Client ID** and **Secret** for use in Workato.
   
8. Go to **Your app name**.
   
9. Click **Install app**.
   
   ![Click Install app](/assets/install-app.k_tVy7g0.png)_Click **Install app**._
   
10. Select the store where you plan to install the app, then click **Install**.
    
11. Open Workato and go to **Tools > Custom OAuth profiles**.
    
12. Click **\+ New custom profile**.
    
13. Search for `Shopify` and select it as your app.
    
14. Enter a **Name** for the account.
    
15. Click **Create new app**.
    
16. Enter the **Client ID** and **Client secret** from Shopify.
    
17. Click **Done**.
    

The custom OAuth profile is successfully configured. Refer to [Connect to Shopify with OAuth 2.0 authentication](#oauth2-connect) to perform the remaining connection steps or to the Shopify [OAuth apps](https://shopify.dev/apps/auth/oauth/getting-started) documentation for more information.

Version `2022-10` and later releases require **published public** custom apps to satisfy Shopify's data protection policy to process customer data. Refer to the Shopify [Requirements](https://shopify.dev/docs/apps/store/data-protection/protected-customer-data#requirements) documentation for more information. You must have approval to access customer protected data if you are connecting through a published public custom app. Refer to the Shopify [Request access to protected customer data](https://shopify.dev/docs/apps/store/data-protection/protected-customer-data#request-access-to-protected-customer-data) documentation for more information.

This requirement doesn't apply if you connect through custom apps using access token authentication or unpublished custom apps. Refer to [Access token authentication](#access-token) for more information.

##### Connect to Shopify with OAuth 2.0 authentication

Complete the following steps to set up an OAuth 2.0 connection to Shopify in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Shopify` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Shopify Connection](/assets/shopify-connection-oauth.Bw8Zvxnf.png)_Shopify Connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
6. Enter the **Shop Name**. You can find this value in the URL for your Shopify account. For example, the shop name is `shopname` if the URL is `shopname.myshopify.com/admin`.
   
7. Optional. Use the **Requested permissions (OAuth scopes)** drop-down menu to select the permissions to request for this connection. Refer to the [Minimum and default scopes](#oauth2-scopes) section for more information.
   
8. Select the **Custom OAuth profile** to use for the connection. Refer to [Create an OAuth profile](#oauth-profile-oauth2) for more information.
   
9. Click **Connect** and sign in to Shopify if prompted.
   
10. Click **Install** to complete the connection.
    

### Access token authentication

You must complete the following steps to use access token authentication:

- [Create a Shopify integration app](#access-token-shopify-config).
- Optional. [Create an OAuth profile](#oauth-profile-access-token).

#### Shopify setup for access token authentication

Refer to the following sections to create a Shopify integration app, an OAuth profile, and connect to Shopify using access token authentication:

##### Create a Shopify integration app

Complete the following steps to create a custom Shopify integration app:

1. Sign in to the [Shopify Admin](https://admin.shopify.com/) page with a Partner account.
   
2. Go to **Settings > Apps**.
   
3. Click **Develop apps**.
   
4. Click **Build apps in Dev Dashboard**.
   
5. Click **Create app**.
   
6. Enter an **App name** and click **Create app**.
   
7. Enter the following URL in the **App URL** field:
   
   ```
   https://www.workato.com
   ```
   
8. Click **Select scopes** and select the scopes to provide Workato.
   
   Access token authentication requires at least the `read_products` permission to successfully connect Workato to Shopify.
   
   The recommended set of scopes are:
   
   - `read_customers`
   - `write_customers`
   - `read_inventory`
   - `write_inventory`
   - `read_products`
   - `write_products`
   - `read_orders`
   - `write_orders`
   - `read_draft_orders`
   - `write_draft_orders`
9. Click **Done**.
   
10. Enter the following URL in the **Redirect URLs** field:
    
    ```
    https://www.workato.com/oauth/callback
    ```
    
11. Click **Release**.
    
12. Optional. Enter a **Version name** and **Version message**.
    
13. Click **Release**.
    
14. Go to **Settings**.
    
15. Copy and save the **Client ID** and **Secret** for use in Workato.
    
16. Go to **Your app name**.
    
17. Click **Install app**.
    
    ![Click Install app](/assets/install-app.k_tVy7g0.png)_Click **Install app**_
    
18. Select the store where you plan to install the app, then click **Install**.
    
19. Use the client credentials grant flow to programmatically request an access token. Refer to the Shopify [Using the client credentials grant](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant) documentation for more information.
    

The custom app is successfully configured in Shopify. Refer to the Shopify [Apps for your Shopify store](https://help.shopify.com/en/manual/apps/custom-apps?shpxid=ee07453d-134E-4EE7-81C4-84EFAF3239C3) documentation for more information.

Optional. Refer to [Create an OAuth profile](#oauth-profile-access-token) to manage permissions and credentials using a custom profile.

##### Create an OAuth profile

Optionally, complete the following steps to create a custom OAuth profile that manages permissions and credentials for your connection:

1. Open Workato and go to **Tools > Custom OAuth profiles**.
   
2. Click **\+ New custom profile**.
   
3. Search for `Shopify` and select it as your app.
   
4. Enter a **Name** for the account.
   
5. Click **Create new app**.
   
6. Enter the **Client ID** and **Client secret** from Shopify.
   
7. Click **Done**.
   

##### Connect to Shopify with access token authentication

Complete the following steps to set up an access token authentication connection to Shopify in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Shopify` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Shopify Connection](/assets/shopify-connection-access-token.DqySWNUW.png)_Shopify Connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Access token**.
   
6. Enter the **Access token** from Shopify.
   
7. Enter the **Shop Name**. You can find this value in the URL for your Shopify account. For example, if the URL is `shopname.myshopify.com/admin`, the shop name is `shopname`.
   
8. Optional. Select the **Custom OAuth profile** to use for the connection. Refer to [Create an OAuth profile](#oauth-profile-access-token) for more information.
   
9. Click **Connect**.

---
