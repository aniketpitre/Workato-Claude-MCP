---
url: >-
  https://docs.workato.com/en/connectors/greenhouse/mark-candidate-as-hired-action.md
description: >-
  The Mark candidate as hired action in the Greenhouse connector lets you set an
  active application's status to hired and set the start date.
---

# Greenhouse - Mark candidate as hired action

This action changes the status of the application to `hired`. Note that only applications with the [active status](/en/connectors/greenhouse/object-types#application-object) can be hired.

> **DEPRECATION NOTICE**
> 
> This action uses the legacy Greenhouse v1 API, which Greenhouse will remove on August 30, 2026.
> 
> Migrate to the [Mark candidate as hired (v3)](/en/connectors/greenhouse/mark-candidate-v3) action before this date.
> 
> Refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) to migrate your recipes.

![Mark candidate as hired action](/assets/mark-candidate-as-hired-action.Cmnj3hh_.png)_Mark candidate as hired action_

## Input

| Input field | Description |
| --- | --- |
| Application ID | The unique Greenhouse application ID. |
| Start date | The start date of the newly hired candidate. |

## Output

The output of this action is the application's information which reflects the `hired` status.

Find out more about the [application object](/en/connectors/greenhouse/object-types#application-object).
