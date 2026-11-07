---
url: 'https://docs.workato.com/en/data-orchestration/destinations.md'
description: >-
  Connect Workato to supported data destinations like Snowflake, BigQuery,
  Redshift, Databricks, Amazon S3, and SQL Server for storage and analysis.
---

# Data destinations

Data destinations are the systems, applications, or locations where you can send data for storage, processing, and analysis.

Use the following links to set up connections to our supported destinations:

- [Amazon S3](/en/connectors/s3/connection-setup)
- [Azure Blob Storage](/en/connectors/azure_blob_storage#connection-setup)
- [Databricks](/en/connectors/databricks#connect)
- [Google BigQuery](/en/connectors/bigquery#how-to-connect-to-bigquery-on-workato)
- [Redshift](/en/connectors/redshift#how-to-connect-to-redshift-on-workato)
- [Snowflake](/en/connectors/snowflake#how-to-connect-to-snowflake-on-workato)
- [SQL Server](/en/connectors/mssql/introduction#how-to-connect-to-sql-server-on-workato)

Refer to the [connectors](/en/connectors/prebuilt-connectors) documentation for more information.

## Example: Connect Workato to a Snowflake destination

These steps demonstrate how to use a Snowflake data warehouse as a destination for your Workato data pipeline. For more in-depth documentation on connecting Snowflake with Workato, refer to the [Snowflake connector](/en/connectors/snowflake) documentation.

To replicate this example, you need Workato and Snowflake accounts and a configured [Snowflake data warehouse](https://docs.snowflake.com/en/user-guide/warehouses-overview).

### Add Snowflake as a connection

Complete the following steps to add Snowflake as a connection:

1. Select **Create > Connection** (or press C twice) in your Workato workspace.
   
2. Search for and select Snowflake.
   
3. Enter the Snowflake connection information.
   
   ![Snowflake connection](/assets/connection.BBLDp5Fr.png)_Snowflake connection_
   
   | Field | Description |
   | --- | --- |
   | Connection name | Give this Snowflake connection a unique name that identifies which Snowflake instance it is connected to. |
   | Account identifier | [Account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier) of your Snowflake instance. Snowflake has multiple methods of identifying an account. Workato supports all methods: [account name, connection name, and account locator](https://docs.snowflake.com/en/user-guide/organizations-connect#connecting-with-a-url). **Account name:** `https://{orgname}-{account_name}`, **Connection name:** `https://{orgname}-{connectionname}`, **Account locator:** `https://{accountlocator}.{region}.{cloud}` If you're using the [account locator](https://docs.snowflake.com/en/user-guide/admin-account-identifier#using-an-account-locator-as-an-identifier), note that `{region}` and `{cloud}` are only required for certain locations. For example: If your account is hosted in AWS US West (Oregon), use `your-account-locator`; If your account is hosted in AWS US East (Ohio), use `your-account-locator.us-east-2`; If your account is hosted in Azure West Europe, use `your-account-locator.west-europe.azure` Learn more about [connecting to your Snowflake account](https://docs.snowflake.com/en/user-guide/organizations-connect). |
   | Authentication type | Choose an authentication type for this connection. Select between Username/Password and OAuth 2.0. |
   | [Warehouse](https://docs.workato.com/connectors/snowflake.html#warehouse-considerations) | Name of the warehouse to use for performing all compute for this connection. See [Warehouse considerations](https://docs.workato.com/connectors/snowflake.html#warehouse-considerations) for more information. |
   | Database | Name of the Snowflake database you plan to connect to. |
   | Username | Username to connect to Snowflake. The role granted to the User should have SYSADMIN privileges or lower. **Required** if you selected Username/Password authentication type. |
   | Password | Password to connect to Snowflake. The role granted to the User should have SYSADMIN privileges or lower. **Required** if you selected Username/Password authentication type. |
   | Client ID | Client ID to be used for the OAuth 2.0 authorization flow and token request. Learn more about [OAuth 2.0 setup](https://docs.workato.com/connectors/snowflake.html#configuring-oauth-2-0). **Required** if you selected OAuth 2.0 authentication type. |
   | Client secret | Client secret to be used for the OAuth 2.0 token request. **Required** if you selected OAuth 2.0 authentication type. |
   | Schema | **Optional**. Name of the schema within the Snowflake database you wish to connect to. Defaults to **public**. |
   | [Database timezone](https://docs.workato.com/connectors/snowflake.html#database-timezone) | **Optional**. Apply this to all timestamps without timezone. |
   
4. Select **Connect**.
   

### Use Marketo activity to update rows in Snowflake

This example borrows from the steps in the [Marketo, Salesforce, and Snowflake recipe](/en/getting-started/use-cases/marketo-salesforce-snowflake) use case. These steps assume an existing connection with Marketo and Snowflake but can be modified to fit your pipeline's needs.

Create a new recipe or update an existing recipe to add a set of values to rows in Snowflake.

1. Add a new action to the recipe with **Add step > Action in app**.
   
2. Search for and select `Marketo` in the **Choose an app** search box.
   
3. Select **New lead activity in Marketo batch** as the trigger.
   
4. Use the calendar modal to select the date from which the recipe should begin to monitor events in the **When first started, this recipe should pick up events from** field.
   
   Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field.
   
   ![Select activity](/assets/new-lead-activity-trigger.DyA4oJn5.png)_New lead activity batch trigger_
   
5. Search for and select `New Lead` in the **Activity** field.
   
   ![Select activity](/assets/new-lead-activity.3xfONKu1.png)_Select New lead as the activity_
   
6. Use the **List** drop-down menu to limit lead activity monitoring to a specific list. Lead activities from all lists are included if this field is empty.
   
7. Select an option for **Enrich lead data**:
   
   - **Yes**: The trigger output performs additional requests to supplement each activity record with the associated lead data.
     
   - **No**: Excludes lead enrichment requests to reduce the number of API requests.
     
8. Select **Save**.
   
9. Select the + **Add step** button and select **Action in app**.
   
10. Search for and select `Snowflake` in the **Choose an app** search box.
    
11. Select **Insert row** for your action.
    
12. Use the **Table** drop-down menu to select the name of the Snowflake table in which you plan to insert rows.
    
13. Select **Save**.

---
