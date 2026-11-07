---
url: 'https://docs.workato.com/en/ahq-audit-log-streaming.md'
description: >-
  Set up audit log streaming in Automation HQ to send logs from all current and
  future managed workspaces to a single external log provider.
---

# Audit log streaming for Automation HQ

Enable an audit log streaming system for your entire organization. This includes all current and future workspaces that Automation HQ manages.

> **INFO**
> 
> You can't modify log settings within managed workspaces.

Automation HQ adapts [Audit log streaming](/en/features/activity-audit-log-streaming#audit-log-streaming) to provide a single logging mechanism and destination for all workspaces in your organization.

_Automation HQ audit log streaming_

Complete the following steps to enable audit log streaming:

1. Go to **Automation HQ**.
   
2. Click the **Settings** tab.
   
3. Click **Set up audit log streaming**. The **Stream logs from all workspaces to an external log provider** interface appears.
   
   _Set up audit log streaming_
   
4. Choose an **Audit log destination** from the drop-down menu. Refer to [Audit log streaming destinations](/en/features/activity-audit-log-streaming-destinations#audit-stream-destination) for more information on destination types.
   
   _Choose audit log streaming destination_
   
5. Use the following tabs to complete the steps for your selected destination:
   
   **Amazon S3 bucket**
   
   Complete the following steps to configure Amazon S3 as your audit log destination:
   
   1. [Create a new connection](/en/connectors/s3#connection-setup) for Amazon S3, or use an existing connection.
      
      _Configure Amazon S3 as your audit log destination_
      
   2. Use the **Choose a bucket** drop-down menu to select a bucket from your Amazon S3 instance.
      
   3. Select the events to stream:
      
      - **Job status only**: Logs whether a job succeeded or failed.
      - **Full job details**: Logs job details, including status and data for each line action.
      - **User activity**: Logs all user activity in the workspace.
      - **API platform logs**: Logs all API requests handled by the API platform.
      - **Workato Log events**: Logs all messages sent to the Workato logging service.
      - **Genie conversations**: Logs the full details of genie conversations, including data for every response.
      
      Additionally, select the **Log types** and **Log levels** to include if you plan to stream events from the [Workato logging service](/en/features/logging-service).
      
   4. Optional. Use the **Customize log message** field to define log messages using JSON format. You can add custom fields and structures. For more details, refer to the [Customize log message](/en/features/activity-audit-log-streaming-customize-log) documentation.
      
   5. Click **Save** to enable streaming to the Amazon S3 bucket.
      
   
   **Azure Monitor**
   
   Complete the following steps to configure Azure Monitor as your audit log destination:
   
   1. Use the **Audit log destination** drop-down menu to select **Azure Monitor**.
      
   2. Click **Set up connection**. Note that the shared key authentication method uses the legacy [HTTP Data Collector API](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-collector-api), which is deprecated and will stop working in September 2026. Migrate to client credentials authentication instead.
      
   3. Select an existing connection or refer to the [Azure Monitor](/en/connectors/azure_monitor) guide to create a new connection. Save the **Immutable ID** and the **Data source** name (stream name) from the [Create a data collection rule and assign permissions](/en/connectors/azure_monitor#register-app-client-creds) step for later use if your authentication type is **Client credentials**.
      
      ![Configure Azure Monitor as your audit log destination](/assets/automation-hq-workspace-settings-configure-azure-monitor.CNanla7K.png)_Configure Azure Monitor as your audit log destination_
      
   4. Complete the following steps if your authentication type is **Client credentials**:
      
      1. Enter the **Immutable ID** of your workspace's data collection rule in the **Azure Data Collection Rule ID** field.
         
      2. Enter the name of the stream your data collection rule uses as a data source in the **Azure Stream Name** field.
         
   5. Enter a name in the **Log Type** field to automatically create a new table for the logs. This field only supports letters, numbers, and underscores (`_`), and may not exceed `100` characters. This field is optional for client credentials authentication.
      
   6. Optional. Enter a **Resource ID** to associate the logs with a specific Azure resource.
      
   7. Select the events to stream:
      
      - **Job status only**: Logs whether a job succeeded or failed.
      - **Full job details**: Logs job details, including status and data for each line action.
      - **User activity**: Logs all user activity in the workspace.
      - **API platform logs**: Logs all API requests handled by the API platform.
      - **Workato Log events**: Logs all messages sent to the Workato logging service.
      - **Genie conversations**: Logs the full details of genie conversations, including data for every response.
      
      Additionally, select the **Log types** and **Log levels** to include if you plan to stream events from the [Workato logging service](/en/features/logging-service).
      
   8. Optional. Enter the logging message you plan to use in the **Customize log message** field. Refer to the [Custom log messages](/en/features/activity-audit-log-streaming-customize-log) guide for more information.
      
   9. Click **Save** to apply your audit log streaming settings.
      
   10. Ensure your Azure Monitor Workspace receives the audit logs by querying the specified log type.
       
       ![Verify your audit logs](/assets/verify-logs.wHU3iO_v.png)_Verify your audit logs_
       
   
   **Azure Blob Storage**
   
   Complete the following steps to configure Azure Blob Storage as your audit log destination:
   
   1. [Create a new connection](/en/connectors/azure_blob_storage#connection-setup) for Azure Blob Storage, or select an existing connection.
      
      _Configure Azure Blob Storage as your audit log destination_
      
   2. Use the **Container name** drop-down menu to select a container from your Azure Blob Storage instance. You can refresh the container list if your desired container isn't listed.
      
   3. Select the events to stream:
      
      - **Job status only**: Logs whether a job succeeded or failed.
      - **Full job details**: Logs job details, including status and data for each line action.
      - **User activity**: Logs all user activity in the workspace.
      - **API platform logs**: Logs all API requests handled by the API platform.
      - **Workato Log events**: Logs all messages sent to the Workato logging service.
      - **Genie conversations**: Logs the full details of genie conversations, including data for every response.
      
      Additionally, select the **Log types** and **Log levels** to include if you plan to stream events from the [Workato logging service](/en/features/logging-service).
      
   4. Optional. Use the **Customize log message** field to define log messages using JSON format. You can add custom fields and structures. For more details, refer to the [Customize log message](/en/features/activity-audit-log-streaming-customize-log) documentation.
      
   5. Click **Save** to enable streaming to Azure Blob Storage.
      
   
   **Cloud based logging service**
   
   Complete the following steps to configure a cloud based logging service as your audit log destination:
   
   1. Provide the HTTP logging endpoint in the **Destination URL** field. For example, for Sumo Logic, this is the URL of an HTTP source.
      
      _Configure a cloud based logging service_
      
   2. Enable the **Requires authentication** toggle if the endpoint requires authentication, and provide the necessary credentials.
      
   3. Select the events to stream:
      
      - **Job status only**: Logs whether a job succeeded or failed.
      - **Full job details**: Logs job details, including status and data for each line action.
      - **User activity**: Logs all user activity in the workspace.
      - **API platform logs**: Logs all API requests handled by the API platform.
      - **Workato Log events**: Logs all messages sent to the Workato logging service.
      - **Genie conversations**: Logs the full details of genie conversations, including data for every response.
      
      Additionally, select the **Log types** and **Log levels** to include if you plan to stream events from the [Workato logging service](/en/features/logging-service).
      
   4. Optional. Use the **Customize log message** field to customize log messages using JSON format. You can use custom fields and define the JSON structure. For more details, refer to the [Customize log message](/en/features/activity-audit-log-streaming-customize-log) documentation.
      
   5. Click **Save** to enable streaming to your cloud based logging service.
      
   

Audit log streaming is now enabled and configured for all workspaces in Automation HQ.

---
