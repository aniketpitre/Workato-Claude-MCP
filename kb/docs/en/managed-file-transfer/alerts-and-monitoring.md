---
url: 'https://docs.workato.com/en/managed-file-transfer/alerts-and-monitoring.md'
description: >-
  Monitor Managed File Transfer with run history, logs, performance analytics,
  and configurable notifications for visibility into transfers.
---

# Alerts and monitoring

Workato provides detailed logs, run and attempt history, and configurable notifications to enhance visibility into file transfer operations.

## Run history and analytics

The **Runs** tab of a file transfer asset provides a historical view of transfers.

Each run displays the following:

| Column | Description |
| --- | --- |
| **File name** | The name of the transferred file. |
| **Start time** | When the transfer started. |
| **End time** | When the transfer ended. |
| **File size** | The size of the transferred file. |
| **Status** | Each run displays one of the following statuses: **Queued**: File detected, waiting to process.; **Running**: Transfer in progress.; **Successful**: Transfer completed. Displays the number of retries used, if applicable.; **Failed**: Transfer failed after exhausting all automatic retry attempts. Refer to [Error handling and retries](/en/managed-file-transfer/error-handling-and-retries) for more information.; **Stopped**: File wasn't picked up because the transfer auto-stopped before this run started. Refer to [Transfer auto-stop](/en/managed-file-transfer/error-handling-and-retries#transfer-auto-stop) for more information. |
| **Duration** | How long the transfer took. |

Additionally, the **Runs** tab provides the following capabilities:

- Use the search bar to search file names.
  
- Use the **Period** and **Status** drop-down menus to filter logs.
  
- Use the **Original run ID** search bar to find a sequence of attempts with the same `original_run_id` value. This includes the original attempt and all manual retries.
  
- Click **Retry** on a failed row to retry a single transfer or click **Retry all failed** to retry all failed transfers.
  
