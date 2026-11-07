---
url: 'https://docs.workato.com/en/features/activity-audit-log-streaming.md'
description: >-
  Set up audit log streaming in Workato to replicate and store log data in an
  external destination beyond standard retention periods.
---

# Audit log streaming

Audit log streaming replicates and stores log data in a destination you specify. This lets you maintain access to logs beyond the [audit log](/en/features/activity-audit-log#log-retention) and [Workato logging service](/en/features/logging-service#log-limits) retention periods and ensures you have ample time to review and analyze your activity logs for security and operational insights.

Each job or event is represented as a JSON file, which Workato sends to the log provider using the HTTP POST method. Workato supports the following destinations:

- [Amazon S3 Bucket](/en/features/activity-audit-log-streaming-destinations#amazon-s3-bucket)
- [Azure Monitor](/en/features/activity-audit-log-streaming-destinations#azure-monitor)
- [Azure Blob](/en/features/activity-audit-log-streaming-destinations#azure-blob-storage)
- A [cloud-based logging service](/en/features/activity-audit-log-streaming-destinations#cloud-based-logging-services), such as Sumo Logic, Datadog, Splunk, or [Google Cloud Storage Buckets](/en/features/activity-audit-log-streaming-destinations#google-cloud-storage-buckets)

Refer to [Audit log streaming destinations](/en/features/activity-audit-log-streaming-destinations) for more information.

> **FEATURE AVAILABILITY**
> 
> Audit log streaming is available on specific pricing plans. Refer to your pricing plan and contract to learn more.

## Audit log size

Log file size varies from 1 KB to 1 MB based on the details that are present in the logs.

The file size quota for logs is 40 MB.

When streaming full job details, the system does not send step-specific log lines if the overall file size exceeds 40 MB. If a file exceeds 40 MB, the system still sends contextual job information, such as `user_id`, `recipe_id`, and `time_executed`. However, the “lines” column displays the default text, `Log lines exceed size limit`.

## Set up audit log streaming

1. Sign in to your Workato account.
   
2. Go to **Workspace admin > Settings > [Log streaming](https://app.workato.com/members/settings/log_streaming)** and select **Set up audit log streaming**:
   
   ![Enable audit log streaming](/assets/enable-audit-log-streaming.DYpo11KE.png)
   
3. Select the audit log destination.
   
4. Configure the streaming connection and options.
   
5. Choose the events to include in your audit log stream.
   
   Consult [Audit log streaming types](/en/features/activity-audit-log-streaming-sample#audit-log-streaming-types) for more information about events.
   
6. Optional. [Customize a log message](/en/features/activity-audit-log-streaming-customize-log) if required.
   
7. Select **Save**.
   

## Does data masking apply to audit log streaming?

Yes. When data masking is enabled, Workato doesn't log or stream the input or output of any trigger or action. Instead, a placeholder replaces the data in both:

- **Workato UI logs**
- **Audit log streaming destinations**

Refer to the [Enable data masking](/en/features/data-masking#enable-data-masking) section for instructions on enabling this feature.

### How masked data appears in job logs

When job logs are streamed to an external logging service through audit log streaming, masked data remains hidden. Instead of displaying sensitive information, Workato replaces it with a `"masked"` placeholder.

The following example illustrates how masked data appears in a job details log:

```json
"lines": [
    {
        "input": {"data": "masked"},
        "output": {"data": "masked"},
        "adapter_name": "timer",
        "adapter_operation": "trigger_event",
        "line_stat": {
            "details": [
                {
                    "name": "execution_time",
                    "average": 0.002,
                    "total": 0.002,
                    "min": 0.002,
                    "max": 0.002,
                    "count": 1
                }
            ],
            "total": 0.002
        },
        "recipe_line_number": 1,
        "mask_data": true
    }
]
```

Refer to the [Activity audit log file details and sample data](/en/features/activity-audit-log-streaming-sample#full-job-details) section for a complete example of a job details log.

---

---
url: >-
  https://docs.workato.com/en/features/activity-audit-log-streaming-customize-log.md
description: >-
  Customize Workato audit log messages with JSON and placeholders before
  streaming them to destinations like Amazon S3, Splunk, or Datadog.
---

# Custom log messages

You can customize audit log messages before streaming them to external destinations like Amazon S3, Splunk, or Datadog.

For example, a customized log message can include the source application and environment metadata so that event logs are automatically processed in the destination application.

## Create a custom log message

Complete the following steps to create a custom log message:

1. Go to **Workspace admin > Settings > Log streaming**.
   
2. Locate the **Customize log message** field and enter a custom log message using JSON. You can also use [placeholders](#placeholders) to define the JSON structure. Workato replaces placeholders with actual log messages before streaming the event.
   
   ![Customize the log message](/assets/customize-log-message.CiaX9tKN.png)_Customize the log message_
   
3. Click **Save**.
   

## Supported placeholders

Workato supports the following placeholders:

| Placeholder | Description | Example |
| --- | --- | --- |
| `{{{log_message}}}` | Audit log event message as JSON | [See examples](/en/features/activity-audit-log-streaming-sample#json-file-content-sample-data) |
| `{{{log_message_str}}}` | Audit log event message as an escaped JSON string. **Required for logs sent to [Grafana Loki](#loki-log-example).** | [See example](/en/features/activity-audit-log-streaming-sample#example-log-message-str) |
| `{{{now}}}` | Timestamp | `2023-06-02T01:30:01.002-04:00` |
| `{{{now_utc}}}` | Timestamp in milliseconds | `1685683801002.2139` |
| `{{{now_utc_micro}}}` | Timestamp in microseconds | `1685683801002213` |
| `{{{now_utc_nano}}}` | Timestamp in nanoseconds | `1685683801002214000` |

> **JSON KEYS**
> 
> Currently, if you're using the placeholders in a JSON object, each key must match the name of the placeholder in the value. For example, if you use the placeholder `{{{log_message_str}}}`, you must give it the key `"log_message_str"`:
> 
> ```json
> {
>  "log_message_str": {{{log_message_str}}},
>  "now_utc_micro": {{{now_utc_micro}}}
> }
> ```

## Example custom log message

In the following example, we send the `source`, `environment`, and `service` fields to Datadog so that the message is automatically routed and stored in the correct bucket.

The `{{{log_message}}}` is the placeholder that Workato uses to substitute the actual audit log event message in JSON format.

```json
{
  "source": "workato",
  "environment": "staging",
  "hostname": "workato_cloud",
  "service": "emp_onboarding",
  "log_message": {{{log_message}}}
}
```

> **VALID JSON REQUIRED**
> 
> Make sure you define valid JSON. If the JSON is invalid or does not contain either the `{{{log_message}}}` or `{{{log_message_str}}}` placeholder, then Workato will send the default log message without any customization.

The following images show what the log message looks like in the Datadog log explorer.

![Custom audit log message fields](/assets/custom-audit-log-message.B6wnceTi.png)_Custom audit log message fields_

![Custom audit log message for recipe started event](/assets/custom-recipestarted-audit-log-message.Ds0dEigi.png)_Custom recipe started activity audit log message_

![Custom audit log message for a successfully completed job](/assets/custom-job-history-audit-log-message.BCU4w6Zk.png)_Custom job history audit log message_

## Example custom log message for Grafana Loki

The [Grafana Loki HTTP API](https://grafana.com/docs/loki/latest/api/#push-log-entries-to-loki) requires the log message to be sent as a string, so you must use the `{{{log_message_str}}}` placeholder instead of `{{{log_message}}}`.

The Loki API also expects a nanosecond timestamp formatted as a string. Use the `"{{{now_utc_nano}}}"` placeholder surrounded by double quotes to ensure the timestamp is converted to a string.

Format the JSON structure for the custom audit log message as follows:

```json
{
  "streams": [
    {
      "stream": {
        "label": "workato"
      },
      "values": [
          ["{{{now_utc_nano}}}", {{{log_message_str}}}]
      ]
    }
  ]
}
```

Example custom log message sent to Loki:

```json
{
 "streams": [
  {
   "stream": {
    "label": "workato"
   },
   "values": [
    [
     "1685687453790827508",
     "{\"event\":\"recipe_started\",\"details\":{\"run_once\":false,\"request\":{\"ip_address\":\"76.100.203.123\",\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36\"}},\"user\":{\"id\":1234567,\"external_id\":null,\"email\":\"example.user@workato.com\",\"name\":\"Example User\",\"environment_id\":1234567,\"environment_type\":\"dev\",\"account_id\":1234567,\"account_name\":\"Example User\"},\"team\":{\"id\":1234567,\"external_id\":null,\"email\":\"example.user@workato.com\",\"name\":\"Example User's team\",\"environment_id\":1234567,\"environment_type\":\"dev\",\"account_id\":1234567,\"account_name\":\"Example User\"},\"resource\":{\"type\":\"Flow\",\"id\":16983123,\"name\":\"Cat Fact Generator\",\"path\":\"Home/AI Testing\",\"folder_id\":9020123},\"timestamp\":\"2023-06-02 06:30:53 UTC\"}"
    ]
   ]
  }
 ]
}
```

---

---
url: >-
  https://docs.workato.com/en/features/activity-audit-log-streaming-destinations.md
description: >-
  Configure audit log streaming destinations in Workato, including Amazon S3,
  Azure Monitor, Azure Blob Storage, and Google Cloud Storage.
---

# Audit log streaming destinations

Before you begin, refer to our [set up audit log streaming](/en/features/activity-audit-log-streaming) guide for instructions on enabling audit log streaming in your workspace.

Workato supports cloud connections to the following audit log streaming destinations:

- [Amazon S3 Bucket](#amazon-s3-bucket)
- [Azure Monitor](#azure-monitor)
- [Azure Blob Storage](#azure-blob-storage)
- [Cloud based logging services](#cloud-based-logging-services)
- [Google Cloud Storage Bucket](#google-cloud-storage-buckets)

## Amazon S3 Bucket

To stream your audit logs to Amazon S3, select an existing Amazon S3 connection or create one that has a region and bucket set up. This connection must be assigned an IAM role with the following policy permissions:

- `ListAllMyBuckets`: This list permission allows Workato to list all buckets belonging to your S3 account. This permission is required even if your connection is restricted to one bucket within S3.
- `PutObject`: This write permission allows Workato to stream your activity audit logs to the bucket you specify during setup.

![Minimum S3 permissions for ALS](/assets/als-s3-permissions-policy.CbZqLwlp.png)_Minimum permissions for audit log streaming to S3_

To ensure the audit logs are streamed successfully, confirm that your Amazon S3 connection meets the following requirements:

- The specified S3 bucket must exist.
- The region specified in the S3 connection must match the region of the selected bucket.
- The IAM role ARN (Amazon Resource Name) associated with the S3 connection must be valid.
- The IAM role must have the `ListAllMyBuckets` and `PutObject` permissions.
- Use a cloud connection, not an [on-prem connection](/en/on-prem/agents).
- Allowlist Workato's [data center IP addresses](/en/security/ip-allowlists) if you use an IP allowlist to secure your storage.

Learn more about setting up an IAM role and permissions policy in our [IAM role-based authentication](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws) documentation.

> **IAM ROLE PERMISSIONS**
> 
> When you update your IAM role bucket permissions, you must disconnect and re-establish your S3 connection in Workato before you can continue using S3 as a streaming destination. This is a security feature designed to help you manage secure access to your resources.
> 
> Additionally, if you plan to restrict access to a specific bucket within S3, you must configure this setting when you [set up your S3 connection](/en/connectors/s3#connection-setup).
> 
> The IAM role must be configured at the bucket level and _not_ at the `bucket/object` level.

## Azure Monitor

Complete the following steps to stream your audit logs to Azure Monitor:

> **SHARED KEY DEPRECATED**
> 
> Shared key authentication method uses the legacy [HTTP Data Collector API](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-collector-api), which is deprecated and will stop working in September 2026. Migrate to client credentials authentication instead.

1. Use the **Audit log destination** drop-down menu to select **Azure Monitor**.
   
2. Click **Set up connection**.
   
3. **Client credentials authentication**
   
   1. Select an existing connection or refer to the [Azure Monitor](/en/connectors/azure_monitor) guide to create a new connection. Save the **Immutable ID** and the **Data source** name (stream name) from the [Create a data collection rule and assign permissions](/en/connectors/azure_monitor#register-app-client-creds) step for later use.
      
      > **CONNECTION REQUIREMENTS**
      > 
      > Ensure the connection to Azure Monitor meets the following requirements:
      > 
      > - Use a cloud connection, not an [on-prem connection](/en/on-prem/agents).
      > - Allowlist Workato's [data center IP addresses](/en/security/ip-allowlists) if you use an IP allowlist to secure your storage.
      
   2. Enter the **Immutable ID** of your workspace's data collection rule in the **Azure Data Collection Rule ID** field.
      
   3. Enter the name of the stream your data collection rule uses as a data source in the **Azure Stream Name** field.
      
   4. Optional. Enter a name in the **Log Type** field to automatically create a new table for the logs. This field only supports letters, numbers, and underscores (`_`), and may not exceed `100` characters.
      
   
   **Shared key authentication**
   
   1. Select an existing connection or refer to the [Azure Monitor](/en/connectors/azure_monitor) guide to create a new connection.
      
      > **CONNECTION REQUIREMENTS**
      > 
      > Ensure the connection to Azure Monitor meets the following requirements:
      > 
      > - Use a cloud connection, not an [on-prem connection](/en/on-prem/agents).
      > - Allowlist Workato's [data center IP addresses](/en/security/ip-allowlists) if you use an IP allowlist to secure your storage.
      
   2. Enter a name in the **Log Type** field to automatically create a new table for the logs. This field only supports letters, numbers, and underscores (`_`), and may not exceed `100` characters.
      
   
4. Optional. Enter a **Resource ID** to associate the logs with a specific Azure resource.
   
5. Select the events to stream:
   
   - **Job status only**: Logs whether a job succeeded or failed.
   - **Full job details**: Logs job details, including status and data for each line action.
   - **User activity**: Logs all user activity in the workspace.
   - **API platform logs**: Logs all API requests handled by the API platform.
   - **Workato Log events**: Logs all messages sent to the Workato logging service.
   - **Genie conversations**: Logs the full details of genie conversations, including data for every response.
   
   Additionally, select the **Log types** and **Log levels** to include if you plan to stream events from the [Workato logging service](/en/features/logging-service).
   
6. Optional. Enter the logging message you plan to use in the **Customize log message** field. Refer to the [Custom log messages](/en/features/activity-audit-log-streaming-customize-log) guide for more information.
   
7. Click **Save** to apply your audit log streaming settings.
   
8. Ensure your Azure Monitor Workspace receives the audit logs by querying the specified log type.
   
   ![Verify your audit logs](/assets/verify-logs.wHU3iO_v.png)_Verify your audit logs_
   

## Azure Blob Storage

Select an Azure Blob connection that has containers set up. The connection should have read/write access to the containers. Reference our [Azure blob documentation](/en/connectors/azure_blob_storage#create-an-auth-code-grant-isu) to learn how to change role access of the Integration System User (ISU) in Microsoft Entra ID. Azure charges [additional fees](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/#pricing) for every 10,000 logs streamed to Azure Blob.

> **CONNECTION REQUIREMENTS**
> 
> Ensure the connection to Azure Blob Storage meets the following requirements:
> 
> - Use a cloud connection, not an [on-prem connection](/en/on-prem/agents).
> - Allowlist Workato's [data center IP addresses](/en/security/ip-allowlists) if you use an IP allowlist to secure your storage.

## Cloud based logging services

You can use any log service provider (such as Sumo Logic, Datadog, or Splunk) as a streaming destination. Learn more about configuring an HTTP based log collection using [Sumo Logic](https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/HTTP-Source) or [Datadog](https://docs.datadoghq.com/logs/log_collection/?tab=httpussite).

### How to use a cloud based logging service destination

Go to the **Destination URL** field and enter the HTTP URL from your cloud-based logging service provider. Workato audit log streaming posts the audit log events in real-time to this URL.

If your log service provider requires authentication to send HTTP requests, enable the **Requires authentication** slider, then select the **Link your account** button to specify an HTTP connection with your authentication information. You can create a new HTTP connection or link to an existing connection.

![Link an HTTP connection](/assets/link-your-account.BPurmmNo.png)_Link to an HTTP connection_

> **SUPPORTED AUTHENTICATION METHODS FOR HTTP CONNECTIONS**
> 
> When setting up the HTTP connector for log streaming, ensure that you use one of the following authentication methods:
> 
> - Basic
> - Query
> - `oauth2_auth_code_grant`
> - `oauth2_client_credentials_grant`
> - Custom
> 
> Note that audit log streaming to REST-based destinations is only compatible with the preceding listed authentication methods. You will not be able to successfully configure streaming if you use another authentication method.
> 
> ![Validation failed](/assets/validation-failed.-uJ9rrlc.png)_Validation failed_

## Google Cloud Storage Buckets

You can stream your audit logs from Workato to a Google Cloud Storage Bucket. Complete the steps in the following sections to configure the log streaming connection.

### Prerequisites

You must have the following features and access:

- A Workato account with the [Audit Log Streaming](/en/features/activity-audit-log-streaming#audit-log-streaming) feature enabled
- Access to the following Google Cloud products and services:
  - Cloud Logging
  - Google Cloud Storage Buckets
  - Roles & IAM
  - API’s & Services
- Google Oauth2 playground (for troubleshooting)
- Use a cloud connection, not an [on-prem connection](/en/on-prem/agents).
- Allowlist Workato's [data center IP addresses](/en/security/ip-allowlists) if you use an IP allowlist to secure your storage.

### Enable Google Cloud Logging API

You must enable the following API to send logs to a Google Cloud Platform (GCP) instance. Refer to the Google documentation on how to [enable an API](https://cloud.google.com/endpoints/docs/openapi/enable-api) for more information.

Complete the following steps to enable Cloud Logging API:

1. Sign in to your Google Cloud Console.
   
2. Go to **Enabled API's & Services**.
   
3. Search for `Cloud Logging API` and ensure that is enabled.
   

### Create a user account

You must create a connection to your GCP instance using a shared user account or assign an individual with permissions to write logs to your Google Cloud Storage Bucket. This user must be in your organization’s directory with a valid email address. Use this account to authenticate the integration between Workato and GCP in the OAuth 2.0 workflow. Refer to the Google documentation on how to [add users](https://support.google.com/cloudidentity/topic/7558418) for more information.

### Assign user account role permissions

The user account you plan to use for authentication must be granted the required roles and permissions. Refer to the Google documentation on how to [grant a role](https://cloud.google.com/iam/docs/manage-access-service-accounts#single-role) for more information.

Complete the following steps to assign required permissions to your user account:

1. Sign in to your Google Cloud Console.
   
2. Go to **Google Cloud Logging > Permissions > Assign Principal**.
   
3. Select the account you created in the previous section, then assign the **Logging Admin** role.
   
4. Go to **Google Cloud Buckets** and select the bucket in which you plan to store Workato logs, or create a new bucket if necessary.
   
5. Go to **Permissions > Assign Principal**, select the user account, and then assign the **Storage Object Admin** role.
   

### Configure an OAuth consent screen

You must configure an OAuth consent screen before you create your OAuth application.

Complete the following steps to configure your OAuth consent screen:

1. Sign in to your Google Cloud Console.
   
2. Select the **project ID** in which you plan to stream your activity logs.
   
3. Go to **APIs & Services**.
   
4. Go to the **OAuth Consent Screen** configuration page and select **Credentials**.
   
5. Go to **Authorized domains > click Add Domain** > and enter `workato.com`.
   
   ![Add the Workato domain](/assets/add-workato-domain.DVXjME7X.png)_Add the Workato domain_
   
6. Select **Scopes for Google APIs**.
   
7. Click **Add scope**.
   
8. Ensure that you have the following Cloud Logging API scopes:
   
   - `.../auth/logging.admin`
   - `.../auth/logging.read`
   - `.../auth/logging.write`
   
   ![Add scopes](/assets/google-cloud-api-scopes.BsX_KJYc.png)_Required API scopes_
   
9. Click **Add > Submit for verification**.
   

### Create an external OAuth app

You must create an OAuth application in your GCP instance to generate a `clientID` and `clientSecret`. This enables Workato to use the Google Cloud Logging APIs you enabled in the previous section.

Complete the following steps to create an external OAuth app:

1. Sign in to your Google Cloud Console.
   
2. Go to **APIs & Services > Credentials > Create Credentials > OAuth Client ID**.
   
3. Select **Application Type**, then enter a name for the app. We recommend that you name your app `Workato - GCP Integration - US`.
   
4. Enter the following as the authorized redirect URI: `https://www.workato.com/oauth/callback`.
   
5. Click **Create**. A `clientID` and `clientSecret` are automatically generated after your app is created. We recommend that you download the JSON file for safekeeping.
   
6. Go to **APIs & Services > OAuth Consent Screen**.
   
7. Use the form to register the app and include `workato.com` in the list of authorized domains. Note that you can use any user account for the developer contact information.
   
8. Click **Save and Continue**.
   

### Create a HTTP connection with OAuth2 authorization code grant

Complete the following steps to create an HTTP connection with OAuth2 authorization code grant:

1. Sign in to your Workato account.
   
2. Go to **Projects > Connections**.
   
3. Click **Create > Connection** (or press C twice), then search for and select HTTP as your connector.
   
4. Provide a name for your connection in the **Connection name** field.
   
5. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
6. Use the **Connection type** drop-down menu to select **Cloud**. On-prem HTTP connections don't support log streaming.
   
7. Use the **Authentication type** drop-down menu to select **OAuth2 authorization code grant**.
   
8. Enter the following URL in the **OAuth2 authorization URL field**: `https://accounts.google.com/o/oauth2/token` and input the authorization URL: `https://accounts.google.com/o/oauth2/auth?response_type=code&scope=https://www.googleapis.com/auth/cloud-platform&access_type=offline&prompt=consent`
   
9. Enter the **OAuth2 Client ID** that you generated in the preceding section.
   
10. Enter the **OAuth2 Client Secret** that you generated in the preceding section.
    
11. Use the **How does the API require credentials to be sent to request a token?** drop-down menu to select **Header**.
    
12. Click **Connect**. An OAuth consent dialogue box opens and prompts you to authenticate your request.
    
13. Click **Continue**.
    
14. Enter the user account email address and password.
    
15. Select **Allow** to enable Workato to connect to your Google Cloud Logging instance.
    

### Configure audit log streaming

Complete the following steps to stream your audit logs to Google Cloud:

1. Sign in to your Workato account.
   
2. Go to **Workspace admin > Settings > Debug and logs > Log streaming**.
   
   ![Go to log streaming](/assets/go-to-log-streaming.CZXjZMvW.png)_Go to Log streaming_
   
3. Click **Set up audit log streaming**.
   
4. Use the **Audit log destination** drop-down menu to select **Cloud based logging service**.
   
   ![External log provider](/assets/external-log.CyDnx8VX.png)_Configure your logs to stream to an external log provider_
   
5. Enter the following URL as your **Audit log destination**: `https://logging.googleapis.com/v2/entries:write`.
   
6. Select the **Requires authentication** toggle.
   
7. Click **Set up connection**, then use the **Existing connections** drop-down menu to select the connection you set up in the preceding section.
   
   ![Go to Existing connections](/assets/go-to-log-streaming.CZXjZMvW.png)_Select the connection from Existing connections_
   
8. Go to the **Choose events to stream** section and select the checkboxes for the events you plan to stream.
   
9. Enter the logging message you plan to use in the **Customize log message** field.
   
   > **REQUIRED FORMAT**
   > 
   > Google Cloud Logging expects JSON payloads in a specific format. We recommend that you include the following message format in your log message. Replace the project name and the log name with your own values.
   > 
   > ```json
   > {
   >   "logName" : "projects/your-project-name/logs/workato-logs",
   >   "resource": { "type": "gce_instance"},
   >  "entries": [
   >   {
   >    "jsonPayload": {
   >     "data": {{{ log_message }}}
   >    }
   >   }
   >  ]
   > }
   > ```
   
10. Click **Save**. Your logs are now configured to flow into your default bucket.
    

### Create a log sink to route logs to a specific GCP Bucket

You must create a log sink to route logs to a specific GCP bucket.

> **HOURLY BATCH PROCESSING FOR LOGS**
> 
> Logs are routed from the default cloud logging to the destination in hourly batches.

Complete the following steps to create a log sink:

1. Sign in to your Google Cloud Console.
   
2. Go to **Cloud Logging Explorer > Log Router > Create Sink**.
   
3. Provide a **Sink name**, such as `Workato to GCP`, then click **Next**.
   
   ![Create a sink](/assets/sink.BfZqzN7D.png)_Create a sink_
   
4. Use the **Select sink service** drop-down menu to select **Google Cloud Bucket**.
   
5. Click **Browse** to locate and select the Google Cloud Bucket you plan to use, then click **Next**.
   
6. Choose the logs you plan to include in the router by entering the log name in the **Inclusion filter** field and then click **Next**.
   
7. Click **Create Sink**.
   
   ![Bucket details](/assets/bucket-details.Cr0Vtl88.png)_Google Cloud Bucket details_
   

### Troubleshooting

Complete the following steps to troubleshoot your log streaming:

1. Go to [https://developers.google.com/oauthplayground/](https://developers.google.com/oauthplayground/)
   
2. Find and authorize **Cloud Logging API v2**.
   
3. Sign in using the user account credentials for your Google Cloud Bucket. This automatically generates an access token.
   
4. Configure the `POST` request with the following message format, replacing the names with your GCP instance values:
   
   ```json
   
   {
   
     "logName" : "projects/your-project-name/logs/your-log-name",
   
     "resource": { "type": "gce_instance"},
   
    "entries": [
   
     {
   
      "jsonPayload": {
   
       "data": "hello world"
   
      }
   
     }
   
    ]
   
   }
   ```
   
5. Go to Google Logs Explorer and run a query to check for `logName = {your-log-name}`, replacing the values with the GCP information you configured.
   
   > **LOG MISSING**
   > 
   > If you do not see a log, the `POST` request may have failed. Check the error response code in your `POST` request to view the exact error. If you receive a permissions error, check that your user account has the required permissions.
   

> **ADDITIONAL TROUBLESHOOTING**
> 
> Ensure the connection to your streaming destination meets the following requirements:
> 
> - Use a cloud connection, not an [on-prem connection](/en/on-prem/agents).
> - Allowlist Workato's [data center IP addresses](/en/security/ip-allowlists) if you use an IP allowlist to secure your storage.

---
