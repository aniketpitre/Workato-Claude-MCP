---
url: 'https://docs.workato.com/en/data-orchestration/how-to/connect-data-sources.md'
description: >-
  Connect Workato to data sources like Salesforce, NetSuite, Oracle, Workday,
  SAP, and SQL Server to start building integration recipes.
---

# Connect to data sources

When you start building a recipe, the first step is establishing a connection between Workato and an application.

Each connection is associated with one instance of the application, such as a user account, and can be re-used across recipes.

- [NetSuite](/en/connectors/netsuite/netsuite-connect)
- [Oracle](/en/connectors/oracle/introduction)
- [Salesforce](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato)
- [SAP OData](/en/connectors/sap-odata/connection-setup)
- [SAP RFC](/en/connectors/sap/connection-setup)
- [SQL Server](/en/connectors/mssql/introduction#how-to-connect-to-sql-server-on-workato)
- [Workday](/en/connectors/workday#connection-setup)

Refer to the [connectors](/en/connectors/prebuilt-connectors) documentation for more information.

## Example: Connect Workato to Salesforce

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Salesforce` in the **New Connection** page.
   
3. Provide a name for your connection in the **Name** field.
   
   ![Salesforce connection setup](/assets/connect-to-salesforce.B5puhQuy.png)_Salesforce connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Sandbox** drop-down menu to determine the account connection type.
   
6. Optional. Click **Advanced** to configure advanced connection options.
   
7. Optional. Select the **Custom OAuth profile**. App requests use the profile specified in Workato when you select this option. This ensures that the connection is restricted to the same set of scopes you selected for all users with the profile, and the authentication flow uses the client app linked to the custom profile.
   
8. Click **Connect**, enter your Salesforce account credentials when prompted, and then click **Log In** to verify the connection.
   
   ![Salesforce connection setup](/assets/login.CIu5oc0P.png)_Log in to your Salesforce account_

---
