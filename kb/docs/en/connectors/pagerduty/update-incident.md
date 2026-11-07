---
url: 'https://docs.workato.com/en/connectors/pagerduty/update-incident.md'
description: >-
  The Update incident action in the PagerDuty connector lets you update an
  existing incident, including changing its status, by incident ID.
---

# PagerDuty - Update incident action

This action updates an incident in PagerDuty.

## Input

| Field | Description |
| --- | --- |
| ID **Required** | The incident ID. |
| From **Required** | The email address of the user making the request. |
| Status | Select the updated status of the incident. |

## Output

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
