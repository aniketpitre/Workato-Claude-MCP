---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/search-records-soql-where.md
description: >-
  This action retrieves a CSV stream of Salesforce records that match the SOQL
  WHERE clause you provide.
---

# Salesforce - Search records using SOQL query WHERE clause action (batch)

This action retrieves a CSV stream of Salesforce records that match the SOQL WHERE clause you provide. Each job can retrieve up to 2,000 records. Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information about SOQL.

> **SELECT CLAUSE IN SOQL**
> 
> SOQL queries don't support the `SELECT *` operation often used in SQL queries. You must specify specific fields to retrieve in the SELECT clause.

## Input

| Input fields | Description |
| --- | --- |
| Search for | Select the type of Salesforce object to search for. |
| SOQL WHERE clause | Enter a SOQL query to filter records by. For example: `StageName = 'Closed Lost' AND IsClosed = false` |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| Limit | Enter the maximum number of records to return each job. The default value for this field is 150 and the maximum is 2,000. |
| Offset | Enter a number of rows to skip before returning query results. The maximum offset is 2,000 rows. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

The output of this action varies based on your selected **Search for** object and **Fields to retrieve**. Refer to Salesforce's [Overview of Salesforce Objects and Fields](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_concepts.htm) guide for more information on available objects and fields.
