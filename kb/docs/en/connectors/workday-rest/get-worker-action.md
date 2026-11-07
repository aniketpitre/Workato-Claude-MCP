---
url: 'https://docs.workato.com/en/connectors/workday-rest/get-worker-action.md'
description: >-
  The Get worker by ID action in the Workday REST connector lets you retrieve
  the full details of a worker record using its Workday ID.
---

# Workday REST - Get worker by ID action

Use this action to get details of a worker by the workday ID.

![Get worker by ID action](/assets/get-worker-by-id.BunYkz4R.png)_Get worker by ID action_

## Input

| Input field | Description |
| --- | --- |
| Worker ID | Workday ID of the worker record to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| Descriptor | Worker full name |
| ID | Workday ID or the worker record. |
| HREF | API resource URL of the worker record. |
| Primary supervisory organization | Primary supervisory organization object of this worker record. Contains descriptor (full name), Workday ID and HREF. |
| Business title | Full business title of the worker record. |
| Primary work email | Primary work email of the worker record. |
| Is manager | Boolean data. `True` if the worker record is a manager. |
| Primary work phone | Primary phone number of the worker record. |
| Location | Location object of this worker record. Contains descriptor (full name) and Workday ID. |
| Primary work address text | Full primary address of the worker record. |
| Supervisory organizations managed | Supervisory organizations managed by the worker record. |
| Years of service | Years of service, as an integer, by the worker. |
| Date of birth | Date of birth of the worker record. Format: YYYY-MM-DD |

---
