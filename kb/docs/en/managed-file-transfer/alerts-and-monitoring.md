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
  
- Click **Retry** on a failed row to retry a single transfer or click **Retry all failed** to retry all failed transfers.
  
- Select a row to view its detailed [attempt history](#attempt-history).
  

### Attempt history

You can select a row in the **Runs** tab to view its attempt history and the details of each attempt:

**For each attempt**

| Field | Description |
| --- | --- |
| **Attempt** | The attempt number. |
| **Provenance** | How the attempt was initiated: **Original** for the first attempt, **Auto-retry** for an automatic retry, or **Manual retry** followed by the name of the user who triggered it. |
| **Start time** | When the attempt started. |
| **End time** | When the attempt ended. |
| **Status** | The outcome of the attempt. |
| **Duration** | How long the attempt took. |
| **Details** | The error message for failed attempts, or a success summary. |

**Overall**

| Field | Description |
| --- | --- |
| **File run ID** | The unique identifier for the file run. Used to find the run in [Workato Logs](#workato-logs). |
| **Source path** | The full path of the source file. |
| **Start time** | When the first attempt started. |
| **End time** | When the final attempt ended. |
| **Duration** | Total time across all attempts. |
| **Attempted automatic retries** | The number of automatic retries used. |

Use the **Attempt type** drop-down menu to filter by original transfers, auto-retries, or manual retries and the **Status** drop-down menu to filter by outcome.

## Workato Logs

File orchestration activity displays in Workato Logs as **File transfer** and **SFTP server** events. Go to **Tools > Logs** to view events across all file transfers in one place, filter by run, and correlate file orchestration events with other platform activity.

Logs include the following columns for file orchestration entries:

| Column | Description |
| --- | --- |
| **Time** | The time the event occurred. |
| **Log type** | The category of the event. |
| **Log level** | The severity of the event, such as `INFO`, `WARN`, or `ERROR`. |
| **Data** | Event-specific details in JSON format. |

Depending on the log type, the **Data** field includes the following additional fields:

**File transfer**

| Field | Description |
| --- | --- |
| **Transfer ID** | The identifier of the file transfer. |
| **File run ID** | The identifier of the specific transfer run. |

```json
{
  message: "Source transfer complete.",
  event: "MFT_SOURCE_DOWNLOAD_COMPLETE",
  start_time: "2025-05-17T09:15:32.123Z",
  end_time: "2025-05-17T09:15:32.423Z",
  file_transfer: "mft_flow_banking_partners_001",
  file_run_id: "4C1V-9bn5-2re7-8km3"
}
```

**SFTP server**

| Field | Description |
| --- | --- |
| **Username** | The account username used to authenticate. |
| **IP address** | The IP address the connection originated from. |

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
