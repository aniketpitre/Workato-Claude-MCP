---
url: >-
  https://docs.workato.com/en/connectors/ceridian-dayforce/new-updated-employee-trigger.md
description: >-
  The New/updated employee trigger activates when an employee is created or
  updated in Ceridian Dayforce.
---

# Ceridian Dayforce - New/updated employee trigger

The **New/updated employee** trigger activates when an employee is created or updated in Ceridian Dayforce.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Select how frequently to check for new events. Defaults to minutes if left blank. Minimum value allowed is minutes. Refer to [Polling intervals](https://docs.workato.com/en/recipes/polling-intervals.html) for more information. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| XRefCode | The external reference codes for the new/updated employees returned in your search. |
