---
url: 'https://docs.workato.com/en/connectors/openapi/new-record-batch-trigger.md'
description: >-
  The New/updated record batch trigger in the OpenAPI connector runs when
  records of the selected object are created or updated, returning them in
  batches.
---

# OpenAPI - New/updated record batch trigger

The **New/updated record batch** trigger runs when a record of the selected object is created or updated. The list of objects is dynamically generated based on the API endpoints found in the [OpenAPI document](https://restfulapi.net/).

![New/updated record batch trigger](/assets/openapi-new-updated-record-batch-trigger.NRTK4VI9.png)_New/updated record batch trigger_

## Input

| Input fields | Description |
| --- | --- |
| Trigger poll interval | Select how frequently to check for new events. |
| Object | Select an object from the drop-down list of linked objects. |
| Timestamp record field | Determine the latest timestamp for filtering when retrieving the next batch of events. |
| When first started, this recipe should pick up events from | When you start recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get events created one hour ago. |
| Filter | Provide configuration and filter criteria for checking for new or updated records. |
| Record list field | Records in this field are available in the output of this trigger. Defaults to `Results`. |
| Identifier record hold | Use this field to uniquely identify individual records. This is required for deduplication to ensure each unique record is processed only once. Defaults to `Id`. |
| Set trigger condition | Define further guidelines added to a specific trigger to filter the type of trigger events selected for processing. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

---
