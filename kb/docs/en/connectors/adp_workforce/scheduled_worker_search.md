---
url: >-
  https://docs.workato.com/en/connectors/adp_workforce/scheduled_worker_search.md
description: >-
  The Scheduled worker search trigger in the ADP Workforce Now connector picks
  up workers matching a search filter on a schedule, in batches.
---

# ADP Workforce Now - Scheduled worker search trigger

This trigger picks up entries that match a specified search filter. Entries are processed as a list of a specified batch size. It checks for entries based on the specified schedule.

## Input

| Input field | Description |
| --- | --- |
| Role code | Select the type of worker to filter for this trigger. Available options are: - Employee - Manager - Practitioner - Administrator - Supervisor |
| Trigger on | Select the type of schedule - **Specific interval** or **Specific date/time** |
| Schedule settings (**Specific interval**) | Every | Select the interval between each search. Select one of these options: - 5 minutes - 15 minutes - 30 minutes - 45 minutes - One hour - One day - One week - 30 days |
| Start at | Date and time to begin the first search. Leave blank to begin immediately when the recipe is first started. |
| Schedule settings (**Specific date/time**) | Timezone | Choose the timezone for the schedule to be set in. |
| Hour | Configure the hour of the day to run the search. |
| Minute | Configure the minute of the hour to run the search. |
| Days of the week | Select 'Yes' for each of the days you wish to run the search. |
| Batch size | Configure the batch size of the list of entries in each individual job. This defaults to **100**. Maximum batch size is **100**. |

## Output

The output of this trigger is a list of workers. The attributes of each worker is based on the worker object in your ADP Workforce Now instance. All custom fields are supported.
