---
url: 'https://docs.workato.com/en/connectors/greenhouse/reject-application-action.md'
description: >-
  The Reject application action in the Greenhouse connector lets you reject an
  active application and set its status to rejected, with an optional email.
---

# Greenhouse - Reject application action

This action rejects an application and changes the status to `rejected`. Note that only applications with the [active status](/en/connectors/greenhouse/object-types#application-object) can be rejected.

> **DEPRECATION NOTICE**
> 
> This action uses the legacy Greenhouse v1 API, which Greenhouse will remove on August 30, 2026.
> 
> Migrate to the [Reject application (v3)](/en/connectors/greenhouse/reject-application-v3) action before this date.
> 
> Refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) to migrate your recipes.

![Reject application action](/assets/reject-application-action.B6D2CmDw.png)_Reject application action_

## Input

| Input field | Description |
| --- | --- |
| Application ID | The unique Greenhouse application ID. |
| Email template ID | The template to use for the rejection email. |
| Rejection reason | The reason for the rejection. |
| Send email at | Provide a date and time for the rejection email. This can be used to coordinate the release of updates for the application. |

## Output

The output of this action is the application's information which reflects the `rejected` status.

Find out more about the [application object](/en/connectors/greenhouse/object-types#application-object).

---
