---
url: 'https://docs.workato.com/en/connectors/vercel/report-check-result-action.md'
description: >-
  The Report check result action updates a Vercel check run with a status and
  conclusion.
---

# Vercel - Report check result action

The **Report check result** action updates a check run in Vercel with a status and conclusion.

## Input

| Input field | Description |
| --- | --- |
| Deployment ID | Select a deployment or enter a deployment UID. |
| Check run ID | Select a check run on the deployment or enter a check run ID. |
| Status | Select the progress of the run. Options include **Queued**, **Running**, and **Completed**. |
| Conclusion | Select the final result. Options include **Succeeded**, **Failed**, **Neutral**, **Skipped**, **Timeout**, and **Canceled**. |

## Output

| Output field | Description |
| --- | --- |
| ID | The check run ID. |
| Check ID | The ID of the check. |
| Deployment ID | The ID of the deployment. |
| Name | The check name. |
| Status | The run status. Options include `queued`, `running`, and `completed`. |
| Conclusion | The final result of the run. |
| Conclusion text | An explanatory note about the result. |
| Started at | When the run started, in ISO 8601 format. This field is empty if the run is still queued. |
| Completed at | When the run completed, in ISO 8601 format. The time between **Started at** and **Completed at** is how long the run took. This field is empty if the run hasn't completed. |
| Created at | When Vercel created the run, in ISO 8601 format. |
| Updated at | When the run was last changed, in ISO 8601 format, for example when its status or conclusion was updated. |
| External ID | The ID of the run in another system. |
| External URL | The URL of the run in another system. |
| Output | Details shown for the run in Vercel. |
| Task summary | Counts of total, pending, succeeded, and failed tasks. |
| Targets | The environments the check runs on. |
| Requires | When the check starts. |
| Blocks | What the check blocks. |
| Timeout | The timeout in milliseconds. |

---
