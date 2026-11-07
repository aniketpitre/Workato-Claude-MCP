---
url: 'https://docs.workato.com/en/connectors/rpa-by-workato/get-job-logs-batch.md'
description: The Get job logs batch action retrieves the logs of an RPA job you specify.
---

# RPA by Workato - Get job logs action (batch)

The **Get job logs** batch action retrieves the logs of an RPA job you specify.

## Input

| Input fields | Description |
| --- | --- |
| Job ID | Provide the ID of the job you plan to retrieve logs from or input a Job ID datapill from the output of the [Start job](/en/connectors/rpa-by-workato/start-job) action. |

## Output

| Output fields | Description |
| --- | --- |
| Log message | The message of the retrieved log. |
| Log type | The type of log retrieved. |
| Created at | A timestamp indicating when the retrieved log was created. |
| Class name | The name of the class associated with the retrieved job. |
| Step name | The step the job was completing in Robotiq.ai at the time of the log's creation. |
| Source | The source of the retrieved log. |
| List size | The total number of logs retrieved. |
| List index | The position of the log within the list. |

---
