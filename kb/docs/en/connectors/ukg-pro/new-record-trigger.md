---
url: 'https://docs.workato.com/en/connectors/ukg-pro/new-record-trigger.md'
description: >-
  The New record trigger in the UKG Pro connector picks up new employee person
  and employment records, processing each one as a separate job.
---

# UKG Pro - New record trigger

This trigger picks up new records in your UKG Pro instance. Each new record is processed as a separate job. It checks for new records once every poll interval.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the UKG Pro object to monitor: Employee person, Employment |
| Company | Select the company to monitor. |
| When first started, this recipe should pick up events from | Employees created after this time will be processed by the recipe. If left blank, the default date will be set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| Object-specific fields | Record details specific to the object type will be provided as datapills. Refer to the [UKG Pro API documentation](https://connect.ultipro.com/documentation#/api/) for more details on the output fields of each object. |

---
