---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/get-activity-history-action.md
description: >-
  Configure the Get activity history (batch) action to retrieve a full audit
  trail of request creation, task assignments, status updates, and comments.
---

# Get activity history (batch) action

Use the **Get activity history (batch)** action to retrieve a complete activity history for requests, including creation, task assignments, status updates, and user comments. This provides a full audit trail to track all activities related to the requests.

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Choose the workflow app you plan to get activity history for. |
| Record ID | Specify the request to get activity history for. Use a datapill or enter the exact ID. |
| Activity type | Choose activity types to search for. |
| Performed by | Enter an email address of a specific user to show only activities performed by a specific user. |
| Activities from | Retrieve activities that occurred on or after this date. |
| Activities to | Retrieve activities that occurred on or before this date. |
| Sort direction | Select the order in which activities are retrieved. Default is oldest to newest. |
| Next page token | Get activity records starting from this offset. |

## Output

| Output field | Description |
| --- | --- |
| Activity records | This object contains details about the activities requested. |
| Activity ID (Activity records) | A unique identifier for the activity performed. |
| Request record ID (Activity records) | The ID of the request record associated with the activity. |
| Activity type (Activity records) | The type or category of the activity (for example, comment or status change). |
| Comment text (Activity records) | The content of a comment, if the activity involved one. |
| Activity summary (Activity records) | A brief description of what the activity entailed. |
| Performed at (Activity records) | The date and time when the activity was executed. |
| List size (Activity records) | The total number of items in the list (if part of a paginated response). |
| List index (Activity records) | The position of the current item within the list. |
| Performed by (Activity records) | An object nested within the `Activity records` object containing details about the user who performed the activity. |
| User ID (Performed by) | The user's ID. |
| Email (Performed by) | The user's email address. |
| Status (Performed by) | The user's status. |
| List size | The size of the list. |
| List index | The position in the list. |
