---
url: >-
  https://docs.workato.com/en/connectors/databricks/new-row-custom-sql-trigger.md
description: >-
  The New rows using custom SQL (batch) trigger in the Databricks connector
  picks up rows matching your SQL query as a batch each poll interval.
---

# Databricks - New rows using custom SQL (batch) trigger

This trigger picks up rows when any rows matching the custom SQL you specify are inserted. These rows are processed as a batch of rows for each job. This trigger checks for new rows once every poll interval.

![New rows using custom SQL (batch) trigger](/assets/databricks-new-row-custom-sql.RrIxLieP.png)_New rows using custom SQL (batch) trigger_

* * *

## Input

To use this trigger, configure the following input fields.

- SQL
  
- Enter your custom SQL query. This query runs at each poll interval to pick up new rows. Databricks supports SQL ANSI-92 compliant SQL statements. \[Learn more\]. The SQL used here generates the output datatree. To do this, the SQL is executed once when you provide it.
  
- Unique key
  
- Select a unique key column to identify rows. Workato uses this to deduplicate existing rows.
  
- Output fields
  
- Define the columns returned in your query. You can use the output as datapills in downstream applications.
  
- Trigger poll interval
  
- _Optional_. How frequently to check for new events. If left blank, defaults to five minutes. Minimum value: five minutes. [Learn more about polling intervals](/en/recipes/polling-intervals).
