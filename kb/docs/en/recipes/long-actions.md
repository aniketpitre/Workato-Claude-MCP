---
url: 'https://docs.workato.com/en/recipes/long-actions.md'
description: >-
  Learn how Workato long actions process bulk data over minutes to hours without
  timeout errors, including supported connectors and long pauses.
---

# Long actions

Long actions (or long running actions) are a special class of Workato actions that excels at processing bulk data. Long actions may require several minutes to hours to complete.

Under normal circumstances, actions throw a [timeout error](/en/recipes/jobs#timeouts) after a certain amount of time has elapsed. However, long actions allow the action to complete without raising a timeout error.

> **LONG ACTIONS NOW SUPPORTED IN TEST MODE**
> 
> Long actions are now supported in test mode. This means that you can click the **Test recipe** button to test recipes that contain batch actions, wait actions, long queries, and multi-step SDK actions.

## How does this work?

Workato temporarily puts the job on hold and checks periodically to determine if the long action has completed processing when the job execution reaches a long action. Workato proceeds to the next step in the recipe after the action completes.

> **LONG ACTIONS JOB SEQUENCE**
> 
> If your recipe has a long action step and job, note that [when the action is put on hold](/en/recipes/long-actions#how-does-this-work), Workato automatically disregards the job sequence. The next job begins to process even if the previous job is not finished and the recipe concurrency is set to `1`.

## Handle long pauses in recipes

Workato supports long pauses in recipe execution for up to 732 days. This includes single-step pauses, such as the Scheduler by Workato [Wait for time duration](/en/features/scheduler/actions/wait-for-time-duration) and [Wait until specified time](/en/features/scheduler/actions/wait-until-specified-time) actions, and cumulative pauses across multiple steps.

Use pauses to wait until a specific time or for an external event, such as an approval or trigger.

Recipes may fail if they exceed the total configured cumulative pause duration across all long actions.

## Supported long actions

Long actions are supported by applications including Salesforce, NetSuite, database applications, and more.

| Connector | Long actions |
| --- | --- |
| Anaplan | Run data import: Run a data import process in Anaplan., Run data export: Run a data export process in Anaplan., Run deletion: Run a delete action in Anaplan., Run process: Run a process in Anaplan. |
| Azure OpenAI | Generate images: Generates images in Azure OpenAI. |
| Google BigQuery | Search rows: Searches rows in Google BigQuery., Search rows using custom SQL: Searches rows in Google BigQuery using custom SQL., Run custom sql in BigQuery: Runs custom SQL in Google BigQuery., Load data into BigQuery: Loads data into Google BigQuery., Select rows: Selects rows in a table in Google BigQuery., Select rows using custom SQL: Selects rows in Google BigQuery using custom SQL., Select rows using custom SQL and insert into table: Selects rows using custom SQL and inserts rows into a table in Google BigQuery., Load data from Google Cloud Storage into BigQuery: Loads data from Google Cloud Storage into Google BigQuery. |
| Google Sheets | Update rows in bulk: Updates rows in bulk in Google Sheets. |
| Hubspot | Import CRM Data: Imports CRM data in Hubspot., Export object data: Export content from HubSpot to a file. You can use the file contents in subsequent recipe steps to upload the file into other applications. |
| Marketo | Bulk import objects from file: Bulk imports objects from a file in Marketo., Bulk export objects from file: Bulk exports objects from a file in Marketo. |
| Netsuite | Create standard records in bulk: Creates standard records in bulk in Netsuite., Update standard records in bulk: Updates standard records in bulk in Netsuite., Upsert standard records in bulk: Upserts standard records in bulk in Netsuite., Create custom records in bulk: Creates custom records in bulk in Netsuite., Update custom records in bulk: Updates custom records in bulk in Netsuite., Upsert custom records in bulk: Upserts custom records in bulk in Netsuite. |
| Salesforce | Create records in bulk from CSV file: Creates records in bulk from a CSV file in Salesforce., Update records in bulk from CSV file: Updates records in bulk from a CSV file in Salesforce., Upsert records in bulk from CSV file: Upserts records in bulk from a CSV file in Salesforce., Create records in bulk from CSV file (API 1.0): Creates records in bulk from a CSV file in the Salesforce API 1.0., Update records in bulk from CSV file (API 1.0): Updates records in bulk from a CSV file in the Salesforce API 1.0., Upsert records in bulk from CSV file (API 1.0): Upserts records in bulk from a CSV file in the Salesforce API 1.0., Retry bulk job for failed records from CSV file: Retry a bulk job for failed records from a CSV file in Salesforce., Search records in bulk using SOQL query (API 1.0): Searches records in bulk using a SOQL query in Salesforce API 1.0., Search records in bulk using SOQL query (API 2.0): Searches records in bulk using a SOQL query in the Salesforce API 2.0. |
| SAP RFC | Call remote function module: Calls a remote function module in SAP RFC., Call BAPI: Calls BAPI in SAP RFC. |
| Shopify | Reorder product media using GraphQL: Reorders product media using GraphQL in Shopify., Create file using GraphQL: Creates a file using GraphQL in Shopify. |
| JSON Transformations by Workato | JSON transformation: Executes a JSON transformation in JSON Transformations by Workato. |
| RPA by Workato | Start job: Starts a job in RPA by Workato. |
| Callable recipes by Workato | Wait for async calls: Waits for specified async calls to complete before proceeding to the next step in Callable recipes by Workato. |
| SQL Transformations by Workato | Query data: Queries data in SQL Transformations by Workato. |
| Workato Data Tables | Create record: Creates a record in Workato Data Tables., Create records (batch): Creates records in batches in Workato Data Tables., Update record: Updates a record in Workato Data Tables., Update records (batch): Updates records in batches in Workato Data Tables., Upsert record: Upserts a record in Workato Data Tables., Upsert records (batch): Upserts records in batches in Workato Data Tables. These actions run as long actions only while uploading values into the data table's file-type columns. The job pauses between uploads. |
| Wrike | Create from blueprint: Creates from blueprint in Wrike. |
| Zendesk | Create/update record: Creates/updates a record in Zendesk. |
| Zoho CRM | Bulk create standard objects: Bulk creates standard objects in Zoho CRM., Bulk update standard objects: Bulk updates standard objects in Zoho CRM., Bulk upsert standard objects: Bulk upserts standard objects in Zoho CRM., Bulk create custom objects: Bulk creates custom objects in Zoho CRM., Bulk update custom objects: Bulk updates custom objects in Zoho CRM., Bulk upsert custom objects: Bulk upserts custom objects in Zoho CRM. |
| HTTP | Send request (offload proxy): Sends an offload proxy request in HTTP. You can designate this HTTP action as a long action by setting the **Wait for response field** to **Yes**. |
| Google Workspace | Transfer Data: Transfers data in Google Workspace. |
| Nasuni Management Console | Create share: Creates a share in Nasuni Management Console., Create volume: Creates a volume in Nasuni Management Console., Request snapshot volume: Requests a snapshot volume in Nasuni Management Console., Update share: Updates a share in Nasuni Management Console., Global lock folders: Manages global lock folders in Nasuni Management Console., Create directory: Creates a directory in Nasuni Management Console., Bring path into cache: Brings a path into the cache in Nasuni Management Console., Pin data to cache: Pins data to a cache in Nasuni Management Console., Disable pinning mode for folder: Disables pinning mode for a folder in Nasuni Management Console., Auto caching for file: Enables auto caching for files in Nasuni Management Console., Disable auto cache mode: Disables auto cache mode in Nasuni Management Console., Update folder quota: Updates folder quotas in Nasuni Management Console., Delete folder quota: Delete the folder quota in Nasuni Management Console. |
| SQL Server | Bulk load into table from an on-prem file: Bulk loads files into a table from an on-prem file in SQL Server., Export Query result: Exports a query result as a CSV in SQL Server., Run long query using custom SQL: Run long query using custom SQL: Runs a long query using custom SQL in SQL Server. |
| Databricks | Export query result: Exports a query result as a CSV in Databricks., Run long query using custom SQL: Runs a long query using custom SQL in Databricks. |
| IBM Db2 | Export query result: Exports a query result as a CSV in IBM Db2., Run long query using custom SQL: Runs a long query using custom SQL in IBM Db2. |
| JDBC | Export query result: Exports a query result as a CSV in JDBC., Run long query using custom SQL: Runs a long query using custom SQL in JDBC. |
| Knack | Export query result: Exports a query result as a CSV in Knack., Run long query using custom SQL: Runs a long query using custom SQL in Knack. |
| MongoDB | Export query result: Exports a query result as a CSV in MongoDB., Run long query using custom SQL: Runs a long query using custom SQL in MongoDB. |
| MSSQL | Export query result: Exports a query result as a CSV in MSSQL., Run long query using custom SQL: Runs a long query using custom SQL in MSSQL. |
| MySQL | Export query result: Exports a query result as a CSV in MySQL., Run long query using custom SQL: Runs a long query using custom SQL in MySQL. |
| Oracle | Export query result: Exports a query result as a CSV in Oracle., Run long query using custom SQL: Runs a long query using custom SQL in Oracle. |
| PostgreSQL | Export query result: Exports a query result as a CSV in PostgreSQL., Run long query using custom SQL: Runs a long query using custom SQL in PostgreSQL. |
| Amazon Redshift | Export query result: Exports a query result as a CSV in Amazon Redshift., Run long query using custom SQL: Runs a long query using custom SQL in Amazon Redshift. |
| Snowflake | Export query result: Exports a query result as a CSV in Snowflake., Run long query using custom SQL: Runs a long query using custom SQL in Snowflake. |

### Wait long actions

Wait long actions are supported by the applications in the following table.

| Connector | Long actions |
| --- | --- |
| Scheduler by Workato | Wait for interval: Waits for a specified interval of time., Wait until specified time: Waits until a time you specify. |
| Workbot for Slack | Wait for user action: Suspends the Workbot job until the user provides input. The job continues to the next action when Workbot receives the input. |
| Workbot for Microsoft Teams | Wait for user action: Suspends the Workbot job until the user provides input. The job continues to the next action when Workbot receives the input. |
| Workflow apps | Wait for user action: Suspends the Workflow app job until the user provides input. The job continues to the next action when the Workflow app receives the input. |

---
