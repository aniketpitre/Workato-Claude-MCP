---
url: 'https://docs.workato.com/en/connectors/workday-rest/new-worker-trigger.md'
description: >-
  The New worker trigger in the Workday REST connector picks up workers created
  in your Workday instance, processing each as a separate job.
---

# Workday REST - New worker trigger

This trigger picks up workers that are created in your Workday instance. Each row is processed as a separate job. When first started, all existing workers will be processed as individual jobs. Subsequently, it triggers when a worker is created. It checks for new rows once every poll interval.

![New worker trigger](/assets/new-worker-trigger.Crjmur0b.png)_New worker trigger_

## Input

| Input field | Description |
| --- | --- |
| Name filter | **Optional**. Use this to filter workers by name. Only workers with names that start with the provided text will be processed. |

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
