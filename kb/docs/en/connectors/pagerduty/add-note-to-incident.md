---
url: 'https://docs.workato.com/en/connectors/pagerduty/add-note-to-incident.md'
description: >-
  The Add note to incident action in the PagerDuty connector lets you add a note
  with additional description to an existing incident.
---

# PagerDuty - Add note to incident action

This action adds a note to an incident in PagerDuty.

## Input

| Field | Description |
| --- | --- |
| Incident ID **Required** | The incident ID. |
| From email **Required** | The email address of a valid user associated with the account making the request. |
| Note **Required** | Additional description to add as a note. |

## Output

| Field | Description |
| --- | --- |
| ID | The note ID. |
| User | The user for this note. It contains the following fields. ID, Type, Summary, Self, HTML URL |
| Content | The note content. |
| Created at | The date and time when this record was created. |

---
