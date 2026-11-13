---
url: 'https://docs.workato.com/en/limits.md'
description: >-
  Reference for Workato platform quotas across workspaces, recipes, connections,
  environment properties, and other features that affect performance.
---

# Platform quotas

Workato enforces specific quotas, formerly referred to as limits, on our platform features and capabilities to optimize system performance and stability.

> **DEFAULT QUOTAS**
> 
> The quotas on this page are defaults based on Workato best practices and are configured to enable optimal platform performance. Customers on Enterprise plans or above can contact their Customer Success Representative to request an extension of these quotas for their specific use cases.

## Workspace quotas

### General workspace quotas

View general workspace quotas

| Description | Quota |
| --- | --- |
| Maximum number of collaborators in a workspace | 100 |
| Maximum number of child workspaces under one AHQ workspace | 100 |
| Maximum number of recipes in a workspace | 5,000 |
| Maximum number of tags in a workspace | 1,000 |

### Environment property quotas

View environment property quotas

| Description | Quota |
| --- | --- |
| Maximum number of environment properties per environment | 1,000 |
| Maximum length of an environment property name | 100 characters |
| Maximum length of an environment property value | 1,024 characters |

### Project property quotas

View project property quotas

| Description | Quota |
| --- | --- |
| Maximum number of project properties per project | 1,000 |
| Maximum length of project property name | 100 characters |
| Maximum length of project property value | 1,024 characters |

* * *

## Connection quotas

View connection quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Combined maximum of runtime user connections (RUC) and verified user access (VUA) connections per workspace | 100,000 per workspace | NA |
| Maximum shared connections per workspace | 500 per workspace | Shared connections, also known as parent connections, are established by the recipe builder when configuring runtime user connections (RUC) or verified user access (VUA) and are visible in the recipe editor as **This recipe's connection**. |

* * *

## Recipe quotas

### General recipe design time quotas

View general recipe design time quotas

| Description | Quota |
| --- | --- |
| Maximum recipe name length | 255 characters |
| Maximum number of webhook recipes subscribed to same URL | 100 |

### Recipe code size quotas

Recipe code size quotas vary by data center.

View US Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size | 90MB |
| Maximum number of steps in recipe code | 1,000 |

View EU Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View SG Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View JP Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View AU Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View IL Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View KR Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View UK Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View Self-service (Workato Free, Workato Pro, or Developer Sandbox) recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

### Job report quotas

View Job report quotas

| Description | Quota |
| --- | --- |
| Maximum number of columns in a job report | 10 |
| Maximum job report column value length | 256 characters |
| Maximum job report size | 5 KB |

### Test automation design time quotas

View Test automation design quotas

| Description | Quota |
| --- | --- |
| Maximum test case name length | 255 characters |
| Maximum test case description length | 1,000 characters |
| Maximum test case body length | 1,000,000 characters |
| Maximum batch size of test cases request when requested by IDs | 500 |
| Maximum number of test cases per recipe | 100 |

### General recipe run time quotas

View general recipe run time quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Job details: Maximum data storage of inputs/outputs across all steps | 1 MB | Job details are truncated if the total data exceeds 1 MB. |
| Webhook rate limits | Steady rate: 20 events per second, equivalent to 72,000 events per hour; Burst allowance: 9,000 events that can be processed beyond the steady rate in a burst | NA |
| Webhook byte quotas | 30 MB per minute, Burst allowance: 30 MB | These byte quotas represent the total memory in all your webhooks. |
| Maximum number of recipes subscribed to the same webhook URL | 100 | NA |
| Maximum recipe concurrency | Variable depending on your contract and plan. | This quota can be increased by contacting Customer Success. |
| Maximum number of recipe steps | 1,000 | NA |

### Queue size quotas

View queue size quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Size of recipe function queue | 10,000 | NA |
| Size of user actions queue | 1,000 | NA |
| Size of long action queue | 10,000 | Applies to recipe jobs with long running actions. These jobs enter a sleep state and move to the long action queue where they await processing. |
| Size of poller events queue | 10,000 | NA |
| Size of webhooks events queue | 20,000 | NA |

### Timeout limits

View timeout limits

