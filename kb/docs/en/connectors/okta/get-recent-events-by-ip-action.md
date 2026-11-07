---
url: 'https://docs.workato.com/en/connectors/okta/get-recent-events-by-ip-action.md'
description: >-
  The Get recent log on events by IP address action in the Okta connector lets
  you retrieve up to 100 log events from the last 12 hours for an IP.
---

# Okta - Get recent log on events by IP address action

This action retrieves a log on recent events that originated from a specified IP address.

This action will retrieve up to 100 actions from the last 12 hours.

![Get recent log on events by IP address ction](/assets/get-recent-log-on-events-by-ip-address.CJGY52A5.png)_Get recent log on events by IP address action_

## Input

| Field | Description |
| --- | --- |
| IP address | The IP address as the source of the log events. |

## Output

The output datatree contains a list of logs on events. Each log event contains information about the event like the timestamp, the actor, the client used, the authentication and security contents.

Refer to [Event outputs](/en/connectors/okta/events-output-datatree) for the full list of output fields.

---
