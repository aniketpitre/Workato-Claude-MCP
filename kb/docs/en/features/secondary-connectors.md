---
url: 'https://docs.workato.com/en/features/secondary-connectors.md'
description: >-
  Learn how secondary connectors let you connect two instances of the same app
  in Workato to move and sync data between them in a recipe.
---

# Secondary connectors

There are use cases where you are required to move data between two different instances of the same app, for example, an organization located in two different states might have two different Salesforce accounts, but would have to sync the data between the two states.

To automate such use cases in Workato, we support the notion of a **secondary connector**. In the example above, you would connect the primary Salesforce connector to the corporate instance and the secondary Salesforce instance to the subsidiary.

## How to use a Secondary connector on Workato

To use a secondary connector, select the secondary connector from the app picklist when choosing a trigger or action. The secondary connector has the same set of triggers and actions as the primary.

![Snowflake secondary connector](/assets/secondary-connector.Csk8wzo7.png)_Moving new rows in subsidiary Snowflake instance to main Snowflake instance_

> **SECONDARY CONNECTORS CREATE SEPARATE CONNECTIONS**
> 
> Secondary connectors establish a separate connection from primary connectors.

Workato supports secondary connectors for the following apps:

- [Amazon S3](/en/connectors/s3)
- [Azure Blob Storage](/en/connectors/azure_blob_storage)
- [Confluence](/en/connectors/confluence)
- [DocuSign](/en/connectors/docusign)
- [FTP/FTPS](/en/connectors/ftp)
- [HTTP](/en/developing-connectors/http-v2)
- [JDBC](/en/connectors/jdbc)
- [Jira](/en/connectors/jira)
- [Marketo](/en/connectors/marketo)
- [MySQL](/en/connectors/mysql)
- [NetSuite SOAP](/en/connectors/netsuite)
- [Okta](/en/connectors/okta)
- [On-prem files](/en/connectors/on-prem-files)
- [Oracle](/en/connectors/oracle)
- [PostgreSQL](/en/connectors/postgresql)
- [Quickbase](/en/connectors/quickbase)
- [Redshift](/en/connectors/redshift)
- [Salesforce](/en/connectors/salesforce)
- [SAP RFC](/en/connectors/sap)
- [ServiceNow](/en/connectors/servicenow)
- [SFTP](/en/connectors/sftp)
- [Slack](/en/connectors/slack)
- [Snowflake](/en/connectors/snowflake)
- [SQL Server](/en/connectors/mssql)
- [Workfront](/en/connectors/workfront)
- [Wrike](/en/connectors/wrike)
- [Zendesk](/en/connectors/zendesk)

---