| Description | Quota | Notes |
| --- | --- | --- |
| Standard job timeout | 90 minutes | [Workspace admins](/en/workspace-admin-settings.html#workspace-info) can configure a custom job execution time quota. If you observe a timeout that differs from 90 minutes, your workspace admin may have set a different quota. |
| HTTP action request timeout | If wait for response is `true`, the timeout is 1 hour; If wait for response is `false`, the timeout is 120 seconds | NA |
| Polling trigger timeout | 5 minutes | NA |
| Long pause/action timeout | 732 days | Recipes may fail if they exceed the total configured cumulative pause duration across all long actions. |

### Payload quotas

View payload quotas

| Description | Quota |
| --- | --- |
| Maximum trigger event payload size in bytes | 50 MB |
| Maximum payload size for callable recipes that are API platform endpoints | 1 MB (compressed) |

* * *

## Enterprise security quotas

View enterprise security quotas

| Description | Quota |
| --- | --- |
| Default data retention period for **Standard** and **Business** editions | 30 days |
| Default data retention period for **Enterprise** edition | 90 days |

* * *

## Workato Identity quotas

### SCIM provisioning quotas

View SCIM provisioning quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum users per add-to-group or remove-from-group API request | 100 users per request | SCIM provisioning has no request rate limit. The batch quota applies only to the number of users you can include in a single group-membership API request. |

### OAuth token quotas

View OAuth token quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Lifetime of an OAuth access token issued by Workato Identity | 1 hour | Refresh tokens don't have a lifetime quota. |

### End-user group quotas

View end-user group quotas

| Description | Quota |
| --- | --- |
| Time for adding a user to an end-user group, removing a user from a group, or removing a user from a workspace to take effect | Up to 1 hour |

* * *

## Workflow apps quotas

View Workflow apps quotas

| Feature | Description | Quota |
| --- | --- | --- |
| Tasks | Maximum expiration time for a task | 370 days |
| Workflow stages | Maximum number of workflow stages | 1,000 |
| User groups | Maximum number of user groups per user | 50 |
| Pages | Maximum file size for files uploaded to standard Pages | 500 MB |
| Pages | Maximum file size for files uploaded to public Pages | 100 MB |
| Recipe as a data source for drop-down components | Maximum number of records the **Workflow apps New open or search event from a drop-down** component trigger can return. If the number of records exceeds this quota, you can enable typeahead search and use the recipe to search for and load search results. | 1,000 |
| Data tables as a data source for drop-down components | Maximum number of records searchable using `contains` logic. If the data table has more than 100 records, Workflow apps uses `starts with` search logic instead. | 100 |
| Workflow apps connector | Maximum number of users or user groups you can share a request with using the Share requests action | 20 |

[General data tables and data tables column quotas](#data-tables-limits) also apply to Workflow apps.

* * *

## Data orchestration quotas

### SQL collection quotas

View SQL collection quotas

| Description | Quota |
| --- | --- |
| Recommended maximum number of records | 50,000 |

### SQL Transformations quotas

View SQL Transformations quotas

| Description | Quota |
| --- | --- |
| Maximum size of each data source used in a query | 10 GB |

* * *

## API platform quotas

View API platform quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Job timeout | 30 seconds (default), 240 seconds (maximum) | You can configure the job timeout to a maximum of 240 seconds. However, testing an API endpoint directly in Workato using an endpoint's **Test request** tab is limited to a fixed 30-second job timeout, regardless of your configured value. |
| Request header size (single header) | 16 KB | NA |
| Request headers and url size combined (all headers) | 64 KB | NA |
| Maximum JWKS size | 64 KB | NA |
| Maximum payload size | 5 MB | NA |
| Maximum attachment size | 5 GB | Attachments accept multipart/form-data. |
| Maximum tracer payload | 1 MB | The tracer payload is the complete record of an API request captured for debugging and monitoring. It includes details of the request, and metadata. The tracer payload may be truncated if the total request size exceeds 1 MB. |
| Maximum cache key size | 10 kB | NA |
| Maximum cache entry value size | 10 kB | Requests exceeding this quota do not cache even when successful. Contact your Workato Customer Success Manager to adjust this quota. |
| Maximum number of API keys per API client | 20 | NA |
| Maximum cache entry count per user ID | 10,000 entries | If exceeded, entries are flushed, from oldest to newest, to accommodate new entries. To adjust this quota, contact your Workato Customer Success Manager for support. |

* * *

## Event streams quotas

View Event streams quotas

| Description | Quota |
| --- | --- |
| Maximum message retention period | 90 days |
| Maximum number of topics per workspace | 20 |
| Maximum size of a single published message | 10 MB |
| Maximum total payload size returned in a single batch | 50 MB |

* * *

## Connector quotas

### Job execution timeout limits

View job execution timeout limits

| Description | Quota | Notes |
| --- | --- | --- |
| Standard job execution timeout | 90 minutes | This quota applies to all connectors except the following: REST, Salesforce, ServiceNow, SFTP Workspace admins can configure a custom job execution time quota in **Workspace admin > Settings > Workspace > General**, under [Active Job Execution Time Limit](/en/workspace-admin-settings.html#workspace-info). If you observe a timeout that differs from 90 minutes, your workspace admin may have set a different quota. |
| Job execution timeout for REST connector actions | If wait for response is `true`: 3,600 seconds (1 hour); If wait for response is `false`: 5,400 seconds (1.5 hours) | This quota applies to the following REST connector action: **Make request (v2)** action |
| Job execution timeout for Salesforce connector actions | 24 hours | This quota applies to the following Salesforce actions: **Insert bulk job** action, **Update bulk job** action, **Upsert bulk job** action, **Insert bulk job (v1)** action, **Update bulk job (v1)** action, **Upsert bulk job (v1)** action, **Retry bulk jobs** action, **Search subjects SOQL bulk CSV** action |
| Job execution timeout for ServiceNow connector actions | 600 seconds | This quota applies to the following ServiceNow actions: **Upload attachment** action |
| Job execution timeout for SFTP actions | 700 seconds | This quota applies to the following SFTP action: **Streamable download** action |

### Read request timeout limits

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
| Maximum number of fields for the Generate XML document from XSD action | 5,000 fields |
| Maximum nesting depth of a schema built from XSD or sample XML | 300 |
| Maximum number of properties, objects, and arrays in a schema built from XSD or sample XML | 15,000 |
| Maximum number of child properties in a single object of an XML-derived schema | 5,000 |
| Maximum time to build one XML schema, per request or response | 10 seconds |

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

### Dynamic schema building quotas

View dynamic schema building quotas

The following quotas apply to connectors that build their input and output schemas from your input at runtime, such as [XML tools by Workato](/en/connectors/xml-tools-workato).

| Description | Quota |
| --- | --- |
| Maximum nesting depth of a schema returned by a connector that builds schemas dynamically | 300 |
| Maximum number of properties, objects, and arrays in a single schema build | 15,000 |
| Maximum number of child properties in a single object | 5,000 |
| Maximum time to build one schema, per request or response | 10 seconds |

### Language connectors quotas

View language connectors quotas

| Description | Quota |
| --- | --- |
| Memory quota for language connectors | 200 MB |

* * *

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

### Kafka connector quotas

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

* * *

## Agentic quotas

### Agent Studio quotas

View Agent Studio quotas

| Description | Quota |
| --- | --- |
| Maximum data storage per document in a knowledge base | 100 MB |
| Sliding token context window | 64,000 |

### Genie task quotas

View genie task quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Rate quota for genie task requests | 500 requests per second | No quota applies to genie tasks triggered from Slack or Microsoft Teams. |

### Headless API quotas

View Headless API quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Rate quota for unauthenticated Headless API requests | 200 requests per second globally | 50 requests per second per genie and 50 requests per second per source IP also apply. |
| Rate quota for authenticated Headless API requests | 50 requests per second globally | 20 requests per second per workspace apply to all endpoints except **Send a message**. 5 requests per second per workspace apply to the **Send a message** endpoint. |
| Concurrent server-sent event (SSE) streams for authenticated Headless API requests | 1,000 concurrent streams globally | 100 concurrent SSE streams per workspace also apply. |

### Business event quotas

View business event quotas

| Description | Quota |
| --- | --- |
| Rate quota for business event requests | 16 requests per second |

* * *

## AI feature quotas

### AI by Workato quotas

View AI by Workato quotas

| Description | Quota |
| --- | --- |
| Rate limit for AI by Workato connector actions in direct customer workspaces | 60 requests per minute |
| Rate limit for AI by Workato connector actions in Embedded partner and customer workspaces | 10 requests per minute |
| Rate limit for AI by Workato connector actions in Self-service (Workato Free, Workato Pro, or Developer Sandbox) workspaces | 5 requests per minute |
| Token quotas for AI by Workato connector in Self-service (Workato Free, Workato Pro, or Developer Sandbox) workspaces | 10,000 tokens per request |

### IDP by Workato quotas

View IDP by Workato quotas

| Description | Quota |
| --- | --- |
| Rate limit for IDP by Workato connector actions in direct customer workspaces | 60 requests per minute |
| Rate limit for IDP by Workato connector actions in Embedded partner and customer workspaces | 10 requests per minute |
| Rate limit for IDP by Workato connector actions in Self-service (Workato Free, Workato Pro, or Developer Sandbox) workspaces | 5 requests per minute |

* * *

## AIRO quotas

View AIRO quotas

| Description | Quota |
| --- | --- |
| AIRO token budget per minute | Each workspace has its own AIRO token budget per model, computed over a rolling 60-second window. When a workspace exceeds its budget, subsequent requests are throttled and users may see up to a 30-second delay in AIRO responses until the budget refreshes. |
| Maximum file size for uploads in AIRO chat | 500 MB |
| Maximum file size for AIRO playbook uploads | 25 MB |

* * *

## MCP quotas

### MCP server quotas

View MCP server quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum number of access tokens created for a single MCP Server (API key) | 50 | NA |
| Maximum entries per IP allowlist or blocklist | 500 | Applies to the allowed-IP and blocked-IP lists independently. |
| Rate limit for refreshing the tool list from an upstream MCP server | 1 request per 60 seconds | NA |
| Synchronous tool-execution timeout. After this window elapses, the call detaches and continues in the background. | 30 seconds | Not configurable. |
| Total tool-execution timeout, including any background continuation after the synchronous phase. | 300 seconds | Set in the recipe settings. Requests that exceed this timeout don't return a response to the MCP client. |

### Dynamic client registration (DCR) quotas

View DCR quotas

| Description | Quota |
| --- | --- |
| Hourly rate limit for DCR requests per workspace in the US Data Center | 100,000 requests per hour |
| Daily rate limit for DCR requests per workspace in the US Data Center | 400,000 requests per day |
| Weekly rate limit for DCR requests per workspace in the US Data Center | 500,000 requests per week |

* * *

## On-prem quotas

View On-prem quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum number of on-prem groups per workspace | 20 | NA |
| Maximum number of on-prem agents per on-prem group | 10 | NA |
| Maximum request time for on-prem connectors | 500 seconds | This quota doesn't include database connector long actions. |

* * *

## Connector SDK quotas

View Connector SDK quotas

| Description | Quota |
| --- | --- |
| Maximum number of SDK/custom connectors in one workspace | 150 |
| Timeout for HTTP request inside SDK connectors in the Test code console | 40 seconds |
| Timeout for HTTP request inside SDK connectors in a job at runtime | 3 minutes |
| Timeout for compiling an SDK connector | 5 seconds |
| SDK Timeout credentials refresh | 30 seconds |
| Maximum number of swap outs in multi-step actions | 100 |
| Minimum swap interval in multi-step actions | 60 seconds |
| Maximum number of job suspensions | 50 |
| [Maximum consecutive polling without any jobs produced](/en/developing-connectors/sdk/guides/trigger-limit.html#consecutive-polls-in-a-single-poll-cycle-without-jobs) | 600 |
| [Maximum number of events in a single poll](/en/developing-connectors/sdk/guides/trigger-limit.html#number-of-events-per-poll) | 1,000 |
| Maximum data allowed in custom connector code | 10 MB |
| Compatible code formats | UTF-8 and JSON compatible |

* * *

## Custom connector quotas

View custom connectors quotas

| Description | Quota |
| --- | --- |
| Maximum number of SDK/custom connectors in one workspace | 150 |

* * *

## Lookup tables quotas

View lookup tables quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum number of lookup tables in a workspace | 100 | NA |
| Maximum number of columns in a lookup table | 10 | NA |
| Maximum number of rows in a lookup table | 100,000 | The Lookup tables connector **Get all entries** action retrieves only the first 10,000 entries.; Tables with more than 50,000 entries can't be downloaded as a CSV file. |
| Maximum row size | 128 KB | NA |
| Maximum number of rows in a lookup table in Recipe lifecycle management imports and exports | 10,000 | NA |
| Maximum file size for a lookup table imported through Recipe lifecycle management | 10 MB | This quota applies independently of the row count quota. A lookup table can exceed 10 MB with fewer than 10,000 rows when rows contain large values. Imports that exceed this quota are blocked before the diff screen appears. |
| Maximum batch size in lookup table connector actions | 10,000 | This quota applies to the following connector actions: **Add entries (batch)** action, **Get all entries (batch)** action |

* * *

## Data tables quotas

View general data tables quotas

| Description | Quota |
| --- | --- |
| Maximum number of data tables per workspace | 100 |
| Maximum number of rows per table | 1,000,000 |
| Maximum number of rows in a data table that can be [exported](/en/recipe-development-lifecycle/export.html#export-a-manifest-as-a-package) or [deployed](/en/features/environments/deployment.html#what-can-be-deployed) | 10,000 |
| Maximum number of columns per table | 100 |
| Maximum number of **Link to a table** column types per table | 20 |
| Maximum number of **Multi-value** column types per table | 20 |
| Maximum record size | 100,000 bytes |
| Maximum table size | 1,000,000,000 bytes |
| Maximum number of visible records (rows) at one time in the data tables UI | 200 |
| Maximum number of filters that can be applied simultaneously to a table in the data tables UI. Note that each additional filter is treated as an `AND` operand. | 10 |
| Maximum number of filters that can be applied to a field/column | 1 |

View data tables column quotas

| Column type | Description | Quota | Example |
| --- | --- | --- | --- |
| Short text | Text field used to store small strings or textual data. Typically, this data type is for names, short descriptions, status codes, or small identifiers. | Maximum of 10,000 characters. Sorting and filtering is supported for only the first 756 characters. | `A very short description`, `user@example.com`, `John Doe` |
| Long text | Multi-line text field. Typically, this data type is for large amounts of text, such as descriptions, comments, or any large block of text. | Maximum of 10,000 characters. Sorting and filtering is supported for only the first 756 characters. | `A long description or comment that can span many lines…` |
| Integer | Whole numbers without any fractional or decimal parts. Integers can represent both positive and negative values, including zero. | Integers are 64-bit (8-byte) and can range between `-9223372036854775808` and `9223372036854775807`. | `5000`, `100000`, `2147483647` |
| Decimal | IEEE-754 floating-point numbers. Commonly used for precise calculations involving fractional numbers, such as percentages or scientific measurements. | Floating-point numbers do not enforce a fixed number of decimal places. Precision is determined by the number’s range. For example, smaller values can represent more decimal places accurately, while larger values lose precision due to spacing between representable values. | `0.1`, `3.141592653589793`, `1.7976931348623157 × 10³⁰⁸` |
| Boolean | A true/false value. | NA | `TRUE`, `FALSE` |
| Date | Calendar dates (such as, year, month, and day) without time information. Useful for fields such as birthdates, event dates, or transaction dates. Date columns inherit the timezone and date and time format of your workspace. This means that the exact date format can vary, depending on your settings. | Supports a range of dates between 262,145 BCE and 262,143 CE. | `13/11/2024`, `11/13/2024` |
| DateTime | Date and time (including hours, minutes, seconds). Used to track exact moments of events, transactions, or logs. DateTime columns inherit the timezone and date and time format of your workspace. This means that the exact date and time format can vary, depending on your settings. | Follows RFC 3339 protocol. | `13/11/2024 00:00:00`, `11/13/2024 12:00 AM` |
| File | Allows you to upload or download files to/from your data tables. | Maximum file size: `500 MB`. File names can have up to `255` characters. | NA |
| Link to a table | Display data from a different data table in your workspace. Choose a **Linked data table** to select another data table to link to your current table and **Display data from** to determine which column from the data table you have selected displays as a dropdown. | Each data table can link to a maximum of `20` data tables. Data tables supports linking to **short text** and **long text** column types. | NA |
| Multi-value | This column supports storing multiple values in a single cell. Multi-value columns do not support nulls, empty strings, or duplicate values. Sorting columns is not supported. Supported value types include short **Text**, **Integer**, **Decimal**, **Date**, **DateTime**, and **Link to a table**. | Each data table can have a maximum of `20` multi-value columns. Each cell within a multi-value column can store up to `20` values. | NA |

View data tables connector quotas

| Description | Quota |
| --- | --- |
| Maximum batch size for all Data table connector batch triggers | 1,000 |
| Maximum batch size for all Data table connector batch actions, except **Delete records by condition**, which deletes up to 200 records per run | 1,000 |

* * *

## FileStorage quotas

View FileStorage quotas

| Description | Quota |
| --- | --- |
| Maximum file size | 10 GB |
| Maximum storage capacity available to a workspace's environment for direct customers | 100 GB |
| Maximum storage capacity available to an environment for Embedded customers | 100 GB |

* * *

## Resources quotas

View resources limits

| Description | Limit |
| --- | --- |
| Maximum size of a single resource file | 50 MB |
| Maximum combined size of all resources in an environment | 5 GB |
| Maximum number of versions stored per resource | 100 |

* * *

## Recipe lifecycle management quotas

View Recipe lifecycle management quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum import package file size | 100 MB | You can import one package at a time. |

* * *

## Custom OAuth profile quotas

View Custom OAuth profile quotas

| Description | Quota |
| --- | --- |
| Maximum number of Custom OAuth profiles | 50 |

* * *

## Logging service quotas

View logging service quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Retention period for log entries | 30 days or 1 million entries | This quota is independent of custom data retention quotas. |
| Maximum size of the data column for a single log entry | 10 KB | Content that exceeds the quota is truncated. |

* * *

## Audit log streaming quotas

View audit log streaming quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum size of a single audit log replication payload sent to a streaming destination | 40 MB | Payloads that exceed the quota are truncated before they reach the streaming destination. |

* * *

## Message templates quotas

View message templates quotas

| Description | Quota |
| --- | --- |
| Maximum number of Message templates in a workspace | 100 |

* * *

## Workato schemas quotas

View schemas quotas

| Description | Quota |
| --- | --- |
| Maximum number of schemas in a workspace | 100 |

* * *

## Developer API quotas

View Developer API quotas

Workato enforces specific quotas on Developer APIs to optimize performance and stability. Requests made to the Developer API are subject to the following timeout limit:

| Description | Quota |
| --- | --- |
| Timeout limit | 40 seconds |

In addition, Developer API resources have the following rate and payload quotas:

| Collection | Type | Resource | Quota |
| --- | --- | --- | --- |
| **Agent studio** | GET | List genies: [/api/agentic/genies](https://docs.workato.com/workato-api/agent-studio.html#list-genies) | 1,000 requests per minute |
| **Agent studio** | GET | Get a genie by ID: [/api/agentic/genies/:id](https://docs.workato.com/workato-api/agent-studio.html#get-a-genie-by-id) | 1,000 requests per minute |
| **Agent studio** | GET | All [genie conversation](https://docs.workato.com/workato-api/agent-studio.html#conversations) endpoints | 10 requests per second |
| **Agent studio** | All | All other [genie](https://docs.workato.com/workato-api/agent-studio.html#genies) endpoints | 60 requests per minute |
| **Agent studio** | GET | List Knowledge bases: [/api/agentic/knowledge\_bases](https://docs.workato.com/workato-api/agent-studio.html#list-knowledge-bases) | 1,000 requests per minute |
| **Agent studio** | GET | Get a Knowledge base by ID: [/api/agentic/knowledge\_bases/:id](https://docs.workato.com/workato-api/agent-studio.html#get-a-knowledge-base-by-id) | 1,000 requests per minute |
| **Agent Studio** | All | All other [Knowledge bases](https://docs.workato.com/workato-api/agent-studio.html#knowledge-bases) endpoints | 60 requests per minute |
| **Agent Studio** | GET | List Skills: [/api/agentic/skills](https://docs.workato.com/workato-api/agent-studio.html#list-skills) | 1,000 requests per minute |
| **Agent Studio** | GET | Get a skill by ID: [api/agentic/skills/:id](https://docs.workato.com/workato-api/agent-studio.html#get-a-skill-by-id) | 1,000 requests per minute |
| **Agent studio** | All | All other [Skills](https://docs.workato.com/workato-api/agent-studio.html#skills) endpoints | 60 requests per minute |
| **API clients** | All | All [API client](https://docs.workato.com/workato-api/api-client-apis.html) endpoints | 60 requests per minute |
| **API platform** | All | All [API platform](/en/workato-api/api-platform.html) endpoints | 60 requests per minute |
| **Collaborator groups** | All | All [Collaborator groups](/en/workato-api/collaborator-groups.html) endpoints | 60 requests per minute |
| **XChange** | All | All [XChange](/en/workato-api/xchange.html) endpoints | 60 requests per second |
| **Connections** | GET | List connections: [/api/connections](/en/workato-api/connections.html#list-connections) | 60 requests per minute |
| **Connections** | All | All other [Connections](/en/workato-api/connections.html) endpoints | 1 request per second |
| **Connectors** | All | All [Connectors](/en/workato-api/api-connectors.html) endpoints | 60 requests per minute |
| **Custom connectors** | POST | Generate schema from JSON: [/api/sdk/generate\_schema /json](/en/workato-api/custom_connectors.html#generate-schema-from-json) | 60 requests per minute |
| **Custom connectors** | POST | Generate schema from CSV: [/api/sdk/generate\_schema /csv](/en/workato-api/custom_connectors.html) | 60 requests per minute |
| **Custom connectors** | All | All other [Custom connectors](/en/workato-api/custom_connectors.html) endpoints | 1 request per second |
| **Custom OAuth profiles** | All | All [Custom OAuth profiles](/en/workato-api/custom-oauth-profiles.html#create-custom-oauth-profile) endpoints | 60 requests per minute |
| **Data pipelines** | All | All [Data pipelines](/en/workato-api/data-pipelines.html) endpoints | 60 requests per minute |
| **Data tables** | GET, POST | Read endpoints: [Query records](/en/workato-api/data-tables.html#query-records), [Download file from the record](/en/workato-api/data-tables.html#download-file-from-the-record), [Describe uploaded file](/en/workato-api/data-tables.html#describe-uploaded-file) | 100 requests per second |
| **Data tables** | POST, PUT, DELETE | Write endpoints: [Create record](/en/workato-api/data-tables.html#create-record), [Update record](/en/workato-api/data-tables.html#update-record), [Delete record](/en/workato-api/data-tables.html#delete-record), [Generate link to upload file](/en/workato-api/data-tables.html#generate-link-to-upload-file), All other [Record import](/en/workato-api/data-tables.html#record-import-apis) endpoints | 20,000 values per second |
| **Data tables** | All | All other [Data tables](/en/workato-api/data-tables.html) endpoints | 60 requests per minute |
| **Environment management** | All | All [Environment management](/en/workato-api/environment-management.html) endpoints | 60 requests per minute |
| **Environment properties** | All | All [Environment properties](/en/workato-api/account-properties.html) endpoints | 60 requests per minute |
| **Environment roles** | All[](/en/workato-api/environment-roles.html) | All [Environment roles](/en/workato-api/environment-roles.html) endpoints | 60 requests per minute |
| **Event streams** | All | All [Event streams](/en/workato-api/event-streams.html) endpoints | 60 requests per minute |
| **Event streams** | All | All [Event streams](/en/workato-api/event-streams.html) endpoints | Maximum payload size:​ 1 MB |
| **Event streams public API** | All | All [Event streams public API](/en/workato-api/pubsub.html) endpoints | 60 requests per minute |
| **Event streams public API** | All | All [Event streams public API](/en/workato-api/pubsub.html) endpoints | Maximum payload size:​ 10 MB |
| **Folders** | All | All [Folders](/en/workato-api/folders.html) endpoints | 60 requests per minute |
| **Jobs** | POST | Repeat jobs: [/api/recipes/:recipe\_id/repeat\_jobs](/en/workato-api/jobs.html#repeat-jobs) | 25 jobs per request |
| **Jobs** | POST | Repeat jobs: [/api/recipes/:recipe\_id/repeat\_jobs](/en/workato-api/jobs.html#repeat-jobs) | 1 request per second |
| **Jobs** | POST | Cancel jobs: [/api/recipes/:recipe\_id/cancel\_jobs](/en/workato-api/jobs.html#cancel-jobs) | 25 jobs per request |
| **Jobs** | POST | Cancel jobs: [/api/recipes/:recipe\_id/cancel\_jobs](/en/workato-api/jobs.html#cancel-jobs) | 1 request per second |
| **Jobs** | POST | Force an on-demand run of a recipe: [/api/recipes/:recipe\_id/force\_run](/en/workato-api/recipes.html#force-run-a-recipe) | 1 request per second |
| **Jobs** | All | All other [Jobs](/en/workato-api/jobs.html) endpoints | 60 requests per minute |
| **Lookup tables** | POST | Delete lookup tables in batch: [/api/lookup\_tables/batch\_delete](/en/workato-api/lookup-tables.html#lut-delete) | 1 request per second |
| **Lookup tables** | All | All other [Lookup tables](workato-api/lookup-tables.html) endpoints | 60 requests per minute |
| **On-prem** | All | All [On-prem](/en/workato-api/on-prem.html) endpoints | 60 requests per minute |
| **Projects** | All | All [Projects](/en/workato-api/projects.html) endpoints | 60 requests per minute |
| **Project grants** | All[](/en/workato-api/project-grants.html) | All [Project grants](/en/workato-api/project-grants.html) endpoints | 60 requests per minute |
| **Project properties** | All | All [Project properties](/en/workato-api/project-properties.html) endpoints | 60 requests per minute |
| **Project roles** | All[](/en/workato-api/project-roles.html) | All [Project roles](/en/workato-api/project-roles.html) endpoints | 60 requests per minute |
| **Resources** | All | All [Resources](/en/workato-api/static-assets.html) endpoints | 60 requests per minute |
| **Recipes** | POST | Create a recipe: [/api/recipes](/en/workato-api/recipes.html#create-a-recipe) | 1 request per second |
| **Recipes** | POST | Start analyzing recipe health: [/api/recipes/:recipe\_id/health](/en/workato-api/recipes.html#start-analyzing-recipe-health) | 20 requests per minute |
| **Recipes** | All | All other [Recipes](/en/workato-api/recipes.html#get-recipe-details) endpoints | 60 requests per minute |
| **Recipe lifecycle management** | POST | Import a package into a folder: [/api/packages/import/:folder\_id](/en/workato-api/recipe-lifecycle-management.html#import-package-into-a-folder) | 500 requests per hour per user ID. If this quota is exceeded, the system denies additional requests until the following hour when the request allowance resets. |
| **Recipe lifecycle management** | All | All other [Recipe lifecycle management](/en/workato-api/recipe-lifecycle-management.html) endpoints | 60 requests per minute |
| **Legacy roles** | All | All [Legacy roles](/en/workato-api/roles.html) endpoints | 60 requests per minute |
| **Role migration** | All[](/en/workato-api/role-migration.html) | All [Role migration](/en/workato-api/role-migration.html) endpoints | 60 requests per minute |
| **Tag assignments** | All | All [Tag assignments](/en/workato-api/tag-assignments.html) endpoints | 60 requests per minute |
| **Test automation** | All | All [Test Automation](/en/workato-api/test-automation.html) endpoints | 60 requests per minute |
| **Workspace collaborators** | POST | Invite a collaborator: [/api/member\_invitations](/en/workato-api/team.html#invite-collaborator) | 60 requests per minute Additionally, you can send one request per user and workspace ID every 20 minutes to this endpoint. |
| **Workspace collaborators** | All | All other Workspace collaborators endpoints | 60 requests per minute |
| **Workspace details** | All | All [Workspace details](/en/workato-api/users.html) endpoints | 60 requests per minute |
| **Workato Identity IAM** | All | All [Workato Identity IAM](/en/workato-api/workato-identity-iam.html) endpoints | 60 requests per minute |
| **Cross-workspace sharing** | Read | All read [Cross-workspace sharing](/en/workato-api/cross-workspace-sharing.html) endpoints | 600 requests per minute |
| **Cross-workspace sharing** | Write | All write [Cross-workspace sharing](/en/workato-api/cross-workspace-sharing.html) endpoints | 60 requests per minute |

* * *

## Embedded API quotas

View Embedded API quotas

Workato enforces rate limits on Embedded APIs to optimize performance and stability. These quotas apply at the Embed admin workspace level, not at the individual customer workspace level or per API key. This means all API requests from an Embed admin workspace share the same rate limit, regardless of which customer workspace is invoked or which admin API key makes the request. The Embedded API is only accessible from Embed admin workspaces.

Requests made to the Embedded API are subject to the following timeout limit:

| Description | Quota |
| --- | --- |
| Timeout limit | 40 seconds |

In addition, Embedded API resources have the following rate limits:

| Collection | Type | Resource | Quota |
| --- | --- | --- | --- |
| **API clients** | GET | List Developer API Clients: [/api/v2/managed\_users/:managed\_user\_id /developer\_api\_clients](/en/oem/oem-api/api-clients.html#list-developer-api-clients) | 1,000 requests per minute |
| **API clients** | GET | List Developer API Client roles: [/api/v2/managed\_users/:managed\_user\_id /developer\_api\_client\_roles](/en/oem/oem-api/api-clients.html#list-developer-api-client-roles) | 1,000 requests per minute |
| **API clients** | All | All other [API Client](/en/oem/oem-api/api-clients.html) endpoints | 60 requests per minute |
| **API platform** | All | All [API portals](/en/oem/oem-api/api-platform.html#list-api-portals) endpoints | 60 requests per minute |
| **API platform** | All | All [API collections](/en/oem/oem-api/api-platform.html#list-api-collections) endpoints | 1,000 requests per minute |
| **API platform** | All | All [API endpoint](/en/oem/oem-api/api-platform.html#list-api-endpoints) endpoints | 1,000 requests per minute |
| **API platform** | All | All [API clients](/en/oem/oem-api/api-platform.html#list-api-clients) endpoints | 1,000 requests per minute |
| **API platform** | All | All [API access profiles](/en/oem/oem-api/api-platform.html#list-access-profiles) endpoints | 1,000 requests per minute |
| **API platform** | All | All [API certificate bundles](/en/oem/oem-api/api-platform.html#list-certificate-bundles) endpoints | 60 requests per minute |
| **Collaborator groups** | GET | List group project grants: [/api/v2/managed\_users/:managed\_user\_id/ user\_groups/:id/project\_grants](/en/oem/oem-api/collaborator-groups.html#list-collaborator-grants) | 60 requests per minute |
| **Collaborator groups** | All | All other [Collaborator groups](/en/oem/oem-api/collaborator-groups.html) endpoints | 10 requests per second |
| **Connections** | GET | List connections: [/api/managed\_users/:managed\_user\_id /connections](/en/oem/oem-api/connections.html#list-connections) | 1,000 requests per minute |
| **Connections** | All | All other [Connections](/en/oem/oem-api/connections.html) endpoints | 60 requests per minute |
| **Connectors** | All | All [Connectors](/en/oem/oem-api/adapters.html) endpoints | 1,000 requests per minute |
| **Custom connectors** | All | All [Custom connectors](/en/oem/oem-api/custom_connectors.html) endpoints | 60 requests per minute |
| **Custom OAuth profiles** | All | All [Custom OAuth profiles](/en/oem/oem-api/custom-oauth-profiles.html) endpoints | 60 requests per minute |
| **Customer managers** | All | All [Customer managers](/en/oem/oem-api/customer-managers.html) endpoints | 60 requests per minute |
| **Customer workspace collaborators** | All | All [Customer workspace collaborators](/en/oem/oem-api/team.html) endpoints | 60 requests per minute. Additionally, you can send one request per user and workspace ID every 20 minutes to the **Invite collaborator to managed customer workspace** endpoint. |
| **Data retention** | All | All [Data retention](/en/oem/oem-api/data-retention.html) endpoints | 60 requests per minute |
| **Data tables** | GET, POST | Read endpoints: [Query records](/en/oem/oem-api/data-tables.html#query-records), [Download file from the record](/en/oem/oem-api/data-tables.html#download-file-from-the-record), [Describe uploaded file](/en/oem/oem-api/data-tables.html#describe-uploaded-file) | 200 requests per second |
| **Data tables** | POST, PUT, DELETE | Write endpoints: [Create record](/en/oem/oem-api/data-tables.html#create-record), [Update record](/en/oem/oem-api/data-tables.html#update-record), [Delete record](/en/oem/oem-api/data-tables.html#delete-record), [Generate link to upload file](/en/oem/oem-api/data-tables.html#generate-link-to-upload-file), All other [Record import](/en/oem/oem-api/data-tables.html#record-import-apis) endpoints | 40,000 values per second |
| **Data tables** | All | All other [Data tables](/en/oem/oem-api/data-tables.html) endpoints | 60 requests per minute |
| **Dynamic field mapping** | All | All [Dynamic field mapping](/en/oem/oem-api/dynamic-field-mapping.html) endpoints | 60 requests per minute |
| **Environment management** | All | All [Environment management](/en/oem/oem-api/environment-management.html) endpoints | 60 requests per minute |
| **Environment properties** | GET | List properties by prefix: [/api/managed\_users/:managed\_user\_id /properties](/en/oem/oem-api/account-properties.html#list-properties-by-prefix) | 1,000 requests per minute |
| **Environment properties** | All | All other [Environment properties](/en/oem/oem-api/account-properties.html) endpoints | 60 requests per minute |
| **Environment roles** | All[](/en/oem/oem-api/environment-roles.html) | All [Environment roles](/en/oem/oem-api/environment-roles.html) endpoints | 10 requests per second |
| **Event streams** | All | All [Event streams](/en/oem/oem-api/event-streams.html) endpoints | 60 requests per minute |
| **Folders** | All | All [Folders](/en/oem/oem-api/folders.html) endpoints | 60 requests per minute |
| **Jobs** | POST | Repeat jobs: [/api/managed\_users/:managed\_user\_id/recipes /:recipe\_id/repeat\_jobs](/en/oem/oem-api/jobs.html#repeat-jobs) | 25 jobs per request |
| **Jobs** | POST | Repeat jobs: [/api/managed\_users/:managed\_user\_id/recipes /:recipe\_id/repeat\_jobs](/en/oem/oem-api/jobs.html#repeat-jobs) | 1 request per second |
| **Jobs** | POST | Force an on-demand run of a recipe: [/api/managed\_users/:managed\_user\_id /recipes/:recipe\_id/force\_run](/en/oem/oem-api/recipes.html#force-run-a-recipe) | 1 request per second |
| **Jobs** | All | All other [Jobs](/en/oem/oem-api/jobs.html) endpoints | 1,000 requests per minute |
| **JWT Public Key** | All | All [JWT public key](/en/oem/oem-api/jwt-direct-link-configurations.html) endpoints | 60 requests per minute |
| **Legacy roles** | All | All [Legacy roles](/en/oem/oem-api/roles.html) endpoints | 60 requests per minute |
| **Lookup tables** | GET | List rows: [/api/managed\_users/:managed\_user\_id /lookup\_tables/:lookup\_table\_id/rows](/en/oem/oem-api/lookup-tables#list-rows) | 1,000 requests per minute |
| **Lookup tables** | All | All other [Lookup tables](/en/oem/oem-api/lookup-tables.html) endpoints | 60 requests per minute |
| **Manage customers** | POST | Create customer: [/api/managed\_users](/en/oem/oem-api/managed-users.html#create-customer-account) | 1,000 requests per minute |
| **Manage customers** | DELETE | Remove member from customer workspace: [/api/managed\_users/:id/members /:member\_id](/en/oem/oem-api/managed-users.html#remove-member-from-customer-account) | 1,000 requests per minute |
| **Manage customers** | POST | Provision environments: [/api/managed\_users/:id/environments](/en/oem/oem-api/managed-users.html#provision-environments) | 1,000 requests per minute |
| **Manage customers** | All | All [Usage](/en/oem/oem-api/managed-users.html#get-usage-v2) endpoints | 1,000 requests per minute |
| **Manage customers** | All | All other [Members](/en/oem/oem-api/managed-users.html#get-list-of-customer-account-members) endpoints | 60 requests per minute |
| **Manage customers** | All | All other [Manage customers](/en/oem/oem-api/managed-users.html) endpoints | 60 requests per minute |
| **On-prem** | All | All [On-prem](/en/oem/oem-api/on-prem.html) endpoints | 60 requests per minute |
| **Picklists** | All | All [Picklists](/en/oem/oem-api/picklists.html) endpoints | 60 requests per minute |
| **Project grants** | All[](/en/oem/oem-api/project-grants.html) | All [Project grants](/en/oem/oem-api/project-grants.html) endpoints | 60 requests per minute |
| **Project roles** | All[](/en/oem/oem-api/project-roles.html) | All [Project roles](/en/oem/oem-api/project-roles.html) endpoints | 10 requests per second |
| **Projects** | GET | List projects: [/api/managed\_users/:managed\_user\_id /projects](/en/oem/oem-api/project-properties.html#list-projects) | 1,000 requests per minute |
| **Projects** | All | All [Deployments](/en/oem/oem-api/project-properties.html#list-deployments) endpoints | 60 requests per minute |
| **Projects** | All | All other [Projects](/en/oem/oem-api/project-properties.html) endpoints | 60 requests per minute |
| **Recipes** | GET | List recipes in a customer workspace: [/api/managed\_users/:id/recipes](/en/oem/oem-api/recipes.html#list-recipes-in-a-customer-account) | 2,000 requests per minute |
| **Recipes** | GET | Get recipe in a customer workspace: [/api/managed\_users/:id/recipes /:recipe\_id](/en/oem/oem-api/recipes.html#get-recipe-in-a-customer-account) | 2,000 requests per minute |
| **Recipes** | All | All [Recipe versions](/en/oem/oem-api/recipes.html#get-recipe-versions-in-a-customer-workspace) endpoints | 60 requests per minute |
| **Recipes** | All | All other [Recipes](/en/oem/oem-api/recipes.html) endpoints | 1,000 requests per minute |
| **Recipe lifecycle management** | POST | Import package into a customer workspace: [/api/managed\_users/:managed\_user\_id /imports](/en/oem/oem-api/recipe-lifecycle-management.html#package-import) | 1,000 requests per minute |
| **Recipe lifecycle management** | GET | Get status of package import: [/api/managed\_users/:managed\_user\_id /imports/:package\_id](/en/oem/oem-api/recipe-lifecycle-management.html#get-package-status) | 1,000 requests per minute |
| **Recipe lifecycle management** | All | All other [Recipe lifecycle management](/en/oem/oem-api/recipe-lifecycle-management.html) endpoints | 60 requests per minute |
| **Role migration** | All[](/en/oem/oem-api/role-migration.html) | All [Role migration](/en/oem/oem-api/role-migration.html) endpoints | 60 requests per minute |
| **Tag assignments** | All | All [Tag assignments](/en/oem/oem-api/tag-assignments.html) endpoints | 1,000 requests per minute |
| **Test Automation** | All | All [Test Automation](/en/oem/oem-api/test-automation.html) endpoints | 60 requests per minute |

---
