---
url: 'https://docs.workato.com/en/connectors/ukg-pro/terminated-employee-trigger.md'
description: >-
  The Terminated employees trigger in the UKG Pro connector picks up terminated
  employee events, processing each termination as a separate job.
---

# UKG Pro - Terminated employees trigger

This trigger picks up terminated employee events. Each termination event is processed as a separate job. It checks for terminated employees once every poll interval.

## Input

| Input field | Description |
| --- | --- |
| Company | Select the company to monitor. |
| When first started, this recipe should pick up events from | Employees terminated after this time will be processed by the recipe. If left blank, the default date will be set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| Employee fields | Refer to the [UKG Pro API documentation](https://connect.ultipro.com/documentation#/api/) for more information on the employee object. |

---
