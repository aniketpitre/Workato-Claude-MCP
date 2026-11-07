---
url: 'https://docs.workato.com/en/connectors/pagerduty/list-log-entries.md'
description: >-
  The List log entries action in the PagerDuty connector lets you retrieve log
  entries within a date range, with options to filter the results.
---

# PagerDuty - List log entries action

This action lists log entries for the specified incident in PagerDuty.

## Input

| Field | Description |
| --- | --- |
| Since | Start of the date range |
| Until | End of the date range |
| Is overview | True will return a subset of log entries that shows most important changes. |
| Include | Can be incidents, services, teams, and channels. Separate the values with comma. |

## Output

The output to this action is a list of log entries. Each log entry contains the following fields.

| Field | Description |
| --- | --- |
| ID | The log entry ID. |
| Type | A string that determines the schema of the object. This must be the standard name for the entity. |
| Summary | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier. |
| Self | The API show URL at which the object is accessible.i |
| HTML URL | The URL at which the entity is uniquely displayed in the Web app. |
| Created at | The date and time at which the log entry was created. |
| Agent | The agent who created or updated the incident log entry. |
| Channel | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channeltype. |
| Incident | An incident object. This object contains the following fields. ID, Type, Summary, Self, HTML URL |
| Teams | A list of teams involved in the incident's lifecycle. Each team contains the following fields. ID, Type, Summary, Self, HTML URL |
| Context | Contexts to be included with the trigger such as links to graphs or images. |
| Event details | A description about the event. |

---
