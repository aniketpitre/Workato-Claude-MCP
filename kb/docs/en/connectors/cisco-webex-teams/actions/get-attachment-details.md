---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/actions/get-attachment-details.md
description: >-
  The Get attachment details action in the Cisco Webex Teams connector lets you
  retrieve details of a specific attachment action by its ID.
---

# Cisco Webex Teams - Get attachment details action

This action retrieves the details of a specific attachment in Cisco Webex Teams.

## Input

| Field | Description |
| --- | --- |
| Attachment action ID | Enter the unique ID of the attachment to retrieve. You can obtain this value from the output of the [New button submission trigger](/en/connectors/cisco-webex-teams/triggers/new-button-submission). |
| Input schema | Specify the input schema. Ensure it matches the schema defined in the upstream button triggering this recipe. |

## Output

| Field | Description |
| --- | --- |
| Attachment action ID | The unique ID of the attachment action. |
| Message ID | The ID of the message associated with the attachment action. |
| Room ID | The ID of the room where the attachment action occurred. |
| Type | The type of the attachment action. |
| Person ID | The ID of the person who performed the attachment action. |
| Inputs | The inputs provided during the attachment action. |
| Created | The timestamp when the attachment action was created. |
