---
url: 'https://docs.workato.com/en/connectors/greenhouse/move-application-v3.md'
description: >-
  The Move application (v3) action moves an application to a different stage or
  job in Greenhouse using the v3 API.
---

# Greenhouse - Move application (v3) action

The **Move application (v3)** action moves an application to a different stage within the same job or transfers it to another job in Greenhouse using the v3 API.

This action is available for OAuth 2.0 connections only.

## Input

| Input field | Description |
| --- | --- |
| Application ID | Enter the ID of the application to move. |
| From stage ID | Enter the ID of the stage the application is currently in. |
| To stage ID | Enter the ID of the stage to move the application to. |
| To job ID | Enter the ID of the job to transfer the application to. |
| Email from user ID | Enter the user ID used as the sender for the move notification email. |

## Output

| Output field | Description |
| --- | --- |
| Application ID | ID of the application. |
| Moved | Indicates whether the application was successfully moved. |

---
