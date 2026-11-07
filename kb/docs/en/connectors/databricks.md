---
url: 'https://docs.workato.com/en/connectors/databricks.md'
description: >-
  The Databricks connector provides tools that allow you to maintain data
  solutions at scale.
---

# Databricks

[Databricks](https://www.databricks.com/) is an enterprise-grade platform that provides tools that enable you to build, deploy, share, and maintain data solutions at scale. The Databricks connector allows you to fetch data from Databricks and send it to other applications such as Amplitude, Netsuite, and more.

## Connection setup

The Databricks connector supports the following authentication types:

- [OAuth 2.0 (Service Principal)](#oauth2)
- [Personal access token](#personal-access-token)

> **USERNAME/PASSWORD AUTHENTICATION DEPRECATED**
> 
> As of July 2024, basic username/password authentication for Databricks is deprecated. Refer to the Databricks [End of life for Databricks-managed passwords](https://docs.databricks.com/aws/en/release-notes/product/2024/july#end-of-life-for-databricks-managed-passwords) documentation for more information.

### OAuth 2.0 (Service Principal) authentication

You must generate the following values from Databricks to use this authentication method:

- Client ID
- Secret

#### Databricks setup for OAuth 2.0 (Service Principal) authentication

You must create a service principal to generate a client ID and secret.

##### Create a service principal

Complete the following steps to create a service principal in Databricks:

1. As an account admin, log in to the [Account console](https://accounts.cloud.databricks.com/).
   
2. Click **Users & groups**.
   
3. Click the **Service principals** tab.
   
4. Click **Add service principal**.
   
5. Enter a name in the **New service principal display name** field.
   
6. Click **Add service principal**.
   
7. Click the **Credentials & secrets** tab.
   
8. Click **Generate secret** under the **OAuth secrets** section.
   
9. Enter the number of days in the **Lifetime (days)** field.
   
10. Click **Generate**.
    
11. Copy and save the **Secret** and **Client ID** for use in Workato.
    
    > **SAVE YOUR CREDENTIALS**
    > 
    > The secret is only displayed once. If you lose it, you must create a new one.
    

#### Connect to Databricks with OAuth 2.0 (Service Principal) authentication

Complete the following steps to set up an OAuth 2.0 (Service Principal) authentication connection to Databricks in Workato:

1. Click **Create > Connection**.
   
2. Search for `Databricks` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Databricks overview](/assets/databricks-connect.B8QqhpyM.png)_Connect to Databricks_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the name of your server in the **Server hostname** field. For example, `example.cloud.databricks.com`.
   
6. Enter the **HTTP path**. For example, `sql/protocolv1/o/3957355953478232/0710-102114-bfnouzcv`.
   
7. Enter the **Port** your server uses. The default is `443`.
   
   > **CONNECTION DETAILS**
   > 
   > Refer to the Databricks [Get connection details for a Databricks compute resource](https://docs.databricks.com/aws/en/integrations/compute-details) documentation for information on how to retrieve connection details such as **Server hostname**, **HTTP path**, and **Port**.
   
8. Optional. Use the **Catalog** drop-down menu to select the catalog you plan to use for this connection. The default value is `hive_metastore`.
   
9. Optional. Use the **Schema** drop-down menu to select the schema you plan to use for this connection. The default value is `default`.
   
10. Optional. Use the **Database timezone** drop-down menu to select the timezone you plan to use. Workato uses this to convert timestamps during reads and writes.
    
11. Use the **Authentication type** drop-down menu to select **OAuth 2.0 (Service Principal)**.
    
12. Use the **Account type** drop-down menu to select the account type you plan to use.
    
13. Enter your **Client ID** and **Client secret**. Refer to [Create a service principal](#create-service-principal) for more information.
    
14. Optional. Select one or more **Scope** values from the drop-down menu. Workato uses the `sql` scope by default if none are selected.
    
15. Click **Connect**.
    

### Personal access token authentication

You must generate the following value from Databricks to use this authentication method:

- Personal access token

#### Databricks setup for personal access token authentication

Generate a personal access token from a Databricks workspace.

##### Generate a personal access token

Complete the following steps to create a personal access token in Databricks:

1. In your Databricks workspace, click your username and select **Settings**.
   
2. Click **Developer**.
   
3. Click **Manage** next to **Access tokens**.
   
4. Click **Generate new token**.
   
5. Enter a comment in the **Comment** field.
   
6. Enter the number of days in the **Lifetime (days)** field.
   
7. Select a **Scope**.
   
8. Select scopes from the **API scope(s)** drop-down menu.
   
9. Click **Generate**.
   
10. Copy and save the token for use in Workato.
    
    > **SAVE YOUR CREDENTIALS**
    > 
    > The token is only displayed once. If you lose it, you must create a new one.
    

#### Connect to Databricks with personal access token authentication

Complete the following steps to set up a personal access token authentication connection to Databricks in Workato:

1. Click **Create > Connection**.
   
2. Search for `Databricks` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Databricks overview](/assets/databricks-connect.B8QqhpyM.png)_Connect to Databricks_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the name of your server in the **Server hostname** field. For example, `example.cloud.databricks.com`.
   
6. Enter the **HTTP path**. For example, `sql/protocolv1/o/3957355953478232/0710-102114-bfnouzcv`.
   
7. Enter the **Port** your server uses. The default is `443`.
   
   > **CONNECTION DETAILS**
   > 
   > Refer to the Databricks [Get connection details for a Databricks compute resource](https://docs.databricks.com/aws/en/integrations/compute-details) documentation for information on how to retrieve connection details such as **Server hostname**, **HTTP path**, and **Port**.
   
8. Optional. Use the **Catalog** drop-down menu to select the catalog you plan to use for this connection. The default value is `hive_metastore`.
   
9. Optional. Use the **Schema** drop-down menu to select the schema you plan to use for this connection. The default value is `default`.
   
10. Optional. Use the **Database timezone** drop-down menu to select the timezone you plan to use. Workato uses this to convert timestamps during reads and writes.
    
11. Use the **Authentication type** drop-down menu to select **Personal Access Token**.
    
12. Enter your **Personal Access Token**. Refer to [Generate a personal access token](#generate-personal-access-token) for more information.
    
13. Click **Connect**.

---
