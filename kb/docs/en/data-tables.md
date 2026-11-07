---
url: 'https://docs.workato.com/en/data-tables.md'
description: >-
  Workato data tables store data referenced by recipes in a scalable, secure,
  spreadsheet-like interface, and power data storage for workflow apps.
---

# Data tables

Data tables enable you to store data frequently used or referenced by recipes efficiently. Each data table has a [spreadsheet-like user interface](/en/data-tables/data-table-interface), which displays the stored data in columns (table structure) and rows (table data). Data tables are also used in Workato as the primary data store for your [workflow apps](/en/workflow-apps).

Workato provides a [connector](/en/data-tables/data-table-connector) to make using data tables more efficient. Workato also provides a way to [lookup records using formula mode](/en/formulas/other-formulas#data-table-lookup) to further boost the efficiency of using data tables in your recipes.

Data tables are designed to be scalable and secure out of the box without any additional maintenance. You can create and modify data in a data table with a few clicks.

> **REGULATORY COMPLIANCE**
> 
> Data tables aren't designed to store sensitive PCI data, including credit card numbers.

## Use cases

Typical data tables use cases include the following:

- Store data from chargeable APIs from third-party systems that are frequently referenced in recipes.
- Store data from slow or non-performant APIs from third-party systems that are frequently referenced in recipes.
- Store workflow apps data. This can be in a single table or multiple tables linked through [link to a table](/en/data-tables/user-interface/column-types) columns.

> **INCOMPATIBLE USE CASES**
> 
> Data tables aren't designed for the following use cases:
> 
> - **Relational database solution**: Given the various quotas enforced, data tables are not ideal as long-term large relational databases.
> - **Storing large data in a single cell**: The [long text](/en/data-tables/user-interface/column-types) column type can store only up to 10,000 characters, which is insufficient for large data storage.

## Key terms

The following list describes terminology useful for managing and interacting with your data tables:

- Record
  
- A set of values for each column in a data table. Each record is identifiable through a unique record ID and is represented by a single row entry in the **Data tables** interface.
  
- Column
  
- A column in a data table represents a specific record field. Each column has its own unique ID and is displayed as an individual column in the **Data tables** interface.
  
- Record ID
  
- Workato automatically generates a unique ID for each record in a data table. Workato requires the Record ID to perform certain Data table connector actions, including update record and delete record actions.
  
- Column ID
  
- Workato automatically generates a unique ID for each column in a data table. Workato typically references the Column ID in recipe actions to ensure resilience against column name changes.
  

## Back up your data tables

Workato recommends that you establish a regular backup strategy for your data tables by periodically exporting your data table records to [Workato FileStorage](/en/features/workato-filestorage). This approach helps you recover data in scenarios where records, columns, or entire tables are accidentally deleted or modified.

> **PERMANENT DELETION**
> 
> Deleting a data table is a permanent action and can't be undone. Workato can't recover deleted tables, rows, or columns.

---
