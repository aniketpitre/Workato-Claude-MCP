---
url: 'https://docs.workato.com/en/connectors/pagerduty/search-incident.md'
description: >-
  The Search incident action in the PagerDuty connector lets you find existing
  incidents by date range, incident key, statuses, or urgencies.
---

# PagerDuty - Search incident action

This action searches for existing incidents in PagerDuty.

## Input

| Field | Description |
| --- | --- |
| Since | Start of the date range |
| Until | End of the date range |
| Incident key | Incident de-duplication key. Incidents with child alerts do not have an incident key; querying by incident key will return incidents whose alerts have alert\_key matching the given incident key. |
| Statuses | status may be triggered, acknowledged, and resolved. Separate the values with comma. |
| Urgencies | Urgency may be high or low. Separate the values with comma. |

## Output

The output to this action is a list of incidents. Each incident contains the following field.

| Field | Description |
| --- | --- |
| ID | The incident ID. |
| Type | A string that determines the schema of the object. This must be the standard name for the entity. |
| Summary | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier. |
| Self | The API show URL at which the object is accessible. |
| HTML URL | The URL at which the entity is uniquely displayed in the Web app. |
| Incident number | The number of the incident. This is unique across your account. |
| Created at | The date and time when this record was created. |
| Status | The current status of the incident. |
| Incident key | The incident's de-duplication key. |
| Pending actions | The list of pending actions on the incident. Each pending action contains the following fields. Type of action, Updated at |
| Service | The service object contains the following fields. ID, Type, Summary, Self, HTML URL |
| Assignments | List of all assignments for this incident. This list will be empty if the Incident.status is resolved. |
| Acknowledgments | List of all acknowledgments for this incident. This list will be empty if the Incident.status is resolved or triggered. Each acknowledgment contains the following fields. At, Acknowledger |
| Last status change at | The time at which the status of the incident last changed. |
| Last status change by | The agent that created or updated this incident. The agent object contains the following fields. ID, Type, Summary, Self, HTML URL |
| First trigger log entry | This object contains the following fields. ID, Type, Summary, Self, HTML URL |
| Escalation policy | This object contains the following fields. ID, Type, Summary, Self, HTML URL |
| Teams | A list of teams involved in the incident's lifecycle. Each team contains the following fields. ID, Type, Summary, Self, HTML URL |
| Urgency | The current urgency of the incident. |

---
