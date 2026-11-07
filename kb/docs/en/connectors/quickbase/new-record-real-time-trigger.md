---
url: >-
  https://docs.workato.com/en/connectors/quickbase/new-record-real-time-trigger.md
description: >-
  The New record (real-time) trigger in the Quickbase connector picks up new
  records in a table in real time and processes each one as a separate job.
---

# Quickbase - New record trigger (real-time)

This trigger picks up new records in your Quickbase instance in real-time. Workato processes each record as a separate job.

## Input

| Input field | Description |
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
