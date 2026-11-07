---
url: >-
  https://docs.workato.com/en/connectors/hubspot/triggers/new-updated-record-batch.md
description: >-
  The New/updated record batch trigger monitors new or updated records in your
  HubSpot instance and processes records in batches.
---

# HubSpot - New/updated record trigger (batch)

The **New/updated record** batch trigger monitors new or updated records in your HubSpot instance. It checks for new jobs once every poll interval and retrieves all new or updated instances of the object. It processes these records in batches instead of processing a single record per job. To configure this trigger, you must first select the object you plan to trigger jobs off.

This trigger supports the following objects:

- Contact
- Company
- Deal
- Ticket

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object you plan to monitor. |
| Properties | If not configured, the default set of properties for each record type is returned. You can retrieve custom sets of properties by configuring this field. Custom fields are supported. |
| Filter Groups | Use filters to only trigger on created/updated records that meet your filter criteria. When multiple filter groups are provided, they are combined using a logical AND operator. You can have a maximum of two filter groups. Last modified date is unavailable to use as a property for filtering. |
| Batch Size | Provide number of records to return in each job. Minimum is 1 and maximum is 100. Defaults to 100. |
| When first started, this recipe should pick up events from | Configure this field to retrieve records that have been created since a time in the past. Leave blank to pull records from one hour ago. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

Workato returns a list representing new or updated records. You can use these datapills in subsequent recipe steps. The output datapills depend on what you select in the **Properties** input field. If this field is blank, a default set of properties are returned.
