---
url: 'https://docs.workato.com/en/connectors/rpa-by-workato/get-job-detail.md'
description: The Get job detail action retrieves information from an RPA job you specify.
---

# RPA by Workato - Get job detail action

The **Get job detail** action retrieves information from an RPA job you specify.

## Input

| Input fields | Description |
| --- | --- |
| Stage | Select the stage of the process you plan to retrieve. Alternatively, you can switch to **Use stage ID** and enter `0` for `DEV`, `1` for `TEST`, or `2` for `PROD`. |
| Department ID | Select the department associated with the job you plan to retrieve. Alternatively, you can switch to **Use department ID** and input a Department ID datapill. |
| Process ID | Select the process that contains the job you plan to retrieve. |
| Job ID | Provide the ID of the job you plan to retrieve information about or input a Job ID datapill from the output of the [Start job](/en/connectors/rpa-by-workato/start-job) action. |

## Output

| Output fields | Description |
| --- | --- |
| Process name | The name of the process that contains the retrieved job. |
| Process ID | The ID of the process that contains the retrieved job. |
| Department name | The name of the department associated with the retrieved job. |
| Department ID | The ID of the department associated with the retrieved job. |
| Job name | The name of the retrieved job. |
| Job status | The status of the retrieved job. |
| Canceled description | A description of the job's cancellation, if it was canceled. |
| Started at | A timestamp indicating when the retrieved job started. |
| Completed at | A timestamp indicating when the retrieved job completed in Robotiq.ai. |
| Priority | The retrieved job's priority level. |
| Timeout | The number of minutes Robotiq.ai will wait for the job to be run by a bot. The job is cancelled if this length of time is exceeded. |
| Schedule ID | The ID of the job's schedule in Robotiq.ai. |
| Retry attempts | The number of times Robotiq.ai retries the job if it encounters an error. |
| Job execution timeout | The maximum run time for the process. |
| Robot name | The name of the robot assigned to the job. |
| Robot ID | The ID of the robot assigned to the job. |
| Error details | The job's error message, if applicable. |
| Job status last updated at | A timestamp indicating when the job's status was last updated. |

---
