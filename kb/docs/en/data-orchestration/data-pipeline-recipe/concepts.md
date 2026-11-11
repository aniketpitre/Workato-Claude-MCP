---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/concepts.md
description: >-
  Learn key Workato data pipeline concepts, including connectivity, sync types,
  incremental cursors, source filters, schema drift, delete tracking, merge
  strategies, and field-level data protection.
---

# Data pipeline key concepts

Workato data pipelines extract, replicate, and sync data to maintain accurate and up-to-date datasets. Pipelines connect source applications to destination data warehouses, move data in bulk, and preserve schema integrity. The following sections define key concepts that explain how data pipelines process and manage data.

## Source applications and destinations

Data pipelines extract data from a source application, such as Salesforce, and sync it to a destination, such as Snowflake. A single pipeline retrieves data from multiple objects or fields within the source application and replicates that data in the specified destination.

## Connectivity

Workato connects to cloud sources, such as Stripe, Slack, and QuickBooks Online, over HTTPS without an on-prem agent. Sources that run inside a private network, such as an on-premises database or an SAP system that isn't exposed to the internet, connect through a Workato [on-prem agent](/en/on-prem). Refer to your source application's configuration guide to confirm which connection method it supports.

## Object labels and API names

Sources such as Microsoft Dynamics 365, Microsoft Dynamics Business Central, and ServiceNow display both a human-readable label and an API or logical name for each object, for example `Account (account)` in Microsoft Dynamics 365. The label is the name you see in the source application, and the API or logical name is the identifier the source's API uses.

Rename behavior varies by source. For example, Workato continues to sync a Google Sheets tab after you rename it, but treats a renamed Airtable field as a different field the next time it discovers the table's schema. Refer to your source application's configuration guide to confirm which behavior applies.

## Object syncs

A sync refers to the overall process where the pipeline extracts data from the source and loads it into the destination. Each sync processes multiple objects in parallel and uses one of the following types:

- Full sync
  
- Extracts all available records from the source and loads them into the destination. This ensures the destination table contains a complete snapshot of the source data at the time of sync.
  
- Incremental sync
  
- Extracts records created or updated since the last successful sync, based on the object's [incremental cursor](#primary-keys-and-incremental-cursors). Deleted records sync only for objects that support [delete tracking](#delete-tracking).
  
- Re-sync
  
- A manual one-time sync for a specific object. Re-syncs extract and load the current data for that object immediately. This type is useful when only one object needs to be synced again due to errors, skipped syncs, or changes in data.
  

A data pipeline starts with a full historical sync. Objects that use incremental sync switch to incremental syncs after the initial sync completes. Objects that use full sync run a full sync on every scheduled run, either because you set the object's sync mode to **Full sync** or because the object doesn't support incremental sync. Re-syncs allow users to reprocess specific objects outside the normal schedule.

Sync mode options for each object vary by source. Sources such as Salesforce, Braintree, and Freshdesk let you choose the sync mode when you add an object to the pipeline, with a **Sync mode** drop-down set to **Full sync** or **Incremental**. These sources default an object to **Full sync** when the source doesn't provide a way to track changes for it, such as a timestamp. SAP Concur sets the sync mode automatically, based on whether its API exposes a usable modification-time filter for the object. Google Sheets supports only full sync.

Refer to the [Sync types and execution](/en/data-orchestration/sync-types) guide for more information.

## Primary keys and incremental cursors

Incremental sync for API and database sources typically relies on two properties of each object:

- **Incremental cursor**: A field the pipeline uses to find records created or updated since the last successful sync, typically a last-modified timestamp. Objects can also use a creation timestamp, such as PagerDuty's `created_at`, or a date range, such as the Gong `user_activity_stats` object.
- **Primary key**: A unique identifier, such as a record ID, that the destination uses to update existing rows so it doesn't insert duplicate rows.

An object can be limited to full sync when it lacks a usable cursor or primary key, such as the Chargebee `CouponCode` and `Gift` objects. Sources such as Braintree and Apollo.io also re-read a recent time window on each incremental run. For example, Braintree re-reads a trailing 3-day window to capture status changes that its creation-timestamp cursor doesn't reflect.

File-based sources track files instead of individual records. For example, SFTP and OneDrive process files created or modified after the last recorded modification time.

