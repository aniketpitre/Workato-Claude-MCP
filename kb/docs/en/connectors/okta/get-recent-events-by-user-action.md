---
url: >-
  https://docs.workato.com/en/connectors/okta/get-recent-events-by-user-action.md
description: >-
  The Get recent log on events by user action in the Okta connector lets you
  retrieve up to 100 log events from the last 12 hours for a specific user.
---

# Okta - Get recent log on events by user action

This action retrieves a log on recent events for a specific user. This action uses the email address to identify the user.

This action will retrieve up to 100 actions from the last 12 hours.

![Get recent log on events by user ction](/assets/get-recent-log-on-events-by-user.BpQC--eJ.png)_Get recent log on events by user action_

## Input

| Field | Description |
| --- | --- |
| User ID | The unique ID of the target user. |

## Output

The output datatree contains a list of logs on events. Each log event contains information about the event like the timestamp, the actor, the client used, the authentication and security contents.

Refer to [Event outputs](/en/connectors/okta/events-output-datatree) for the full list of output fields.
