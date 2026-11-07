---
url: >-
  https://docs.workato.com/en/features/scheduler/actions/wait-until-specified-time.md
description: >-
  Use the Wait until specified time action to specify the time to wait until
  before proceeding on to the next step.
---

# Scheduler by Workato - Wait until specified time action

The **Wait until specified time** action allows you to specify the time to wait until before proceeding on to the next step. If the time specified is in the past, the recipe immediately proceeds on to the next step.

![Wait until the specified time](/assets/scheduler_wait_until.qG6Cn4yC.png)

## Input

| Field | Description |
| --- | --- |
| Time | Specify the date and time for the job to resume. The job pauses until this time, then continues its subsequent actions. The time entered uses your workspace's timezone. |

How can I set a dynamic time?

You can configure the recipe to wait until a specific time, such as next Monday at 8:00 AM PST, before the job proceeds to the next step.

Complete the following steps to set up a dynamic time for resuming the job:

1. Switch the **Time** input field to [formula mode](/en/formulas/formula-mode).
   
2. Enter a [date formula](/en/formulas/date-formulas). For example, the following date formula configures the recipe to wait until the next Monday at 8:00 AM PST before proceeding to the next step:
   
   `today.beginning_of_week + 7.days + 8.hours`
   

## Output

| Field | Description |
| --- | --- |
| Resumed at | The timestamp at which the job resumed. |