Refer to your source application's configuration guide for the sync modes each object supports.

## Historical start date

The **When first started, this pipeline should pick up records from** field sets the earliest date from which the pipeline extracts records during the historical sync. The pipeline extracts all available records if you leave this field blank. You can't change this value after you run the pipeline.

The effect of this date on full-sync objects varies by source. Sources such as Outreach and Sage Intacct apply it only to objects that support incremental sync, so full-sync objects always extract their complete record set. Apollo.io also uses it to limit full sync runs for objects such as `calls`. Refer to your source application's configuration guide for its behavior.

## Source filters

Sources such as Salesforce, Snowflake, and Slack let you narrow which records sync. You can enter a SOQL condition in the **SOQL WHERE clause** field of a [Salesforce](/en/data-orchestration/data-pipeline-recipe/configure-salesforce) object's settings, enter a SQL condition in the **WHERE clause** field when you configure [Snowflake as a data pipeline source](/en/data-orchestration/data-pipeline-recipe/configure-snowflake-source), or limit a [Slack](/en/data-orchestration/data-pipeline-recipe/configure-slack) pipeline to a specific list of channels.

Source filters aren't available for every source or object. Refer to your source application's configuration guide to confirm whether it supports them.

## Sync frequency

Data pipelines run on a scheduled cadence to keep source and destination systems in sync. The default frequency is 15 minutes. A 5-minute interval is available upon request and can be enabled on a per-customer basis.

You can schedule syncs on a time-based interval or with a cron expression. Schedule options vary by source. Each scheduled run syncs every selected object, with incremental sync for objects that use it. Choose a schedule that aligns with your operational requirements and system capacity.

The pipeline skips the next scheduled sync if the current sync runs longer than expected and overlaps with it.

## Pipeline runs

Each data pipeline sync consists of multiple runs, with one run per selected object. A sync represents the entire activity for all objects, while a run tracks the execution for a single object within that sync.

