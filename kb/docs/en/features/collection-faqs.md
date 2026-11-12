---
url: 'https://docs.workato.com/en/features/collection-faqs.md'
description: >-
  Answers to common questions about SQL Collection by Workato, including data
  transformation, large datasets, connection setup, and available actions.
---

# SQL Collection by Workato FAQs

Get answers to frequently asked questions (FAQs) about SQL Collection by Workato.

## What is SQL Collection by Workato and why should I use it?

View answer

[SQL Collection by Workato](/en/features/collection#collection-by-workato) is a native application that allows you to manipulate table data. You should use this app to synchronize related data across multiple systems, such as databases and web services. SQL Collection by Workato lets you run SQL statements with data from various sources and create temporary tables for data processing.

## How does SQL Collection handle data transformation?

View answer

SQL Collection handles [data transformation](/en/features/collection#transformation) seamlessly as it is built on SQL lite and functions like a database. You can create lists and query them using standard SQL syntax, including keywords like `WHERE`, `GROUP BY`, and `JOIN`. After you transform data, you can load it directly into your target system or export it as a CSV file.

## Does SQL Collection work with large datasets?

View answer

Yes. SQL Collection supports [large datasets](/en/features/collection#collection-works-with-large-datasets), but performance depends on the structure of your data, including row size and column count. We recommend that you use datasets that don't exceed **50,000 records** per SQL Collection list to ensure reliable performance.

SQL Collection can handle larger datasets, such as 100,000 to 200,000 records, if the rows are small and have fewer columns. Datasets that exceed the recommended quotas may impact performance or stability. Split tables into smaller chunks or use parallel recipes to process larger datasets efficiently.

## Is a connection setup required to use SQL Collection by Workato?

View answer

No. SQL Collection does not require a [connection setup](/en/features/collection#connection-setup). You can start using SQL Collection by selecting **App > SQL Collection by Workato** from the recipe editor.

## What are the available actions in SQL Collection by Workato?

View answer

SQL Collection offers several [actions](/en/features/collection#actions), including:

- Create list in SQL Collection action
- Insert rows in SQL Collection action
- Create list in SQL Collection from CSV
- Insert rows in SQL Collection from CSV file
- Query list in SQL Collection

## How does the Create list in SQL Collection action work?

View answer

This action [creates a SQL Collection list](/en/features/collection#create-list-in-sql-collection-action) in the recipe from a list input. The SQL Collection list contains column headers based on the list's schema. You can specify primary and secondary indexes for the list.

## What should I do if I encounter a COLLECTION DATE ERROR when using SQL Collection for dates?

View answer

You may receive an [invalid format error](/en/features/collection#create-list-in-sql-collection-action) for the Date field. To correct this error, you must use Mapper by Workato to update the date format or skip date fields if they are not required.

## Why does my WHERE clause return no rows for a boolean column in SQL Collection?

View answer

SQL Collection stores [`Boolean` field values](/en/features/collection#create-list-in-sql-collection-action) as the text values `t` (true) and `f` (false), not as native booleans. Comparing a boolean column to `true` or `false` matches no rows. Compare it to the string values instead: `WHERE is_active = 't'` or `WHERE is_active = 'f'`.

## How does the Query list in SQL Collection action work?

View answer

This action allows you to [perform standard SQL queries](/en/features/collection#query-list-in-sql-collection) on your lists. You can write your SQL query, define the schema, and choose whether to convert the results to a CSV string.

## What should I keep in mind when using SQL keywords in the Query list in SQL Collection action?

View answer

Some [SQL keywords](/en/features/collection#query-list-in-sql-collection), like `DELETE`, do not return list outputs. This means that datapills from these actions should not be used to export your list.

---
