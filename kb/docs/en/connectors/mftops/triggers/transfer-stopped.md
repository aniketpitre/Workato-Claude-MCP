---
url: 'https://docs.workato.com/en/connectors/mftops/triggers/transfer-stopped.md'
description: >-
  Monitor a transfer in real-time for stops caused by reaching the consecutive
  run error threshold.
---

# MFTOps - Transfer stopped trigger (real-time)

The **Transfer stopped (real-time)** trigger monitors a transfer in real-time for stops caused by reaching the consecutive run error threshold. Refer to [Transfer auto-stop](/en/managed-file-transfer/error-handling-and-retries#transfer-auto-stop) for more information.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events up to one week old. Defaults to one hour ago. You can't change this value after you run or test this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| Operation ID | A monotonic sequence number that tells you where an event sits in Workato Logs. |
| Event time | The time the event occurred. |
| Transfer ID | The identifier of the file transfer. |
| Transfer name | The name of the file transfer. |
| Stopped at | The time the transfer stopped. |
| Error | Details about the failure that triggered the stop. Contains the following fields: **Error stage**: The stage the failure occurred in., **Error type**: The category of the error., **Error message**: A human-readable description of the error. |
| Consecutive run error count | The number of consecutive failed runs that triggered the stop. |
| Stopped queued run count | The number of file runs that were queued but not yet picked up when the transfer stopped. |

---
