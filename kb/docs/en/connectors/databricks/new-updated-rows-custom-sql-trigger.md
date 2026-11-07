---
url: >-
  https://docs.workato.com/en/connectors/databricks/new-updated-rows-custom-sql-trigger.md
description: >-
  The New/updated rows via custom SQL (batch) trigger in the Databricks
  connector picks up new and updated rows matching your SQL query each poll
  interval.
---

# Databricks - New/updated rows via custom SQL (batch) trigger

This trigger picks up rows when any rows matching the custom SQL are inserted/updated. These rows are processed as a batch of rows for each job. This trigger checks for new rows once every poll interval.

![New/updated rows using custom SQL](/assets/databricks-new-updated-rows-custom-sql.msLF4qMh.png)_New/updated rows via custom SQL (batch) trigger_

* * *

## Input

To use this trigger, configure the following input fields.

- SQL
  
- Enter your custom SQL query. This query runs at each poll interval to pick up new/updated rows. Databricks supports SQL ANSI-92 compliant SQL statements.
  
  Use bind variables (for example,`id = :id`) and the parameter field to parameterize inputs.
  
  You must manually define the schema when you use bind variables.
  
- Unique key
  
- Select a unique key column to identify rows. Workato uses this to deduplicate existing rows.
  
- Sort column
  
- Select a column to identify updated rows. Along with the **Unique key**, this field enables Workato to identify which columns to use for deduplicating existing and updated rows.
  
- Output fields
  
- Define the columns returned in your query. You can use the output as datapills in downstream applications.
  
- Trigger poll interval
  
- _Optional_. How frequently to check for new events. If left blank, defaults to five minutes. Minimum value: five minutes. [Learn more about polling intervals](/en/recipes/polling-intervals).
