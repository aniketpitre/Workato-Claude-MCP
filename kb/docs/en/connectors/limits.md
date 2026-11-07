---
url: 'https://docs.workato.com/en/connectors/limits.md'
description: >-
  Review the timeout, language, database, and connector-specific quotas that
  apply to Workato connectors.
---

# Connector quotas

Connectors have the following quotas:

> **DEFAULT QUOTAS**
> 
> The quotas on this page are defaults based on Workato best practices and are configured to enable optimal platform performance. Customers on Enterprise plans or above can contact their Customer Success Representative to request an extension of these quotas for their specific use cases.

## Job execution timeout limits

View job execution timeout limits

| Description | Quota | Notes |
| --- | --- | --- |
| Standard job execution timeout | 90 minutes | This quota applies to all connectors except the following: REST, Salesforce, ServiceNow, SFTP Workspace admins can configure a custom job execution time quota in **Workspace admin > Settings > Workspace > General**, under [Active Job Execution Time Limit](/en/workspace-admin-settings.html#workspace-info). If you observe a timeout that differs from 90 minutes, your workspace admin may have set a different quota. |
| Job execution timeout for REST connector actions | If wait for response is `true`: 3,600 seconds (1 hour); If wait for response is `false`: 5,400 seconds (1.5 hours) | This quota applies to the following REST connector action: **Make request (v2)** action |
| Job execution timeout for Salesforce connector actions | 24 hours | This quota applies to the following Salesforce actions: **Insert bulk job** action, **Update bulk job** action, **Upsert bulk job** action, **Insert bulk job (v1)** action, **Update bulk job (v1)** action, **Upsert bulk job (v1)** action, **Retry bulk jobs** action, **Search subjects SOQL bulk CSV** action |
| Job execution timeout for ServiceNow connector actions | 600 seconds | This quota applies to the following ServiceNow actions: **Upload attachment** action |
| Job execution timeout for SFTP actions | 700 seconds | This quota applies to the following SFTP action: **Streamable download** action |

## Read request timeout limits

View read request timeout limits

The read request timeout limit is the number of seconds the client (gateway) waits for the server to respond. A read timeout occurs when the connection is established and the request is sent, but the server doesn't send a response before the timeout limit is reached. This prevents the request from being read.

| Description | Quota | Notes |
| --- | --- | --- |
| Read request timeout | 180 seconds | This quota applies to all connectors except the following: Amazon S3, Azure blob storage, Bim360, JavaScript, Python, REST, Ruby, Workday, Xactly |
| Read request timeout for select Amazon S3 connector actions | 1,200 seconds | This quota applies to the following S3 connector actions: **Get file** action, **Upload file** action, **Upload file streaming** action |
| Read request timeout for select Azure blob storage connector actions | Variable. If the `blob_type` is **BlockBlob**, the timeout is 900 seconds. Otherwise, the timeout is 180 seconds. | This quota applies to the following Azure blob storage connector actions: **Upload blob storage** action |
| Read request timeout for JavaScript evaluation in actions | 30 seconds | This quota applies to the following action: **Invoke custom JavaScript code** action |
| Read request timeout for Python evaluation in actions | 90 seconds | This quota applies to the following action: **Invoke custom Python code** action |
| Read request timeout for Ruby connector actions | 30 seconds | This quota applies to the following action: **Invoke custom Ruby code** action |
| Read request timeout for REST connector actions | Variable. If wait for request is `true`, the timeout is 3,600 seconds (1 hour). Otherwise, the timeout is 120 seconds. | This quota applies to the following REST connector action: **Make request (v2)** action |
| Read request timeout for Workday connector actions | 300 seconds | This quota applies to the following actions: **Get report** action, **Call operation** action |
| Read request timeout for Xactly connector actions | 300 seconds | This quota applies to the following Xactly connector actions: **Read rows** action |

## Connector-specific quotas

### Ruby connector quotas

View Ruby connector quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Memory quota for Ruby connector actions, including libraries, temporary memory, and inputs | 256 MB | NA |
| Timeout for Ruby connector actions | 30 seconds | NA |
| Read request timeout for Ruby connector actions | 30 seconds | This quota applies to the following action: **Invoke custom Ruby code** action |

### Python connector quotas

View Python connector quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Memory quota for Python connector actions, including libraries, temporary memory, and inputs | 256 MB | NA |
| Timeout for Python connector actions | 90 seconds | NA |
| Maximum code field size (scripts) for Python connector actions | 1 MB | NA |
| Maximum size quota for PDF files processed with the pypdf library | 35 MB | NA |
| Maximum size quota for CSV files processed with the Pandas library | 20 MB | This quota accounts for Pandas’ temporary storage requirements. |
| Maximum size quota for Excel files processed with the Pandas library | 5 MB | Uncompressing Excel files requires additional memory. |
| Read request timeout for Python evaluation in actions | 90 seconds | This quota applies to the following action: **Invoke custom Python code** action |

### JavaScript connector quotas

View JavaScript connector quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Memory quota for JavaScript connector actions, including libraries, temporary memory, and inputs | 256 MB | NA |
| Maximum code field size for JavaScript connector actions | 1 MB | NA |
| Timeout for JavaScript connector actions | 30 seconds | NA |
| Read request timeout for JavaScript evaluation in actions | 30 seconds | This quota applies to the following action: **Invoke custom JavaScript code** action |

### XML tools by Workato quotas

View XML tools by Workato quotas

| Description | Quota |
| --- | --- |
| XML tools by Workato actions, default payload quota | 10 MB |
| Parse XML document action, with streaming enabled | 200 MB |
| Maximum number of fields for the Generate XML document from XSD action | 5000 fields |

### CSV tools by Workato quotas

View CSV tools by Workato quotas

| Description | Quota |
| --- | --- |
| CSV tools parse CSV action maximum rows processed | 50,000 |
| CSV tools CSV composer maximum rows composed | 160,000 |

### JSON tools by Workato quotas

View JSON tools by Workato quotas

| Description | Quota |
| --- | --- |
| JSON tools parse JSON action | 700 MB |

### YAML tools by Workato quotas

View YAML tools by Workato quotas

| Description | Quota |
| --- | --- |
| YAML tools parse YAML action | 170 MB |

### Email by Workato quotas

View Email by Workato quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Message body and attachment quota in Email by Workato actions | 20 MB | This quota is for the combined size of the message body and attachment. |

### PDF tools by Workato quotas

View PDF tools by Workato quotas

| Description | Quota |
| --- | --- |
| PDF tools daily operations | 10,000 operations per day per workspace |
| PDF tools large file processing (files larger than 50 MB) | 10 operations per hour per workspace |
| PDF tools maximum file size per source file for all actions | 100 MB |
| Merge PDF action maximum input | 50 files, 100 MB combined |
| Split PDF action maximum output | 50 output files |

## Language connectors quotas

View language connectors quotas

| Description | Quota |
| --- | --- |
| Memory quota for language connectors | 200 MB |

## Database connector quotas

View general database connector quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Database connectors maximum rows returned (JSON) | 50,000 | NA |
| Database connectors action timeout | 500 seconds | NA |
| Database connectors deferred action timeout (Cloud) | 2 hours | Some database connector action timeouts may vary, including the Snowflake **Run long query custom SQL** action, which has a timeout limit of 60 minutes. |
| Maximum BLOB (Binary Large Object) size | 1 MB | NA |
| Query size quota for **Run custom SQL** actions | 1 MB | This quota is effective December 1, 2025 and applies to the following connectors: **Google BigQuery**, **JDBC**, **IBM Db2**, **MySQL**, **Oracle**, **Postgresql**, **Redshift**, **Snowflake**, **SQL Server** |
| Maximum rows returned by **Select rows using custom SQL** actions | 50,000 | Starting February 8, 2026, the **Select rows using custom SQL** action returns a maximum of 50,000 records for all **new recipes and existing recipes that don't currently exceed this quota**. Starting March 15, 2026, this quota extends to **all recipes** using this action, including existing recipes that currently exceed the quota. Recipes configured to retrieve more than 50,000 records will be truncated to this quota. This applies to the following connectors: **Google BigQuery**, **JDBC**, **IBM Db2**, **Oracle**, **PostgreSQL**, **Redshift**, **Snowflake**, **SQL Server** |

### Apache Kafka connector quotas

View Kafka connector quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum batch size for Apache Kafka connector batch trigger | 100 messages | The batch size is configurable between 1-100 messages. |
| Maximum payload size for the Apache Kafka connector | 10 MB | NA |

### JavaScript Messaging Service (JMS) connector quotas

View JMS connector quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum message size for publish action | 4 MB | Applies to the following action: **Publish message** action |
| Maximum message size | 16 MB | Applies to the following trigger: **New message in queue/topic** trigger |

### Server Message Block (SMB) connector quotas

View SMB connector quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum chunk size | 100 MB | The chunk size is configurable for some actions between 5 MB-100 MB |
| Maximum file size | 100 GB | Applies to the following actions: **Download file** action, **Upload file** action |

### On-prem files connector quotas

View On-prem files connector quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum chunk size | 10 MB | The chunk size is configurable between 32 KB-10 MB. |
| Maximum number of CSV lines chunk size | 2,000 lines | The CSV lines chunk size is configurable between 1-2,000 lines. |

### Java Database Connectivity (JDBC) connector quotas

View JDBC connector quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum number of rows in JDBC connector triggers | 20,000 rows | The number of rows is configurable between 1-20,000 rows. |

### Active Directory connector quotas

View Active Directory connector quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum entries for Active Directory triggers | 1,000 entries | The number of entries is configurable between 1-1,000. Supports pagination. |
| Maximum number of LDAP entries returned by Active Directory batch operations | 1,000 entries | NA |

### SAP RFC connector quotas

View SAP RFC connector quotas

| Description | Quota |
| --- | --- |
| Maximum webhook payload size (bytes) the New IDocs (batch) trigger | 10 MB |
| Maximum webhook rate limits for the New IDocs (batch) trigger | Steady rate: 20 events per second, equivalent to 72,000 events per hour; Burst allowance: 9,000 events that can be processed beyond the steady rate in a burst |
| Maximum byte quotas for the New IDocs (batch) trigger | Steady rate: 30 MB, Burst allowance: 30 MB |

  

> **FURTHER READING**
> 
> Refer to the [Platform quotas](/en/limits) documentation for more information about Workato quotas.

---
