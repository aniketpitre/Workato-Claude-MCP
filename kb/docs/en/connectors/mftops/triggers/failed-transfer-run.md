---
url: 'https://docs.workato.com/en/connectors/mftops/triggers/failed-transfer-run.md'
description: Monitor a transfer run for failures in real-time.
---

# MFTOps - Failed transfer run trigger (real-time)

The **Failed transfer run (real-time)** trigger monitors a transfer run for failures in real-time.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events up to one week old. Defaults to one hour ago. You can't change this value after you run or test this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Transfers to monitor | Select **All transfers** to monitor every file transfer, or **Selected transfers** to monitor only the transfers you list by ID. |
| Transfer IDs | Provide one or more transfer IDs to monitor, separated by commas. Required when **Transfers to monitor** is set to **Selected transfers**. |

## Output

| Output field | Description |
| --- | --- |
| Operation ID | A monotonic sequence number that tells you where an event sits in Workato Logs. |
| Event time | The time the event occurred. |
| Run ID | The identifier of the failed transfer run. |
| Transfer ID | The identifier of the file transfer. |
| Transfer name | The name of the file transfer. |
| Failed at | The time the run failed. |
| Started at | The time the run started. |
| File | Details about the file being transferred when the run failed. Contains the following fields: **Original file name**: The name of the source file.; **Original file path**: The full path of the source file.; **Original size (bytes)**: The size of the source file, in bytes. |
| Source | Details about the source endpoint. Contains the following fields: **Source ID**: The identifier of the source endpoint.; **Source path**: The directory path the source polls for files.; **Source name**: The name of the source endpoint.; **Source type**: The type of the source endpoint, such as `sftp`. |
| Target | Details about the target endpoint. Contains the following fields: **Target ID**: The identifier of the target endpoint.; **Target path**: The directory path files are delivered to.; **Target name**: The name of the target endpoint.; **Target type**: The type of the target endpoint, such as `workato_files`. |
| Error | Details about the failure. Contains the following fields: **Error stage**: The stage the failure occurred in, such as `source_download`, `pre_processing`, `target_upload`, or `post_processing`.; **Error type**: The category of the error, such as `connection_error`.; **Error message**: A human-readable description of the error. |

---

---
url: >-
  https://docs.workato.com/en/connectors/mftops/triggers/successful-transfer-run.md
description: Monitor a transfer run in real-time for successful transfers.
---

# MFTOps - Successful transfer run trigger (real-time)

The **Successful transfer run (real-time)** trigger monitors a transfer run in real-time for successful transfers.

> **BACKUP USE CASE**
> 
> Ensure [auto-deletion](/en/managed-file-transfer/transfer-flows#add-a-source) is disabled if you plan to use this trigger to back up files.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events up to one week old. Defaults to one hour ago. You can't change this value after you run or test this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Transfers to monitor | Select **All transfers** to monitor every file transfer, or **Selected transfers** to monitor only the transfers you list by ID. |
| Transfer IDs | Provide one or more transfer IDs to monitor, separated by commas. Required when **Transfers to monitor** is set to **Selected transfers**. |

## Output

| Output field | Description |
| --- | --- |
| Operation ID | A monotonic sequence number that tells you where an event sits in Workato Logs. |
| Event time | The time the event occurred. |
| Run ID | The identifier of the successful transfer run. |
| Transfer ID | The identifier of the file transfer. |
| Transfer name | The name of the file transfer. |
| Completed at | The time the run completed. |
| Started at | The time the run started. |
| File | Details about the transferred file. Contains the following fields: **Original file name**: The name of the source file.; **Original file path**: The full path of the source file.; **Original size (bytes)**: The size of the source file, in bytes. |
| Source | Details about the source endpoint. Contains the following fields: **Source ID**: The identifier of the source endpoint.; **Source path**: The directory path the source polls for files.; **Source name**: The name of the source endpoint.; **Source type**: The type of the source endpoint, such as `sftp`. |
| Target | Details about the target endpoint. Contains the following fields: **Target ID**: The identifier of the target endpoint.; **Target path**: The directory path files are delivered to.; **Target name**: The name of the target endpoint.; **Target type**: The type of the target endpoint, such as `workato_files`. |

---
