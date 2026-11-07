---
url: 'https://docs.workato.com/en/connectors/salesforce/triggers/deleted-record.md'
description: This trigger monitors Salesforce for deleted objects of a type you specify.
---

# Salesforce - Deleted record trigger

This trigger monitors Salesforce for deleted objects of a type you specify.

The object picklist only fetches soft-deleted records which remain in Salesforce for a limited period (typically 15 days) after deletion and are stored in the Recycle Bin.

If you cannot find an object in the picklist, its records are likely hard deleted immediately upon deletion. Hard-deleted records are permanently removed from Salesforce and aren’t stored in the Recycle Bin. These objects aren’t supported by the **Deleted object** trigger.

To resolve the issue, configure the object so that its records are soft deleted and retained in the Recycle Bin for 15 days, if applicable. Junction records (used to create many-to-many relationships) are usually hard deleted and cannot be configured for soft-deletion. Contact your Salesforce administrator for more details about how your organization handles deletions.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the standard or custom object type to monitor. |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output of this trigger varies based on your selected **Object** and **Fields to retrieve**. Refer to Salesforce's [Overview of Salesforce Objects and Fields](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_concepts.htm) guide for more information on available objects and fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/export-new-records.md
description: >-
  This trigger monitors Salesforce for new records that match the SOQL WHERE
  clause you provide and retrieves them as a CSV stream.
---

# Salesforce - Export new records trigger

This trigger monitors Salesforce for new records that match the SOQL WHERE clause you provide and retrieves them as a CSV stream.

There is an expected delay when this trigger creates a job. The job processes after a query is completed in Salesforce. You can't test recipes using this trigger due to the processing delay.

This trigger uses [V2.0 of the Salesforce Bulk API](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/queries.html). Refer to the [Salesforce bulk operations](/en/connectors/salesforce/salesforce-bulk) guide for more information about bulk operations.

