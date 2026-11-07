---
url: 'https://docs.workato.com/en/connectors/filevine/new-updated-object-trigger.md'
description: >-
  The New/updated object trigger initiates a recipe in real-time when a selected
  object is created or updated in Filevine.
---

# Filevine - New/updated object trigger (real-time)

The **New/updated object** trigger monitors Filevine in real-time for newly created or updated objects of a type you specify.

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the Filevine object to monitor. |
| Event type | Select the type of event to monitor. |

## Output

| Output field | Description |
| --- | --- |
| Object ID | Unique identifier of the object that triggered the event. |
| Other | Any additional data associated with the event. |
| Timestamp | Time when the event occurred. |
| Object | Snapshot of the object at the time of the event. |
| Event | Type of event that triggered the recipe. |
| Organization ID | ID of the organization where the event originated. |
| Project ID | ID of the project related to the object. |
| User ID | ID of the user who triggered the event. |
| User type | Type of user who performed the action. |

---
