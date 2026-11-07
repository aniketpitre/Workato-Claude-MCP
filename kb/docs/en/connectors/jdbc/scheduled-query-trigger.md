---
url: 'https://docs.workato.com/en/connectors/jdbc/scheduled-query-trigger.md'
description: >-
  The JDBC scheduled query trigger runs custom SQL on a schedule you set and
  picks up new or updated rows as batches each poll interval.
---

# JDBC - Scheduled query trigger

## New/updated batch of rows via scheduled custom SQL trigger

This trigger picks up rows that are inserted/updated in the selected table or view. Each row is processed as a separate job. It checks for new/updated rows once every poll interval.

| Input field | Description |
| --- | --- |
| [SQL](#sql) | Custom SQL query to be executed at each poll interval to pick up new rows. |
| [Schedule](#schedule) | Choose how often you want the SQL to be run. |
| [Timezone](#timezone) | Choose the timezone for the schedule to be set in. |
| [Hour](#hour) | Configure the hour of the day you wish to execute the SQL query. |
| [Minute](#minute) | Configure the minute in the hour you wish to execute the SQL query. |
| [Day of month](#day-of-month) | Configure the day of the month you wish to execute the SQL query. |
| [Days of week](#days-of-week) | Select the days of the week you wish to execute the SQL query. |
| [Batch size](#batch-size) | Configure the batch size to process in each individual job for this recipe. The maximum batch size is 50,000, and the default is 100. |

## Input

### SQL

Provide the SQL to be executed to select rows. The SQL here will be used to generate the output datatree. To do this, the SQL will be executed once when you provide it. You can map datapills here to execute dynamically changing SQL statements. Remember to wrap datapills in quotes (`''`).

Avoid using limit clauses like `TOP` in your SQL. This is because the limit to the number of rows returned in the query is based on the value defined in the [**Batch size** input field](#batch-size). Adding your own limit clause will cause the action to fail.

### Schedule

Select the type of schedule you want for your integration use case. This input field is a pick list with the following available choices:

- hourly
- daily
- monthly

### Timezone

Select the timezone for the scheduler to be set in. This is a required field.

### Hour

Configure the hour of the day you wish to execute the scheduled SQL query. This is required only if you selected **daily** or **monthly** as the [Schedule](#schedule).

### Minute

Configure the minute in the hour you wish to execute the scheduled SQL query. This is required.

### Day of month

Provide a value between **1** to **31** for the day of the month. In shorter months, the values may be rounded down to the last day of the month. For example: if you use the value **31** and the month ends before the 31st, the trigger will run the SQL query on the last day of the month (for example, 28th Feb, 31st Mar, 30th Apr, and so on)

Needed only if you selected **monthly** as the [Schedule](#schedule). This is an optional field that defaults to first day of the month if left empty.

### Days of week

Choose the days of the week you wish to execute the scheduled SQL query. This is required only if you selected **hourly** and **daily** as the [Schedule](#schedule). If you selected **hourly**, the trigger will execute the SQL hourly on days that are selected here.

### Batch size

Batch size of rows to return in each job. This can be any number between **1** and the maximum batch size. The maximum batch size is 50,000, and the default is 100.

In any given poll, if there are fewer rows than the configured batch size, this trigger will deliver all rows as a smaller batch.

---
