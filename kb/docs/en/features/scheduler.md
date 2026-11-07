---
url: 'https://docs.workato.com/en/features/scheduler.md'
description: >-
  Run recipes at customized intervals using the Scheduler by Workato. Configure
  simple or complex schedules to trigger workflows independent of external app
  events.
---

# Scheduler by Workato

[Video](https://www.youtube.com/embed/lLOnyzPYdGM)

Scheduler by Workato is a native app designed to run recipes at specified intervals. You can define straightforward schedules, such as running a recipe hourly or daily, as well as more advanced configurations, like running a recipe every two weeks or only on weekdays.

For workflows that do not rely on events from other applications, Scheduler by Workato enables precise control over how frequently a recipe runs.

> **LONG ACTIONS JOB SEQUENCE**
> 
> If your recipe has a long action step and job, note that [when the action is put on hold](/en/recipes/long-actions#how-does-this-work), Workato automatically disregards the job sequence. The next job begins to process even if the previous job is not finished and the recipe concurrency is set to `1`.

## Triggers

- [New recurring event](/en/features/scheduler/triggers/new-recurring-event)

> **DEPRECATED TRIGGERS**
> 
> The following triggers are deprecated:
> 
> - New scheduled event
> - New scheduled event (advanced)
> 
> Support for existing recipes using the deprecated triggers will continue. However, users won't be able to select these triggers when creating new recipes.
> 
> Old recipes using the deprecated triggers will continue to run as configured. You can continue to run the recipe without any disruptions.

## Actions

[Video](https://www.youtube.com/embed/dXJIUGC6yZw?rel=0&rel=0)

The following actions are supported:

- [Get current time](/en/features/scheduler/actions/get-current-time)
- [Wait time duration](/en/features/scheduler/actions/wait-for-time-duration)
- [Wait until the specified time](/en/features/scheduler/actions/wait-until-specified-time)

## Supported datetime formats

Scheduler by Workato supports the following datetime formats for all custom inputs:

| Datetime format | Description | Example |
| --- | --- | --- |
| %H:%M:%S | 24-hour format with seconds | 15:23:23 |
| %H:%M | 24-hour format without seconds | 15:23 |
| %I:%M %P | 12-hour format without seconds | 3:23 PM |
| %I:%M:%S %P | 12-hour format with seconds | 3:23:23 PM |

---
