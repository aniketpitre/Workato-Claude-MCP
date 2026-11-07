---
url: 'https://docs.workato.com/en/connectors/quickbase/new-updated-record-trigger.md'
description: >-
  The New/updated record trigger in the Quickbase connector picks up new or
  updated records in a table once every poll interval, one job per record.
---

# Quickbase - New/updated record trigger

This trigger picks up new or updated records in your Quickbase instance. It checks for new or updated records once every poll interval and Workato processes each record as a separate job.

## Input

| Field | Description |
| --- | --- |
| Application | Select an application in your Quickbase account. |
| Application token | Required if this application is configured to require tokens for data access. You can obtain this value from the application in **Settings > App properties > Manage application token**. |
| Table | Select the table to monitor for new or updated records. |
| Query | Use a Quickbase query to fetch only records that match your query. Query syntax is `{'fid'.operator.'matching_value'}`. For example, `{'7'.EX.'Test'}`. |
| When first started, this recipe should pick up events from | Fetch records created after a specified time. You can't change this value after you test or run this recipe. Learn more about this [input field](/en/recipes/triggers#since-from). |
| Trigger poll interval | Determine how frequently to check for new events. Defaults to five minutes if left blank. Minimum value allowed is five minutes. |

## Output

The output datatree contains information about the new or updated record. This includes the record ID, the fields of the record, and the timestamp.

| Field | Description |
| --- | --- |
| Record ID | The ID of the new or updated record. |
| Fields | The fields of the new or updated record. |
| Created time | The time the record was created. |
| Modified time | The time the record was last modified. |

---

---
url: >-
  https://docs.workato.com/en/connectors/quickbase/new-updated-record-real-time-trigger.md
description: >-
  The New/updated record (real-time) trigger in the Quickbase connector picks up
  new or updated records in a table in real time, one job per record.
---

# Quickbase - New/updated record trigger (real-time)

This trigger picks up new records in your Quickbase instance in real-time. Workato processes each record as a separate job.

## Input

| Field | Description |
| --- | --- |
| Application | Select an application in your Quickbase account. |
| Application token | Required if this application is configured to require tokens for data access. You can obtain this value from the application in **Settings > App properties > Manage application token**. |
| Table | Select the table to monitor for new records. |
| When first started, this recipe should pick up events from | Fetch records created after a specified time. You can't change this value after you test or run this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output datatree contains information about the new record. This includes the record ID, the fields of the record, and the timestamp.

| Field | Description |
| --- | --- |
| Record ID | The ID of the new record. |
| Fields | The fields of the new record. |
| Created time | The time the record was created. |
| Modified time | The time the record was last modified. |

---

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

---
