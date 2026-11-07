---
url: 'https://docs.workato.com/en/features/logging-service.md'
description: >-
  Workato Logging Service provides centralized storage to collect, search, and
  filter recipe log entries using the Logger by Workato connector.
---

# Workato Logging Service

Logging is an essential tool for testing, troubleshooting, and debugging. The Workato Logging Service provides centralized storage for collecting and searching through log entries. You can add log entries to recipes by using the [Logger by Workato](#logger-by-workato) connector.

On the Logs page, you can filter logs by recipe ID, by a search term in the log data, and more. For example, you can use the `ERROR` log level to find logs with errors. Refer to [Filter log entries](#filter-log-entries) for more information.

You can also send OPA logs to the Workato Logging Service. Refer to the [on-prem documentation](/en/on-prem/agents/logging#opa-logs-in-logging-service) for more information.

![Example log entry data](/assets/example-log-data.DfN7ah71.png)_Example log entry data_

> **LOG STREAMING**
> 
> Refer to [Audit log streaming](/en/features/activity-audit-log-streaming) to replicate and store log data in one of the following destinations:
> 
> - [Amazon S3 Bucket](/en/features/activity-audit-log-streaming-destinations#amazon-s3-bucket)
> - [Azure Monitor](/en/features/activity-audit-log-streaming-destinations#azure-monitor)
> - [Azure Blob](/en/features/activity-audit-log-streaming-destinations#azure-blob-storage)
> - A [cloud-based logging service](/en/features/activity-audit-log-streaming-destinations#cloud-based-logging-services), such as Sumo Logic, Datadog, Splunk, or [Google Cloud Storage Buckets](/en/features/activity-audit-log-streaming-destinations#google-cloud-storage-buckets)

> **FEATURE AVAILABILITY**
> 
> The **Workato Logging Service** feature is included in specific pricing plans. It includes access to the Logs page and the Logger by Workato connector. Refer to your pricing plan and contract to learn more.
> 
> Your [environment role](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) must include the [Logs privilege](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#tools) to access this feature.

VIDEO GUIDE: WAYS TO USE WORKATO LOGGING SERVICE

[Video](https://www.youtube.com/embed/CbfIoJkFxxU)

## Workato Logging Service use cases

VIDEO GUIDE: TROUBLESHOOT STEPS IN A LOOP FASTER

[Video](https://www.youtube.com/embed/eoiiQMheGpo)

A job report shows only the last execution of a step repeated in a loop in workspaces without full loop visibility. Refer to [Repeat steps](/en/recipes/jobs#repeat-steps). Logging provides visibility into each iteration of [repeated steps](/en/recipes/steps#repeat-step) so you can troubleshoot and debug steps nested within a loop.

Some business objects, such as customer workspaces, are integrated into multiple workflows. Logging allows you to track every time a recipe interacts with a certain customer (for example, customer workspace `ACME Corp`).

## How to access the Logs page

You must have one of the following to view the **Logs** page:

- The [Environment admin](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) role or the legacy [Admin](/en/roles#system-roles) collaborator role.
- The [**Logs** privilege](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#tools).

Complete the following steps to view the logs page:

1. Log in to your Workato account.
   
2. Click **Tools > Logs**.
   
   ![Workato Logging Service](/assets/workato-logging-service.BdhsyaAv.png)_Workato Logging Service_
   

> **OPEN THE LOGS PAGE IN YOUR REGION**
> 
> Each [data center](/en/datacenter/datacenter-overview) is independent, so use the following links to open Workato Logging service for your region:
> 
> Open Workato Logging service using the [data center](/en/datacenter/datacenter-overview) for your region.
> 
> ### Workato Enterprise customers
> 
> - [US Data Center](https://app.workato.com/logs)
> - [EU Data Center](https://app.eu.workato.com/logs)
> - [JP Data Center](https://app.jp.workato.com/logs)
> - [SG Data Center](https://app.sg.workato.com/logs)
> - [AU Data Center](https://app.au.workato.com/logs)
> - [IL Data Center](https://app.il.workato.com/logs)
> - [CN Data Center](https://app.workatoapp.cn/logs)
> - [KR Data Center](https://app.kr.workato.com/logs)
> - [UK Data Center](https://app.uk.workato.com/logs)
> 
> ### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users
> 
> - [Self-service Data Center](https://app.trial.workato.com/logs)

## View log entries

VIDEO GUIDE: HOW TO SEARCH IN LOGS

[Video](https://www.youtube.com/embed/hzJDBEPxaMM)

Complete the following steps to view a log entry on the Logs page:

1. Log in to your Workato account.
   
2. Click **Tools > Logs**.
   
3. Select the log you plan to review.
   
4. _Optional._ Select the **Hide columns** button above the list of logs and uncheck the box next to the column name to hide a column. You can show a column by checking the box next to the column name.
   
   ![Showing columns all columns in the Logs page](/assets/logging-show-hide-columns.D0nfPtsb.png)_Showing all columns in the Logs page_
   

Each log entry contains fields with metadata about when and how the log was created. This information is displayed in columns on the Logs page.

![All columns displayed on the Logs page](/assets/logging-all-columns-displayed-refresh.H20eg0QL.png)_All columns displayed on the Logs page_

### Log columns

| Log column | Description |
| --- | --- |
| Time | The time this log entry was created, according to the workspace's timezone. |
| Log type | The source of the log entry, such as the `Job`, `Polling error` or `OPA`. |
| Log level | Possible log levels are `DEBUG` (OPA logs only), `INFO`, `WARN`, `ERROR`. OPA `TRACE` logs are not currently supported in Logging Service. |
| Data | The [log message](#logger-by-workato) from Logger by Workato. |
| Recipe ID | The recipe ID. |
| Job ID | The job ID. |
| Step number | The step number of the action in the recipe that created this log. |
| Agent | The [on-prem agent](/en/on-prem/agents) that the log originated from. Only OPA versions 23.0 and newer can send logs to the Logging Service, and the [OPA logging feature](/en/on-prem/agents/logging#opa-logs-in-logging-service) must be enabled. |
| On-prem group | The [on-prem group](/en/on-prem/groups) associated with the agent that originated the log. Only OPA versions 23.0 and newer can send logs to the Logging Service, and the [OPA logging feature](/en/on-prem/agents/logging#opa-logs-in-logging-service) must be enabled. |

### Filter log entries

You can filter the log entries by each column listed in the [Log columns](#log-columns) section.

Several filters are shown by default. Select additional filters by clicking the **+** (plus) icon and choosing the filter(s) you plan to display:

![Select filters to display on the Logs page](/assets/logging-select-additional-filters.DBKsqK0N.png)_Select filters to display on the Logs page_

#### Example: Filter entries by data

To filter entries by searching for a term in the **Data** field:

1. Select the **Filter by data** button on the Logs page.
   
   ![The Filter by data button](/assets/logging-filter-by-data-button.bcYPo1Sm.png)_The Filter by data button_
   
2. Enter a search term in the **contains** field that appears.
   
   ![Searching logs by a term in the Data field](/assets/logging-filter-by-data.DpfNnOD8.png)_Searching logs by a term in the Data field_
   
3. Click the checkmark in the **contains** field or type **Enter**.
   
   The Logs page displays only logs that have a **Data** field containing the term you entered.
   
   ![Logs filtered by a term in the Data field](/assets/logging-filter-by-data-result-refresh.9ELG7pVe.png)_Logs filtered by a term in the Data field_
   

### Refresh log entries

Workato's Logging Service includes a **Refresh** button that allows you to manually refresh log entries instead of waiting for automatic log updates. This feature reduces wait times and provides you with quicker access to the latest log information.

![Refresh button](/assets/refresh-button.DB1q2IKa.png)_Refresh button_

## Trigger error logging

You can view error logging to help you understand why a trigger error occurs. Error logging enables you to troubleshoot recipe triggers effectively. Trigger errors can occur for various reasons, including issues with [polling](/en/features/logging-service#polling-errors), webhooks, or [trigger filters](/en/features/logging-service#trigger-filter-errors). Identifying and resolving these errors is crucial for maintaining the functionality of your recipes.

![Filter errors](/assets/filter-error.DikIf0VH.png)_Filter errors_

> **TRIGGER ERRORS VISIBILITY**
> 
> A job isn't generated for a recipe when a trigger error occurs. This means that there is no job ID, and no entry is created in the job history table. These errors are only visible on the logging service page. Data-related errors don't generate a prompt or notification because no job was generated.

### Trigger filter errors

Trigger filter errors occur when the conditions set in the trigger filters are invalid or when the data does not match the expected format.

Trigger filter errors are logged automatically. Automatic logging helps diagnose and troubleshoot issues related to trigger filters effectively.

### Polling errors

Polling errors occur in three main conditions:

- When a poll request fails
- When the poll response cannot be parsed successfully
- When the fetched data size exceeds the trigger event size quota of 50 MB

The following example displays log data for a polling error due to a timeout issue:

![Polling errors](/assets/polling-error.BMhyosQh.png)_Polling errors_

### Webhook errors

Webhook errors occur when there is an issue with accepting or processing a webhook event. These errors can occur for various reasons, such as an invalid request, incorrect URL, or server issues. Addressing webhook errors is essential to ensure the reliability of your webhook-based triggers.

There are two types of webhook errors:

- Webhook Gateway errors
  
- These errors occur at the gateway level, typically due to rate limiting, verification failures, or invalid requests. These errors prevent the webhook event from reaching the processing stage.
  
- Webhook Processing errors
  
- These errors occur during the processing of the webhook event after it has been accepted by the gateway. These can be due to data parsing issues, processing logic failures, or downstream service errors.
  

Both types of webhook errors are logged automatically and handled similarly.

The following example displays log data for a webhook error:

![Webhook errors](/assets/webhook-error.BGVYPWb7.png)_Webhook errors_

Refer to the Webhooks connector [Debug common errors](/en/connectors/workato-webhooks/common-errors) page for more troubleshooting information.

## Log entry details

1. Click the log entry to expand the log data. This displays the full log message.
   
2. Enter a search term in the **Data** field of the log entry to refine your search.
   
   ![Log entry data](/assets/log-data.B8tcS7D1.png)_Log entry data_
   
   > **INPUT AND OUTPUT MESSAGE FIELD BEHAVIOR**
   > 
   > The input and output message fields contain the same data for log entries. The message field under output contains the data for both the input and output fields, leaving the input field empty.
   

## Add log entry with Logger by Workato

1. Log in to your Workato account.
   
2. Go to **Projects**.
   
3. Click **Create > Recipe** or press C+R to create a new recipe, or click an existing recipe and select **Edit recipe**.
   
4. Click the **+** (plus) button under **Actions** to add a new step.
   
5. Select **Action in an app**.
   
6. Search for and select **Logger by Workato**.
   
7. Customize the content of your log message by filling out the **Message** field. You can insert datapills into this field.
   
8. Toggle **Send to Workato log service** and select the log level. The Logger by Workato connector supports the log levels `INFO`, `WARN`, and `ERROR`.
   
   This creates a log entry for every job, including test jobs.
   
   ![Logger by Workato](/assets/logger-by-workato.Dtad2E18.png)_Logger by Workato_
   

> **MONITOR RECIPE JOBS IN REAL-TIME WITH LOGS**
> 
> The Logs page is updated as each log step is completed. This means that you do not need to wait for the entire recipe job to finish processing before viewing the logs. This enables you to track the real-time progress of long running recipes.

## Add log entries from OPA

You can send logs to the Logging Service if you use OPA versions 23.0 or newer and have the **Send to Workato logs** setting enabled. To enable this setting:

1. Log in to your Workato account.
   
2. Click **Tools > On-prem groups > Settings > Log management**.
   
3. Enable the **Send to Workato logs** setting. Note that this setting is disabled by default. Refer to the [on-prem documentation](/en/on-prem/agents/logging#opa-logs-in-logging-service) for more information.
   

![OPA logs in the Workato Logging Service](/assets/opa-logs-detail.2xSlcLCh.png)_OPA logs in the Workato Logging Service_

## Log encryption

Logs are encrypted at rest and in transit with a unique encryption key for each workspace and environment (if applicable).

Check out how it works with Workato's [Encryption Key Management](/en/security/data-protection/encryption-key-management/).

## Log quotas

Each log entry has a maximum retention period of 30 days or 1 million entries. This quota is independent of the [customized retention periods](/en/security/data-protection/data-retention/#customize) for other components in your workspace. You can [stream logs to an external destination](/en/features/activity-audit-log-streaming) to maintain logs beyond this retention period.

In each workspace or environment, every log type source has a retention quota of 1,000,000 log entries. This retention quota prevents the logging service from being overloaded and ensures that older logs do not displace newer ones. When this threshold is reached, the system deletes the oldest entries for that specific log type source to make space for incoming logs.

**Log entry quota exceeded**

#### Scenario 1: Exceeding log entry quota

Consider the following scenario. Within a week the following activities occur in your environments:

- Your dev environment created 1,250,000 log entries.
- Your test environment created 1,000,000 log entries.
- Your production environment created 500,000 log entries.

Your logs page displays:

- In your dev environment, only the most recent 1,000,000 log entries.
- In your test environment, all 1,000,000 log entries.
- In your production environment, all 500,000 log entries.

**Log retention period exceeded**

#### Scenario 2: Exceeding log retention period

Consider the following scenario. Your workspace created 10,000 log entries on January 1, 2023 and 18,000 log entries on February 1, 2023.

If you view the Logs page on February 15, 2023, you only see the 18,000 log entries that were created on February 1, 2023. The 10,000 log entries created on January 1, 2023 have been deleted due to the maximum retention period of 30 days.

### Size quotas

The data column for each log entry has a maximum quota of 10 KB. Once the quota is exceeded, the contents are truncated.

### Character encoding

UTF-8 character encoding is used in log entries and international characters are supported (e.g. "こんにちは世界!").

---
