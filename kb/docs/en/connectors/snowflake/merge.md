---
url: 'https://docs.workato.com/en/connectors/snowflake/merge.md'
description: >-
  The Merge action in the Snowflake connector lets you insert or update rows in
  a target table by matching values against a source table.
---

# Snowflake - Merge action

This action merges data between two tables in Snowflake, allowing you to insert or update rows in a target table by matching values with a source table.

**Ensure that both tables have an identical schema**. This action only supports the following cases:

- Values that match (for updates).
- Values that do not match (for inserts).

## Input

| Input field | Description |
| --- | --- |
| Source table | Choose the source table or enter a custom table name. This table provides the data for the merge. |
| Target table | Choose the target table or enter a custom table name. This table receives the merged data. |
| Join expression | Define the merge condition. You can choose from the source and target table columns or enter it manually. |

## Output

| Output field | Description |
| --- | --- |
| Rows affected | The total number of rows affected by the merge operation. |
| Rows updated | The number of rows updated in the target table. |
| Rows inserted | The number of rows inserted into the target table. |

---
