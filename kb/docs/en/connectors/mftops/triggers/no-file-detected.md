---
url: 'https://docs.workato.com/en/connectors/mftops/triggers/no-file-detected.md'
description: Monitor a file transfer in real-time for poll events that find no files.
---

# MFTOps - No file detected trigger (real-time)

The **No file detected (real-time)** trigger monitors a file transfer in real-time for poll events that find no files.

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
| Transfer ID | The identifier of the file transfer. |
| Transfer name | The name of the file transfer. |
| Polled at | The time of the scheduled poll that found no files. |
| Source | Details about the monitored source endpoint. Contains the following fields: **Source ID**: The identifier of the source endpoint.; **Source path**: The directory path the source polls for files.; **Source name**: The name of the source endpoint.; **Source type**: The type of the source endpoint, such as `sftp`. |

---
