---
url: 'https://docs.workato.com/en/connectors/ukg-pro/updated-employee-trigger.md'
description: >-
  The New/updated employees trigger in the UKG Pro connector picks up new or
  updated employees, processing each one as a separate job.
---

# UKG Pro - New/updated employees trigger

This trigger picks up new or updated employees in your UKG Pro instance. Each new employee is processed as a separate job. It checks for new or updated employees once every poll interval.

## Input

| Input field | Description |
| --- | --- |
| Poll interval | The frequency to check for new or updated employees. |
| When first started, this recipe should pick up events from | Employees created after this time will be processed by the recipe. If left blank, the default date will be set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| Employee fields | Refer to the [UKG Pro API documentation](https://connect.ultipro.com/documentation#/api/) for more information on the employee object. |

---
