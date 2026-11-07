---
url: 'https://docs.workato.com/en/features/activity-audit-log-streaming-retry.md'
description: >-
  Learn how Workato retries failed audit log streaming using a persistent cache
  and exponential backoff over a seven-day window.
---

# Audit log streaming retry

Workato retries sending failed audit logs, such as user activities, job summaries, or job details to the [destination](/en/features/activity-audit-log-streaming-destinations) you specify.

Workato stores audit logs in a persistent cache and applies an exponential backoff formula for retries. The system removes audit logs from the cache when they successfully reach the destination or after seven days without a successful delivery.

Workato marks audit logs as failed events after seven days of unsuccessful retries. Most logs reach the destination within 7-8 retry attempts.

> **FEATURE AVAILABILITY**
> 
> Audit log streaming retry is available for all log streaming destinations.

## Zero retention recipes

You can configure a recipe to have “zero retention" by selecting **Do not store any data** on the [recipe settings](/en/recipes/settings#data-retention) page. This results in Workato not storing any jobs data, including job lines of input or output, on the Workato platform or in your external storage location.

> **FEATURE AVAILABILITY**
> 
> The zero data retention capability is available on specific pricing plans. Refer to your pricing plan and contract to learn more.

For zero retention recipes, Workato performs the following tasks:

1. Sends an audit log without job input and output data.

**If the initial attempt to send an audit log for zero retention recipes fails**, Workato completes the following actions:

1. Stores the audit logs in a persistent cache for retry.
2. Uses the exponential backoff formula to retry sending the audit log to your destination.
3. Removes the audit log from the persistent cache upon successful delivery of the audit log to your destination or after seven days, whichever happens earlier.
4. Logs every retry for an event into the Workato Logs service.

* * *

## Email notifications

When audit log streaming fails, Workato sends email notifications to the workspace admin of your account and to all users designated in the [error notifications](/en/user-accounts-and-teams/admin-email#error-notifications) email list.

Audit log streaming can fail due to errors in the connection to your streaming [destination](/en/features/activity-audit-log-streaming-destinations). We classify these connection error events into two categories: involuntary and voluntary. Our email notification protocols differ for each of these event categories as follows:

### Voluntary disconnect

A voluntary disconnect is when you disconnect the connection to your destination manually. When this happens, Workato waits eight (8) hours before disabling audit log streaming retry. This delay is designed to account for situations where you temporarily disconnect your connection to update your connection credentials, such as your IAM Role ID. After the eight (8) hour interval has passed, Workato sends an email notification informing you that audit log streaming has stopped. For transparency, when the ALR (Audit Log Receiver) connection has been manually disconnected for more than eight (8) hours and the Workato system disables the ALR, the system logs this action in the activity audit.

The following table describes the frequency and contents of voluntary disconnect notification emails:

| Frequency | Contents |
| --- | --- |
| One (1) time only. | Account ID, Resource name, Resource ID, Event type, Event summary, Error time, Guidance on how to re-establish your connection |

### Involuntary disconnect

An involuntary disconnect is when audit logs fail to stream because the connection to your destination is no longer valid. In this scenario, there are two types of error notification emails Workato can send:

- **General notifications:** Workato sends this type of notification when Audit log streaming stops because of an invalid connection. _All invalid Audit log streaming connections trigger this type of notification email._
  
- **Granular notifications:** Workato sends this type of notification when Audit log streaming is disrupted due to an invalid connection caused by specific errors Workato has identified. _Only invalid connections where the error matches one of the error scenarios we’ve already identified trigger these types of email notifications._
  

The following table describes the frequency and contents of involuntary disconnect notification emails:

| Frequency | Contents |
| --- | --- |
| No more than one (1) time every 24 hours. | Account ID; Resource name; Resource ID; Event type; Event summary; Error time; Guidance on how to re-establish your connection; Error codes, as applicable for granular notifications |

#### Error codes for granular notifications

This section describes the types of errors Workato can identify. If your connection encounters one of these errors, Workato sends an email notification specifying the error type. If the error you encounter is not listed in this section, Workato sends you a general error notification.

Error codes are organized based on streaming destinations:

- [S3 error codes](#s3-error-codes)
- [HTTP error codes](#http-error-codes)
- [Azure Monitor error codes](#azure-monitor-error-codes)
- [Azure Blob error codes](#azure-blob-error-codes)

##### S3 error codes

| Error code | Description |
| --- | --- |
| `PermanentRedirect` (`301 Moved Permanently`) | The AWS region was set up incorrectly. This means that the region provided in the connection does not match the region where the bucket was initially set up. |
| `InvalidAccessKeyID` (`403 Forbidden`) | This error occurs when the Role ARN is invalid. |
| `AccessDenied` (`403 Forbidden`) | This error occurs when your connection does not have the required permissions for Audit log streaming. |
| `NoSuchBucket` (`404 Not Found`) | This error occurs when Workato is unable to locate the S3 bucket specified in your connection. This can happen if the S3 bucket has been deleted. |
| `InvalidBucketName` (`400 Bad Request`) | The S3 bucket name provided is invalid. |

##### HTTP error codes

| Error code | Description |
| --- | --- |
| `404 Destination Not Found` | Workato was unable to find the requested resource which could be due to various reasons such as a mistyped URL, a broken link, or the resource being moved or deleted. |
| `403 Forbidden` | This error occurs when the streaming connection does not have the required permissions. |
| `401 Unauthorized` | This error occurs when the streaming connection does not have the required authentication requirements. This can be caused by an invalid token. |

##### Azure Monitor error codes

| Error code | Description |
| --- | --- |
| `Invalid Authorization`(`403 Forbidden`) | This error occurs when the shared key provided is malformed or otherwise invalid. |
| `Error Building Signature` | This error occurs when the provided Workspace ID or shared key is malformed or otherwise invalid. |
| `Streaming Destination Not Found` | This error occurs when the provided Workspace ID is malformed or otherwise invalid. This error can also occur if your Log Analytics Workspace has been deleted. |

##### Azure Blob error codes

| Error code | Description |
| --- | --- |
| `404 ContainerNotFound` | The container specified in your streaming destination connection may have been disabled or deleted. |
| `404 ResourceNotFound` | Workato was unable to find the storage account specified in your connection. This can happen if the storage account is disabled or deleted. |
| `403 AuthorizationPermissionMismatch` | The Azure user or registered application does not have sufficient access to the specified storage account. This can happen if the client credentials secret token is expired or deleted. |
| `401 InvalidAuthenticationInfo` | This error occurs when the Azure user or registered application does not have the required permissions for Audit log streaming. This can occur when the authentication token is disabled, deleted, or expired. |

* * *

### Error notification email recipients for Embedded accounts

The email recipients for Embedded accounts are determined by the workspace where audit log streaming is enabled, as described in the following table.

| Log streaming enabled in.. | Email recipients |
| --- | --- |
| Embedded partner admin workspace | Embedded partner admin |
| Embedded customer workspaces with a shared streaming destination | Embedded partner admin |
| Embedded customer workspaces with distinct streaming destinations | Embedded customer |

* * *

### Error notification email recipients for AHQ accounts

The email recipients for AHQ accounts are determined by the workspace where audit log streaming is enabled, as described in the following table.

| Log streaming enabled in.. | Email recipients |
| --- | --- |
| AHQ admin workspace | AHQ admin |
| AHQ managed workspaces with a shared streaming destination | AHQ admin |
| AHQ managed workspaces with distinct streaming destinations | Managed workspace admin |

---