> **REPLICATE DATA TO A DATA WAREHOUSE**
> 
> You can use this trigger with the [Get object schema action](/en/connectors/salesforce/database-syncs#get-object-schema-action) to fetch schema information from a Salesforce object and replicate it to a data warehouse.

Refer to the [ETL/ELT](/en/features/etl-elt-guide#bulk-vs-batch) documentation for more information about bulk triggers and ELT/ETL processes.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the standard or custom object type to monitor. |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| SOQL WHERE clause | Enter a SOQL query to filter records by. For example: `StageName = 'Closed Lost' AND IsClosed = false`. Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information. |
| When exporting records to form the CSV, fetch them in batches of | Enter the maximum number of records to process in each batch. Defaults to `10000`. |
| Include deleted records? | Select whether to include deleted records in the results. Defaults to `No`. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output fields | Description |
| --- | --- |
| All records successfully processed | Indicates whether all CSV rows across Salesforce bulk jobs processed successfully. |
| Number of records processed | The total number of CSV rows processed in Salesforce, excluding the header row. |
| Number of records failed | The total number of CSV rows that encountered issues and were not processed in Salesforce. |
| Number of retried records | The total number of CSV rows that retried processing in Salesforce. This field is relevant for the [Retry objects bulk job in Salesforce from CSV file](/en/connectors/salesforce/actions/retry-job-csv) action. |
| CSV content | The contents of the retrieved record as a CSV stream. You can write the CSV stream to a file using a file connector, such as Box or SFTP. You can also parse it to use as a list in Workato using the [Parse CSV](/en/connectors/csv-by-workato/parse-csv-action) action in the CSV tools by Workato utility connector. |
| Object name | The name of the retrieved object. |
| Object schema | An object containing information about the object's fields, such as `Field name`, `Custom field?`, and `Length`. |
| Created from | The date and time the object was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/export-new-updated-records.md
description: >-
  This trigger retrieves Salesforce records created or updated since the last
  job as a CSV stream.
---

# Salesforce - Export new/updated records trigger

This trigger monitors Salesforce for newly created or updated records that match the SOQL WHERE clause you provide and retrieves them as a CSV stream.

There is an expected delay when this trigger creates a job. The job processes after a query is completed in Salesforce. You can't test recipes using this trigger due to the processing delay.

This trigger uses [V2.0 of the Salesforce Bulk API](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/queries.html). Refer to the [Salesforce bulk operations](/en/connectors/salesforce/salesforce-bulk) guide for more information about bulk operations.

> **REPLICATE DATA TO A DATA WAREHOUSE**
> 
> You can use this trigger with the [Get object schema action](/en/connectors/salesforce/database-syncs#get-object-schema-action) to fetch schema information from a Salesforce object and replicate it to a data warehouse.

Refer to the [ETL/ELT](/en/features/etl-elt-guide#bulk-vs-batch) documentation for more information about bulk triggers and ELT/ETL processes.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the standard or custom object type to monitor. |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| SOQL WHERE clause | Enter a SOQL query to filter records by. For example: `StageName = 'Closed Lost' AND IsClosed = false`. Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information. |
| Schedule settings | Configure the trigger schedule. Refer to the [scheduler trigger](/en/features/scheduler) to configure this section. |
| When exporting records to form the CSV, fetch them in batches of | Enter the maximum number of records to process in each batch. Defaults to `10000`. |
| Include deleted records? | Select whether to include deleted records in the results. Defaults to `No`. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output fields | Description |
| --- | --- |
| All records successfully processed? | Whether all records were processed successfully. |
| Number of records processed | The number of records processed. |
| Number of records failed | The number of records that failed to process. |
| Number of retried records | The number of records Workato retried processing. |
| CSV content | Datapill that contains the output of the trigger. Take note to utilize it primarily alongside streaming compatible actions like S3 upload file streaming action. |
| Object name | Name of the object being retrieved. |
| Object schema | The schema of the object being retrieved, based on the fields the user has selected. Each field has with it the associated name, label, original datatype, and mapped datatype. This allows for easy processing with database uploads and any additional transformations required. |
| Created or updated from | The time and date the record was created or updated. |

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/change-data-capture-trigger.md
description: >-
  This trigger monitors Salesforce Change Data Capture events in real-time for
  changes to object fields you specify.
---

# Salesforce - Monitor changes in a record trigger (real-time)

This trigger monitors Salesforce [change data capture](/en/data-orchestration/change-data-capture) events in real-time for changes to object fields you specify. You can use this trigger to keep external systems in sync with Salesforce and perform specific actions based on the changed field and event type.

![Monitor changes in a record trigger](/assets/monitor-changes-trigger.EiXN-A8F.png)_Monitor changes in a record trigger_

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object type to monitor. Salesforce supports a subset of standard objects and all custom objects. Refer to the Salesforce [Associated objects change event](https://developer.salesforce.com/docs/atlas.en-us.240.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm) documentation for an exhaustive object list. |
| Monitor changes | Select the operations to monitor the object for. Defaults to `Update`. The operation type that triggers the job affects the fields Salesforce returns in the change event body: Update - Only changed fields, Create and Undelete - All non empty fields, Delete - No fields |
| Fields to retrieve | Select up to ten additional fields to include in the event notification for this specific object. |
| SOQL WHERE clause | Enter a SOQL query to filter records by. For example: `StageName = 'Closed Lost' AND IsClosed = false`. Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information. |
| Channel ID | Enter a custom channel ID to retrieve events when a recipe is temporarily down and restarting. You can use the [Salesforce tooling API](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_custom_channel_tooling_api.htm) to create a custom channel. |

## Output

| Field name | Description |
| --- | --- |
| Replay ID | A number indicating the sequence of event notifications. This number is not unique for notifications triggered by bulk edits. |
| Change event header | Commit number | The system change number (SCN) of a committed transaction, which increases sequentially. This field is provided for diagnostic purposes. The field value isn't guaranteed to be unique in Salesforce, but it is unique in a single database instance. The commit number might not be unique or sequential if your Salesforce organization migrates to another database instance. |
| Commit user | The ID of the user that ran the change operation. |
| Sequence number | The sequence of the change within a transaction. The sequence number starts at `1`. A lead conversion is an example of a transaction that can have multiple changes. A lead conversion results in a sequence of changes, all within the same transaction. Refer to the Salesforce [Change Events for Lead Conversion](https://developer.salesforce.com/docs/atlas.en-us.234.0.change_data_capture.meta/change_data_capture/cdc_standard_objects_lead_conversion.htm) guide for more information. |
| Entity name | The object API name generated for the change event. |
| Change type | The operation that caused the change. For example: CREATE, UPDATE, DELETE, UNDELETE |
| Changed fields | A list of the fields that were changed, including the LastModifiedDate system field. This field is empty for operations other than UPDATE, including record creation. |
| Change origin | Returns the Salesforce API and the API client ID that initiated the change, if set by the client. This field is only populated for changes made by API apps or from Lightning Experience. |
| Transaction key | A string that uniquely identifies each Salesforce transaction. You can use this key to identify and group all changes that were made in the same transaction. |
| Commit timestamp | The date and time when the change occurred, represented as the number of milliseconds since January 1, 1970 00:00:00 GMT. |
| Record ID | Contains a single record ID. Salesforce combines record change notifications into one merge event if multiple records with the same object type are changed in the same transaction within one second. Refer to the [Salesforce merged events](https://developer.salesforce.com/docs/atlas.en-us.238.0.change_data_capture.meta/change_data_capture/cdc_subscribe_merged_events.htm) documentation for more information. Salesforce sends one change event for all affected records. Workato then separates each of these into distinct event notifications. You may see multiple events with the same transaction key. This is done to improve usability and consistency, as the user can be certain that each trigger event pertains only to a single record. |
| Change event body _Note that fields selected in_ `Fields to Retrieve` _are returned alongside the fields mentioned for each specific operation._ | Create | The event message body includes non-empty fields and system fields for a new record, such as the `CreatedDate` and `OwnerId` fields. |
| Update | The body includes only the changed fields for an updated record. It includes empty fields only if they are updated to an empty value (null). It also includes the `LastModifiedDate` system field. The body includes the `LastModifiedById` field only if it has changed (if the user who modified the record is different than the user who saved it). |
| Delete | The body doesn’t include any fields or system fields for a deleted record. |
| Undelete | The body includes all non-empty fields from the original record and system fields for an undeleted record. |

## Permissions

You must have the following permissions enabled to ensure this trigger works as expected:

- Manage Flow
- Flow User
- Customize Application

| To receive change events for | Required permission |
| --- | --- |
| A specific standard or custom object | View All for the object |
| User | View All Users |
| Standard objects that don’t have the View All permission, such as Task and Event | View All Data |

Event notifications are linked to field-level security settings. Delivered events contain only the fields that a subscribed user is allowed to view. Fields that users can't access aren't included in the change event message.

Refer to the [Salesforce data capture](https://developer.salesforce.com/docs/atlas.en-us.234.0.change_data_capture.meta/change_data_capture/cdc_security_perms.htm) documentation for more information.

## Quotas

- Salesforce only allows monitoring up to five distinct objects. You must get an add on license if you plan to monitor more than five objects. Refer to [Allocations](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_allocations.htm) for more information. You can have up to 100 recipes that monitor the same object but only a maximum of five objects can be monitored across all recipes.
- The maximum event message size that Salesforce can publish is 1 MB. You can reach this quota if your entity has hundreds of custom fields or long text area fields.
- Maximum number of event notifications within a 24 hour period is 25,000 for Enterprise Edition and 50,000 for Performance and Unlimited Editions.

Refer to [Allocations](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_allocations.htm) for more information.

Salesforce change data capture notifications group event messages when identical edits are done in bulk for multiple records. Will we then get a single job for the single notification event?

We create separate jobs to prevent the user from having to handle the two separate cases with a single record and multiple records. Each job contains details for a single record. Job information contains the same Salesforce `replayId`.

---
