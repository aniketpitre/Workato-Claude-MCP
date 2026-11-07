---
url: 'https://docs.workato.com/en/connectors/pagerduty/new-incident.md'
description: >-
  The New incident trigger in the PagerDuty connector picks up new incidents on
  each poll interval, processing each incident as a separate job.
---

# PagerDuty - New incident trigger

This trigger checks for new incidents in PagerDuty. Checks for new events on every poll interval. Each incident is processed as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Select from the picklist or input your own value. Choose from how frequently to check for new events. |
| When first started, this recipe should pick up events from | Get incidents created since the given date/time. Leave empty to get incidents created since the recipe starts. Once recipe has been run or tested, this value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

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