The pipeline executes runs in parallel to improve performance. Each run extracts data from the source and loads it into the destination. Run-level data appears in the **Runs** tab, which helps you monitor pipeline execution. Refer to the [Object runs](/en/data-orchestration/data-pipeline-recipe/monitor#object-runs) section for more information.

## Concurrency limit

Use the optional **Concurrency limit** field during pipeline setup to cap the number of concurrent operations the pipeline runs against a source. This helps when the source can handle only a limited number of concurrent requests, for example an SFTP server that accepts only one active session at a time. The pipeline uses the default quota set by Workato if you leave this field blank.

## Schema replication and schema drift management

Schema drift refers to inconsistencies between the source and destination that occur when changes appear in the source data. These changes may include added or deleted fields, modified field types, or other structural updates. Unmanaged schema drift can cause transformation errors, data loss, and inaccurate analysis.

Workato pipelines detect schema drift during syncs and apply schema changes based on your pipeline configuration. Use the **Auto-sync new fields** option to sync new source fields automatically, or use **Block new fields** to keep the schema fixed and add new fields manually. You can configure this behavior during [pipeline setup](/en/data-orchestration/data-pipeline-recipe/configure-pipeline-sources).

The pipeline doesn't backfill historical values for a new field during incremental syncs. It captures values only from the time it detects the field.

The following schema changes require manual updates in the destination:

- **Deleted fields**: The pipeline keeps a field's column in the destination for historical reference when the field is deleted in the source. Manually delete the column from the destination table to remove the field and its data. Refer to [Deleted fields in the source](/en/data-orchestration/data-pipeline-recipe/troubleshoot#deleted-fields-in-the-source).
- **Data type changes in Salesforce**: Pipelines don't update the destination schema when a field's data type changes in Salesforce, so you must update the destination schema manually. Refer to [Schema handling](/en/data-orchestration/data-pipeline-recipe/troubleshoot#schema-handling).

## Delete tracking

Delete tracking marks records that no longer exist in the source so your destination reflects deletions instead of only insertions and updates. Workato typically sets a synthetic `_workato_is_deleted` column to `true` for deleted records in the destination table.

Workato uses one of the following methods to detect deletions, based on the source:

- **Native deletion signal**: The source exposes a flag that indicates a record was deleted, such as the `deleted` flag on Chargebee records.
- **Destination-inferred**: The source doesn't expose a deletion signal. Workato compares each full sync against the previous run and marks records that no longer appear.
- **Change tracking**: The source provides a change-tracking mechanism that Workato reads to detect deletions, such as SQL Server Change Tracking or the ServiceNow `sys_audit_delete` table.

Objects with a primary key keep their deleted records in the destination table. A full sync merges records into the existing table on the primary key, so its row count doesn't drop when records are deleted in the source. Exclude rows where `_workato_is_deleted` is `true` to query only records that exist in the source. Refer to [How a full sync works](/en/data-orchestration/sync-types#how-a-full-sync-works).

Delete tracking isn't available for every source or object. For example, SFTP doesn't support delete tracking. Refer to your source application's configuration guide for the delete tracking behavior it supports.

## Destination schema and table organization

Snowflake, Databricks, and PostgreSQL destinations let you choose the schema where the pipeline creates its tables. BigQuery uses a dataset, and S3 Iceberg uses a namespace. Snowflake and PostgreSQL also let you set a schema for the pipeline that overrides the schema on your connection. PostgreSQL supports only existing schemas.

Snowflake also lets you set a **Table prefix**, which adds a value to the beginning of every table name. A table prefix helps prevent table name conflicts when multiple pipelines write to the same schema. You can't change the **Schema** or **Table prefix** in Snowflake after the pipeline runs for the first time.

Ensure the destination schema, BigQuery dataset, or S3 Iceberg warehouse and catalog are newly created and empty before you start a pipeline. This prevents errors during the initial sync and allows the pipeline to create destination tables without conflicts. Refer to your destination's configuration guide for the options it supports.

## Destination tables and merge strategies

Pipelines create destination tables based on the source schema. For Snowflake, Databricks, BigQuery, PostgreSQL, and SQL Server destinations, the pipeline also creates a stage and temporary tables to support data replication and update operations, so the destination connection needs permission to create them.

File-based sources, such as Amazon S3 and SFTP, let you choose how rows merge into the destination table in the **Choose a merge strategy** field:

- **Upsert**: Inserts new rows and updates existing rows. Use the **Merge method** field to select one or more columns to use as the primary key. The pipeline uses the system-generated `_file` and `_line` columns as a composite primary key if you leave the field blank.
- **Append only**: Inserts all rows and doesn't match or update existing records.

## Synthetic columns

Workato adds synthetic columns to destination tables to mark deleted records, trace pipeline runs, and identify source files. The columns depend on the source and include:

| Column | Purpose |
| --- | --- |
| `_workato_is_deleted` | Set to `true` for records Workato detects as deleted. Refer to [Delete tracking](#delete-tracking). |
| `_workato_run_id` | Identifies the pipeline run that wrote the row. |
| `_workato_synced_at` | Records when Workato last synced the row. |
| `_file` and `_line` | Identify the source file and the row number within that file, for file-based sources. |

Refer to your source application's configuration guide for the synthetic columns it adds.

## Field-level data protection

Field-level data protection helps protect sensitive information during sync. You can choose one of the following options for each field:

- **Replicate as is**: Data values at the source replicate identically to the destination.
- **Hash**: Hashes sensitive data values in the field before Workato syncs them to your destination. This option replicates the data structure and protects the content.

Workato completes the following steps to hash each value in transit, before it loads the value into your destination:

- Appends your destination's unique salt to the field value, and treats a `NULL` value as an empty string.
- Encodes the result as UTF-8 and hashes it with the SHA-256 algorithm.
- Writes the hash to the destination as a Base64-encoded string.

The same value always produces the same hash within a destination, so you can join hashed columns across tables in that destination. The same value produces a different hash in each destination, because each destination has its own salt. You can't recover the original values from the hashed values, even with the salt.

Workato clears the existing values in a field's destination column when you switch the field between **Replicate as is** and **Hash** after the pipeline syncs it. Workato also replaces the column with a column whose data type fits the hashed values when you switch a field to **Hash**. Values load in the selected format from the next sync. Workato continues to hash a field's values if the source later changes the field's data type.

Workato recommends that you hash personally identifiable information (PII) and other sensitive fields. You can configure field-level data protection for each field when you add an object during [pipeline setup](/en/data-orchestration/data-pipeline-recipe/configure-pipeline-sources). Workato records field-level data protection changes in the audit logs.
