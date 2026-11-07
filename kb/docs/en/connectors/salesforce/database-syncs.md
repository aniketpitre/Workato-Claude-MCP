---
url: 'https://docs.workato.com/en/connectors/salesforce/database-syncs.md'
description: >-
  Learn how to sync Salesforce to databases and data warehouses using Workato,
  with the Get object schema action and detection of new or updated custom data.
---

# Sync Salesforce with databases/data warehouses

[Data pipelines](/en/data-orchestration/data-pipeline-recipe/create-data-pipeline-recipe) allow you to integrate Salesforce as a source for data warehouses.

Additionally, Workato provides a range of actions that can integrate Salesforce with databases through recipes.

The [Get object schema](/en/connectors/salesforce/actions/get-object-schema) action retrieves the schema of a standard or custom object in Salesforce. Use this action when you need to replicate a Salesforce object's fields in a data warehouse. The output provides the metadata of an sObject and a list of fields and their data types. The array contains only the fields that the connected user can view, as defined by the user's field-level security settings.

## Detect new or updated custom data

This boolean field is available in Salesforce triggers for all single-record and batch New, New/Updated record triggers as well as Scheduled record search using SOQL. Use this field only if trying to replicate object records to a database.

When 'Yes' is selected, the trigger output will include data of any newly added or modified custom fields. It is then used in conjunction with a replicate data action in the corresponding database. This is currently supported on the Snowflake adapter.

When new/updated data is detected from the data source, Workato first inspects the new object definition against the existing Snowflake table schema. Any mismatches will be reconciled by updating the table definition in Snowflake. Following that, the data is then deduplicated and inserted/updated in the Snowflake table.

Refer to this [recipe](https://www.workato.com/recipes/1169161?st=39eedb) for an example.

---
