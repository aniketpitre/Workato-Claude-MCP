---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/connect-to-snowflake.md
description: >-
  Set up Snowflake as a data pipeline destination in Workato to replicate data
  from source applications using the source schema.
---

# Configure Snowflake as your data pipeline destination

Set up Snowflake as a destination for your data pipeline. This connection enables Workato to replicate data from source applications into Snowflake using the source schema.

## Features supported

The following features are supported when using Snowflake as a pipeline destination:

- Automatic creation of destination tables based on source schema
- Support for full and incremental data loads
- Field-level data replication without explicit field mapping
- Schema drift handling and update operations
- Use of staging and temporary tables for data integrity

## Prerequisites

You must have the following configuration and access:

- A Snowflake account with access to a database, warehouse, and schema
- A user role with privileges to create tables and load data
- A supported authentication method: OAuth 2.0, key-pair authentication, or username/password

## Connect to Snowflake

Complete the following steps to connect to Snowflake as a data pipeline destination. This connection allows the pipeline to replicate and load data into Snowflake.

Connect to Snowflake

1. Select **Create > Connection** or press C twice.
   
2. Search for `Snowflake` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Snowflake connection](/assets/connection.BBLDp5Fr.png)_Snowflake connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the [Account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier) of your Snowflake instance in one of the supported formats:
   
   - Account name: `https://{orgname}-{account_name}`
   - Connection name: `https://{orgname}-{connectionname}`
   - Account locator: `https://{accountlocator}.{region}.{cloud}`
   
   Refer to the Snowflake [Connecting to your accounts guide](https://docs.snowflake.com/en/user-guide/organizations-connect#connecting-with-a-url) for more details.
   
   > **ACCOUNT LOCATOR FORMAT**
   > 
   > Certain locations require you to include the `{region}` and `{cloud}` in your account locator URL. For example:
   > 
   > - **AWS US West (Oregon)**: `your-account-locator`
   > - **AWS US East (Ohio)**: `your-account-locator.us-east-2`
   > - **Azure West Europe**: `your-account-locator.west-europe.azure`
   > 
   > Refer to the [Using an account locator as an identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier#using-an-account-locator-as-an-identifier) guide for more information.
   
6. Enter the **Warehouse name** to define the compute resources for this connection. Refer to the [Warehouse considerations](/en/connectors/snowflake#warehouse-considerations) section for more information.
   
7. Enter the **Database name** for the target Snowflake database.
   
8. Select an **Authentication type**:
   
   - **OAuth 2.0**: Requires a **Client ID** and **Client secret**.
   - **Key-pair authentication**: Requires a Snowflake **User name**, a **Private key** in PKCS#8 format, and a **Private key passphrase** if the key is encrypted.
   - **Username/Password**: Requires a **User name** and **Password**.
   
   > **SNOWFLAKE USERNAME/PASSWORD DEPRECATION**
   > 
   > Snowflake plans to deprecate single-factor password authentication for users by **November 2025**.
   > 
   > We strongly encourage you to migrate all existing **Username/Password** connections to **OAuth 2.0** or **Key-pair authentication** before this date. Existing **Username/Password** connections will remain operational until the deprecation date.
   
   Refer to the [Snowflake connector authentication options](/en/connectors/snowflake#supported-authentication-methods) section for configuration steps.
   
9. Optional. Specify a **Role** for authentication. This role must be an existing role assigned to the user. If left blank, Snowflake uses the default role assigned to the user.
   
10. Optional. Enter the **Schema**. If left blank, the default schema is `public`.
    
11. Optional. Set the **Use improved datetime handling (Recommended)** to **Yes** to ensure correct timezone handling for timestamps.
    
12. Optional. Define the **Database timezone** to apply to timestamps without an assigned timezone.
    
13. Click **Connect** to verify and establish the connection.
    

## Configure the destination action

Before you start the pipeline, ensure the schema in Snowflake is newly created and empty. This prevents errors during the initial sync and ensures the pipeline can create destination tables without conflicts.

Complete the following steps to configure the destination action:

1. Click the **Load data to target table in destination app** action. This action defines how the pipeline replicates data in the destination.
   
   ![Load data to target table in destination app](/assets/configure-destination-action.Bg2UqkRW.png)_Configure the Load data to target table in destination app action_
   
2. Select **Snowflake** from the list of available destination apps.
   
3. Choose the Snowflake connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
   ![Choose a Snowflake connection](/assets/choose-snowflake-connection.C2OQtUZD.png)_Choose a Snowflake connection_
   
4. The **Load data to target table in destination app** action automatically replicates the object schema from the source to Snowflake. Explicit field mapping isn't required.
   
   Workato pipelines create destination tables based on the source schema. The pipeline also creates a stage and temporary tables to support data replication and update operations.
   
5. Optional. Click the **Load data to target table in destination app** action to configure how tables are created in Snowflake.
   
   1. Enter a **Schema** to organize tables under a specific schema. Workato uses the default schema from your connection if left blank.
      
   2. Enter a **Table prefix** to add a value to the beginning of every table name. This helps prevent naming conflicts when multiple pipelines write to the same schema.
      
      ![Configure Snowflake schema and table prefix](/assets/configure-snowflake-schema-prefix.BurSv7gu.png)_Configure Snowflake schema and table prefix_
      
      You can't change the **Schema** or **Table prefix** after the pipeline runs for the first time.
      
6. Select **Save** to save the pipeline.
   

## Identifier handling

Workato applies the following transformations to object and field names when replicating data into Snowflake:

- Column names are uppercased
- Special characters such as `$`, spaces, or dashes are replaced with underscores (`_`)
- Identifiers are wrapped in double quotes to support special characters and reserved words

These transformations ensure compatibility with Snowflake's SQL syntax and reserved keywords.

### Example

The following source table structure:

| Source object | Source field |
| --- | --- |
| `Account` | `$Name$`, `CreatedDate`, `Limit` |

Results in the following table created in Snowflake:

```sql
CREATE TABLE "ACCOUNT" ("_NAME_", "CREATEDDATE", "LIMIT")
```

Snowflake treats unquoted identifiers as case-insensitive, so you can run queries such as the following:

```sql
SELECT createddate FROM account;
SELECT "LIMIT" FROM ACCOUNT;
```

Quoted queries must match the exact case of the identifier.
