---
url: 'https://docs.workato.com/en/connectors/rpa-by-workato/start-job.md'
description: The Start job action starts an RPA job in the process you specify.
---

# RPA by Workato - Start job action

The **Start job** action starts an RPA job in the process you specify.

## Input

| Input fields | Description |
| --- | --- |
| Stage | Select the stage of the job you plan to start. Alternatively, you can switch to **Use stage ID** and enter `0` for `DEV`, `1` for `TEST`, or `2` for `PROD`. |
| Department ID | Select the department associated with the job you plan to start. Alternatively, you can switch to **Use department ID** and input a Department ID datapill. |
| Process ID | Provide the ID of the process that contains the job you plan to start. |
| Job name | Provide the name of the job you plan to start. |
| Wait for response? | Select whether to wait for the RPA job to complete before proceeding with the next step of the recipe. The maximum allowed wait time is three hours. |

## Output

| Output fields | Description |
| --- | --- |
| Job ID | The ID of the job. |
| Process name | The name of the process that contains the job. |
| Process ID | The ID of the process that contains the job. |
| Department name | The name of the department associated with the job. |
| Department ID | The ID of the department associated with the job. |
| Job name | The name of the job. |
| Job status | The status of the job. |
| Canceled description | A description of the job's cancellation, if it was canceled in Robotiq.ai. |
| Started at | A timestamp indicating when the job started. |
| Completed at | A timestamp indicating when the job completed. |
| Priority | The job's priority level. |
| Timeout | The number of minutes Robotiq.ai will wait for the job to be run by a bot. The job is cancelled if this length of time is exceeded. |
| Schedule ID | The ID of the job's schedule in Robotiq.ai. |
| Retry attempts | The number of times Robotiq.ai retries the job if it encounters an error. |
| Job execution timeout | The maximum run time for the process. |
| Robot name | The name of the robot assigned to the job. |
| Robot ID | The ID of the robot assigned to the job. |
| Error details | The job's error message, if applicable. |
| Job status last updated at | A timestamp indicating when the job's status was last updated. |

---
