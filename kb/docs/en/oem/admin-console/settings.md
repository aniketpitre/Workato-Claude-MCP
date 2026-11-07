---
url: 'https://docs.workato.com/en/oem/admin-console/settings.md'
description: >-
  Set up audit log streaming in the Embedded Admin console to replicate and
  store log data from managed customer workspaces in a destination you specify.
---

# Admin console - Audit log streaming

Audit log streaming replicates and stores log data from all managed customer workspaces in a destination you specify. This lets you maintain access to logs beyond the [audit log](/en/features/activity-audit-log#log-retention) and [Workato logging service](/en/features/logging-service#log-limits) retention periods and ensures you have ample time to review and analyze your activity logs for security and operational insights.

> **LOG STREAMING FOR INDIVIDUAL CUSTOMERS**
> 
> Refer to [Set unique log destinations](#unique-log-destinations) to enable audit log streaming for each customer individually.

Each job or event is represented as a JSON file, which Workato sends to the log provider using the HTTP POST method. Workato supports the following [destinations](/en/features/activity-audit-log-streaming-destinations):

- [Amazon S3 Bucket](/en/features/activity-audit-log-streaming-destinations#amazon-s3-bucket)
- [Azure Monitor](/en/features/activity-audit-log-streaming-destinations#azure-monitor)
- [Azure Blob](/en/features/activity-audit-log-streaming-destinations#azure-blob-storage)
- A [cloud-based logging service](/en/features/activity-audit-log-streaming-destinations#cloud-based-logging-services), such as Sumo Logic, Datadog, Splunk, or [Google Cloud Storage Buckets](/en/features/activity-audit-log-streaming-destinations#google-cloud-storage-buckets)

> **FEATURE AVAILABILITY**
> 
> Audit log streaming is available on specific pricing plans. Refer to your pricing plan and contract to learn more.

## Log streaming events

Available [Log streaming events](/en/features/activity-audit-log-streaming-sample#json-file-content-sample-data) include:

- **Job status only**: Logs whether a job succeeded or failed.
- **Full job details**: Logs job details, including status and data for each line action.
- **User activity**: Logs all user activity in the workspace.
- **API platform logs**: Logs all API requests handled by the API platform.
- **Workato Log events**: Logs all messages sent to the Workato logging service.
- **Genie conversations**: Logs the full details of genie conversations, including data for every response.

## Setting up audit log streaming

1. Sign in to Workato with an Embedded partner workspace.
   
2. Go to **Admin console > Settings > Audit log streaming**.
   
   ![Audit log streaming settings in the Admin console](/assets/alr-settings.Du_xqo1a.png)_Audit log streaming settings in the Admin console_
   
3. Use the **Enable setup and streaming of customer audit logs** toggle to enable audit log streaming.
   
4. Select the events to stream:
   
   - **Job status only**: Logs whether a job succeeded or failed.
   - **Full job details**: Logs job details, including status and data for each line action.
   - **User activity**: Logs all user activity in the workspace.
   - **API platform logs**: Logs all API requests handled by the API platform.
   - **Workato Log events**: Logs all messages sent to the Workato logging service.
   - **Genie conversations**: Logs the full details of genie conversations, including data for every response.
   
   Additionally, select the **Log types** and **Log levels** to include if you plan to stream events from the [Workato logging service](/en/features/logging-service).
   
5. Optionally, [customize the log message format](#customize-log-message).
   
6. Select a **Destination type** from the picklist and enter any required fields for the selected [destination type](/en/features/activity-audit-log-streaming-destinations).
   
7. Select **Save**.
   

> **OVERRIDE BEHAVIOR FOR OEM WORKSPACES**
> 
> Configuring audit log streaming for all OEM customer workspaces overrides any existing audit log streaming settings in the OEM admin workspace. For example, if you set the OEM admin workspace to stream logs to an S3 destination but configure streaming for all OEM customer workspaces to Sumo Logic, the system directs all logs, including those from the OEM admin workspace, to Sumo Logic. Consider this behavior carefully when you set up audit log streaming for multiple workspaces.

## Customize audit log JSON

You can customize the audit log JSON format for your destination application. For example, you can define a `source` application, such as `workato`, to process the event logs in the destination application automatically.

Go to **Admin console > Settings > Audit log streaming > Customize log message** to create a custom log message in JSON format. Define the JSON structure with placeholders for Workato audit log fields and any custom fields. Workato replaces each placeholder with the actual value before it streams the event.

Refer to [Supported placeholders](/en/features/activity-audit-log-streaming-customize-log#placeholders) for more information.

![Customize the log message](/assets/customize-log-message.CiaX9tKN.png)_Customize the log message_

## Identifying customers from JSON files

The JSON file includes the `user_id` and `user_external_id` parameters in the `context` block for all log files related to job details. These two IDs refer to the Workato customer ID and the partner-provided external ID for the customer.

![Audit log streaming](/assets/alr-external-id.Bj_rTbHP.png)_Sample JSON from a job event_

The JSON file includes the `id` and `external_id` parameters nested in the `user` and `team` for all log files related to user activity. The IDs in the `team` block refer to the customer, while the IDs in the `user` block refer to the specific customer team member who performed the action.

![Audit log streaming](/assets/alr-external-id-user._dKBmalN.png)_Sample JSON from a user activity event_

If the partner did not provide any external ID while creating the customer or customer team member, the `external_id` value is `null`.

## Set unique audit log destinations

Partners can provide audit log replication configuration on each customer individually. This setting is available on each customer's **Settings** page as long as the audit log replication setting is not configured in the partner's **Admin console**. Therefore, if each customer requires a separate audit log destination, don't configure the overall setting in the **Admin console**.

> **FURTHER READING**
> 
> See our [audit log streaming guide for direct connections](/en/features/activity-audit-log-streaming) for more information about the following topics:
> 
> - [Audit stream destinations](/en/features/activity-audit-log-streaming-destinations)
> - [JSON file details](/en/features/activity-audit-log-streaming-sample#json-file-details)
> - [JSON file content - sample data](/en/features/activity-audit-log-streaming-sample#json-file-content-sample-data)

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/encryption-key-management/guides.md
description: >-
  Browse setup guides for connecting key management services to Workato
  Enterprise Key Management and configuring custom encryption keys.
---

# Encryption key management guides

**[Connecting Amazon Key Management Service (KMS) to Workato EKM](/en/security/data-protection/encryption-key-management/guides/setting-up-amazon-key-management-service)**  
Connect your AWS Key Management Service account to Workato Enterprise Key Management.

**[Configuring Workato EKM with a custom key](/en/security/data-protection/encryption-key-management/guides/setting-up-custom-kms-key)**  
Configure Workato Enterprise Key Management with a custom key.

---

---
url: >-
  https://docs.workato.com/en/features/environments/deployment-permission-update.md
description: >-
  Learn how the Workato Deployment permission controls who can deploy projects
  across environments and how admins enable it for custom roles.
---

# Environment deployment permission update

Starting on December 12, 2023, Workato is introducing a new **Deployment** permission. The Deployment permission determines access to project [deployments](/en/features/environments/deployment) across [environments](/en/features/environments).

To deploy a project to an environment, you must have this permission enabled in both the DEV environment and the target environment.

This replaces the previous requirement of having the [Recipe lifecycle management permission](/en/privileges#recipe-lifecycle-management) enabled in the Development (DEV) environment and having any access in the target environment to deploy to it.

## Role permissions

The Deployment permission is enabled for [system roles](/en/roles#system-roles) and [custom roles](/en/roles#custom-roles) as follows:

- **Admin:** Enabled
- **Analyst:** Enabled
- **Operator:** Disabled
- **Custom:** Disabled until an admin manually enables it

> **LOSS OF ACCESS FOR CUSTOM ROLES**
> 
> All collaborators with existing custom roles _will lose access to deployment functionality_ as a result of this change. Admins can restore access for these collaborators by updating the custom role(s) to enable the Deployment permission in the appropriate environments.
> 
> If you do not have access to the **Deployments** tab for a project, ask your admin to update your permissions.

## Why is this change important?

This security enhancement provides better control over who can deploy to production or test environments by separating deployment permissions from recipe lifecycle management permissions.

## How to enable the Deployment permission for a custom role

If you are an administrator and you plan to enable the Deployment permission for a given custom role, complete the following steps:

1. Navigate to **Workspace admin > Access control** and select **Collaborator roles**.
   
2. Select the custom role you plan to update.
   
3. Select the **Recipe development** tab.
   
4. Select the **Deployment** checkbox in the **Deployment** section.
   
   ![Deployment permission](/assets/new-deployment-permission.TcXp9bFR.png) _Deployment permission_
   
5. Select **Save changes**.

---
