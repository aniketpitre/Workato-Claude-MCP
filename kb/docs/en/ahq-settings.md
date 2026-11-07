---
url: 'https://docs.workato.com/en/ahq-settings.md'
description: >-
  Configure Automation HQ settings in Workato, including organization-wide audit
  log streaming and cross-workspace grants for sharing Event streams topics.
---

# Automation HQ settings

Automation HQ provides audit log streaming to help administrators stream logs from all managed workspaces into a single destination.

You can configure [audit log streaming](/en/features/activity-audit-log) for the entire organization in the [Settings](/en/ahq-hq-workspace#settings). The following log types are available to stream:

- **Job status only**: Logs whether a job succeeded or failed.
- **Full job details**: Logs job details, including status and data for each line action.
- **User activity**: Logs all user activity in the workspace.
- **API platform logs**: Logs all API requests handled by the API platform.
- **Workato Log events**: Logs all messages sent to the Workato logging service.
- **Genie conversations**: Logs the full details of genie conversations, including data for every response.

You can also [customize log messages](/en/features/activity-audit-log-streaming#customize-log-message) and [select the destination](/en/features/activity-audit-log-streaming#audit-stream-destination) for logs. Workato supports the following destinations:

- [Amazon S3 Bucket](/en/features/activity-audit-log-streaming-destinations#amazon-s3-bucket)
- [Azure Monitor](/en/features/activity-audit-log-streaming-destinations#azure-monitor)
- [Azure Blob](/en/features/activity-audit-log-streaming-destinations#azure-blob-storage)
- A [cloud-based logging service](/en/features/activity-audit-log-streaming-destinations#cloud-based-logging-services), such as Sumo Logic, Datadog, Splunk, or [Google Cloud Storage Buckets](/en/features/activity-audit-log-streaming-destinations#google-cloud-storage-buckets)

Audit log streaming is disabled by default. Refer to [Audit log streaming for Automation HQ](/en/ahq-audit-log-streaming) to configure audit log streaming.

![Workspace settings](/assets/automation-hq-workspace-settings.BoacIY44.png)_Workspace settings_

## Cross-workspace grants

Cross-workspace grants let source workspaces share Event streams topics with other managed workspaces in your Automation HQ organization.

You can enable [cross-workspace grants](/en/cross-share-streams) for the entire organization in the [Settings](/en/ahq-hq-workspace#settings) interface.

Cross-workspace grants are disabled by default. Refer to [Enable cross-workspace grants](/en/cross-share-streams#enable-cross-workspace-grants) to configure this setting.

> **FURTHER READING**
> 
> - [Audit log streaming](/en/ahq-audit-log-streaming)
> - [Automation HQ workspace](/en/ahq-hq-workspace)

---
