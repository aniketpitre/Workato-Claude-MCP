---
url: 'https://docs.workato.com/en/connectors/salesforce/triggers/new-event.md'
description: >-
  This trigger monitors Salesforce in real-time for new PushTopic events in
  subscribed channels.
---

# Salesforce - New PushTopic event trigger (real-time)

This trigger uses the [Salesforce Streaming API](https://developer.salesforce.com/docs/atlas.en-us.202.0.api_streaming.meta/api_streaming/intro_stream.htm) to monitor Salesforce in real-time for new PushTopic events in subscribed channels. Any PushTopic events not picked up within 24 hours, for example, if the recipe was stopped for longer than 24 hours, are not be processed by the recipe. This trigger picks up events from the last 24 hours when you start the recipe, provided the PushTopic has been active for that duration.

## Prerequisites

You must [create a PushTopic](https://developer.salesforce.com/docs/atlas.en-us.202.0.api_streaming.meta/api_streaming/create_a_pushtopic.htm) object in Salesforce before you can use this trigger. Workato recommends creating focused PushTopics to minimize the number of trigger events and avoid running jobs on unnecessary trigger events.

Workato fetches the output schema as defined in the PushTopic automatically. You can define a new schema by using a SOQL query or manually specifying the fields.

![PushTopic trigger setup](/assets/pushtopic-trigger-setup.pHgIs1Kr.png)_The recipe receives data as specified in the schema_

## Input

| Input fields | Description |
| --- | --- |
| Pushtopics | Select a PushTopic to subscribe to. |
| Output schema | Define a new schema by using a SOQL query or manually adding fields. |

## Output

| Output fields | Description |
| --- | --- |
| Replay ID | A number indicating the sequence of event notifications. |
| Created date | The date and time the event was created. |
| Type | The type of trigger event. |

Additional outputs load dynamically based on the PushTopic schema.

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/scheduled-search-soql-where.md
description: >-
  This trigger searches Salesforce using a SOQL query WHERE clause on a schedule
  you specify.
---

# Salesforce - Scheduled record search using SOQL query WHERE clause trigger (batch)

This trigger searches Salesforce using a SOQL query WHERE clause on a schedule you specify and returns the results in batches.

> **SELECT CLAUSE IN SOQL**
> 
> SOQL queries don't support the `SELECT *` operation often used in SQL queries. You must specify specific fields to retrieve in the SELECT clause.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the type of Salesforce object to search for. |
| SOQL WHERE clause | Enter a SOQL query to filter records by. For example: `StageName = 'Closed Lost' AND IsClosed = false` |
| Schedule | Select how often to search Salesforce. |
| Time zone | Select a time zone for the schedule. |
| Hour | Enter the hour to search Salesforce. This field uses 24-hour format, for example: `11` for 11am or `23` for 11pm. Defaults to `00` (12am). |
| Minute | Enter how many minutes past the hour to search Salesforce in double digit format. For example: `01` for 1 minute past the hour. |
| Day of month | Enter a number between `1` and `31` to specify the day of the month to search Salesforce. Shorter months round this value down to the last day of the month. Defaults to `1`. |
| Sunday | Select whether to allow searches on Sundays. |
| Monday | Select whether to allow searches on Mondays. |
| Tuesday | Select whether to allow searches on Tuesdays. |
| Wednesday | Select whether to allow searches on Wednesdays. |
| Thursday | Select whether to allow searches on Thursdays. |
| Friday | Select whether to allow searches on Fridays. |
| Saturday | Select whether to allow searches on Saturdays. |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| Batch size | Enter the maximum number of records to contain in each batch. The default value for this field is `100` and the maximum is `2000`. Salesforce records with many custom fields require smaller batch sizes. |

## Output

| Output fields | Description |
| --- | --- |
| Range | The range of records retrieved in the current batch. |
| Scheduled time | The date and time scheduled for the search. |
| Total number of objects | The total number of matching objects retrieved from Salesforce. |
| First batch | A boolean indicating whether the current batch contains the beginning of the results list. |
| Last batch | A boolean indicating whether the current batch contains the end of the results list. |
| Starting offset | The offset number for the first record of this batch. |
| Ending offset | The offset number for the last record of this batch. |

Additional outputs load dynamically based your selected **Object**. Refer to Salesforce's [Overview of Salesforce Objects and Fields](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_concepts.htm) guide for more information on available objects and fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/scheduled-search-soql.md
description: This trigger searches Salesforce using a SOQL query on a schedule you specify.
---

# Salesforce - Scheduled records search using SOQL query trigger (batch)

This trigger searches Salesforce using a SOQL query on a schedule you specify.

> **SELECT CLAUSE IN SOQL**
> 
> SOQL queries don't support the `SELECT *` operation often used in SQL queries. You must specify specific fields to retrieve in the SELECT clause.

## Input

| Input fields | Description |
| --- | --- |
| SOQL query | Enter a SOQL query to filter records by. You must select `ID` using the `SELECT` statement for this trigger to work. |
| Schedule | Select how often to search Salesforce. |
| Time zone | Select a time zone for the schedule. |
| Hour | Enter the hour to search Salesforce. This field uses 24-hour format, for example: `11` for 11am or `23` for 11pm. Defaults to `00` (12am). |
| Minute | Enter how many minutes past the hour to search Salesforce in double digit format. For example: `01` for 1 minute past the hour. |
| Day of month | Enter a number between `1` and `31` to specify the day of the month to search Salesforce. Shorter months round this value down to the last day of the month. Defaults to `1`. |
| Sunday | Select whether to allow searches on Sundays. |
| Monday | Select whether to allow searches on Mondays. |
| Tuesday | Select whether to allow searches on Tuesdays. |
| Wednesday | Select whether to allow searches on Wednesdays. |
| Thursday | Select whether to allow searches on Thursdays. |
| Friday | Select whether to allow searches on Fridays. |
| Saturday | Select whether to allow searches on Saturdays. |
| Batch size | Enter the maximum number of records to contain in each batch. The default value for this field is `100` and the maximum is `2000`. Salesforce records with many custom fields require smaller batch sizes. |

![Salesforce Scheduled records search example](/assets/scheduled-records-search-soql-query.JTSk9dd6.png) _Example of valid query in scheduled records search_

## Output

| Output fields | Description |
| --- | --- |
| Range | The range of records retrieved in the current batch. |
| Scheduled time | The date and time scheduled for the search. |
| Total number of objects | The total number of matching objects retrieved from Salesforce. |
| First batch | A boolean indicating whether the current batch contains the beginning of the results list. |
| Last batch | A boolean indicating whether the current batch contains the end of the results list. |
| Starting offset | The offset number for the first record of this batch. |
| Ending offset | The offset number for the last record of this batch. |
| First record name | The name of the first record. |
| Last record name | The name of the last record. |
| Records | An object containing information about the current record. |

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/threshold-met-batch.md
description: >-
  This trigger monitors Salesforce for when the number of newly created objects
  reaches a threshold you specify.
---

# Salesforce - Threshold met for new records created trigger (batch)

This trigger monitors Salesforce for when the number of newly created objects reaches a threshold you specify. When Salesforce reaches the new object threshold, Workato triggers a job, retrieves the newly created objects in batches, and waits for the number of new jobs to reach the threshold again.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object type to monitor. |
| Threshold | Enter the number of records that must be created in Salesforce to trigger a new job. |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| Batch size | Enter the maximum number of records to contain in each batch. The minimum value for this field is `1` and the maximum is `10000`. Salesforce records with many custom fields require smaller batch sizes. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output fields | Description |
| --- | --- |
| Job ID | The Salesforce ID of the job. |
| Batch ID | The Salesforce ID of the batch. |
| State | The current state of the batch. For example: `Open` or `Closed` |
| Created date | The date and time the batch was created. |
| Number of records processed | The number of records processed. |
| Number of records failed | The number of records that failed to process. |

---
