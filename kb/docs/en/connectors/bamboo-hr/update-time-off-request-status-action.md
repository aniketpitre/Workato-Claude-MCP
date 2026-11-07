---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/update-time-off-request-status-action.md
description: >-
  The Update time off request status action in the BambooHR connector lets you
  approve, deny, or cancel a specified time off request.
---

# BambooHR - Update time off request status action

This action updates the status of a specified time off request. Managers can approve or deny the request, whereas requester can cancel the request.

## Input

![Update time off request status action](/assets/update-time-off-request-action.Dmy6W2hi.png)_Update time off request status action_

| Input field | Description |
| --- | --- |
| Request ID _required_ | The ID of the time off request to be approved/canceled/denied. |
| Status _required_ | The new status of the time off request. Select from the picklist or input either approved, canceled or denied. |
| Note | Enter any notes you want to attach to the status updated. By default note will be made on behalf of the person performing the status update. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status indicating the outcome of the request. |
