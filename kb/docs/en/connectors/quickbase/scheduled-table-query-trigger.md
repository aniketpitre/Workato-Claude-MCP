---
url: >-
  https://docs.workato.com/en/connectors/quickbase/scheduled-table-query-trigger.md
description: >-
  The Scheduled record search using query trigger in the Quickbase connector
  runs a query on a set schedule and returns matching records in batches.
---

# Quickbase - Scheduled record search using query trigger (batch)

This trigger executes a Quickbase query on a specified schedule. Records meeting the query are returned in lists of records for each trigger event.

## Input

| Field | Description |
| --- | --- |
| Application | Select an application in your Quickbase account. |
| Application token | Required if this application is configured to require tokens for data access. You can obtain this value from the application in **Settings > App properties > Manage application token**. |
| Table | Select the table to query. |
| Schedule | Specify the schedule for the query. You can choose between an hourly, daily, or monthly occurrence. |
| Time zone | Select a timezone from the list. |
| Hour | Specify the hour you plan the query to occur. Hours are listed in 24-hour format. For example, 11 for 11am, 23 for 11pm. Defaults to 00 (12am) if left empty. |
| Minute | Minutes past the hour. For example, 00 for 0 minutes. |
| Day of month | Specify the day of the month you plan the query to occur. Numbers 1 - 31 are rounded down to the last day of month for shorter months. Defaults to first day of the month if left empty. |
| Sunday | Select **Yes** from the drop-down if you plan for the query to run on Sunday. |
| Monday | Select **Yes** from the drop-down if you plan for the query to run on Monday. |
| Tuesday | Select **Yes** from the drop-down if you plan for the query to run on Tuesday. |
| Wednesday | Select **Yes** from the drop-down if you plan for the query to run on Wednesday. |
| Thursday | Select **Yes** from the drop-down if you plan for the query to run on Thursday. |
| Friday | Select **Yes** from the drop-down if you plan for the query to run on Friday. |
| Saturday | Select **Yes** from the drop-down if you plan for the query to run on Saturday. |
| Query | Use a Quickbase query to fetch only records that match your query. Query syntax is `{'fid'.operator.'matching_value'}`. For example, `{'7'.EX.'Test'}`. |
| Batch size | Enter the number of records you plan for this action to return. The minimum is 1 and maximum is 1000. |

## Output

The output datatree contains information about the records returned by the query. This includes the range of record IDs, the records themselves, and the scheduled time.

| Field | Description |
| --- | --- |
| Range | The range of record IDs retrieved from the search. |
| First record ID | The ID of the first record in the batch. |
| Last record ID | The ID of the last record in the batch. |
| Records | This contains a list of records. Each record contains information about the fields of the record. |
| Scheduled time | The time the search was executed. |
| Total number of records | The number of records retrieved in this search. |
| First batch | Whether this is the first batch of records. |
| Last batch | Whether this is the last batch of records. |
| Starting offset | The offset number for the first record of this batch. |
| Ending offset | The offset number for the last record of this batch. |
