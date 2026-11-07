---
url: >-
  https://docs.workato.com/en/connectors/greenhouse/advance-application-action.md
description: >-
  The Advance application action in the Greenhouse connector lets you move an
  active application to the next stage in the hiring pipeline.
---

# Greenhouse - Advance application action

This action moves the application to the next stage. Note that only applications with the [active status](/en/connectors/greenhouse/object-types#application-object) can be advanced.

> **DEPRECATION NOTICE**
> 
> This action uses the legacy Greenhouse v1 API, which Greenhouse will remove on August 30, 2026.
> 
> Migrate to the [Move application (v3)](/en/connectors/greenhouse/move-application-v3) action before this date. The v3 action supports broader transitions, including moving applications across stages and jobs.
> 
> Refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) to migrate your recipes.

![Advance application action](/assets/advance-application-action.Dq67EXDt.png)_Advance application action_

## Input

| Input field | Description |
| --- | --- |
| Application ID | The unique Greenhouse application ID. |
| From stage ID | The ID of the job stage this application is currently in. |

## Output

The output of this action is the application's information which reflects its new status.

Find out more about the [application object](/en/connectors/greenhouse/object-types#application-object).
