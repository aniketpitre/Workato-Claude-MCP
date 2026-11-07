---
url: 'https://docs.workato.com/en/connectors/databricks/new-row-trigger.md'
description: >-
  The New rows (batch) trigger in the Databricks connector picks up rows
  inserted in a selected table or view, processed as a batch each poll interval.
---

# Databricks - New rows (batch) trigger

This trigger picks up rows that are inserted in the selected table or view. These rows are processed as a batch of rows for each job. This trigger checks for new rows once every poll interval.

![New rows (batch) trigger](/assets/databricks-new-batch-rows.zH8uAgPv.png)_New rows (batch) trigger_

* * *

## Input

To use this trigger, configure the following input fields.

- Table name
  
- Select a table from which to process rows. Workato only displays the first 1,000 table names. Enter in the name if the table you plan to use is not displayed.
  
- Trigger poll interval
  
- _Optional_. How frequently to check for new events. If left blank, defaults to five (5) minutes. Minimum value: five (5) minutes. [Learn more about polling intervals](/en/recipes/polling-intervals).

---

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

---

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

---
