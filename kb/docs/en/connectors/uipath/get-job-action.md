---
url: 'https://docs.workato.com/en/connectors/uipath/get-job-action.md'
description: The Get job action retrieves details about a job by its ID.
---

# UiPath - Get job action

The **Get job** action retrieves details about a job by its ID.

## Input

| Input field | Description |
| --- | --- |
| Job ID | Provide the ID for the job to retrieve details for. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the job instance. |
| Key | Unique key assigned to the job for internal reference. |
| Info | Supplementary information or logs related to the job execution. |
| Start time | The date and time when the job execution started. |
| End time | The date and time when the job execution completed or stopped. |
| State | The current or final status of the job. |
| Source | Indicates how the job was triggered. |
| Type | Specifies the job type, such as `Attended`, `Unattended`, or `NonProduction`. |
| Host machine | The name of the robot machine that executed the job. |

---
