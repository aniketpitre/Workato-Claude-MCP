---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/search-records-soql-batch.md
description: >-
  This action retrieves a list of Salesforce records that match the SOQL query
  you provide.
---

# Salesforce - Search records using SOQL query (batch)

This action retrieves a list of Salesforce records that match the SOQL query you provide. Each job can retrieve up to 2,000 records. The maximum length of the SOQL query is 16,000 characters. Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information about SOQL.

> **SELECT CLAUSE IN SOQL**
> 
> SOQL queries don't support the `SELECT *` operation often used in SQL queries. You must specify specific fields to retrieve in the SELECT clause.

## Input

| Input fields | Description |
| --- | --- |
| SOQL query | Provide a valid SOQL query excluding the LIMIT param. Enclose clauses with parentheses for logical operators. Returned records include deleted records by default. You can use `IsDeleted = false` to exclude them. |
| Output schema | Click **Use SOQL** to describe all fields in your response using SOQL, or click **add fields manually** to fill out the **Add new field** modal and configure the **Name**, **Hint**, **Label**, **Data type**, whether the parameter is **Optional**, and where the parameter should **Nest under**. |
| Limit | Enter the maximum number of records to return each job. The default value for this field is 150 and the maximum is 2,000. Workato omits the limit clause when aggregate functions are used. |
| Offset | Enter a number of rows to skip before returning query results. The maximum offset is 2,000 rows. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

| Output fields | Description |
| --- | --- |
| Done | Indicates whether this response contains the end of the retrieved record list. |
| Total size | The total number of matching records retrieved. |
| Records | An object containing records that match the provided SOQL query. `List index` is the position of the current record in the list. `List size` is the total number of records retrieved. |