- Select a row to view its detailed [attempt history](#attempt-history).
  

### Attempt history

You can select a row in the **Runs** tab to view the following information for the original attempt and any automatic retries. Manual retries create a separate run with its own attempt history.

**For each attempt**

| Field | Description |
| --- | --- |
| **Attempt** | The attempt number. |
| **Start time** | When the attempt started. |
| **End time** | When the attempt ended. |
| **Status** | The outcome of the attempt. Use the **Status** drop-down menu to filter by this field. |
| **Duration** | How long the attempt took. |
| **Details** | The error message for failed attempts, or a success summary. |

**Overall**

| Field | Description |
| --- | --- |
| **File run ID** | The unique identifier for the file run. Used to find the run in [Workato Logs](#workato-logs). |
| **Source path** | The full path of the source file. |
| **Start time** | When the first attempt started. |
| **End time** | When the final attempt ended. |
| **Retries** | The number of automatic retries used, if applicable. |
| **Related runs** | Links to additional runs with the same `original_run_id`, if applicable. |

## Workato Logs

File orchestration activity displays in Workato Logs as **File transfer** and **SFTP server** events. Go to **Tools > Logs** to view events across all file transfers in one place, filter by run, and correlate file orchestration events with other platform activity.

Logs include the following columns for file orchestration entries:

| Column | Description |
| --- | --- |
| **Time** | The time the event occurred. |
| **Log type** | The category of the event. |
| **Log level** | The severity of the event, such as `INFO`, `WARN`, or `ERROR`. |
| **Data** | Event-specific details in JSON format. |
| **Recipe ID** | The ID of the recipe that triggered the transfer, if applicable. |
| **Step number** | The number of the recipe step that triggered the transfer, if applicable. |

The contents of the **Data** JSON vary depending on the event. The following examples define commonly included fields:

**File transfer**

File transfers record automatic retries in the `attempts` array alongside the original attempt, instead of creating separate log events. Manual retries create a new event, with an `original_run_id` field identifying the run it retried and a new `run_id` identifying the manual retry.

```json
{
  event_type: "transfer.run.succeeded",
  timestamp: "2026-11-02T22:31:19.614Z",
  user_id: 48141,
  transfer_id: "mft-7hQ2kR-9pLxTz-A3",
  transfer_name: "Bank reports to Partners",
  run_id: "mftr-7hQ3mS-2vNbWq-A3",
  execution_id: "d9e1bb1e-d4c4-4327-9e76-29f4a7825c83",
  status: "succeeded",
  started_at: "2026-11-02T22:30:40.100Z",
  ended_at: "2026-11-02T22:31:19.600Z",
  duration_ms: 39500,
  attempts_count: 2,
  attempts_truncated: false,
  file: {
    name: "bank_report_14362.txt",
    source_path: "/Outbound Banking Reports/bank_report_14362.txt",
    reported_size_bytes: 235233,
    measured_size_bytes: 235233,
    best_known_size_bytes: 235233
  },
  source: {
    id: "6c0d96b8-3d29-48e1-855f-d007858eef39",
    name: "Bank reports",
    type: "workato_files",
    directory_path: "/Outbound Banking Reports"
  },
  targets: [
    {
      id: "5cf694c6-0969-4d4d-9df4-f8004094dd51",
      name: "Partner A",
      type: "sftp",
      directory_path: "/Processed",
      processing_action_types: ["compress"]
    }
  ],
  attempts: [
    {
      attempt_id: "a1f2c3d4-1111-4a1a-9999-000000000001",
      attempt_number: 1,
      origin: "original",
      status: "failed",
      started_at: "2026-11-02T22:30:40.100Z",
      ended_at: "2026-11-02T22:30:43.200Z",
      duration_ms: 3100,
      failure: {
        stage: "target_write",
        error_code: "target_access_denied",
        error_type_id: "err.ssh.auth.no_more_methods_available",
        error_type_name: "No more authentication methods available",
        error_message: "The target file could not be written because access was denied. Check the target connection permissions."
      }
    },
    {
      attempt_id: "d9e1bb1e-d4c4-4327-9e76-29f4a7825c83",
      attempt_number: 2,
      origin: "auto_retry",
      status: "succeeded",
      started_at: "2026-11-02T22:31:19.000Z",
      ended_at: "2026-11-02T22:31:19.600Z",
      duration_ms: 600
    }
  ]
}
```

| Field | Description |
| --- | --- |
| `event_type` | The type of event, such as `transfer.run.succeeded` or `transfer.run.failed`. |
| `timestamp` | The date and time when the event occurred. |
| `user_id` | The ID of the user associated with the transfer. |
| `transfer_id` | The ID of the file transfer. |
| `transfer_name` | The name of the file transfer. |
| `run_id` | The ID of the specific transfer run. |
| `original_run_id` | The ID of the retried run. This field only exists for manual retries. |
| `execution_id` | The ID of the run's final attempt. Matches the `attempt_id` of the last entry in `attempts`. |
| `status` | The outcome of the run: `succeeded` or `failed`. |
| `started_at` | When the run started. |
| `ended_at` | When the run ended. |
| `duration_ms` | The run duration in milliseconds. |
| `attempts_count` | The number of attempts made during the run. |
| `attempts_truncated` | Whether the `attempts` array was truncated and doesn't include every attempt made during the run. |
| `file` | Details about the transferred file, including its name, size, and source path. |
| `source` | The file's source location. |
| `targets` | The destinations the file was sent to. |
| `attempts` | Details about attempts made during the run, including error details for failed attempts. |

**SFTP server**

```json
{
  event_type: "sftp.file.downloaded",
  timestamp: "2026-07-28T20:15:57.326396973Z",
  user_id: 48141,
  account_id: "53f60e7a-f29e-46fe-9f41-1c3bf66136ff",
  account_username: "JadeLee+prod",
  session_id: "019faa5e-a1c2-7a19-aefe-3bbf79a05dd4",
  file_name: "bank_report_14362.txt",
  file_path: "/incoming/bank_report_14362.txt",
  byte_range_start: 0,
  byte_range_end: 5172220,
  download_duration_seconds: 0.81006177
}
```

| Field | Description |
| --- | --- |
| `event_type` | The type of event, such as `sftp.file.downloaded`, `sftp.authentication.success`, or `sftp.session.disconnected`. |
| `timestamp` | The date and time when the event occurred. |
| `user_id` | The ID of the user associated with the SFTP account. |
| `account_id` | The ID of the SFTP account. |
| `account_username` | The account username used to authenticate. |
| `ip_address` | The IP address the connection originated from. This field only exists for events related to authentication and connection. |
| `session_id` | The ID of the SFTP connection. |
| `file_name` | The name of the file. |
| `file_path` | The full path of the file on the SFTP server. |
| `byte_range_start` | The starting byte offset of the file operation. |
| `byte_range_end` | The ending byte offset of the file operation. |
| `download_duration_seconds` | The duration of the download in seconds. |

## Triggers

Use **MFTOps** to build recipes that react to file transfer events, such as sending notifications, alerting external systems, or automating remediation steps. MFTOps supports the following triggers:

- [No file detected](/en/connectors/mftops/triggers/no-file-detected)
- [Failed transfer run](/en/connectors/mftops/triggers/failed-transfer-run)
- [Successful transfer run](/en/connectors/mftops/triggers/successful-transfer-run)
- [Transfer stopped](/en/connectors/mftops/triggers/transfer-stopped)

> **FEATURE AVAILABILITY**
> 
> Contact your Customer Success Manager for information about access to Workato MFT.

---
